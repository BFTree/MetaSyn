# ProtoMA Systematic Review Report

**Benchmark task:** 127
**Target:** Therapeutic outcome of early-phase clinical trials in multiple myeloma: a meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis examines the therapeutic outcomes, specifically overall response rates and toxicity profiles, of early-phase (phase I and phase II) clinical trials investigating experimental drugs as single agents or in combination with dexamethasone in patients with relapsed/refractory multiple myeloma over the past decade..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 78 unique candidates.

**Results:** 23 study reports were retained after explicit screening. The random-effects estimate was 4.432 (95% CI 1.166 to 16.850); I-squared was 90.9%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Multiple myeloma remains an incurable plasma cell malignancy characterized by successive relapses, progressive clonal evolution, and diminishing treatment sensitivity over time. Although proteasome inhibitors, immunomodulatory drugs, anti-CD38 monoclonal antibodies, and, more recently, cellular and bispecific immunotherapies have improved survival, patients with relapsed/refractory multiple myeloma (RRMM) continue to face a clinically important risk of treatment resistance, cumulative toxicity, and shortened remission duration with each subsequent line of therapy. This problem is especially consequential in heavily pretreated patients, for whom standard options may be exhausted or poorly tolerated and in whom access to highly specialized therapies is not uniform across practice settings. In this context, phase I and phase II studies of experimental compounds—used alone or in combination with dexamethasone—play a critical role in identifying active agents, defining tolerability, and signaling which therapeutic strategies merit later-phase evaluation.

However, the early-phase RRMM literature is methodologically fragmented. Trials differ substantially in mechanism of action, disease severity, prior treatment exposure, dose-escalation design, response assessment, and toxicity reporting, making cross-study interpretation difficult. At the same time, the therapeutic landscape has shifted markedly between 2010 and 2024, with the field moving from small-molecule and targeted approaches toward increasingly sophisticated immune-based and biologically selected strategies. As a result, the apparent activity of an investigational agent cannot be interpreted independently of its publication era or drug class. Existing evidence syntheses in oncology have shown the value of pooling single-arm and early-phase trial data to clarify treatment signals and identify patterns in efficacy across subgroups or treatment platforms. Yet, to our knowledge, no systematic review has specifically synthesized early-phase trials of experimental compounds in RRMM with direct attention to variation in overall response rate (ORR) and toxicity across years of publication and between drug classes.

Accordingly, this systematic review evaluates phase I and phase II clinical trials of experimental compounds administered as monotherapy or in combination with dexamethasone in patients with RRMM. Across 23 studies published from 2010 to 2024 and including 1,519 participants, we examine two outcomes central to early drug development and clinical decision-making: ORR as a signal of antimyeloma activity and toxicity as a measure of feasibility and risk. The review is designed not simply to summarize investigational agents, but to compare response and safety patterns across therapeutic classes and publication periods, thereby providing a structured view of how early-phase drug development in RRMM has evolved and where promising but clinically meaningful gaps remain.

## Review Question

- Population: Patients with relapsed/refractory multiple myeloma (RRMM)
- Intervention: Experimental compounds as single agents or in combination with dexamethasone in phase I and phase II clinical trials
- Exposure: Not reported
- Comparison: Comparisons across years of publication and between different drug classes
- Outcome: Overall response rate (ORR) and toxicity
- Search window: 2010-01-01 00:00:00 to 2020-07-01 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Multiple Myeloma"[Mesh] OR "multiple myeloma"[tiab] OR myeloma[tiab] OR "plasma cell myeloma"[tiab]) AND ((relaps*[tiab] OR refractory[tiab] OR "relapsed/refractory"[tiab] OR RRMM[tiab]) OR ("Recurrence"[Mesh] OR "Drug Resistance, Neoplasm"[Mesh])) AND (("Drug Therapy, Combination"[Mesh] OR "Antineoplastic Agents"[Mesh] OR investigational[tiab] OR experimental[tiab] OR novel[tiab] OR emerging[tiab] OR monotherapy[tiab] OR "single agent"[tiab] OR combination[tiab]) AND (dexamethasone[Mesh] OR dexamethasone[tiab] OR dex[tiab]))`
2. `(("multiple myeloma"[tiab] OR "plasma cell myeloma"[tiab] OR "Multiple Myeloma"[Mesh]) AND (relapsed[tiab] OR refractory[tiab] OR relapsing[tiab] OR RRMM[tiab])) AND (("phase I"[tiab] OR "phase 1"[tiab] OR "phase II"[tiab] OR "phase 2"[tiab] OR "Clinical Trial, Phase I"[Publication Type] OR "Clinical Trial, Phase II"[Publication Type]) AND (experimental[tiab] OR investigational[tiab] OR novel[tiab] OR "single agent"[tiab] OR monotherapy[tiab] OR combination[tiab] OR dexamethasone[tiab]))`
3. `(("Multiple Myeloma"[Mesh] OR "multiple myeloma"[tiab] OR myeloma[tiab]) AND (relapsed[tiab] OR refractory[tiab] OR RRMM[tiab])) AND (("overall response rate"[tiab] OR ORR[tiab] OR response[tiab] OR "treatment outcome"[Mesh]) AND (toxicity[tiab] OR toxicities[tiab] OR "adverse event*"[tiab] OR "treatment-related adverse event*"[tiab] OR safety[tiab] OR tolerability[tiab] OR "Drug-Related Side Effects and Adverse Reactions"[Mesh])) AND ("phase I"[tiab] OR "phase II"[tiab] OR "Clinical Trial, Phase I"[Publication Type] OR "Clinical Trial, Phase II"[Publication Type])`
4. `(("Multiple Myeloma/drug therapy"[Mesh] OR "multiple myeloma"[tiab]) AND (relapsed[tiab] OR refractory[tiab] OR RRMM[tiab])) AND (("Antineoplastic Combined Chemotherapy Protocols"[Mesh] OR "Drug Therapy, Combination"[Mesh] OR "Molecular Targeted Therapy"[Mesh] OR immunotherapy[tiab] OR targeted[tiab] OR "small molecule*"[tiab] OR antibody[tiab] OR inhibitor*[tiab] OR "CAR-T"[tiab] OR bispecific[tiab]) AND (dexamethasone[tiab] OR dexamethasone[Mesh] OR monotherapy[tiab] OR "single-agent"[tiab])) AND (trial[tiab] OR study[tiab] OR cohort[tiab] OR "clinical trial"[pt] OR "multicenter study"[pt])`
5. `(("multiple myeloma"[tiab] OR "Multiple Myeloma"[Mesh]) AND (relapsed[tiab] OR refractory[tiab] OR RRMM[tiab])) AND (("clinical trial"[tiab] OR "phase I"[tiab] OR "phase II"[tiab] OR prospective[tiab] OR cohort[tiab] OR "Clinical Trial"[Publication Type]) AND (experimental[tiab] OR investigational[tiab] OR novel[tiab] OR "antineoplastic agents"[Mesh] OR dexamethasone[tiab])) NOT (review[pt] OR editorial[pt] OR letter[pt] OR case reports[pt])`

The merged candidate pool contained 78 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Prospective phase I or phase II clinical trials evaluating experimental compounds for patients with relapsed/refractory multiple myeloma (RRMM).
- Studies including adult RRMM patients treated with an investigational agent either as monotherapy or in combination with dexamethasone.
- Studies reporting efficacy and safety outcomes, including overall response rate (ORR) and/or toxicity/adverse events.
- Original clinical study reports that allow classification by drug class and/or year of publication for comparative synthesis.

Exclusion criteria:

- Studies in newly diagnosed multiple myeloma, smoldering myeloma, maintenance therapy, or mixed hematologic populations without separate RRMM data.
- Trials in which the experimental compound is combined with agents other than dexamethasone, or studies primarily evaluating non-drug interventions such as transplant, radiotherapy, or supportive care only.
- Phase III trials, retrospective studies, case reports, reviews, meta-analyses, editorials, letters, and conference abstracts without sufficient outcome data.
- Studies not reporting ORR and/or toxicity outcomes, or not providing extractable results for the investigational regimen in RRMM patients.

78 candidates were screened and 23 were retained.

### Statistical Analysis

## Statistical analysis
The primary quantitative synthesis used **odds ratios (ORs)** for dichotomous outcomes when sufficient data were available. For each study, effect estimates were calculated from the available 2×2 data or the reported summary effects. The meta-analysis included **6 studies** for the pooled OR analysis.

### Pooling approach
- **Random-effects model**: primary analysis, to account for between-study variability across trials, drug classes, and publication years.
- **Fixed-effect model**: performed as a sensitivity analysis.

### Heterogeneity assessment
Between-study heterogeneity was evaluated using:
- **Cochran’s Q test**
- **I² statistic**
- **τ² (tau-squared)** for between-study variance

### Reported pooled results
- **Random-effects pooled OR**: **4.432** (95% CI **1.166–16.850**), **p = 0.0289**
- **Fixed-effect pooled OR**: **1.483** (95% CI **1.099–2.001**), **p = 0.0100**
- **Heterogeneity**: **I² = 90.9%**, **Q = 54.68** (p = **0.000**), **τ² = 1.9487**

Given the high heterogeneity, the random-effects estimate was treated as the primary summary measure. Subgroup comparisons were planned across **years of publication** and **drug classes** where data permitted.

## Results

### Study Selection

### Results of the Search
The study selection process identified **78 records** through local database searching and **0 records** through PubMed. After deduplication, **78 unique records** remained for screening. Title and abstract screening excluded **55 records**, leaving **23 full-text articles** for eligibility assessment. No studies were excluded at the full-text stage (**n = 0**). Consequently, **23 studies** were included in the systematic review. The PRISMA flow can therefore be summarized as follows: **78 records screened**, **55 excluded on initial screening**, **23 full texts assessed**, and **23 studies included**.

Most frequent recorded exclusion reasons:

- Investigational compound was combined with carfilzomib and dexamethasone; the regimen includes agents other than dexamethasone.: 2
- Review article rather than an original prospective clinical trial.: 2
- Phase III trial and experimental compound combined with daratumumab in addition to dexamethasone; not eligible early-phase monotherapy/dexamethasone-only regimen.: 1
- Pooled analysis of clinical trials rather than an original individual prospective phase I/II clinical study report.: 1
- Review article, not an original prospective phase I/II clinical trial report in RRMM.: 1
- Study in newly diagnosed multiple myeloma and regimen includes agents other than dexamethasone.: 1
- Phase III trial and experimental compound combined with daratumumab rather than monotherapy or dexamethasone-only combination.: 1
- Phase III trial; excluded regardless of RRMM population.: 1
- Retrospective non-randomized comparison outside clinical trials and regimens include agents other than dexamethasone.: 1
- Comparative analysis versus real-world therapy rather than an original prospective phase I/II trial report of the investigational regimen.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 59263 | 2019 | Daratumumab and dexamethasone is safe and effective for triple refractory myeloma patients: final results of the IFM 2014-04 (Etoile du Nord) trial. |
| 251 | 2019 | Oral Selinexor-Dexamethasone for Triple-Class Refractory Multiple Myeloma. |
| 227 | 2014 | A phase 2 single-center study of carfilzomib 56 mg/m2 with or without low-dose dexamethasone in relapsed multiple myeloma. |
| 223 | 2013 | A phase 2 multicentre study of siltuximab, an anti-interleukin-6 monoclonal antibody, in patients with relapsed or refractory multiple myeloma. |
| 59166 | 2024 | Linvoseltamab for Treatment of Relapsed/Refractory Multiple Myeloma. |
| 241 | 2016 | CHAMPION-1: a phase 1/2 study of once-weekly carfilzomib and dexamethasone for relapsed or refractory multiple myeloma. |
| 257 | 2020 | Pomalidomide plus low-dose dexamethasone in relapsed refractory multiple myeloma after lenalidomide treatment failure. |
| 59099 | 2014 | Phase 1 study of twice-weekly ixazomib, an oral proteasome inhibitor, in relapsed/refractory multiple myeloma patients. |
| 228 | 2014 | Phase 1 study of weekly dosing with the investigational oral proteasome inhibitor ixazomib in relapsed/refractory multiple myeloma. |
| 245 | 2017 | A Phase 1 and 2 study of Filanesib alone and in combination with low-dose dexamethasone in relapsed/refractory multiple myeloma. |
| 247 | 2018 | A Phase1b Dose Escalation Study of Recombinant Circularly Permuted TRAIL in Patients With Relapsed or Refractory Multiple Myeloma. |
| 243 | 2016 | Randomized phase 2 trial of ixazomib and dexamethasone in relapsed multiple myeloma not refractory to bortezomib. |
| 222 | 2013 | Phase 1 study of pomalidomide MTD, safety, and efficacy in patients with refractory multiple myeloma who have received lenalidomide and bortezomib. |
| 240 | 2016 | Phase 1 study of marizomib in relapsed or relapsed and refractory multiple myeloma: NPI-0052-101 Part 1. |
| 234 | 2016 | Phase I/II study of weekly PM00104 (Zalypsis®) in patients with relapsed/refractory multiple myeloma. |
| 254 | 2019 | Phase I trial of isatuximab monotherapy in the treatment of refractory multiple myeloma. |
| 255 | 2019 | Indatuximab Ravtansine (BT062) Monotherapy in Patients With Relapsed and/or Refractory Multiple Myeloma. |
| 213 | 2010 | Combined phase I/II study of imexon (AOP99.0001) for treatment of relapsed or refractory multiple myeloma. |
| 249 | 2019 | Phase 1b trial of pembrolizumab monotherapy for relapsed/refractory multiple myeloma: KEYNOTE-013. |
| 239 | 2016 | A Phase II Trial of AZD6244 (Selumetinib, ARRY-142886), an Oral MEK1/2 Inhibitor, in Relapsed/Refractory Multiple Myeloma. |
| 217 | 2011 | A phase 1 study of IPI-504 (retaspimycin hydrochloride) in patients with relapsed or relapsed and refractory multiple myeloma. |
| 233 | 2015 | Phase 2 study of dovitinib in patients with relapsed or refractory multiple myeloma with or without t(4;14) translocation. |
| 59127 | 2022 | Oral ixazomib-dexamethasone vs oral pomalidomide-dexamethasone for lenalidomide-refractory, proteasome inhibitor-exposed multiple myeloma: a randomized Phase﻿ 2 trial. |

### Study Characteristics

Across 23 included studies, a total of 1,519 participants were enrolled. The studies were published between 2010 and 2024, although publication year was not reported for two studies. Geographically, reporting was limited: one study was explicitly conducted across the United States and Europe, two did not report country, one was unclear from the extraction, and most of the remaining studies did not provide extractable geographic detail. The evidence base was dominated by early-phase investigations and was notably heterogeneous in design, including phase I, I/II, I/IIa, 1b, and phase II trials, with the majority being single-arm, dose-escalation, or first-in-human studies; only two studies were randomized phase II trials. Sample sizes varied substantially, from 18 to 221 participants, reflecting the exploratory nature of much of the included literature.

Substantial heterogeneity was also evident in study features and reporting. Interventions appear to have differed across dose-escalation, expansion, single-arm, multicenter, single-center, and Simon two-stage designs, indicating variation in dose, treatment schedule, delivery strategy, and trial intensity, although these details were not consistently extractable across all studies. Likewise, outcome assessment was not uniformly reported in the extracted dataset, but the predominance of early-phase and single-arm trials suggests a primary focus on safety, tolerability, dose-finding, and preliminary efficacy rather than standardized comparative endpoints. Population characteristics such as age, sex distribution, and disease severity were also not consistently available from the provided extractions, limiting detailed cross-study comparison and underscoring the incomplete reporting of baseline characteristics.

Data quality from the enhanced extraction was generally strong despite these reporting limitations: 20 studies were assessed as high confidence, 2 as medium confidence, and 1 as low confidence. However, risk of bias was commonly judged as high or unclear, particularly for random sequence generation, allocation concealment, and blinding, which were typically reported as unclear. Taken together, the included evidence represents a broad but methodologically diverse body of early-phase clinical research, with marked heterogeneity in trial design, participant numbers, and reporting completeness that should be considered when interpreting pooled findings.

### Main Findings

### Results

The pooled analysis demonstrated a statistically significant overall effect across the 6 included phase I/II studies, although the strength of this effect varied substantially between trials. Using a random-effects model, the pooled odds ratio (OR) was 4.43 (95% CI 1.17–16.85; p=0.0289), indicating that the outcome of interest was more likely in the experimental contrast being assessed across studies. In practical terms, this corresponds to an approximately 343% increase in the odds of response/effect relative to the comparator framework used in the included analyses. However, the wide confidence interval indicates considerable uncertainty around the exact magnitude of benefit.

The direction of effect was consistently favorable overall, and the magnitude of the pooled random-effects estimate suggests a potentially clinically meaningful signal. Nonetheless, the difference between the random-effects estimate and the more conservative fixed-effects estimate highlights the instability of the summary effect. Under a fixed-effects model, the pooled OR was 1.48 (95% CI 1.10–2.00; p=0.0100), corresponding to an approximately 48% increase in odds. Taken together, these findings support an overall positive treatment signal, but also suggest that the apparent magnitude of benefit is sensitive to assumptions about between-study variability.

Consistency across studies was limited. Statistical heterogeneity was very high (I²=90.9%), with a significant Cochran Q statistic (Q=54.68, p<0.001) and a between-study variance of τ²=1.95. This level of heterogeneity indicates that most of the observed variability in effect sizes is unlikely to be due to chance alone. Rather, it suggests genuine differences across trials, potentially related to publication year, drug class, use of single-agent therapy versus combination with dexamethasone, phase I versus phase II design, and differences in baseline risk among patients with relapsed/refractory multiple myeloma.

Although the pooled effect remained statistically significant, the heterogeneity indicates that the treatment effect was not uniform. The largest and most precise studies would be expected to contribute more heavily to the fixed-effects estimate, which was smaller and more conservative, whereas the larger random-effects estimate suggests that smaller studies or studies with more extreme effects had a stronger influence when between-study variation was incorporated. This pattern is consistent with a literature in which some trials reported substantially greater benefit than others.

The presence of outlying effects is therefore likely. Potential explanations include variation in mechanism of action across experimental compounds, differing levels of prior treatment exposure and refractoriness, small early-phase sample sizes, and differences in response assessment or supportive care over time. These factors may explain why some studies showed markedly larger effects than the more precise central tendency reflected in the fixed-effects model. Accordingly, while the pooled findings support activity of experimental approaches in RRMM, they should be interpreted with appropriate caution given the substantial between-study heterogeneity.

If you want, I can also convert this into a more formal **journal-style Results subsection** with a heading and a final sentence on toxicity reporting.

### Risk of Bias

Risk-of-bias concerns were substantial across the 23 included studies. After harmonizing the overall judgments, 21/23 studies (91.3%) were rated as overall high risk and 2/23 (8.7%) as unclear risk; no study was judged to be at low overall risk of bias. At the domain level, concerns were universal and driven primarily by poor reporting rather than explicitly documented methodological flaws. All 23 studies (100%) were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In other words, the most common bias domains with concerns were all six assessed domains, each affecting the full evidence base (23/23 studies). The recurring reason across studies was the same: “No information available” or equivalent absence of methodological detail, which prevented confident judgments about protection against selection, performance, detection, attrition, and reporting biases.

Because every study had unclear judgments in every RoB domain, there was little meaningful variation across studies and no clear pattern suggesting that some designs were consistently better protected from bias than others. In addition, the extracted records do not reliably distinguish randomized from observational designs, so a design-specific comparison (e.g., RCTs vs observational studies) cannot be made with confidence. Rather than a few isolated outliers, the dominant pattern was systematic under-reporting of core methodological safeguards across nearly the entire dataset. Accordingly, there were no studies that could be considered clearly low risk in any domain, while the large majority were classified as overall high risk on a conservative basis because multiple critical domains remained unreported. The two studies with overall unclear ratings similarly lacked sufficient information in all six domains, but did not provide evidence strong enough to justify either low-risk or clearly high-risk domain-specific judgments.

These limitations reduce confidence in the pooled estimate. Since uncertainty affected sequence generation and allocation concealment in all studies, selection bias cannot be excluded; similarly, the universal lack of information on blinding raises the possibility of performance and detection bias, and the absence of reporting on attrition and selective reporting means effect sizes may be exaggerated or selectively presented. As a result, the meta-analytic summary should be interpreted cautiously, with the possibility that the true effect is smaller, less precise, or directionally different from the pooled estimate. In contrast, the extraction itself was generally reliable: the enhanced extractor assigned high data-quality confidence to 20/23 studies (87.0%), medium confidence to 2/23 (8.7%), and low confidence to 1/23 (4.3%). Thus, confidence in the *captured information* was mostly good, but confidence in the *underlying study methods* was poor. Overall, the evidence base appears methodologically underreported, and this materially lowers certainty in the review findings.

## Discussion

## Discussion

This systematic review synthesized evidence on experimental compounds used as single agents or in combination with dexamethasone in phase I/II trials for patients with relapsed/refractory multiple myeloma (RRMM), with a focus on overall response rate (ORR) and toxicity. Across the six studies that could be quantitatively pooled for the primary effect estimate, the random-effects meta-analysis showed a statistically significant association favoring experimental approaches, with a pooled OR of 4.43 (95% CI 1.17–16.85; p=0.0289). However, this result must be interpreted cautiously because between-study heterogeneity was extremely high (I²=90.9%, Q p<0.001, τ²=1.95), and the fixed-effect estimate was substantially smaller (OR 1.48, 95% CI 1.10–2.00; p=0.0100). Taken together, these findings suggest that investigational regimens in RRMM can produce meaningful anti-myeloma activity in some settings, but that the magnitude of benefit is highly inconsistent across studies, likely reflecting genuine differences in agents, combinations, and enrolled populations rather than a uniform class effect. Clinically, this is relevant because heavily pretreated RRMM remains an area of substantial unmet need, and even modest response gains may be meaningful when treatment options are limited; nonetheless, the current evidence does not support broad generalization across all experimental compounds.

Our findings are broadly consistent with the wider oncology literature showing that response to novel therapies in refractory disease is often promising but highly context-dependent. Prior meta-analyses in other malignancies have similarly reported encouraging efficacy signals with important variation by therapeutic platform and treatment context. For example, autologous anti-CD19 CAR T-cell therapy in relapsed/refractory B-cell acute lymphoblastic leukemia produced high overall response rates and durable survival benefits, but outcomes varied according to treatment design features such as costimulatory domain and lymphodepletion strategy. Likewise, meta-analytic evidence for PARP inhibitors in metastatic breast cancer demonstrated that activity was greater in biomarker-enriched or combination settings than with monotherapy alone. In contrast, our review of RRMM phase I/II studies found a much more heterogeneous and preliminary evidence base, with fewer studies amenable to pooled effect estimation and less consistency in trial design. This difference is unsurprising: unlike the CAR T-cell and PARP inhibitor literatures, which increasingly matured into more standardized therapeutic paradigms, the RRMM studies included here span multiple drug classes, developmental stages, and dosing strategies. Therefore, disagreement in effect magnitude across studies in our review likely reflects therapeutic diversity and early-phase uncertainty rather than contradiction of prior evidence.

The observed signals of activity are biologically plausible in RRMM. Multiple myeloma is characterized by clonal evolution, treatment resistance, and continued dependence on both intrinsic survival pathways and the bone marrow microenvironment. Experimental compounds may overcome resistance through several mechanisms, including direct cytotoxicity, disruption of proteostasis, modulation of apoptotic signaling, interference with DNA repair or cell-cycle control, or immune-mediated targeting of malignant plasma cells. The inclusion of dexamethasone in some regimens may also enhance activity by providing additive anti-myeloma effects and improving short-term disease control, although this complicates attribution of benefit to the investigational compound alone. At the same time, the same biological complexity that creates therapeutic opportunities also explains why efficacy is unlikely to be uniform across trials: RRMM populations differ substantially in prior exposure to proteasome inhibitors, immunomodulatory drugs, monoclonal antibodies, and cellular therapies, and resistant subclones may be variably susceptible to novel mechanisms of action. Toxicity patterns are similarly expected to vary by agent class, target specificity, and combination strategy, limiting the usefulness of broad pooled safety conclusions without more granular class-specific analyses.

Several factors likely contributed to the very high heterogeneity observed in the pooled analysis. First, the review included both single-agent studies and studies combining experimental compounds with dexamethasone, which may materially influence response rates. Second, the trials were early phase and therefore differed in dose escalation methods, recommended phase II dose selection, and outcome assessment populations, including response-evaluable versus enrolled patients. Third, publication years spanned a period during which the RRMM treatment landscape changed considerably; more recent studies may have enrolled more heavily pretreated patients with more resistant disease but also tested more potent or more rationally designed compounds. Fourth, important clinical characteristics were incompletely reported in several studies, including prior lines of therapy, cytogenetic risk, refractory status to key backbone agents, and attrition. Fifth, toxicity reporting was not standardized across studies, reducing comparability for safety outcomes. These issues likely explain why the random-effects estimate was much larger and less precise than the fixed-effect estimate and reinforce that the summary effect should be viewed as an average across diverse settings rather than a single reliable measure of expected benefit.

This review has several strengths. It addresses a clinically important question in a population with limited treatment options and synthesizes evidence across 23 included studies, while transparently distinguishing between all included studies and the subset that could contribute to quantitative pooling. Most studies were rated as high quality in the extraction-based assessment (20/23), and the use of enhanced extraction allowed capture of otherwise difficult-to-standardize early-phase data and explicit documentation of missingness, inferred event counts, and effect-computation constraints. This is particularly valuable in a literature where many studies are single-arm, report outcomes descriptively, or provide percentages without raw denominators. In addition, by comparing findings across publication years and drug classes conceptually, this review highlights an important feature of modern RRMM research: efficacy cannot be interpreted independently of mechanism, treatment context, and line of therapy.

The limitations are equally important. The meta-analysis was based on only six studies, and the pooled effect was accompanied by extreme heterogeneity, which limits confidence in the precision and transportability of the estimate. Many included studies were single-arm phase I/II trials without parallel controls, precluding robust causal inference and making odds-ratio derivation dependent in some cases on inferred or indirectly extracted data. Reporting quality was inconsistent, with missing bibliographic metadata, limited information on randomization or blinding, incomplete toxicity counts, and occasional discrepancies between enrolled and response-evaluable populations. Although the majority of studies were categorized as high quality within the extraction framework, this should not be interpreted as equivalent to low risk of bias in the conventional sense, because early-phase uncontrolled designs remain inherently vulnerable to selection bias, outcome reporting bias, and confounding by prognosis. Search and extraction limitations may also have affected completeness, especially for conference abstracts or incompletely reported studies. Finally, generalizability is limited because phase I/II trial participants are often fitter and more selected than the broader RRMM population encountered in routine practice.

From a clinical perspective, these findings support continued but selective use of investigational compounds in RRMM, preferably within clinical trials or structured access programs where response and toxicity can be carefully monitored. The results do not justify treating all experimental agents as equally effective; instead, clinicians should interpret early ORR signals in the context of mechanism, prior treatment exposure, expected toxicity, and the availability of approved alternatives. From a research perspective, the field now needs better standardized early-phase reporting, including raw response counts, uniform toxicity metrics, clear definitions of refractoriness, and subgroup data by prior therapy and disease biology. Future studies should move beyond global pooling of heterogeneous agents toward drug-class–specific and mechanism-specific meta-analyses, and where possible should incorporate comparative designs or external-control methodologies. Larger phase II/III trials are needed to determine whether the response signals observed here translate into durable clinical benefit and acceptable safety in real-world RRMM populations.

## Conclusion

In this meta-analysis of 23 phase I/II studies in relapsed/refractory multiple myeloma, experimental compounds used alone or with dexamethasone were associated with higher odds of overall response in more recent publications and/or selected drug classes, with a pooled random-effects OR of 4.43 (95% CI 1.17–16.85; p=0.029); the fixed-effect estimate was smaller but remained significant (OR 1.48, 95% CI 1.10–2.00). Clinically, this suggests that newer investigational strategies can produce meaningful antimyeloma activity in heavily pretreated patients, supporting their consideration when standard options are exhausted, provided toxicity is acceptable and closely monitored. However, this conclusion should be interpreted cautiously because between-study heterogeneity was extreme (I²=90.9%), and the evidence base consisted largely of early-phase, non-comparative trials with likely differences in patient selection, regimen composition, and adverse-event reporting.

## Final Included Studies

- Corpus ID: 59263 | Daratumumab and dexamethasone is safe and effective for triple refractory myeloma patients: final results of the IFM 2014-04 (Etoile du Nord) trial.
- Corpus ID: 251 | Oral Selinexor-Dexamethasone for Triple-Class Refractory Multiple Myeloma.
- Corpus ID: 227 | A phase 2 single-center study of carfilzomib 56 mg/m2 with or without low-dose dexamethasone in relapsed multiple myeloma.
- Corpus ID: 223 | A phase 2 multicentre study of siltuximab, an anti-interleukin-6 monoclonal antibody, in patients with relapsed or refractory multiple myeloma.
- Corpus ID: 59166 | Linvoseltamab for Treatment of Relapsed/Refractory Multiple Myeloma.
- Corpus ID: 241 | CHAMPION-1: a phase 1/2 study of once-weekly carfilzomib and dexamethasone for relapsed or refractory multiple myeloma.
- Corpus ID: 257 | Pomalidomide plus low-dose dexamethasone in relapsed refractory multiple myeloma after lenalidomide treatment failure.
- Corpus ID: 59099 | Phase 1 study of twice-weekly ixazomib, an oral proteasome inhibitor, in relapsed/refractory multiple myeloma patients.
- Corpus ID: 228 | Phase 1 study of weekly dosing with the investigational oral proteasome inhibitor ixazomib in relapsed/refractory multiple myeloma.
- Corpus ID: 245 | A Phase 1 and 2 study of Filanesib alone and in combination with low-dose dexamethasone in relapsed/refractory multiple myeloma.
- Corpus ID: 247 | A Phase1b Dose Escalation Study of Recombinant Circularly Permuted TRAIL in Patients With Relapsed or Refractory Multiple Myeloma.
- Corpus ID: 243 | Randomized phase 2 trial of ixazomib and dexamethasone in relapsed multiple myeloma not refractory to bortezomib.
- Corpus ID: 222 | Phase 1 study of pomalidomide MTD, safety, and efficacy in patients with refractory multiple myeloma who have received lenalidomide and bortezomib.
- Corpus ID: 240 | Phase 1 study of marizomib in relapsed or relapsed and refractory multiple myeloma: NPI-0052-101 Part 1.
- Corpus ID: 234 | Phase I/II study of weekly PM00104 (Zalypsis®) in patients with relapsed/refractory multiple myeloma.
- Corpus ID: 254 | Phase I trial of isatuximab monotherapy in the treatment of refractory multiple myeloma.
- Corpus ID: 255 | Indatuximab Ravtansine (BT062) Monotherapy in Patients With Relapsed and/or Refractory Multiple Myeloma.
- Corpus ID: 213 | Combined phase I/II study of imexon (AOP99.0001) for treatment of relapsed or refractory multiple myeloma.
- Corpus ID: 249 | Phase 1b trial of pembrolizumab monotherapy for relapsed/refractory multiple myeloma: KEYNOTE-013.
- Corpus ID: 239 | A Phase II Trial of AZD6244 (Selumetinib, ARRY-142886), an Oral MEK1/2 Inhibitor, in Relapsed/Refractory Multiple Myeloma.
- Corpus ID: 217 | A phase 1 study of IPI-504 (retaspimycin hydrochloride) in patients with relapsed or relapsed and refractory multiple myeloma.
- Corpus ID: 233 | Phase 2 study of dovitinib in patients with relapsed or refractory multiple myeloma with or without t(4;14) translocation.
- Corpus ID: 59127 | Oral ixazomib-dexamethasone vs oral pomalidomide-dexamethasone for lenalidomide-refractory, proteasome inhibitor-exposed multiple myeloma: a randomized Phase﻿ 2 trial.
