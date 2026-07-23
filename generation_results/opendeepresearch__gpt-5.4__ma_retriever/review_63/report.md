# Systematic Review of Pre- versus Post-operative Esophageal Function After Laparoscopic Vertical Sleeve Gastrectomy (LVSG) in Adults With Morbid Obesity

## Review Question

This review examined primary cohort studies in the local MetaSyn PubMed corpus, published from 1999-01-01 through 2023-11-30, evaluating whether laparoscopic vertical sleeve gastrectomy (LVSG/LSG) changes:

- lower esophageal sphincter pressure (LESP),
- lower esophageal sphincter length (LESL),
- DeMeester Score (DMS), and/or
- body mass index (BMI),

using pre-operative versus post-operative esophageal physiology testing in adults with morbid obesity.

The target evidence base was limited to cohort studies using conventional esophageal manometry or high-resolution manometry, with or without 24-hour ambulatory pH monitoring.

---

## Search Strategy

## Data Source

Only the local MetaSyn PubMed corpus was used for retrieval, as required.

## Exact Local-Corpus Search Queries Used

1. `(sleeve gastrectomy OR vertical sleeve gastrectomy OR laparoscopic sleeve gastrectomy) AND (esophageal manometry OR high-resolution manometry OR lower esophageal sphincter OR DeMeester OR 24-hour pH) AND obesity`

2. `("sleeve gastrectomy" OR "vertical sleeve gastrectomy" OR "laparoscopic sleeve gastrectomy") AND (DeMeester OR "24-hour pH" OR pH-metry OR pH-monitoring) AND (preoperative OR postoperative OR before OR after)`

3. `("sleeve gastrectomy" OR "laparoscopic sleeve gastrectomy") AND (manometry OR "high-resolution manometry" OR "lower esophageal sphincter length" OR LES length OR LES pressure) AND (before AND after)`

These queries were formulated directly from the seed question and PI/ECO elements and did not rely on the title of any source review or meta-analysis.

---

## Retrieval Results

## Initial Retrieval

The first search returned **20 candidate records** from the local corpus.

Among the candidate set identified across the local searches, the following corpus IDs were specifically surfaced as likely relevant during screening:

- **8364**
- **108072**
- **69468**
- **4538**
- **8366**
- **4539**
- **4541**
- **4543**
- **69514**
- **4540**
- **4544**
- **4542** (comparative study with an LSG subgroup, flagged for possible relevance)

Additional records were flagged as clear exclusions during screening because they were reviews, outside the date window, or otherwise mismatched in design:

- **69467**
- **69533**
- **69508**
- **69461**
- **69486**
- **69506**

## Record-Level Retrieval Performed

Targeted record retrieval from the local corpus was then performed for key studies:

- `fetch_metasyn_record(corpus_id=8364, section="results", chunk=1)`
- `fetch_metasyn_record(corpus_id=4540, section="results", chunk=1)`
- `fetch_metasyn_record(corpus_id=4541, section="results", chunk=1)`
- `fetch_metasyn_record(corpus_id=4540, section="methods", chunk=1)`
- `fetch_metasyn_record(corpus_id=8364, section="methods", chunk=1)`
- `fetch_metasyn_record(corpus_id=4540, section="results", chunk=2)`

Only studies with enough information in the returned local-corpus evidence to verify design and extract outcome-relevant findings were retained for the final synthesis.

---

## Eligibility Criteria Applied

## Inclusion Criteria

- Full peer-reviewed journal cohort studies
- Adults with morbid obesity undergoing LVSG/LSG
- Published from 1999-01-01 through 2023-11-30
- Pre- and post-operative esophageal physiological testing
- Outcomes relevant to LESP, LESL, DMS, and/or BMI
- No sample-size restriction
- No language restriction

## Exclusion Criteria

- Non-human studies
- Duplicates
- Abstract-only conference articles
- Opinion pieces
- Editorial letters
- Case studies
- Reviews
- Meta-analyses

---

## Screening Decisions

## Included Studies

Four studies were sufficiently supported by the retrieved local-corpus evidence to include in the qualitative synthesis:

1. **Corpus ID 8364** – clearly eligible retrospective cohort with pre/post manometry and pH-metry, adults with morbid obesity, 62 cases.
2. **Corpus ID 108072** – clearly eligible prospective cohort with pre/post stationary esophageal manometry in morbid obesity, 37 patients.
3. **Corpus ID 69468** – clearly eligible prospective cohort with pre/post high-resolution manometry in 45 morbidly obese patients.
4. **Corpus ID 4538** – prospective pre/post manometry cohort in sleeve gastrectomy patients; included with caution because the abstract snippet identified “obese patients” and a mean BMI of 38.3 kg/m², which is compatible with bariatric eligibility, but the abstract snippet did not explicitly repeat “morbid obesity.”

## Excluded or Not Included in the Final Synthesis

### Clearly excluded from the evidence base
- **Corpus ID 69467** – review article; excluded by design.
- **Corpus IDs 69533, 69508, 69461, 69486, 69506** – flagged during screening as outside the date window or design-mismatched; excluded.

### Retrieved as candidates but not retained in the final synthesis
- **Corpus ID 4542** – comparative prospective study with an LSG subgroup; not retained because the available returned evidence did not confirm extractable LSG-specific pre/post outcome data for this review.
- **Corpus IDs 8366, 4539, 4541, 4543, 69514, 4540, 4544** – surfaced as candidates, but the available returned evidence in this research record was insufficient to verify all eligibility elements and outcome extractability strictly enough for final inclusion.

## Important screening limitation

Exact de-duplicated record counts across all three searches could not be reconstructed from the available research trace because only the first search’s total hit count (**20**) was explicitly documented, and the later query outputs were described qualitatively rather than as full enumerated lists. Accordingly, this report provides a transparent narrative screening account rather than a fully numeric PRISMA flow diagram.

---

## Included Study Characteristics

## 1) [Outcomes of laparoscopic sleeve gastrectomy by means of esophageal manometry and pH-metry, before and after surgery](https://pmc.ncbi.nlm.nih.gov/articles/PMC7020704/) — Corpus ID **8364** [1]

- Year: 2020
- Design: Retrospective pre/post cohort
- Sample: 62 cases with available data
- Population: Morbid obesity undergoing LSG
- Testing: Esophageal manometry + 24-hour ambulatory pH monitoring
- Outcomes assessed: BMI, esophageal amplitude pressure, total LES length, LES resting pressure, LES residual pressure, LES relaxation time, intragastric pressure, DeMeester score

## 2) [Functional importance of laparoscopic sleeve gastrectomy for the lower esophageal sphincter in patients with morbid obesity](https://pubmed.ncbi.nlm.nih.gov/22065341/) — Corpus ID **108072** [2]

- Year: 2012
- Design: Prospective cohort
- Sample: 37 patients; healthy controls also described
- Population: Patients with morbid obesity
- Testing: Stationary esophageal manometry; gastroscopy in a study collective
- Outcomes assessed: LES pressure, esophageal motility, BMI

## 3) [Impact of laparoscopic sleeve gastrectomy on esophageal physiology](https://pubmed.ncbi.nlm.nih.gov/33600675/) — Corpus ID **69468** [3]

- Year: 2021
- Design: Prospective cohort
- Sample: 45 morbidly obese patients
- Population: Morbid obesity
- Testing: High-resolution esophageal manometry; clinical and endoscopic assessment
- Outcomes assessed: BMI, GERD prevalence, LES hypotonia/length, intragastric pressure, motility abnormalities

## 4) [Manometric changes of the lower esophageal sphincter after sleeve gastrectomy in obese patients](https://pubmed.ncbi.nlm.nih.gov/20013071/) — Corpus ID **4538** [4]

- Year: 2010
- Design: Prospective cohort
- Sample: 20 patients
- Population: Obese adults undergoing sleeve gastrectomy; abstract-level evidence supports bariatric-severity obesity, but morbid obesity is not restated explicitly in the snippet
- Testing: Esophageal manometry
- Outcomes assessed: LES resting pressure, total LES length, abdominal LES length, BMI

---

## Findings by Outcome

## BMI Change

BMI decreased consistently across all included studies.

- **Corpus ID 8364**: a statistically significant difference was reported between pre-operative and 3-month post-operative BMI [1].
- **Corpus ID 108072**: postoperative BMI fell from **50.5 to 39.5 kg/m²** in one subgroup and from **47.5 to 45 kg/m²** in another [2].
- **Corpus ID 69468**: BMI decreased from **46.28 ± 5.79 kg/m²** to **32.28 ± 4.65 kg/m²** post-operatively (**p < 0.01**) [3].
- **Corpus ID 4538**: BMI decreased from **38.3 kg/m²** to **28.2 kg/m²** at 6 months [4].

### Interpretation

Weight loss after LVSG was robust and consistent across studies. BMI reduction is the most reproducible finding in this evidence base.

---

## Lower Esophageal Sphincter Pressure (LESP)

The direction of change in LESP was **inconsistent across studies**.

### Studies reporting decreased LESP after LVSG
- **Corpus ID 8364**: LESP was significantly reduced after surgery [1].
- **Corpus ID 4538**: mean LESP decreased from **14.2 ± 5.8 mmHg** pre-operatively to **11.2 ± 5.7 mmHg** post-operatively (**p = 0.01**); postoperative LESP fell in **17/20 patients (85%)** [4].

### Studies reporting increased LESP after LVSG
- **Corpus ID 108072**: postoperative LESP increased significantly:
  - from **8.4 to 21.2 mmHg** in one subgroup,
  - from **11 to 24 mmHg** in another subgroup,
  both with **p < 0.0001** [2].

### Studies suggesting adverse LES physiology but without extractable mean pre/post LESP values in the snippet
- **Corpus ID 69468**: postoperative reflux was associated with **LES hypotonia**, **shortening of LES length**, and **increased intragastric pressure** [3].

### Interpretation

The evidence does **not** support a single uniform effect of LVSG on LESP. Some studies suggest LVSG weakens the LES, while another found the opposite. Possible reasons include:

- different manometry methods (conventional vs high-resolution),
- variable surgical technique,
- different postoperative time points,
- different baseline reflux/hiatal hernia profiles,
- subgrouping strategies and small sample sizes.

---

## Lower Esophageal Sphincter Length (LESL)

Evidence on LES length is limited but tends to suggest **possible shortening or disruption** after LVSG in at least some patients.

- **Corpus ID 8364**: no significant difference was reported in parameters other than BMI, LESP, LES relaxation time, and DeMeester score; this suggests **no significant change in LES total length** in that study [1].
- **Corpus ID 69468**: postoperative reflux was associated with **shortening of LES length** [3].
- **Corpus ID 4538**: both **abdominal LES length** and **total length of the high-pressure zone** at the esophagogastric junction were reported to be affected after sleeve gastrectomy, indicating unfavorable manometric changes in LES length parameters [4].
- **Corpus ID 108072**: the retrieved abstract evidence focused on LES pressure and motility; LES length was not reported in the available snippet [2].

### Interpretation

LESL findings are sparse and heterogeneous. Two studies suggest shortening or impairment of LES length-related anatomy/pressure zone after LVSG, while one study did not find a significant total-length change. Overall, the evidence leans toward potential adverse structural-functional changes in some patients, but certainty is low.

---

## DeMeester Score (DMS)

Evidence for DMS was available primarily from one clearly eligible study.

- **Corpus ID 8364**: the **DeMeester score increased significantly** after LSG [1]. The abstract states that the increase in reflux episodes longer than 5 minutes was the main driver of the higher score.
- **Corpus ID 69468**: GERD prevalence increased from **17.8%** to **31.1%** post-operatively, with **de novo GERD in 22.2%**, but a DeMeester score was not reported in the available abstract snippet [3].
- **Corpus IDs 108072 and 4538**: no extractable DMS data were available in the returned evidence [2][4].

### Interpretation

The only directly extractable DMS evidence indicates worsening acid reflux after LVSG. The broader physiologic pattern in other included studies is consistent with that direction, but direct DMS data are too sparse for a strong pooled conclusion.

---

## Overall Pattern of Esophageal Physiologic Change After LVSG

Across the included studies, the most defensible overall interpretation is:

- **BMI decreases consistently and substantially** after LVSG.
- **Esophageal physiologic effects are mixed and often unfavorable**, particularly regarding reflux-related measures.
- **LESP does not change uniformly** across studies.
- **LESL may shorten in some cohorts**, though evidence is limited.
- **Objective reflux burden may worsen**, supported most directly by increased DeMeester score in one study and increased GERD prevalence/LES hypotonia signals in others.

This pattern is clinically plausible: LVSG appears highly effective for weight reduction, but it may alter the gastroesophageal junction in ways that can worsen reflux physiology in a subset of patients.

---

## Feasibility of Meta-analysis

A formal quantitative meta-analysis was **not feasible** based on the available local-corpus evidence extracted in this review.

## Reasons meta-analysis was not feasible

- **Inconsistent outcome reporting**
  - Some studies reported mean LESP values; others reported only directional statements or associations.
  - DMS was directly extractable from only one included study.
  - LESL was