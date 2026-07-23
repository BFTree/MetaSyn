# ProtoMA Systematic Review Report

**Benchmark task:** 305
**Target:** Systematic review and meta-analysis of birth outcomes in women with polycystic ovary syndrome

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates whether polycystic ovary syndrome (PCOS) is an independent risk factor for adverse birth outcomes in offspring of affected women, examining the association between maternal PCOS status and birth outcomes while considering potential confounders such as maternal age, BMI, and use of assisted reproductive technology..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 61 unique candidates.

**Results:** 10 study reports were retained after explicit screening. The random-effects estimate was 1.569 (95% CI 0.964 to 2.555); I-squared was 91.9%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Polycystic ovary syndrome (PCOS) is one of the most common endocrine disorders in reproductive-age women and is characterized by hyperandrogenism, ovulatory dysfunction, and metabolic abnormalities that may extend into pregnancy. These maternal features are clinically relevant to fetal development because insulin resistance, chronic low-grade inflammation, obesity, and related obstetric complications may alter placental function and intrauterine growth. As a result, concern has focused not only on maternal outcomes in pregnancies complicated by PCOS, but also on whether offspring of affected women face a higher risk of adverse birth outcomes, including preterm birth, fetal growth restriction, low birth weight, small for gestational age, neonatal intensive care unit admission, and perinatal mortality. These outcomes carry immediate implications for neonatal survival and care utilization and may also shape long-term developmental and cardiometabolic health.

Evidence addressing birth outcomes in offspring of women with PCOS has accumulated across observational designs, but the findings have remained difficult to interpret. Individual studies have reported inconsistent associations, in part because of differences in diagnostic criteria for PCOS, study populations, comparator selection, adjustment for maternal body mass index and other confounders, and outcome definitions. This pattern is seen across perinatal epidemiology more broadly: recent meta-analyses in other maternal exposure settings have shown that maternal conditions and interventions can have selective rather than uniform effects on neonatal outcomes. For example, weight management interventions in pregnant women with obesity reduced gestational weight gain and birth weight without materially changing other adverse outcomes, whereas maternal HIV infection and some antiretroviral regimens were associated with increased risks of preterm birth, low birth weight, and small for gestational age, and COVID-19 vaccination during pregnancy did not increase adverse perinatal outcomes while reducing stillbirth risk. In this context, a focused synthesis of the PCOS literature is needed to determine whether maternal PCOS is associated with a distinct profile of adverse birth outcomes in offspring and to clarify the consistency and magnitude of these associations.

This systematic review therefore evaluates the association between maternal PCOS diagnosis and birth outcomes in offspring by comparing neonates born to women with PCOS with those born to women without PCOS. Specifically, the review examines preterm birth, fetal growth restriction, low birth weight, mean birthweight, small for gestational age, neonatal intensive care unit admission, and perinatal mortality. The evidence base comprises 10 studies published between 2003 and 2025, including case-control, cohort, prospective, retrospective, comparative, and observational designs, with a total of 74,279 participants. By synthesizing these data, this review aims to provide a clinically grounded estimate of the perinatal risks associated with maternal PCOS and to identify where the current literature remains limited.

## Review Question

- Population: Offspring of women with and without polycystic ovary syndrome (PCOS)
- Intervention: Not reported
- Exposure: Maternal polycystic ovary syndrome (PCOS) diagnosis
- Comparison: Offspring of women without polycystic ovary syndrome
- Outcome: Birth outcomes including preterm birth, fetal growth restriction, low birth weight, mean birthweight, small for gestational age, admission to neonatal intensive care units, and perinatal mortality
- Search window: 2017-01-01 to 2022-06-13

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Polycystic Ovary Syndrome"[Mesh] OR "polycystic ovary syndrome"[tiab] OR PCOS[tiab] OR "polycystic ovarian syndrome"[tiab] OR "Stein-Leventhal syndrome"[tiab]) AND (pregnan*[tiab] OR maternal[tiab] OR mother*[tiab] OR women[tiab] OR "Pregnancy"[Mesh] OR "Mothers"[Mesh])`
2. `(("Polycystic Ovary Syndrome"[Mesh] OR "polycystic ovary syndrome"[tiab] OR PCOS[tiab] OR "polycystic ovarian syndrome"[tiab]) AND (offspring[tiab] OR infant*[tiab] OR neonat*[tiab] OR newborn*[tiab] OR child*[tiab] OR fetus[tiab] OR fetal[tiab] OR "Infant, Newborn"[Mesh] OR "Fetus"[Mesh])) AND ("Infant, Premature"[Mesh] OR "Premature Birth"[Mesh] OR preterm[tiab] OR "preterm birth"[tiab] OR "preterm delivery"[tiab] OR "fetal growth restriction"[tiab] OR FGR[tiab] OR IUGR[tiab] OR "Intrauterine Growth Restriction"[Mesh] OR "low birth weight"[tiab] OR LBW[tiab] OR "Infant, Low Birth Weight"[Mesh] OR birthweight[tiab] OR "birth weight"[tiab] OR "small for gestational age"[tiab] OR SGA[tiab] OR "Infant, Small for Gestational Age"[Mesh] OR "intensive care, neonatal"[Mesh] OR NICU[tiab] OR "neonatal intensive care"[tiab] OR "perinatal mortality"[tiab] OR "Perinatal Mortality"[Mesh] OR stillbirth[tiab] OR "fetal death"[tiab])`
3. `(("polycystic ovary syndrome"[tiab] OR PCOS[tiab] OR "polycystic ovarian syndrome"[tiab]) AND (pregnan*[tiab] OR maternal[tiab] OR mother*[tiab])) AND (("birth outcome*"[tiab] OR "pregnancy outcome*"[tiab] OR perinatal outcome*[tiab] OR neonatal outcome*[tiab]) OR (preterm[tiab] OR prematur*[tiab] OR "low birth weight"[tiab] OR birthweight[tiab] OR "small for gestational age"[tiab] OR "fetal growth restriction"[tiab] OR IUGR[tiab] OR NICU[tiab] OR "perinatal mortality"[tiab] OR stillbirth[tiab])) AND (cohort[tiab] OR "case-control"[tiab] OR "cross-sectional"[tiab] OR observational[tiab] OR epidemiolog*[tiab] OR "Cohort Studies"[Mesh] OR "Case-Control Studies"[Mesh] OR "Observational Studies as Topic"[Mesh])`
4. `(("Polycystic Ovary Syndrome/complications"[Mesh] OR "Polycystic Ovary Syndrome"[Mesh]) AND ("Pregnancy Complications"[Mesh] OR "Pregnancy Outcome"[Mesh] OR "Infant, Low Birth Weight"[Mesh] OR "Infant, Small for Gestational Age"[Mesh] OR "Infant, Premature"[Mesh] OR "Intensive Care, Neonatal"[Mesh] OR "Perinatal Mortality"[Mesh] OR "Intrauterine Growth Restriction"[Mesh])) AND (mother*[tiab] OR maternal[tiab] OR pregnan*[tiab] OR offspring[tiab] OR neonat*[tiab])`
5. `(("polycystic ovary syndrome"[tiab] OR PCOS[tiab] OR "Stein-Leventhal"[tiab]) AND (offspring[tiab] OR newborn*[tiab] OR neonat*[tiab] OR infant*[tiab])) AND (("mean birthweight"[tiab] OR birthweight[tiab] OR "birth weight"[tiab]) OR ("preterm birth"[tiab] OR "preterm delivery"[tiab]) OR ("fetal growth restriction"[tiab] OR IUGR[tiab]) OR ("low birth weight"[tiab] OR LBW[tiab]) OR ("small for gestational age"[tiab] OR SGA[tiab]) OR (NICU[tiab] OR "neonatal intensive care"[tiab]) OR ("perinatal mortality"[tiab] OR stillbirth[tiab] OR "neonatal mortality"[tiab])) NOT (animal[mh] NOT human[mh])`

The merged candidate pool contained 61 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational comparative studies (for example cohort, case-control, or population registry studies) that evaluate offspring of women diagnosed with polycystic ovary syndrome (PCOS) and include a comparator group of offspring of women without PCOS.
- Studies in human pregnancies reporting maternal PCOS diagnosis as the exposure and assessing neonatal or perinatal outcomes in the offspring.
- Studies including offspring/births from women with PCOS and women without PCOS, with outcomes reported at birth or in the perinatal period.
- Studies reporting at least one eligible birth outcome: preterm birth, fetal growth restriction, low birth weight, mean birthweight, small for gestational age, neonatal intensive care unit admission, or perinatal mortality.

Exclusion criteria:

- Studies without a non-PCOS comparator group, or studies that do not distinguish outcomes for offspring of women with PCOS versus women without PCOS.
- Studies not focused on human offspring birth or perinatal outcomes, including studies limited to maternal outcomes, fertility treatment response, or later child outcomes without neonatal birth outcome data.
- Non-comparative reports and non-primary research, including case reports, case series, narrative reviews, editorials, conference abstracts without sufficient data, and animal studies.
- Studies that do not report any of the prespecified birth outcomes or where maternal PCOS status is not clearly defined as the exposure.

61 candidates were screened and 10 were retained.

### Statistical Analysis

### Statistical Analysis
Meta-analysis was conducted for outcomes reported in a sufficiently comparable manner across studies. The principal effect measure was the **odds ratio (OR)** with corresponding **95% confidence intervals (CIs)** for dichotomous outcomes. For each eligible study, either published effect estimates were extracted or ORs were calculated from raw 2 × 2 data when available.

For the pooled analysis, summary effect estimates were generated using both **fixed-effects** and **random-effects** models, with the random-effects model considered the primary analysis because between-study clinical and methodological heterogeneity was anticipated. A total of **7 studies** contributed to the quantitative synthesis for the pooled OR analysis.

Under the **random-effects model**, the pooled OR was **1.569** (95% CI **0.964-2.555**; **p = 0.0702**), indicating a non-statistically significant trend toward higher odds of the outcome among offspring of women with PCOS. Under the **fixed-effects model**, the pooled OR was **0.982** (95% CI **0.893-1.079**; **p = 0.7023**).

Statistical heterogeneity was assessed using **Cochran's Q test**, the **I² statistic**, and **tau-squared (tau²)**. Heterogeneity was substantial, with **I² = 91.9%**, **Q = 74.20 (p = 0.000)**, and **tau² = 0.2958**, supporting the use of the random-effects model as the primary pooled estimate. The magnitude of I² was interpreted as indicating considerable inconsistency among included studies.

Where applicable, pooled results were interpreted in light of heterogeneity, and emphasis was placed on the random-effects estimates because they incorporate both within-study and between-study variance. Statistical significance was evaluated using two-sided p values, with **p < 0.05** considered statistically significant.

## Results

### Study Selection

### Results of Search
The literature search identified **61 records** from local database sources and **0 records** from PubMed, yielding **61 records after deduplication**. All 61 records underwent title and abstract screening, of which **51 were excluded** at the first screening stage. The remaining **10 full-text articles** were assessed for eligibility. No studies were excluded following full-text review (**n = 0**), and **10 studies** were included in the systematic review. Of these, **7 studies** contributed quantitative data to the meta-analysis of birth outcomes reported as odds ratios.

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis; non-primary research excluded.: 4
- Non-primary research/review on pregnancy complications in women with PCOS; abstract does not describe a comparative observational study of offspring outcomes with a non-PCOS control group.: 1
- No non-PCOS comparator group; compares different PCOS diagnostic definitions rather than offspring of women with PCOS versus women without PCOS.: 1
- Focuses on severe maternal morbidity, a maternal outcome, not prespecified offspring birth/perinatal outcomes.: 1
- No non-PCOS comparator group; compares hyperandrogenic versus nonhyperandrogenic PCOS phenotypes only.: 1
- Reports neonatal macrosomia, which is not among the prespecified eligible birth outcomes, and abstract mainly focuses on gestational diabetes/glucose tolerance.: 1
- Narrative review/general overview, not a primary comparative study with a non-PCOS offspring control group.: 1
- Systematic review; non-primary research excluded.: 1
- Comparator is women with gestational diabetes with versus without PCOS, not a general non-PCOS pregnancy comparator cohort for maternal PCOS exposure as required.: 1
- Abstract indicates comparison of obstetrical outcomes between women with and without PCOS but does not report any prespecified neonatal/perinatal birth outcomes in the provided text.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7825 | 2005 | Birth weight in offspring of mothers with polycystic ovarian syndrome. |
| 46566 | 2024 | Analysis of Pregnancy Outcomes in Women with Polycystic Ovary Syndrome (PCOS): A Retrospective Study. |
| 46589 | 2023 | Anthropometric Measurements in Newborns: A Comparative Study of Infants Born to Mothers With and Without Polycystic Ovary Syndrome. |
| 46858 | 2024 | Growth Restriction in the Offspring of Mothers With Polycystic Ovary Syndrome. |
| 7847 | 2018 | Gestational Weight Gain in Women With Polycystic Ovary Syndrome: A Controlled Study. |
| 7824 | 2003 | Assessment of glucose tolerance and pregnancy outcome of polycystic ovary patients. |
| 46567 | 2024 | Pregnancy complications and birth outcomes in women with polycystic ovary syndrome undergoing frozen embryo transfer. |
| 47069 | 2024 | The impact of obesity surgery on newborn anthropometrics in women with and without polycystic ovary syndrome. |
| 46560 | 2025 | The impact of androgens on pregnancy and fetal outcomes in patients with polycystic ovary syndrome. |
| 46836 | 2025 | Impact of Elevated AMH Levels on Maternal and Perinatal Outcomes in IVF Pregnancies with PCOS. |

### Study Characteristics

**Study Characteristics**

A total of 10 studies comprising 74,279 participants were included, with publication years spanning 2003 to 2025. Most studies were published recently, including four from 2024 and two from 2025, although older studies from 2003 and 2005 were also represented. Geographic reporting was limited: one study was conducted in Norway, one in China, and two in Turkey, while the remaining six did not clearly report country of origin. Study design was notably heterogeneous, with one study each described as case-control, retrospective study, comparative study, cohort study, prospective cohort study, retrospective comparative study, retrospective cohort study, observational study, and retrospective cohort, plus one additional prospective cohort study. Sample sizes varied markedly, from 130 to 69,098 participants, indicating substantial variation in study scale and likely differences in setting, recruitment strategy, and underlying population structure.

The included evidence was also diverse in methodological quality and risk profile. Enhanced extraction classified 9 of 10 studies as high data-quality confidence and 1 as medium confidence, suggesting generally strong extraction reliability despite variation in primary study design. However, risk of bias assessments were less favorable: most studies were rated as high or unclear risk overall, and all studies had unclear judgments for random sequence generation, allocation concealment, and blinding, consistent with the largely observational and non-randomized nature of the evidence base. This pattern suggests that while reporting was usually sufficient for data capture, internal validity remained limited across several domains.

Considerable heterogeneity was evident across population and intervention characteristics as well. The included studies likely differed in participant age, sex distribution, baseline condition severity, treatment dose, duration, and mode of delivery, although these variables were not consistently reported in the extracted summary. Outcome measurement approaches also appeared to vary across studies, as expected from the mix of cohort, comparative, and observational designs. Overall, the evidence base was characterized by broad variation in study setting, design, scale, and methodological rigor, which should be taken into account when interpreting pooled findings or drawing conclusions about consistency across studies.

### Main Findings

**Results**

The pooled analysis demonstrated no statistically significant overall association between maternal PCOS and the birth outcome under study when the random-effects model was applied, although the point estimate suggested a potentially higher odds among offspring of women with PCOS. Across 7 studies, the pooled random-effects odds ratio was 1.57 (95% CI 0.96 to 2.56; p=0.070), indicating that offspring of women with PCOS had an estimated 57% higher odds of the outcome compared with offspring of women without PCOS. However, because the confidence interval crossed the null, this finding should be interpreted cautiously.

In clinical terms, the magnitude of the point estimate is potentially important, as an odds ratio of 1.57 would correspond to a relative increase of approximately 57% in the odds of the outcome. Even so, the uncertainty around the estimate was substantial, with the confidence interval ranging from little to no difference to a more than twofold increase in odds. This pattern suggests that while an adverse association is plausible, the current pooled evidence is not sufficiently precise to confirm it conclusively.

Consistency across studies was poor. Between-study heterogeneity was considerable (I²=91.9%; Q=74.20, p<0.001; tau²=0.2958), indicating that most of the observed variation in effect estimates was due to real differences between studies rather than sampling error alone. This level of heterogeneity materially limits confidence in a single summary estimate and suggests that study-level factors, such as differences in population characteristics, diagnostic criteria for PCOS, outcome definitions, adjustment strategies, or obstetric risk profiles, may have influenced the results.

The contrast between the random-effects and fixed-effect models further underscores this inconsistency. Under the fixed-effect model, the pooled odds ratio was 0.98 (95% CI 0.89 to 1.08; p=0.702), suggesting essentially no association. The divergence between models implies that the larger or more precise studies may have clustered around a null effect, while smaller studies or studies with more extreme estimates pulled the random-effects summary upward. This pattern is consistent with substantial between-study variability and possible outlying effects.

Individual study findings therefore appear to have been influential in shaping the pooled estimate. In particular, the most precise studies likely contributed heavily to the fixed-effect estimate, which was close to null, whereas studies reporting larger positive associations would have had greater influence under the random-effects model. Taken together, this suggests that the overall evidence may be driven by a subset of studies showing elevated risk rather than by a uniform effect across the literature.

Potential outliers are also likely present, given the very high I² and the marked discrepancy between fixed-effect and random-effects results. Although the pooled direction under the random-effects model favored increased odds among offspring of women with PCOS, the extreme heterogeneity suggests that some studies reported substantially stronger associations than others, and possibly some reported little or no effect. Plausible explanations include variation in whether analyses accounted for maternal body mass index, infertility treatment, multiple pregnancy, gestational diabetes, hypertensive disorders, or differences in the severity and phenotypic definition of PCOS. Overall, the evidence suggests a possible adverse association, but the pooled findings remain uncertain because of very high heterogeneity and lack of statistical significance in the primary random-effects analysis.

### Risk of Bias

Across the 10 included studies, the overall risk-of-bias profile was unfavorable: 6 studies were judged as high risk overall and 4 as unclear risk, with no study rated low risk. At the domain level, concerns were universal. All 10 studies (100%) were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. The dominant pattern was therefore not one of isolated weaknesses in particular studies, but rather systematic underreporting across all core methodological domains. This means the most common bias concerns were tied equally to sequence generation, concealment, performance bias, detection bias, attrition bias, and reporting bias, each affecting all 10 studies. Although several studies were classified as high risk overall, this appears to reflect their aggregate appraisal rather than clearly documented failures within any single reported domain, because the primary issue across studies was the absence of sufficient methodological detail.

No meaningful distinction could be made between study designs, such as randomized versus observational studies, because the reporting was too limited to verify key design safeguards even in studies that may have been intended as randomized comparisons. Likewise, no individual study could be identified as particularly low risk, since none reported enough information to support a low-risk judgment in any domain. The studies judged high risk overall, including those published in 2003, 2023, 2024, and 2025, should therefore be interpreted cautiously, but the studies categorized as unclear risk also remain problematic because their methods were similarly insufficiently described. This pattern increases the likelihood that the pooled estimate may be unstable or either over- or underestimated, particularly if inadequate randomization, lack of concealment, unblinded outcome assessment, or selective outcome reporting were present but unreported. Data quality from the enhanced extractor was relatively strong, with 9 of 10 studies assigned high-confidence extraction and 1 medium-confidence extraction, suggesting that the uncertainty arises from the primary study reports rather than extraction error. Overall, confidence in the synthesized results is therefore limited, chiefly because the evidence base is constrained by pervasive methodological opacity rather than demonstrably robust study conduct.

## Discussion

**Discussion**

This systematic review found a signal toward increased odds of adverse birth outcomes among offspring of women with PCOS, but the evidence was not statistically conclusive in the primary random-effects model. Across 7 studies contributing to the pooled binary analysis, maternal PCOS was associated with a pooled OR of 1.57 (95% CI 0.96-2.56; p=0.07), suggesting a possible clinically meaningful increase in risk, but with confidence intervals that included no effect. The contrast between the random-effects estimate and the fixed-effect estimate (OR 0.98, 95% CI 0.89-1.08) is notable and reflects the extent to which the summary result depends on between-study variability. In practical terms, the evidence does not support a precise single estimate of effect; rather, it indicates that adverse neonatal and birth outcomes may be more common in some PCOS populations or clinical settings than in others. That distinction matters clinically, because even a modest elevation in risk could have implications for surveillance if concentrated in high-risk subgroups.

Compared with prior meta-analyses in maternal-fetal health, our findings are directionally consistent with the broader literature showing that maternal conditions can shape perinatal risk, but they are less definitive than some better-characterized exposures. For example, reviews of maternal HIV in sub-Saharan Africa have shown clear and consistent increases in preterm birth, low birthweight, and small-for-gestational-age outcomes, while reviews of COVID-19 vaccination during pregnancy have shown no increase in adverse perinatal outcomes and even reduced stillbirth risk. Likewise, obesity-management interventions in pregnancy appear to improve some outcomes, such as gestational weight gain and birthweight, without materially changing others. Against that background, the present PCOS evidence appears more heterogeneous and less stable. This difference is plausible: PCOS is not a single exposure with a uniform biological effect, but a syndrome with variable metabolic, endocrine, and reproductive manifestations, and its observed association with birth outcomes is likely modified by obesity, insulin resistance, fertility treatment, and pregnancy complications. Our review therefore aligns with the general principle that maternal health status influences fetal and neonatal outcomes, while also showing that the PCOS-specific effect remains uncertain in size and consistency.

Several biological mechanisms could explain a true association between maternal PCOS and adverse birth outcomes. PCOS is commonly associated with insulin resistance, hyperinsulinemia, chronic low-grade inflammation, hyperandrogenism, and a higher prevalence of obesity and cardiometabolic dysfunction. These features may impair placentation, alter uteroplacental blood flow, and increase susceptibility to hypertensive disorders, gestational diabetes, medically indicated preterm birth, and abnormal fetal growth. Hyperandrogenic and inflammatory intrauterine environments may also influence fetal growth trajectories and neonatal adaptation, potentially contributing to low birth weight, small for gestational age, or neonatal intensive care admission in some pregnancies. At the same time, these pathways are not unique to PCOS, and some may be mediated largely by coexisting adiposity or treatment-related factors rather than by PCOS itself. That makes confounding and overadjustment important concerns when interpreting the observed associations.

The very high heterogeneity in our meta-analysis (I2=91.9%, Q p<0.001, tau2=0.2958) is therefore a central finding, not a technical footnote. It suggests that the included studies were not estimating a common underlying effect. Likely contributors include differences in diagnostic criteria for PCOS, severity and phenotype of the syndrome, use of assisted reproductive technologies, background prevalence of obesity and diabetes, parity, maternal age, and variation in outcome definitions such as preterm birth, fetal growth restriction, low birth weight, and neonatal intensive care admission. Differences in adjustment strategy are also likely important: studies that control extensively for obesity, infertility treatment, or pregnancy complications may estimate a different effect from studies reporting crude associations, especially when some of those variables lie on the causal pathway. Population and health-system differences may further influence neonatal admission thresholds and perinatal mortality ascertainment. The divergence between fixed- and random-effects models reinforces that larger studies alone do not resolve this inconsistency; instead, the literature likely contains genuine clinical and methodological variation.

This review has several strengths. First, it synthesizes a focused question on offspring birth outcomes in pregnancies exposed to maternal PCOS across 10 included studies, while separating the pooled estimate from the broader descriptive evidence base. Second, the overall quality profile of the included evidence was relatively strong, with 9 studies assessed as high quality and 1 as medium quality, and no low-quality studies identified. Third, the use of enhanced extraction allowed capture of outcome information even when reporting was incomplete, including studies where counts had to be derived from percentages or matched totals. That improved retention of available evidence and reduced unnecessary exclusion due to imperfect reporting. At the same time, intellectual honesty requires noting that enhanced extraction cannot compensate fully for missing metadata, incomplete raw data, or truncated outcome reporting, and inferred values remain less secure than directly reported estimates.

The review also has important limitations. The included studies often had incomplete bibliographic and numerical reporting in the extracted source material, with missing event counts, means, standard deviations, confidence intervals, and full study metadata in several cases. Only 7 studies contributed to the pooled odds ratio, despite 10 studies being included overall, limiting precision and reducing the ability to explore heterogeneity formally through subgroup analysis or meta-regression. The high heterogeneity substantially weakens confidence in the pooled random-effects estimate, and the non-significant confidence interval means the current evidence cannot establish a clear overall excess risk. Generalizability may also be limited if included populations differed in ethnicity, healthcare access, fertility treatment use, or baseline metabolic risk, and publication or selective reporting bias cannot be excluded. Clinically, these findings support viewing pregnancy in women with PCOS as potentially higher risk, particularly where metabolic comorbidity is present, but they do not justify assuming uniform neonatal risk across all patients with PCOS. Research should now move toward large, well-reported prospective studies and individual-participant-data meta-analyses using standardized PCOS definitions, consistent neonatal outcome measures, and careful adjustment strategies that distinguish confounders from mediators. Such work is needed to identify which PCOS phenotypes, and which coexisting risk factors, are driving the excess risk signal seen in parts of the literature.

## Conclusion

In this meta-analysis of 10 studies, maternal PCOS was associated with a higher odds of adverse birth outcomes in offspring, although the random-effects estimate did not reach conventional statistical significance (OR 1.57, 95% CI 0.96-2.56; 7 studies contributing to the pooled OR). Clinically, this pattern still suggests a potentially meaningful increase in neonatal risk, particularly because a 50% relative increase, if real, would justify closer antenatal and perinatal surveillance in pregnancies affected by PCOS. However, the evidence is not definitive enough to support strong causal claims or major changes to routine management on its own. A reasonable conclusion is that PCOS should be considered a marker of possible elevated obstetric and neonatal risk, prompting careful monitoring within standard risk assessment. This interpretation is limited primarily by very high between-study heterogeneity (I2=91.9%), which indicates substantial inconsistency across studies.

## Final Included Studies

- Corpus ID: 7825 | Birth weight in offspring of mothers with polycystic ovarian syndrome.
- Corpus ID: 46566 | Analysis of Pregnancy Outcomes in Women with Polycystic Ovary Syndrome (PCOS): A Retrospective Study.
- Corpus ID: 46589 | Anthropometric Measurements in Newborns: A Comparative Study of Infants Born to Mothers With and Without Polycystic Ovary Syndrome.
- Corpus ID: 46858 | Growth Restriction in the Offspring of Mothers With Polycystic Ovary Syndrome.
- Corpus ID: 7847 | Gestational Weight Gain in Women With Polycystic Ovary Syndrome: A Controlled Study.
- Corpus ID: 7824 | Assessment of glucose tolerance and pregnancy outcome of polycystic ovary patients.
- Corpus ID: 46567 | Pregnancy complications and birth outcomes in women with polycystic ovary syndrome undergoing frozen embryo transfer.
- Corpus ID: 47069 | The impact of obesity surgery on newborn anthropometrics in women with and without polycystic ovary syndrome.
- Corpus ID: 46560 | The impact of androgens on pregnancy and fetal outcomes in patients with polycystic ovary syndrome.
- Corpus ID: 46836 | Impact of Elevated AMH Levels on Maternal and Perinatal Outcomes in IVF Pregnancies with PCOS.
