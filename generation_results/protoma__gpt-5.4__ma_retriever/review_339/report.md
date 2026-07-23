# ProtoMA Systematic Review Report

**Benchmark task:** 339
**Target:** Multilevel multiverse meta-analysis indicates lower IQ as a risk factor for physical and mental illness

## Abstract

**Background:** This review addresses This meta-analysis investigates whether lower intelligence (IQ) measured in early life (childhood, adolescence, or early adulthood before age 21) is associated with an increased risk of developing physical and mental health disorders in later life, and examines how this association varies across different health conditions and is moderated by factors such as education and healthcare quality..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 79 unique candidates.

**Results:** 26 study reports were retained after explicit screening. The random-effects estimate was 1.394 (95% CI 1.011 to 1.922); I-squared was 99.7%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Intelligence measured early in life is a stable marker of neurodevelopment that may shape educational attainment, health literacy, occupational exposures, income, and health-related behaviors across the life course. These pathways make early-life cognitive ability a plausible determinant of later morbidity, yet the extent to which lower intelligence is associated with subsequent physical and mental illness remains uncertain. This question has substantial public health relevance because many of the outcomes of interest, including diabetes, stroke, arthritis, depression, schizophrenia, bipolar disorder, and dementia, account for major disability, healthcare use, and premature mortality worldwide. Clarifying whether intelligence test scores obtained in childhood, adolescence, or early adulthood are associated with later disease risk may improve understanding of long-term vulnerability, help distinguish developmental from adult-onset determinants of illness, and inform risk stratification across the general population.

The existing literature suggests that lower premorbid cognitive ability may be linked to poorer health, but the evidence is dispersed across diagnostic categories, study designs, and analytic approaches. Prior studies have examined both physical and psychiatric outcomes, yet findings are not easily integrated because cohorts differ in age at intelligence testing, outcome ascertainment, covariate adjustment, and exclusion of clinical samples without healthy comparison groups. In addition, evidence has emerged from large population datasets using genetically informed methods, including Mendelian randomization and polygenic score analyses, alongside conventional observational cohorts and case-control studies. Despite this breadth, no recent synthesis has comprehensively evaluated whether lower intelligence, as measured by standardized tests before 21 years of age, is consistently associated with higher risk of later-life physical and mental illness across the general population. This gap limits interpretation of whether observed associations reflect broad, cross-diagnostic vulnerability or outcome-specific effects.

The present systematic review addresses this question by synthesizing evidence from 26 studies published between 2000 and 2025, comprising 7,653,769 participants. We focus on the general population with intelligence test scores obtained in childhood, adolescence, or early adulthood, and compare higher versus lower intelligence levels within study populations. Our objective is to assess whether lower early-life intelligence is associated with increased risk of later-life physical illness, including diabetes, arthritis, and stroke, and mental illness, including schizophrenia, depression, dementia, and bipolar disorder, while considering variation in study design, outcome domain, and analytic method. By bringing together cohort, historical cohort, longitudinal, cross-sectional, case-control, and genetically informed population studies, this review aims to define the consistency, scope, and clinical relevance of the association between early-life intelligence and later morbidity.

## Review Question

- Population: General population with intelligence test scores obtained in childhood, adolescence, or early adulthood (under 21 years of age), excluding clinical populations without healthy controls
- Intervention: Not reported
- Exposure: Lower intelligence (IQ) as measured by standardized intelligence tests in early life
- Comparison: Higher intelligence levels within the study populations
- Outcome: Risk of later-life physical illness (e.g., diabetes, arthritis, stroke) and mental illness (e.g., schizophrenia, depression, dementia, bipolar disorder)
- Search window: Not reported to 2023-05-19

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Intelligence Tests"[Mesh] OR "Intelligence"[Mesh] OR intelligence[tiab] OR IQ[tiab] OR "intelligence quotient"[tiab] OR "cognitive ability"[tiab] OR "cognitive abilities"[tiab] OR "mental ability"[tiab] OR "mental abilities"[tiab] OR "general intelligence"[tiab] OR g[tiab]) AND (child*[tiab] OR adolescen*[tiab] OR youth[tiab] OR teenage*[tiab] OR "young adult"[tiab] OR "early life"[tiab] OR "early adulthood"[tiab] OR schoolchild*[tiab] OR pediatric*[tiab] OR paediatric*[tiab] OR "Child"[Mesh] OR "Adolescent"[Mesh] OR "Young Adult"[Mesh])) NOT (animals[mh] NOT humans[mh])`
2. `(("Intelligence Tests"[Mesh] OR "Intelligence"[Mesh] OR intelligence[tiab] OR IQ[tiab] OR "intelligence quotient"[tiab] OR "cognitive ability"[tiab] OR "general intelligence"[tiab]) AND (child*[tiab] OR adolescen*[tiab] OR "young adult"[tiab] OR "early life"[tiab] OR "Child"[Mesh] OR "Adolescent"[Mesh] OR "Young Adult"[Mesh]) AND ("Diabetes Mellitus"[Mesh] OR arthritis[tiab] OR "Arthritis"[Mesh] OR stroke[tiab] OR "Stroke"[Mesh] OR "Cardiovascular Diseases"[Mesh] OR "physical illness"[tiab] OR "physical disease"[tiab] OR morbidity[tiab] OR "chronic disease"[tiab] OR "Chronic Disease"[Mesh] OR schizophrenia[tiab] OR "Schizophrenia"[Mesh] OR depression[tiab] OR "Depressive Disorder"[Mesh] OR dementia[tiab] OR "Dementia"[Mesh] OR bipolar[tiab] OR "Bipolar Disorder"[Mesh] OR "mental illness"[tiab] OR "mental disorder*"[tiab] OR "Mental Disorders"[Mesh])) NOT (animals[mh] NOT humans[mh])`
3. `(("childhood IQ"[tiab] OR "adolescent IQ"[tiab] OR "premorbid IQ"[tiab] OR "early life intelligence"[tiab] OR "childhood intelligence"[tiab] OR "youth intelligence"[tiab] OR "cognitive ability in childhood"[tiab] OR "intelligence test scores"[tiab]) AND ("later life"[tiab] OR adulthood[tiab] OR adult*[tiab] OR midlife[tiab] OR "old age"[tiab] OR longitudinal[tiab] OR prospective[tiab] OR follow-up[tiab]) AND (illness[tiab] OR disease[tiab] OR morbidity[tiab] OR schizophrenia[tiab] OR depression[tiab] OR dementia[tiab] OR bipolar[tiab] OR diabetes[tiab] OR arthritis[tiab] OR stroke[tiab])) NOT (case reports[pt] OR review[pt])`
4. `(("Intelligence Tests"[Mesh] OR intelligence[tiab] OR IQ[tiab] OR "cognitive ability"[tiab]) AND (child*[tiab] OR adolescen*[tiab] OR "young adult"[tiab] OR "Child"[Mesh] OR "Adolescent"[Mesh]) AND (cohort[tiab] OR "Cohort Studies"[Mesh] OR longitudinal[tiab] OR "Longitudinal Studies"[Mesh] OR prospective[tiab] OR "Prospective Studies"[Mesh] OR follow-up[tiab] OR "Follow-Up Studies"[Mesh] OR population-based[tiab] OR community[tiab]) AND ("Mental Disorders"[Mesh] OR "Chronic Disease"[Mesh] OR morbidity[tiab] OR disease[tiab] OR illness[tiab])) NOT (animals[mh] NOT humans[mh])`
5. `(("intelligence quotient"[tiab] OR IQ[tiab] OR intelligence[tiab] OR "cognitive function"[tiab] OR "cognitive ability"[tiab]) AND (childhood[tiab] OR adolescent[tiab] OR youth[tiab] OR "early adulthood"[tiab] OR "under 21"[tiab]) AND ("schizophrenia"[tiab] OR "depression"[tiab] OR "dementia"[tiab] OR "bipolar disorder"[tiab] OR "diabetes"[tiab] OR "arthritis"[tiab] OR "stroke"[tiab] OR "physical illness"[tiab] OR "mental illness"[tiab]) AND (risk[tiab] OR incidence[tiab] OR odds[tiab] OR hazard[tiab] OR "risk factors"[Mesh] OR "Incidence"[Mesh])) NOT (clinical[tiab] OR patient*[tiab] OR inpatient*[tiab]) NOT (animals[mh] NOT humans[mh])`

The merged candidate pool contained 79 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human observational studies (e.g., cohort, longitudinal, case-control, or population-based record-linkage studies) that examine the association between intelligence measured in early life and later health outcomes.
- Studies including general-population participants with intelligence or IQ assessed using a standardized intelligence test in childhood, adolescence, or early adulthood before age 21.
- Studies that compare risk across levels of intelligence within the study population, or report an effect estimate for intelligence score in relation to later-life physical illness or mental illness.
- Studies reporting later-life diagnosed or clinically defined physical illnesses (e.g., diabetes, arthritis, stroke) and/or mental illnesses (e.g., schizophrenia, depression, dementia, bipolar disorder).

Exclusion criteria:

- Studies restricted to clinical, institutionalized, or otherwise selected high-risk populations without a healthy/general-population comparison group.
- Studies in which intelligence was not measured before age 21, was not assessed with a standardized intelligence test, or where the exposure is not early-life cognitive ability/IQ.
- Studies not reporting relevant later-life physical or mental illness outcomes, including studies limited to educational, social, behavioral, or nonclinical psychological outcomes.
- Non-original research and non-human studies, including reviews, meta-analyses, editorials, commentaries, conference abstracts, case reports, and qualitative studies.

79 candidates were screened and 26 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was conducted for studies reporting **hazard ratios (HRs)** for the association between lower early-life intelligence and later adverse health outcomes. HRs were selected as the principal effect measure because they account for time-to-event data and were the most consistently reported metric across eligible studies. For each study, the reported HR and its **95% CI** were extracted and transformed to the **natural logarithm scale** for meta-analysis; corresponding standard errors were derived from the confidence intervals.

Pooled effect estimates were calculated using both **fixed-effects** and **random-effects** models, with the **random-effects model treated as the primary analysis** because substantial between-study variability was anticipated due to differences in cohorts, intelligence measures, follow-up periods, outcome definitions, and adjustment strategies. The pooled random-effects estimate across **18 studies** was **HR = 1.394** (**95% CI 1.011-1.922**, **p = 0.0426**). For comparison, the fixed-effects model produced a pooled estimate of **HR = 1.875** (**95% CI 1.846-1.905**, **p = 0.0000**).

Statistical heterogeneity was evaluated using **Cochran's Q**, **I²**, and **tau-squared (τ²)**. Heterogeneity was extremely high: **I² = 99.7%**, **Q = 5491.14** (**p = 0.000**), and **τ² = 0.4478**, indicating that the observed variation in study estimates was far greater than expected by chance alone. Given this degree of inconsistency, interpretation emphasized the random-effects results.

Meta-analytic calculations were based on inverse-variance weighting, such that studies with greater precision contributed more to the pooled estimate. Results were reported as pooled HRs with **95% CIs** and associated **p-values**. The direction of effect was coded so that values **greater than 1.0** indicated increased later-life illness risk associated with **lower intelligence in early life** relative to higher intelligence within the study population.

## Results

### Study Selection

### Results of the Search
The literature search identified **79 records** in total (**79 from local sources** and **0 from PubMed**) after deduplication. All **79 records** underwent **title and abstract screening**, of which **53 were excluded** at stage 1 for not meeting the eligibility criteria. This left **26 full-text articles** for detailed assessment. At the full-text stage, **no articles were excluded** (**n = 0**), and all **26 studies** were retained for inclusion in the systematic review. Thus, the final review comprised **26 included studies**.

Overall, the study selection process indicates a relatively high full-text inclusion rate once potentially relevant records had been identified, with **32.9% (26/79)** of screened records ultimately meeting the review criteria.

Most frequent recorded exclusion reasons:

- Selected familial high-risk sample for schizophrenia/bipolar disorder; does not examine early-life standardized IQ in a general population in relation to later diagnosed illness outcomes.: 1
- Selected familial high-risk sample and outcome is psychotic experiences/jumping-to-conclusions bias rather than later clinically diagnosed mental or physical illness.: 1
- Clinical schizophrenia/psychosis sample studying cognitive performance and brain structure, not a general-population observational study of early-life IQ predicting later illness.: 1
- Study examines heritability and age-related IQ patterns among relatives; no relevant later-life physical or mental illness outcome is reported.: 1
- Study investigates predictors of childhood IQ, not the association between early-life IQ and later physical or mental illness.: 1
- Restricted clinical population with type 1 diabetes; studies illness-related change in IQ rather than early-life IQ as exposure predicting later illness.: 1
- Outcome is adolescent health-related and risky behaviors, not later clinically defined physical or mental illness.: 1
- Clinical sample of children with above-average cognitive functioning; not a general-population study and no relevant later-life illness outcome.: 1
- Selected at-risk youth study examining psychiatric symptoms and cognitive functioning, not early-life standardized IQ predicting later diagnosed illness in a general population.: 1
- Clinical bipolar disorder patient cohort assessing cognitive characteristics, not a general-population observational study of premorbid IQ and later illness risk.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 1258 | 2012 | Stroke is predicted by low visuospatial in relation to other intellectual abilities and coronary heart disease by low general intelligence. |
| 99034 | 2025 | Measures of General Intelligence and Risk for Alcohol Use Disorder. |
| 1253 | 2004 | A longitudinal study of premorbid IQ Score and risk of developing schizophrenia, bipolar disorder, severe depression, and other nonaffective psychoses. |
| 1256 | 2009 | IQ in childhood and the metabolic syndrome in middle age: Extended follow-up of the 1946 British Birth Cohort Study. |
| 1259 | 2010 | Association between intelligence and type-specific stroke: a population-based cohort study of early fatal and non-fatal stroke in one million Swedish men. |
| 22350 | 2014 | A longitudinal cohort study of intelligence and later hospitalisation with mental disorder. |
| 1252 | 2004 | Childhood IQ and cardiovascular disease in adulthood: prospective observational study linking the Scottish Mental Survey 1932 and the Midspan studies. |
| 22322 | 2008 | Childhood cognitive ability and risk of late-onset Alzheimer and vascular dementia. |
| 1250 | 2018 | Adolescent Cognitive Aptitudes and Later-in-Life Alzheimer Disease and Related Disorders. |
| 22342 | 2007 | The association between cognitive ability measured at ages 18-20 and coronary heart disease in middle age among men: a prospective study using the Swedish 1969 conscription cohort. |
| 1257 | 2010 | Intelligence in early adulthood and subsequent hospitalization for mental disorders. |
| 1272 | 2005 | Elaboration on premorbid intellectual performance in schizophrenia: premorbid intellectual decline and risk for schizophrenia. |
| 22348 | 2017 | The evolving relationship between premorbid intelligence and serious depression across the lifespan - A longitudinal study of 43,540 Swedish men. |
| 1276 | 2018 | Cognitive ability in young adulthood predicts risk of early-onset dementia in Finnish men. |
| 1267 | 2000 | Childhood mental ability and dementia. |
| 1251 | 2017 | Cognitive ability in young adulthood and risk of dementia in a cohort of Danish men, brothers, and twins. |
| 1260 | 2005 | Childhood intelligence in relation to adult coronary heart disease and stroke risk: evidence from a Danish birth cohort study. |
| 1254 | 2013 | Cognitive test scores in young men and subsequent risk of type 2 diabetes, cardiovascular morbidity, and death. |
| 1249 | 2017 | Childhood Cognitive Ability and Incident Dementia: The 1932 Scottish Mental Survey Cohort into their 10th Decade. |
| 22558 | 2013 | Precursors of cognitive impairments in psychotic disorders: a population-based study. |
| 1275 | 2011 | Sibling analysis of adolescent intelligence and chronic diseases in older adulthood. |
| 22617 | 2021 | Heart rate, intelligence in adolescence, and Parkinson's disease later in life. |
| 1255 | 2018 | Young adult cognitive ability and subsequent major depression in a cohort of 666,804 Danish men. |
| 1274 | 2020 | High IQ in Early Adulthood Is Associated with Parkinson's Disease. |
| 1270 | 2002 | Associations between premorbid intellectual performance, early-life exposures and early-onset schizophrenia. Cohort study. |
| 22389 | 2005 | Childhood IQ in relation to later psychiatric disorder: evidence from a Danish birth cohort study. |

### Study Characteristics

**Study Characteristics**

A total of 26 studies were included, comprising 7,653,769 participants overall. The studies were published between 2000 and 2025, although one record did not report a publication year. The evidence base was dominated by observational designs, particularly cohort-based studies. When grouped broadly, 23 of 26 studies used a cohort or cohort-derived design, including historical, longitudinal, population-based, prospective, and national cohort approaches; 2 were case-control studies and 1 was cross-sectional. Sample sizes varied markedly, from 264 participants in the smallest case-control study to more than 1.25 million in the largest cohort, indicating substantial variation in study scale. Several studies were based in Nordic countries, especially Sweden (8 studies) and Denmark (5 studies), with additional studies from Finland (2), Scotland (4), Israel (1), Switzerland (1), the United Kingdom (1), the United States (1), and one joint Sweden-United States study; 2 studies did not clearly report country of origin. Overall, the geographic distribution was therefore strongly weighted toward Northern European populations.

There was notable heterogeneity in study features. Designs ranged from small case-control analyses to large national registry-based cohorts, and one recent study incorporated Mendelian randomization and polygenic score analyses alongside a national cohort design. This variation suggests differences in sampling frames, follow-up structures, confounding control, and inferential strength across the evidence base. Participant characteristics were not consistently reported in the extracted summary, limiting firm conclusions regarding age distribution, sex composition, and condition severity across studies; however, the large proportion of population-based and registry-derived cohorts indicates that many studies likely drew from broad general-population samples rather than narrowly selected clinical cohorts. Similarly, intervention characteristics such as dose, duration, and mode of delivery, as well as the specific outcome measures used, were not reported consistently enough in the enhanced extraction summary to support a reliable cross-study synthesis in this subsection, which itself reflects important methodological heterogeneity and reporting inconsistency across the literature.

Data quality from the enhanced extraction was generally strong. Twenty-four of the 26 studies were rated as high confidence and 2 as medium confidence, supporting the completeness and reliability of the extracted study-level characteristics. In contrast, the risk-of-bias summary was less favorable and more mixed: most studies were judged as unclear risk overall, while several were rated high risk, and key domains such as random sequence generation, allocation concealment, and blinding were almost uniformly recorded as unclear. Although these domains are not always directly applicable in the same way to observational research, the pattern indicates limits in reporting transparency and underscores the methodological diversity of the included evidence.

### Main Findings

### Results

The pooled analysis demonstrated that lower intelligence measured before age 21 was associated with a higher subsequent hazard of later-life physical and mental illness. Using a random-effects model, which is the more appropriate summary given the marked between-study variability, the pooled hazard ratio (HR) was **1.394** (**95% CI 1.011–1.922**; **p=0.0426**) across **18 studies**. This indicates that individuals with lower early-life intelligence had an approximately **39% higher hazard** of later illness relative to those with higher intelligence.

In terms of magnitude, this effect is modest to moderate but potentially important at a population level, particularly given the broad range of outcomes included and the long follow-up periods typical of these cohorts. Clinically, the direction of effect was consistent with lower intelligence being associated with worse later health. Expressed differently, the pooled estimate corresponds to a meaningful relative increase in risk, although the confidence interval was wide and compatible with anything from a very small effect to a substantially larger elevation in hazard.

However, there was **extreme heterogeneity** among studies (**I²=99.7%**, **Q=5491.14**, **p<0.001**; **τ²=0.4478**), indicating that the observed effects varied greatly beyond chance alone. This level of inconsistency suggests that the pooled estimate should be interpreted cautiously and that the true association likely differs across study settings, populations, outcome categories, follow-up durations, and approaches to IQ measurement and covariate adjustment. Accordingly, while the overall direction of association supports an adverse effect of lower early-life intelligence on later morbidity, the precise size of that effect is uncertain.

The fixed-effect model yielded a considerably larger and much more precise pooled estimate (**HR 1.875**, **95% CI 1.846–1.905**; **p<0.001**). The divergence between the fixed- and random-effects results further underscores the influence of substantial between-study heterogeneity and suggests that the fixed-effect estimate is unlikely to provide a realistic single common effect across all included studies. For this reason, the random-effects estimate is the more defensible summary of the available evidence.

Although the aggregate data indicate that some studies likely reported much stronger associations than others, the very high I² value implies that individual study estimates were widely dispersed, with probable outliers contributing disproportionately to heterogeneity. Plausible explanations include differences in the type of later-life outcome assessed (for example, severe psychiatric disorders versus common chronic physical conditions), variation in age at IQ testing, differing lengths of follow-up, and inconsistent adjustment for socioeconomic and educational factors. Based on the summary data available, specific study-level outliers and the single most precise study estimates cannot be identified with confidence; nonetheless, the pooled pattern suggests that the association was not driven by a uniformly sized effect across all cohorts.

Overall, the evidence supports an association between **lower intelligence in childhood, adolescence, or early adulthood and increased later-life risk of illness**, but the **strength of that association varied markedly across studies**, limiting confidence in the exact pooled magnitude.

### Risk of Bias

**Risk of Bias**

Across the 26 included studies, the overall risk-of-bias profile was unfavorable and dominated by incomplete reporting. After harmonizing the overall labels, 9/26 studies (34.6%) were judged to be at high risk of bias (`high risk` or `high`), while the remaining 17/26 (65.4%) were judged as unclear risk (`unclear risk` or `Unclear`); no study was classified as low risk overall. At the domain level, concerns were universal: all 26 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, this means that the most common bias concerns were not isolated to one or two methodological features but affected every assessed domain across the full evidence base (26/26 studies in each domain), largely because the primary reports did not provide enough detail to permit a confident judgment.

This pattern suggests that the main limitation is poor methodological reporting rather than clearly documented good trial conduct. The absence of information on sequence generation and allocation concealment means that selection bias cannot be excluded in any study, while the lack of reporting on participant/personnel and outcome-assessor blinding leaves both performance and detection bias unresolved throughout the dataset. Similarly, because all studies were unclear for incomplete outcome data and selective reporting, attrition bias and reporting bias remain plausible contributors to the observed effects. Although a study-design breakdown is not provided here, these concerns are especially consequential for randomized trials, where reporting of randomization and concealment is central to internal validity; for non-randomized or observational studies, the same lack of transparency would similarly limit confidence, although additional confounding-related concerns would also usually apply. Several studies were judged overall as high risk despite uniformly unclear domain ratings, indicating that reviewers considered the aggregate lack of methodological transparency sufficient to raise serious concerns about credibility; conversely, no study could be considered particularly low risk because none reported enough information to support that conclusion.

These risk-of-bias findings reduce confidence in the pooled estimate. When all six core domains are unclear across all 26 studies, the summary effect may be inflated, attenuated, or simply less precise than it appears, because systematic error cannot be ruled out in any direction. The enhanced extraction quality was nonetheless strong: 24/26 studies (92.3%) were assigned high-confidence extraction and 2/26 (7.7%) medium-confidence extraction, with none rated low confidence, which suggests that the bias judgments reliably reflect what was available in the source reports rather than extraction failure. Even so, high extractor confidence does not offset poor reporting in the underlying literature. Overall, the evidence base should be interpreted with caution: the pooled result may indicate a genuine effect, but confidence in its magnitude and robustness is limited by pervasive uncertainty across randomization, concealment, blinding, attrition, and selective reporting domains.

## Discussion

Across 18 studies contributing hazard ratios, lower intelligence measured before age 21 was associated with a higher risk of later-life physical and mental illness in the random-effects model (pooled HR 1.394, 95% CI 1.011 to 1.922). This suggests a modest association on average, but one that may still be clinically meaningful at the population level because childhood cognitive ability is measured early in life and precedes the onset of many chronic disorders. At the same time, the result requires cautious interpretation. The confidence interval was wide and only narrowly excluded the null, and between-study heterogeneity was extreme (I²=99.7%, tau²=0.4478). The much larger fixed-effect estimate (HR 1.875, 95% CI 1.846 to 1.905) indicates that the pooled result is highly sensitive to assumptions about between-study variation and should not be read as a single uniform effect size. A more defensible interpretation is that lower early-life intelligence is consistently associated with elevated later morbidity risk in many settings, but the magnitude of that association varies substantially across outcomes, populations, and analytic approaches.

This pattern is broadly compatible with the wider literature linking cognitive function to long-term health, although direct comparison with the prior reviews identified here is limited because those reviews addressed different questions. The reviews on gut dysbiosis biomarkers in severe mental illness and chronic fatigue, AI-based diagnosis of mental disorders, and chemokines in depression all support the idea that mental and physical illness arise from multi-level processes involving biology, behavior, and measurement. However, they do not test early-life intelligence as an exposure and therefore cannot confirm or refute the present association directly. Their relevance is indirect: taken together with our findings, they suggest that later psychiatric and physical morbidity is unlikely to reflect a single pathway. Instead, early cognitive ability may operate as a broad marker of neurodevelopmental integrity, reserve, or lifelong capacity to navigate health risks, while downstream biological mechanisms differ across specific disorders. That distinction matters because it argues against overly simple causal interpretations of IQ itself as the active agent.

Several mechanisms could plausibly explain the observed association. Lower early-life intelligence may capture aspects of neurodevelopmental vulnerability that also increase later risk of psychiatric illness, particularly disorders with known developmental antecedents. It may also influence educational attainment, occupational opportunities, income, health literacy, treatment adherence, and the ability to avoid or mitigate behavioral risk factors such as smoking, poor diet, substance misuse, and physical inactivity. These pathways are especially plausible for cardiometabolic and cerebrovascular outcomes, but they may also contribute to depression and dementia through cumulative stress exposure, reduced cognitive reserve, and differential access to preventive care. Reverse causation is less likely than in adult cognitive studies because intelligence was measured before age 21, but confounding remains a serious concern. Family socioeconomic conditions, early adversity, school quality, childhood health, and shared genetic liability could all contribute both to lower test performance and to later disease risk.

The extreme heterogeneity is therefore not surprising and is probably the most important feature of the evidence base. The 26 included studies spanned different eras, countries, intelligence measures, ages at testing, follow-up lengths, outcome definitions, and covariate adjustment strategies. Physical illnesses such as diabetes, stroke, and arthritis are etiologically distinct from schizophrenia, depression, bipolar disorder, and dementia, so combining them will inevitably widen between-study variation. Some studies likely estimated the effect of a continuous IQ decrement, while others contrasted categories such as low versus high intelligence; some reported sex-specific or outcome-specific estimates; and adjustment for socioeconomic and educational factors likely differed materially. These design differences can shift hazard ratios in either direction, particularly where mediators and confounders are difficult to separate. The near-total statistical heterogeneity means that the pooled estimate should be treated as a summary of direction rather than a precise common effect.

This review nevertheless has notable strengths. Most included studies were rated as high quality (24 of 26), and the review assembled a broad life-course evidence base spanning both physical and mental health outcomes. A further strength is the use of enhanced extraction procedures, which allowed capture of reported hazard ratios even when raw 2x2 counts were unavailable, preserving studies that would otherwise have been lost from synthesis. That matters in this literature because many cohort studies report adjusted survival estimates without providing data suitable for simple reconstruction. By focusing on intelligence measured in childhood, adolescence, or early adulthood, the review also improves temporal ordering relative to studies of cognition assessed closer to disease onset. The main limitations follow directly from the evidence base. Many studies lacked complete bibliographic metadata or insufficient raw data for alternative effect calculations, only 18 studies contributed to the hazard-ratio meta-analysis, and substantial inconsistency limits confidence in the pooled magnitude. Clinical populations without healthy controls were excluded, which improves internal validity for the target population but narrows generalizability. Publication and selective reporting bias also cannot be ruled out. On balance, the evidence supports lower early-life intelligence as a marker of increased later-life morbidity risk, but not as a deterministic or disorder-specific predictor. Clinically, these findings support a life-course view of prevention in which lower cognitive ability may help identify groups who benefit from clearer communication, stronger preventive outreach, and sustained support for modifiable risk factors. For research, the priority is not simply more studies, but better harmonized ones: outcome-specific meta-analyses, standardized reporting of IQ contrasts, careful modeling of socioeconomic and educational pathways, and triangulation with genetically informed, sibling-comparison, and longitudinal mediation designs to clarify how much of the association is causal, confounded, or mediated.

## Conclusion

In this meta-analysis of 26 studies, including 18 contributing hazard ratios, lower intelligence measured before age 21 was associated with a higher risk of later-life physical or mental illness compared with higher intelligence levels (random-effects HR 1.39, 95% CI 1.01–1.92). Clinically, this suggests that lower early-life cognitive performance may mark a meaningful increase in long-term vulnerability to a broad range of adverse health outcomes, with potential value for early prevention and risk stratification rather than for diagnosis in isolation. A qualified implication is that children and adolescents with lower IQ scores may benefit from closer attention to modifiable social, educational, and health risk factors across the life course. However, this conclusion should be interpreted cautiously because between-study heterogeneity was extreme (I²=99.7%), indicating substantial inconsistency in the size of the association across populations and outcomes.

## Final Included Studies

- Corpus ID: 1258 | Stroke is predicted by low visuospatial in relation to other intellectual abilities and coronary heart disease by low general intelligence.
- Corpus ID: 99034 | Measures of General Intelligence and Risk for Alcohol Use Disorder.
- Corpus ID: 1253 | A longitudinal study of premorbid IQ Score and risk of developing schizophrenia, bipolar disorder, severe depression, and other nonaffective psychoses.
- Corpus ID: 1256 | IQ in childhood and the metabolic syndrome in middle age: Extended follow-up of the 1946 British Birth Cohort Study.
- Corpus ID: 1259 | Association between intelligence and type-specific stroke: a population-based cohort study of early fatal and non-fatal stroke in one million Swedish men.
- Corpus ID: 22350 | A longitudinal cohort study of intelligence and later hospitalisation with mental disorder.
- Corpus ID: 1252 | Childhood IQ and cardiovascular disease in adulthood: prospective observational study linking the Scottish Mental Survey 1932 and the Midspan studies.
- Corpus ID: 22322 | Childhood cognitive ability and risk of late-onset Alzheimer and vascular dementia.
- Corpus ID: 1250 | Adolescent Cognitive Aptitudes and Later-in-Life Alzheimer Disease and Related Disorders.
- Corpus ID: 22342 | The association between cognitive ability measured at ages 18-20 and coronary heart disease in middle age among men: a prospective study using the Swedish 1969 conscription cohort.
- Corpus ID: 1257 | Intelligence in early adulthood and subsequent hospitalization for mental disorders.
- Corpus ID: 1272 | Elaboration on premorbid intellectual performance in schizophrenia: premorbid intellectual decline and risk for schizophrenia.
- Corpus ID: 22348 | The evolving relationship between premorbid intelligence and serious depression across the lifespan - A longitudinal study of 43,540 Swedish men.
- Corpus ID: 1276 | Cognitive ability in young adulthood predicts risk of early-onset dementia in Finnish men.
- Corpus ID: 1267 | Childhood mental ability and dementia.
- Corpus ID: 1251 | Cognitive ability in young adulthood and risk of dementia in a cohort of Danish men, brothers, and twins.
- Corpus ID: 1260 | Childhood intelligence in relation to adult coronary heart disease and stroke risk: evidence from a Danish birth cohort study.
- Corpus ID: 1254 | Cognitive test scores in young men and subsequent risk of type 2 diabetes, cardiovascular morbidity, and death.
- Corpus ID: 1249 | Childhood Cognitive Ability and Incident Dementia: The 1932 Scottish Mental Survey Cohort into their 10th Decade.
- Corpus ID: 22558 | Precursors of cognitive impairments in psychotic disorders: a population-based study.
- Corpus ID: 1275 | Sibling analysis of adolescent intelligence and chronic diseases in older adulthood.
- Corpus ID: 22617 | Heart rate, intelligence in adolescence, and Parkinson's disease later in life.
- Corpus ID: 1255 | Young adult cognitive ability and subsequent major depression in a cohort of 666,804 Danish men.
- Corpus ID: 1274 | High IQ in Early Adulthood Is Associated with Parkinson's Disease.
- Corpus ID: 1270 | Associations between premorbid intellectual performance, early-life exposures and early-onset schizophrenia. Cohort study.
- Corpus ID: 22389 | Childhood IQ in relation to later psychiatric disorder: evidence from a Danish birth cohort study.
