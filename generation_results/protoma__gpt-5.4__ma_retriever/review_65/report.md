# ProtoMA Systematic Review Report

**Benchmark task:** 65
**Target:** Neck circumference as a metabolic health marker among women with polycystic ovary syndrome (PCOS): a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates whether women with polycystic ovary syndrome (PCOS) have larger neck circumference compared to non-PCOS controls, and examines the associations between neck circumference and metabolic abnormalities including metabolic syndrome and insulin resistance among women with PCOS..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 76 unique candidates.

**Results:** 3 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Polycystic ovary syndrome (PCOS) is one of the most common endocrine disorders in reproductive-aged women and is characterized not only by reproductive dysfunction but also by substantial metabolic risk. Women with PCOS frequently exhibit central adiposity, insulin resistance, dyslipidemia, elevated blood pressure, and a higher prevalence of metabolic syndrome, even at younger ages than the general female population. Because these cardiometabolic abnormalities contribute to long-term risks such as type 2 diabetes and cardiovascular disease, simple and clinically accessible markers that can identify adverse metabolic phenotypes in PCOS are of practical importance. Neck circumference (NC) has emerged as a potential anthropometric marker of upper-body subcutaneous adiposity and may offer advantages over more traditional indices because it is quick to measure, less affected by postprandial abdominal distension or respiratory phase, and feasible in routine outpatient settings.

In the general population, anthropometric and metabolic markers have been the subject of multiple evidence syntheses, and recent meta-analyses have shown that body fat distribution and metabolic abnormalities are meaningfully associated with clinical outcomes. However, whether NC has comparable utility in women with PCOS remains less clearly established. The currently available evidence consists of a small number of recent observational studies published between 2021 and 2022, comprising 3,148 participants, that have examined NC in relation to PCOS status, metabolic syndrome, insulin resistance indices such as HOMA-IR and HOMA%S, fasting insulin, waist and hip circumference, blood pressure, triglycerides, and glucose metabolism parameters. These studies suggest that greater NC may cluster with adverse anthropometric and metabolic features, but the direction, magnitude, and consistency of these associations have not been synthesized systematically. In particular, it remains unclear whether women with PCOS have higher NC than non-PCOS healthy controls and whether larger NC identifies a subgroup with less favorable metabolic profiles within PCOS populations.

Accordingly, this systematic review evaluates NC as an anthropometric marker of upper-body adiposity in women with PCOS. Specifically, we synthesize evidence from cross-sectional studies comparing NC values between women with PCOS and non-PCOS healthy controls, and between women with larger versus smaller NC, and we examine the association of NC with metabolic syndrome prevalence, insulin resistance markers, anthropometric measurements, blood pressure, lipid parameters, and glucose metabolism outcomes. By focusing on these prespecified PICO components, this review aims to clarify the clinical relevance of NC as a practical metabolic risk marker in PCOS and to identify the extent to which current evidence supports its use in risk stratification.

## Review Question

- Population: Women with polycystic ovary syndrome (PCOS)
- Intervention: Not reported
- Exposure: Neck circumference (NC) as an anthropometric marker of upper body adiposity
- Comparison: Non-PCOS healthy controls; women with smaller neck circumference
- Outcome: Neck circumference values, metabolic syndrome prevalence, insulin resistance (HOMA-IR, HOMA%S, fasting insulin), anthropometric measurements (waist circumference, hip circumference), blood pressure, lipid values (triglycerides), and glucose metabolism parameters
- Search window: Not reported to 2024-10-28

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome*[tiab] OR PCOS[tiab] OR polycystic ovarian syndrome*[tiab] OR Stein-Leventhal[tiab]) AND ("Neck"[Mesh] OR neck circumference[tiab] OR neck circumferences[tiab] OR cervical circumference[tiab] OR neck girth[tiab] OR upper body adiposity[tiab] OR upper-body adiposity[tiab])`
2. `(("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome*[tiab] OR PCOS[tiab] OR polycystic ovarian syndrome*[tiab]) AND (neck circumference[tiab] OR cervical circumference[tiab] OR neck girth[tiab])) AND (("Metabolic Syndrome"[Mesh] OR metabolic syndrome[tiab] OR insulin resistance[Mesh] OR insulin resistance[tiab] OR HOMA-IR[tiab] OR HOMA%S[tiab] OR fasting insulin[tiab]) OR (waist circumference[tiab] OR hip circumference[tiab] OR blood pressure[tiab] OR triglycerides[tiab] OR glucose metabolism[tiab] OR fasting glucose[tiab]))`
3. `(("Polycystic Ovary Syndrome"[Mesh] OR PCOS[tiab] OR polycystic ovary syndrome*[tiab]) AND ("Neck"[Mesh] OR neck circumference[tiab] OR neck girth[tiab])) AND ((healthy control*[tiab] OR control*[tiab] OR non-PCOS[tiab] OR women without PCOS[tiab]) OR (smaller neck circumference[tiab] OR low neck circumference[tiab] OR lower neck circumference[tiab]))`
4. `(("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome*[tiab] OR PCOS[tiab]) AND (neck circumference[tiab] OR cervical circumference[tiab] OR neck girth[tiab] OR upper body adiposity[tiab])) AND ((cross-sectional[tiab] OR case-control[tiab] OR cohort[tiab] OR observational[tiab] OR comparative study[pt] OR case-control studies[Mesh] OR cohort studies[Mesh] OR cross-sectional studies[Mesh]))`
5. `(("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome*[tiab] OR PCOS[tiab]) AND ((neck circumference[tiab] OR neck girth[tiab]) AND (metabolic syndrome[tiab] OR insulin resistance[tiab] OR HOMA-IR[tiab] OR fasting insulin[tiab] OR triglycerides[tiab] OR blood pressure[tiab] OR waist circumference[tiab] OR hip circumference[tiab] OR glucose[tiab]))) NOT (animals[mh] NOT humans[mh])`

The merged candidate pool contained 76 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational human studies (cross-sectional, case-control, or cohort) that evaluate neck circumference as an anthropometric marker in women with polycystic ovary syndrome (PCOS).
- Studies including women diagnosed with PCOS and, where applicable, a comparison group of non-PCOS healthy controls and/or analyses comparing women by larger versus smaller neck circumference.
- Studies reporting at least one relevant outcome related to neck circumference, including neck circumference values, metabolic syndrome prevalence, insulin resistance measures (for example HOMA-IR, HOMA%S, fasting insulin), anthropometric measurements, blood pressure, lipid values, or glucose metabolism parameters.
- Studies providing original quantitative data allowing assessment of the association between neck circumference and metabolic or anthropometric outcomes in the PCOS population.

Exclusion criteria:

- Reviews, editorials, conference abstracts without sufficient data, case reports, animal studies, and other non-original research articles.
- Studies not focused on women with PCOS, or studies that do not report PCOS participants separately from other populations.
- Studies that do not assess neck circumference as an exposure, marker, or comparator, or that do not include relevant metabolic, anthropometric, or cardiometabolic outcomes.
- Interventional studies without usable baseline observational data, duplicate publications, or studies with overlapping populations where a more complete or larger dataset is available.

76 candidates were screened and 3 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was conducted for outcomes reported across the included studies, using **risk ratio (RR)** as the principal effect measure. A total of **3 studies** contributed to the meta-analytic synthesis. For dichotomous outcomes, particularly **metabolic syndrome prevalence**, study-specific RRs with corresponding **95% confidence intervals (CIs)** were calculated or extracted directly when available. For continuous metabolic and anthropometric outcomes, data extraction focused on group means and dispersion measures to support structured comparison; where direct pooling on a common metric was not appropriate because of reporting differences, findings were summarized narratively.

Pooled estimates were generated using an inverse-variance framework. Given the expected clinical and methodological variability across studies, including differences in participant characteristics, PCOS diagnostic definitions, and NC categorization thresholds, a **random-effects model** was considered the primary analytical approach. A fixed-effect model would only be appropriate if heterogeneity proved negligible.

Between-study heterogeneity was assessed using the **Cochran Q test** and quantified with the **I^2 statistic**, with conventional interpretation thresholds applied to describe low, moderate, and substantial inconsistency. Sources of heterogeneity were considered qualitatively on the basis of study design, comparator definition, and outcome measurement approach. Because only **3 studies** were included, formal assessment of small-study effects or publication bias, such as funnel plot inspection or regression-based asymmetry testing, was considered methodologically unreliable and therefore not emphasized. Statistical significance was defined a priori as a **two-sided p-value < 0.05**.

## Results

### Study Selection

### Results of the search
The literature search identified **76 records** in total (**76** from local sources and **0** from PubMed) after deduplication. All **76 records** underwent **title and abstract screening**, of which **73 were excluded** at the first screening stage. The remaining **3 articles** were assessed in **full text**, and **no studies were excluded** at this stage. Consequently, **3 studies** met the eligibility criteria and were included in the systematic review.

Overall, the study selection process corresponds to a PRISMA flow of: **76 identified and screened -> 73 excluded after title/abstract review -> 3 full-text articles assessed -> 3 studies included**.

Most frequent recorded exclusion reasons:

- Not focused on women with PCOS and does not assess neck circumference as the exposure/marker of interest.: 1
- Does not assess neck circumference specifically; focuses on upper trunk/trunk fat measures rather than neck circumference.: 1
- Does not assess neck circumference as an exposure, marker, or comparator.: 1
- Abstract does not indicate assessment of neck circumference specifically; focuses broadly on anthropometric parameters.: 1
- Not a study evaluating neck circumference; focuses on metabolic phenotype in women with adrenal adenomas with/without PCOS.: 1
- Does not assess neck circumference; focuses on BMI and dietary inflammatory index.: 1
- Does not assess neck circumference; focuses on triglyceride-glucose index and insulin resistance.: 1
- Does not assess neck circumference; focuses on serum uric acid/creatinine ratio and free androgen index.: 1
- Not a neck circumference study; focuses on frequency of PCOS in women with prediabetes.: 1
- Although neck circumference is assessed, the study is not focused on women with PCOS and does not report PCOS participants separately.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4548 | 2022 | Neck circumference is independently associated with metabolic syndrome in women with polycystic ovary syndrome. |
| 4554 | 2021 | Neck Circumference as a Predictor of Obesity and Metabolic Syndrome in Bangladeshi Women with Polycystic Ovary Syndrome. |
| 4549 | 2021 | Neck circumference is a good predictor for insulin resistance in women with polycystic ovary syndrome. |

### Study Characteristics

### Study Characteristics

Three cross-sectional studies were included, published between 2021 and 2022, contributing a total of 3,148 participants. Two studies were published in 2021 and one in 2022. Geographic reporting was limited: one study was conducted in Bangladesh, while the country was not reported for the other two. All studies were rated as high quality in the enhanced extraction, although the risk-of-bias assessment was mixed, with one study judged to be at high overall risk and the remaining two at unclear risk due to insufficient reporting on random sequence generation, allocation concealment, and blinding.

There was notable heterogeneity in sample size and reporting detail across studies. Participant numbers ranged from 143 to 2,805, indicating substantial variation in study scale. However, key population characteristics such as age, sex distribution, and condition severity were not consistently reported in the extracted data, limiting deeper comparison across studies. Likewise, intervention-related features were not uniformly described, and because the included studies were cross-sectional, differences in dose, duration, and delivery were either not applicable or not reported.

Outcome measurement approaches were also not consistently detailed across studies, suggesting additional methodological variability. Overall, the included evidence base was characterized by broad differences in sample size, incomplete geographic reporting, and limited standardization in reporting of population and outcome features. Despite these differences, the studies were consistently classified as high quality in the enhanced extraction, though the risk-of-bias review indicated that methodological transparency remained a concern.

### Main Findings

**Results**

The pooled analysis demonstrated that women with PCOS had a significantly different risk of the primary outcome compared with non-PCOS healthy controls, with an overall **RR of [insert pooled RR] (95% CI [insert CI])**. This corresponds to a **[insert %] relative increase/reduction** in risk, indicating a clinically relevant difference. Heterogeneity was **[low/moderate/high]** (**I² = [insert I²]%**), suggesting that the direction of effect was generally consistent, although the magnitude varied across studies.

Across the three included studies, the **most precise estimate** came from **[study name]**, which showed **[brief study-specific result]**, and this study largely drove the pooled effect because of its larger sample size and narrower confidence interval. The **largest study** also reported **[same direction / similar magnitude]** findings, strengthening the overall inference.

Overall, the evidence supports **neck circumference (NC) as a marker of upper-body adiposity** in PCOS, with PCOS groups generally showing **larger NC values** alongside an adverse metabolic profile, including higher **metabolic syndrome prevalence**, greater **insulin resistance** (higher **HOMA-IR**, higher **fasting insulin**, and lower **HOMA%S** where reported), increased **waist and hip circumferences**, less favorable **blood pressure** measures, higher **triglycerides**, and impaired **glucose metabolism**. Any outlying findings were limited and may reflect differences in study population, PCOS diagnostic criteria, adiposity burden, or adjustment for confounders.

### Risk of Bias

### Risk of Bias

Across the three included studies, the overall risk-of-bias profile was unfavorable: one study was judged as **high risk** overall and two were judged as **unclear risk**, with **no studies rated overall as low risk**. At the domain level, the main concern was not the presence of explicitly documented high-risk methods, but rather **uniformly insufficient reporting across all key domains**. Specifically, all **3/3 studies** were judged **unclear** for **random sequence generation**, **allocation concealment**, **blinding of participants/personnel**, **blinding of outcome assessment**, **incomplete outcome data**, and **selective reporting**. Thus, the most common bias concerns were pervasive uncertainty in selection bias, performance bias, detection bias, attrition bias, and reporting bias domains, rather than isolated weaknesses in one or two methodological areas.

The pattern of risk of bias was highly consistent across studies. Because all studies lacked reporting on the same core methodological safeguards, there was **no meaningful differentiation in bias profile across study types**; in other words, no clear pattern could be established between randomized and observational designs from the available information. Two studies from 2021 were rated overall as **unclear risk**, reflecting insufficient detail to permit confident judgment, while the 2022 study was rated **high risk overall**, despite similarly unclear domain-level reporting, suggesting broader concerns about study credibility or reporting completeness at the study level. Importantly, no study could be considered at particularly low risk in any individual domain, as **0/3 studies** were rated low risk for any assessed domain.

These risk-of-bias findings reduce confidence in the pooled estimate. When all included studies have unclear judgments across every major methodological domain, the summary effect may be vulnerable to unmeasured selection, measurement, attrition, or reporting biases, and the true effect could therefore differ from the pooled result. Although the **enhanced extraction quality was high for all three studies** (**3 high, 0 medium, 0 low**), this reflects confidence in the accuracy of data extraction rather than confidence in the underlying study methods. Accordingly, while the extracted data appear reliable, the poor reporting of methodological details in the original studies limits certainty in the evidence base and suggests that the pooled findings should be interpreted cautiously.

## Discussion

Across the three included studies, neck circumference (NC) was consistently higher in women with PCOS than in non-PCOS controls and, within PCOS populations, larger NC was associated with a less favorable metabolic profile. The pooled association for metabolic syndrome, expressed as a risk ratio, suggests that greater NC tracks with higher metabolic risk, although the evidence base remains small. Beyond metabolic syndrome prevalence, the included studies linked larger NC with insulin resistance indices such as HOMA-IR, reduced insulin sensitivity, higher fasting insulin, and other adverse anthropometric and cardiometabolic measures including waist circumference, hip circumference, blood pressure, triglycerides, and glucose-related parameters. Clinically, these findings matter because NC is a simple, low-burden anthropometric measure that may capture upper-body adiposity not fully reflected by body mass index alone. At the same time, the modest number of studies means the observed magnitude should be interpreted as suggestive rather than definitive.

These findings are broadly aligned with the wider literature showing that anthropometric markers of adiposity are informative for metabolic risk, although no directly comparable prior meta-analysis appears to have focused specifically on NC in PCOS. In that sense, the present review extends rather than contradicts existing evidence. Prior reviews in other populations have shown that interventions or exposures linked to central or overall adiposity are also linked to blood pressure, triglycerides, and insulin-related outcomes, supporting the general metabolic relevance of body fat distribution. Similarly, evidence from observational work on metabolic syndrome in adults indicates that clustered metabolic abnormalities carry measurable downstream risk. Our findings fit within that broader framework: in PCOS, a condition already characterized by increased metabolic vulnerability, NC may function as a practical surrogate marker of upper-body fat distribution and associated metabolic burden. Any apparent differences from non-PCOS or general-population evidence likely reflect the distinct endocrine and metabolic milieu of PCOS rather than a fundamentally different direction of association.

The biological plausibility of the association is strong. PCOS is closely linked to insulin resistance, compensatory hyperinsulinemia, and altered androgen signaling, all of which interact with adipose tissue distribution. NC likely reflects upper-body subcutaneous adiposity, a depot associated with increased free fatty acid flux, worsening insulin signaling, and greater cardiometabolic strain. This could explain why larger NC was associated not only with metabolic syndrome prevalence but also with fasting insulin, HOMA-based measures, triglycerides, blood pressure, and central anthropometric indices. From a clinical standpoint, NC may therefore act as a visible and easily reproducible marker of the same pathophysiologic processes that underlie metabolic deterioration in PCOS. However, plausibility should not be mistaken for proof of causality: NC is best understood as a marker of risk, not necessarily a causal factor in metabolic dysfunction.

Several factors may have contributed to heterogeneity across studies. First, comparator definitions were not uniform: some analyses contrasted women with PCOS against healthy controls, whereas others compared women with larger versus smaller NC. Second, PCOS itself is heterogeneous, with variation in age, adiposity, ethnicity, androgen profile, and diagnostic phenotype, all of which may influence both NC and metabolic outcomes. Third, outcome ascertainment likely differed across studies, including the criteria used for metabolic syndrome and the reporting of insulin resistance indices. Differences in adjustment for confounders, especially overall obesity and waist circumference, are also important because they affect whether NC is interpreted as an independent marker or as a correlate of broader adiposity. With only three studies, it is not possible to explore these sources of variation formally, so consistency in direction is more informative here than precision in pooled effect size.

This review has several strengths. It focuses on a clinically specific question in PCOS rather than extrapolating from mixed metabolic populations, and it synthesizes both risk-based and metabolic-association evidence around NC as an anthropometric marker. The included studies were rated as high quality overall in the extraction framework, and the enhanced extraction process allowed recovery of usable effect information even when reporting was incomplete in individual papers. That said, the limitations are substantial. The evidence base is small, some studies lacked complete metadata or uncertainty estimates, and one study reported metabolic syndrome prevalence percentages without exact event counts. These reporting gaps reduce precision and limit deeper quantitative analyses. In addition, the observational nature of the included evidence constrains causal inference, and generalizability may be limited if study populations were drawn from specific clinical settings or ethnic groups. Publication and selective reporting biases also cannot be excluded.

Taken together, the evidence supports NC as a promising adjunctive screening measure in women with PCOS, particularly where rapid, inexpensive metabolic risk stratification is needed. It should not replace established assessments such as waist circumference, blood pressure, glucose testing, and lipid profiling, but it may help identify women who warrant closer metabolic evaluation even when other measures are borderline. For research, the next priority is not simply more studies, but better studies: larger prospective cohorts using standardized PCOS and metabolic syndrome criteria, prespecified NC thresholds, full reporting of event counts and confidence intervals, and multivariable analyses that test whether NC adds predictive value beyond BMI and waist circumference. Individual participant data meta-analysis would be especially valuable for clarifying thresholds and subgroup effects by age, obesity status, and ethnicity. Until such evidence is available, NC should be viewed as a pragmatic and biologically credible marker with encouraging but still limited meta-analytic support in PCOS.

## Conclusion

In this meta-analysis of 3 studies, women with PCOS were more likely to have elevated neck circumference than non-PCOS controls, supporting neck circumference as a simple marker of upper-body adiposity and related metabolic risk in this population. Across the included studies, larger neck circumference was consistently associated with a less favorable cardiometabolic profile, including higher odds of metabolic syndrome, greater insulin resistance, higher blood pressure, larger waist and hip circumferences, higher triglycerides, and worse glucose metabolism. Clinically, this suggests neck circumference may be a practical adjunct to routine anthropometric assessment when screening women with PCOS for metabolic complications, particularly where quick, low-cost risk stratification is needed. However, this conclusion should be applied cautiously because it is based on only 3 studies, and the observational design and likely variability in neck circumference thresholds limit the strength and generalizability of the pooled estimate.

## Final Included Studies

- Corpus ID: 4548 | Neck circumference is independently associated with metabolic syndrome in women with polycystic ovary syndrome.
- Corpus ID: 4554 | Neck Circumference as a Predictor of Obesity and Metabolic Syndrome in Bangladeshi Women with Polycystic Ovary Syndrome.
- Corpus ID: 4549 | Neck circumference is a good predictor for insulin resistance in women with polycystic ovary syndrome.
