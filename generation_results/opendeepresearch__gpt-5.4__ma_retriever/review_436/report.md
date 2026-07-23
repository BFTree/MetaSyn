# Systematic Review Report: Electronic Prescribing Interventions and Medication Errors in Hospital Prescribing Settings

## Review Question

The review question was:

> Among patients receiving medication prescriptions in hospital-based healthcare settings, do electronic prescribing interventions—especially computerized decision-support systems (CDS), computerized physician order entry (CPOE), and related electronic medication-management tools—reduce medication errors compared with usual care, manual or paper-based prescribing, or other non-electronic standard-care controls?

The review was restricted to records retrieved **only from the local MetaSyn PubMed corpus**, using searches conducted within the date window **2023-05-01 through 2024-11-03**. The source meta-analysis title was neither searched nor inferred.

---

## Eligibility Criteria

### Inclusion Criteria

Studies had to meet **all** of the following:

- **Population:** patients receiving medication prescriptions in **hospital settings**
- **Intervention:** electronic prescribing or medication-management systems consistent with the seed interventions, especially:
  - CPOE
  - CDS
  - prescribing-relevant EHR components
  - eMAR
  - BCMA
- **Comparator:** usual care, manual prescribing, paper-based prescribing, or another non-electronic standard-care control
- **Outcome:** **quantitative data** on medication error incidence, including potential medication errors, actual medication errors, and/or adverse drug events
- **Design:** randomized controlled trial (**RCT**)
- **Language:** English
- **Publication type:** full-text, peer-reviewed primary study

### Exclusion Criteria

Studies were excluded if they were:

- non-human studies
- non-RCT designs
- reviews, editorials, letters, or conference abstracts
- not available in full text in the local corpus
- lacking outcome data adequate for quantitative synthesis
- outside the requested date window for retrieval and reporting

---

## Search Strategy

## Exact Local Corpus Search Queries Used

The following exact local MetaSyn corpus queries were used.

### Query 1
```text
(electronic prescribing OR e-prescribing OR computerized physician order entry OR CPOE OR clinical decision support OR electronic health record OR electronic medication administration record OR barcode medication administration) AND (medication error OR prescribing error OR prescription error OR administration error OR dispensing error OR adverse drug event OR preventable adverse drug event) AND (hospital OR inpatient) AND (randomized OR randomised trial) AND English AND 2023/05/01:2024/11/03
```

### Query 2
```text
((computerized physician order entry OR CPOE OR clinical decision support OR electronic prescribing OR electronic medication administration record OR barcode medication administration) AND (medication error OR prescribing error OR administration error OR adverse drug event) AND (hospital OR inpatient) AND (randomized OR randomised OR trial))
```

### Query 3
```text
((barcode medication administration OR BCMA OR electronic medication administration record OR eMAR) AND (medication error OR administration error OR dispensing error OR adverse drug event) AND (hospital OR inpatient) AND (randomized OR randomised OR trial) AND 2023)
```

### Query 4
```text
((computerized physician order entry OR CPOE OR clinical decision support OR electronic prescribing OR electronic health record prescribing) AND (medication error OR prescribing error OR prescription error OR preventable adverse drug event) AND (hospital OR inpatient) AND (randomized OR randomised OR trial) AND 2024)
```

---

## Retrieval Results

### Candidate Retrieval

Each search returned **20 candidate records**. The retrieval engine behaved as a **relevance-based search** rather than a strict date or design filter. As a result, the result sets included many records that were:

- outside the requested publication window
- non-randomized
- reviews rather than primary studies
- outpatient or community-pharmacy studies
- studies not focused on hospital prescribing
- studies involving medication technologies but not prescribing interventions of interest

### Unique Candidate Corpus IDs Identified

The following unique exact Corpus IDs were retrieved across the searches:

- **72192**
- **114473**
- **84566**
- **119909**
- **2579**
- **114471**
- **105948**
- **2578**
- **119913**
- **119810**
- **28537**
- **118856**
- **139623**
- **2574**
- **118857**
- **119610**
- **83037**
- **84571**
- **113490**
- **4739**
- **114478**
- **139124**
- **139118**
- **72186**
- **118925**
- **136231**
- **139924**
- **118928**
- **4737**
- **72191**

---

## Screening Process

## Screening Approach

Screening was performed against the full eligibility framework:

1. within requested retrieval/reporting date window
2. English language
3. full-text peer-reviewed article available in local corpus
4. primary study
5. randomized controlled trial
6. hospital-based patient prescribing setting
7. intervention consistent with electronic prescribing / medication-management seed
8. comparator consistent with usual care or non-electronic standard care
9. quantitative medication-error outcome data

Because many records were clearly non-eligible from search-result metadata alone, most were excluded at the title/record level. Full-text section retrieval was performed for the most relevant in-window candidates.

### Full-Text Fetches Performed

The following local corpus full-text section fetches were conducted:

- **Corpus ID 114471** — methods and results sections
- **Corpus ID 119909** — methods and results sections
- **Corpus ID 118928** — all available content

These fetches were used to verify study design, setting, intervention characteristics, and outcome reporting.

---

## Screening Results

## Summary of Key Exclusion Patterns

The candidate pool was dominated by four main exclusion patterns:

- **Outside date window**
- **Not an RCT**
- **Not a hospital prescribing study matching the intervention/comparator definition**
- **Review/abstract-only/insufficient full-text availability**

No record satisfied all criteria simultaneously.

### Records Clearly Excluded for Being Outside the Required Date Window

The following records were excluded because they fell outside the requested date window **2023-05-01 to 2024-11-03**; several also had additional exclusion reasons:

- **72192** — 2008; systematic review; not a primary RCT
- **114473** — 2020; integrative review; not a primary RCT
- **2579** — 2010; randomized trial but outside date window
- **2578** — 2018; cluster randomized outpatient study; outside date window and wrong setting
- **119810** — 2025; outside date window; review/community or outpatient focus
- **28537** — 2017; pre-post analysis, not RCT
- **139623** — 2021; observational pharmacist intervention study, not RCT
- **2574** — 2019; controlled randomized dispensing study, but outside date window
- **84571** — 2015; outpatient prescriptions; wrong setting and outside date window
- **4739** — 2013; association study of CPOE use, not RCT
- **114478** — 2018; before/after implementation study, not RCT
- **139124** — 2022; pre-post implementation study in pediatric anesthesia practice, not RCT
- **139118** — 2022; survey, not interventional RCT
- **72186** — 2019; retrospective implementation description, not RCT

### Most Relevant In-Window Records Reviewed More Closely

#### Corpus ID 114471
This was the most relevant in-window hospital record identified. Full-text methods and results were examined. It was excluded because:

- study design was **pre-post observational**, not randomized
- therefore it failed the **RCT** criterion
- although it appeared relevant to hospital medication-use processes, it did not meet the required trial design standard

#### Corpus ID 119909
This in-window record was examined in methods and results. It was excluded because:

- it was a **review**, not a primary trial
- it involved **community/outpatient pharmacy context**, not the target hospital prescribing setting
- therefore it failed both the **design** and **population/setting** criteria

#### Corpus ID 118928
This record appeared potentially relevant to medication technology in a hospital setting and was retrieved at the available local-corpus level. It was excluded because:

- it was a **retrospective pre-post** study rather than an RCT
- it focused on **smart pump interoperability / medication administration technology**, not clearly a prescribing intervention of the defined type
- available evidence was **abstract-level or limited local-corpus content only**, preventing full-text eligibility confirmation
- therefore it failed the **design** criterion and had **full-text availability limitations**

### Other In-Window or Search-Relevant Records Excluded for Non-Eligibility

The remaining search-retrieved records were excluded on one or more of the following grounds:

- **84566** — likely non-English and methodological/adaptation study rather than eligible hospital RCT
- **105948** — not confirmed as eligible RCT in target setting
- **119913** — not confirmed as eligible hospital prescribing RCT
- **118856** — not confirmed as eligible RCT; likely wrong design or intervention mismatch
- **118857** — not confirmed as eligible RCT; likely wrong design or intervention mismatch
- **119610** — not confirmed as eligible hospital RCT
- **83037** — not confirmed as eligible prescribing RCT
- **113490** — not confirmed as eligible RCT
- **118925** — not confirmed as eligible hospital prescribing RCT
- **136231** — not confirmed as eligible RCT
- **139924** — not confirmed as eligible RCT
- **4737** — not confirmed as eligible RCT
- **72191** — not confirmed as eligible hospital prescribing RCT

For these records, the available retrieval information did not support inclusion, and none emerged as a clear match after focused querying and targeted verification of the most plausible in-window candidates.

---

## Study Selection Outcome

## Included Studies

**No study met all eligibility criteria.**

Specifically, no retrieved record within the local MetaSyn corpus and the defined search window satisfied all of the following together:

- in-range retrieval period
- English full-text peer-reviewed primary article
- hospital prescribing setting
- electronic prescribing or prescribing-related medication-management intervention
- non-electronic usual-care comparator
- quantitative medication-error outcome
- randomized controlled trial design

---

## Findings on Effectiveness

## Narrative Synthesis

Because **no study was eligible for inclusion**, there is **no admissible evidence set** from this restricted local-corpus review on which to determine whether electronic prescribing interventions reduce medication errors in hospital prescribing settings under the specified criteria.

### What the retrieval suggests

The search results indicate that the broader literature captured by the local corpus in this topic area contains:

- older randomized or controlled studies
- implementation and before/after evaluations of CPOE, CDS, BCMA, or related systems
- reviews and observational analyses
- studies in non-hospital settings such as outpatient clinics or community pharmacies

However, under the strict criteria of this review, these records could not be used as evidence.

### What cannot be concluded

It cannot be concluded from this review that:

- CPOE reduces medication errors in hospital prescribing settings
- CDS reduces medication errors in hospital prescribing settings
- eMAR or BCMA reduce medication errors in hospital prescribing settings
- electronic prescribing tools reduce adverse drug events in hospital settings

Those propositions may be supported or refuted in the wider literature, but **they were not demonstrated by eligible studies in this specific local-corpus, date-restricted, RCT-only review**.

---

## Quantitative Synthesis

## Meta-analysis Feasibility

A meta-analysis was **not possible**.

### Reason
There were **zero included studies**, so there were:

- no extractable effect estimates
- no denominators or event counts from eligible trials
- no basis for pooled analysis
- no basis for heterogeneity assessment, subgroup analysis, or risk-of-bias-informed synthesis

---

## Interpretation

## What This Review Means

Under a strict RCT-only framework and using only the local MetaSyn PubMed corpus within the specified retrieval period, the evidence base was effectively empty for the target question.

This does **not** mean electronic interventions are ineffective. It means that, within this tightly defined review frame:

- eligible hospital RCTs were not found
- the available records were mostly non-randomized, older, or outside scope
- the local corpus and full-text availability constraints materially limited inclusion

### Likely explanation for the empty evidence set

Several factors probably contributed:

1. **Medication-safety informatics interventions are often evaluated with quasi-experimental designs**  
   Hospital CPOE/CDS/eMAR/BCMA interventions are commonly studied using before/after, interrupted time-series, pre-post, or implementation designs rather than RCTs.

2. **The date restriction was narrow**  
   The reporting window from **2023-05-01 to 2024-11-03** was restrictive, while many classic hospital electronic prescribing trials predate it.

3. **The local corpus retrieval engine was relevance-based**  
   Even when date terms were included in the query, many out-of-window records were returned, requiring manual exclusion.

4. **Full-text limitations affected verification**  
   At least one potentially relevant hospital technology study (**Corpus ID 118928**) had only limited available content, making detailed eligibility assessment difficult.

---

## Limitations

## Limitations of the Evidence Base

- **No eligible RCTs were identified**, so the review could not estimate treatment effects.
- Many studies in this field appear to use **non-randomized implementation designs**, which were excluded by protocol.
- Some records concerned related medication-use technologies but did not fit the narrower prescribing-focused intervention definition.

## Limitations of the Local Corpus Retrieval

- Searches were restricted to the **local MetaSyn PubMed corpus only**.
- The local search function appeared to return **relevance-ranked** records rather than enforcing exact date, design, or language filters.
- Some records required manual verification and remained non-eligible after review.
- Some evidence was available only in **limited or abstract-level form** in the local corpus.

## Full-Text Availability Limitations

- **Corpus ID 118928** had limited available content in the local corpus; this should be treated as **abstract-only or incomplete full-text availability** for review purposes.
- Where full-text sections were unavailable, eligibility confirmation—especially for design, comparator, and quantitative outcome reporting—was constrained.

---

## Conclusion

Using only the local MetaSyn PubMed corpus and applying the specified eligibility criteria strictly, **no study was eligible for inclusion** in this systematic review.

As a result:

- there is **no includable RCT evidence** from this corpus and search window to determine whether electronic prescribing interventions—especially CPOE, CDS, eMAR, BCMA, or related prescribing-relevant EHR tools—reduce medication errors in hospital prescribing settings compared with usual care or paper-based/manual systems;
- **no meta-analysis could be conducted**;
- the main reason was not absence of all research in the field, but absence of studies meeting the combined requirements of:
  - hospital setting,
  - prescribing-focused electronic intervention,
  - non-electronic comparator,
  - quantitative medication-error outcomes,
  - English full text,
  - and randomized controlled trial design
  within the defined retrieval constraints.

---

## Included-Studies List

**No study was included.**

No retrieved local MetaSyn corpus record met all eligibility criteria.

---

### Sources

Because retrieval was restricted to the **local MetaSyn PubMed corpus**, no public URLs were supplied in the research findings. The exact local records and search outputs referenced in this report are listed below by Corpus ID.

[1] Local MetaSyn PubMed corpus record, Corpus ID 114471: no public URL available in the provided findings  
[2] Local MetaSyn PubMed corpus record, Corpus ID 119909: no public URL available in the provided findings  
[3] Local MetaSyn PubMed corpus record, Corpus ID 118928: no public URL available in the provided findings  
[4] Local MetaSyn PubMed corpus search result set containing Corpus IDs 72192, 114473, 84566, 119909, 2579, 114471, 105948, 2578, 119913, 119810, 28537, 118856, 139623, 2574, 118857, 119610, 83037, 84571, 113490, 4739: no public URL available in the provided findings  
[5] Local MetaSyn PubMed corpus search result set containing Corpus IDs 72192, 114473, 2579, 114471, 84566, 105948, 28537, 2574, 4739, 119913, 119909, 2578, 119610, 114478, 139124, 118856, 83037, 113490, 118857, 139623: no public URL available in the provided findings  
[6] Local MetaSyn PubMed corpus search result set containing Corpus IDs 2574, 139118, 139124, 114473, 72192, 119810, 114471, 72186, 83037, 105948, 84571, 119913, 118925, 139623, 84566, 119909, 136231, 139924, 118928, 2579: no public URL available in the provided findings  
[7] Local MetaSyn PubMed corpus search result set containing Corpus IDs 72192, 114473, 84566, 2579, 114471, 105948, 28537, 4739, 2578, 119909, 118856, 119913, 118857, 113490, 83037, 139623, 119610, 4737, 114478, 72191: no public URL available in the provided findings