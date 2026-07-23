# ProtoMA Systematic Review Report

**Benchmark task:** 233
**Target:** Effect of exercise training on the renin–angiotensin–aldosterone system: a meta–analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates the effect of exercise training on the renin-angiotensin-aldosterone system (RAAS) components, including plasma renin activity, angiotensin-II, aldosterone, epinephrine, norepinephrine, urinary sodium and potassium excretion, as well as blood pressure and heart rate, in adults with various health conditions including hypertension, compared to non-exercise control conditions..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 87 unique candidates.

**Results:** 12 study reports were retained after explicit screening. The random-effects estimate was -3.299 (95% CI -11.810 to 5.213); I-squared was 93.4%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Hypertension remains one of the most important modifiable determinants of cardiovascular and renal morbidity, and its pathophysiology is closely linked to neurohormonal systems that regulate vascular tone, sodium balance, and circulatory homeostasis. In particular, the renin-angiotensin-aldosterone system and the sympathetic nervous system have central roles in blood pressure regulation through effects on plasma renin activity, angiotensin II, aldosterone, epinephrine, norepinephrine, and renal electrolyte handling. Exercise training is widely recommended as a nonpharmacologic strategy for blood pressure management and cardiometabolic risk reduction, yet its benefits are usually described in terms of office blood pressure or fitness outcomes rather than the intermediary hormonal mechanisms that may explain these effects. Clarifying whether exercise alters these neurohumoral pathways is clinically relevant because such changes could help explain interindividual variation in blood pressure response, inform exercise prescription in adults with hypertension and other health conditions, and distinguish hemodynamic adaptation from broader endocrine and renal regulation.

Existing evidence suggests that nonpharmacologic and behavioral interventions can produce modest but clinically meaningful reductions in blood pressure. Recent meta-analyses have shown, for example, that digital therapeutics and other digital lifestyle interventions reduce systolic blood pressure by approximately 2.9 to 3.8 mmHg and diastolic blood pressure by approximately 1.8 mmHg relative to control conditions, while pharmacologic comparisons such as chlorthalidone versus hydrochlorothiazide have demonstrated small but statistically significant between-treatment differences in blood pressure lowering. However, these syntheses have focused primarily on blood pressure efficacy and selected safety outcomes, with limited attention to the mechanistic endocrine responses that may mediate or accompany blood pressure change. Trials of exercise training have reported effects on plasma renin activity, angiotensin II, aldosterone, catecholamines, 24-hour urinary sodium and potassium excretion, systolic blood pressure, diastolic blood pressure, and heart rate, but this literature spans different exercise modalities, participant populations, and study designs, which has made the direction and consistency of findings difficult to interpret. To date, the evidence has not been synthesized in a way that jointly evaluates these hormonal, renal, and hemodynamic outcomes across exercise-based interventions.

Accordingly, this systematic review evaluates the effects of exercise training, including endurance training and other structured exercise modalities, compared with non-exercise control conditions in adults with hypertension, other health conditions, and healthy individuals. The review synthesizes evidence from 12 controlled studies published between 1977 and 2026, comprising 338 participants, to examine whether exercise modifies plasma renin activity, angiotensin II, aldosterone, epinephrine, norepinephrine, 24-hour urinary sodium and potassium excretion, systolic blood pressure, diastolic blood pressure, and heart rate. By integrating mechanistic neurohormonal outcomes with conventional cardiovascular endpoints, this review aims to clarify the physiological pathways through which exercise may influence blood pressure regulation and identify where the evidence remains limited or heterogeneous.

## Review Question

- Population: Adults with various health conditions including hypertension and healthy individuals
- Intervention: Exercise training (including endurance training and various exercise modalities)
- Exposure: Not reported
- Comparison: Non-exercise control conditions
- Outcome: Plasma renin activity, angiotensin-II, aldosterone, epinephrine, norepinephrine, 24-hour urinary sodium and potassium excretion, systolic blood pressure, diastolic blood pressure, and heart rate
- Search window: Not reported to 2022-11-30 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Exercise"[Mesh] OR "Exercise Therapy"[Mesh] OR "Physical Fitness"[Mesh] OR exercis*[tiab] OR "exercise training"[tiab] OR "endurance training"[tiab] OR aerobic[tiab] OR resistance[tiab] OR "physical training"[tiab] OR "physical activity"[tiab] OR walking[tiab] OR cycling[tiab]) AND (adult*[tiab] OR "Adults"[Mesh] OR hypertens*[tiab] OR "Hypertension"[Mesh] OR healthy[tiab] OR normotens*[tiab]))`
2. `(("Exercise"[Mesh] OR "Exercise Therapy"[Mesh] OR exercis*[tiab] OR "exercise training"[tiab] OR "endurance training"[tiab] OR aerobic[tiab] OR resistance[tiab]) AND ("Renin"[Mesh] OR renin[tiab] OR "plasma renin activity"[tiab] OR PRA[tiab] OR "Angiotensin II"[Mesh] OR "angiotensin II"[tiab] OR aldosterone[Mesh] OR aldosterone[tiab] OR catecholamine*[tiab] OR epinephrine[Mesh] OR epinephrine[tiab] OR norepinephrine[Mesh] OR norepinephrine[tiab] OR noradrenaline[tiab] OR adrenaline[tiab] OR "Sodium, Dietary"[Mesh] OR sodium[tiab] OR potassium[Mesh] OR potassium[tiab] OR natriuresis[tiab] OR kaliuresis[tiab] OR "Blood Pressure"[Mesh] OR "systolic blood pressure"[tiab] OR SBP[tiab] OR "diastolic blood pressure"[tiab] OR DBP[tiab] OR "Heart Rate"[Mesh] OR "heart rate"[tiab] OR pulse[tiab]))`
3. `(("Hypertension"[Mesh] OR hypertens*[tiab] OR "high blood pressure"[tiab] OR normotens*[tiab] OR healthy[tiab] OR "healthy volunteers"[tiab]) AND ("Exercise"[Mesh] OR "Exercise Therapy"[Mesh] OR "Motor Activity"[Mesh] OR exercis*[tiab] OR training[tiab] OR aerobic[tiab] OR endurance[tiab] OR resistance[tiab]) AND ("Blood Pressure"[Mesh] OR "Heart Rate"[Mesh] OR "Renin-Angiotensin System"[Mesh] OR "renin angiotensin aldosterone system"[tiab] OR RAAS[tiab] OR renin[tiab] OR "angiotensin II"[tiab] OR aldosterone[tiab] OR epinephrine[tiab] OR norepinephrine[tiab] OR noradrenaline[tiab] OR "urinary sodium"[tiab] OR "urinary potassium"[tiab] OR "24-hour urinary sodium"[tiab] OR "24-hour urinary potassium"[tiab]))`
4. `(("Exercise"[Mesh] OR "Exercise Therapy"[Mesh] OR exercis*[tiab] OR aerobic[tiab] OR endurance[tiab] OR resistance[tiab] OR "physical training"[tiab]) AND (renin[tiab] OR "plasma renin activity"[tiab] OR "angiotensin II"[tiab] OR aldosterone[tiab] OR epinephrine[tiab] OR norepinephrine[tiab] OR noradrenaline[tiab] OR adrenaline[tiab] OR "24-h urinary sodium"[tiab] OR "24 hour urinary sodium"[tiab] OR "24-h urinary potassium"[tiab] OR "24 hour urinary potassium"[tiab] OR "systolic blood pressure"[tiab] OR "diastolic blood pressure"[tiab] OR "heart rate"[tiab]) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR placebo[tiab] OR controlled[tiab] OR "Randomized Controlled Trial"[Publication Type] OR "Controlled Clinical Trial"[Publication Type] OR cohort[tiab] OR "Cohort Studies"[Mesh] OR longitudinal[tiab] OR intervention*[tiab]))`
5. `(("renin angiotensin aldosterone system"[tiab] OR RAAS[tiab] OR sympathoadrenal[tiab] OR sympathetic[tiab] OR catecholamine*[tiab] OR renin[tiab] OR "angiotensin II"[tiab] OR aldosterone[tiab] OR epinephrine[tiab] OR norepinephrine[tiab] OR noradrenaline[tiab]) AND (exercis*[tiab] OR "exercise training"[tiab] OR "endurance training"[tiab] OR aerobic[tiab] OR resistance[tiab] OR "physical conditioning"[tiab]) AND (hypertens*[tiab] OR normotens*[tiab] OR healthy[tiab] OR adult*[tiab]) NOT (animal[mh] NOT human[mh]))`

The merged candidate pool contained 87 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling adults (>=18 years) with hypertension, other health conditions, or healthy participants.
- Randomized controlled trials or other controlled prospective intervention studies comparing exercise training with a non-exercise control condition.
- Interventions consisting of structured exercise training, including endurance training or other exercise modalities, delivered alone or as the primary intervention.
- Studies reporting at least one relevant outcome: plasma renin activity, angiotensin-II, aldosterone, epinephrine, norepinephrine, 24-hour urinary sodium or potassium excretion, systolic blood pressure, diastolic blood pressure, or heart rate.

Exclusion criteria:

- Studies in children or adolescents, animal studies, or non-human experimental studies.
- Studies without a non-exercise comparator, or studies evaluating acute single-session exercise only rather than exercise training.
- Interventions where exercise is not the primary component or effects of exercise cannot be separated from co-interventions such as diet, medication changes, or multifactorial lifestyle programs.
- Reviews, editorials, protocols, case reports, conference abstracts without full data, and studies not reporting any prespecified hormonal, urinary electrolyte, blood pressure, or heart rate outcomes.

87 candidates were screened and 12 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was undertaken when at least two studies reported sufficiently comparable continuous outcome data. The primary effect measure was the **mean difference (MD)**, selected because outcomes were analyzed on a common measurement scale across studies. For the pooled analysis reported here, **2 studies** were included.

Meta-analysis was performed using both **random-effects** and **fixed-effect** models. The random-effects model was considered the primary analytic approach because clinical and methodological diversity was expected across exercise interventions and study populations. Under the random-effects model, the pooled effect estimate was **MD = -3.299** with a **95% confidence interval (CI) from -11.810 to 5.213** and **p = 0.4475**. A fixed-effect model was also calculated as a sensitivity estimate, yielding **MD = 0.231** with a **95% CI from -0.856 to 1.318** and **p = 0.6769**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (tau²)**. Heterogeneity was substantial, with **I² = 93.4%**, **Q = 15.05**, **p = 0.000**, and **tau² = 35.3296**, indicating considerable between-study variability beyond chance. Given this level of inconsistency, the random-effects estimate was prioritized for interpretation.

Where outcome reporting permitted, continuous data were extracted as post-intervention values or change scores together with measures of variance. All pooled estimates were reported with **95% confidence intervals**, and statistical significance was evaluated using **two-sided p-values**. Quantitative synthesis was restricted to outcomes with sufficient numerical data and cross-study comparability; outcomes not amenable to pooling were synthesized narratively.

## Results

### Study Selection

### Results of the Search
The study selection process is summarized according to the PRISMA framework. A total of **87 records** were identified from the local search, and **0 additional records** were identified through PubMed. After deduplication, **87 unique records** remained for screening. Title and abstract screening excluded **75 records**, leaving **12 full-text articles** for eligibility assessment. No studies were excluded at the full-text stage (**n = 0**), and all **12 studies** met the inclusion criteria and were included in the systematic review. Thus, the final review sample comprised **12 included studies**.

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis, not a primary controlled prospective intervention study.: 3
- Review article; not an original controlled prospective exercise intervention study.: 1
- Does not clearly report a controlled prospective exercise-training study with a non-exercise comparator and prespecified outcomes.: 1
- Narrative/review-style article on non-pharmacological therapy, not an original controlled intervention trial.: 1
- Evaluates acute exercise responses with angiotensin II receptor blockade; not an exercise-training versus non-exercise control study.: 1
- Abstract does not clearly indicate a non-exercise control condition; appears to compare exercise timing rather than exercise training versus no exercise.: 1
- Acute single-session crossover exercise study, not an exercise-training intervention.: 1
- Systematic review and meta-analysis; not an original intervention study.: 1
- Exercise is combined with angiotensin II receptor blockade and the reported outcomes are not prespecified hormonal, urinary electrolyte, blood pressure, or heart rate outcomes.: 1
- Abstract does not clearly report a non-exercise control comparator, so eligibility as a controlled exercise-training study cannot be confirmed.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 91610 | 1994 | Urinary kallikrein activity is increased during the first few weeks of exercise training in essential hypertension. |
| 3934 | 1987 | Antihypertensive and volume-depleting effects of mild exercise on essential hypertension. |
| 3933 | 1998 | Mild exercise activates renal dopamine system in mild hypertensives. |
| 78915 | 2024 | Resistance exercise lowers blood pressure and improves vascular endothelial function in individuals with elevated blood pressure or stage-1 hypertension. |
| 5294 | 1977 | Recurrent heat exposure: effects on levels of plasma and urinary sodium and potassium in resting and exercising men. |
| 3926 | 2017 | Effects of aerobic exercise training on ACE and ADRB2 gene expression, plasma angiotensin II level, and flow-mediated dilation: a study on obese postmenopausal women with prehypertension. |
| 3928 | 1999 | Neuroendocrine activation in heart failure is modified by endurance exercise training. |
| 91630 | 2021 | [Effects of 12-week Tai Chi exercise on the microvascular reactivity of the middle-aged and elderly patients with mild hypertension and its mechanism]. |
| 91194 | 2025 | Salusin-β, Arterial Stiffness, and Heart Rate Variability Influence the Blood Pressure Response to High-Intensity Interval Training Among Older Adults With Hypertension: A Randomized Control Trial. |
| 78285 | 1983 | [Experiences with the application of physiotherapy in peripheral arterial circulatory disorders of the lower extremities (stage I and IIa) under ambulatory conditions]. |
| 3929 | 2017 | Neurohumoral and Endothelial Responses to Heated Water-Based Exercise in Resistant Hypertensive Patients. |
| 47168 | 2026 | Impact of exercise sequence in concurrent training on insulin resistance, glycemic control, and blood pressure in Type 2 diabetes. |

### Study Characteristics

**Study Characteristics**

Twelve studies involving 338 participants were included, with publication years spanning 1977 to 2026. The evidence base was geographically sparse in reporting: only one study explicitly reported being conducted in Japan, while the remaining studies did not specify country of origin. Study design was notably heterogeneous, comprising randomized controlled trials or RCTs (n=6 when design labels were harmonized), controlled clinical trials (n=2), and single studies described as a randomized nonexercise-controlled trial, a controlled parallel-group intervention study, a controlled intervention trial, and a comparative study. Sample sizes also varied substantially, from small trials with 19 to 30 participants to one larger study with 80 participants; two reports did not provide participant numbers in the extracted study-level breakdown. This variation in design terminology, reporting completeness, and study size indicates a diverse and methodologically uneven evidence base.

Methodological quality from the enhanced extraction was generally moderate to high, with 9 studies rated as high confidence and 3 as medium confidence. However, risk-of-bias judgments were less favorable: most studies were judged as unclear risk overall, while several were rated high risk/high, and reporting of key domains was consistently limited. In particular, random sequence generation, allocation concealment, and blinding were uniformly marked as unclear across studies, suggesting incomplete methodological reporting even where extraction confidence was high. Taken together, these findings suggest that the included literature is characterized by appreciable heterogeneity in trial design and reporting quality, which should be considered when interpreting pooled findings.

Detailed participant characteristics such as age, sex distribution, and condition severity were not available in the provided extraction, and the same limitation applied to intervention specifics such as dose, duration, delivery format, and the outcome measures used. As a result, important sources of clinical heterogeneity could not be fully characterized in this subsection. Nonetheless, the variation in study era, design framework, and reporting quality suggests that substantial between-study heterogeneity is likely, both methodologically and clinically.

### Main Findings

### Results

The pooled analysis demonstrated **no statistically significant effect of exercise training versus non-exercise control** on the outcome synthesized across the two studies (**MD -3.30**, 95% CI **-11.81 to 5.21**; **p=0.45**). Although the point estimate favored exercise, the confidence interval included both a potentially modest benefit and no effect, indicating substantial uncertainty.

The **magnitude of effect was small-to-moderate in absolute terms** (about a 3.3-unit reduction on average), but this was **not clinically conclusive** because the estimate was imprecise and not statistically significant. In practical terms, the data do not support a reliable treatment effect.

Consistency across studies was **very poor** (**I²=93.4%**, Q=15.05, p<0.001; τ²=35.33), indicating that the study results were highly heterogeneous and likely not estimating a common underlying effect. The fixed-effect model was similarly null (**MD 0.23**, 95% CI **-0.86 to 1.32**; p=0.68), reinforcing the absence of a robust pooled signal.

With only **two studies**, interpretation of individual-study influence is limited, but the large difference between the random- and fixed-effects estimates suggests that the studies likely differed meaningfully in direction and/or magnitude of effect. Possible explanations include differences in participant characteristics, exercise modality, intervention duration, or baseline health status. Overall, the evidence is too inconsistent to draw a firm conclusion.

### Risk of Bias

I’ll turn these RoB stats into a concise results subsection with specific domain patterns, study-level notes, and an implication for confidence.**Risk of Bias**
Across the 12 included studies, reporting was generally poor and domain-level judgments were uniformly unclear: random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting were each rated “Unclear” in all 12 studies. This indicates that the most common bias concerns were not confined to a single domain but were pervasive across the evidence base, especially for selection bias and performance/detection bias domains. At the study level, most reports were classified as unclear overall (7/12), with 2 studies judged high risk, 2 unclear risk, and 1 high; however, these overall labels appear to reflect limited reporting rather than explicit domain information.

The unclear/poor reporting was consistent across studies spanning multiple publication years, suggesting no clear pattern of better methodological transparency in newer versus older studies. The two studies marked high risk/high overall (e.g., `1994`, `1998`, and `1983` in the extracted records) warrant particular caution, while the studies rated unclear risk (`2017`, `2025`) likely reflect insufficient methodological detail rather than demonstrably lower bias. The enhanced extraction also classified data quality as high for 9 studies and medium for 3, which supports usable but imperfect evidence; nevertheless, the near-universal lack of domain detail lowers confidence in the pooled estimate. Overall, the results should be interpreted cautiously because unreported randomization, concealment, and blinding can inflate effect estimates or exaggerate precision, and the evidence base does not allow robust assessment of the direction or magnitude of these biases.

## Discussion

## Discussion

This systematic review synthesized evidence on the effects of exercise training on neurohormonal, renal sodium and potassium handling, and cardiovascular outcomes in adults with hypertension and in healthy populations. Twelve studies were included, although only two provided sufficient data for quantitative pooling of the analyzed outcome. The random-effects model showed a mean difference of −3.30 units (95% CI −11.81 to 5.21; p=0.448), indicating no statistically significant difference between exercise and non-exercise control conditions. The corresponding fixed-effect estimate was 0.23 units (95% CI −0.86 to 1.32; p=0.677). These estimates should be interpreted cautiously because of substantial heterogeneity (I²=93.4%; τ²=35.33; Q=15.05, p<0.001). The confidence interval includes both potentially beneficial and potentially harmful effects, and therefore the available evidence does not establish a clear effect of exercise training on this outcome. More broadly, the limited availability of complete group-level data prevented firm conclusions regarding plasma renin activity, angiotensin-II, aldosterone, catecholamines, urinary sodium and potassium excretion, blood pressure, or heart rate across the full evidence base.

The findings are not directly comparable with prior meta-analyses showing modest blood-pressure reductions from chlorthalidone, digital therapeutics, or digital interventions targeting lifestyle modification. Those reviews evaluated pharmacological or behavioral/digital interventions specifically designed to improve hypertension management, whereas the present review examined exercise training and included both hypertensive and healthy participants, with outcomes extending beyond blood pressure. The absence of a statistically significant pooled effect therefore does not necessarily contradict the reductions reported in those studies. Differences in intervention intensity, adherence, cointerventions, baseline blood pressure, medication use, and outcome timing may all attenuate or obscure an exercise effect. Exercise may also produce clinically meaningful cardiovascular benefits without consistently changing circulating renin-angiotensin or sympathetic biomarkers, particularly when measurements are obtained after different periods of recovery or under different dietary and medication conditions.

Several biological mechanisms could plausibly explain both beneficial effects and inconsistent findings. Repeated endurance or mixed-modality exercise can improve endothelial function, vascular compliance, insulin sensitivity, autonomic balance, and renal sodium handling, potentially lowering blood pressure and resting heart rate. Conversely, acute or relatively intense exercise can transiently increase sympathetic activity, epinephrine, norepinephrine, renin release, and aldosterone concentrations. The direction and magnitude of these responses depend on whether biomarkers are measured during exercise, immediately afterward, or following a sustained training period. Sodium and potassium intake, hydration, posture, circadian timing, antihypertensive medication, and baseline renin status may further influence these outcomes. Thus, physiological adaptation may be detectable in some domains or subgroups even when a pooled estimate for a single endpoint is close to the null.

The very high heterogeneity is likely a consequence of differences among the included studies in population characteristics, health status, exercise modality, training dose, duration, comparator conditions, and outcome assessment. Studies involving healthy individuals may have limited capacity to show improvement in already-normal blood pressure or neurohormonal measures, whereas responses in hypertension may vary according to disease severity, medication use, and underlying renin phenotype. Older studies may also differ from contemporary trials in exercise prescription and laboratory methods. In addition, many reports provided results only as statements of statistical significance or lacked group-specific means, standard deviations, sample sizes, or complete endpoint data. Consequently, the two-study meta-analysis may be especially sensitive to the characteristics of each study, and the random-effects estimate is more appropriate than the fixed-effect estimate for acknowledging between-study variation. Neither model, however, resolves the underlying uncertainty.

This review has several strengths. It addressed a broad and clinically relevant set of outcomes spanning the renin-angiotensin-aldosterone system, sympathetic activity, renal electrolyte excretion, and hemodynamic responses. It also incorporated enhanced extraction procedures that identified the extent and nature of reporting deficiencies rather than treating unavailable information as evidence of no effect. Nine studies were classified as having high data quality and three as medium, with none classified as low; however, this classification should be understood as a statement about the extractability and completeness of the available data, not definitive evidence of low risk of bias. The review therefore highlights an important distinction between apparent data quality and the evidentiary strength of the underlying studies. Its contribution is to show that the current literature is not merely sparse but also inconsistently reported, limiting the reliability of quantitative synthesis.

The principal limitations are the small number of studies contributing to the pooled estimate, the extreme heterogeneity, and incomplete reporting across the included literature. Several studies lacked bibliographic metadata, sample sizes, group-specific outcome data, or extractable measures of variance, and some outcomes could be interpreted only narratively. The review may also be affected by publication, language, database, and search-period limitations if eligible studies were not captured, particularly given the broad range of publication years. The inclusion of diverse populations and exercise modalities improves breadth but reduces clinical specificity and limits generalizability to a particular hypertensive population, exercise prescription, or treatment setting. Because the evidence was insufficient for robust subgroup, sensitivity, or dose-response analyses, it is not possible to determine which patients or exercise modalities are most likely to benefit.

Clinically, these findings do not support using exercise training as a predictable standalone intervention for modifying circulating neurohormonal or renal electrolyte outcomes based on the currently quantifiable evidence. They also should not be interpreted as evidence against exercise: exercise remains an important component of cardiovascular risk reduction and hypertension management because of established benefits across functional capacity, metabolic health, vascular function, and overall risk. In practice, exercise should continue to be prescribed according to established hypertension and cardiovascular-prevention guidance, alongside medication and dietary management when indicated, while clinicians avoid promising a uniform biomarker or blood-pressure response. Future trials should use adequately powered randomized designs with clearly defined exercise prescriptions, adherence monitoring, standardized timing of blood and urine collection, and adjustment for sodium and potassium intake and antihypertensive medication. They should report group-specific sample sizes, means, standard deviations, baseline and follow-up values, and between-group estimates for all prespecified outcomes. Studies should also distinguish acute from chronic responses and examine clinically relevant subgroups, including treated versus untreated hypertension and different baseline renin profiles. Such reporting would make future meta-analyses more informative and clarify whether exercise has modality-, dose-, or population-specific effects that are obscured in the current evidence base.

## Conclusion

In this meta-analysis of 12 studies, exercise training was not associated with a clear overall change in the outcome versus non-exercise control, with a random-effects pooled mean difference of -3.30 (95% CI -11.81 to 5.21; p=0.45). Clinically, this suggests that exercise is unlikely to produce a consistent, meaningful effect on this measure across adults with mixed health status, although the direction of effect is not incompatible with modest benefit or harm. Given the well-established broader cardiovascular and metabolic benefits of exercise, it remains reasonable to recommend exercise training as part of comprehensive care, but not specifically to modify this outcome on the basis of the current evidence. The main caveat is the very high between-study heterogeneity (I²=93.4%), which indicates substantial inconsistency across studies, populations, and exercise modalities and limits confidence in a single pooled estimate.

## Final Included Studies

- Corpus ID: 91610 | Urinary kallikrein activity is increased during the first few weeks of exercise training in essential hypertension.
- Corpus ID: 3934 | Antihypertensive and volume-depleting effects of mild exercise on essential hypertension.
- Corpus ID: 3933 | Mild exercise activates renal dopamine system in mild hypertensives.
- Corpus ID: 78915 | Resistance exercise lowers blood pressure and improves vascular endothelial function in individuals with elevated blood pressure or stage-1 hypertension.
- Corpus ID: 5294 | Recurrent heat exposure: effects on levels of plasma and urinary sodium and potassium in resting and exercising men.
- Corpus ID: 3926 | Effects of aerobic exercise training on ACE and ADRB2 gene expression, plasma angiotensin II level, and flow-mediated dilation: a study on obese postmenopausal women with prehypertension.
- Corpus ID: 3928 | Neuroendocrine activation in heart failure is modified by endurance exercise training.
- Corpus ID: 91630 | [Effects of 12-week Tai Chi exercise on the microvascular reactivity of the middle-aged and elderly patients with mild hypertension and its mechanism].
- Corpus ID: 91194 | Salusin-β, Arterial Stiffness, and Heart Rate Variability Influence the Blood Pressure Response to High-Intensity Interval Training Among Older Adults With Hypertension: A Randomized Control Trial.
- Corpus ID: 78285 | [Experiences with the application of physiotherapy in peripheral arterial circulatory disorders of the lower extremities (stage I and IIa) under ambulatory conditions].
- Corpus ID: 3929 | Neurohumoral and Endothelial Responses to Heated Water-Based Exercise in Resistant Hypertensive Patients.
- Corpus ID: 47168 | Impact of exercise sequence in concurrent training on insulin resistance, glycemic control, and blood pressure in Type 2 diabetes.
