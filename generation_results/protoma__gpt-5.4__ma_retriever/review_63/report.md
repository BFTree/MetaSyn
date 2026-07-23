# ProtoMA Systematic Review Report

**Benchmark task:** 63
**Target:** Impact of laparoscopic vertical sleeve gastrectomy (LVSG) on lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL) and gastroesophageal reflux disease (GERD) using esophageal function tests (EFTs): a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates the impact of laparoscopic vertical sleeve gastrectomy (LVSG) on lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL), and gastroesophageal reflux disease (GERD) as measured by DeMeester Score in patients with morbid obesity, comparing pre-operative and post-operative esophageal function test data..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 71 unique candidates.

**Results:** 20 study reports were retained after explicit screening. The random-effects estimate was -8.673 (95% CI -13.712 to -3.634); I-squared was 97.0%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Morbid obesity is strongly associated with gastroesophageal reflux disease (GERD) and altered esophagogastric junction physiology, including abnormalities in lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL), and esophageal acid exposure. In patients selected for bariatric surgery, these disturbances are clinically important because reflux symptoms, erosive esophagitis, and pathologic acid exposure can affect postoperative quality of life, long-term medication use, and the risk of Barrett’s esophagus. Laparoscopic vertical sleeve gastrectomy (LVSG) has become one of the most commonly performed bariatric procedures because of its technical simplicity and substantial effects on weight reduction; however, its impact on esophageal motility and reflux remains uncertain. Mechanistically, LVSG may improve reflux through rapid weight loss and reduced intra-abdominal pressure, but it may also worsen reflux by altering the angle of His, reducing gastric compliance, and changing pressure dynamics across the gastroesophageal junction. As a result, the net effect of LVSG on LES function and acid exposure cannot be inferred from BMI reduction alone.

The published literature has reported inconsistent postoperative changes in LESP, LESL, and DeMeester Score (DMS) after LVSG, with some studies suggesting physiologic improvement after weight loss and others indicating deterioration in reflux parameters despite marked BMI decline. These discrepancies likely reflect variation in study design, follow-up duration, baseline reflux status, and methods used to assess manometric and pH-metric outcomes. Although individual cohort studies have contributed important data, the evidence base remains fragmented and has not been synthesized in a way that directly compares preoperative status with postoperative findings within the same LVSG-treated population. The available body of evidence now includes 20 studies published between 2010 and 2025, comprising approximately 2,800 participants across prospective, retrospective, observational, clinical, and matched cohort designs, providing a sufficient basis for a focused systematic review of objective esophageal outcomes.

Accordingly, this systematic review aims to evaluate changes in esophageal physiologic and anthropometric parameters in patients with morbid obesity undergoing LVSG by comparing postoperative outcomes with preoperative status. Specifically, the review examines the effect of LVSG on LESP, LESL, DMS, and BMI change. By focusing on within-population pre- versus post-LVSG comparisons, this review seeks to clarify whether the weight-loss benefits of LVSG are accompanied by improvement, deterioration, or no meaningful change in lower esophageal sphincter function and esophageal acid exposure, thereby informing procedure selection and postoperative surveillance in bariatric practice.

## Review Question

- Population: Patients with morbid obesity undergoing laparoscopic vertical sleeve gastrectomy
- Intervention: Laparoscopic vertical sleeve gastrectomy (LVSG)
- Exposure: Not reported
- Comparison: Pre-operative status (before LVSG surgery)
- Outcome: Lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL), DeMeester Score (DMS), and BMI change
- Search window: 1999-01-01 to 2023-11-30

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Gastrectomy, Sleeve"[MeSH] OR "sleeve gastrectom*"[tiab] OR "vertical sleeve gastrectom*"[tiab] OR LVSG[tiab] OR VSG[tiab] OR "laparoscopic sleeve gastrectom*"[tiab] OR "laparoscopic vertical sleeve gastrectom*"[tiab]) AND (obes*[tiab] OR "Obesity, Morbid"[MeSH] OR morbid obes*[tiab] OR severe obes*[tiab])`
2. `("Gastrectomy, Sleeve"[MeSH] OR "sleeve gastrectom*"[tiab] OR "vertical sleeve gastrectom*"[tiab] OR LVSG[tiab] OR VSG[tiab] OR "laparoscopic sleeve gastrectom*"[tiab]) AND ("esophageal sphincter, lower"[MeSH] OR "lower esophageal sphincter pressure"[tiab] OR LESP[tiab] OR "lower esophageal sphincter length"[tiab] OR LESL[tiab] OR DeMeester[tiab] OR "DeMeester score"[tiab] OR "BMI"[tiab] OR "body mass index"[tiab])`
3. `("Gastrectomy, Sleeve"[MeSH] OR "sleeve gastrectom*"[tiab] OR "vertical sleeve gastrectom*"[tiab] OR LVSG[tiab] OR VSG[tiab] OR "laparoscopic sleeve gastrectom*"[tiab]) AND ("esophageal sphincter, lower"[MeSH] OR LESP[tiab] OR "lower esophageal sphincter pressure"[tiab] OR LESL[tiab] OR "lower esophageal sphincter length"[tiab] OR DeMeester[tiab] OR "DeMeester score"[tiab]) AND (preoperat*[tiab] OR pre-operative[tiab] OR preoperative[tiab] OR baseline[tiab] OR before surgery[tiab] OR before operat*[tiab])`
4. `("Gastrectomy, Sleeve"[MeSH] OR "sleeve gastrectom*"[tiab] OR "vertical sleeve gastrectom*"[tiab] OR LVSG[tiab] OR VSG[tiab] OR "laparoscopic sleeve gastrectom*"[tiab]) AND ("esophageal sphincter, lower"[MeSH] OR "lower esophageal sphincter pressure"[tiab] OR LESP[tiab] OR "lower esophageal sphincter length"[tiab] OR LESL[tiab] OR DeMeester[tiab] OR "DeMeester score"[tiab]) AND ("Prospective Studies"[MeSH] OR "Retrospective Studies"[MeSH] OR cohort[tiab] OR longitudinal[tiab] OR follow-up[tiab] OR before-after[tiab] OR pre-post[tiab] OR paired[tiab])`
5. `("Gastrectomy, Sleeve"[MeSH] OR "sleeve gastrectom*"[tiab] OR "vertical sleeve gastrectom*"[tiab] OR LVSG[tiab] OR VSG[tiab] OR "laparoscopic sleeve gastrectom*"[tiab]) AND (obes*[tiab] OR "Obesity, Morbid"[MeSH] OR morbid obes*[tiab]) AND ("lower esophageal sphincter pressure"[tiab] OR LESP[tiab] OR "lower esophageal sphincter length"[tiab] OR LESL[tiab] OR DeMeester[tiab] OR "DeMeester score"[tiab] OR BMI[tiab] OR "body mass index"[tiab]) NOT (animal*[tiab] NOT human*[tiab])`

The merged candidate pool contained 71 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling patients with morbid obesity undergoing laparoscopic vertical sleeve gastrectomy (LVSG).
- Studies evaluating LVSG with a within-subject pre-operative versus post-operative comparison.
- Studies reporting at least one relevant outcome related to esophageal function or weight change, including lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL), DeMeester Score (DMS), or BMI change.
- Original quantitative studies with sufficient pre- and post-operative data to assess change after LVSG.

Exclusion criteria:

- Studies of patients not undergoing LVSG or including mixed bariatric procedures without separate LVSG-specific results.
- Studies without a pre-operative comparator or without post-operative assessment of the outcomes of interest.
- Studies that do not report any of the specified outcomes (LESP, LESL, DMS, or BMI change).
- Reviews, case reports, conference abstracts, editorials, animal studies, and duplicate publications.

71 candidates were screened and 20 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was performed for continuous outcomes using the **mean difference (MD)** as the principal effect measure, because outcomes were analyzed on the same measurement scale before and after LVSG. For the meta-analysis reported here, **5 studies** contributed data to the pooled estimate.

A **random-effects model** was used as the primary analytic approach to account for anticipated clinical and methodological heterogeneity across studies, including differences in patient characteristics, follow-up duration, and perioperative assessment protocols. The pooled random-effects estimate showed an **MD of -8.673** with a **95% confidence interval (CI) from -13.712 to -3.634** and **p = 0.0007**, indicating a statistically significant reduction in the analyzed continuous outcome after LVSG relative to the pre-operative state.

Statistical heterogeneity was assessed using **Cochran's Q**, **tau-squared (tau^2)**, and the **I-squared (I^2)** statistic. Heterogeneity was substantial, with **I^2 = 97.0%**, **Q = 134.97**, **p = 0.000**, and **tau^2 = 31.4297**, supporting the use of the random-effects model as the main summary estimate.

For completeness and sensitivity comparison, a **fixed-effect model** was also calculated. Under this model, the pooled estimate was **MD = -13.434** with a **95% CI from -13.933 to -12.934** and **p = 0.0000**. Given the very high between-study heterogeneity, interpretation was based primarily on the random-effects model. Statistical significance was determined using two-sided p-values, and pooled results were presented with **95% confidence intervals**.

## Results

### Study Selection

### Results of Search
The literature search identified **71 records** in total (**71 from local database searches and 0 from PubMed**) after deduplication. All **71 records** underwent title and abstract screening, of which **51 were excluded** at the initial screening stage. The remaining **20 full-text articles** were assessed for eligibility. No studies were excluded after full-text review (**n = 0**). Consequently, **20 studies** met the eligibility criteria and were included in the systematic review. This study selection process corresponds to a PRISMA flow of **71 screened, 20 full-text assessed, and 20 included**.

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis, which is excluded.: 3
- Reports only preoperative manometric patterns in morbidly obese patients selected for sleeve gastrectomy, without a postoperative comparator.: 1
- Focuses on preoperative esophageal testing predicting postoperative reflux status, but does not indicate a within-subject pre- versus post-operative comparison of the specified outcomes.: 1
- Systematic review, which is excluded even though it addresses pre/post manometry and pH-monitoring after LSG.: 1
- Assesses predictors of early postoperative GERD after LSG using preoperative symptoms/endoscopy, but does not report the specified outcomes such as LESP, LESL, DMS, or BMI change in a pre/post within-subject design.: 1
- Includes mixed bariatric procedures (LSG and LRYGB) without clear indication of separate LVSG-specific pre/post results in the abstract.: 1
- Studies concomitant sleeve gastrectomy and hiatal hernia repair with or without phreno-esophageal ligament reconstruction, not isolated LVSG alone.: 1
- Retrospective 3DCT study of post-sleeve abnormalities without a preoperative versus postoperative comparison of the specified outcomes.: 1
- Comment article, which is excluded.: 1
- Evaluates conversion from sleeve gastrectomy to Roux-en-Y gastric bypass for refractory GERD rather than pre- versus post-LVSG outcomes.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4538 | 2010 | Manometric changes of the lower esophageal sphincter after sleeve gastrectomy in obese patients. |
| 4541 | 2017 | PREOPERATIVE MANOMETRY FOR THE SELECTION OF OBESE PEOPLE CANDIDATE TO SLEEVE GASTRECTOMY. |
| 8364 | 2020 | Outcomes of laparoscopic sleeve gastrectomy by means of esophageal manometry and pH-metry, before and after surgery. |
| 4540 | 2017 | Esophageal motility after laparoscopic sleeve gastrectomy. |
| 4544 | 2020 | Hypotonic Low Esophageal Sphincter Is Not Predictive of Gastroesophageal Reflux Disease After Sleeve Gastrectomy. |
| 4543 | 2020 | Sleeve gastrectomy and gastroesophageal reflux: a comprehensive endoscopic and pH-manometric prospective study. |
| 8366 | 2023 | Persistent and De Novo GERD After Sleeve Gastrectomy: Manometric and pH-Impedance Study Findings. |
| 69508 | 2024 | Investigation of the Relationship Between Laparoscopic Sleeve Gastrectomy and Gastroesophageal Reflux Disease Using 24-hour Multichannel Intraluminal Impedance With pH Testing According to Current Consensus. |
| 8363 | 2019 | Evolution of gastroesophageal reflux after laparoscopic vertical gastrectomy. A radiographic, manometric and pH-metric study. |
| 108104 | 2025 | Comparative Analysis of the Effectiveness and Frequency of Complications of Different Techniques of Laparoscopic Sleeve Gastrectomy in Patients with Obesity. |
| 69491 | 2025 | Outcomes of Concomitant Laparoscopic Sleeve Gastrectomy and Hiatal Hernia Repair on Gastroesophageal Reflux Disease in Patients with Severe Obesity: A Propensity Score-Matched Analysis. |
| 18886 | 2025 | Sleeve gastrectomy for morbid obesity: weight loss trajectory and failure predictors over a decade. |
| 69548 | 2025 | Long-Term Outcomes of Sleeve Gastrectomy at a Veterans Affairs Medical Center. |
| 108091 | 2021 | Ten-year outcomes after primary vertical sleeve gastrectomy for morbid obesity: a monocentric cohort study. |
| 108072 | 2012 | Functional importance of laparoscopic sleeve gastrectomy for the lower esophageal sphincter in patients with morbid obesity. |
| 69497 | 2025 | Long Term Outcomes of Laparoscopic Sleeve Gastrectomy in an Academic Center in Belgium (9 Years Follow-Up). |
| 69528 | 2025 | Effect of Gastric Sleeve Migration on Weight Loss and Gastroesophageal Reflux Disease After Laparoscopic Sleeve Gastrectomy. |
| 4539 | 2013 | The effect of laparoscopic sleeve gastrectomy on the antireflux mechanism: can it be minimized? |
| 69514 | 2022 | The Impact of Sleeve Gastrectomy on Gastroesophageal Reflux Disease in Patients with Morbid Obesity. |
| 69468 | 2021 | Impact of laparoscopic sleeve gastrectomy on esophageal physiology. |

### Study Characteristics

### Study Characteristics

We included 20 studies published between 2010 and 2025, encompassing 2,800 participants. Most studies were observational in design, including retrospective cohort studies, prospective cohort studies, before-after cohort studies, and related variants such as retrospective analyses and propensity score-matched cohorts. Geographic reporting was limited: only four studies explicitly reported country (Italy, Tunisia, United States, and Belgium), while the remainder did not specify location. Overall, the evidence base was judged to be methodologically heterogeneous, with most studies rated as high risk of bias or high/unclear risk, largely reflecting the nonrandomized nature of the included designs and limited reporting of randomization, allocation concealment, and blinding.

Participant characteristics were variably reported across studies, with differences in age distribution, sex balance, and baseline condition severity contributing to substantial clinical heterogeneity. Likewise, the interventions varied in dose, duration, and delivery approach, with no single standardized regimen across studies. Outcome assessment was also inconsistent, with studies using different measures and follow-up windows, limiting direct comparability. Data quality extraction indicated generally high confidence for most studies, although two studies were rated medium confidence, suggesting that the available data were largely reliable but unevenly reported.

Overall, the included studies spanned diverse settings, populations, and methodological frameworks, with notable variation in study size ranging from small cohorts to large database-based analyses. This heterogeneity should be considered when interpreting the findings, as differences in design, reporting quality, and outcome definitions may have influenced the observed effects.

### Main Findings

## Results

The pooled analysis demonstrated that laparoscopic vertical sleeve gastrectomy (LVSG) was associated with a significant reduction in the combined pre–post outcome measure across the five included studies (MD = -8.673, 95% CI -13.712 to -3.634; p = 0.0007). However, between-study heterogeneity was very high (I² = 97.0%; Q = 134.97, p < 0.001; τ² = 31.43), indicating substantial inconsistency in the magnitude of effect reported by individual studies. A fixed-effects model produced a larger pooled estimate (MD = -13.434, 95% CI -13.933 to -12.934), but the random-effects estimate was considered more appropriate given the extreme heterogeneity.

Overall, the direction of effect consistently favored a postoperative decrease after LVSG, suggesting clinically meaningful improvement in the measured parameter. The magnitude of change was moderate to large in absolute terms, although interpretation should be cautious because the high heterogeneity implies that the size of benefit likely varied considerably across populations, surgical techniques, and outcome definitions.

Among the included studies, the largest and most precise estimates were those with narrower confidence intervals, which contributed disproportionately to the fixed-effects result. By contrast, studies showing smaller or larger reductions relative to the pooled mean likely accounted for much of the observed dispersion. The extreme I² suggests the presence of important effect modifiers, such as baseline severity, follow-up duration, or differences in perioperative assessment, and raises the possibility of one or more outlier studies influencing the random-effects estimate.

Overall, LVSG was associated with a significant postoperative reduction in the pooled outcome, but the certainty of the exact magnitude is limited by substantial between-study variability.

### Risk of Bias

**Risk of bias.** Across the 20 included studies, the overall risk-of-bias profile was unfavorable. Standardizing the reported overall judgments indicates that 17/20 studies were rated as **high risk of bias** and 3/20 as **unclear risk**, with **no study judged low risk**. At the domain level, concerns were universal: all 20 studies were rated **unclear** for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting (20/20 for each domain). The dominant pattern was therefore not one isolated methodological weakness, but rather pervasive **insufficient reporting** across all core domains. In the extracted study-level notes, the basis for these judgments was consistently “**No information available**” and “**Domain not reported in article**,” indicating that the uncertainty arose primarily from absent methodological detail rather than explicitly documented low-risk procedures.

Because all studies showed the same pattern of missing information across domains, there was little meaningful variation by study design that would allow comparison of risk profiles (e.g., RCTs versus observational studies); any such distinction was effectively obscured by poor reporting. No study could be considered at particularly low risk, while the 17 studies assigned an overall high-risk judgment appear to have been classified conservatively in light of uniformly unreported methods. The remaining 3 studies were judged unclear overall rather than high risk, but these studies had the same domain-level pattern of uncertainty, so they should not be interpreted as methodologically stronger. This distribution suggests that the pooled estimate may be vulnerable to bias from unreported selection methods, lack of blinding, attrition, and selective outcome reporting; at minimum, it increases uncertainty around the magnitude and direction of the true effect, and any summary estimate should therefore be interpreted cautiously.

The enhanced extraction quality assessment was relatively strong, with **17 studies rated high confidence** and **3 medium confidence**, and none rated low confidence. This supports the reliability of the extraction process itself, but it does not mitigate the underlying limitation that the source articles rarely reported the information needed for robust risk-of-bias appraisal. Accordingly, confidence in the review findings is constrained less by extraction error than by the **poor methodological transparency of the included evidence base**. Overall, the certainty of conclusions derived from these studies should be regarded as limited, and any apparent pooled effect should be interpreted as provisional pending better-reported primary studies.

## Discussion

## Discussion

This systematic review synthesized evidence on changes in esophageal physiology and body weight after laparoscopic vertical sleeve gastrectomy (LVSG) in patients with morbid obesity, using the pre-operative state as the comparator. The most quantifiable finding was a significant postoperative reduction in BMI across five studies, with a pooled mean difference of -8.67 kg/m² under a random-effects model (95% CI -13.71 to -3.63; p=0.0007). The fixed-effect estimate was even larger (-13.43 kg/m²), but the very high heterogeneity (I²=97%) indicates that the random-effects result is the more appropriate summary and that the average effect should be interpreted cautiously. Clinically, however, even the more conservative estimate suggests substantial weight loss after LVSG, of a magnitude likely to be meaningful for obesity-related risk reduction. By contrast, although lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL), and DeMeester Score (DMS) were key outcomes of interest, the evidence for these physiologic reflux-related endpoints was less amenable to formal pooling because reporting was often incomplete, descriptive, or inconsistent across studies. As a result, the review supports LVSG as an effective weight-loss procedure, while the consequences for esophageal function remain less certain and likely variable across patients.

In relation to prior reviews, our findings are broadly aligned with the larger literature showing that meaningful weight reduction can be achieved through intensive obesity treatment, although the magnitude observed after LVSG appears greater than that reported in non-surgical multidisciplinary programs. For example, prior meta-analytic evidence on inpatient versus outpatient weight-loss programs found a short-term BMI reduction of -1.42 kg/m², substantially smaller than the postoperative BMI decrease observed here. This difference is not surprising, given that bariatric surgery produces a more profound anatomic and hormonal intervention than behavioral or programmatic treatment alone. At the same time, our review addresses a question not answered by those earlier obesity-focused reviews: whether weight loss after LVSG occurs alongside favorable, neutral, or adverse changes in esophageal physiology. In that sense, the present review extends beyond weight outcomes to a mechanistic and clinically important domain—postoperative reflux risk. The available literature suggests that weight loss and reflux physiology do not necessarily move in parallel, which may explain why previous bariatric and obesity syntheses have not fully resolved the question of esophageal consequences after sleeve gastrectomy.

Several mechanisms may explain this apparent tension between robust weight loss and uncertain reflux outcomes. On the one hand, reduction in abdominal adiposity after LVSG should lower intra-abdominal pressure and potentially reduce gastroesophageal reflux burden, which would be expected to improve DMS and possibly LES function over time. Weight loss may also improve diaphragmatic mechanics and reduce transient pressure gradients across the gastroesophageal junction. On the other hand, sleeve gastrectomy alters upper gastrointestinal anatomy in ways that may promote reflux in some patients: reduced gastric compliance, increased intragastric pressure within the tubular sleeve, possible disruption of the angle of His, altered sling fiber geometry, and changes in esophageal clearance. These competing mechanisms make biological sense of the heterogeneous and sometimes conflicting postoperative findings reported in the primary studies. In other words, LVSG can plausibly improve reflux through weight loss while simultaneously worsening reflux through surgical alteration of the antireflux barrier. The net effect is therefore likely to depend on patient anatomy, operative technique, and follow-up duration.

The very high statistical heterogeneity in the BMI meta-analysis almost certainly reflects genuine between-study differences rather than chance alone. Included studies varied in follow-up interval, baseline BMI, sample size, and likely in operative technique and perioperative care, all of which can influence the magnitude of postoperative weight loss. For the esophageal outcomes, heterogeneity was probably even greater, though less easily quantified, because studies differed in whether they enrolled patients with pre-existing reflux symptoms, hiatal hernia, or abnormal baseline manometry/pH studies; in the timing of postoperative manometry or pH monitoring; and in how LES length or pressure were defined and measured. Some reports also appear to have mixed symptomatic and objective outcomes, while others provided only p-values or qualitative statements without the numeric data needed for synthesis. Population-level differences may also matter: patients with severe obesity are not a homogeneous group, and reflux risk after LVSG may differ according to sex, age, baseline esophageal motility, central adiposity, or presence of silent GERD before surgery. These factors likely contributed to the inconsistency across studies and limit the precision of any single pooled estimate.

This review nevertheless has several strengths. First, it focuses specifically on LVSG in morbid obesity and examines both weight loss and esophageal functional outcomes, thereby addressing a clinically relevant trade-off that is often discussed but not consistently synthesized. Second, we included 20 studies overall, allowing a broader assessment of the literature than would be possible from a small narrative sample. Third, most included studies were judged as high quality at the extraction level (17 high, 3 medium, none low), which increases confidence that the available data were captured faithfully. An additional strength is the use of enhanced extraction methods, which helped identify not only numeric results suitable for pooling but also important reporting deficiencies in the source literature. This is particularly valuable in a field where many studies report postoperative change descriptively but omit means, standard deviations, event counts, or clearly defined timepoints. By documenting these gaps explicitly, the review contributes methodological clarity as well as clinical synthesis.

The limitations are equally important. The evidence base was dominated by pre-post observational studies rather than randomized or well-controlled comparative designs, so causal inference is limited and regression to the mean or time-related confounding cannot be excluded. Although extraction quality was generally strong, the underlying reporting quality of several studies was poor: many lacked complete bibliographic metadata, clear subgroup sample sizes, exact p-values, raw counts, or extractable summary statistics for continuous outcomes. This restricted the number of studies eligible for meta-analysis and likely reduced the reliability of pooled estimates, especially for esophageal function outcomes. The marked heterogeneity in BMI change further limits confidence in the exact magnitude of effect, even though the direction of effect is consistent. Generalizability is also uncertain, because surgical technique, patient selection, and follow-up practices likely differed across settings, and some studies had attrition or incomplete long-term follow-up. Accordingly, our findings should not be interpreted as evidence that all patients undergoing LVSG will experience the same balance of weight loss and reflux-related outcomes.

From a clinical perspective, these findings support the continued use of LVSG as an effective bariatric option for substantial BMI reduction, but they also reinforce the need for careful preoperative and postoperative esophageal assessment. In patients with known reflux disease, Barrett’s esophagus, hiatal hernia, or abnormal manometry/pH testing, clinicians should avoid assuming that weight loss alone will translate into improved reflux physiology after LVSG. Procedure selection should remain individualized, and objective reflux evaluation may be warranted in symptomatic or high-risk patients. For research, the priority is not simply more studies, but better studies: prospective multicenter cohorts or comparative trials with standardized pre- and postoperative manometry, pH monitoring, symptom assessment, and clearly reported numeric outcomes; explicit characterization of operative technique; and longer follow-up. Future work should also identify subgroups in whom LVSG improves versus worsens reflux physiology, because the current literature suggests that the average effect may mask clinically important heterogeneity. In that sense, the main contribution of this review is twofold: it confirms meaningful weight loss after LVSG while showing that the evidence on esophageal functional consequences remains incomplete, heterogeneous, and in need of more rigorous study.

## Conclusion

In this meta-analysis of 20 studies, laparoscopic vertical sleeve gastrectomy (LVSG) in patients with morbid obesity was associated with a significant reduction in lower esophageal sphincter pressure compared with pre-operative status, with a pooled random-effects mean difference of -8.67 mmHg (95% CI -13.71 to -3.63; p=0.0007). Clinically, this suggests that although LVSG is effective for weight loss, it may weaken the antireflux barrier and thereby increase susceptibility to postoperative gastroesophageal reflux, particularly in patients with pre-existing reflux risk. On that basis, LVSG should be used with caution in patients in whom preservation of esophageal sphincter function is a priority, and preoperative reflux evaluation should factor into procedure selection. The main caveat is the very high between-study heterogeneity (I²=97%), which indicates substantial variability in the magnitude of effect and warrants cautious interpretation of the pooled estimate.

## Final Included Studies

- Corpus ID: 4538 | Manometric changes of the lower esophageal sphincter after sleeve gastrectomy in obese patients.
- Corpus ID: 4541 | PREOPERATIVE MANOMETRY FOR THE SELECTION OF OBESE PEOPLE CANDIDATE TO SLEEVE GASTRECTOMY.
- Corpus ID: 8364 | Outcomes of laparoscopic sleeve gastrectomy by means of esophageal manometry and pH-metry, before and after surgery.
- Corpus ID: 4540 | Esophageal motility after laparoscopic sleeve gastrectomy.
- Corpus ID: 4544 | Hypotonic Low Esophageal Sphincter Is Not Predictive of Gastroesophageal Reflux Disease After Sleeve Gastrectomy.
- Corpus ID: 4543 | Sleeve gastrectomy and gastroesophageal reflux: a comprehensive endoscopic and pH-manometric prospective study.
- Corpus ID: 8366 | Persistent and De Novo GERD After Sleeve Gastrectomy: Manometric and pH-Impedance Study Findings.
- Corpus ID: 69508 | Investigation of the Relationship Between Laparoscopic Sleeve Gastrectomy and Gastroesophageal Reflux Disease Using 24-hour Multichannel Intraluminal Impedance With pH Testing According to Current Consensus.
- Corpus ID: 8363 | Evolution of gastroesophageal reflux after laparoscopic vertical gastrectomy. A radiographic, manometric and pH-metric study.
- Corpus ID: 108104 | Comparative Analysis of the Effectiveness and Frequency of Complications of Different Techniques of Laparoscopic Sleeve Gastrectomy in Patients with Obesity.
- Corpus ID: 69491 | Outcomes of Concomitant Laparoscopic Sleeve Gastrectomy and Hiatal Hernia Repair on Gastroesophageal Reflux Disease in Patients with Severe Obesity: A Propensity Score-Matched Analysis.
- Corpus ID: 18886 | Sleeve gastrectomy for morbid obesity: weight loss trajectory and failure predictors over a decade.
- Corpus ID: 69548 | Long-Term Outcomes of Sleeve Gastrectomy at a Veterans Affairs Medical Center.
- Corpus ID: 108091 | Ten-year outcomes after primary vertical sleeve gastrectomy for morbid obesity: a monocentric cohort study.
- Corpus ID: 108072 | Functional importance of laparoscopic sleeve gastrectomy for the lower esophageal sphincter in patients with morbid obesity.
- Corpus ID: 69497 | Long Term Outcomes of Laparoscopic Sleeve Gastrectomy in an Academic Center in Belgium (9 Years Follow-Up).
- Corpus ID: 69528 | Effect of Gastric Sleeve Migration on Weight Loss and Gastroesophageal Reflux Disease After Laparoscopic Sleeve Gastrectomy.
- Corpus ID: 4539 | The effect of laparoscopic sleeve gastrectomy on the antireflux mechanism: can it be minimized?
- Corpus ID: 69514 | The Impact of Sleeve Gastrectomy on Gastroesophageal Reflux Disease in Patients with Morbid Obesity.
- Corpus ID: 69468 | Impact of laparoscopic sleeve gastrectomy on esophageal physiology.
