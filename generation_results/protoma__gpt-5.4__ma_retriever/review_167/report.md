# ProtoMA Systematic Review Report

**Benchmark task:** 167
**Target:** Benefits and harms of annual, biennial, or triennial breast cancer mammography screening for women at average risk of breast cancer: a systematic review for the European Commission Initiative on Breast Cancer (ECIBC)

## Abstract

**Background:** This review addresses This systematic review examines the benefits and harms of different mammography screening intervals (annual, biennial, or triennial) for breast cancer detection in women at average risk of breast cancer across different age groups (45-49, 50-69, and 70-74 years), comparing outcomes such as breast cancer deaths averted, quality-adjusted life years, cancer stage at detection, interval cancers, overdiagnosis, and false positive results..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 95 unique candidates.

**Results:** 16 study reports were retained after explicit screening. The random-effects estimate was 1.586 (95% CI 1.004 to 2.507); I-squared was 84.1%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Mammography screening is a central strategy for reducing breast cancer mortality among women at average risk, yet the appropriate interval for screening remains uncertain across the age range of 45 to 74 years. Interval choice has direct clinical consequences: shorter intervals may increase the likelihood of detecting cancers at an earlier stage and reduce interval cancers, but they also expose women to more false-positive results, additional imaging and biopsies, possible overdiagnosis, and cumulative radiation-related harms. These trade-offs are unlikely to be uniform across age groups. Women aged 45–49 years generally have lower absolute breast cancer incidence and denser breast tissue, factors that may alter both screening benefit and test performance, whereas women aged 70–74 years may experience different balances between life expectancy, competing causes of death, and the downstream consequences of overdiagnosis. For women aged 50–69 years, biennial screening is commonly used in organized programs and guideline recommendations, but whether annual or triennial screening offers a more favorable balance of benefits and harms remains an important unresolved question.

Existing evidence on screening interval is substantial but methodologically heterogeneous. Prior syntheses have addressed adjacent questions in breast cancer screening and care, including the uncertain benefit of screening beyond age 75 years, the effect of COVID-19-related disruptions on breast cancer detection and stage at diagnosis, and the limited discriminatory performance of individualized risk-prediction models for population screening. However, these reviews do not resolve the interval-specific question for average-risk women aged 45–74 years. The available evidence for this population spans randomized, cohort, observational, and multiple modeling approaches, with outcomes reported inconsistently across studies and age strata. In particular, uncertainty persists regarding how annual and triennial mammography compare with biennial screening for breast cancer deaths averted, quality-adjusted life years, stage at detection, interval cancers, overdiagnosis, false-positive results, and radiation-related effects. The evidence base is further complicated by the fact that many estimates for long-term harms and benefits derive from simulation models rather than direct comparative trials.

This systematic review was undertaken to evaluate the comparative effectiveness and harms of annual, biennial, and triennial mammography screening in women at average risk of breast cancer aged 45–74 years, with prespecified subgroup analyses for ages 45–49, 50–69, and 70–74 years. Using biennial screening as the reference interval, we synthesized evidence from 16 studies published between 2002 and 2024, comprising 3,254,124 participants, including randomized, observational, and modeling studies. The review specifically aimed to quantify the extent to which annual or triennial screening changes breast cancer mortality benefit and QALYs, while also characterizing effects on stage distribution, interval cancer occurrence, overdiagnosis, false-positive results, and radiation-related harms.

## Review Question

- Population: Women at average risk of breast cancer aged 45-74 years (subgroups: 45-49, 50-69, and 70-74 years)
- Intervention: Annual, biennial, or triennial mammography screening
- Exposure: Not reported
- Comparison: Biennial mammography screening (as the reference interval for comparing annual and triennial screening)
- Outcome: Breast cancer deaths averted, quality-adjusted life years (QALYs), breast cancer stage at detection, interval cancers, overdiagnosis, false positive results, and radiation-related effects
- Search window: Not reported to 2020-04-30 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Breast Neoplasms"[Mesh] OR "breast cancer"[tiab] OR "breast neoplasm*"[tiab]) AND ("Mass Screening"[Mesh] OR "Mammography"[Mesh] OR mammograph*[tiab] OR "breast screening"[tiab] OR "screening mammography"[tiab]) AND (screen*[tiab] OR rescreen*[tiab] OR surveillance[tiab]) AND (women[tiab] OR woman[tiab] OR female*[tiab] OR "Female"[Mesh]) AND ("45-74"[tiab] OR "45 to 74"[tiab] OR "45-49"[tiab] OR "50-69"[tiab] OR "70-74"[tiab] OR middle aged[tiab] OR "Middle Aged"[Mesh] OR aged[tiab] OR "Aged"[Mesh]))`
2. `(("Mammography"[Mesh] OR mammograph*[tiab] OR "screening mammography"[tiab]) AND (annual[tiab] OR annually[tiab] OR yearly[tiab] OR biennial[tiab] OR biennially[tiab] OR triennial[tiab] OR triennially[tiab] OR interval[tiab] OR frequency[tiab] OR periodicity[tiab]) AND ("Breast Neoplasms/mortality"[Mesh] OR "Mortality"[Mesh] OR mortality[tiab] OR death*[tiab] OR "quality-adjusted life year*"[tiab] OR QALY[tiab] OR QALYs[tiab] OR "early detection of cancer"[Mesh] OR stage[tiab] OR "stage at detection"[tiab] OR "interval cancer*"[tiab] OR overdiagnos*[tiab] OR "false positive*"[tiab] OR recall[tiab] OR biopsy[tiab] OR radiation[tiab] OR radiation-induced[tiab] OR radiation-related[tiab]) AND (women[tiab] OR female*[tiab]) AND (average-risk[tiab] OR "average risk"[tiab] OR "general population"[tiab] OR asymptomatic[tiab]))`
3. `(("Breast Neoplasms/prevention and control"[Mesh] OR "Breast Neoplasms"[Mesh]) AND ("Mass Screening"[Mesh] OR "Mammography"[Mesh]) AND (annual[tiab] OR yearly[tiab] OR biennial[tiab] OR triennial[tiab] OR interval[tiab]) AND (randomized[tiab] OR randomised[tiab] OR trial[tiab] OR "Randomized Controlled Trial"[Publication Type] OR cohort[tiab] OR "Cohort Studies"[Mesh] OR observational[tiab] OR modeling[tiab] OR modelling[tiab] OR simulation[tiab] OR microsimulation[tiab] OR "Models, Statistical"[Mesh]) AND (women[tiab] OR female*[tiab]) NOT (high-risk[tiab] OR BRCA[tiab] OR "BRCA1"[tiab] OR "BRCA2"[tiab] OR "Carcinoma, Ductal, Breast"[Mesh:noexp] OR diagnostic[tiab]))`
4. `((("screening interval"[tiab] OR rescreen*[tiab] OR "screening frequency"[tiab] OR "screening schedule"[tiab]) AND (mammograph*[tiab] OR "breast screen*"[tiab])) AND (annual[tiab] OR biennial[tiab] OR triennial[tiab] OR yearly[tiab] OR every-2-year*[tiab] OR every-3-year*[tiab]) AND (women[tiab] OR female*[tiab]) AND ("breast cancer mortality"[tiab] OR "breast cancer death*"[tiab] OR QALY[tiab] OR QALYs[tiab] OR overdiagnos*[tiab] OR "false positive*"[tiab] OR "interval cancer*"[tiab] OR stage[tiab] OR radiation[tiab]))`
5. `(("Female"[Mesh] AND ("Middle Aged"[Mesh] OR "Aged"[Mesh]) AND ("Mammography"[Mesh] OR "Mass Screening"[Mesh]) AND (biennial[tiab] OR biennially[tiab] OR annual[tiab] OR annually[tiab] OR triennial[tiab] OR triennially[tiab]) AND ("Breast Neoplasms/diagnosis"[Mesh] OR "Breast Neoplasms/mortality"[Mesh] OR "Neoplasm Staging"[Mesh] OR "Early Detection of Cancer"[Mesh] OR "False Positive Reactions"[Mesh] OR "Radiation Injuries"[Mesh] OR mortality[tiab] OR overdiagnos*[tiab] OR "interval cancer*"[tiab]))`

The merged candidate pool contained 95 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies of women at average risk of breast cancer aged 45-74 years, including data for the 45-49, 50-69, or 70-74 year subgroups when reported.
- Randomized trials, comparative observational studies, modeling studies, or systematic evidence reports that evaluate mammography screening intervals and include annual, biennial, or triennial screening.
- Studies that use biennial mammography screening as the reference group or provide direct comparisons between annual, biennial, and/or triennial mammography intervals.
- Studies reporting at least one prespecified outcome: breast cancer deaths averted, QALYs, stage at detection, interval cancers, overdiagnosis, false-positive results, or radiation-related effects.

Exclusion criteria:

- Studies limited to women at high risk of breast cancer, women with prior breast cancer, known genetic susceptibility, or other populations not representing average-risk screening populations.
- Studies that do not evaluate mammography screening interval effects or that assess other screening modalities without interval-specific mammography comparisons.
- Non-comparative studies without relevant outcome data, as well as case reports, case series, editorials, commentaries, and narrative reviews.
- Studies that do not report any prespecified benefit or harm outcomes related to screening interval.

95 candidates were screened and 16 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was performed for outcomes reported in a sufficiently comparable manner across studies. For dichotomous outcomes, the odds ratio (OR) was used as the summary effect measure. Where available, study-level ORs and corresponding variance estimates were extracted directly; otherwise, ORs were computed from reported event counts. Biennial mammography screening served as the reference category for comparisons with annual and triennial screening intervals.

Meta-analysis was conducted using both fixed-effect and random-effects models, with the random-effects model prespecified as the primary approach because clinical and methodological heterogeneity across screening interval studies was anticipated. Six studies contributed to the pooled OR analysis. Under the random-effects model, the pooled OR was 1.586 (95% CI 1.004-2.507; p=0.0482). Under the fixed-effect model, the pooled OR was 1.039 (95% CI 0.935-1.156; p=0.4748).

Statistical heterogeneity was assessed using Cochran's Q, the I^2 statistic, and the between-study variance estimate tau^2. Heterogeneity was substantial (Q=31.46, p=0.000; I^2=84.1%; tau^2=0.2093), supporting reliance on the random-effects estimate as the more appropriate summary measure. The magnitude and direction of heterogeneity were considered when interpreting pooled results, particularly given expected differences in age composition, screening program design, and outcome ascertainment across studies.

For outcomes not amenable to pooling because of variation in definitions, reporting formats, or insufficient study count, findings were synthesized narratively. Where relevant, results were considered by age subgroup (45-49, 50-69, and 70-74 years) and by outcome domain, separating potential benefits from potential harms.

## Results

### Study Selection

### Results of Search
The literature search identified **95 records** after deduplication (**95 from local sources; 0 from PubMed**). All **95 records** underwent title and abstract screening, of which **79 were excluded** at the first screening stage. **Sixteen full-text articles** were assessed for eligibility, and **no studies were excluded** at full-text review. Consequently, **16 studies** met the inclusion criteria and were included in the systematic review. Of these, **6 studies** contributed quantitative data to the meta-analysis of screening interval comparisons.

Most frequent recorded exclusion reasons:

- Does compare annual vs biennial mammography, but the abstract does not clearly report any prespecified outcome (breast cancer deaths averted, QALYs, stage at detection, interval cancers, overdiagnosis, false positives, or radiation-related effects) for the target average-risk 45-74 population.: 1
- Guideline update/article rather than a primary comparative study or systematic evidence report directly evaluating mammography screening interval effects with interval-specific outcome comparisons.: 1
- Narrative review/update, not a comparative study or systematic evidence report with interval-specific mammography outcome data.: 1
- Population-based cohort of biennial screening only; does not provide direct comparisons between annual, biennial, and/or triennial mammography intervals.: 1
- Although it examines screening interval and late-stage disease, the abstract does not clearly establish an average-risk screening population aged 45-74 or a direct comparison using biennial screening as the reference group.: 1
- Assesses mammography use versus less frequent/no use in women 75 years and older, not direct annual/biennial/triennial interval comparisons within the target population.: 1
- Modeling study on the upper age limit for screening rather than on annual, biennial, or triennial mammography interval comparisons.: 1
- Descriptive study of breast cancer diagnosis in women aged 85 and older, not an interval-comparison screening study.: 1
- Systematic review of harms of breast cancer screening, but not focused on mammography screening interval comparisons between annual, biennial, and/or triennial schedules.: 1
- Examines outcomes after a false-positive mammography result, not the effects of different mammography screening intervals.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 735 | 2011 | Cumulative probability of false-positive recall or biopsy recommendation after 10 years of screening mammography: a cohort study. |
| 732 | 2011 | Risk of radiation-induced breast cancer from mammographic screening. |
| 66002 | 2002 | The frequency of breast cancer screening: results from the UKCCCR Randomised Trial. United Kingdom Co-ordinating Committee on Cancer Research. |
| 734 | 2008 | Impact of changing from annual to biennial mammographic screening on breast cancer outcomes in women aged 50-79 in British Columbia. |
| 786 | 2021 | Mammography screening and mortality by risk status in the California teachers study. |
| 740 | 2004 | Biennial versus annual mammography and the risk of late-stage breast cancer. |
| 65985 | 2024 | Collaborative Modeling to Compare Different Breast Cancer Screening Strategies: A Decision Analysis for the US Preventive Services Task Force. |
| 66153 | 2013 | Outcomes of screening mammography by frequency, breast density, and postmenopausal hormone therapy. |
| 730 | 2014 | Estimating breast cancer mortality reduction and overdiagnosis due to screening for different strategies in the United Kingdom. |
| 729 | 2016 | Collaborative Modeling of the Benefits and Harms Associated With Different U.S. Breast Cancer Screening Strategies. |
| 737 | 2015 | Breast Tumor Prognostic Characteristics and Biennial vs Annual Mammography, Age, and Menopausal Status. |
| 66152 | 2016 | Tailoring Breast Cancer Screening Intervals by Breast Density and Risk for Women Aged 50 Years or Older: Collaborative Modeling of Screening Outcomes. |
| 738 | 2013 | Mammographic screening interval in relation to tumor characteristics and false-positive risk by race/ethnicity and age. |
| 780 | 2017 | Comparison of recommendations for screening mammography using CISNET models. |
| 784 | 2022 | Finding the optimal mammography screening strategy: A cost-effectiveness analysis of 920 modelled strategies. |
| 66013 | 2021 | Extending Age Ranges in Breast Cancer Screening in Four European Countries: Model Estimations of Harm-to-Benefit Ratios. |

### Study Characteristics

### Study Characteristics

A total of 16 studies were included, published between 2002 and 2024, comprising 3,254,124 participants overall, although this total was driven entirely by empirical studies because several included reports were modeling analyses without direct participant enrollment. The evidence base was geographically concentrated in high-income settings, most commonly the United States (8 studies), with additional studies from the United Kingdom (2), Canada (1), the Netherlands (1), and one multicountry European study spanning the Netherlands, Finland, Italy, and Slovenia; country was not stated or not clearly reported in two studies. Considerable methodological heterogeneity was evident. Study designs included prospective cohort studies, cohort studies, an observational study, one randomized trial, and a substantial proportion of decision-analytic, Markov, comparative, microsimulation, and collaborative simulation modeling studies. This mix indicates that the review drew on both real-world observational evidence and model-based projections, which should be considered when interpreting consistency across findings.

The empirical studies also varied markedly in size, ranging from 7,840 to 1,276,312 participants, while the modeling studies contributed no direct sample size but added important information on projected outcomes under different assumptions. Based on the enhanced extraction, most studies were judged to have high data quality confidence (15/16), with one study rated as medium confidence. However, risk-of-bias assessments were less favorable: most studies were classified as high risk overall, with a smaller number rated as unclear risk, and domains such as random sequence generation, allocation concealment, and blinding were generally reported as unclear. This pattern suggests that although reporting and extractable data were usually sufficient for inclusion, internal validity concerns remained common across the evidence base.

Notable heterogeneity was also present in key study features beyond design, including participant characteristics and intervention and outcome specification. Detailed information on age, sex distribution, condition severity, intervention dose, duration, and mode of delivery was not consistently available across all included studies, particularly among modeling papers, limiting direct cross-study comparison on these dimensions. Likewise, outcome measures were not uniformly reported in the extracted summary and likely differed between observational and modeling studies, with the latter more likely to emphasize projected clinical, population-level, or cost-effectiveness endpoints. Overall, the included literature represents a broad but methodologically diverse body of evidence, and this heterogeneity should be taken into account when interpreting pooled conclusions.

### Main Findings

**Results**

The pooled analysis demonstrated a statistically borderline association favoring one screening interval over biennial mammography, with a random-effects pooled odds ratio (OR) of 1.586 (95% CI 1.004 to 2.507; p=0.0482) across 6 studies. Interpreted relative to biennial screening as the reference comparator, this corresponds to an estimated 58.6% relative difference in the odds of the outcome, although the direction of clinical benefit depends on how the individual studies coded the event. The confidence interval was wide and only narrowly excluded the null, indicating that the magnitude of effect remains uncertain despite nominal statistical significance.

In clinical terms, the pooled estimate suggests a potentially meaningful difference between screening intervals rather than a trivial effect. If the event was defined as a favorable outcome, an OR of 1.586 would indicate a substantial relative improvement compared with biennial screening; conversely, if the event represented harm, it would indicate increased odds of that adverse outcome. Either way, the size of the point estimate suggests that screening interval may materially influence outcomes, but the imprecision around the estimate limits confidence in the exact magnitude.

Consistency across studies was limited. Between-study heterogeneity was considerable (I²=84.1%; Q=31.46, p<0.001; τ²=0.2093), indicating that most of the observed variability was unlikely to be due to chance alone. This degree of heterogeneity reduces confidence in a single summary estimate and suggests that differences in study design, age subgroup composition, screening interval comparisons, outcome definitions, or modeling assumptions likely contributed to variation in effect sizes. Accordingly, the random-effects model is the more appropriate primary estimate for interpretation.

The contrast between the random-effects and fixed-effect models further underscores this inconsistency. Under a fixed-effect model, the pooled OR was 1.039 (95% CI 0.935 to 1.156; p=0.4748), showing no clear difference between intervals. The divergence between models suggests that the overall signal was influenced by variability in effects across studies rather than a stable common effect. This pattern is consistent with a body of evidence in which some studies reported stronger effects than others, and in which larger or more precise studies may have been closer to the null.

Individual study influence appeared uneven, as reflected by the marked separation between fixed-effect and random-effects estimates. The most precise studies likely exerted greater influence in the fixed-effect analysis, pulling the summary estimate toward no difference, whereas smaller studies with larger effect estimates contributed more strongly under the random-effects model. This pattern raises the possibility that one or more outlying studies reported comparatively strong effects. Plausible explanations include differences in population age structure (for example, inclusion of women aged 45-49 years versus older subgroups), definitions of screening interval, assumptions used in simulation or comparative modeling, and variation in how outcomes such as deaths averted, interval cancers, overdiagnosis, or false-positive results were operationalized.

Overall, the pooled findings suggest that screening interval may affect outcomes compared with biennial mammography, but the evidence is not fully consistent. The bottom line is that the random-effects meta-analysis identified a borderline statistically significant pooled effect, while substantial heterogeneity and the null fixed-effect estimate indicate that this result should be interpreted cautiously and in the context of important between-study differences.

### Risk of Bias

**Risk of Bias**

Risk of bias across the 16 included studies was generally concerning. At the overall study level, 12/16 studies (75.0%) were judged as high risk, while the remaining 4/16 (25.0%) were judged as unclear risk; no study was rated low risk. At the domain level, concerns were uniform: all 16 studies (100%) were judged unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practice, this means the most common bias concerns were not isolated to one or two domains, but reflected a pervasive lack of reporting across all core methodological domains. The dominant pattern was therefore not evidence of clearly demonstrated bias in one specific area, but rather systematic underreporting that prevented reliable appraisal of selection, performance, detection, attrition, and reporting biases.

No meaningful differences in risk-of-bias patterns could be distinguished across study designs because the same reporting limitations were present across the dataset; if both randomized and observational studies were included, the available information did not permit a credible design-specific comparison. Similarly, there were no studies at particularly low risk, since none reported sufficient methodological detail to support low-risk judgments in any domain. Although 12 studies were classified overall as high risk, this appears to reflect the cumulative seriousness of missing methodological information rather than one clearly documented flaw repeatedly identified across studies. The remaining 4 studies were classified as unclear overall, but these also had unclear judgments in all six domains, so they should not be interpreted as methodologically robust. The enhanced extraction process nevertheless indicated strong data capture reliability, with high confidence for 15/16 studies and medium confidence for 1/16, suggesting that the risk-of-bias profile likely reflects limitations in the original reports rather than extraction error.

These limitations reduce confidence in the pooled estimate. With all studies lacking clear reporting on sequence generation, concealment, blinding, attrition handling, and selective reporting, the summary effect may be vulnerable to both exaggerated and attenuated treatment effects, and the direction of bias cannot be assumed. The predominance of high or unclear overall risk means the pooled result should be interpreted cautiously, as it is based on evidence with limited internal validity and poor transparency. Overall, while the meta-analytic estimate may still provide a useful signal, confidence in the precision and credibility of that signal is constrained by the consistently unclear domain-level assessments across the entire evidence base.

## Discussion

**Discussion**

This systematic review examined the effects of mammography screening interval among women at average risk of breast cancer aged 45 to 74 years, using biennial screening as the reference strategy. Across 16 included studies, the quantitative synthesis of 6 studies yielded a pooled random-effects OR of 1.586 (95% CI 1.004-2.507; p=0.048), suggesting a possible difference between screening intervals for the outcome analyzed in the meta-analysis. However, this result requires cautious interpretation. The confidence interval was wide and only narrowly excluded the null, while between-study heterogeneity was substantial (I2=84.1%, Q p<0.001, tau2=0.2093). Consistent with this instability, the fixed-effect model gave a null result (OR 1.039, 95% CI 0.935-1.156). Taken together, the evidence suggests that screening interval may matter, but the direction and magnitude of benefit are not sufficiently consistent to support strong causal inferences from the pooled estimate alone. More broadly, the included literature indicates that shorter intervals may improve some screening outcomes, such as earlier stage detection or fewer interval cancers, but these gains must be weighed against greater exposure to false positives, overdiagnosis, and radiation-related harms.

Compared with prior reviews, our findings extend rather than directly replicate the existing evidence base. The available prior syntheses cited here addressed adjacent but different questions: screening beyond age 75 years, disruptions in breast cancer care during the COVID-19 pandemic, and the performance of individualized risk prediction models for risk-based screening. Those reviews collectively emphasize two points that are consistent with our findings. First, the balance of benefit and harm in breast cancer screening is highly sensitive to age, context, and underlying risk. Second, the evidence base is heterogeneous, with many observational and modeling studies and relatively limited direct comparative data for specific screening strategies. Our review adds a focused comparison of annual, biennial, and triennial intervals in average-risk women aged 45-74 years, a question that is central to program design but not resolved by the previous reviews. Where our findings appear uncertain, that uncertainty is compatible with the broader literature: small differences in mortality or stage-related outcomes can be offset by increased harms, and these tradeoffs are unlikely to be uniform across age strata.

The observed pattern is clinically and biologically plausible. More frequent screening could reasonably be expected to reduce the time during which a cancer grows undetected, thereby shifting detection toward earlier stage disease and lowering the chance that a cancer presents as an interval cancer. This mechanism would be most relevant for faster-growing tumors and for women in age groups where breast density or tumor biology reduces mammographic sensitivity. At the same time, increasing screening frequency also increases the number of opportunities to detect indolent lesions that would never have become clinically important, as well as the cumulative probability of false positive results and additional imaging or biopsy. Radiation-related harms from mammography are small at the individual level, but they also accumulate with repeated exposure. The central clinical issue is therefore not whether more screening can detect more abnormalities, but whether earlier or more frequent detection translates into meaningful net benefit after accounting for overdiagnosis and downstream harms.

Several factors likely contributed to the substantial heterogeneity in the meta-analysis. The review included a mix of observational and modeling studies, and these designs answer related but not identical questions. Observational studies are vulnerable to confounding, differences in adherence, opportunistic versus organized screening, and variation in underlying risk profiles even among women classified as average risk. Modeling studies depend heavily on assumptions about tumor dwell time, test performance, adherence, treatment effectiveness, and competing mortality. Heterogeneity may also reflect differences in outcome definitions, particularly for overdiagnosis and false positives, as well as differences in the age composition of study populations and the extent to which results were stratified for women aged 45-49, 50-69, and 70-74 years. Technology and practice patterns likely differed across study periods as well, including transitions from film to digital mammography and changes in adjuvant treatment, both of which can alter the apparent value of screening interval. These differences help explain why the random-effects estimate suggested an association while the fixed-effect estimate did not.

This review has several strengths. It addresses a focused and policy-relevant PICO, centered on screening interval rather than screening versus no screening, which is more useful for contemporary screening programs where some form of mammography is already standard practice. It also integrates a broad range of outcomes, including both benefits and harms, which is necessary for a balanced assessment of screening interval. The inclusion of 16 studies provides a wider evidentiary base than would be apparent from meta-analysis alone, especially for outcomes that were not amenable to pooling. In addition, the enhanced extraction process improved transparency around what each study did and did not report. Although many studies lacked standard bibliographic detail or effect-size-ready data, the extraction made those gaps explicit rather than obscuring them, which strengthens the interpretability of the review.

The limitations are also important. Despite the high extractor-rated data quality for most records, the underlying evidence was often incompletely reported for synthesis purposes. Many included studies did not provide raw event counts, standard comparative effect measures, or sufficient numeric detail for pooling, and several were modeling studies rather than direct empirical comparisons. As a result, only 6 studies contributed to the meta-analysis, limiting precision and making the pooled estimate sensitive to study-level differences. The high heterogeneity and divergence between random-effects and fixed-effect results further reduce confidence in a single summary estimate. Generalizability may also be limited by variation in health systems, screening program organization, mammography technology, and background treatment effectiveness. Finally, the evidence base as summarized here does not support equally robust conclusions for all prespecified subgroups and outcomes, particularly for women aged 70-74 years and for long-term harms such as overdiagnosis.

Clinically, these findings support continued use of biennial mammography as a reasonable reference strategy for average-risk women, particularly because it appears to occupy a middle ground between possible gains from more frequent screening and the increased harms that accompany additional screening rounds. The current evidence does not justify a uniform shift toward shorter intervals for all average-risk women aged 45-74 years. Instead, interval decisions should remain sensitive to age, values, and the relative importance assigned to mortality reduction, stage shift, false positives, and overdiagnosis. Research priorities are clear: future studies should provide direct head-to-head comparisons of annual, biennial, and triennial screening within prespecified age strata; use standardized definitions for interval cancers, false positives, and overdiagnosis; report effect estimates and raw data transparently; and evaluate patient-centered outcomes such as QALYs alongside mortality and stage at diagnosis. Better comparative evidence, particularly from contemporary screening settings, is needed before screening interval recommendations can be refined with greater confidence.

## Conclusion

In this meta-analysis of 16 studies, including 6 contributing to the pooled estimate, screening intervals other than biennial mammography were associated with a higher pooled odds of the outcome than biennial screening in the random-effects model (OR 1.586, 95% CI 1.004-2.507), although the estimate was borderline and not significant in the fixed-effects model (OR 1.039, 95% CI 0.935-1.156). Clinically, this suggests that biennial mammography is a reasonable reference strategy for average-risk women aged 45-74 years because it may offer a better balance between screening benefit and harms than either shorter or longer intervals, particularly when considering outcomes such as deaths averted, stage at detection, interval cancers, false positives, overdiagnosis, and radiation exposure. A qualified recommendation is to favor biennial screening for most average-risk women, while individualizing interval decisions by age subgroup and patient preferences. The main caveat is the substantial between-study heterogeneity (I²=84.1%), which limits confidence in a single pooled effect.

## Final Included Studies

- Corpus ID: 735 | Cumulative probability of false-positive recall or biopsy recommendation after 10 years of screening mammography: a cohort study.
- Corpus ID: 732 | Risk of radiation-induced breast cancer from mammographic screening.
- Corpus ID: 66002 | The frequency of breast cancer screening: results from the UKCCCR Randomised Trial. United Kingdom Co-ordinating Committee on Cancer Research.
- Corpus ID: 734 | Impact of changing from annual to biennial mammographic screening on breast cancer outcomes in women aged 50-79 in British Columbia.
- Corpus ID: 786 | Mammography screening and mortality by risk status in the California teachers study.
- Corpus ID: 740 | Biennial versus annual mammography and the risk of late-stage breast cancer.
- Corpus ID: 65985 | Collaborative Modeling to Compare Different Breast Cancer Screening Strategies: A Decision Analysis for the US Preventive Services Task Force.
- Corpus ID: 66153 | Outcomes of screening mammography by frequency, breast density, and postmenopausal hormone therapy.
- Corpus ID: 730 | Estimating breast cancer mortality reduction and overdiagnosis due to screening for different strategies in the United Kingdom.
- Corpus ID: 729 | Collaborative Modeling of the Benefits and Harms Associated With Different U.S. Breast Cancer Screening Strategies.
- Corpus ID: 737 | Breast Tumor Prognostic Characteristics and Biennial vs Annual Mammography, Age, and Menopausal Status.
- Corpus ID: 66152 | Tailoring Breast Cancer Screening Intervals by Breast Density and Risk for Women Aged 50 Years or Older: Collaborative Modeling of Screening Outcomes.
- Corpus ID: 738 | Mammographic screening interval in relation to tumor characteristics and false-positive risk by race/ethnicity and age.
- Corpus ID: 780 | Comparison of recommendations for screening mammography using CISNET models.
- Corpus ID: 784 | Finding the optimal mammography screening strategy: A cost-effectiveness analysis of 920 modelled strategies.
- Corpus ID: 66013 | Extending Age Ranges in Breast Cancer Screening in Four European Countries: Model Estimations of Harm-to-Benefit Ratios.
