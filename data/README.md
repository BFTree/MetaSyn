# MetaSyn Dataset

## Download

```
https://huggingface.co/datasets/BFTree/MetaSyn
```

Place the three files in this directory:

```
data/
├── papers.json      # 442 meta-analysis records with full annotations
├── corpus.json      # 140,585 PubMed articles (the retrieval corpus)
└── test_ids.json    # list of 88 test-split paper IDs
```

---

## How the Dataset Was Built

Constructing MetaSyn required solving several non-trivial problems:

**1. Source selection.**  
We collected 442 meta-analyses published in the *Nature* Portfolio (2015–2024). Nature Portfolio journals enforce strict methodological standards — every included meta-analysis must report explicit search strategies, PICO criteria, and study-level statistics. This makes the ground truth auditable and consistent, unlike datasets scraped from heterogeneous venues.

**2. Corpus construction.**  
For each meta-analysis, we retrieved its reference list and used PubMed to expand a topic-matched candidate pool. The final corpus of 140,585 articles was assembled so that the retrieval ceiling (fraction of ground-truth included studies that appear in the corpus at K=200) is 90.9% across the test split — high enough to make the benchmark meaningful, without leaking the answer trivially.

**3. PICO/ECO annotation.**  
Each entry was annotated with Population, Intervention, Comparator, and Outcome (PICO) fields extracted from the paper and verified by expert annotators. Entries using exposure-based designs (ECO) were also included. These fields serve as the input to any system being evaluated.

**4. Hard-negative construction.**  
A key difficulty is that most retrieval benchmarks use random negatives, which are easy to reject. MetaSyn's negatives are *topic-matched*: articles that share population and setting with a meta-analysis but fail at least one explicit eligibility criterion (e.g., wrong study design, out-of-scope population, or wrong comparator). These distractors require genuine criterion-level reasoning to exclude.

**5. Effect-size and heterogeneity fields.**  
Beyond inclusion lists, each entry records the pooled effect size, confidence interval, I² heterogeneity, and conclusion direction extracted from the paper. These enable evaluation of synthesis quality, not just retrieval.

---

## `papers.json` — Field Reference

Each record is a dictionary. The 442 records are stored as a JSON array.

### Identification

| Field | Type | Description |
|-------|------|-------------|
| `ID` | int | Internal MetaSyn paper ID |
| `Title` | str | Meta-analysis title |
| `Abstract` | str | Full abstract |
| `source` | str | Source journal |
| `origin_collector_id` | str | Internal reference identifier |

### Research Question & Eligibility

| Field | Type | Description |
|-------|------|-------------|
| `Research_Question` | str | The clinical/scientific question the MA addresses |
| `Population` | str | PICO — target population |
| `Intervention` | str | PICO — intervention (null if ECO design) |
| `Exposure` | str | ECO — exposure (null if PICO design) |
| `Comparison` | str | PICO — comparator |
| `Outcome` | str | PICO — primary outcome(s) |
| `inclusion_criteria` | str | Verbatim eligibility inclusion criteria |
| `exclusion_criteria` | str | Verbatim eligibility exclusion criteria |

### Search Strategy

| Field | Type | Description |
|-------|------|-------------|
| `search_strategies` | str | PubMed search string(s) used in the original MA |
| `search_start_date` | str | Search window start (`YYYY-MM-DD` or null) |
| `search_end_date` | str | Search window end (`YYYY-MM-DD`) |

### Ground-Truth Corpus Match

| Field | Type | Description |
|-------|------|-------------|
| `matched_corpus_ids` | list[int] | Corpus IDs of the included studies found in MetaSyn corpus |
| `matched_ref_count` | int | Number of matched included studies |
| `match_rate` | float | Fraction of all cited studies found in corpus |
| `raw_titles` | list[str] | Raw reference titles from the paper |
| `extracted_titles` | list[str] | Cleaned titles used for matching |

### Effect & Statistics

| Field | Type | Description |
|-------|------|-------------|
| `Effect_Size_Type` | str | Type of effect measure (OR, RR, MD, SMD, …) |
| `Effect_Size_Value` | float | Pooled point estimate |
| `Effect_Size_Category` | str | Categorised magnitude (small / medium / large) |
| `CI_Lower` | float | 95% confidence interval lower bound |
| `CI_Upper` | float | 95% confidence interval upper bound |
| `P_Value` | float | Overall p-value |
| `Statistical_Significance` | str | `Significant` / `Not significant` |
| `I2_Value` | float | I² heterogeneity statistic (%) |
| `Q_Value` | float | Cochran's Q statistic |
| `Tau2_Value` | float | Between-study variance (τ²) |
| `Heterogeneity` | str | Narrative heterogeneity description |
| `Heterogeneity_Level` | str | Low / Moderate / High / Not reported |
| `Total_Sample_Size` | int | Total participants across all included studies |
| `study_count` | int | Number of included studies |
| `Publication_Bias` | str | Publication bias assessment method or result |

### Synthesis

| Field | Type | Description |
|-------|------|-------------|
| `Effect_Direction` | str | `Positive` / `Negative` / `Mixed` / `NR` |
| `Conclusion_Summary` | str | One-sentence conclusion |
| `conclusion_paragraph` | str | Full conclusion paragraph from the paper |
| `Key_Insights` | str | Main quantitative findings |
| `Introduction` | str | Introduction section excerpt |
| `Topic` | str | Broad topic category |

---

## `corpus.json` — Field Reference

A JSON array of 140,585 PubMed article records.

| Field | Type | Description |
|-------|------|-------------|
| `ID` | int | Internal corpus ID (referenced by `matched_corpus_ids`) |
| `pmid` | str | PubMed ID |
| `title` | str | Article title |
| `abstract` | str | Full abstract |
| `year` | int | Publication year |
| `journal` | str | Journal name |

---

## `test_ids.json`

A JSON array of 88 integer IDs identifying the test-split papers in `papers.json`.

```json
[63, 24, 203, ...]
```

---

## Statistics

| Statistic | Value |
|-----------|-------|
| Total meta-analyses | 442 |
| Train / test | 354 / 88 |
| Corpus articles | 140,585 |
| Unique journals | 8 (Nature Portfolio) |
| Median study count per MA | 14 |
| Mean study count per MA | 18.3 |
| Median corpus match rate | 82% |
| Retrieval ceiling @ K=200 (test) | 90.9% |
