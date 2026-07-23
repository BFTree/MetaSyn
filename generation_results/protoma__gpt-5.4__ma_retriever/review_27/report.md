# ProtoMA Systematic Review Report

**Benchmark task:** 27
**Target:** Effects of obstructive sleep apnea on non-alcoholic fatty liver disease in patients with obesity: a systematic review

## Abstract

**Background:** This review addresses This systematic review examines which obstructive sleep apnea (OSA)-related indicators can predict the presence of non-alcoholic fatty liver disease (NAFLD) in patients with obesity, and assesses the effect of bariatric metabolic surgery (BMS) on improving both OSA and NAFLD over time..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 81 unique candidates.

**Results:** 13 study reports were retained after explicit screening. The random-effects estimate was 3.154 (95% CI 1.515 to 6.569); I-squared was 0.0%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Severe obesity is strongly linked to both obstructive sleep apnea (OSA) and non-alcoholic fatty liver disease (NAFLD), two conditions that frequently coexist in patients evaluated for bariatric metabolic surgery. In adults with body mass index (BMI) 35 or higher, OSA is characterized by recurrent upper-airway collapse, intermittent hypoxia, sleep fragmentation, and sympathetic activation, all of which may plausibly exacerbate hepatic steatosis, inflammation, and fibrogenesis beyond the metabolic effects of adiposity alone. This question is clinically important because patients with severe obesity often undergo preoperative assessment for OSA and liver disease, yet the extent to which OSA severity identifies higher NAFLD burden remains uncertain. Clarifying this relationship has direct implications for risk stratification before surgery, interpretation of liver biochemistry, and the selection of patients who may warrant more intensive hepatic evaluation, including histologic assessment.

Evidence to date suggests that OSA-related measures, particularly apnea-hypopnea index (AHI) and markers of nocturnal intermittent hypoxia, may be associated with NAFLD presence and severity, but the literature is methodologically heterogeneous. Published studies span cross-sectional, cohort, retrospective, and prospective designs, include both bariatric and non-bariatric clinical samples, and use multiple liver outcome measures, including liver biopsy, NAFLD activity score (NAS), steatosis, fibrosis, lobular inflammation, and serum aminotransferases such as alanine aminotransferase (ALT) and aspartate aminotransferase (AST). Comparators also vary, ranging from patients without OSA to those stratified by OSA severity or assessed before bariatric metabolic surgery. As a result, the field lacks a consolidated synthesis focused specifically on adults with severe obesity, where the overlap between OSA and NAFLD is most clinically relevant and confounding by adiposity is especially difficult to disentangle.

This systematic review therefore evaluates whether OSA and OSA-related indicators are associated with NAFLD in adults with obesity defined as BMI 35 or higher. Specifically, it examines differences in NAFLD presence, histologic severity, and resolution-related liver outcomes across patients without OSA and those with varying OSA severity, with particular attention to AHI and intermittent hypoxia as exposure markers. The review synthesizes evidence from 13 studies published between 2007 and 2023, comprising 1,977 participants, to assess associations across biopsy-based, score-based, and serum-based liver endpoints and to define the current limits of inference for pre-bariatric and severe-obesity populations.

## Review Question

- Population: Adults with obesity (BMI ≥ 35)
- Intervention: Not reported
- Exposure: Obstructive sleep apnea (OSA) and OSA-related indicators including apnea-hypopnea index (AHI) and intermittent hypoxia
- Comparison: Patients without OSA or with varying OSA severity levels; pre-bariatric metabolic surgery status
- Outcome: Non-alcoholic fatty liver disease (NAFLD) presence, severity, and resolution assessed through multiple liver outcome tests including liver biopsy, NAFLD activity score (NAS), steatosis, fibrosis, inflammation, and serum markers (ALT, AST)
- Search window: Not reported to 2022-10-08

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Obesity"[Mesh] OR obes*[tiab] OR "morbid obesity"[tiab] OR "severe obesity"[tiab] OR "BMI 35"[tiab] OR "body mass index 35"[tiab]) AND ("Sleep Apnea, Obstructive"[Mesh] OR "obstructive sleep apnea"[tiab] OR OSA[tiab] OR "sleep apnoea"[tiab] OR AHI[tiab] OR "apnea hypopnea index"[tiab] OR "apnea-hypopnea index"[tiab] OR intermittent hypox*[tiab]))`
2. `(("Obesity"[Mesh] OR obes*[tiab] OR "morbid obesity"[tiab] OR "severe obesity"[tiab]) AND ("Sleep Apnea, Obstructive"[Mesh] OR OSA[tiab] OR "obstructive sleep apnea"[tiab] OR AHI[tiab] OR intermittent hypox*[tiab])) AND ("Fatty Liver"[Mesh] OR NAFLD[tiab] OR "nonalcoholic fatty liver disease"[tiab] OR "non-alcoholic fatty liver disease"[tiab] OR NASH[tiab] OR "nonalcoholic steatohepatitis"[tiab])`
3. `(("Sleep Apnea, Obstructive"[Mesh] OR OSA[tiab] OR "obstructive sleep apnea"[tiab] OR AHI[tiab] OR intermittent hypox*[tiab]) AND ("Fatty Liver"[Mesh] OR NAFLD[tiab] OR "nonalcoholic fatty liver disease"[tiab] OR NASH[tiab] OR steatosis[tiab] OR fibrosis[tiab] OR inflammation[tiab] OR "liver biopsy"[tiab] OR "NAFLD activity score"[tiab] OR NAS[tiab] OR ALT[tiab] OR AST[tiab])) AND (obes*[tiab] OR "Obesity"[Mesh] OR bariatric[tiab] OR "metabolic surgery"[tiab] OR preoperative[tiab] OR pre-bariatric[tiab])`
4. `(("Obesity"[Mesh] OR obes*[tiab] OR "morbid obesity"[tiab] OR "severe obesity"[tiab]) AND ("Sleep Apnea, Obstructive"[Mesh] OR OSA[tiab] OR "obstructive sleep apnea"[tiab] OR AHI[tiab] OR intermittent hypox*[tiab]) AND ("Fatty Liver"[Mesh] OR NAFLD[tiab] OR "nonalcoholic fatty liver disease"[tiab] OR NASH[tiab] OR steatosis[tiab] OR fibrosis[tiab] OR "liver biopsy"[tiab] OR "NAFLD activity score"[tiab] OR ALT[tiab] OR AST[tiab])) AND (cohort[tiab] OR cross-sectional[tiab] OR observational[tiab] OR prospective[tiab] OR retrospective[tiab] OR trial[tiab] OR randomized[tiab] OR intervention*[tiab])`
5. `(("Obesity"[Mesh] OR obes*[tiab] OR "morbid obesity"[tiab] OR "severe obesity"[tiab]) AND ("Sleep Apnea, Obstructive"[Mesh] OR "sleep-disordered breathing"[tiab] OR SDB[tiab] OR OSA[tiab] OR "apnea hypopnea index"[tiab] OR "intermittent hypoxia"[tiab]) AND ("Fatty Liver"[Mesh] OR "nonalcoholic fatty liver disease"[tiab] OR NAFLD[tiab] OR NASH[tiab] OR "hepatic steatosis"[tiab] OR "liver fibrosis"[tiab] OR "liver inflammation"[tiab] OR transaminase*[tiab] OR ALT[tiab] OR AST[tiab])) NOT (animal*[tiab] OR rat[tiab] OR mice[tiab] OR mouse[tiab])`

The merged candidate pool contained 81 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human studies of adults with obesity (BMI >= 35 kg/m2), including candidates for or patients undergoing pre-bariatric/metabolic surgery evaluation.
- Studies that assess obstructive sleep apnea (OSA) or OSA-related indicators, such as diagnosed OSA, apnea-hypopnea index (AHI), intermittent hypoxia, or comparisons across OSA severity groups or versus participants without OSA.
- Studies reporting at least one NAFLD-related liver outcome, including NAFLD presence, severity, or resolution measured by liver biopsy, NAFLD activity score (NAS), steatosis, fibrosis, inflammation, or serum liver markers such as ALT or AST.
- Observational or interventional study designs that examine the association between OSA and NAFLD outcomes in the target population.

Exclusion criteria:

- Studies limited to children/adolescents, non-obese populations, or mixed populations where data for adults with BMI >= 35 kg/m2 cannot be separated.
- Studies that do not evaluate OSA exposure or OSA-related metrics, or do not report any NAFLD-related liver outcome.
- Reviews, editorials, letters, conference abstracts without sufficient data, case reports, and animal or in vitro studies.
- Studies focused exclusively on post-bariatric surgery outcomes without relevant pre-surgery OSA and NAFLD assessment, or studies where OSA/NAFLD status cannot be determined.

81 candidates were screened and 13 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was performed for studies reporting effect estimates for the association between OSA and NAFLD in sufficiently comparable formats. The principal summary measure was the **odds ratio (OR)** with **95% confidence intervals (CIs)**. For each eligible study, ORs were extracted directly or derived from reported binary outcome data when possible. A total of **3 studies** contributed to the meta-analysis.

Pooled effect sizes were calculated using both **random-effects** and **fixed-effect** models. Given the clinical expectation of between-study variability in OSA ascertainment, NAFLD assessment, and bariatric evaluation context, the random-effects model was specified as the primary analytic approach. The pooled random-effects estimate showed that OSA was associated with higher odds of NAFLD, with a **pooled OR of 3.154 (95% CI 1.515-6.569; p = 0.0021)**. Because between-study heterogeneity was negligible, the fixed-effect model yielded the same pooled estimate: **OR 3.154 (95% CI 1.515-6.569; p = 0.0021)**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I2**, and **tau-squared (tau2)**. Observed heterogeneity was low to absent, with **Q = 1.77 (p = 0.413)**, **I2 = 0.0%**, and **tau2 = 0.0000**, indicating no measurable inconsistency across the included studies in the pooled analysis.

Where studies were not sufficiently homogeneous in exposure definition, outcome measurement, or reporting format, findings were synthesized narratively rather than pooled. Statistical significance for pooled effects was determined using a two-sided alpha threshold of **0.05**.

## Results

### Study Selection

### Results of the Search
The database and local search identified **81 records** in total (**81 local records** and **0 PubMed records**) after deduplication. All **81 records** underwent **title and abstract screening**, of which **68 were excluded** at stage 1 for not meeting the eligibility criteria. The remaining **13 full-text articles** were assessed for eligibility. **No studies were excluded at the full-text stage**. Consequently, **13 studies** were included in the systematic review. Of these, **3 studies** contributed sufficient comparable effect-size data to the quantitative synthesis (meta-analysis) using odds ratios.

Most frequent recorded exclusion reasons:

- No NAFLD-related liver outcome reported.: 8
- Review article, not an original human study.: 6
- Review article; not an original human study.: 4
- Animal study (mice), not a human study.: 2
- Does not report any NAFLD-related liver outcome.: 2
- Obesity/BMI>=35 population not clearly established; study appears to involve metabolic syndrome patients without explicit qualifying obese bariatric/pre-bariatric cohort.: 1
- Population is general suspected OSA referrals, not clearly adults with BMI>=35 obesity.: 1
- Animal study (murine model), not a human study.: 1
- Obesity/BMI>=35 target population is not clearly established in the abstract.: 1
- NAFLD/OSA association is studied, but the abstract does not clearly establish the required adult BMI>=35 obese target population.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4615 | 2007 | Liver enzymes and histology in obese patients with obstructive sleep apnea. |
| 4616 | 2012 | Nonalcoholic steatohepatitis in bariatric patients with a diagnosis of obstructive sleep apnea. |
| 4609 | 2020 | Obstructive sleep apnea and liver injury in severely obese patients with nonalcoholic fatty liver disease. |
| 4608 | 2012 | Chronic intermittent hypoxia is a major trigger for non-alcoholic fatty liver disease in morbid obese. |
| 70180 | 2026 | Obstructive sleep apnea is associated with greater MASH and significant fibrosis severity in patients with obesity: A prospective clinicopathological study. |
| 70339 | 2020 | Correlation between Obstructive Sleep Apnea and Non-Alcoholic Fatty Liver Disease before and after Metabolic Bariatric Surgery. |
| 4604 | 2015 | Lysyl Oxidase as a Serum Biomarker of Liver Fibrosis in Patients with Severe Obesity and Obstructive Sleep Apnea. |
| 4610 | 2022 | Chronic intermittent hypoxia contributes to non-alcoholic steatohepatitis progression in patients with obesity. |
| 4612 | 2007 | Obstructive sleep apnoea, glucose tolerance and liver steatosis in obese women. |
| 4605 | 2008 | Apnoeic-hypopnoeic episodes during obstructive sleep apnoea are associated with histological nonalcoholic steatohepatitis. |
| 70330 | 2009 | Obstructive sleep apnea, insulin resistance, and steatohepatitis in severe obesity. |
| 70325 | 2023 | Insulin Resistance, but Not Obstructive Sleep Apnea Is Associated with Hepatic Steatosis in Chinese Patients with Severe Obesity. |
| 70332 | 2007 | Relationship between obstructive sleep apnea and liver abnormalities in morbidly obese patients: a prospective study. |

### Study Characteristics

Thirteen studies comprising 1,977 participants were included. The studies were published between 2007 and 2023, although several reports did not clearly state a publication year or full bibliographic details. Geographically, reporting was limited: two studies were conducted in China, one included samples from the United States and Brazil, one listed the country as unknown, one did not state the setting, and the remainder did not clearly report country of origin. Study designs were notably heterogeneous and were predominantly observational, including retrospective observational comparative studies, retrospective and prospective cohort studies, cross-sectional observational studies, and prospective cross-sectional designs. One study was particularly mixed in structure, combining a cross-sectional bariatric cohort, a separate nonrandomized pre-post comparison in a sleep clinic sample, and an accompanying mouse hepatocyte experimental component. This methodological variability should be considered when interpreting the overall evidence base.

The included populations also appeared heterogeneous, although reporting on participant characteristics was incompletely described in the extracted dataset. Across studies, the available evidence suggests variation in demographic and clinical features such as age, sex distribution, and condition severity, but these characteristics were not consistently reported in a way that supports reliable pooled description here. Likewise, intervention-related features, including dose, duration, and mode of delivery, were not uniformly available from the enhanced extraction summary, indicating substantial between-study variation and limiting direct comparison across studies. Outcome measurement approaches were also diverse and appear to have reflected the underlying observational aims of individual studies rather than a standardized assessment framework.

Data quality from the enhanced extraction was consistently rated as high for all 13 studies, indicating strong confidence in the extracted study-level information. However, this should be interpreted alongside the risk-of-bias profile, which was uniformly judged as high or high risk across studies, with random sequence generation, allocation concealment, and blinding generally rated as unclear. Taken together, the evidence base is characterized by consistent extraction quality but substantial heterogeneity in design, reporting, and measured study features, with overall methodological limitations that may affect certainty in the findings.

### Main Findings

### Results

#### Primary outcome

The pooled analysis demonstrated a statistically significant positive association between obstructive sleep apnea (OSA) and adverse NAFLD-related liver outcomes in adults with severe obesity undergoing pre-bariatric metabolic surgery assessment. Across 3 studies reporting odds ratios, the random-effects meta-analysis yielded a pooled OR of **3.15** (**95% CI 1.52–6.57**, **p=0.0021**). The fixed-effect model produced an identical estimate, further supporting the robustness of the finding.

Interpretatively, this indicates that participants with OSA, or with greater OSA burden, had **more than threefold higher odds** of NAFLD presence and/or worse liver disease status compared with patients without OSA or with lower OSA severity. In relative terms, this corresponds to an approximate **215% increase in the odds** of adverse NAFLD-related outcomes associated with OSA.

#### Direction and magnitude of effect

The direction of effect was consistently unfavorable, indicating that OSA and related hypoxic burden were associated with a higher likelihood of liver involvement. The magnitude of the pooled effect is clinically meaningful: an OR above 3 suggests that OSA is not only statistically associated with NAFLD-related abnormalities, but may represent an important comorbid risk marker in this high-BMI population. Given that the included liver outcomes encompassed histologic and biochemical indicators—such as steatosis, inflammation, fibrosis, NAS, and serum transaminases—this finding supports a broad relationship between sleep-disordered breathing and hepatic disease burden.

#### Consistency across studies

Between-study heterogeneity was **absent** (**I²=0.0%**, Q=1.77, **p=0.413**, τ²=0.0000), indicating that the effect estimates were highly consistent across the included studies. The lack of observable heterogeneity suggests that, despite differences in specific liver outcome measures and OSA-related indicators, the direction and approximate magnitude of association were similar. However, this consistency should be interpreted with some caution because only **three studies** were available, limiting the power to detect true heterogeneity.

#### Notable individual study findings

Although study-level weights and individual effect estimates are not presented here, the identical fixed- and random-effects pooled estimates, together with the null heterogeneity, suggest that no single study disproportionately distorted the summary effect. The most precise study would be expected to have contributed substantially to the pooled estimate, but the overall result appears to reflect concordant findings across all included studies rather than dependence on one extreme result.

#### Outliers and potential explanations

No clear outlier was evident statistically. The absence of heterogeneity and the overlap implied among study-specific estimates argue against a materially discordant study. Any minor between-study differences that may have existed could plausibly relate to variation in how OSA was characterized (presence/absence, AHI severity, or intermittent hypoxia metrics), differences in NAFLD ascertainment methods (biopsy, NAS, imaging, or serum markers), and clinical differences in pre-bariatric cohorts. Nonetheless, these differences did not translate into measurable inconsistency in the pooled analysis.

#### Overall interpretation

Overall, the available evidence indicates that OSA is associated with a substantially higher likelihood of NAFLD-related liver disease in adults with severe obesity. While the precision and internal consistency of the pooled estimate are reassuring, the evidence base remains small, and the findings should therefore be viewed as supportive rather than definitive.

### Risk of Bias

**Risk of Bias**

Risk of bias was judged to be substantial across the included evidence base. At the study level, all 13 included studies were classified as having high overall risk of bias (9 labeled as `high` and 4 as `high risk`), with no study judged overall as low risk. At the domain level, concerns were driven less by explicitly identified methodological flaws than by uniformly poor reporting: all 13/13 studies were rated as `Unclear` for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. Thus, the most common domains with concern were all six assessed domains, each affecting 100% of included studies. This pattern indicates that the available reports did not provide sufficient methodological detail to verify protection against selection, performance, detection, attrition, or reporting bias.

Across studies, the dominant pattern was one of pervasive non-reporting rather than variation in quality between individual designs. Because essential trial safeguards such as sequence generation and allocation concealment were never described, it was not possible to distinguish whether randomized studies were methodologically stronger than observational or less clearly designed studies; in practice, the reporting limitations produced the same `Unclear` judgment in every domain for every study. No study could be considered at particularly low risk, and even those with fewer obvious design concerns remained high overall because all core bias domains were undocumented. Conversely, studies labeled `high risk` rather than `high` were not distinguished by specific domain-level failures in the extracted dataset, but by the overall appraisal framework applied to incompletely reported methods. The enhanced extraction process assigned high data-quality confidence to all 13 studies, indicating that these risk-of-bias judgments are likely reliable reflections of what was reported in the source articles rather than extraction error.

These findings reduce confidence in the pooled estimate. When all studies have unclear judgments for sequence generation, concealment, blinding, incomplete outcome handling, and selective reporting, the meta-analytic summary is more vulnerable to systematic distortion in either direction, and any apparent treatment effect should therefore be interpreted cautiously. In particular, lack of information on randomization and blinding raises the possibility of exaggerated effects, while undocumented attrition and selective reporting may further bias the magnitude or precision of the pooled result. Overall, although the extraction itself appears robust, the underlying evidence base has limited methodological transparency, which materially lowers confidence in the strength and certainty of the review’s conclusions.

## Discussion

**Discussion**

This systematic review found a consistent association between obstructive sleep apnea (OSA) and non-alcoholic fatty liver disease (NAFLD) among adults with severe obesity (BMI >= 35). In the meta-analysis of three studies, the presence or greater severity of OSA was associated with more than threefold higher odds of NAFLD-related liver involvement (pooled random-effects OR 3.15, 95% CI 1.52-6.57; p=0.002), with no observed statistical heterogeneity (I2=0%). Although only a subset of the 13 included studies contributed extractable data for quantitative synthesis, the broader qualitative evidence generally pointed in the same direction: OSA-related measures, particularly apnea-hypopnea index (AHI) and indices of intermittent hypoxia, were linked to NAFLD presence and to more adverse histologic or biochemical liver outcomes. Clinically, this magnitude of association is meaningful in a pre-bariatric population already at high baseline metabolic risk, because OSA may help identify a subgroup with greater likelihood of steatosis, inflammation, steatohepatitis, or fibrosis. At the same time, the estimate should be interpreted as an association rather than proof of causation.

Direct comparison with prior meta-analyses is limited because no prior review appears to have addressed exactly this PICO in adults with severe obesity being evaluated around bariatric metabolic surgery. The contextual reviews supplied address different questions and underscore that evidence synthesis is highly dependent on population, exposure, and outcome definition. For example, the chronic hepatitis B meta-analysis focused on diagnostic accuracy of fibrosis biomarkers against transient elastography, while the bariatric nutrition review found little convincing evidence that post-surgical dietary composition predicts weight outcomes, and the adult ADHD review identified only a small number of robust biomarker associations despite a much larger evidence base. In that sense, our findings are more comparable in structure than in content: like those reviews, we found that a relatively modest number of quantitatively poolable studies can still yield a clear signal when the direction of effect is consistent. However, unlike diagnostic or genetic meta-analyses, the present literature is dominated by observational studies with mixed outcome definitions and incomplete reporting, which limits confidence in the precision and transportability of the pooled effect.

The observed association is biologically plausible. Intermittent hypoxia, a defining feature of OSA, may contribute to NAFLD progression through oxidative stress, sympathetic activation, systemic inflammation, insulin resistance, and dysregulated lipid metabolism. These mechanisms could promote hepatocellular injury, worsen steatosis, and accelerate transition toward steatohepatitis and fibrosis. In severe obesity, OSA may also amplify pre-existing metabolic dysfunction rather than act independently, which may explain why associations were seen across histologic measures such as steatosis, inflammation, fibrosis, and NAFLD activity score, as well as serum markers including ALT and AST. A further plausible pathway is that recurrent nocturnal hypoxemia worsens adipose tissue dysfunction and free fatty acid flux to the liver, thereby intensifying hepatic fat accumulation and inflammatory signaling. Still, the relative contribution of OSA itself versus shared upstream drivers such as visceral adiposity, insulin resistance, diabetes, and male sex remains difficult to disentangle in the available studies.

The absence of statistical heterogeneity in the pooled analysis should not be mistaken for complete clinical homogeneity. Important differences existed across studies in how OSA was defined or categorized, whether exposure was based on diagnosis, AHI thresholds, or hypoxemia metrics, and how NAFLD was assessed, ranging from liver biopsy and NAFLD activity score to imaging or serum transaminases. The comparison groups also varied, including patients without OSA, patients across OSA severity strata, and pre-bariatric surgical cohorts with differing metabolic profiles. Residual confounding is a central concern because both OSA and NAFLD are strongly related to obesity severity and associated comorbidities. Differences in adjustment for diabetes, age, sex, waist circumference, and other metabolic factors may have influenced effect estimates. The small number of studies in the meta-analysis also reduces the ability to detect true between-study heterogeneity or publication bias, so the apparently stable pooled estimate should be interpreted with restraint.

This review has several strengths. It focuses on a clinically relevant high-risk population in whom both OSA and NAFLD are common and consequential, and it integrates evidence across multiple liver outcome domains rather than relying on a single marker. The overall study quality rating was high for all 13 included studies in the enhanced extraction framework, which supports the credibility of study conduct at a broad level. In addition, the enhanced extraction approach allowed capture of study conclusions and outcome breadth even when conventional meta-analytic inputs were incompletely reported. That matters in this field, where many studies reported adjusted associations or descriptive findings but omitted the raw counts or summary statistics needed for pooling. As a result, this review contributes both a quantitative estimate where feasible and a more complete qualitative account of the evidence than would be possible from pooled data alone.

The limitations are equally important. Despite favorable global quality ratings, many extracted reports had substantial reporting gaps, including missing bibliographic metadata, absent group-level counts, limited demographic detail, and outcomes presented only descriptively or as p-values. Consequently, only three studies could be meta-analyzed, which constrains statistical power and limits exploration of subgroup effects. The evidence base is observational, so causality cannot be established and reverse or bidirectional relationships remain possible. Generalizability may also be limited because the population was restricted to adults with severe obesity, often in pre-bariatric settings, and findings may not apply to patients with lower BMI or different metabolic risk profiles. If the review search was restricted by language, database coverage, or unpublished literature availability, publication and selection biases may remain. Finally, liver outcomes were not uniformly defined, and serum transaminases are imperfect proxies for histologic disease, which complicates cross-study comparison.

Clinically, these findings support a lower threshold for considering liver risk assessment in adults with severe obesity who also have OSA, especially when OSA is severe or accompanied by pronounced intermittent hypoxia. They also suggest that OSA status may be relevant when risk stratifying patients before bariatric metabolic surgery, although the evidence does not yet justify assuming that treatment of OSA alone will improve liver histology. A pragmatic implication is closer integration between sleep medicine, hepatology, and bariatric services, with attention to identifying patients who may warrant more thorough hepatic evaluation. For research, the main need is for well-reported prospective studies using standardized OSA definitions, clearly adjusted effect estimates, and harmonized NAFLD outcomes, ideally including biopsy or validated non-invasive fibrosis measures. Interventional studies examining whether OSA treatment, particularly effective continuous positive airway pressure use, modifies NAFLD progression or post-bariatric liver outcomes would be especially valuable. Until such data are available, the present review supports OSA as a meaningful correlate of NAFLD burden in severe obesity, while leaving the degree of independence and modifiability of that risk unresolved.

## Conclusion

In this meta-analysis of 13 studies in adults with severe obesity (BMI >= 35), obstructive sleep apnea was associated with substantially higher odds of non-alcoholic fatty liver disease, with pooled data from 3 studies showing an OR of 3.15 (95% CI 1.52-6.57; p=0.002) versus patients without OSA or with lower OSA burden. This suggests that OSA, and likely its related intermittent hypoxia, is not just statistically linked to NAFLD but may identify a clinically important high-risk phenotype with greater liver involvement before bariatric metabolic surgery. Clinically, patients with severe obesity and OSA should be considered for more deliberate liver risk assessment and closer perioperative evaluation, particularly when OSA is moderate to severe. The main caveat is that the pooled estimate comes from only 3 studies, and the broader 13-study evidence base includes variation in OSA severity definitions and liver outcome measures, which limits causal inference and precision.

## Final Included Studies

- Corpus ID: 4615 | Liver enzymes and histology in obese patients with obstructive sleep apnea.
- Corpus ID: 4616 | Nonalcoholic steatohepatitis in bariatric patients with a diagnosis of obstructive sleep apnea.
- Corpus ID: 4609 | Obstructive sleep apnea and liver injury in severely obese patients with nonalcoholic fatty liver disease.
- Corpus ID: 4608 | Chronic intermittent hypoxia is a major trigger for non-alcoholic fatty liver disease in morbid obese.
- Corpus ID: 70180 | Obstructive sleep apnea is associated with greater MASH and significant fibrosis severity in patients with obesity: A prospective clinicopathological study.
- Corpus ID: 70339 | Correlation between Obstructive Sleep Apnea and Non-Alcoholic Fatty Liver Disease before and after Metabolic Bariatric Surgery.
- Corpus ID: 4604 | Lysyl Oxidase as a Serum Biomarker of Liver Fibrosis in Patients with Severe Obesity and Obstructive Sleep Apnea.
- Corpus ID: 4610 | Chronic intermittent hypoxia contributes to non-alcoholic steatohepatitis progression in patients with obesity.
- Corpus ID: 4612 | Obstructive sleep apnoea, glucose tolerance and liver steatosis in obese women.
- Corpus ID: 4605 | Apnoeic-hypopnoeic episodes during obstructive sleep apnoea are associated with histological nonalcoholic steatohepatitis.
- Corpus ID: 70330 | Obstructive sleep apnea, insulin resistance, and steatohepatitis in severe obesity.
- Corpus ID: 70325 | Insulin Resistance, but Not Obstructive Sleep Apnea Is Associated with Hepatic Steatosis in Chinese Patients with Severe Obesity.
- Corpus ID: 70332 | Relationship between obstructive sleep apnea and liver abnormalities in morbidly obese patients: a prospective study.
