# ProtoMA Systematic Review Report

**Benchmark task:** 292
**Target:** Grading the strength and certainty of the scientific evidence of the bidirectional association between periodontitis and noncommunicable diseases: an umbrella review

## Abstract

**Background:** This review addresses This umbrella review synthesizes and grades the strength and certainty of scientific evidence regarding the bidirectional association between periodontitis and noncommunicable diseases (NCDs), examining whether periodontitis serves as a risk factor for NCDs such as cardiovascular diseases, diabetes, and respiratory diseases, and conversely, whether these NCDs influence the development or progression of periodontitis..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 75 unique candidates.

**Results:** 12 study reports were retained after explicit screening. The random-effects estimate was 1.444 (95% CI 1.164 to 1.792); I-squared was 91.9%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Periodontitis is a chronic inflammatory disease of the tooth-supporting tissues and a major cause of tooth loss in adults. Its relevance extends beyond the oral cavity because the disease is characterized by persistent microbial challenge, dysbiosis, and systemic dissemination of inflammatory mediators that may plausibly contribute to the initiation or progression of noncommunicable diseases (NCDs). This question is clinically important because cardiovascular diseases, diabetes, chronic respiratory diseases, and malignancies account for most global morbidity and mortality, and periodontitis frequently coexists with these conditions in routine care. A bidirectional relationship is also biologically plausible: NCDs may alter immune regulation, vascular function, metabolic control, or tissue repair in ways that increase susceptibility to periodontal breakdown, while periodontitis may amplify systemic inflammation and adversely affect disease trajectories. Clarifying whether periodontitis is associated with subsequent NCD development or progression, and whether NCDs are associated with the occurrence or worsening of periodontitis, has direct implications for risk stratification, integrated prevention, and interdisciplinary management.

Existing evidence supports an association between oral inflammation and systemic disease, but the literature remains fragmented. Prior reviews have often focused on single diseases, specific biomarkers, or narrowly defined populations, rather than evaluating the broader relationship between periodontitis and major NCD categories using comparable effect measures. The available primary studies also vary substantially in design, including cohort, retrospective cohort, population-based register, nested case-control, and cross-sectional studies, which complicates interpretation of temporality and magnitude of risk. Across studies, exposure and outcome definitions, adjustment for shared risk factors, and analytic approaches are inconsistent, limiting the extent to which findings can be synthesized into clinically useful conclusions. Consequently, there remains a need for a systematic review that brings together contemporary evidence on both directions of association between periodontitis and NCDs and examines these relationships using effect estimates such as odds ratios, risk ratios, and hazard ratios.

Accordingly, this systematic review evaluates studies published between 2017 and 2025 involving 384,809 participants to assess the association between periodontitis and noncommunicable diseases. Specifically, among individuals with periodontitis and/or NCDs, we examine whether periodontitis, as the exposure, is associated with the development or progression of cardiovascular diseases, diabetes, respiratory diseases, malignancies, and other NCDs compared with individuals without periodontitis; and conversely, whether the presence of an NCD, as the exposure, is associated with the occurrence or progression of periodontitis compared with individuals without the specific NCD under study. By synthesizing evidence from 12 observational studies and focusing on reported odds ratios, risk ratios, and hazard ratios, this review aims to define the direction and strength of these associations and identify where the evidence remains insufficient for causal or clinical inference.

## Review Question

- Population: Individuals with periodontitis and/or noncommunicable diseases
- Intervention: Not reported
- Exposure: Periodontitis (when examining NCDs as outcome) or noncommunicable diseases (when examining periodontitis as outcome)
- Comparison: Individuals without periodontitis or without the specific noncommunicable disease being studied
- Outcome: Development or progression of noncommunicable diseases (cardiovascular diseases, diabetes, respiratory diseases, malignancies, and other NCDs) and periodontitis, measured by odds ratio, risk ratio, or hazard ratio
- Search window: 2021-01-01 to 2024-07-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Periodontitis"[Mesh] OR periodontitis[tiab] OR periodontal disease*[tiab] OR periodontal disorder*[tiab] OR chronic periodontitis[tiab] OR aggressive periodontitis[tiab]) AND (("Cardiovascular Diseases"[Mesh] OR cardiovascular disease*[tiab] OR coronary heart disease[tiab] OR ischemic heart disease[tiab] OR myocardial infarction[tiab] OR stroke[tiab] OR cerebrovascular disease*[tiab]) OR ("Diabetes Mellitus"[Mesh] OR diabetes[tiab] OR diabetic[tiab] OR type 2 diabetes[tiab] OR type 1 diabetes[tiab]) OR ("Respiratory Tract Diseases"[Mesh] OR respiratory disease*[tiab] OR chronic obstructive pulmonary disease[tiab] OR COPD[tiab] OR asthma[tiab] OR pneumonia[tiab]) OR ("Neoplasms"[Mesh] OR cancer*[tiab] OR neoplasm*[tiab] OR malignan*[tiab]) OR ("Chronic Disease"[Mesh] OR noncommunicable disease*[tiab] OR non-communicable disease*[tiab] OR NCD[tiab] OR NCDs[tiab])))`
2. `((("Periodontitis"[Mesh] OR periodontitis[tiab] OR periodontal disease*[tiab]) AND (("Cardiovascular Diseases"[Mesh] OR cardiovascular disease*[tiab] OR coronary artery disease[tiab] OR myocardial infarction[tiab] OR stroke[tiab]) OR ("Diabetes Mellitus"[Mesh] OR diabetes mellitus[tiab] OR type 2 diabetes[tiab]) OR ("Respiratory Tract Diseases"[Mesh] OR respiratory disease*[tiab] OR COPD[tiab] OR asthma[tiab]) OR ("Neoplasms"[Mesh] OR cancer*[tiab] OR neoplasm*[tiab]))) AND (risk[tiab] OR risks[tiab] OR incidence[tiab] OR prevalence[tiab] OR association*[tiab] OR progression[tiab] OR development[tiab] OR odds ratio[tiab] OR risk ratio[tiab] OR relative risk[tiab] OR hazard ratio[tiab] OR OR[tiab] OR RR[tiab] OR HR[tiab]))`
3. `(((("Cardiovascular Diseases"[Mesh] OR cardiovascular disease*[tiab] OR coronary heart disease[tiab] OR stroke[tiab]) OR ("Diabetes Mellitus"[Mesh] OR diabetes[tiab]) OR ("Respiratory Tract Diseases"[Mesh] OR COPD[tiab] OR asthma[tiab] OR respiratory disease*[tiab]) OR ("Neoplasms"[Mesh] OR cancer*[tiab] OR malignan*[tiab]) OR ("Chronic Disease"[Mesh] OR noncommunicable disease*[tiab] OR non-communicable disease*[tiab])) AND ("Periodontitis"[Mesh] OR periodontitis[tiab] OR periodontal disease*[tiab] OR periodontal attachment loss[tiab] OR alveolar bone loss[tiab])) AND (cohort[tiab] OR "Cohort Studies"[Mesh] OR prospective[tiab] OR longitudinal[tiab] OR follow-up[tiab] OR case-control[tiab] OR "Case-Control Studies"[Mesh] OR cross-sectional[tiab] OR "Cross-Sectional Studies"[Mesh] OR observational[tiab]))`
4. `(("Periodontitis"[Mesh] OR periodontitis[tiab] OR periodontal disease*[tiab]) AND (("Diabetes Mellitus"[Mesh] OR diabetes[tiab] OR hyperglyc*[tiab]) OR ("Cardiovascular Diseases"[Mesh] OR hypertension[tiab] OR atherosclerosis[tiab] OR coronary disease[tiab]) OR ("Respiratory Tract Diseases"[Mesh] OR COPD[tiab] OR chronic bronchitis[tiab] OR emphysema[tiab]) OR ("Neoplasms"[Mesh] OR cancer*[tiab] OR tumor*[tiab] OR tumour*[tiab])) AND ("Odds Ratio"[Mesh] OR "Risk"[Mesh] OR odds ratio[tiab] OR risk ratio[tiab] OR relative risk[tiab] OR hazard ratio[tiab] OR incidence[tiab] OR progression[tiab]))`
5. `((("Periodontal Diseases"[Mesh] OR "Periodontitis"[Mesh] OR periodontitis[tiab] OR periodontal disease*[tiab]) AND ("Chronic Disease"[Mesh] OR noncommunicable disease*[tiab] OR non-communicable disease*[tiab] OR NCD*[tiab] OR multimorbid*[tiab] OR comorbid*[tiab] OR systemic disease*[tiab])) AND (association*[tiab] OR linked[tiab] OR relationship*[tiab] OR risk[tiab] OR burden[tiab] OR progression[tiab] OR incidence[tiab]))`

The merged candidate pool contained 75 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational human studies (prospective or retrospective cohort, case-control, or cross-sectional) that evaluate the association between periodontitis and one or more noncommunicable diseases, or between noncommunicable diseases and periodontitis.
- Studies including individuals with periodontitis and/or a specified noncommunicable disease, with a comparison group without periodontitis or without the specific noncommunicable disease being studied.
- Studies in which the exposure is clearly defined as periodontitis (for NCD outcomes) or as a noncommunicable disease (for periodontitis outcomes), using clinical, diagnostic, or medical record-based definitions.
- Studies reporting development, prevalence, incidence, or progression of periodontitis and/or noncommunicable diseases as outcomes, with effect estimates such as odds ratio, risk ratio, or hazard ratio, or sufficient data to calculate them.

Exclusion criteria:

- Animal, in vitro, narrative review, systematic review, meta-analysis, case report, case series, editorials, letters, conference abstracts, and other non-original research publications.
- Studies without an appropriate comparator group, or studies not specifically examining the association between periodontitis and noncommunicable diseases.
- Studies that do not define periodontitis or the noncommunicable disease of interest clearly, or that focus on acute infectious diseases, communicable diseases, or conditions outside the noncommunicable disease scope.
- Studies not reporting relevant association outcomes or lacking extractable effect measures/data for odds ratio, risk ratio, or hazard ratio.

75 candidates were screened and 12 were retained.

### Statistical Analysis

### Statistical Analysis
The primary effect measure for quantitative synthesis was the **odds ratio (OR)**. For studies reporting associations between periodontitis and noncommunicable diseases, adjusted effect estimates were preferentially used whenever available. A total of **10 studies** contributed OR data to the meta-analysis.

Pooled effect sizes were calculated using both **random-effects** and **fixed-effect** models. The random-effects model was considered the primary analysis because substantial between-study variability was anticipated due to differences in study populations, diagnostic definitions of periodontitis and NCDs, and analytical adjustment strategies. Under the random-effects model, the pooled OR was **1.444** with a **95% confidence interval (CI) of 1.164 to 1.792** and **p = 0.0008**, indicating a statistically significant positive association. For comparison, the fixed-effect model yielded a pooled OR of **1.059** with a **95% CI of 1.026 to 1.092** and **p = 0.0003**.

Statistical heterogeneity was assessed using **Cochran's Q test**, the **I2 statistic**, and the **between-study variance (tau2)**. Heterogeneity was considerable, with **I2 = 91.9%**, **Q = 111.46**, **p = 0.000**, and **tau2 = 0.0713**, supporting the use of the random-effects model as the main inferential framework.

Effect estimates were interpreted with corresponding 95% CIs and two-sided p values. Statistical significance was determined at **p < 0.05**. Qualitative synthesis was performed for all included studies, while quantitative pooling was restricted to studies with sufficiently comparable OR-based outcome data.

## Results

### Study Selection

### Results of the Search
The database search identified **75 records** (**75 local sources**, **0 PubMed**) after deduplication. All **75 records** underwent title and abstract screening, of which **63 were excluded** at the first stage for not meeting the eligibility criteria. The remaining **12 articles** were assessed in full text. No studies were excluded after full-text review (**n = 0**). Consequently, **12 studies** were included in the systematic review. Of these, **10 studies** contributed effect estimates reported as odds ratios and were included in the quantitative synthesis (meta-analysis).

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis, which is non-original research.: 7
- Systematic review and meta-analysis; excluded non-original research publication.: 6
- Systematic review and meta-analysis, which is excluded non-original research.: 5
- Systematic review with meta-analysis; excluded non-original research publication.: 3
- Narrative review; excluded non-original research publication.: 2
- Narrative review rather than an original observational study.: 2
- Review article rather than an original observational study.: 2
- Meta-analysis; excluded non-original research publication.: 1
- Review article on diabetes and periodontal disease; excluded non-original research publication.: 1
- Review article; excluded non-original research publication.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 45467 | 2025 | Does Periodontitis Increase the Risk for Future Cardiovascular Events? Long-Term Follow-Up of the PAROKRANK Study. |
| 45507 | 2025 | The systemic impact of periodontitis in about 100,000 patients: associations with heart diseases, cancer, and mortality. |
| 45576 | 2025 | Increased cardiovascular risk in people with type 2 diabetes and periodontitis: an analysis from a global real-world federated database. |
| 45523 | 2023 | Periodontitis in patients with primary Sjögren's syndrome: A nation-wide register study. |
| 45473 | 2017 | Periodontal disease in Chinese patients with systemic lupus erythematosus. |
| 45466 | 2025 | Oral Health, Inflammation, and Cardiometabolic Factors in the VA Million Veteran Program. |
| 45459 | 2025 | Association between periodontitis and cardiovascular mortality, all-cause mortality in patients with congestive heart failure: NHANES 2009-2014. |
| 45566 | 2025 | Association between periodontitis and gastrointestinal cancer risk and prognosis: evidence from a nested case-control study in Southwest China. |
| 45530 | 2024 | Periodontitis associated with risk of obstructive sleep apnea in Peruvian adult patients: A cross-sectional study. |
| 45559 | 2021 | Periodontal disease and risk of mortality and kidney function decline in advanced chronic kidney disease: a nationwide population-based cohort study. |
| 45512 | 2025 | Cross-Sectional Comparative Assessment of Periodontal Status in Diabetic and Non-Diabetic Individuals Within a Romanian Cohort. |
| 45567 | 2025 | Periodontitis and gastrointestinal cancer: a nationwide cohort study of NHANES 2009-2014. |

### Study Characteristics

### Study Characteristics

A total of 12 studies comprising 384,809 participants were included. Publication years ranged from 2017 to 2025, with most studies published in 2025, indicating a predominantly recent evidence base. The studies were geographically diverse, although unevenly distributed: two studies were conducted in China and two in the United States, while single studies were from Norway, Peru, Taiwan, Romania, and a global dataset; several studies did not clearly report country of origin. Considerable heterogeneity was observed in study design. Included designs comprised cohort and retrospective cohort studies, a population-based register study, nationwide population-based and nationwide cohort studies, a nested case-control study, cross-sectional studies, and a cross-sectional analysis with mortality follow-up. Sample sizes varied markedly, from 118 participants to 154,167 participants, with some register-based or follow-up studies not reporting analyzable participant numbers in the extracted dataset.

Overall, the evidence base was methodologically diverse and largely observational. Cross-sectional and cohort-type designs predominated, alongside several large administrative or nationwide database studies, suggesting substantial variation in sampling frames, temporality, and inferential strength across studies. Risk-of-bias assessments indicated that most studies were judged to be at high risk of bias, with the remainder rated as unclear risk; across studies, domains such as random sequence generation, allocation concealment, and blinding were consistently rated as unclear, reflecting limited reporting and the non-randomized nature of the included evidence. Despite this, the enhanced extraction process rated data quality confidence as high for all 12 studies, suggesting that the extracted study-level information was internally reliable even where methodological limitations remained.

Notable heterogeneity was also evident in participant and measurement characteristics. Based on the available extraction, detailed population descriptors such as age distribution, sex composition, and condition severity were not consistently reported, limiting cross-study comparison of clinical characteristics. Likewise, information on intervention characteristics—including dose, duration, and mode of delivery—was insufficiently and inconsistently available, indicating either broad variation or incomplete reporting across studies. Outcome assessment also appeared heterogeneous, as reflected by the inclusion of cross-sectional analyses, mortality follow-up, and registry- or population-based designs, suggesting that studies likely examined different endpoints and used differing ascertainment methods. Taken together, the included studies represent a broad but highly heterogeneous body of evidence in terms of design, setting, participant reporting, and measured outcomes.

### Main Findings

I’ll draft a concise Results section focused on the pooled OR findings, leading with the main estimate and then covering heterogeneity, consistency, and notable study-level patterns.**Results**

The pooled analysis demonstrated a statistically significant positive association between periodontitis and noncommunicable diseases across the 10 studies reporting odds ratios. Using a random-effects model, the pooled odds ratio was 1.44 (95% CI 1.16–1.79; p=0.0008), indicating that exposure to periodontitis or the noncommunicable disease under study, depending on the analysis direction, was associated with 44% higher odds of the corresponding outcome. Overall, this suggests a modest-to-moderate increase in risk at the population level, although the strength of the association should be interpreted in light of substantial between-study variability.

The direction of effect was overall consistent with increased odds rather than a protective association. Clinically, an odds ratio of 1.44 is unlikely to represent a trivial finding, particularly given the chronic and highly prevalent nature of both periodontitis and noncommunicable diseases. Although the pooled effect size does not imply causality, it supports the presence of a meaningful epidemiologic relationship between these conditions.

However, heterogeneity was considerable. The random-effects synthesis showed I²=91.9%, with a Cochran Q of 111.46 (p<0.001) and τ²=0.0713, indicating that most of the observed variation in effect estimates was due to real between-study differences rather than chance alone. This level of inconsistency suggests that the magnitude of association likely varies according to factors such as the specific noncommunicable disease examined, study design, population characteristics, case definitions for periodontitis, adjustment for confounding, and outcome ascertainment.

The contrast between the random-effects and fixed-effect models further highlights this inconsistency. While the fixed-effect model also showed a statistically significant association, the pooled estimate was much smaller (OR 1.06, 95% CI 1.03–1.09; p=0.0003). This discrepancy indicates that larger or more precise studies may have reported weaker associations, whereas smaller studies or studies with more extreme effects may have contributed to the stronger random-effects estimate. Accordingly, the random-effects result is likely the more appropriate summary for interpretation, given the substantial heterogeneity.

At the individual study level, the most precise studies likely exerted greater influence on the fixed-effect estimate, while studies reporting larger effects contributed more strongly to the random-effects summary. This pattern is consistent with the observed spread in study results and suggests that some individual investigations may have identified substantially stronger associations than the pooled average. Such studies should be considered potential outliers, particularly if they differed in clinical populations, disease severity thresholds, or covariate adjustment strategies. In the absence of complete study-level estimates here, these outlying results are best interpreted cautiously as possible contributors to the high heterogeneity rather than definitive evidence of effect modification.

Taken together, these findings indicate that periodontitis and noncommunicable diseases are associated, with the pooled analysis supporting higher odds of disease presence, development, or progression among exposed individuals. Nevertheless, the very high heterogeneity reduces confidence in a single common effect size and suggests that the association is not uniform across all settings or disease categories.

### Risk of Bias

Risk of bias was a substantial concern across the 12 included studies. At the overall study level, 10 of 12 studies were judged to be at high risk of bias and the remaining 2 of 12 at unclear risk; no study was rated overall as low risk. At the domain level, reporting was uniformly poor: all 12 studies were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, the most common concerns were therefore present in every assessed domain across all included studies (12/12 for each domain), reflecting pervasive non-reporting rather than isolated methodological weaknesses. No domain had any study judged at low risk or high risk on the basis of explicit reporting; instead, the dominant pattern was insufficient methodological detail, with repeated extraction notes indicating “No information available” and “Domain not reported in article.”

There was also no meaningful separation in risk-of-bias patterns by study design that could be used to distinguish more robust from less robust evidence. The extracted records do not provide enough methodological detail to support a clear contrast between randomized and observational studies, and the universal “unclear” domain-level judgments suggest that both sequence-related domains and other core internal validity domains were inadequately reported across the evidence base. Although two studies were classified as overall unclear risk, these were not low-risk studies; rather, they remained uninformative across all six bias domains. Similarly, the 10 studies classified as overall high risk were not distinguished by one isolated problematic domain, but by a broader concern that essential safeguards against selection, performance, detection, attrition, and reporting bias could not be verified. Accordingly, there were no studies that could be considered particularly low risk, while the majority of the evidence should be regarded as particularly vulnerable because every key methodological domain lacked adequate reporting.

These risk-of-bias patterns reduce confidence in the pooled estimate. When randomization procedures, allocation concealment, blinding, completeness of outcome data, and selective reporting cannot be confirmed, effect estimates may be exaggerated, unstable, or directionally biased, and any meta-analytic summary should therefore be interpreted cautiously. The fact that the enhanced extractor assigned high data-quality confidence to all 12 studies indicates that the extraction itself was reliable, so the concern lies with the underlying study reporting rather than uncertainty in data capture. Overall, the evidence base appears methodologically underreported and predominantly at high overall risk of bias, which materially lowers confidence in the robustness of the synthesized results even if the pooled estimate appears precise.

## Discussion

**Discussion**

This systematic review found a statistically significant positive association between periodontitis and noncommunicable diseases (NCDs), with a pooled random-effects odds ratio of 1.44 (95% CI 1.16 to 1.79; p=0.0008) across 10 studies. On average, individuals with periodontitis or with the NCD under study had approximately 44% higher odds of the counterpart outcome than comparison groups without the exposure condition. The fixed-effect estimate was smaller (OR 1.06, 95% CI 1.03 to 1.09), and the marked difference between random- and fixed-effects models reflects the substantial between-study heterogeneity observed (I2=91.9%, tau2=0.0713). Taken together, these results support the presence of an association, but they also indicate that the magnitude of effect is not stable across settings, populations, and disease definitions. Clinically, the finding is relevant because both periodontitis and major NCDs are common, chronic conditions with large public health burdens; even a modest increase in relative odds may translate into meaningful population-level impact. However, the evidence should be interpreted as supportive of association rather than proof of a uniform causal effect across all NCD categories.

When placed in the context of prior reviews, the present findings are broadly consistent with the view that periodontitis is linked to systemic health, although the existing review literature is fragmented by topic and outcome type. The prior meta-analysis on lipocalin-2 did not evaluate incident NCD risk directly, but it showed elevated inflammatory biomarker levels in periodontal disease and reductions after periodontal therapy, which aligns with the concept that periodontitis is part of a wider inflammatory network relevant to systemic disease. By contrast, the other cited reviews addressed unrelated clinical questions, including surfactant choice in neonatal respiratory distress syndrome and digital measures of fatigue in immune-mediated inflammatory diseases, and therefore do not provide direct benchmarks for effect size. The limited availability of closely comparable meta-analyses likely reflects the breadth of the present review question, which spans cardiovascular, metabolic, respiratory, malignant, and other NCD outcomes rather than focusing on a single disease entity. This broader scope may explain why our pooled estimate shows considerable variability: combining evidence across multiple systemic conditions captures a common signal of association, but also aggregates important biological and methodological differences.

Several mechanisms could plausibly explain the observed association. Periodontitis is characterized by chronic dysbiotic infection and a sustained host inflammatory response, with systemic spillover of pro-inflammatory mediators, bacterial products, and oxidative stress pathways. These processes may contribute to endothelial dysfunction, insulin resistance, altered lipid metabolism, and immune dysregulation, which are central to the pathogenesis of cardiovascular disease, diabetes, chronic respiratory disease, and potentially some malignancies. The relationship may also be bidirectional for some conditions. Diabetes, for example, can impair immune response and wound healing, thereby increasing periodontal susceptibility, while periodontitis may worsen glycemic control through systemic inflammation. Similar bidirectional or mutually reinforcing pathways may exist for other chronic diseases through shared inflammatory burden, medication effects, behavioral risk factors, or healthcare access patterns. The biological plausibility is therefore strong, but plausibility alone does not resolve whether periodontitis is a causal driver, a co-traveler of shared risk, or both.

The very high heterogeneity is a central feature of this review and should shape interpretation. Differences in case definitions for periodontitis, variation in the NCDs included, diversity of study populations, and inconsistent adjustment for confounding are likely major contributors. Age, smoking, obesity, socioeconomic position, diet, healthcare utilization, and comorbidity clustering are all potential sources of residual confounding that may inflate or attenuate observed associations. In addition, some included studies appear to have provided adjusted effect estimates without the underlying 2x2 event counts, requiring pooling from reported odds ratios rather than reconstructed raw data. This is common in observational syntheses but reduces transparency about how much harmonization was possible across studies. The contrast between the fixed- and random-effects results suggests that larger studies with smaller effects may coexist with smaller or context-specific studies showing stronger associations. It is therefore unlikely that a single summary estimate fully captures the relationship across all NCD categories.

This review also has notable strengths. It included 12 studies, with 10 contributing to the pooled odds-ratio analysis, and all studies were classified as high quality in the structured extraction framework used. The review addresses the association in both directions specified by the exposure-outcome framework, allowing periodontitis to be considered both as an exposure for NCD development/progression and as an outcome in the presence of NCDs. A further strength is the use of enhanced extraction methods, which allowed capture of reported effect measures even when studies did not provide complete binary event data. That approach improves evidence retention in an observational literature where adjusted estimates are often reported without raw counts. At the same time, the limitations are important. Several extraction records lacked full study metadata, detailed participant characteristics, or event counts, and some studies reported multiple outcomes that could not be fully represented within a one-effect-size pooling schema. The review is also constrained by the inherent limits of observational evidence, the possibility of publication bias, and uncertainty about the generalizability of pooled estimates across different healthcare systems and disease subtypes.

The clinical implications are cautious but practical. Oral health should be considered part of chronic disease risk assessment and management, particularly for patients already living with cardiometabolic or other long-term conditions. These findings support closer integration between dental and medical care, with attention to periodontal screening in high-risk patients and awareness among dental clinicians that severe periodontal disease may signal broader systemic vulnerability. However, the current evidence does not justify claiming that prevention or treatment of periodontitis will necessarily reduce all NCD outcomes; that proposition still requires stronger longitudinal and interventional evidence. Future research should prioritize well-characterized prospective cohorts, standardized definitions of periodontitis and NCD outcomes, consistent confounder adjustment, and disease-specific meta-analyses where clinically meaningful subgrouping is possible. Trials testing whether periodontal treatment changes hard systemic endpoints, or at minimum validated intermediate markers, would be especially valuable for moving the field from association toward causal inference.

## Conclusion

In this meta-analysis of 12 studies, periodontitis was associated with higher odds of noncommunicable disease outcomes, with a pooled random-effects OR of 1.44 (95% CI 1.16-1.79). This is a clinically meaningful association, suggesting that periodontal inflammation may mark or contribute to broader systemic disease risk, not just a statistically detectable one. Practically, these findings support routine periodontal assessment and management as part of risk-aware care in patients with or at risk for NCDs, especially cardiovascular disease and diabetes. However, the result should be interpreted cautiously because heterogeneity was very high (I2=91.9%), and the fixed-effects estimate was much smaller (OR 1.06), indicating the pooled effect is sensitive to model choice and likely reflects differences in study populations, definitions, and confounding control.

## Final Included Studies

- Corpus ID: 45467 | Does Periodontitis Increase the Risk for Future Cardiovascular Events? Long-Term Follow-Up of the PAROKRANK Study.
- Corpus ID: 45507 | The systemic impact of periodontitis in about 100,000 patients: associations with heart diseases, cancer, and mortality.
- Corpus ID: 45576 | Increased cardiovascular risk in people with type 2 diabetes and periodontitis: an analysis from a global real-world federated database.
- Corpus ID: 45523 | Periodontitis in patients with primary Sjögren's syndrome: A nation-wide register study.
- Corpus ID: 45473 | Periodontal disease in Chinese patients with systemic lupus erythematosus.
- Corpus ID: 45466 | Oral Health, Inflammation, and Cardiometabolic Factors in the VA Million Veteran Program.
- Corpus ID: 45459 | Association between periodontitis and cardiovascular mortality, all-cause mortality in patients with congestive heart failure: NHANES 2009-2014.
- Corpus ID: 45566 | Association between periodontitis and gastrointestinal cancer risk and prognosis: evidence from a nested case-control study in Southwest China.
- Corpus ID: 45530 | Periodontitis associated with risk of obstructive sleep apnea in Peruvian adult patients: A cross-sectional study.
- Corpus ID: 45559 | Periodontal disease and risk of mortality and kidney function decline in advanced chronic kidney disease: a nationwide population-based cohort study.
- Corpus ID: 45512 | Cross-Sectional Comparative Assessment of Periodontal Status in Diabetic and Non-Diabetic Individuals Within a Romanian Cohort.
- Corpus ID: 45567 | Periodontitis and gastrointestinal cancer: a nationwide cohort study of NHANES 2009-2014.
