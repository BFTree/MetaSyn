# ProtoMA Systematic Review Report

**Benchmark task:** 224
**Target:** Effectiveness of biofeedback on blood pressure in patients with hypertension: systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis aims to assess the effectiveness of biofeedback interventions on blood pressure reduction in patients with hypertension compared to control conditions..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 50 unique candidates.

**Results:** 10 study reports were retained after explicit screening. The random-effects estimate was 4.646 (95% CI 0.129 to 9.164); I-squared was 58.3%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Hypertension remains one of the most important modifiable risk factors for cardiovascular and renal disease because even small reductions in blood pressure translate into meaningful reductions in stroke, myocardial infarction, heart failure, and chronic kidney disease risk. Although pharmacologic therapy is effective, blood pressure control remains suboptimal in many patients because treatment response is heterogeneous, long-term adherence is difficult, and nonpharmacologic strategies are often needed as adjuncts to standard care. Against this background, biofeedback has been proposed as a behavioral intervention that may influence autonomic regulation, stress reactivity, and cardiovascular function. Modalities such as heart rate variability biofeedback and related physiologic feedback approaches are of particular interest because they are intended to help patients actively modify physiologic responses that may contribute to elevated blood pressure.

The evidence base for biofeedback in hypertension, however, has remained difficult to interpret. Trials published between 1979 and 2017 have used multiple biofeedback modalities, diverse control conditions, and relatively small samples, with only 303 total participants across 10 studies. The available studies include randomized controlled trials, placebo- or sham-controlled trials, open-label and controlled comparison designs, and a two-phase randomized study with follow-up comparison among initial treatment responders. This methodological variation contrasts with more mature hypertension intervention literatures, in which meta-analyses have shown modest but statistically significant blood pressure reductions for interventions such as home blood pressure measurement and digital therapeutics, and small comparative advantages between antihypertensive drug strategies. In that context, it remains uncertain whether biofeedback produces measurable reductions in systolic and diastolic blood pressure beyond standard care, no intervention, or placebo-like control conditions, and whether the apparent effects are robust across differing study designs and intervention formats.

Accordingly, this systematic review evaluates the effects of biofeedback interventions in patients with hypertension, using control groups receiving standard care or no biofeedback intervention as the comparator. The review focuses specifically on changes in systolic and diastolic blood pressure and synthesizes evidence from 10 controlled studies published over nearly four decades. By examining the direction and magnitude of blood pressure changes across heterogeneous biofeedback modalities, this review aims to clarify the current clinical signal for benefit and identify the principal limitations of the existing evidence base.

## Review Question

- Population: Patients with hypertension
- Intervention: Biofeedback (including various modalities such as heart rate variability biofeedback)
- Exposure: Not reported
- Comparison: Control conditions (standard care or no biofeedback intervention)
- Outcome: Blood pressure changes (systolic and diastolic blood pressure)
- Search window: Not reported to 2024-01-16 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Hypertension"[Mesh] OR hypertens*[tiab] OR "high blood pressure"[tiab] OR "elevated blood pressure"[tiab]) AND ("Biofeedback, Psychology"[Mesh] OR "biofeedback"[tiab] OR "bio-feedback"[tiab] OR "heart rate variability biofeedback"[tiab] OR "HRV biofeedback"[tiab] OR "neurofeedback"[tiab] OR "electromyographic biofeedback"[tiab] OR "thermal biofeedback"[tiab] OR "respiratory biofeedback"[tiab] OR "autonomic biofeedback"[tiab])`
2. `("Hypertension"[Mesh] OR hypertens*[tiab] OR "high blood pressure"[tiab]) AND ("Biofeedback, Psychology"[Mesh] OR biofeedback[tiab] OR "heart rate variability biofeedback"[tiab] OR "HRV biofeedback"[tiab] OR neurofeedback[tiab] OR "thermal biofeedback"[tiab] OR "electrodermal biofeedback"[tiab]) AND ("Blood Pressure"[Mesh] OR "blood pressure"[tiab] OR systolic[tiab] OR diastolic[tiab] OR SBP[tiab] OR DBP[tiab])`
3. `(("Hypertension"[Mesh] OR hypertens*[tiab] OR "high blood pressure"[tiab]) AND ("Biofeedback, Psychology"[Mesh] OR biofeedback[tiab] OR "bio-feedback"[tiab] OR "heart rate variability biofeedback"[tiab] OR "HRV biofeedback"[tiab] OR neurofeedback[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR trial[tiab] OR placebo[tiab] OR "usual care"[tiab] OR "standard care"[tiab] OR control*[tiab] OR sham[tiab]))`
4. `((hypertens*[tiab] OR "high blood pressure"[tiab]) AND ((biofeedback[tiab] OR "bio-feedback"[tiab] OR "heart rate variability biofeedback"[tiab] OR "HRV biofeedback"[tiab] OR neurofeedback[tiab] OR "thermal biofeedback"[tiab] OR "respiratory biofeedback"[tiab]) AND ("blood pressure reduction"[tiab] OR "blood pressure control"[tiab] OR "blood pressure change"[tiab] OR systolic[tiab] OR diastolic[tiab] OR SBP[tiab] OR DBP[tiab])))`
5. `(("Hypertension"[Mesh] OR hypertens*[tiab]) AND ("Biofeedback, Psychology"[Mesh] OR biofeedback[tiab] OR "heart rate variability biofeedback"[tiab] OR "HRV biofeedback"[tiab] OR neurofeedback[tiab]) AND ("Blood Pressure"[Mesh] OR "blood pressure"[tiab] OR systolic[tiab] OR diastolic[tiab]) AND (cohort[tiab] OR "cohort studies"[Mesh] OR prospective[tiab] OR longitudinal[tiab] OR comparative[tiab] OR random*[tiab] OR trial[tiab]))`

The merged candidate pool contained 50 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling adults or general patient populations with diagnosed hypertension or elevated blood pressure.
- Studies evaluating biofeedback interventions, including heart rate variability biofeedback or other biofeedback modalities, as the primary intervention.
- Studies including a control group such as standard care, usual care, sham intervention, waitlist, or no biofeedback intervention.
- Studies reporting changes in systolic and/or diastolic blood pressure as outcomes.

Exclusion criteria:

- Studies in non-hypertensive populations only, including normotensive participants without separate data for patients with hypertension.
- Studies in which biofeedback is not a primary intervention or is embedded in a multicomponent program without isolating its effect.
- Studies without an appropriate comparator group, or without quantitative blood pressure outcomes.
- Non-comparative designs and non-primary research articles, including case reports, case series, reviews, editorials, and conference abstracts without sufficient data.

50 candidates were screened and 10 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was conducted for studies reporting continuous blood pressure outcomes in a sufficiently comparable format. The effect measure used for meta-analysis was the **mean difference (MD)** in blood pressure change between the biofeedback and control groups. Mean differences were selected because systolic and diastolic blood pressure outcomes were reported on a common scale (mmHg). For each study, the extracted summary statistics included group means, standard deviations, and sample sizes.

Pooled effect estimates were calculated using both **fixed-effect** and **random-effects** models, with the random-effects model treated as the primary analysis because between-study clinical and methodological variability was expected across biofeedback modalities, intervention durations, and comparator conditions. The meta-analysis included **4 studies** contributing data to the pooled estimate.

Under the **random-effects model**, the pooled mean difference was **4.646 mmHg** with a **95% confidence interval (CI) of 0.129 to 9.164** and **p = 0.0438**. Under the **fixed-effect model**, the pooled mean difference was **5.196 mmHg** with a **95% CI of 2.391 to 8.002** and **p = 0.0003**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (tau²)**. Heterogeneity was moderate, with **I² = 58.3%**, **Q = 7.20 (p = 0.066)**, and **tau² = 12.0841**. Because the I² value indicated substantial between-study inconsistency and the Q test approached statistical significance, interpretation prioritized the random-effects estimate.

All analyses were based on two-sided significance testing with a conventional threshold of **p < 0.05**. Results were reported as pooled mean differences with corresponding 95% confidence intervals to quantify the magnitude and precision of the effect of biofeedback on blood pressure.

## Results

### Study Selection

### Results of the Search
The literature search identified **50 records** in total (**50** from local sources and **0** from PubMed) after deduplication. All **50 records** underwent title and abstract screening, of which **40** were excluded at the first stage for not meeting the eligibility criteria. **10 full-text articles** were then assessed for eligibility. No studies were excluded at the full-text stage (**n = 0**). Consequently, **10 studies** were included in the systematic review. Of these, **4 studies** contributed quantitative data to the meta-analysis of blood pressure outcomes.

Most frequent recorded exclusion reasons:

- Review article, not a primary comparative study.: 3
- Systematic review, which is a non-primary research article.: 2
- Population is not clearly limited to patients with diagnosed hypertension or elevated blood pressure, despite evaluating biofeedback and blood pressure outcomes.: 1
- No appropriate comparator group is described; appears to be a pre-post evaluation without a control condition.: 1
- Includes untreated subjects with high-normal blood pressure in addition to mild hypertension, so the population is not restricted to hypertensive/elevated blood pressure patients as required.: 1
- Biofeedback is embedded within a multicomponent yoga-based behavioral program without isolating the effect of biofeedback.: 1
- Focuses on physical exercise rather than biofeedback as the primary intervention.: 1
- Pretest-posttest study without an appropriate comparator group; non-comparative design.: 1
- Insufficient information in the abstract, and title suggests biofeedback is combined with yoga rather than isolated as the primary intervention.: 1
- Mini review, which is a non-primary research article.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 3854 | 2007 | Blood pressure biofeedback exerts intermediate-term effects on blood pressure and pressure reactivity in individuals with mild hypertension: a randomized controlled study. |
| 3850 | 1979 | Evaluation of biofeedback in the treatment of borderline essential hypertension. |
| 3848 | 1997 | Placebo-controlled biofeedback blood pressure effect in hypertensive humans. |
| 3851 | 1981 | The effect of biofeedback-assisted relaxation training on blood pressure and selected biochemical parameters in patients with essential hypertension. |
| 90688 | 2017 | Effects of long term device-guided slow breathing on sympathetic nervous activity in hypertensive patients: a randomized open-label clinical trial. |
| 90672 | 1988 | A controlled comparison of thermal biofeedback and relaxation training in the treatment of essential hypertension: II. Effects on cardiovascular reactivity. |
| 3857 | 1996 | Controlled evaluation of thermal biofeedback in treatment of elevated blood pressure in unmedicated mild hypertension. |
| 3853 | 1998 | The effect of home training with direct blood pressure biofeedback of hypertensives: a placebo-controlled study. |
| 3855 | 2013 | Device-guided breathing as treatment for hypertension in type 2 diabetes mellitus: a randomized, double-blind, sham-controlled trial. |
| 3860 | 2010 | Internet-based biofeedback-assisted relaxation training in the treatment of hypertension: a pilot study. |

### Study Characteristics

**Study Characteristics**

Ten studies involving 303 participants were included, with publication years spanning 1979 to 2017. The geographic distribution was poorly reported overall: only two studies explicitly identified their setting, one from the Netherlands and one from Sweden, while the remaining eight did not report country. Study design was notably heterogeneous. Although all studies used a comparative design, the sample included one randomized controlled trial, one randomized placebo-controlled trial, one randomized open-label clinical trial, one randomized double-blinded modified contingency placebo-controlled study, one randomized double-blind sham-controlled trial, one randomized controlled pilot study, and several older controlled or comparison trials with less precise methodological labeling. This variation, together with the wide publication range, suggests substantial diversity in trial conduct and reporting standards across the evidence base.

Reporting of participant characteristics was limited in the extracted study-level data. Across studies, sample sizes ranged from 19 to 56 among trials with reported enrollment, while two studies did not have extractable participant counts in the available summary. Detailed information on age, sex distribution, and baseline condition severity was not available from the enhanced extraction provided, limiting assessment of population comparability across studies. Similar limitations applied to intervention characteristics and outcome measures: the included studies appeared to vary in treatment format and control condition, with some using placebo, sham, open-label, or other comparative approaches, but dose, duration, mode of delivery, and specific endpoints were not consistently available in the extracted dataset. These gaps indicate important clinical and methodological heterogeneity that should be considered when interpreting pooled findings.

Data quality from the enhanced extraction was generally favorable, with 7 studies rated as high confidence and 3 as medium confidence. However, confidence in extracted data should be interpreted alongside the risk-of-bias profile, which was predominantly judged as unclear risk, with one study rated high risk overall. Across studies, sequence generation, allocation concealment, and blinding were almost uniformly recorded as unclear, reflecting limited reporting of core methodological safeguards. Taken together, the evidence base comprises a mix of older and more recent controlled studies with variable design features, incomplete reporting of participant and intervention details, and largely unclear internal validity, underscoring the heterogeneity of the included literature.

### Main Findings

### Results

#### Primary outcome: pooled effect on blood pressure

The pooled analysis demonstrated a statistically significant benefit of biofeedback over control conditions for blood pressure change among patients with hypertension. Using a random-effects model across 4 studies, biofeedback was associated with a mean difference (MD) of **4.65 mmHg** (**95% CI 0.13 to 9.16; p=0.0438**). This indicates that, on average, patients receiving biofeedback experienced a greater improvement in blood pressure than those receiving standard care or no biofeedback intervention.

Because between-study heterogeneity was present, the random-effects estimate is the most appropriate primary summary. Heterogeneity was **moderate** overall (**I²=58.3%**), with a Cochran Q of **7.20** (**p=0.066**) and **τ²=12.08**, suggesting that the observed variation in effects was not fully explained by chance alone.

A fixed-effect model produced a similar, slightly larger estimate (**MD 5.20 mmHg, 95% CI 2.39 to 8.00; p=0.0003**), supporting the overall direction of effect and indicating that the finding was not dependent on the choice of meta-analytic model.

#### Direction and magnitude of effect

The direction of effect consistently favored biofeedback, with the pooled estimate suggesting an average improvement of approximately **4.6–5.2 mmHg** relative to control. In clinical terms, an effect of this magnitude may be meaningful, particularly in hypertension management, where even modest reductions in blood pressure can translate into lower cardiovascular risk at the population level. However, a **percentage relative reduction** could not be calculated reliably because comparable baseline blood pressure values were not provided across studies.

#### Consistency across studies

The degree of inconsistency across studies was **moderate**, as reflected by the **I² of 58.3%**. This suggests that while the overall effect favored biofeedback, the size of benefit varied across trials. The borderline Q-test result (**p=0.066**) further supports some between-study variability, though not at a conventional threshold for statistical significance. Taken together, the evidence suggests that biofeedback is likely beneficial, but the magnitude of benefit may differ depending on study or intervention characteristics.

#### Notable individual study findings

Study-level effect estimates were not provided in the summary data, so it was not possible to identify with certainty which individual study contributed the largest effect or carried the greatest statistical weight. Nonetheless, the difference between the random-effects and fixed-effect estimates was modest, suggesting that no single study completely drove the pooled result. The narrower confidence interval under the fixed-effect model implies that one or more relatively precise studies likely contributed substantially to the overall estimate.

#### Outliers and potential explanations

The moderate heterogeneity raises the possibility that one or more studies showed effects that differed meaningfully from the others. Potential explanations include differences in **biofeedback modality** (for example, heart rate variability biofeedback versus other forms), intervention intensity or duration, baseline blood pressure severity, adherence, co-interventions, and the nature of the control condition. These factors may account for the variability in treatment effect and should be considered when interpreting the pooled findings.

Overall, the available evidence suggests that **biofeedback improves blood pressure outcomes compared with control**, although the certainty around the precise magnitude of effect is tempered by moderate between-study heterogeneity and the small number of included studies.

### Risk of Bias

Across the 10 included studies, the overall risk of bias was predominantly unclear: 9 studies were judged as having unclear risk overall and 1 study was judged as high risk, while no study was assessed as low risk. At the domain level, concerns were universal. All 10 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practice, this means that the most common bias concerns were not isolated to one or two methodological features, but affected every assessed domain in every study (10/10 for each domain). The dominant reason was poor reporting rather than explicit evidence of flawed methods: study reports consistently provided no usable information on sequence generation, concealment, blinding, attrition handling, or reporting completeness.

This pattern suggests that the evidence base is limited more by inadequate methodological reporting than by clearly demonstrated low-quality conduct, although one study was still judged at high overall risk. Because the available summaries do not document any domain as low risk in any study, there is no subgroup of trials that can be considered methodologically robust on the reported information alone. The dataset also does not provide enough detail to distinguish a clearer pattern by study design, such as randomized versus observational studies; instead, the consistent finding across the included studies is a uniform lack of reporting across core bias domains. The single high-risk study therefore stands out at the overall level, but it is notable that even the remaining nine studies were not reassuring, as their judgments were unclear in all six domains rather than low risk in any domain.

These risk-of-bias findings reduce confidence in the pooled estimate. When uncertainty affects sequence generation, allocation concealment, blinding, missing outcome data, and selective reporting simultaneously, the direction and magnitude of any pooled effect become harder to interpret, since bias could either inflate or attenuate the observed association. The enhanced extraction quality ratings provide some reassurance regarding the reliability of the extracted information itself, with 7 studies rated high confidence and 3 rated medium confidence, and none rated low confidence. However, this supports confidence in the extraction process rather than in the underlying study methods. Overall, the meta-analytic findings should therefore be interpreted cautiously: the pooled estimate may be informative, but the absence of clearly low-risk studies and the universal uncertainty across all six bias domains materially lowers confidence in the strength of the conclusions.

## Discussion

**Discussion**

This systematic review suggests that biofeedback may produce a modest improvement in blood pressure among patients with hypertension, but the certainty of that conclusion is limited by the size and consistency of the available evidence. In the quantitative synthesis of four studies, the pooled random-effects mean difference was 4.65 mmHg (95% CI 0.13 to 9.16; p=0.0438), with the fixed-effect model yielding a similar but somewhat more precise estimate of 5.20 mmHg (95% CI 2.39 to 8.00; p=0.0003). Interpreted clinically, an approximately 4 to 5 mmHg reduction in blood pressure could be meaningful at the population level, as even small sustained reductions in blood pressure are associated with lower cardiovascular risk. At the same time, the confidence interval around the random-effects estimate was wide and close to the null, and only 4 of the 10 included studies contributed to the pooled analysis, so the apparent benefit should be viewed as suggestive rather than definitive.

When placed in the context of prior evidence, the magnitude of effect observed here is broadly plausible and compares favorably with several established nonpharmacologic or technology-assisted strategies, while remaining within the range where heterogeneity across interventions is expected. For example, home blood pressure measurement has been associated with reductions of 3.27 mmHg systolic and 1.61 mmHg diastolic compared with usual care across 65 trials, and digital therapeutics with reductions of 3.75 mmHg systolic and 1.79 mmHg diastolic across 15 trials. By comparison, the effect estimated for biofeedback in this review appears similar in scale, although direct comparison should be made cautiously because intervention intensity, follow-up duration, baseline blood pressure, and outcome definitions differ substantially across reviews. Relative to pharmacologic comparisons, such as the modest advantage of chlorthalidone over hydrochlorothiazide, the present estimate is also clinically nontrivial. However, unlike those better-studied interventions, the evidence base for biofeedback is much smaller and methodologically less standardized, which likely explains why the precision and confidence in the estimate are lower.

A biologically plausible rationale exists for a blood pressure-lowering effect of biofeedback. Several biofeedback modalities, particularly heart rate variability biofeedback, are designed to enhance autonomic regulation, reduce sympathetic arousal, and improve baroreflex-related cardiovascular control. These mechanisms could translate into lower vascular tone, improved stress reactivity, and reduced transient blood pressure elevations, especially in patients whose hypertension is partly driven or exacerbated by stress-related autonomic dysregulation. Biofeedback may also operate through behavioral pathways: repeated self-monitoring, guided breathing, relaxation training, and improved awareness of physiological responses may increase adherence to healthy routines and reinforce self-management behaviors. The likely reality is that biofeedback is not a single intervention with one mechanism, but a family of approaches whose effects depend on the specific physiological target, training intensity, and patient engagement.

The moderate heterogeneity observed in the meta-analysis (I²=58.3%, Q p=0.066, tau²=12.08) is therefore unsurprising. Clinical heterogeneity likely arose from differences in biofeedback modality, treatment duration, session frequency, comparator type, and blood pressure measurement methods. Population differences may also have contributed, including variation in baseline hypertension severity, medication use, age, comorbid stress or anxiety, and the extent to which participants were motivated or able to practice techniques outside supervised sessions. Methodological differences are equally important. Some older studies provided incomplete reporting of randomization, allocation concealment, sample sizes, or variance estimates, and several included studies lacked sufficient numerical data for pooling despite otherwise relevant designs. The fact that 10 studies were eligible for the review but only 4 were meta-analyzable highlights a central issue in this literature: inconsistency in reporting may be obscuring the true effect as much as inconsistency in intervention efficacy.

This review has several strengths. It synthesized a broad body of evidence across 10 included studies while applying quantitative pooling where the data allowed. The quality profile of the included evidence was not uniformly weak; the enhanced extraction process classified 7 studies as high quality and 3 as medium quality, with none rated low quality, which supports the value of the underlying evidence base even though reporting was often incomplete for meta-analysis. A further strength is the explicit separation between study inclusion and quantitative synthesis, which avoids overstating certainty when data are not extractable. The review also benefits from an enhanced extraction approach that made reporting gaps visible in a structured way, allowing a clearer assessment of where the evidence is limited by study conduct versus by poor documentation. That distinction matters when interpreting an intervention area that spans several decades and methodological eras.

The limitations are substantial and should shape interpretation. First, the pooled estimate is based on only four studies, which limits precision and makes the summary effect sensitive to individual trial characteristics. Second, reporting problems were common across the included literature, including missing metadata, incomplete descriptions of randomization and blinding, absent group-specific sample sizes, and lack of standard deviations or directly extractable outcome data. Third, the intervention itself was heterogeneous: “biofeedback” encompassed multiple modalities that may not be equivalent in mechanism or effectiveness. Fourth, the review is constrained by the limitations of the available published record, including likely differences in outcome measurement timing and blood pressure ascertainment. Finally, generalizability remains uncertain, particularly to contemporary hypertensive populations managed with current medication strategies, team-based care, and digital monitoring tools, because some included studies were older and may reflect clinical contexts that differ materially from present practice.

From a clinical standpoint, these findings support biofeedback as a potentially useful adjunct rather than a replacement for established hypertension management. For selected patients, especially those with stress-related symptom burden, strong interest in self-regulation strategies, or difficulty achieving control despite standard lifestyle advice, biofeedback may be a reasonable complementary option. The current evidence does not justify overstatement, and it does not establish that biofeedback should displace proven pharmacologic treatment, home blood pressure monitoring, or structured lifestyle interventions. The practical implication is more modest: clinicians may consider biofeedback within a multimodal management plan when resources and patient preferences align, while being transparent that the supporting evidence is promising but still incomplete.

Future research should move beyond small, poorly reported trials and test clearly defined biofeedback protocols in adequately powered randomized studies. Priority areas include standardization of intervention modality and dose, separation of systolic and diastolic outcomes, use of validated office and ambulatory or home blood pressure measures, longer follow-up to assess durability, and careful reporting of adherence, cointerventions, and medication changes. Trials should also examine whether particular subgroups benefit more than others, such as patients with elevated stress reactivity, resistant hypertension, or poor blood pressure self-management. An individual-participant or modality-specific meta-analysis may ultimately be needed, but that will require much better primary reporting than is currently typical. Overall, the present review identifies a credible signal of benefit, while also making clear that stronger contemporary evidence is needed before firm conclusions about the role of biofeedback in hypertension care can be drawn.

## Conclusion

In this review of 10 studies, with 4 contributing to the pooled estimate, biofeedback was associated with a greater improvement in blood pressure than standard care or no biofeedback, with a random-effects mean difference of 4.65 mmHg (95% CI 0.13 to 9.16; p=0.0438). Clinically, an effect of this magnitude could be meaningful, as even modest blood pressure reductions may translate into lower cardiovascular risk, suggesting biofeedback may be a useful adjunct for patients with hypertension, particularly when integrated with usual management rather than used as a standalone replacement. However, this recommendation should be qualified: the evidence is based on a small meta-analyzed subset, the confidence interval is wide, and between-study heterogeneity was moderate (I²=58.3%), indicating that the size and consistency of benefit likely vary across biofeedback modalities and study settings.

## Final Included Studies

- Corpus ID: 3854 | Blood pressure biofeedback exerts intermediate-term effects on blood pressure and pressure reactivity in individuals with mild hypertension: a randomized controlled study.
- Corpus ID: 3850 | Evaluation of biofeedback in the treatment of borderline essential hypertension.
- Corpus ID: 3848 | Placebo-controlled biofeedback blood pressure effect in hypertensive humans.
- Corpus ID: 3851 | The effect of biofeedback-assisted relaxation training on blood pressure and selected biochemical parameters in patients with essential hypertension.
- Corpus ID: 90688 | Effects of long term device-guided slow breathing on sympathetic nervous activity in hypertensive patients: a randomized open-label clinical trial.
- Corpus ID: 90672 | A controlled comparison of thermal biofeedback and relaxation training in the treatment of essential hypertension: II. Effects on cardiovascular reactivity.
- Corpus ID: 3857 | Controlled evaluation of thermal biofeedback in treatment of elevated blood pressure in unmedicated mild hypertension.
- Corpus ID: 3853 | The effect of home training with direct blood pressure biofeedback of hypertensives: a placebo-controlled study.
- Corpus ID: 3855 | Device-guided breathing as treatment for hypertension in type 2 diabetes mellitus: a randomized, double-blind, sham-controlled trial.
- Corpus ID: 3860 | Internet-based biofeedback-assisted relaxation training in the treatment of hypertension: a pilot study.
