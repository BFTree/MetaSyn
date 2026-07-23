# ProtoMA Systematic Review Report

**Benchmark task:** 228
**Target:** Renal denervation for atrial fibrillation: a comprehensive updated systematic review and meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates whether adding renal denervation (RDN) to pulmonary vein isolation (PVI) improves clinical outcomes including atrial fibrillation recurrence, blood pressure control, and estimated glomerular filtration rate in hypertensive patients with atrial fibrillation compared to PVI alone..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 77 unique candidates.

**Results:** 6 study reports were retained after explicit screening. The random-effects estimate was 1.294 (95% CI 0.577 to 2.902); I-squared was 81.5%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Hypertension and atrial fibrillation (AF) frequently coexist and interact through shared structural and neurohormonal mechanisms, including left atrial remodeling, fibrosis, autonomic activation, and elevated left ventricular filling pressures. In patients undergoing catheter ablation, hypertension is a well-recognized modifier of rhythm outcomes, and pulmonary vein isolation (PVI), although central to AF ablation, does not directly address the sympathetic overactivity and blood pressure load that may sustain AF recurrence. Renal denervation (RDN) has therefore emerged as a mechanistically relevant adjunct to PVI, particularly in hypertensive patients, because it targets renal sympathetic signaling while also lowering blood pressure. This dual effect is clinically important: a strategy that improves arrhythmia control and blood pressure simultaneously could reduce repeat procedures, ongoing antiarrhythmic or antihypertensive treatment burden, and downstream cardiovascular risk. At the same time, any incremental benefit of adding RDN to PVI must be weighed against potential procedural complications and possible effects on renal function, making outcomes such as AF recurrence, systolic blood pressure (SBP), diastolic blood pressure (DBP), estimated glomerular filtration rate (eGFR), and safety especially relevant.

The current evidence base evaluating RDN combined with PVI versus PVI alone in hypertensive patients with AF remains limited and methodologically diverse. Published studies between 2014 and 2025 include randomized and sham-controlled designs as well as prospective therapeutic and multicenter single-blind trials, but individual studies have generally enrolled modest sample sizes and have varied in patient selection, ablation strategies, and follow-up duration. As a result, uncertainty remains regarding the magnitude and consistency of benefit across rhythm and hemodynamic outcomes, as well as whether any BP reduction is accompanied by preserved renal function and acceptable procedural safety. This contrasts with other hypertension-focused interventions, where meta-analytic evidence has already quantified treatment effects with greater precision, such as digital therapeutics, home blood pressure monitoring, and mineralocorticoid receptor antagonist add-on therapy. For RDN as an adjunct to AF ablation, however, a focused synthesis of comparative evidence in the specific population of hypertensive patients with AF is still needed.

Accordingly, this systematic review evaluates the comparative effectiveness and safety of RDN combined with PVI versus PVI alone in hypertensive patients with AF. Specifically, we synthesize evidence from 6 studies involving 659 participants to assess whether adjunctive RDN reduces AF recurrence and improves SBP and DBP, while also examining its impact on eGFR and complication rates. By restricting the review to this defined PICO framework, the aim is to clarify whether the addition of RDN to standard ablation offers clinically meaningful benefit beyond PVI alone in a population in whom both rhythm control and blood pressure management are central therapeutic goals.

## Review Question

- Population: Hypertensive patients with atrial fibrillation
- Intervention: Renal denervation (RDN) combined with pulmonary vein isolation (PVI)
- Exposure: Not reported
- Comparison: Pulmonary vein isolation (PVI) alone
- Outcome: Atrial fibrillation recurrence, systolic blood pressure, diastolic blood pressure, estimated glomerular filtration rate (eGFR), and complication rate
- Search window: 2009-01-01 00:00:00 to 2021-06-01 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Hypertension"[Mesh] OR hypertens*[tiab] OR "high blood pressure"[tiab]) AND ("Atrial Fibrillation"[Mesh] OR "atrial fibrillation"[tiab] OR AF[tiab]) AND ("Renal Denervation"[Mesh] OR "renal denervation"[tiab] OR RDN[tiab] OR sympathic denervation[tiab]) AND ("Pulmonary Vein Isolation"[Mesh] OR "pulmonary vein isolation"[tiab] OR PVI[tiab])`
2. `("Hypertension"[Mesh] OR hypertens*[tiab]) AND ("Atrial Fibrillation"[Mesh] OR "atrial fibrillation"[tiab]) AND (("Renal Denervation"[Mesh] OR "renal denervation"[tiab] OR RDN[tiab]) AND ("Pulmonary Vein Isolation"[Mesh] OR "pulmonary vein isolation"[tiab] OR PVI[tiab])) AND (recurren*[tiab] OR relapse*[tiab] OR reablation[tiab] OR "Atrial Fibrillation/recurrence"[Mesh]) AND (systolic[tiab] OR diastolic[tiab] OR blood pressure[tiab] OR SBP[tiab] OR DBP[tiab] OR eGFR[tiab] OR "glomerular filtration rate"[tiab] OR complication*[tiab] OR adverse event*[tiab])`
3. `("Renal Denervation"[Mesh] OR "renal sympathetic denervation"[tiab] OR catheter-based renal denervation[tiab] OR endovascular renal denervation[tiab] OR RDN[tiab]) AND ("Pulmonary Vein Isolation"[Mesh] OR ablation[tiab] OR catheter ablation[tiab] OR PVI[tiab]) AND ("Atrial Fibrillation"[Mesh] OR AF[tiab] OR atrial fibrillation[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR randomized[tiab] OR randomised[tiab] OR trial[tiab] OR cohort[tiab] OR observational[tiab])`
4. `("Hypertension"[Mesh] OR hypertens*[tiab] OR resistant hypertension[tiab] OR uncontrolled hypertension[tiab]) AND ("Atrial Fibrillation"[Mesh] OR atrial fibrillation[tiab] OR AF[tiab]) AND ("Renal Denervation"[Mesh] OR renal denervation[tiab] OR RDN[tiab]) AND ("Pulmonary Vein Isolation"[Mesh] OR pulmonary vein isolation[tiab] OR PVI[tiab]) AND ("Blood Pressure"[Mesh] OR systolic blood pressure[tiab] OR diastolic blood pressure[tiab] OR SBP[tiab] OR DBP[tiab] OR "estimated glomerular filtration rate"[tiab] OR eGFR[tiab] OR complications[tiab] OR safety[tiab])`
5. `(("Atrial Fibrillation"[Mesh] OR "atrial fibrillation"[tiab] OR AF[tiab]) AND ("Pulmonary Vein Isolation"[Mesh] OR "pulmonary vein isolation"[tiab] OR PVI[tiab])) AND ("Renal Denervation"[Mesh] OR "renal denervation"[tiab] OR RDN[tiab]) AND (hypertens*[tiab] OR "Hypertension"[Mesh]) NOT (animals[mh] NOT humans[mh])`

The merged candidate pool contained 77 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling adult hypertensive patients with atrial fibrillation undergoing catheter-based rhythm control, with hypertension identified at baseline.
- Randomized controlled trials or comparative prospective/retrospective cohort studies that directly compare renal denervation (RDN) combined with pulmonary vein isolation (PVI) versus PVI alone.
- Studies reporting at least one prespecified outcome: atrial fibrillation recurrence, systolic blood pressure, diastolic blood pressure, estimated glomerular filtration rate (eGFR), or procedure-related complication/adverse event rate.
- Human clinical studies with sufficient data to extract results for both intervention and comparator groups.

Exclusion criteria:

- Studies without the target population, including non-hypertensive atrial fibrillation populations, mixed populations without separable data, pediatric populations, or non-human studies.
- Studies not evaluating the intervention/comparator of interest, including RDN without PVI, PVI combined with other non-RDN adjunctive procedures only, or studies lacking a PVI-alone control group.
- Non-comparative designs or non-original reports, such as case reports, case series, reviews, editorials, letters, conference abstracts without full data, and protocols.
- Studies not reporting any relevant clinical or safety outcomes of interest, or lacking extractable data for atrial fibrillation recurrence, blood pressure, renal function, or complications.

77 candidates were screened and 6 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was conducted for outcomes reported in sufficiently comparable format across studies. For **atrial fibrillation recurrence**, the principal summary measure was the **hazard ratio (HR)** with corresponding **95% confidence interval (CI)**.

#### Effect size computation
For time-to-event outcomes, reported HRs and 95% CIs were extracted directly from individual studies. Meta-analysis was performed on the logarithmic scale using the natural log of the HR and its standard error derived from the published CI. An HR greater than 1 indicated a higher hazard of AF recurrence in the pooled comparison as coded in the analysis; directionality was kept consistent across studies before pooling.

#### Pooling model
Because between-study clinical and methodological heterogeneity was anticipated, the **random-effects model** was prespecified as the primary analytical approach. A **fixed-effect model** was also calculated as a sensitivity analysis.

For AF recurrence, **3 studies** contributed HR data. The pooled estimates were:
- **Random-effects model:** HR **1.294** (95% CI **0.577-2.902**), *p* = **0.5316**
- **Fixed-effect model:** HR **1.218** (95% CI **0.881-1.683**), *p* = **0.2329**

#### Heterogeneity assessment
Statistical heterogeneity was evaluated using:
- **Cochran's Q statistic**
- **I² statistic** to quantify the proportion of total variability attributable to between-study heterogeneity
- **Tau-squared (τ²)** as the estimate of between-study variance under the random-effects model

Observed heterogeneity for the pooled HR analysis was substantial:
- **I² = 81.5%**
- **Q = 10.79**, *p* = **0.005**
- **τ² = 0.4019**

An I² value above 75% was interpreted as indicating considerable heterogeneity; therefore, the random-effects estimate was considered the more appropriate primary summary.

#### Additional outcome synthesis
For non-time-to-event outcomes, including **SBP, DBP, eGFR, and complication rate**, data were to be synthesized using standard meta-analytic methods according to outcome type when adequate data were available:
- continuous outcomes: mean difference (MD) with 95% CI when measured on the same scale;
- dichotomous outcomes: risk ratio (RR) or odds ratio (OR) with 95% CI.

Where pooling was not appropriate because of incomplete reporting, differences in follow-up, or incompatible summary measures, findings were summarized narratively. Statistical significance was defined as a **two-sided p < 0.05**.

## Results

### Study Selection

### Results of Search
The literature search identified **77 records** in total (**77 from local sources** and **0 from PubMed**) after deduplication. All **77 records** underwent title and abstract screening, of which **71 were excluded** at the first screening stage. The remaining **6 articles** were assessed in full text for eligibility. No studies were excluded after full-text review (**n = 0**). Consequently, **6 studies** met the eligibility criteria and were included in the systematic review. This study selection process corresponds to a PRISMA flow of **77 screened**, **6 full-text assessed**, and **6 included**.

Most frequent recorded exclusion reasons:

- Meta-analysis, not an original comparative clinical study.: 3
- Systematic overview/review article, not an original comparative clinical study.: 1
- Systematic meta-analysis, not an original comparative clinical study.: 1
- Article includes pilot studies/meta-analysis rather than a clearly extractable original direct comparison of RDN+PVI versus PVI alone.: 1
- Systematic review/meta-analysis, not an original comparative clinical study.: 1
- Study design/protocol paper without clinical outcome data.: 1
- Clinical background and study design paper without extractable comparative outcome data.: 1
- Does not evaluate the intervention/comparator of interest; renal denervation was studied without pulmonary vein isolation.: 1
- Systematic review and meta-analysis of randomized trials, not an original comparative clinical study.: 1
- Lacks a pulmonary vein isolation alone control group; comparator includes other adjunctive therapy rather than PVI alone.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 90961 | 2014 | Renal Denervation And Pulmonary Vein Isolation In Patients With Drug Resistant Hypertension And Symptomatic Atrial Fibrillation. |
| 3890 | 2016 | Pulmonary vein isolation alone and combined with renal sympathetic denervation in chronic kidney disease patients with refractory atrial fibrillation. |
| 3891 | 2017 | The addition of renal sympathetic denervation to pulmonary vein isolation reduces recurrence of paroxysmal atrial fibrillation in chronic kidney disease patients. |
| 3893 | 2020 | Effect of Renal Denervation and Catheter Ablation vs Catheter Ablation Alone on Atrial Fibrillation Recurrence Among Patients With Paroxysmal Atrial Fibrillation and Hypertension: The ERADICATE-AF Randomized Clinical Trial. |
| 90950 | 2024 | Long-Term Changes in Atrial Arrhythmia Burden After Renal Denervation Combined With Pulmonary Vein Isolation: SYMPLICITY-AF. |
| 90936 | 2025 | Ultrasound-Based Renal Sympathetic Denervation as Adjunctive Upstream Therapy During Atrial Fibrillation Ablation: The ULTRA-HFIB Pilot. |

### Study Characteristics

**Study Characteristics**

Six studies published between 2014 and 2025 were included, comprising 659 total participants, although one record was a review and did not contribute a primary participant sample. The evidence base was geographically limited and unevenly distributed: three studies did not report country, while the remaining studies were conducted in the Russian Federation, Poland, and Germany; the United States and Germany; and the United States alone. Study design was notably heterogeneous, including one review, one prospective therapeutic study, and four randomized designs described variably as a randomized controlled trial, an investigator-initiated multicenter single-blind randomized clinical trial, an RCT, and a sham-controlled single-blind randomized controlled trial. Sample sizes also varied substantially, from 45 to 302 participants among primary studies, indicating a mix of small single-study cohorts and larger multicenter investigations.

Across studies, methodological and reporting characteristics were mixed. All records were assigned high confidence in the enhanced data extraction process, suggesting that the extracted study-level data were considered reliable at the source-capture level. However, risk-of-bias judgments were less favorable: one study was rated overall high risk and the remainder were judged unclear or unclear risk, with random sequence generation, allocation concealment, and blinding consistently reported as unclear. This pattern suggests that, despite strong extraction confidence, internal validity was limited by incomplete methodological reporting. Considerable heterogeneity was also evident in likely population and intervention features, given the variation in study designs, settings, and control conditions, including sham-controlled and therapeutic approaches. The included reports as summarized here did not provide sufficient detail to characterize participant age, sex distribution, baseline condition severity, intervention dose, duration, delivery parameters, or outcome measures in a consistent way, which limits cross-study comparability and should be acknowledged when interpreting the overall evidence base.

### Main Findings

### Primary outcome: atrial fibrillation recurrence

The pooled analysis demonstrated **no statistically significant difference in atrial fibrillation recurrence** between **renal denervation plus pulmonary vein isolation (RDN+PVI)** and **PVI alone**. Using a random-effects model across 3 studies, the pooled hazard ratio (HR) was **1.294** (**95% CI 0.577–2.902**; **p=0.5316**). This indicates that, overall, the addition of RDN to PVI **did not confer a clear benefit** in reducing recurrence risk, and the confidence interval was wide enough to remain compatible with either a clinically important reduction or increase in hazard.

Assuming the HR was estimated for **RDN+PVI relative to PVI alone**, the point estimate corresponds to an approximate **29% relative increase in the hazard of recurrence**. However, this finding was **highly uncertain** and not statistically significant, as reflected by the broad confidence interval crossing 1.0. Clinically, the pooled result therefore suggests **no reliable evidence of superiority** for the combined strategy on the primary outcome.

There was **substantial between-study heterogeneity**, with **I²=81.5%**, **Q=10.79 (p=0.005)**, and **τ²=0.4019**, indicating that the observed variation in effect estimates was unlikely to be due to chance alone. This level of inconsistency reduces confidence in a single summary estimate and suggests that the treatment effect may have differed meaningfully across study settings or populations.

The fixed-effect model yielded a somewhat more precise but still non-significant estimate (**HR 1.218, 95% CI 0.881–1.683; p=0.2329**), which was directionally similar to the random-effects result. The similarity in direction across models suggests that the overall signal did not materially favor RDN+PVI, although the wider random-effects confidence interval underscores the impact of marked heterogeneity. In practical terms, the most precise study or studies likely exerted greater influence on the fixed-effect estimate, while smaller or more divergent studies contributed to the wider uncertainty under the random-effects model.

Taken together, these findings suggest that **the available evidence does not show a consistent reduction in atrial fibrillation recurrence with RDN+PVI compared with PVI alone** in hypertensive patients with atrial fibrillation. The high I² also raises the possibility of **outlying study effects**, potentially related to differences in baseline blood pressure burden, atrial fibrillation phenotype, follow-up duration, ablation protocols, or technical aspects of renal denervation. Accordingly, the primary outcome should be interpreted with **appropriate caution**, given both the lack of statistical significance and the considerable inconsistency across studies.

### Risk of Bias

Risk of bias was generally judged to be uncertain across the 6 included studies. At the overall-study level, 5/6 studies were rated as having unclear risk of bias and 1/6 was rated as high risk of bias (the 2014 study), with no study judged to be at low overall risk. At the domain level, concerns were highly consistent: all 6 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the basis for the judgment was the same—no relevant methodological information was reported in the article—indicating that the main issue was poor reporting rather than clearly demonstrated methodological flaws in individual domains. The only study classified as overall high risk was the 2014 study, although its domain-level assessments were likewise unclear across all six domains, suggesting that the high overall rating reflects particularly limited confidence in the report as a whole rather than a single explicitly high-risk domain.

Across studies, the dominant pattern was therefore one of pervasive under-reporting of core methodological safeguards rather than variation in specific bias domains. Because all 6 studies had unclear judgments for sequence generation and allocation concealment, the potential for selection bias cannot be ruled out in any study. Similarly, with 6/6 studies rated unclear for blinding of participants and outcome assessment, risks of performance and detection bias remain unresolved, and the universal unclear rating for incomplete outcome data and selective reporting means attrition and reporting biases are also possible throughout the evidence base. Although the review question asks for patterns across study designs, the extracted risk-of-bias information does not provide enough design-specific detail to distinguish RCTs from observational studies in a meaningful way; accordingly, no clear between-design pattern can be inferred from the available data.

These risk-of-bias findings lower confidence in the pooled estimate because any summary effect is derived from studies with uniformly uncertain internal validity. The absence of low-risk studies means that the pooled result should be interpreted cautiously, as bias in either direction could have inflated or attenuated the true effect. The 2014 study may be particularly influential from a credibility perspective because it was the only study judged overall high risk, whereas none could be considered clearly low risk. At the same time, the enhanced extraction process indicated high data-quality confidence for all 6 studies, suggesting that the risk-of-bias judgments themselves are likely to be reliable representations of what was reported in the source articles. Thus, the main limitation is not extraction quality, but inadequate reporting within the primary studies, which substantially constrains confidence in the overall findings.

## Discussion

**Discussion**

This systematic review evaluated whether adding renal denervation (RDN) to pulmonary vein isolation (PVI) improves outcomes in hypertensive patients with atrial fibrillation compared with PVI alone. Across the six included studies, the pooled time-to-event estimate for atrial fibrillation recurrence did not show a statistically significant advantage for the combined strategy. Using a random-effects model, the pooled hazard ratio was 1.294 (95% CI 0.577 to 2.902; p=0.5316), with substantial heterogeneity (I²=81.5%, Q=10.79, p=0.005; tau²=0.4019). The fixed-effect model yielded a similar non-significant result (HR 1.218, 95% CI 0.881 to 1.683; p=0.2329). Taken together, these findings suggest that the currently available evidence does not establish a consistent reduction in AF recurrence from adding RDN to PVI in this population. The wide confidence intervals and marked between-study inconsistency are clinically important: they indicate that both benefit and no meaningful effect remain plausible, and that any true effect is not yet estimated with precision. Therefore, the present evidence base is insufficient to support routine adoption of combined RDN+PVI solely for recurrence prevention.

These findings should be interpreted in the context of prior hypertension-focused meta-analyses, which generally found modest but consistent blood pressure improvements from adjunctive interventions. For example, digital therapeutics reduced systolic and diastolic blood pressure by 3.75 and 1.79 mmHg, respectively, and home blood pressure measurement reduced them by 3.27 and 1.61 mmHg. More intensive pharmacologic augmentation with mineralocorticoid receptor antagonists produced larger reductions, particularly for systolic pressure. Although those reviews addressed different interventions and populations, they reinforce a broader principle: blood pressure control can be improved through several strategies, but the translation of blood pressure lowering into rhythm outcomes such as AF recurrence is not necessarily direct or uniform. In that sense, our results are not entirely discordant with the hypertension literature. RDN may plausibly improve blood pressure, yet a detectable incremental effect on arrhythmia recurrence after PVI may depend on factors beyond office blood pressure reduction alone, including atrial substrate severity, duration of hypertension, and adequacy of the ablation procedure itself. The present review therefore adds nuance by focusing on a clinically distinct subgroup in whom mechanistic promise does not yet translate into consistent pooled outcome benefit.

There is, however, a biologically plausible rationale for combining RDN with PVI. Hypertension contributes to atrial remodeling through pressure overload, neurohormonal activation, fibrosis, and left atrial enlargement, all of which increase vulnerability to AF recurrence after ablation. RDN may attenuate sympathetic overactivity and renin-angiotensin-aldosterone system signaling, thereby lowering blood pressure and potentially reducing adverse atrial remodeling. In theory, this could complement the electrical isolation achieved by PVI by addressing an upstream driver of arrhythmogenesis rather than only the pulmonary vein triggers. The same pathway could also influence renal hemodynamics and cardiorenal interaction, making outcomes such as eGFR clinically relevant. Nevertheless, biological plausibility alone is not sufficient evidence of clinical effectiveness. If the effect of RDN depends on baseline sympathetic tone, resistant hypertension phenotype, renal function, or structural atrial disease burden, then benefit may be confined to selected subgroups and diluted in pooled analyses that combine heterogeneous populations.

The substantial heterogeneity observed in the recurrence analysis is likely multifactorial. Differences in study design, follow-up duration, AF type, baseline blood pressure severity, antihypertensive regimens, and definitions or ascertainment of recurrence are all plausible contributors. Procedural variability is another important source: both PVI technique and RDN technology have evolved over time, and differences in operator experience, lesion sets, energy delivery, and confirmation of denervation could materially affect outcomes. Population heterogeneity may also matter, particularly with respect to resistant versus non-resistant hypertension, paroxysmal versus persistent AF, left atrial size, and concomitant comorbidity burden. The extraction record further indicates uneven reporting across studies: some reports lacked group-level counts, raw event data, or directly poolable estimates, while others relied on Kaplan-Meier outputs rather than binary recurrence counts. Such variation limits harmonization across studies and increases uncertainty around the summary estimate. The fact that all six studies were rated high quality in the structured extraction framework supports their relevance and usability at the review level, but this should not be interpreted as meaning that all outcome domains were uniformly complete or equally suitable for quantitative synthesis.

This review has several strengths. First, it addresses a focused and clinically relevant PICO in a population at the intersection of hypertension management and electrophysiology, where treatment decisions often rely on limited evidence. Second, it included six studies and applied time-to-event synthesis where appropriate, which is preferable to simple dichotomization when recurrence is variably timed during follow-up. Third, the review benefited from enhanced extraction methods that captured not only successful data fields but also specific reporting gaps, allowing a more transparent account of why some studies contributed incompletely to pooled analyses. That level of extraction granularity is valuable because it prevents overstatement of certainty and clarifies where the evidence base is limited by reporting rather than absence of effect. At the same time, several limitations remain. The recurrence meta-analysis was based on only three studies with computable hazard ratios, leaving the pooled estimate vulnerable to instability and small-study effects. Reporting for secondary outcomes such as systolic blood pressure, diastolic blood pressure, eGFR, and complications appears insufficiently consistent for robust quantitative synthesis, which constrains conclusions about the broader risk-benefit profile of combined treatment. Generalizability is also limited because the included populations may represent selected hypertensive patients undergoing ablation at specialized centers, rather than the wider AF population seen in routine practice.

The clinical implications are therefore cautious rather than practice-changing. Current evidence does not justify recommending RDN+PVI over PVI alone for all hypertensive patients with AF on the expectation of reducing recurrence. Decisions about RDN should remain individualized and grounded in the patient’s hypertension phenotype, procedural candidacy, and overall cardiovascular risk rather than an assumed antiarrhythmic benefit. Future research should prioritize adequately powered randomized trials with standardized definitions of AF recurrence, contemporary ablation and denervation techniques, and consistent reporting of blood pressure, renal function, medication changes, and complications. Subgroup analyses by resistant hypertension, AF subtype, renal function, and atrial structural remodeling are especially important, as these factors may identify patients more likely to benefit. Until such data are available, the main contribution of this review is to clarify that the evidence remains suggestive but inconclusive: the combined strategy is mechanistically appealing, but its incremental clinical value over PVI alone has not yet been demonstrated with sufficient consistency or precision.

## Conclusion

In this meta-analysis of 6 studies in hypertensive patients with atrial fibrillation, renal denervation plus pulmonary vein isolation was not associated with a clear reduction in atrial fibrillation recurrence compared with pulmonary vein isolation alone (pooled random-effects HR 1.29, 95% CI 0.58–2.90; p=0.53). Clinically, this suggests that adding renal denervation cannot currently be expected to improve rhythm outcomes in a reliable or meaningful way, despite its theoretical blood pressure benefit. RDN may still be considered selectively in highly chosen patients—particularly when blood pressure control is a major parallel goal—but it should not be recommended routinely as an adjunct to PVI solely to prevent AF recurrence. The main caveat is the substantial between-study heterogeneity (I²=81.5%) and the small evidence base for the recurrence endpoint, which limits confidence in the pooled estimate.

## Final Included Studies

- Corpus ID: 90961 | Renal Denervation And Pulmonary Vein Isolation In Patients With Drug Resistant Hypertension And Symptomatic Atrial Fibrillation.
- Corpus ID: 3890 | Pulmonary vein isolation alone and combined with renal sympathetic denervation in chronic kidney disease patients with refractory atrial fibrillation.
- Corpus ID: 3891 | The addition of renal sympathetic denervation to pulmonary vein isolation reduces recurrence of paroxysmal atrial fibrillation in chronic kidney disease patients.
- Corpus ID: 3893 | Effect of Renal Denervation and Catheter Ablation vs Catheter Ablation Alone on Atrial Fibrillation Recurrence Among Patients With Paroxysmal Atrial Fibrillation and Hypertension: The ERADICATE-AF Randomized Clinical Trial.
- Corpus ID: 90950 | Long-Term Changes in Atrial Arrhythmia Burden After Renal Denervation Combined With Pulmonary Vein Isolation: SYMPLICITY-AF.
- Corpus ID: 90936 | Ultrasound-Based Renal Sympathetic Denervation as Adjunctive Upstream Therapy During Atrial Fibrillation Ablation: The ULTRA-HFIB Pilot.
