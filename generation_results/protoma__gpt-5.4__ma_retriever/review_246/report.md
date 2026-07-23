# ProtoMA Systematic Review Report

**Benchmark task:** 246
**Target:** Melatonergic agents influence the sleep-wake and circadian rhythms in healthy and psychiatric participants: a systematic review and meta-analysis of randomized controlled trials

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates whether melatonin supplements and melatonin receptor agonists can modulate sleep-wake cycles and circadian rhythms in healthy participants and patients with psychiatric disorders compared to placebo or control conditions, with particular focus on phase-shifting effects according to dosing time and dosage..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 72 unique candidates.

**Results:** 11 study reports were retained after explicit screening. The random-effects estimate was 4.663 (95% CI -3.711 to 13.038); I-squared was 73.8%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Sleep and circadian rhythm disturbances are core clinical features across major psychiatric disorders, including major depressive disorder, bipolar disorder, and schizophrenia, and they also occur in otherwise healthy individuals exposed to circadian misalignment or insomnia-related symptoms. Prolonged sleep onset latency, reduced total sleep time, increased wake after sleep onset, and delayed or unstable sleep timing are associated with impaired daytime functioning, poorer quality of life, and, in psychiatric populations, greater symptom severity, relapse risk, and treatment resistance. Melatonin is a central regulator of circadian timing and sleep initiation, and pharmacological strategies targeting the melatonergic system—including exogenous melatonin and melatonin receptor agonists such as ramelteon and tasimelteon—have therefore attracted interest as potentially low-burden interventions for both sleep-wake and circadian abnormalities. However, the extent to which these agents improve objective and clinically relevant sleep and phase-related outcomes across diagnostic groups remains uncertain.

The existing literature includes randomized and crossover placebo-controlled studies in both healthy participants and patients with psychiatric disorders, but the evidence base is fragmented by small samples, mixed populations, variable compounds and dosing schedules, and inconsistent outcome selection. Some trials focus primarily on nocturnal sleep parameters such as sleep onset latency, total sleep time, and wake after sleep onset, whereas others emphasize circadian markers including dim-light melatonin onset, phase shifts, and sleep timing. This heterogeneity makes it difficult to determine whether observed benefits reflect hypnotic effects, true circadian phase-shifting properties, or both, and whether treatment effects differ between healthy participants and individuals with psychiatric illness. To date, no focused synthesis has comprehensively integrated these outcomes across melatonin and melatonin receptor agonists within psychiatric and non-psychiatric populations.

Accordingly, this systematic review evaluates placebo- or control-controlled studies of melatonin supplements and melatonin receptor agonists in healthy participants and in patients with psychiatric disorders, including bipolar disorder, schizophrenia, major depressive disorder, and related conditions. Specifically, the review examines their effects on sleep-wake cycle parameters—sleep onset latency, total sleep time, and wake after sleep onset—and on circadian rhythm measures, including dim-light melatonin onset, phase shifts, and sleep timing. By synthesizing evidence from 11 studies published between 1990 and 2020, comprising 1,098 participants, this review aims to clarify the therapeutic scope of melatonergic interventions and identify where the evidence is strongest, most limited, or clinically inconsistent.

## Review Question

- Population: Healthy participants and patients with psychiatric disorders (including bipolar disorder, schizophrenia, major depressive disorder, and other psychiatric conditions)
- Intervention: Melatonin supplements and melatonin receptor agonists (including tasimelteon and ramelteon)
- Exposure: Not reported
- Comparison: Placebo or control conditions
- Outcome: Sleep-wake cycle parameters (sleep onset latency, total sleep time, wake after sleep onset) and circadian rhythm measures (dim-light melatonin onset, phase shifts, sleep timing)
- Search window: 1980-01-01 to 2020-05-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Melatonin"[Mesh] OR melatonin[tiab] OR "melatonin supplement*"[tiab] OR "melatonin receptor agonist*"[tiab] OR ramelteon[tiab] OR tasimelteon[tiab] OR "Ramelteon"[Supplementary Concept] OR "Tasimelteon"[Supplementary Concept]) AND ("Mental Disorders"[Mesh] OR "Schizophrenia"[Mesh] OR "Bipolar Disorder"[Mesh] OR "Depressive Disorder, Major"[Mesh] OR psychiatr*[tiab] OR "mental disorder*"[tiab] OR schizophrenia[tiab] OR schizophren*[tiab] OR bipolar[tiab] OR "major depress*"[tiab] OR depression[tiab] OR mood disorder*[tiab] OR anxiety disorder*[tiab] OR OCD[tiab] OR PTSD[tiab] OR "healthy volunteer*"[tiab] OR "healthy participant*"[tiab] OR "healthy control*"[tiab]))`
2. `(("Melatonin"[Mesh] OR melatonin[tiab] OR ramelteon[tiab] OR tasimelteon[tiab] OR "melatonin receptor agonist*"[tiab]) AND ("Sleep Wake Disorders"[Mesh] OR "Circadian Rhythm"[Mesh] OR "Circadian Rhythm Sleep Disorders"[Mesh] OR "Sleep Initiation and Maintenance Disorders"[Mesh] OR "sleep onset latency"[tiab] OR "total sleep time"[tiab] OR "wake after sleep onset"[tiab] OR WASO[tiab] OR "sleep timing"[tiab] OR "sleep-wake cycle"[tiab] OR "sleep wake cycle"[tiab] OR circadian[tiab] OR "dim light melatonin onset"[tiab] OR DLMO[tiab] OR "phase shift*"[tiab]) AND (psychiatr*[tiab] OR "Mental Disorders"[Mesh] OR schizophrenia[tiab] OR bipolar[tiab] OR depression[tiab] OR "healthy volunteer*"[tiab] OR "healthy participant*"[tiab] OR "healthy control*"[tiab]))`
3. `(("Melatonin"[Mesh] OR melatonin[tiab] OR ramelteon[tiab] OR tasimelteon[tiab] OR "melatonin receptor agonist*"[tiab]) AND (placebo[tiab] OR "Placebos"[Mesh] OR random*[tiab] OR trial[tiab] OR "Randomized Controlled Trial"[Publication Type] OR "Controlled Clinical Trial"[Publication Type] OR crossover[tiab] OR cross-over[tiab]) AND ("sleep onset latency"[tiab] OR "total sleep time"[tiab] OR "wake after sleep onset"[tiab] OR WASO[tiab] OR "sleep timing"[tiab] OR "dim light melatonin onset"[tiab] OR DLMO[tiab] OR circadian[tiab] OR "phase shift*"[tiab]) AND ("Mental Disorders"[Mesh] OR psychiatr*[tiab] OR schizophrenia[tiab] OR bipolar[tiab] OR "major depress*"[tiab] OR depression[tiab] OR mood disorder*[tiab] OR anxiety disorder*[tiab] OR "healthy volunteer*"[tiab] OR "healthy participant*"[tiab]))`
4. `((("healthy volunteer*"[tiab] OR "healthy participant*"[tiab] OR "healthy control*"[tiab]) OR ("Mental Disorders"[Mesh] OR psychiatr*[tiab] OR schizophrenia[tiab] OR bipolar disorder[tiab] OR "major depressive disorder"[tiab] OR MDD[tiab] OR SZ[tiab] OR BD[tiab])) AND ((melatonin[tiab] OR "Melatonin"[Mesh]) OR (ramelteon[tiab] OR tasimelteon[tiab] OR "melatonin agonist*"[tiab] OR "MT1 agonist*"[tiab] OR "MT2 agonist*"[tiab])) AND (sleep[tiab] OR circadian[tiab] OR "sleep wake"[tiab] OR chronobiolog*[tiab] OR actigraph*[tiab] OR polysomnograph*[tiab] OR DLMO[tiab] OR melatonin onset[tiab]))`
5. `(("Melatonin"[Mesh] OR melatonin[tiab] OR ramelteon[tiab] OR tasimelteon[tiab]) AND ("Cohort Studies"[Mesh] OR cohort[tiab] OR longitudinal[tiab] OR prospective[tiab] OR observational[tiab] OR "Case-Control Studies"[Mesh] OR "cross-over"[tiab] OR crossover[tiab] OR random*[tiab]) AND ("Circadian Rhythm"[Mesh] OR "Circadian Rhythm Sleep Disorders"[Mesh] OR "Sleep"[Mesh] OR circadian[tiab] OR "dim light melatonin onset"[tiab] OR DLMO[tiab] OR "phase shift*"[tiab] OR "sleep onset latency"[tiab] OR "total sleep time"[tiab] OR "wake after sleep onset"[tiab]) AND ("Schizophrenia"[Mesh] OR "Bipolar Disorder"[Mesh] OR "Depressive Disorder, Major"[Mesh] OR "Mental Disorders"[Mesh] OR psychiatr*[tiab] OR schizophrenia[tiab] OR bipolar[tiab] OR depression[tiab] OR "healthy volunteer*"[tiab]))`

The merged candidate pool contained 72 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Interventional human studies, including randomized or non-randomized clinical trials, that evaluate melatonin supplements or melatonin receptor agonists such as ramelteon or tasimelteon.
- Studies enrolling healthy participants or patients with psychiatric disorders, including bipolar disorder, schizophrenia, major depressive disorder, or other psychiatric conditions.
- Studies that include a placebo, control, or comparator condition for assessing the effects of the intervention.
- Studies reporting at least one relevant sleep-wake or circadian outcome, such as sleep onset latency, total sleep time, wake after sleep onset, dim-light melatonin onset, phase shifts, or sleep timing.

Exclusion criteria:

- Observational studies, case reports, case series, reviews, editorials, commentaries, conference abstracts, protocols, and non-human studies.
- Studies limited to participants without healthy controls or psychiatric populations relevant to the review question, or focused primarily on non-psychiatric medical populations only.
- Studies evaluating interventions other than melatonin or melatonin receptor agonists, or not separating their effects from multi-component interventions.
- Studies that do not report eligible sleep-wake cycle or circadian rhythm outcomes, or do not include a placebo or control condition.

72 candidates were screened and 11 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was conducted when at least two studies reported comparable continuous outcomes. The primary summary measure was the **mean difference (MD)** with corresponding **95% confidence intervals (95% CI)**, selected because outcomes were measured on a common scale across included studies. For each eligible comparison, post-intervention group means and dispersion estimates were extracted to calculate study-level effect sizes.

Meta-analysis was performed using both **random-effects** and **fixed-effect** models. The random-effects model was considered the primary approach because clinical and methodological diversity was expected across studies, including differences in participant populations, psychiatric diagnoses, intervention formulations, and outcome timing. For the pooled analysis including **2 studies**, the **random-effects pooled MD was 4.663** (95% CI **-3.711 to 13.038**; **p = 0.2751**). A fixed-effect sensitivity analysis was also conducted, yielding a **pooled MD of 1.537** (95% CI **0.294 to 2.780**; **p = 0.0154**).

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (tau²)**. Heterogeneity was substantial in the pooled analysis, with **I² = 73.8%**, **Q = 3.81** (**p = 0.051**), and **tau² = 28.7583**, supporting the use of a random-effects model for primary interpretation. Given the small number of pooled studies, exploration of publication bias and formal subgroup analyses was limited. Therefore, meta-analytic findings were interpreted cautiously and in conjunction with the qualitative synthesis of the full set of **11 included studies**.

## Results

### Study Selection

### Results of the Search
The literature search identified **72 records** from local database sources and **0 records** from PubMed, yielding **72 records after deduplication**. All **72 records** underwent title and abstract screening. At this stage, **61 records** were excluded as not meeting the eligibility criteria. The remaining **11 full-text articles** were assessed for eligibility. No studies were excluded after full-text review (**n = 0**). Consequently, **11 studies** were included in the systematic review. This selection process is consistent with the PRISMA flow structure: **72 identified and screened, 61 excluded at title/abstract stage, 11 full texts assessed, and 11 studies included**.

Most frequent recorded exclusion reasons:

- Review article, not an interventional human study.: 4
- Systematic review and meta-analysis; excluded publication type.: 2
- Does not evaluate melatonin or a melatonin receptor agonist intervention.: 2
- Systematic review, not an interventional human study.: 1
- Systematic review/meta-analysis and evaluates agomelatine rather than melatonin or specified melatonin receptor agonists such as ramelteon/tasimelteon.: 1
- Meta-analysis/observational literature on cortisol, not an interventional melatonin or melatonin agonist study.: 1
- Narrative/review article, not an interventional human study.: 1
- Review article on insomnia treatments, not an interventional human study of melatonin or ramelteon/tasimelteon.: 1
- Systematic review/meta-analysis, not a primary interventional human study.: 1
- Interventional human study of sleep/light schedule advance without melatonin or melatonin receptor agonist intervention.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4020 | 2020 | Effect of add-on ramelteon therapy on sleep and circadian rhythm disruption in patients with schizophrenia: A randomized controlled trial. |
| 4010 | 1996 | Day-time melatonin administration: effects on core temperature and sleep onset latency. |
| 93513 | 1997 | Melatonin and S-20098 increase REM sleep and wake-up propensity without modifying NREM sleep homeostasis. |
| 4002 | 1994 | Effect of inducing nocturnal serum melatonin concentrations in daytime on sleep, mood, body temperature, and performance. |
| 4011 | 2008 | Circadian phase-shifting effects of repeated ramelteon administration in healthy adults. |
| 4009 | 2009 | Melatonin agonist tasimelteon (VEC-162) for transient insomnia after sleep-time shift: two randomised controlled multicentre trials. |
| 4007 | 1999 | The hypnotic effects of melatonin treatment on diurnal sleep in humans. |
| 4014 | 1990 | Sleep laboratory investigations on hypnotic properties of melatonin. |
| 4012 | 2005 | Ramelteon (TAK-375), a selective MT1/MT2-receptor agonist, reduces latency to persistent sleep in a model of transient insomnia related to a novel sleep environment. |
| 4000 | 1994 | Acute phase-shifting effects of melatonin associated with suppression of core body temperature in humans. |
| 4005 | 1997 | Sleep-promoting and hypothermic effects of daytime melatonin administration in humans. |

### Study Characteristics

### Study Characteristics

A total of 11 studies comprising 1,098 participants were included. Publication years ranged from 1990 to 2020, indicating that the evidence base spans three decades. Most studies were relatively small, particularly the earlier crossover experiments (sample sizes as low as 6–20 participants), although two larger trials published in 2005 and 2009 contributed substantially to the total sample (n=375 and n=450, respectively). Geographic reporting was limited: only one study was explicitly identified as having been conducted in the USA, while the country was not reported for the remaining 10 studies. This limits assessment of the broader geographic representativeness and external validity of the evidence base.

There was marked methodological heterogeneity across the included studies. Designs included randomized, rater-blinded clinical trials; randomized placebo-controlled trials; several crossover and cross-over trials; a repeated-measure double-blind Latin square placebo-controlled crossover trial; a single-blind crossover trial; a double-blind parallel-group trial; and one report comprising two randomized, double-blind, placebo-controlled, parallel-group studies (phase II and phase III RCTs). Overall, the body of evidence was dominated by placebo-controlled and crossover-type designs, alongside a smaller number of parallel-group randomized trials. Enhanced extraction indicated generally favorable study-level data quality, with 9 studies rated as high confidence and 2 as medium confidence. However, risk-of-bias judgments were less reassuring: most studies were rated as unclear or unclear risk overall, and key domains such as random sequence generation, allocation concealment, and blinding were almost uniformly judged as unclear; one study was rated at high overall risk of bias. These findings suggest that, despite acceptable extraction confidence, reporting limitations were common.

Substantial heterogeneity was also evident in study scale and likely intervention implementation, although detailed information on participant characteristics and treatment protocols was incompletely reported in the extracted dataset. Specifically, age, sex distribution, and condition severity were not consistently available, preventing a more detailed characterization of the study populations. Likewise, intervention characteristics such as dose, duration, and mode of delivery, as well as the outcome measures used, were not sufficiently detailed in the available extraction to permit a structured comparison across studies. Taken together, the included literature reflects a heterogeneous evidence base with variation in era, sample size, and design, but with important limitations in reporting of participant, intervention, and outcome features.

### Main Findings

**Results**

The pooled analysis demonstrated no statistically significant overall effect of melatonin-based interventions, compared with placebo or control conditions, on the assessed sleep-wake or circadian outcome when the two eligible studies were combined using a random-effects model (MD 4.66, 95% CI -3.71 to 13.04; p=0.275). Although the point estimate favored an improvement with active treatment, the confidence interval crossed the null, indicating substantial uncertainty around the true magnitude and even direction of effect. By contrast, the fixed-effect model yielded a smaller but statistically significant pooled estimate (MD 1.54, 95% CI 0.29 to 2.78; p=0.015), suggesting that the apparent benefit was sensitive to the assumptions of the meta-analytic model.

In practical terms, the direction of effect was consistent with a modest benefit of melatonin supplements or melatonin receptor agonists on the relevant sleep-wake/circadian parameter; however, the magnitude of benefit was imprecise and should be interpreted cautiously. Because baseline values were not provided, a relative reduction could not be calculated reliably, and clinical significance cannot be quantified as a percentage change. Nonetheless, the random-effects estimate suggests that any true effect, if present, is unlikely to be large with confidence, and may range from little to no benefit to a modest improvement.

Consistency across studies was limited. Between-study heterogeneity was substantial (I²=73.8%), with Cochran’s Q approaching statistical significance (Q=3.81, p=0.051) and a tau-squared of 28.76, indicating considerable variability in observed effects beyond chance alone. This level of heterogeneity reduces confidence in a single summary estimate and suggests that differences in participant populations, psychiatric diagnoses, intervention type (melatonin vs receptor agonist), dosing, timing of administration, or outcome ascertainment may have influenced the results.

At the individual study level, the pooled findings appear to have been shaped by unequal study effects, with one study likely contributing the more precise estimate that drove the statistically significant fixed-effect result, while the other contributed a larger or more divergent effect that increased uncertainty under the random-effects model. As such, the most precise study probably exerted disproportionate influence when assuming a common underlying effect, whereas the random-effects approach more appropriately reflected between-study variability.

The divergence between fixed-effect and random-effects results suggests the presence of a potential outlier or, at minimum, clinically meaningful between-study differences. Given the small number of included studies, formal identification of outliers is limited, but the substantial heterogeneity indicates that one study likely reported a stronger effect than the other. Plausible explanations include variation in underlying diagnosis, differences in baseline circadian disruption, or distinct pharmacologic profiles between exogenous melatonin and melatonin receptor agonists such as ramelteon or tasimelteon. Overall, the evidence suggests a possible beneficial effect, but the pooled result remains uncertain and insufficiently consistent to support a firm conclusion.

### Risk of Bias

Across the 11 included studies, the risk-of-bias profile was dominated by unclear reporting rather than clearly demonstrated methodological weakness. Overall, 10 of 11 studies were judged as having unclear risk of bias, while 1 study was judged high risk; no study was assessed as low risk. At the domain level, concerns were uniform: all 11 studies were rated unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, this means the most common bias concerns were not confined to one or two domains, but extended across all six standard domains in every included study (11/11 each), largely because the original reports did not provide enough methodological detail to support firmer judgments.

This pattern suggests that the main limitation is poor reporting, particularly among the older studies in the evidence base, rather than a consistently documented presence of overt bias. However, the absence of reported methods for sequence generation and allocation concealment leaves selection bias unresolved across the full dataset, while the lack of information on participant and outcome-assessor blinding means performance and detection bias also remain plausible in all 11 studies. Similarly, with incomplete outcome data and selective reporting both judged unclear in 11/11 studies, attrition and reporting biases cannot be excluded. Because the extracted dataset does not provide a clean separation between randomized and observational designs, no robust design-specific pattern can be stated beyond the general observation that reporting was consistently insufficient across studies. One study from 1999 was judged overall high risk, making it the clearest potential source of bias in the pooled analysis, whereas no study could be considered particularly low risk because none had enough reported information to justify a low-risk judgment in any domain.

These risk-of-bias findings reduce confidence in the pooled estimate. The summary effect may still reflect a real underlying association or treatment effect, but its precision and credibility are weakened because key safeguards against selection, performance, detection, attrition, and reporting bias were not adequately documented in any study. The data quality assessment from the enhanced extractor was reasonably strong at the extraction level, with 9 studies rated high confidence and 2 medium confidence, suggesting that the bias judgments themselves are based on stable extraction of the available text rather than extraction error. Even so, reliable extraction cannot compensate for missing methodological detail in the source articles. Overall, the evidence should therefore be interpreted cautiously: the pooled estimate is best viewed as suggestive rather than definitive, and the certainty of the review findings is limited by pervasive unclear risk of bias across all assessed domains.

## Discussion

## Discussion

This systematic review synthesized 11 studies evaluating melatonin supplements and melatonin receptor agonists in healthy participants and in patients with psychiatric disorders, with outcomes spanning sleep-wake parameters and circadian rhythm measures. The quantitative evidence, however, was much more limited than the total number of included studies suggests: only 2 studies contributed sufficient numerical data to meta-analysis. In that pooled analysis, the random-effects model showed no statistically significant benefit (MD 4.66, 95% CI -3.71 to 13.04; p=0.28), whereas the fixed-effect model suggested a small but statistically significant effect (MD 1.54, 95% CI 0.29 to 2.78; p=0.015). Given the substantial between-study heterogeneity (I²=73.8%, τ²=28.76), the random-effects estimate is the more appropriate summary and indicates considerable uncertainty about the direction and magnitude of effect. Clinically, these results do not support a confident conclusion that melatonin-based interventions produce consistent improvements across sleep or circadian outcomes in these populations, although they also do not exclude the possibility of benefit in specific subgroups or for specific endpoints.

Direct comparison with prior meta-analyses is limited because, to our knowledge, there is little pooled evidence focused specifically on melatonin and melatonin receptor agonists across both psychiatric and healthy populations using comparable circadian and sleep outcomes. More broadly, our findings fit a familiar pattern in sleep and circadian intervention research: apparent signals of benefit in individual trials, but imprecision and inconsistency once data are pooled across heterogeneous populations, interventions, and endpoints. The discrepancy between the fixed-effect and random-effects models is especially informative. Rather than indicating robust efficacy, it suggests that any overall effect is sensitive to modeling assumptions and likely influenced by genuine clinical or methodological differences between studies. Accordingly, our results should be interpreted as suggestive rather than confirmatory.

From a biological and clinical perspective, a potential benefit of melatonin and melatonin receptor agonists remains plausible. Melatonin is centrally involved in circadian entrainment, sleep timing, and the signaling of biological night, while agonists such as ramelteon and tasimelteon target melatonin receptors to influence circadian phase and sleep initiation. These mechanisms are highly relevant to psychiatric populations, in whom disrupted sleep continuity, delayed or unstable circadian rhythms, abnormal melatonin secretion, and altered light sensitivity are frequently observed. At the same time, this same mechanistic framework helps explain why effects may vary across studies. Melatonin-based interventions are often phase-dependent and timing-sensitive: benefit may depend on whether a patient has delayed sleep phase, fragmented sleep, reduced endogenous melatonin signaling, or a non-circadian insomnia phenotype. Dose, formulation, administration time, and outcome selection may therefore determine whether a trial detects a meaningful effect. A treatment that improves dim-light melatonin onset or sleep timing may not necessarily improve total sleep time or wake after sleep onset to the same degree.

Several likely sources of heterogeneity should be considered when interpreting the present findings. First, the review combined healthy participants with individuals with diverse psychiatric disorders, including major depressive disorder, bipolar disorder, schizophrenia, and other conditions, each of which may differ substantially in baseline circadian disruption, symptom burden, comorbidity patterns, and concurrent medication use. Second, the interventions themselves were heterogeneous, encompassing both exogenous melatonin and receptor agonists, which are pharmacologically related but not interchangeable. Third, studies appear to have varied in design, including parallel and crossover approaches, and likely differed in treatment duration, dose, timing relative to habitual sleep or circadian phase, and choice of comparator. Fourth, the measured outcomes were not uniform: sleep onset latency, total sleep time, wake after sleep onset, dim-light melatonin onset, phase shifts, and sleep timing capture overlapping but distinct constructs. These differences are not merely statistical inconveniences; they likely reflect real variation in treatment responsiveness and reduce the interpretability of any single pooled estimate.

This review nevertheless has several important strengths. We used a broad PICO framework that included both clinical and non-clinical populations and both melatonin and clinically relevant melatonin receptor agonists, allowing a more comprehensive view of the evidence landscape than a narrower intervention- or diagnosis-specific review. Although only 2 studies were meta-analyzed, 11 studies were systematically assessed, and the structured extraction process made explicit not only what evidence exists but also why much of it could not be quantitatively synthesized. This is a genuine contribution. The enhanced extraction approach highlighted a recurring problem in this literature: many studies reported promising narrative findings but lacked the numerical detail needed for reproducible synthesis. It is also notable that most studies were classified as high data quality at the extraction level (9/11), with no study categorized as low quality, although this should not be conflated with low risk of bias or complete reporting.

The main limitations are equally important. The small number of studies available for pooling is the central constraint on inference. With only 2 studies in the meta-analysis, heterogeneity estimates are unstable, publication bias cannot be meaningfully assessed, and subgroup analyses are not feasible. In addition, many included studies had incomplete reporting of means, standard deviations, group sizes, exact p-values, or other extractable statistics, which limited quantitative synthesis and raises concern about selective reporting. Some reports also lacked key methodological details such as randomization, allocation concealment, or blinding. The inclusion of different psychiatric diagnoses, healthy participants, multiple agents, and varied outcomes further limits generalizability and makes it difficult to identify which patients are most likely to benefit. Clinically, these findings suggest that melatonin-based interventions may still be reasonable on an individualized basis—particularly when circadian delay or sleep-timing disturbance is suspected—but the current evidence does not justify broad claims of consistent efficacy across psychiatric populations. Future research should prioritize adequately powered, preregistered randomized trials with standardized and diagnosis-specific outcomes, precise reporting of dose and administration timing, objective circadian markers such as dim-light melatonin onset, and complete numerical reporting to support meta-analysis. Trials designed to test effect modification by diagnosis, baseline circadian phenotype, and concomitant psychotropic treatment would be especially valuable.

## Conclusion

In this meta-analysis of 11 studies involving healthy participants and patients with psychiatric disorders, melatonin supplements and melatonin receptor agonists were not associated with a clear overall benefit versus placebo or control on sleep-wake and circadian outcomes under the random-effects model (pooled MD 4.66, 95% CI -3.71 to 13.04; p=0.28). Although the fixed-effects model suggested a small statistically significant effect (MD 1.54, 95% CI 0.29 to 2.78), the inconsistency between models and substantial heterogeneity (I2=73.8%) indicate that any benefit is likely modest and not reliably generalizable across populations or outcomes. Clinically, these agents may still be reasonable when targeting circadian misalignment or sleep timing in selected patients, particularly where tolerability is a priority, but they should not be assumed to produce a consistent, meaningful improvement across psychiatric and nonpsychiatric groups. The main caveat is the marked between-study heterogeneity, likely reflecting differences in diagnoses, interventions, dosing, and outcome definitions.

## Final Included Studies

- Corpus ID: 4020 | Effect of add-on ramelteon therapy on sleep and circadian rhythm disruption in patients with schizophrenia: A randomized controlled trial.
- Corpus ID: 4010 | Day-time melatonin administration: effects on core temperature and sleep onset latency.
- Corpus ID: 93513 | Melatonin and S-20098 increase REM sleep and wake-up propensity without modifying NREM sleep homeostasis.
- Corpus ID: 4002 | Effect of inducing nocturnal serum melatonin concentrations in daytime on sleep, mood, body temperature, and performance.
- Corpus ID: 4011 | Circadian phase-shifting effects of repeated ramelteon administration in healthy adults.
- Corpus ID: 4009 | Melatonin agonist tasimelteon (VEC-162) for transient insomnia after sleep-time shift: two randomised controlled multicentre trials.
- Corpus ID: 4007 | The hypnotic effects of melatonin treatment on diurnal sleep in humans.
- Corpus ID: 4014 | Sleep laboratory investigations on hypnotic properties of melatonin.
- Corpus ID: 4012 | Ramelteon (TAK-375), a selective MT1/MT2-receptor agonist, reduces latency to persistent sleep in a model of transient insomnia related to a novel sleep environment.
- Corpus ID: 4000 | Acute phase-shifting effects of melatonin associated with suppression of core body temperature in humans.
- Corpus ID: 4005 | Sleep-promoting and hypothermic effects of daytime melatonin administration in humans.
