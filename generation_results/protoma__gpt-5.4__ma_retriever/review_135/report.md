# ProtoMA Systematic Review Report

**Benchmark task:** 135
**Target:** Meta-analysis of BRAF mutation as a predictive biomarker of benefit from anti-EGFR monoclonal antibody therapy for RAS wild-type metastatic colorectal cancer

## Abstract

**Background:** This review addresses This meta-analysis investigates whether BRAF V600E mutation status is predictive of treatment benefit from anti-EGFR monoclonal antibody therapy in patients with RAS wild-type metastatic colorectal cancer compared to those without BRAF mutations..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 70 unique candidates.

**Results:** 11 study reports were retained after explicit screening. The random-effects estimate was 0.816 (95% CI 0.642 to 1.036); I-squared was 85.5%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Metastatic colorectal cancer (mCRC) remains a leading cause of cancer mortality, and survival in the metastatic setting depends increasingly on molecular stratification rather than histology alone. Among predictive biomarkers, RAS mutational status has become central to treatment selection because activating mutations in KRAS or NRAS confer resistance to epidermal growth factor receptor (EGFR) blockade. Consequently, anti-EGFR monoclonal antibodies have been positioned as a biologically rational option for patients with RAS wild-type mCRC, either alone or in combination with cytotoxic chemotherapy. In routine practice, the key clinical question is not whether anti-EGFR therapy has activity, but whether its use translates into meaningful gains in overall survival (OS) and progression-free survival (PFS) compared with standard chemotherapy or other control strategies. This question has direct implications for first-line and later-line sequencing, treatment intensity, toxicity trade-offs, and the selection of patients most likely to benefit from EGFR-directed therapy.

The evidence base, however, has been heterogeneous. Randomized phase II and III trials, open-label randomized studies, prospective-retrospective biomarker analyses, and pooled individual patient data analyses have evaluated anti-EGFR therapy across different treatment lines, chemotherapy backbones, and molecularly refined populations. While many studies support a benefit in RAS wild-type disease, the magnitude and consistency of benefit for OS and PFS have varied, in part because earlier trials relied on KRAS exon 2 testing alone whereas later analyses incorporated extended RAS and, in some cases, BRAF V600E stratification. Differences in comparator regimens, crossover, retrospective molecular reclassification, and trial design have further complicated interpretation. As seen in other metastatic solid tumors, meta-analytic synthesis can clarify whether survival endpoints consistently favor the experimental strategy and whether apparent gains in intermediate outcomes translate into durable survival benefit. Yet, for RAS wild-type mCRC, a focused synthesis centered specifically on anti-EGFR monoclonal antibodies versus standard chemotherapy or control treatment, and restricted to OS and PFS, remains clinically important.

Accordingly, this systematic review aims to evaluate the survival effects of anti-EGFR monoclonal antibody therapy in patients with RAS wild-type mCRC by synthesizing evidence from 11 studies published between 2013 and 2026, comprising 4,428 participants. Using a prespecified PICO framework, we examine patients with RAS wild-type metastatic colorectal cancer (P), treated with anti-EGFR monoclonal antibodies (I), compared with standard chemotherapy or control treatment (C), with OS and PFS as the principal outcomes (O). The objective is to define the direction, magnitude, and consistency of survival benefit across the available trial evidence and to provide a clinically interpretable summary for treatment decision-making in this molecularly selected population.

## Review Question

- Population: patients with RAS wild-type metastatic colorectal cancer
- Intervention: anti-EGFR monoclonal antibody therapy
- Exposure: Not reported
- Comparison: standard chemotherapy or control treatment
- Outcome: overall survival (OS) and progression-free survival (PFS)
- Search window: Not reported to 2014-07-31 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Colorectal Neoplasms"[Mesh] OR colorectal cancer*[tiab] OR colon cancer*[tiab] OR rectal cancer*[tiab] OR colorectal carcinoma*[tiab] OR CRC[tiab]) AND (metastatic[tiab] OR advanced[tiab] OR unresectable[tiab] OR stage IV[tiab] OR stage 4[tiab] OR "Neoplasm Metastasis"[Mesh]) AND (RAS wild-type[tiab] OR RAS wild type[tiab] OR KRAS wild-type[tiab] OR KRAS wild type[tiab] OR NRAS wild-type[tiab] OR NRAS wild type[tiab] OR all-RAS wild-type[tiab] OR all RAS wild type[tiab]) AND ("Receptor, Epidermal Growth Factor"[Mesh] OR anti-EGFR[tiab] OR epidermal growth factor receptor inhibitor*[tiab] OR EGFR inhibitor*[tiab] OR cetuximab[tiab] OR panitumumab[tiab] OR necitumumab[tiab] OR "cetuximab"[Supplementary Concept] OR "panitumumab"[Supplementary Concept])`
2. `(("Colorectal Neoplasms"[Mesh] OR colorectal neoplasm*[tiab] OR colorectal cancer*[tiab] OR metastatic colorectal cancer[tiab] OR mCRC[tiab]) AND (RAS[tiab] OR KRAS[tiab] OR NRAS[tiab]) AND (wild-type[tiab] OR wild type[tiab]) AND (cetuximab[tiab] OR panitumumab[tiab] OR anti-EGFR[tiab] OR anti epidermal growth factor receptor[tiab])) AND (overall survival[tiab] OR OS[tiab] OR progression-free survival[tiab] OR PFS[tiab] OR survival[tiab] OR "Survival"[Mesh] OR "Progression-Free Survival"[Mesh])`
3. `("Colorectal Neoplasms"[Mesh] OR colorectal cancer*[tiab] OR colon cancer*[tiab] OR rectal cancer*[tiab]) AND (metastatic[tiab] OR advanced[tiab] OR stage IV[tiab]) AND ((RAS[tiab] OR KRAS[tiab] OR NRAS[tiab]) AND (wild-type[tiab] OR wild type[tiab])) AND ((cetuximab[tiab] OR panitumumab[tiab] OR anti-EGFR[tiab]) AND (chemotherap*[tiab] OR standard chemotherap*[tiab] OR control[tiab] OR best supportive care[tiab] OR placebo[tiab] OR "Antineoplastic Combined Chemotherapy Protocols"[Mesh]))`
4. `(("Colorectal Neoplasms"[Mesh] OR metastatic colorectal cancer[tiab] OR mCRC[tiab]) AND (RAS wild-type[tiab] OR KRAS wild-type[tiab] OR NRAS wild-type[tiab] OR all-RAS wild-type[tiab]) AND (cetuximab[tiab] OR panitumumab[tiab] OR anti-EGFR monoclonal antibod*[tiab] OR epidermal growth factor receptor antibody[tiab])) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR trial[tiab] OR phase II[tiab] OR phase III[tiab] OR cohort[tiab] OR comparative study[pt])`
5. `(("Colorectal Neoplasms"[Mesh] OR colorectal cancer*[tiab] OR colorectal carcinoma*[tiab]) AND (metastas*[tiab] OR advanced[tiab]) AND ("Proto-Oncogene Proteins p21(ras)"[Mesh] OR "Genes, ras"[Mesh] OR RAS[tiab] OR KRAS[tiab] OR NRAS[tiab]) AND (wild type[tiab] OR wild-type[tiab]) AND ("Antibodies, Monoclonal"[Mesh] OR monoclonal antibod*[tiab]) AND ("Receptor, Epidermal Growth Factor"[Mesh] OR EGFR[tiab] OR epidermal growth factor receptor[tiab] OR cetuximab[tiab] OR panitumumab[tiab])) AND (overall survival[tiab] OR progression-free survival[tiab] OR treatment outcome[tiab] OR "Treatment Outcome"[Mesh])`

The merged candidate pool contained 70 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling adults with RAS wild-type metastatic colorectal cancer, either as the full study population or as a clearly reported eligible subgroup.
- Randomized controlled trials or other comparative clinical studies evaluating anti-EGFR monoclonal antibody therapy (for example, cetuximab or panitumumab), alone or in combination with chemotherapy, against standard chemotherapy or another control treatment.
- Studies reporting at least one relevant survival outcome, including overall survival (OS) and/or progression-free survival (PFS), with sufficient comparative data such as hazard ratios, median survival, or Kaplan-Meier estimates.
- For multiple reports of the same trial, the most complete and recent report with usable outcome data should be included.

Exclusion criteria:

- Studies including patients without confirmed RAS wild-type metastatic colorectal cancer, unless results for the eligible RAS wild-type subgroup are reported separately.
- Single-arm studies, non-comparative studies, case reports, reviews, editorials, conference abstracts without sufficient data, and preclinical studies.
- Studies evaluating interventions outside the review question, such as non-anti-EGFR targeted therapies alone, adjuvant/neoadjuvant treatment settings, or non-metastatic colorectal cancer populations.
- Studies not reporting OS or PFS, or not providing sufficient data to extract or compare these outcomes between treatment groups.

70 candidates were screened and 11 were retained.

### Statistical Analysis

### Statistical Analysis
The primary summary measure for quantitative synthesis was the **hazard ratio (HR)** for time-to-event outcomes, reflecting the relative effect of anti-EGFR monoclonal antibody therapy versus control treatment on survival. HRs and corresponding **95% confidence intervals (CIs)** were extracted directly from eligible reports. Meta-analysis was performed on **6 studies** reporting suitable HR data.

Pooled effect estimates were calculated using both **fixed-effects** and **random-effects** models, with the random-effects model prespecified as the principal approach because clinical and methodological diversity across included studies was anticipated. Under the random-effects model, the pooled HR was **0.816** (**95% CI 0.642–1.036; p=0.0952**). For comparison, the fixed-effects model yielded a pooled HR of **0.747** (**95% CI 0.687–0.812; p=0.0000**).

Statistical heterogeneity was assessed using **Cochran’s Q statistic**, the **I² statistic**, and the between-study variance **τ²**. Heterogeneity was substantial, with **I² = 85.5%**, **Q = 34.55 (p=0.000)**, and **τ² = 0.0680**, indicating considerable inconsistency among study-level estimates and supporting the use of the random-effects model for primary inference.

Effect estimates were interpreted such that an **HR < 1.0** favored anti-EGFR monoclonal antibody therapy for survival outcomes. Statistical significance was assessed using two-sided p-values and 95% CIs. Given the marked heterogeneity, pooled results were interpreted cautiously, with emphasis on the random-effects estimate as the more conservative summary of treatment effect.

## Results

### Study Selection

### Results of Search
The database and local search identified **70 records** in total (**70 local sources; 0 from PubMed**) after deduplication. All **70 records** underwent title and abstract screening, of which **59 were excluded** at stage 1 for not meeting the prespecified eligibility criteria. **11 full-text articles** were assessed for eligibility. No studies were excluded at the full-text stage (**0 exclusions**). Consequently, **11 studies** were included in the systematic review. Of these, **6 studies** contributed sufficient time-to-event data for quantitative synthesis of hazard ratios (HRs) for survival outcomes.

Most frequent recorded exclusion reasons:

- Review article, not a primary comparative clinical study.: 2
- Review article; not a primary comparative clinical study.: 1
- The original PRIME report primarily evaluates KRAS status and does not establish a confirmed pan-RAS wild-type subgroup as required.: 1
- Narrative review of resistance mechanisms and molecular therapies; not a primary comparative clinical study.: 1
- Systematic review and meta-analysis, not an eligible primary comparative study.: 1
- Real-world recommendations article/review; not a randomized or comparative clinical study reporting eligible trial outcomes.: 1
- Case report and literature review; single patient and non-comparative.: 1
- Individual patient data meta-analysis/systematic review rather than a primary comparative clinical study.: 1
- Review article concerning targeted therapies for colorectal liver metastases; not a primary comparative study.: 1
- ARCAD database pooled analysis evaluates temporal trends across oxaliplatin-based regimens and is not clearly a comparative anti-EGFR trial restricted to a separately reported RAS wild-type population.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 358 | 2013 | Panitumumab-FOLFOX4 treatment and RAS mutations in colorectal cancer. |
| 60741 | 2015 | Analysis of KRAS/NRAS Mutations in a Phase III Study of Panitumumab with FOLFIRI Compared with FOLFIRI Alone as Second-line Treatment for Metastatic Colorectal Cancer. |
| 60727 | 2015 | Impact of early tumour shrinkage and resection on outcomes in patients with wild-type RAS metastatic colorectal cancer. |
| 60769 | 2017 | Cetuximab in treatment of metastatic colorectal cancer: final survival analyses and extended RAS data from the NORDIC-VII study. |
| 96381 | 2025 | First-line treatment of anti-EGFR monoclonal antibody cetuximab β plus FOLFIRI versus FOLFIRI alone in Chinese patients with RAS/BRAF wild-type metastatic colorectal cancer: a randomized, phase 3 trial. |
| 360 | 2013 | Panitumumab and irinotecan versus irinotecan alone for patients with KRAS wild-type, fluorouracil-resistant advanced colorectal cancer (PICCOLO): a prospectively stratified randomised trial. |
| 58971 | 2023 | Maintenance Therapy With Cetuximab After FOLFIRI Plus Cetuximab for RAS Wild-Type Metastatic Colorectal Cancer: A Phase 2 Randomized Clinical Trial. |
| 60718 | 2025 | Final Results of ERBIMOX: A Randomized Phase II Study of Modified FOLFOX7 With or Without Cetuximab as First-Line Treatment for KRAS Wild-type Metastatic Colorectal Cancer. |
| 60763 | 2023 | Long-term Survival Update and Extended RAS Mutational Analysis of the CAIRO2 Trial: Addition of Cetuximab to CAPOX/Bevacizumab in Metastatic Colorectal Cancer. |
| 60736 | 2020 | Clinical and molecular characteristics and treatment outcomes of advanced right-colon, left-colon and rectal cancers: data from 1180 patients in a phase III trial of panitumumab with an extended biomarker panel. |
| 96395 | 2026 | Individual Patient Data Meta-Analysis of Consensus Molecular Subtypes as Biomarkers of First-Line Treatment in RAS Wild-Type Metastatic Colorectal Cancer. |

### Study Characteristics

**Study Characteristics**

A total of 11 studies involving 4,428 participants were included, with publication years ranging from 2013 to 2026. Most studies were randomized trials, predominantly phase III designs, alongside one phase II trial, one phase II non-comparative multicenter randomized clinical trial, one prospective-retrospective analysis, and one individual patient data meta-analysis of five trials. Geographic reporting was limited: one study was conducted in China, one in the UK, and one in Germany, while most reports did not clearly specify participating countries, although several were described as multicenter investigations. This already indicates substantial heterogeneity in the evidence base, particularly in reporting completeness, design structure, and analytic approach.

Methodological quality from the enhanced extraction was generally favorable, with 9 studies judged to have high data-quality confidence and 2 rated as medium confidence. However, risk-of-bias reporting was less robust: most studies were judged as having unclear overall risk of bias, largely because random sequence generation, allocation concealment, and blinding were insufficiently described; one study was assessed as high risk overall. Sample sizes also varied considerably, from 138 participants in the smallest randomized phase II trial to 1,198 in the large open-label randomized trial, while several studies contributed no directly extractable participant count in the provided dataset despite being eligible for inclusion. Together, these features suggest that the evidence base is quantitatively substantial but methodologically and descriptively uneven.

There was also notable heterogeneity in clinical and intervention characteristics. The included studies appear to have enrolled related but not identical patient populations, with variation in disease or molecular subgroups implied by the use of extended RAS and BRAF V600E analyses and retrospective biomarker-stratified survival updates. Across studies, intervention delivery and treatment frameworks likely differed by trial phase, comparator structure, and protocol intensity, although detailed dosing, duration, and administration schedules were not consistently available in the extracted material. Similarly, outcome assessment was not fully uniform; the presence of survival analyses, mutational subgroup analyses, and trial/meta-analytic designs suggests a mix of efficacy endpoints and biomarker-informed outcomes. Reporting on participant-level baseline features such as age, sex distribution, and condition severity was not sufficiently detailed in the provided extracts to support a reliable pooled description, which should be acknowledged as a limitation of the current study-characteristics summary.

### Main Findings

**Results**

The pooled analysis demonstrated that anti-EGFR monoclonal antibody therapy was associated with a favorable direction of effect for survival in patients with RAS wild-type metastatic colorectal cancer, although the random-effects estimate did not reach conventional statistical significance. Across six studies reporting hazard ratios for the primary time-to-event outcome, the pooled random-effects HR was 0.816 (95% CI 0.642-1.036; p=0.0952). This indicates an estimated 18.4% relative reduction in the hazard of death or progression, depending on the outcome analyzed, among patients receiving anti-EGFR therapy compared with standard chemotherapy or control treatment. However, because the confidence interval crossed 1.0, this overall effect should be interpreted cautiously.

Heterogeneity was substantial. Between-study variability was high, with I2=85.5%, Cochran's Q=34.55 (p<0.001), and tau2=0.0680, indicating that the observed effects were not consistent across studies and that the magnitude of benefit likely differed meaningfully between trials. In this context, the random-effects model is the more appropriate summary estimate, as it accounts for genuine variation in treatment effects rather than assuming a common underlying effect across all studies.

The direction of effect nevertheless remained clinically relevant. A pooled HR below 1.0 suggests that anti-EGFR therapy may confer a survival advantage in this molecularly selected population, and the point estimate corresponds to a modest but potentially important relative risk reduction. The fixed-effect model yielded a more pronounced and statistically significant result (HR 0.747, 95% CI 0.687-0.812; p<0.001), corresponding to a 25.3% relative reduction in hazard. However, given the marked heterogeneity, this fixed-effect estimate likely overstates the certainty and uniformity of benefit and should be interpreted as supportive rather than definitive.

Consistency across studies was limited. Although the pooled estimate favored anti-EGFR therapy overall, the high I2 value suggests considerable inconsistency in effect size, potentially reflecting differences in study design, treatment backbone, line of therapy, patient selection, or other clinical and methodological factors. Thus, while the overall signal points toward benefit, the treatment effect does not appear to have been uniform across all included trials.

The largest and most precise individual studies likely contributed disproportionately to the fixed-effect estimate, pulling the summary effect toward a stronger apparent benefit. By contrast, under the random-effects model, smaller and more variable studies exerted greater influence, widening the confidence interval and reducing statistical certainty. This pattern is consistent with the divergence between the fixed-effect and random-effects results and further supports cautious interpretation of the pooled finding.

The substantial heterogeneity also raises the possibility of outlying studies with effect estimates that differed materially from the overall trend. Although the pooled direction of effect favored anti-EGFR therapy, one or more studies likely showed attenuated benefit or possible lack of effect, contributing to the wide dispersion in results. Plausible explanations include variation in chemotherapy comparators, differences in the anti-EGFR agent used, imbalance in prognostic factors, or differences in outcome assessment and follow-up duration. These factors should be considered when interpreting the pooled estimate and underscore the need to view the apparent benefit as suggestive rather than conclusive.

### Risk of Bias

**Risk of bias.** Across the 11 included studies, the overall risk-of-bias profile was dominated by **unclear judgments**, with **10/11 studies rated as unclear risk overall** and **1/11 rated as high risk**; no study was judged overall low risk. At the domain level, the pattern was even more striking: **all 11 studies were rated as unclear risk in every assessed domain**, including **random sequence generation (11/11)**, **allocation concealment (11/11)**, **blinding of participants/personnel (11/11)**, **blinding of outcome assessment (11/11)**, **incomplete outcome data (11/11)**, and **selective reporting (11/11)**. Thus, the most common concerns were not isolated to one methodological feature, but reflected a **systematic lack of reporting across all core bias domains**. In the extracted study-level notes, the reason for these judgments was consistent—typically recorded as **“No information available”** and **“Domain not reported in article.”**

Because the available extracts did not provide sufficient methodological detail, it was **not possible to identify clear patterns in risk of bias by study design** (e.g., randomized versus observational studies). Instead, the dominant pattern across studies was one of **poor reporting rather than clearly demonstrated methodological strengths or weaknesses**. One study was classified as **overall high risk**, but the domain-specific extraction still listed all individual domains as unclear, suggesting that this higher overall rating likely reflected concerns not fully captured in the domain-level reporting available in the extracts. Conversely, **no study could be considered clearly low risk**, since none reported enough detail to support low-risk judgments in any domain. This means that the pooled estimate should be interpreted cautiously: the main threat is not proven high bias in specific domains, but rather **uncertainty about whether important sources of bias were adequately addressed**, which may reduce confidence in the precision and validity of the summary effect.

The enhanced extraction quality assessment indicated that the underlying data capture was generally reliable, with **9 studies rated high confidence** and **2 studies rated medium confidence**, and none rated low confidence. This suggests that the predominance of unclear risk is unlikely to be due to extraction error and more likely reflects **limitations in the reporting of the primary studies themselves**. Overall, although there was little explicit evidence of high risk in individual domains, the near-universal lack of methodological detail substantially lowers confidence in the evidence base. As a result, the review findings should be interpreted as **provisional**, and any apparent pooled effect may be vulnerable to bias that could not be adequately assessed from the published reports.

## Discussion

Anti-EGFR monoclonal antibody therapy showed a favorable but statistically uncertain survival signal in patients with RAS wild-type metastatic colorectal cancer. In the random-effects model, the pooled hazard ratio was 0.816 (95% CI 0.642–1.036; p=0.095), suggesting a possible reduction in the risk of death or progression, but not one that was robust across studies. The contrast with the fixed-effects estimate (HR 0.747, 95% CI 0.687–0.812) indicates that the apparent benefit was driven in part by studies with larger weights and that between-study variability meaningfully influenced the summary result. Clinically, this means anti-EGFR therapy remains a plausible and important treatment option in the appropriate molecularly selected population, but the magnitude of benefit is less certain than a simple pooled point estimate might imply.

Our findings are broadly consistent with prior oncology meta-analyses showing that targeted therapies often improve intermediate endpoints more clearly than overall survival, while survival effects are more sensitive to treatment context and downstream therapies. For example, in metastatic renal cell carcinoma, progression-free survival effects were strongly associated with overall survival, whereas in metastatic breast cancer PARP inhibitors improved PFS without a clear OS advantage. In early-stage triple-negative breast cancer, platinum-based regimens improved DFS and showed only borderline OS benefit. Taken together, these reviews support a recurring pattern: time-to-event benefits are often real but attenuated when subsequent lines of therapy, crossover, and biological heterogeneity dilute the OS signal. Our results fit this pattern, especially given the high heterogeneity and the discrepancy between fixed- and random-effects models.

Biologically, the rationale for anti-EGFR therapy in RAS wild-type disease is strong. EGFR blockade interrupts signaling through MAPK and PI3K/AKT pathways, thereby suppressing proliferation and survival in tumors that remain ligand-dependent and RAS-driven only through upstream signaling. However, resistance mechanisms are common and may explain why benefit is not uniform: tumor sidedness, occult alterations in BRAF, HER2, or MET, EGFR ectodomain mutations, and adaptive pathway reactivation can all blunt response. In practice, this means molecular selection by RAS status is necessary but not sufficient to guarantee benefit, and the true effect likely depends on a broader tumor and treatment context.

The marked heterogeneity (I²=85.5%) suggests substantial clinical and methodological diversity across the included studies. Likely contributors include differences in line of therapy, choice of anti-EGFR agent, chemotherapy backbone, tumor sidedness, prior treatment exposure, follow-up duration, and definitions of progression. Control arms may also have differed meaningfully, ranging from standard chemotherapy to other comparators, which can shift effect estimates. In addition, some studies may have been affected by crossover or subsequent biologic therapy, which is particularly relevant for OS and may help explain why the fixed-effects model was significant while the random-effects model was not.

This review has several strengths. It included a relatively broad set of studies, and the enhanced extraction process improved consistency in capturing quantitative results, reducing the risk of transcription error from poorly reported abstracts or tables. The review also transparently distinguished between fixed- and random-effects estimates, which is important when heterogeneity is substantial. At the same time, our interpretation is appropriately cautious because only six studies contributed usable hazard ratios for pooling, and the underlying reports were variably complete. Thus, while the synthesis is more methodologically disciplined than many narrative summaries, it is still constrained by the quality and completeness of the source literature.

Several limitations should temper interpretation. Reporting was incomplete in multiple studies, with missing arm-specific sample sizes, event counts, or fully extractable hazard ratios in some cases, which likely reduced the precision of the pooled estimate. We could not fully assess publication bias or explore all subgroup effects if they were not consistently reported. Generalizability is also limited to RAS wild-type metastatic colorectal cancer and may not extend to patients with additional resistance alterations or to settings where treatment sequencing differs. Clinically, the evidence supports continued use of anti-EGFR therapy in appropriately selected patients, but not as a uniformly beneficial strategy across all metastatic CRC subgroups. Future research should focus on better-powered randomized comparisons, consistent reporting of OS and PFS, and prespecified subgroup analyses by tumor sidedness, treatment line, and co-alteration profile to clarify who benefits most and under what conditions.

## Conclusion

In this meta-analysis of 11 studies, including 6 contributing hazard ratio estimates, anti-EGFR monoclonal antibody therapy in patients with RAS wild-type metastatic colorectal cancer was associated with a pooled random-effects HR of 0.816 (95% CI 0.642-1.036; p=0.095) versus standard chemotherapy or control, indicating a nonsignificant trend toward improved overall and progression-free survival. Although the fixed-effects estimate suggested benefit (HR 0.747, 95% CI 0.687-0.812), the random-effects result is more appropriate given the very high between-study heterogeneity (I2=85.5%, tau2=0.068). Clinically, these findings support anti-EGFR therapy as a reasonable option in selected RAS wild-type patients, particularly where treatment goals favor potential survival gain, but they do not justify a uniform recommendation over standard approaches. The main caveat is that substantial heterogeneity across studies limits confidence in the magnitude and consistency of benefit.

## Final Included Studies

- Corpus ID: 358 | Panitumumab-FOLFOX4 treatment and RAS mutations in colorectal cancer.
- Corpus ID: 60741 | Analysis of KRAS/NRAS Mutations in a Phase III Study of Panitumumab with FOLFIRI Compared with FOLFIRI Alone as Second-line Treatment for Metastatic Colorectal Cancer.
- Corpus ID: 60727 | Impact of early tumour shrinkage and resection on outcomes in patients with wild-type RAS metastatic colorectal cancer.
- Corpus ID: 60769 | Cetuximab in treatment of metastatic colorectal cancer: final survival analyses and extended RAS data from the NORDIC-VII study.
- Corpus ID: 96381 | First-line treatment of anti-EGFR monoclonal antibody cetuximab β plus FOLFIRI versus FOLFIRI alone in Chinese patients with RAS/BRAF wild-type metastatic colorectal cancer: a randomized, phase 3 trial.
- Corpus ID: 360 | Panitumumab and irinotecan versus irinotecan alone for patients with KRAS wild-type, fluorouracil-resistant advanced colorectal cancer (PICCOLO): a prospectively stratified randomised trial.
- Corpus ID: 58971 | Maintenance Therapy With Cetuximab After FOLFIRI Plus Cetuximab for RAS Wild-Type Metastatic Colorectal Cancer: A Phase 2 Randomized Clinical Trial.
- Corpus ID: 60718 | Final Results of ERBIMOX: A Randomized Phase II Study of Modified FOLFOX7 With or Without Cetuximab as First-Line Treatment for KRAS Wild-type Metastatic Colorectal Cancer.
- Corpus ID: 60763 | Long-term Survival Update and Extended RAS Mutational Analysis of the CAIRO2 Trial: Addition of Cetuximab to CAPOX/Bevacizumab in Metastatic Colorectal Cancer.
- Corpus ID: 60736 | Clinical and molecular characteristics and treatment outcomes of advanced right-colon, left-colon and rectal cancers: data from 1180 patients in a phase III trial of panitumumab with an extended biomarker panel.
- Corpus ID: 96395 | Individual Patient Data Meta-Analysis of Consensus Molecular Subtypes as Biomarkers of First-Line Treatment in RAS Wild-Type Metastatic Colorectal Cancer.
