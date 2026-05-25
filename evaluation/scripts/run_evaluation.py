#!/usr/bin/env python
"""
Run Evaluation - Evaluate all reports in a directory.

Usage:
    python evaluation/scripts/run_evaluation.py \\
        --corpus data/corpus.json \\
        --papers data/papers.json \\
        --test-ids data/test_ids.json \\
        --results-dir path/to/system_outputs \\
        --output-dir evaluation/results

LLM configuration is read from environment variables:
    - OPENAI_API_KEY: API key
    - OPENAI_BASE_URL: API base URL (default: https://api.openai.com/v1)
    - OPENAI_MODEL: Model name (default: gpt-4o-mini)
"""

import argparse
import json
import re
import statistics
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'framework'))

from evaluator import ReportEvaluator


def load_json(path: str) -> any:
    """Load JSON file."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def scan_results_directory(base_dir: str) -> List[Dict]:
    """
    Scan directory for results.json + report.md pairs.

    Returns:
        List of {results_json, report_md, model, retrieval_mode, paper_id}
    """
    base_path = Path(base_dir)
    pairs = []

    for results_file in base_path.rglob('results.json'):
        report_file = results_file.parent / 'report.md'
        if not report_file.exists():
            continue

        parts = results_file.relative_to(base_path).parts
        if len(parts) >= 4:
            model = parts[0]
            retrieval_mode = parts[1]
            paper_match = re.search(r'paper_(\d+)', parts[2])
            if paper_match:
                paper_id = int(paper_match.group(1))
                pairs.append({
                    'results_json': str(results_file),
                    'report_md': str(report_file),
                    'model': model,
                    'retrieval_mode': retrieval_mode,
                    'paper_id': paper_id
                })

    return pairs


def aggregate_results(results: List[Dict]) -> Dict:
    """
    Aggregate results by model_retrieval_mode.

    For each metric, compute mean, std, and count of valid (non-None) values.
    """
    from collections import defaultdict

    groups = defaultdict(list)
    for r in results:
        key = f"{r['model']}_{r['retrieval_mode']}"
        groups[key].append(r)

    aggregated = {}
    for group_key, group_results in groups.items():
        # Collect all metric names
        metric_names = set()
        for r in group_results:
            metric_names.update(k for k in r['metrics'].keys() if not k.endswith('_skipped'))

        group_result = {'num_papers': len(group_results)}

        for metric_name in metric_names:
            values = [
                r['metrics'].get(metric_name)
                for r in group_results
                if r['metrics'].get(metric_name) is not None
            ]

            if values:
                group_result[f"{metric_name}"] = round(statistics.mean(values), 4)
                group_result[f"{metric_name}_std"] = round(statistics.stdev(values), 4) if len(values) > 1 else 0
                group_result[f"{metric_name}_count"] = len(values)
            else:
                group_result[metric_name] = None
                group_result[f"{metric_name}_std"] = None
                group_result[f"{metric_name}_count"] = 0

        aggregated[group_key] = group_result

    return aggregated


def main():
    parser = argparse.ArgumentParser(description='Evaluate meta-analysis reports')
    parser.add_argument('--corpus', required=True, help='Path to corpus.json')
    parser.add_argument('--papers', required=True, help='Path to papers.json')
    parser.add_argument('--test-ids', required=True, help='Path to test_ids.json')
    parser.add_argument('--results-dir', required=True, help='Directory with results')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    parser.add_argument('--model', default=None, help='LLM model name (optional, overrides OPENAI_MODEL env)')

    args = parser.parse_args()

    # Load data
    print("Loading data...")
    papers = load_json(args.papers)
    test_ids = set(load_json(args.test_ids))
    papers_by_id = {p["ID"]: p for p in papers}

    # Scan for results
    print(f"Scanning {args.results_dir}...")
    pairs = scan_results_directory(args.results_dir)
    print(f"Found {len(pairs)} result pairs")

    # Group by model_retrieval_mode
    from collections import defaultdict
    groups = defaultdict(list)
    for pair in pairs:
        if pair['paper_id'] not in test_ids:
            continue
        key = f"{pair['model']}_{pair['retrieval_mode']}"
        groups[key].append(pair)

    # Initialize evaluator (LLM config from environment variables)
    evaluator = ReportEvaluator(
        corpus_path=args.corpus,
        papers_path=args.papers,
        model=args.model  # Optional override
    )

    # Evaluate each group
    all_results = []
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for group_key, group_pairs in groups.items():
        print(f"\n{'='*60}")
        print(f"Evaluating {group_key} ({len(group_pairs)} papers)")
        print(f"{'='*60}")

        group_results = []

        for i, pair in enumerate(group_pairs):
            if pair['paper_id'] not in papers_by_id:
                print(f"  [{i+1}/{len(group_pairs)}] Skipping paper {pair['paper_id']} (no GT)")
                continue

            print(f"  [{i+1}/{len(group_pairs)}] Evaluating paper_{pair['paper_id']}")

            try:
                # Read files
                with open(pair['report_md'], 'r', encoding='utf-8') as f:
                    report_text = f.read()
                with open(pair['results_json'], 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Get IDs
                included_ids = data.get("included_paper_ids", [])
                retrieved_ids = [
                    p.get("corpus_id")
                    for p in data.get("retrieved_papers", [])
                    if "corpus_id" in p
                ]

                # Evaluate
                eval_result = evaluator.evaluate(
                    report_text=report_text,
                    included_ids=included_ids,
                    retrieved_ids=retrieved_ids,
                    ground_truth_paper_id=pair['paper_id']
                )

                if 'error' in eval_result:
                    print(f"    Error: {eval_result['error']}")
                    continue

                group_results.append({
                    'paper_id': pair['paper_id'],
                    'metrics': eval_result['metrics'],
                    'extracted_data': eval_result['extracted_data']
                })

            except Exception as e:
                print(f"    Error: {e}")

        # Aggregate group results
        if group_results:
            aggregated = aggregate_results(group_results)
            aggregated['num_papers'] = len(group_results)

            # Add per-paper results
            output_data = {
                'model': group_pairs[0]['model'] if group_pairs else '',
                'retrieval_mode': group_pairs[0]['retrieval_mode'] if group_pairs else '',
                'evaluated_at': datetime.now().isoformat(),
                'per_paper_results': group_results,
                'aggregated': aggregated
            }

            # Save
            output_path = output_dir / f"{group_key}.json"
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)

            print(f"  Saved to {output_path}")

            # Print summary
            print(f"\n  Summary ({group_key}):")
            for key, val in sorted(aggregated.items()):
                if key in ['num_papers'] or (key.endswith('_count') and val is not None):
                    continue
                if key.endswith('_std'):
                    continue
                if key.endswith('_count'):
                    continue
                std_key = f"{key}_std"
                count_key = f"{key}_count"
                std_val = aggregated.get(std_key, 'N/A')
                count_val = aggregated.get(count_key, 'N/A')
                print(f"    {key}: {val} (std={std_val}, n={count_val})")

        all_results.extend(group_results)

    print(f"\n{'='*60}")
    print(f"Total evaluated: {len(all_results)} reports")
    print(f"Output directory: {output_dir}")


if __name__ == '__main__':
    main()
