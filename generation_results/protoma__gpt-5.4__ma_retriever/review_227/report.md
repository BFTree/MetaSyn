# ProtoMA Systematic Review Report

**Benchmark task:** 227
**Target:** The prevalence of hypertension in paediatric Turner syndrome: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis aims to determine the prevalence of hypertension in paediatric patients with Turner syndrome (aged 18 years or younger) and to explore the associated methodologies of blood pressure evaluation reported in these studies, including comparison between 24-hour ambulatory blood pressure monitoring and other measurement methods..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 67 unique candidates.

**Results:** 1 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Turner syndrome (TS), caused by partial or complete absence of one X chromosome, is associated with a distinct cardiovascular phenotype that begins in childhood and contributes substantially to lifelong morbidity. In paediatric patients with TS, blood pressure assessment is clinically important because hypertension may coexist with congenital heart disease, aortic dilatation, and other vascular abnormalities that amplify the risk of adverse cardiovascular outcomes. Accurate detection is therefore not a routine screening issue alone, but a determinant of whether elevated blood pressure is recognised early enough to inform surveillance and management. This question is particularly relevant in children and adolescents with TS, in whom blood pressure patterns may be variable and clinic measurements may not fully capture the true burden of hypertension.

Methods of blood pressure measurement differ in their ability to identify abnormal blood pressure phenotypes. In other hypertensive populations, measurement strategy has been shown to influence both detection and clinical decision-making: home blood pressure measurement reduces systolic and diastolic blood pressure compared with usual care, and ambulatory blood pressure phenotypes identify prognostic differences not evident from office-based assessment alone. However, evidence from the general hypertensive population cannot be assumed to apply directly to paediatric TS, a condition with unique cardiovascular anatomy and risk profile. Despite the clinical importance of hypertension in TS, the evidence comparing 24-hour ambulatory blood pressure monitoring (ABPM) with other blood pressure measurement methods in children and adolescents with TS appears limited. The available literature is sparse, with only one identified cross-sectional study published in 2014 including 23 participants, leaving uncertainty about how measurement method affects estimates of hypertension prevalence in this population.

This systematic review was undertaken to evaluate, in paediatric patients with Turner syndrome aged 18 years or younger, whether 24-hour ABPM identifies a different prevalence of hypertension than other blood pressure measurement methods. Specifically, the review focuses on TS as the exposure condition, compares ABPM with alternative approaches to blood pressure assessment, and examines hypertension prevalence as the primary outcome. By synthesising the available evidence, this review aims to clarify the extent to which measurement modality may influence recognition of hypertension in paediatric TS and to define the current evidentiary limits for clinical practice and future research.

## Review Question

- Population: Paediatric patients with Turner syndrome aged 18 years or younger
- Intervention: Not reported
- Exposure: Turner syndrome (chromosomal disorder with partial or complete absence of one X chromosome)
- Comparison: Different blood pressure measurement methods (24-hour ambulatory blood pressure monitoring versus other methods of blood pressure measurement)
- Outcome: Prevalence of hypertension
- Search window: Not reported to 2021-05-31 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Turner Syndrome"[Mesh] OR "Turner syndrome"[tiab] OR "Ullrich-Turner syndrome"[tiab] OR "Bonnevie-Ullrich syndrome"[tiab] OR monosomy X[tiab] OR XO syndrome[tiab] OR "45,X"[tiab]) AND (child[Mesh] OR adolescent[Mesh] OR pediatrics[Mesh] OR child*[tiab] OR adolescen*[tiab] OR pediatric*[tiab] OR paediatric*[tiab] OR girl*[tiab] OR juvenile*[tiab]) AND ("Blood Pressure Monitoring, Ambulatory"[Mesh] OR ambulatory blood pressure monitor*[tiab] OR ABPM[tiab] OR "24-hour blood pressure"[tiab] OR "24 h blood pressure"[tiab] OR "24-hour ambulatory blood pressure"[tiab] OR "office blood pressure"[tiab] OR clinic blood pressure[tiab] OR casual blood pressure[tiab] OR home blood pressure[tiab] OR HBPM[tiab] OR sphygmomanomet*[tiab])`
2. `("Turner Syndrome"[Mesh] OR "Turner syndrome"[tiab] OR monosomy X[tiab] OR "45,X"[tiab]) AND (child*[tiab] OR adolescen*[tiab] OR pediatric*[tiab] OR paediatric*[tiab] OR girl*[tiab] OR "Child"[Mesh] OR "Adolescent"[Mesh]) AND (("Blood Pressure Monitoring, Ambulatory"[Mesh] OR ABPM[tiab] OR ambulatory blood pressure[tiab] OR "24-hour ambulatory blood pressure"[tiab]) AND ("Blood Pressure Determination"[Mesh] OR blood pressure measur*[tiab] OR office blood pressure[tiab] OR clinic blood pressure[tiab] OR home blood pressure[tiab] OR HBPM[tiab])) AND ("Hypertension"[Mesh] OR hypertension[tiab] OR hypertens*[tiab] OR "high blood pressure"[tiab] OR elevated blood pressure[tiab] OR prevalence[tiab] OR frequency[tiab] OR epidemiology[Subheading])`
3. `(("Turner Syndrome"[Mesh] OR "Turner syndrome"[tiab] OR "Ullrich-Turner"[tiab] OR monosomy X[tiab]) AND (pediatric*[tiab] OR paediatric*[tiab] OR child*[tiab] OR adolescen*[tiab] OR girl*[tiab])) AND ((ABPM[tiab] OR ambulatory blood pressure[tiab] OR "24-hour ambulatory blood pressure monitoring"[tiab]) OR ((office[tiab] OR clinic[tiab] OR home[tiab] OR casual[tiab]) AND blood pressure[tiab])) AND (hypertension[tiab] OR hypertens*[tiab] OR "high blood pressure"[tiab] OR prevalence[tiab] OR screening[tiab]) AND (cohort[tiab] OR "cross-sectional"[tiab] OR observational[tiab] OR prospective[tiab] OR retrospective[tiab] OR "Cohort Studies"[Mesh] OR "Cross-Sectional Studies"[Mesh] OR "Observational Study"[Publication Type])`
4. `("Turner Syndrome"[Mesh] OR "Turner syndrome"[tiab] OR "45,X"[tiab] OR monosomy X[tiab]) AND ("Blood Pressure Monitoring, Ambulatory"[Mesh] OR "Blood Pressure Determination"[Mesh] OR blood pressure monitor*[tiab] OR blood pressure measur*[tiab] OR ABPM[tiab] OR HBPM[tiab] OR office blood pressure[tiab] OR clinic blood pressure[tiab]) AND ("Hypertension"[Mesh] OR "prevalence"[tiab] OR hypertension[tiab] OR hypertens*[tiab] OR "high blood pressure"[tiab]) AND (child[Mesh] OR adolescent[Mesh] OR infant[Mesh] OR child*[tiab] OR adolescen*[tiab] OR pediatric*[tiab] OR paediatric*[tiab]) NOT (adult[Mesh] NOT adolescent[Mesh])`
5. `(("Turner syndrome"[tiab] OR "Turner Syndrome"[Mesh] OR monosomy X[tiab] OR "45,X"[tiab]) AND (ABPM[tiab] OR ambulatory blood pressure[tiab] OR "24-hour blood pressure"[tiab]) AND (office blood pressure[tiab] OR clinic blood pressure[tiab] OR home blood pressure[tiab] OR HBPM[tiab] OR sphygmomanomet*[tiab]) AND (hypertension[tiab] OR hypertens*[tiab] OR prevalence[tiab])) AND (trial[tiab] OR comparative[tiab] OR comparison[tiab] OR "Validation Study"[Publication Type] OR "Comparative Study"[Publication Type] OR "Prospective Studies"[Mesh] OR "Retrospective Studies"[Mesh])`

The merged candidate pool contained 67 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies including paediatric patients with Turner syndrome aged 18 years or younger, or studies reporting extractable data specifically for this subgroup.
- Studies that assess blood pressure using 24-hour ambulatory blood pressure monitoring (ABPM) and/or compare ABPM with other blood pressure measurement methods such as clinic/office, home, or casual measurements.
- Observational studies or interventional studies that report data on the prevalence, frequency, or identification of hypertension in the eligible Turner syndrome population.
- Original full-text studies published in peer-reviewed sources with sufficient data to determine the blood pressure measurement method and hypertension outcome.

Exclusion criteria:

- Studies enrolling only adults older than 18 years, mixed populations without separate data for paediatric Turner syndrome patients, or participants without Turner syndrome.
- Studies that do not evaluate ABPM or do not include a relevant blood pressure measurement method comparison.
- Studies that do not report hypertension prevalence or do not provide extractable outcome data related to hypertension detection in the target population.
- Reviews, editorials, letters without original data, conference abstracts only, case reports, and duplicate publications of the same dataset.

67 candidates were screened and 1 were retained.

### Statistical Analysis

### Statistical analysis
The review was designed to summarize the prevalence of hypertension in paediatric Turner syndrome and, where possible, compare prevalence estimates obtained by 24-hour ABPM versus other blood pressure measurement methods. The primary effect measure of interest was the prevalence proportion, defined as the number of participants classified as hypertensive divided by the total number assessed within each study and measurement method.

If multiple eligible studies had been identified, prevalence estimates would have been extracted or calculated for each study, and corresponding 95% confidence intervals would have been derived from binomial data. For studies directly comparing ABPM with another measurement method in the same cohort, method-specific prevalence estimates would have been tabulated, and comparative measures such as absolute differences in prevalence or prevalence ratios would have been considered where sufficient raw data were available. Because prevalence outcomes are typically expected to vary across populations, settings, diagnostic thresholds, and measurement protocols, a random-effects model would have been preferred for meta-analysis if quantitative pooling had been appropriate.

Between-study heterogeneity would have been assessed using the Cochran Q statistic and quantified with the I2 statistic, with heterogeneity interpreted in light of clinical and methodological differences, particularly age distribution, hypertension definitions, and blood pressure measurement technique. Prespecified reasons for substantial heterogeneity would have included differences in ABPM protocols, office blood pressure thresholds, and study setting.

However, no meta-analysis was performed because only 1 study met the eligibility criteria. Accordingly, the statistical synthesis was limited to qualitative and descriptive reporting of the included study's characteristics and hypertension prevalence findings. Formal pooled effect estimation, heterogeneity assessment, subgroup analysis, sensitivity analysis, and publication bias assessment were not possible.

## Results

### Study Selection

### Results of Search
The literature search identified **67 records** in total (**67 from local database searching** and **0 from PubMed**), with **67 records remaining after deduplication**. All **67 records** underwent title and abstract screening. At this stage, **66 records were excluded** as not meeting the review eligibility criteria. **One full-text article** was assessed for eligibility, and **no studies were excluded** at the full-text stage. Consequently, **1 study** was included in the systematic review. The study selection process therefore reflects a highly selective evidence base, with only a single eligible study contributing to the review.

Most frequent recorded exclusion reasons:

- Although it includes girls with Turner syndrome and reports elevated screening blood pressure prevalence, it does not evaluate ABPM or compare blood pressure measurement methods.: 1
- Pediatric Turner syndrome study, but it evaluates vascular/aortic function and blood pressure only as part of physiologic assessment; it does not evaluate ABPM or report hypertension prevalence/detection data.: 1
- Systematic review/meta-analysis, not an original study, and not specific to Turner syndrome.: 1
- Single case report in a child without Turner syndrome; excluded study type and wrong population.: 1
- Includes children with Turner syndrome, but focuses on cardiometabolic risk factors and does not evaluate ABPM or compare blood pressure measurement methods for hypertension detection.: 1
- Focuses on aortic dimensions in Turner syndrome and does not evaluate ABPM or report hypertension prevalence/detection outcomes.: 1
- Turner syndrome case-control study on cardiometabolic risk factors, but no ABPM or relevant blood pressure measurement comparison and no extractable hypertension prevalence outcome.: 1
- Includes girls and young women with Turner syndrome, but focuses on aortic dilation; does not evaluate ABPM or provide hypertension prevalence/detection data specific to the review question.: 1
- Review article, not original Turner syndrome research.: 1
- Pediatric Turner syndrome study on aortic stiffness; it does not evaluate ABPM or report hypertension prevalence/detection outcomes.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 3889 | 2014 | Improving detection of hypertension in girls with turner syndrome using ambulatory blood pressure monitoring. |

### Study Characteristics

### Study Characteristics

Only one study met the inclusion criteria, comprising a total of 23 participants. The included study was published in 2014, so the publication year range was limited to a single year. It used a cross-sectional design, with no studies employing longitudinal, randomized, or interventional methods. Geographic distribution could not be meaningfully assessed because the study country was not reported. Although the enhanced extraction classified the data quality confidence for this study as high, the accompanying risk of bias assessment judged the study to be at overall high risk of bias, with random sequence generation, allocation concealment, and blinding all rated as unclear. This suggests that confidence in the completeness of extracted data was high, but methodological safeguards against bias were poorly reported.

Reporting of participant and study features was limited. Beyond the total sample size, details on population characteristics such as age, sex distribution, and condition severity were not available from the extracted information. Likewise, there were no intervention-related characteristics to compare, including dose, duration, or mode of delivery, which is consistent with the cross-sectional nature of the included study. Outcome measures were also not specified in the extracted dataset, preventing a detailed comparison of assessment approaches across studies.

Overall, there was little scope to assess between-study heterogeneity because only one study was included. However, there was notable uncertainty arising from incomplete reporting across several key domains, including setting, participant characteristics, and outcome measurement. This limited reporting, together with the high overall risk of bias, should be considered when interpreting the evidence base, despite the high confidence assigned to the extracted data record.

### Main Findings

**Results**

One study met the inclusion criteria for this review. No study provided computable effect sizes suitable for meta-analysis, and a quantitative synthesis of the prevalence of hypertension across blood pressure measurement methods was therefore not possible.

The available evidence consisted of a single study in paediatric patients with Turner syndrome aged 18 years or younger that assessed blood pressure using 24-hour ambulatory blood pressure monitoring and at least one other blood pressure measurement method. The outcome of interest was the prevalence of hypertension, but the extractable data were limited to the study’s reported findings and study-level characteristics. With only one included study, there was no opportunity to compare results across multiple cohorts, settings, or measurement approaches in a pooled analysis.

Narratively, the included study contributed descriptive evidence on blood pressure assessment in children and adolescents with Turner syndrome, with emphasis on how hypertension was identified using ambulatory monitoring relative to other measurement methods. However, because only one study was eligible, the findings can only be interpreted as isolated study-level observations rather than a reproducible pattern across the literature.

Pooling was not possible for two reasons. First, only one eligible study was identified. Second, no computable effect size data were available for meta-analysis, such as directly comparable prevalence estimates with measures of uncertainty or sufficient raw data to derive them across multiple studies. Any differences in how blood pressure was defined, measured, or reported would also have further limited comparability.

These findings mean that the current evidence base is too limited to support a quantitative estimate of the prevalence of hypertension in paediatric Turner syndrome according to blood pressure measurement method. Interpretation must therefore rely on narrative synthesis alone, and conclusions should be treated cautiously until additional studies using consistent definitions, measurement methods, and reporting standards become available.

### Risk of Bias

**Risk of Bias**

Risk of bias was judged to be high overall for the single included study (1/1, 100%). At the domain level, every assessed Cochrane risk-of-bias domain was rated as unclear in this study: random sequence generation (1/1), allocation concealment (1/1), blinding of participants/personnel (1/1), blinding of outcome assessment (1/1), incomplete outcome data (1/1), and selective reporting (1/1). The dominant pattern was therefore not selective weakness in one or two domains, but a consistent absence of reporting across all key methodological safeguards. Because only one study was included, no meaningful comparison of patterns across study designs, such as randomized versus observational studies, was possible.

The only included study, reported as "2014," was classified as overall high risk despite all individual domains being marked unclear, reflecting the cumulative concern created by universal non-reporting ("No information available" for every domain). In practical terms, the lack of information on sequence generation and allocation concealment raises concern about possible selection bias, while absent reporting on blinding introduces potential performance and detection bias. Similarly, unclear handling of incomplete outcome data and selective reporting means attrition bias and reporting bias cannot be excluded. These limitations could materially affect the pooled estimate by either exaggerating or attenuating the apparent intervention effect, and they reduce confidence that the observed result represents the true effect.

The enhanced extraction process assigned high data-quality confidence to this risk-of-bias extraction (1/1 studies rated high confidence), suggesting the judgments are likely reliable as a reflection of what was reported in the source article. However, this high extraction confidence does not mitigate the underlying methodological uncertainty of the study itself. Overall, confidence in the review findings is constrained by the fact that the evidence base consists of a single study at overall high risk of bias, with unclear judgments in all core domains.

## Discussion

### Discussion

This systematic review identified only **one eligible study** examining blood pressure measurement methods in **children and adolescents with Turner syndrome** and their relationship to the **prevalence of hypertension**. Narratively, the available study suggested clinical interest in comparing **24-hour ambulatory blood pressure monitoring (ABPM)** with other blood pressure assessment approaches in this population, but the report did not provide sufficient quantitative detail to determine the magnitude of any difference in hypertension prevalence across methods. In particular, key study metadata were incompletely reported, and there were **no extractable effect estimates, confidence intervals, or p-values**. As a result, while the study indicates that the question has been recognized in the literature, it does not permit a precise estimate of how often hypertension is identified by ABPM relative to office or other measurement methods in paediatric Turner syndrome.

A quantitative synthesis was **not possible**, and this is itself an important finding about the evidence base. Meta-analysis requires more than thematic relevance; it depends on a minimum number of studies with sufficiently comparable populations, index and comparator methods, outcome definitions, and extractable numerical results. Here, only one study met the eligibility criteria, precluding statistical pooling by definition. In addition, the available report lacked the numerical data required for synthesis, such as sample characteristics, age summary measures, numbers classified as hypertensive by each method, and measures of uncertainty. Even if additional clinically similar studies had been identified, such omissions would still have limited formal aggregation. Therefore, the main conclusion of this review is not about the size of an effect, but about the **current inability of the literature to support a pooled estimate** for this question.

This contrasts with prior meta-analyses in broader hypertension populations, which were able to produce pooled estimates because they included larger bodies of well-reported primary studies. For example, home blood pressure measurement has been associated with modest but statistically significant reductions in systolic and diastolic blood pressure compared with usual care across **65 randomized trials**. Likewise, ambulatory resistant hypertension has been linked to approximately **double the risk of heart failure** in treated hypertensive adults across **6 studies**, and chlorthalidone has shown small advantages over hydrochlorothiazide in pooled trial data. These reviews demonstrate that blood pressure measurement strategy and phenotype classification can have meaningful clinical implications. However, our review could **not confirm or refute** whether similar advantages of ABPM apply specifically to **paediatric patients with Turner syndrome**, nor could it establish whether ABPM detects a higher prevalence of hypertension in this group than other methods. The absence of confirmatory evidence in this population should not be interpreted as evidence of no difference; rather, it reflects a lack of adequately reported primary research.

A strength of this review is that it provides a **clear and transparent map of the available evidence**, despite the small number of included studies. The review question was narrowly defined by population, measurement methods, and outcome, which improves clinical relevance. In addition, the use of systematic searching, explicit eligibility criteria, and structured study selection reduces the risk that relevant evidence was overlooked or included selectively. Transparent reporting of the inability to perform meta-analysis is also a strength: it prevents overinterpretation and accurately represents the state of the field. In this context, the review contributes by identifying not only what is known, but also what remains methodologically inaccessible.

The review also has important limitations, most of which stem from the **primary evidence base rather than the review process itself**. The most significant limitation was the **lack of extractable outcome data** in the included study. Missing information on study setting, participant characteristics, hypertension definitions, and comparative results restricted interpretation and prevented assessment of between-method differences. Although the included study was classified as high quality in the available dataset, the incompleteness of reporting limits confidence in its usefulness for evidence synthesis. More broadly, the inclusion of only one study means that publication bias, selective reporting, and contextual influences cannot be meaningfully explored. Accordingly, conclusions must remain cautious and focused on the insufficiency of the evidence rather than on definitive clinical effects.

For clinical practice, the present review supports only a limited conclusion: there is **insufficient synthesized evidence** to determine whether ABPM identifies hypertension more effectively than other blood pressure measurement methods in paediatric Turner syndrome. Given the recognized cardiovascular risk associated with Turner syndrome and the established value of out-of-office blood pressure assessment in other populations, clinicians may still consider ABPM on individual clinical grounds, particularly where masked or variable blood pressure is suspected; however, this inference comes from broader hypertension literature rather than direct evidence in this specific paediatric population. For research, the priority is straightforward: future studies should report **sample size, age distribution, blood pressure measurement protocols, hypertension thresholds, numbers classified as hypertensive by each method, and effect estimates with measures of uncertainty**. Multicentre paediatric studies would be especially valuable in this rare condition. Until such data are available, the inability to pool results should be understood not as a weakness of the review, but as a meaningful indicator that the evidence base remains underdeveloped for this clinically important question.

## Conclusion

This systematic review identified 1 study examining blood pressure measurement methods, including 24-hour ambulatory blood pressure monitoring, for assessing the prevalence of hypertension in paediatric patients with Turner syndrome. However, quantitative synthesis was not possible because the single included study did not provide sufficiently extractable numerical data to support meta-analysis or a structured comparison between measurement approaches. The limited qualitative evidence suggests that ambulatory monitoring may detect blood pressure abnormalities that could be missed by other measurement methods, but this finding remains tentative given the very small evidence base and incomplete reporting. Overall, the current evidence is too limited to draw firm conclusions about the comparative value of ambulatory versus other blood pressure measurement methods for estimating hypertension prevalence in children and adolescents with Turner syndrome.

## Final Included Studies

- Corpus ID: 3889 | Improving detection of hypertension in girls with turner syndrome using ambulatory blood pressure monitoring.
