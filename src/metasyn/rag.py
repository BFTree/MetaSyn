"""One-pass RAG generation and explicit included-article extraction."""

from __future__ import annotations

import os
import re
import unicodedata
from typing import Any

from openai import OpenAI


def _value(row: dict[str, Any], key: str) -> str:
    value = row.get(key)
    return "Not reported" if value in (None, "", "NR") else str(value).strip()


def build_prompt(review: dict, candidates: list[dict]) -> str:
    """Build the fixed-pool prompt used in the final experiments."""
    blocks = []
    for candidate in candidates:
        blocks.append(
            "\n".join(
                [
                    f"[Candidate {int(candidate['rank']):03d}]",
                    f"Corpus ID: {int(candidate['corpus_id'])}",
                    f"Title: {candidate.get('title') or 'Not reported'}",
                    f"Publication year: {candidate.get('year') or 'Not reported'}",
                    f"Abstract: {candidate.get('abstract') or 'Not reported'}",
                ]
            )
        )
    candidate_text = "\n\n---\n\n".join(blocks)
    return f"""You are conducting a systematic review and evidence synthesis. Use only the fixed ranked candidate pool supplied below; do not search for or invent any other article.

Review target
Research question: {_value(review, 'Research_Question')}
Population: {_value(review, 'Population')}
Intervention: {_value(review, 'Intervention')}
Exposure: {_value(review, 'Exposure')}
Comparison: {_value(review, 'Comparison')}
Outcome: {_value(review, 'Outcome')}
Search start date: {_value(review, 'search_start_date')}
Search end date: {_value(review, 'search_end_date')}

Inclusion criteria
{_value(review, 'inclusion_criteria')}

Exclusion criteria
{_value(review, 'exclusion_criteria')}

Screen the titles and abstracts against the complete criteria, then write a useful evidence-synthesis report. Clearly identify the final included primary-study articles in a dedicated list near the end. The heading wording is up to you. For every included article, reproduce both its exact candidate title and its exact `Corpus ID: <number>`. If no candidate is eligible, explicitly say that none were included. Do not treat the source systematic review, other reviews, protocols, editorials, conference abstracts, or out-of-date articles as eligible when the criteria exclude them. Do not claim access to information beyond the supplied title and abstract.

Fixed source-review-disjoint top-{len(candidates)} candidate pool (the primary ranking; no coarse publication-year filter)

{candidate_text}
"""


def create_client(
    api_key: str | None = None, base_url: str | None = None
) -> OpenAI:
    key = api_key or os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required")
    url = base_url or os.environ.get("OPENAI_BASE_URL")
    return OpenAI(api_key=key, base_url=url) if url else OpenAI(api_key=key)


def generate_report(
    prompt: str,
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
) -> tuple[str, dict]:
    model_name = model or os.environ.get("OPENAI_MODEL")
    if not model_name:
        raise RuntimeError("OPENAI_MODEL is required")
    client = create_client(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
    )
    report = response.choices[0].message.content or ""
    usage = getattr(response, "usage", None)
    return report.strip(), {
        "model": model_name,
        "input_tokens": int(getattr(usage, "prompt_tokens", 0) or 0),
        "output_tokens": int(getattr(usage, "completion_tokens", 0) or 0),
        "total_tokens": int(getattr(usage, "total_tokens", 0) or 0),
    }


def _clean_heading(line: str) -> str:
    cleaned = line.strip()
    cleaned = re.sub(r"^\s{0,3}#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"^\s*>\s*", "", cleaned)
    cleaned = cleaned.strip(" *_`:#\t")
    return re.sub(r"\s+", " ", cleaned).casefold()


def _included_heading_score(line: str) -> int:
    heading = _clean_heading(line)
    if not heading or len(heading) > 120 or heading.endswith("."):
        return 0
    if "inclusion criter" in heading or "eligibility criter" in heading:
        return 0
    subjects = r"(?:stud(?:y|ies)|articles?|reports?|publications?|evidence|literature)"
    if re.search(
        rf"\bfinal\b.*\b(?:included|eligible|selected|retained)\b.*\b{subjects}\b",
        heading,
    ):
        return 10
    if re.search(
        rf"\b(?:included|eligible|selected|retained)\b.*\b{subjects}\b", heading
    ):
        return 7
    if re.search(
        rf"\b{subjects}\b.*\b(?:included|eligible|selected|retained)\b", heading
    ):
        return 6
    if heading in {"final selection", "included evidence", "eligible evidence"}:
        return 5
    return 0


def _looks_like_next_heading(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    decision = stripped.strip(" *_`:#\t").rstrip(".").strip()
    if re.fullmatch(
        r"(?i)(?:none|zero|0)(?:\s+(?:was\s+|were\s+)?"
        r"(?:included|eligible|selected|retained))?",
        decision,
    ):
        return False
    if re.match(r"^\s{0,3}#{1,6}\s+\S", line):
        return True
    heading = _clean_heading(line)
    if len(heading) > 100 or heading.endswith("."):
        return False
    return bool(
        re.fullmatch(
            r"(?:executive )?(?:summary|background|methods?|results?|discussion|"
            r"limitations?|conclusions?|references?|sources?|appendix|excluded "
            r"(?:studies|articles)|study characteristics|evidence synthesis|"
            r"certainty of evidence|risk of bias)(?: and [a-z ]+)?",
            heading,
        )
    )


def find_included_section(report: str) -> tuple[str | None, str | None]:
    lines = report.splitlines(keepends=True)
    choices = []
    for index, line in enumerate(lines):
        score = _included_heading_score(line)
        if score:
            choices.append((score, index))
    if not choices:
        return None, None
    _, start = max(choices, key=lambda item: (item[0], item[1]))
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if _looks_like_next_heading(lines[index]):
            end = index
            break
    return "".join(lines[start + 1 : end]).strip(), lines[start].strip()


def _normalize_title(text: str) -> str:
    normalized = unicodedata.normalize("NFKC", text).casefold()
    normalized = re.sub(r"[\W_]+", " ", normalized, flags=re.UNICODE)
    return re.sub(r"\s+", " ", normalized).strip()


def _rank_order(ids: set[int], candidates: list[dict]) -> list[int]:
    return [
        int(item["corpus_id"])
        for item in candidates
        if int(item["corpus_id"]) in ids
    ]


def raw_explicit_ids_in_text(text: str) -> set[int]:
    found: set[int] = set()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if "|" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        normalized = [_normalize_title(cell) for cell in cells]
        if "corpus id" not in normalized:
            continue
        id_column = normalized.index("corpus id")
        for row in lines[index + 1 :]:
            if "|" not in row:
                break
            row_cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
            if id_column >= len(row_cells):
                continue
            if re.fullmatch(r":?-{3,}:?", row_cells[id_column]):
                continue
            match = re.fullmatch(
                r"(?:Corpus ID\s*:\s*)?(\d+)", row_cells[id_column], re.I
            )
            if match:
                found.add(int(match.group(1)))
    for match in re.finditer(
        r"(?im)\b(?:corpus|article|study)[\s_-]*ids?\b[\s*_`]*"
        r"(?:is|are|[:=#-])?[\s*_`]*"
        r"([0-9][0-9,;\s\[\]`()/-]*)",
        text,
    ):
        found.update(int(raw) for raw in re.findall(r"\d+", match.group(1)))
    found.update(
        int(raw) for raw in re.findall(r"(?i)metasyn://corpus/(\d+)", text)
    )
    for match in re.finditer(
        r"(?m)^\s*(?:[-*+]\s*|\d{1,3}[.)]\s*)?(?:[\[`(]\s*)?(\d+)"
        r"(?:\s*[\]`)])?\s*(?:[|:\-]|\u2013|\u2014)",
        text,
    ):
        found.add(int(match.group(1)))
    return found


def title_ids_in_text(text: str, candidates: list[dict]) -> set[int]:
    haystack = f" {_normalize_title(text)} "
    found: set[int] = set()
    for candidate in candidates:
        title = _normalize_title(str(candidate.get("title") or ""))
        if len(title) >= 16 and len(title.split()) >= 3 and f" {title} " in haystack:
            found.add(int(candidate["corpus_id"]))
    return found


def title_ids_on_lines_without_explicit_ids(
    text: str, candidates: list[dict]
) -> set[int]:
    """Match title-only list entries without repairing an unknown stated ID."""
    title_only_lines = [
        line for line in text.splitlines() if not raw_explicit_ids_in_text(line)
    ]
    return title_ids_in_text("\n".join(title_only_lines), candidates)


def unmatched_title_entries_in_list(text: str, candidates: list[dict]) -> list[str]:
    """Return title-only list entries that cannot be mapped to a candidate."""
    entries: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^\s*(?:[-*+]\s+|\d{1,3}[.)]\s+)(.+?)\s*$", line)
        if not match:
            continue
        entry = match.group(1).strip().strip("*_`").strip()
        entry = re.sub(r"(?i)^title\s*:\s*", "", entry).strip()
        if (
            not entry
            or _explicit_empty(entry)
            or raw_explicit_ids_in_text(entry)
            or title_ids_in_text(entry, candidates)
        ):
            continue
        key = _normalize_title(entry)
        if len(key) < 8 or key in seen:
            continue
        seen.add(key)
        entries.append(entry)
    return entries


def _explicit_empty(text: str) -> bool:
    normalized = _normalize_title(text)
    return bool(
        re.search(
            r"^(?:none|zero|0)\b|"
            r"\b(?:included|eligible|selected|retained|qualified)(?: primary)? "
            r"(?:studies|study|articles|article|reports|report) (?:none|zero|0)\b|"
            r"\b(?:none|zero) (?:of the candidates? )?(?:was |were )?"
            r"(?:included|eligible|selected|retained|qualified)\b|"
            r"\bno (?:candidate |primary )*(?:studies|study|articles|article|reports|report) "
            r"(?:was |were )?(?:included|eligible|selected|retained|qualified|met)\b|"
            r"\bno (?:eligible|included|selected|retained|qualified) "
            r"(?:studies|study|articles|article|reports|report)\b|"
            r"\bno candidates?(?: from [^.]{0,120})? "
            r"(?:met|satisfied) (?:all )?(?:the )?"
            r"(?:inclusion|eligibility) criteria\b|"
            r"\b(?:final )?(?:set|list) of included (?:primary )?"
            r"(?:studies|study|articles|article|reports|report) (?:is|was) empty\b|"
            r"\b(?:included|eligible|selected|retained) (?:primary )?"
            r"(?:studies|study|articles|article|reports|report) (?:none|zero|0)\b",
            normalized,
        )
    )


def _matching_lines(text: str, ids: set[int], candidates: list[dict]) -> str:
    if not ids:
        return ""
    id_patterns = [re.compile(rf"(?<!\d){corpus_id}(?!\d)") for corpus_id in ids]
    titles = {
        int(item["corpus_id"]): _normalize_title(str(item.get("title") or ""))
        for item in candidates
        if int(item["corpus_id"]) in ids
    }
    selected = []
    for line in text.splitlines():
        normalized_line = f" {_normalize_title(line)} "
        if any(pattern.search(line) for pattern in id_patterns) or any(
            title and f" {title} " in normalized_line for title in titles.values()
        ):
            selected.append(line.rstrip())
    return "\n".join(selected).strip()


def extract_included_articles(report: str, candidates: list[dict]) -> dict:
    """Apply the exact final-experiment included-article parser."""
    candidate_ids = {int(item["corpus_id"]) for item in candidates}
    report_raw_explicit = raw_explicit_ids_in_text(report)
    report_explicit = report_raw_explicit & candidate_ids
    report_titles = title_ids_in_text(report, candidates)
    visible = report_explicit | report_titles
    unmatched_visible = report_raw_explicit - candidate_ids
    section, heading = find_included_section(report)
    unmatched: set[int] = set()
    unmatched_entries: list[str] = []

    if section is not None:
        section_raw_explicit = raw_explicit_ids_in_text(section)
        section_explicit = section_raw_explicit & candidate_ids
        section_titles = title_ids_in_text(section, candidates)
        section_unmatched_entries = unmatched_title_entries_in_list(
            section, candidates
        )
        if section_raw_explicit:
            selected = section_explicit | title_ids_on_lines_without_explicit_ids(
                section, candidates
            )
            unmatched = section_raw_explicit - candidate_ids
            unmatched_entries = section_unmatched_entries
            method = "included_section_ids_and_titles"
            empty_reason = None
            list_text = section
            explicit = section_explicit
        elif section_titles:
            selected = section_titles
            unmatched_entries = section_unmatched_entries
            method = "included_section_titles"
            empty_reason = None
            list_text = section
            explicit = set()
        elif section_unmatched_entries:
            selected = set()
            unmatched_entries = section_unmatched_entries
            method = "included_section_unmapped_entries"
            empty_reason = None
            list_text = section
            explicit = set()
        elif (
            _explicit_empty(section)
            or _explicit_empty(heading or "")
            or (not section.strip() and _explicit_empty(report))
        ):
            selected = set()
            unmatched = set()
            method = "included_section_explicit_empty"
            empty_reason = "model_explicitly_reported_no_included_articles"
            list_text = section
            explicit = set()
        else:
            selected = (
                report_explicit
                | title_ids_on_lines_without_explicit_ids(report, candidates)
                if report_raw_explicit
                else visible
            )
            unmatched = unmatched_visible if report_raw_explicit else set()
            explicit = report_explicit
            method = "whole_report_fallback" if selected or unmatched else "unresolved_empty"
            empty_reason = (
                None
                if selected or unmatched
                else "no_candidate_id_or_exact_title_was_extracted"
            )
            list_text = _matching_lines(report, selected, candidates)
    else:
        selected = visible
        unmatched = unmatched_visible
        explicit = report_explicit
        if selected or unmatched:
            method = "whole_report_fallback"
            empty_reason = None
            list_text = _matching_lines(report, selected, candidates)
        elif _explicit_empty(report):
            method = "whole_report_explicit_empty"
            empty_reason = "model_explicitly_reported_no_included_articles"
            list_text = _matching_lines(report, selected, candidates) or report.strip()
        else:
            method = "unresolved_empty"
            empty_reason = "no_candidate_id_or_exact_title_was_extracted"
            list_text = ""

    included_ids = _rank_order(selected, candidates)
    candidates_by_id = {int(item["corpus_id"]): item for item in candidates}
    included_articles = [
        {
            "corpus_id": corpus_id,
            "title": str(candidates_by_id[corpus_id].get("title") or "Not reported"),
        }
        for corpus_id in included_ids
    ]
    return {
        "included_article_ids": included_ids,
        "included_articles": included_articles,
        "list_text": list_text,
        "extraction_method": method,
        "explicit_included_article_ids": _rank_order(explicit, candidates),
        "unmatched_included_article_ids": sorted(unmatched),
        "unmatched_included_entries": unmatched_entries,
        "visible_article_ids": _rank_order(visible, candidates),
        "included_section_heading": heading,
        "selection_empty": not included_ids and not unmatched and not unmatched_entries,
        "selection_empty_reason": empty_reason,
        "selection_resolved": bool(included_ids)
        or bool(unmatched)
        or bool(unmatched_entries)
        or empty_reason == "model_explicitly_reported_no_included_articles",
    }
