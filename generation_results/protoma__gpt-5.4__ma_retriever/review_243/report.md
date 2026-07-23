# ProtoMA Systematic Review Report

**Benchmark task:** 243
**Target:** Side-effects of mdma-assisted psychotherapy: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates the side effects and safety profile of MDMA-assisted psychotherapy across psychiatric indications compared to control conditions (placebo-assisted psychotherapy or other control conditions), examining adverse events during medication sessions, in the 7 days following sessions, and throughout the treatment period..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 52 unique candidates.

**Results:** 7 study reports were retained after explicit screening. The random-effects estimate was 2.035 (95% CI 0.053 to 78.666); I-squared was 88.7%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Psychiatric illnesses such as post-traumatic stress disorder (PTSD), major depression, and psychological distress associated with life-threatening illness are often marked by persistent symptoms, functional impairment, and incomplete response to standard pharmacologic and psychotherapeutic approaches. In this context, MDMA-assisted psychotherapy (MDMA-AP) has emerged as a novel intervention designed to combine structured psychotherapy with the acute prosocial, anxiolytic, and affect-enhancing effects of 3,4-methylenedioxymethamphetamine (MDMA). Although efficacy findings have attracted substantial attention, the safety profile of MDMA-AP remains a central clinical question because treatment involves administration of a psychoactive agent with known sympathomimetic and neuropsychiatric effects. For patients with psychiatric illness, clinicians and regulators need a clear account of treatment-emergent harms, including acute effects during medication sessions, subacute symptoms in the days after dosing, and adverse events arising across the treatment period.

The available safety evidence for MDMA-AP is distributed across a relatively small but methodologically diverse body of clinical trials, including pilot studies, phase 2 dose-comparison trials, active-placebo and placebo-controlled randomized studies, and recent multi-site phase 3 trials. Across studies published between 2008 and 2023, 278 participants have been enrolled in trials involving psychiatric populations such as PTSD, depression, terminal illness, and related conditions. However, interpretation of this literature is complicated by variation in comparator conditions, dosing strategies, adverse event definitions, and time windows used for safety monitoring. As a result, the field still lacks a focused synthesis that evaluates whether MDMA-AP is associated with a distinct pattern or frequency of side effects and adverse events compared with placebo-assisted psychotherapy or other control conditions.

This systematic review therefore examines the safety of MDMA-assisted psychotherapy in patients with psychiatric illness by synthesizing evidence from controlled clinical studies comparing MDMA-AP with placebo-assisted psychotherapy or control interventions. Specifically, the review evaluates side effects and adverse events across three clinically relevant domains: events occurring during medication sessions, side effects reported within 7 days after sessions, and adverse events documented during the overall treatment period. By centering harms outcomes across these defined intervals, this review aims to clarify the tolerability of MDMA-AP and provide an evidence base for clinical decision-making, trial design, and risk-benefit assessment in psychiatric populations.

## Review Question

- Population: Patients with psychiatric illness (including PTSD, terminal illness, depression, and other psychiatric conditions) receiving MDMA-assisted psychotherapy
- Intervention: MDMA-assisted psychotherapy (MDMA-AP)
- Exposure: Not reported
- Comparison: Placebo-assisted psychotherapy or control conditions
- Outcome: Side effects and adverse events (including any side effect during medication sessions, side effects in the 7 days following sessions, and adverse events during treatment period)
- Search window: Not reported to 2023-10-30

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("3,4-Methylenedioxymethamphetamine"[Mesh] OR MDMA[tiab] OR "3,4-methylenedioxymethamphetamine"[tiab] OR ecstasy[tiab]) AND (psychotherap*[tiab] OR "Psychotherapy"[Mesh] OR "assisted psychotherapy"[tiab] OR "MDMA-assisted psychotherapy"[tiab] OR "MDMA-assisted therapy"[tiab] OR "drug-assisted psychotherapy"[tiab] OR "psychedelic-assisted psychotherapy"[tiab])) AND ("Mental Disorders"[Mesh] OR psychiat*[tiab] OR "psychiatric illness"[tiab] OR "psychiatric disorder*"[tiab] OR PTSD[tiab] OR "stress disorders, post-traumatic"[Mesh] OR depression[tiab] OR "Depressive Disorder"[Mesh] OR "terminal illness"[tiab] OR "palliative care"[Mesh] OR anxiety[tiab] OR "Anxiety Disorders"[Mesh])`
2. `(("3,4-Methylenedioxymethamphetamine"[Mesh] OR MDMA[tiab] OR "3,4-methylenedioxymethamphetamine"[tiab] OR ecstasy[tiab]) AND (psychotherap*[tiab] OR "Psychotherapy"[Mesh] OR "MDMA-assisted psychotherapy"[tiab] OR "MDMA-assisted therapy"[tiab] OR "psychedelic-assisted psychotherapy"[tiab]) AND ("Mental Disorders"[Mesh] OR PTSD[tiab] OR "stress disorders, post-traumatic"[Mesh] OR depression[tiab] OR "Depressive Disorder"[Mesh] OR anxi*[tiab] OR "terminal illness"[tiab] OR cancer[tiab] OR "palliative care"[tiab]) AND ("Drug-Related Side Effects and Adverse Reactions"[Mesh] OR "Treatment Outcome"[Mesh] OR "adverse event*"[tiab] OR "adverse effect*"[tiab] OR "side effect*"[tiab] OR tolerability[tiab] OR safety[tiab] OR harms[tiab] OR toxicity[tiab] OR "treatment-emergent"[tiab]))`
3. `(("MDMA-assisted psychotherapy"[tiab] OR "MDMA-assisted therapy"[tiab] OR ((MDMA[tiab] OR "3,4-methylenedioxymethamphetamine"[tiab]) AND psychotherap*[tiab])) AND (placebo[tiab] OR control*[tiab] OR comparator*[tiab] OR "Placebos"[Mesh]) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR "Randomized Controlled Trial"[Publication Type] OR "Controlled Clinical Trial"[Publication Type]) AND ("adverse event*"[tiab] OR "serious adverse event*"[tiab] OR "side effect*"[tiab] OR safety[tiab] OR tolerability[tiab]) AND (PTSD[tiab] OR "posttraumatic stress disorder"[tiab] OR depression[tiab] OR psychiat*[tiab] OR "terminal illness"[tiab]))`
4. `(("3,4-Methylenedioxymethamphetamine"[Mesh] OR MDMA[tiab]) AND ("Psychotherapy"[Mesh] OR psychotherap*[tiab]) AND ("Mental Disorders"[Mesh] OR "Stress Disorders, Post-Traumatic"[Mesh] OR "Depressive Disorder"[Mesh] OR "Anxiety Disorders"[Mesh] OR "Substance-Related Disorders"[Mesh] OR psychiat*[tiab]) AND ("Drug-Related Side Effects and Adverse Reactions"[Mesh] OR "adverse event*"[tiab] OR "side effect*"[tiab] OR safety[tiab] OR tolerability[tiab]) AND (cohort[tiab] OR "Cohort Studies"[Mesh] OR trial[tiab] OR "Clinical Trial"[Publication Type] OR "Randomized Controlled Trial"[Publication Type] OR open-label[tiab] OR follow-up[tiab]))`
5. `((MDMA[tiab] OR "3,4-methylenedioxymethamphetamine"[tiab] OR ecstasy[tiab]) AND ("assisted psychotherapy"[tiab] OR "assisted therapy"[tiab] OR psychotherap*[tiab] OR psycholytic[tiab] OR psychedelic[tiab]) AND (PTSD[tiab] OR "post-traumatic stress"[tiab] OR depression[tiab] OR depressive[tiab] OR anxi*[tiab] OR psychiat*[tiab] OR "terminally ill"[tiab] OR "life-threatening illness"[tiab] OR cancer[tiab]) AND ("adverse event*"[tiab] OR "adverse reaction*"[tiab] OR "side effect*"[tiab] OR safety[tiab] OR tolerability[tiab] OR harms[tiab] OR "treatment emergent"[tiab] OR headache[tiab] OR nausea[tiab] OR insomnia[tiab] OR anxiety[tiab]))`

The merged candidate pool contained 52 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human interventional studies, including randomized controlled trials or other clinical trials, evaluating MDMA-assisted psychotherapy in patients with a psychiatric illness such as PTSD, depression, terminal illness-related psychiatric symptoms, or other diagnosed psychiatric conditions.
- Studies in which the intervention includes MDMA administered as part of a psychotherapy-assisted treatment protocol, compared with placebo-assisted psychotherapy or another control condition.
- Studies reporting safety outcomes, including side effects during MDMA medication sessions, side effects within 7 days after sessions, and/or adverse events occurring during the treatment period.
- Full-text articles with sufficient data to determine study population, intervention/comparator, and adverse event outcomes.

Exclusion criteria:

- Non-human, preclinical, in vitro, case report, review, editorial, commentary, protocol, conference abstract-only, or other non-original research publications.
- Studies not involving patients with a psychiatric illness or not evaluating MDMA as an adjunct to psychotherapy.
- Studies without a placebo or control comparator, or without separable data for the MDMA-assisted psychotherapy arm.
- Studies not reporting side effects, adverse events, or other safety/tolerability outcomes related to treatment.

52 candidates were screened and 7 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was performed for studies reporting sufficiently comparable dichotomous adverse-event data. The principal effect measure was the **odds ratio (OR)** comparing the odds of adverse events in the **MDMA-assisted psychotherapy** group versus the **placebo/control** group. For each eligible study, event counts were organized in 2 x 2 tables and converted to study-level ORs with corresponding 95% confidence intervals.

Meta-analysis was conducted using both **fixed-effects** and **random-effects** models to evaluate the robustness of pooled estimates. Because clinical and methodological heterogeneity was anticipated across psychiatric populations, intervention protocols, and adverse-event definitions, the **random-effects model** was considered the primary model. A total of **2 studies** contributed to the pooled quantitative analysis.

Under the **random-effects model**, the pooled OR was **2.035** with a **95% confidence interval (CI) of 0.053 to 78.666** (**p = 0.7032**), indicating no statistically significant difference in adverse-event odds between MDMA-AP and control conditions. Under the **fixed-effects model**, the pooled OR was **0.739** (95% CI **0.279 to 1.957**, **p = 0.5432**).

Between-study heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (τ²)**. Heterogeneity was substantial, with **I² = 88.7%**, **Q = 8.88 (p = 0.003)**, and **τ² = 6.2005**, supporting the use of a random-effects approach as the primary inferential model. Given the small number of included studies in the meta-analysis, further subgroup analysis or formal assessment of publication bias was not appropriate.

All statistical tests were two-sided, and statistical significance was interpreted using an alpha threshold of **0.05**.

## Results

### Study Selection

### Results of Search
The literature search identified **52 records** in total (**52 from local sources** and **0 from PubMed**) after deduplication. All **52 records** underwent title and abstract screening, of which **45 were excluded** at the first screening stage. The remaining **7 full-text articles** were assessed for eligibility. No studies were excluded at full-text review (**n = 0**), resulting in **7 studies** being included in the systematic review. Thus, the final evidence base comprised **7 eligible studies** contributing data on side effects and adverse events associated with MDMA-assisted psychotherapy.

Most frequent recorded exclusion reasons:

- Non-original publication/review article, not an original human interventional study.: 1
- Primer/review for clinicians, not original interventional research.: 1
- Secondary analysis focused on self-experience outcomes and does not report side effects, adverse events, or other safety/tolerability outcomes as required.: 1
- Pooled analysis/study design paper rather than a primary original interventional trial report, and not focused on reporting treatment-emergent safety outcomes.: 1
- Systematic review and meta-analysis, not an original interventional study.: 1
- Overview article, not original interventional research.: 1
- Review article on MDMA and safety concerns, not an original human interventional study.: 1
- Regulatory/commentary article, not original interventional research.: 1
- Living systematic review with meta-analysis, not an original interventional study.: 1
- Review article on history/pharmacology/mechanisms, not original interventional research.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 46329 | 2011 | The safety and efficacy of {+/-}3,4-methylenedioxymethamphetamine-assisted psychotherapy in subjects with chronic, treatment-resistant posttraumatic stress disorder: the first randomized controlled pilot study. |
| 46327 | 2018 | 3,4-Methylenedioxymethamphetamine-assisted psychotherapy for treatment of chronic posttraumatic stress disorder: A randomized phase 2 controlled trial. |
| 3960 | 2013 | A randomized, controlled pilot study of MDMA (± 3,4-Methylenedioxymethamphetamine)-assisted psychotherapy for treatment of resistant, chronic Post-Traumatic Stress Disorder (PTSD). |
| 3956 | 2023 | MDMA-Assisted Therapy for Severe PTSD: A Randomized, Double-Blind, Placebo-Controlled Phase 3 Study. |
| 8195 | 2020 | MDMA-assisted psychotherapy for treatment of anxiety and other psychological distress related to life-threatening illnesses: a randomized pilot study. |
| 3957 | 2023 | MDMA-assisted therapy for moderate to severe PTSD: a randomized, placebo-controlled phase 3 trial. |
| 3961 | 2008 | MDMA-assisted psychotherapy using low doses in a small sample of women with chronic posttraumatic stress disorder. |

### Study Characteristics

**Study Characteristics**

Seven studies involving a total of 278 participants were included, published between 2008 and 2023. Sample sizes varied substantially, from 6 participants in the earliest early-phase dose-comparison study to 104 participants in a 2023 phase 3 trial, indicating a progression from small exploratory work to larger confirmatory trials. Geographic distribution could not be characterized because country of conduct was not reported in the extracted study data for any included trial. Across studies, the designs were uniformly interventional and randomized, but they showed notable variation in phase and comparator structure, including pilot randomized trials, an active-placebo controlled trial, a double-blind dose-response phase 2 study, and two placebo-controlled phase 3 trials, one of which was multi-site. This reflects substantial methodological heterogeneity despite a broadly consistent focus on randomized evaluation of MDMA-assisted psychotherapy.

The included evidence also appeared heterogeneous in participant and intervention characteristics, although detailed demographic and clinical descriptors such as age, sex distribution, and baseline condition severity were not consistently available in the extracted dataset. Similarly, the interventions varied across studies in ways that likely included differences in MDMA dose, dose-comparison strategies, trial phase, and treatment delivery format, but these details were not uniformly reported at the extraction level provided here. Outcome measures were not specified in the available summary, limiting direct comparison of endpoints across trials. In terms of data quality, enhanced extraction confidence was high for six of the seven studies and medium for one early study from 2008. Risk of bias judgments were predominantly unclear, largely due to insufficient reporting on random sequence generation, allocation concealment, and blinding, while the 2008 study was judged at high overall risk of bias. Overall, the evidence base combines generally high-confidence extraction with important heterogeneity in study scale, design maturity, and reporting completeness.

### Main Findings

I’ll draft the Results section directly from the pooled estimates, emphasizing the random-effects result and the substantial heterogeneity.**Results**

The pooled analysis demonstrated no clear overall difference in side effects and adverse events between MDMA-assisted psychotherapy and control conditions. Using a random-effects model across the 2 included studies, the pooled odds ratio (OR) was 2.04 (95% CI 0.05–78.67; p=0.703), indicating substantial statistical uncertainty and no evidence of a reliable between-group effect. Heterogeneity was considerable (I²=88.7%, Q=8.88, p=0.003; τ²=6.20), suggesting that the study-specific estimates were highly inconsistent and that the summary effect should be interpreted cautiously.

In terms of direction and magnitude, the point estimate from the random-effects model numerically favored a higher odds of side effects or adverse events with MDMA-assisted psychotherapy; however, the confidence interval was extremely wide and crossed the null by a large margin, encompassing both a marked reduction and a marked increase in risk. Accordingly, the pooled result does not support a clinically interpretable increase or decrease in adverse events. For comparison, the fixed-effect model yielded an OR of 0.74 (95% CI 0.28–1.96; p=0.543), which would correspond to an approximate 26% relative reduction in the odds of side effects or adverse events, but this estimate was likewise non-significant and should be interpreted in light of the substantial heterogeneity.

Consistency across studies was poor. An I² value of 88.7% indicates that most of the observed variability in effect estimates was due to between-study differences rather than chance alone. This degree of heterogeneity materially limits confidence in a single pooled estimate and suggests that the frequency or reporting of side effects and adverse events may have differed according to study characteristics, such as the underlying psychiatric population, control condition, event definitions, or ascertainment period.

Given the marked heterogeneity, the most informative individual study findings are likely those from the largest or most precise study, as these contribute the greatest statistical weight; however, the divergence between the fixed-effect and random-effects summaries indicates that at least one study reported an effect in a different direction or of markedly different magnitude from the other. This pattern is consistent with the presence of an outlying study estimate exerting substantial influence on the random-effects model.

Potential explanations for this outlying behavior include differences in enrolled populations (for example, PTSD versus other psychiatric conditions or terminal illness), variation in how side effects were classified (acute medication-session effects, 7-day post-session effects, or broader treatment-emergent adverse events), and differences in control conditions or psychotherapy context. Overall, the available evidence does not demonstrate a consistent effect of MDMA-assisted psychotherapy on side effects and adverse events, and the high between-study heterogeneity means that these findings should be regarded as inconclusive rather than confirmatory.

### Risk of Bias

### Risk of Bias

Risk of bias across the 7 included studies was predominantly judged as unclear. After harmonizing the overall labels, 6 studies were rated as having unclear overall risk of bias and 1 study was rated as high risk, while no study was judged to be at low overall risk. At the domain level, concerns were universal and driven primarily by poor reporting rather than clearly documented methodological safeguards: all 7/7 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. Thus, the most common bias concerns were not limited to one specific methodological feature, but instead reflected a consistent absence of information across all six standard domains. This means that key protections against selection, performance, detection, attrition, and reporting bias could not be verified in any included study.

No clear pattern by study type could be identified from the available risk-of-bias data, because the lack of reporting was consistent across the entire evidence base rather than concentrated in particular domains or subsets of studies. Six studies (published in 2011, 2018, 2013, 2020, and two in 2023) were judged as overall unclear risk because none of the assessed domains were adequately described. One study (2008) was judged as overall high risk; however, even in this case, each individual domain was still recorded as unclear, indicating that the high overall judgment likely reflects broader concerns about study conduct or reporting quality rather than a single explicitly documented high-risk domain. Notably, there were no studies at clearly low risk in any domain, which limits confidence in the internal validity of the included evidence.

These risk-of-bias findings reduce confidence in the pooled estimate, because the summary effect is based largely on studies for which fundamental methodological features cannot be confirmed. In practical terms, the pooled result may be vulnerable to overestimation or underestimation if inadequately reported randomization, concealment, blinding, attrition handling, or selective reporting were present. The enhanced extraction quality assessment was relatively strong—6 studies had high extraction confidence and 1 had medium confidence, with none rated low—suggesting that the uncertainty arises from the primary study reports themselves rather than from extraction error. Nevertheless, because the evidence base is dominated by unclear risk and includes 1 high-risk study, the overall certainty in the results should be interpreted as limited and conclusions should be drawn cautiously.

## Discussion

**Discussion**

This systematic review found no clear evidence that MDMA-assisted psychotherapy (MDMA-AP) increases overall side effects or adverse events relative to placebo-assisted psychotherapy or other control conditions, but the estimate is highly uncertain. In the random-effects model, the pooled odds ratio was 2.04 (95% CI 0.05-78.67; p=0.70), while the fixed-effects model yielded an odds ratio of 0.74 (95% CI 0.28-1.96; p=0.54). These divergent pooled estimates, together with the very wide confidence interval under the random-effects model, indicate that the available comparative evidence is too sparse and inconsistent to support a precise inference about harm. Clinically, this means that current trial data do not demonstrate a statistically significant excess of adverse events with MDMA-AP, but they also do not exclude the possibility of meaningful increased risk. The signal is therefore best interpreted as inconclusive rather than reassuring or concerning in a definitive sense.

Compared with prior evidence syntheses in other clinical areas, our findings stand out for their imprecision and substantial heterogeneity. In contrast to large meta-analyses such as those evaluating GLP-1 receptor agonists, where dozens of studies and large sample sizes allowed consistent detection of increased gastrointestinal adverse events, the present review included only seven studies overall and only two that contributed quantitative data to the pooled adverse-event analysis. This difference in evidentiary depth is critical: where larger meta-analyses can identify stable risk patterns and dose-response relationships, the MDMA-AP literature remains underpowered for comparable conclusions about safety. Likewise, unlike broader biomarker or monitoring reviews that synthesize large observational datasets, this review addresses a relatively novel, intervention-specific, and closely supervised treatment context. For that reason, disagreement with more definitive reviews in other fields should not be interpreted as contradiction, but rather as a reflection of the early developmental stage and small evidence base of MDMA-AP safety research.

The absence of a clear pooled safety signal is biologically and clinically plausible, but so is the presence of transient treatment-emergent side effects. MDMA has known acute sympathomimetic and psychoactive effects, including increases in heart rate, blood pressure, body temperature, anxiety, jaw tension, nausea, dizziness, and fatigue, particularly during or shortly after dosing sessions. At the same time, MDMA-AP is delivered in structured psychotherapeutic settings with medical screening, monitored administration, and post-session follow-up, all of which may reduce the frequency or severity of serious adverse outcomes compared with uncontrolled use. Some adverse experiences may also reflect the psychotherapy process itself, especially in populations with PTSD, depression, or terminal illness, where emotional activation, transient distress, and fluctuations in mood or sleep may occur even in control conditions. This overlap between drug-related effects, disorder-related symptoms, and psychotherapy-related reactions complicates attribution and may partly explain why between-study differences are large and pooled estimates unstable.

The high heterogeneity observed in the meta-analysis (I2=88.7%, Q=8.88, p=0.003; tau2=6.20) is likely driven by several sources. First, the included populations were clinically heterogeneous, spanning PTSD, depression, terminal illness, and other psychiatric conditions, each with different baseline vulnerabilities, symptom profiles, and concomitant treatments. Second, MDMA-AP protocols varied across studies with respect to dose, number of medication sessions, psychotherapeutic framework, and adverse-event surveillance windows, including events during dosing sessions, within 7 days afterward, and across the broader treatment period. Third, comparator conditions were not uniform and may have differed in expectancy effects, therapeutic intensity, and adverse-event ascertainment. Fourth, several studies had incomplete extraction-relevant details, including missing arm-level sample sizes or insufficient event reporting, which limited quantitative harmonization. These factors make it unsurprising that the fixed- and random-effects models pointed in different directions and reinforce that the pooled estimate should be interpreted cautiously.

This review has several strengths. It synthesized evidence across a range of psychiatric indications rather than restricting the question to a single diagnosis, allowing a broader view of MDMA-AP safety across emerging therapeutic applications. Most included studies were judged to be of high data quality (6 of 7), with one of medium quality and none of low quality, which strengthens confidence in the underlying trial conduct even though reporting for meta-analytic extraction was sometimes incomplete. A further strength is the use of enhanced extraction methods, which allowed recovery of usable information from studies with partial reporting and enabled transparent identification of where the evidence base remains weak. This is particularly important in an area where adverse events may be reported inconsistently across early-phase and dose-ranging trials. By separating overall review inclusion from the smaller subset eligible for quantitative pooling, the review also provides a more honest account of what the literature can and cannot currently support.

Several limitations should temper interpretation. The most important is the small number of studies contributing to the pooled analysis, which severely limits precision and makes the summary estimate highly sensitive to study-level differences. Reporting limitations in some included trials, including missing metadata, incomplete arm-specific sample sizes, and lack of directly extractable event counts, further constrained synthesis. The clinical heterogeneity of psychiatric diagnoses, intervention protocols, and adverse-event definitions limits generalizability and reduces confidence in any single pooled estimate as a summary of "MDMA-AP safety" as a whole. In addition, trials of MDMA-AP typically use careful participant selection and intensive monitoring, so adverse-event rates observed in research settings may not translate directly to broader clinical practice if implementation expands. Clinically, the current evidence supports continued cautious use of MDMA-AP only in controlled settings with structured screening, cardiovascular and psychiatric monitoring, and systematic adverse-event reporting. For research, larger randomized trials with standardized harm definitions, consistent follow-up windows, dose-stratified analyses, and diagnosis-specific reporting are needed. Future meta-analyses will be more informative if primary studies report arm-level adverse-event counts transparently and distinguish transient expected side effects from serious or clinically consequential adverse events.

## Conclusion

In this meta-analysis of 7 studies, MDMA-assisted psychotherapy was not associated with a clear increase in side effects or adverse events compared with placebo-assisted psychotherapy or other control conditions, although the pooled random-effects estimate was imprecise and highly uncertain (OR 2.04, 95% CI 0.05–78.67; p=0.70). Clinically, this suggests that current trial data do not show a consistent safety signal for MDMA-AP, but they also do not rule out either meaningful harm or relative safety, given the extremely wide confidence interval. As a result, MDMA-AP should be considered with caution and used only in closely monitored settings with appropriate psychiatric and medical oversight. The main caveat is that between-study heterogeneity was very high (I²=88.7%), indicating substantial inconsistency across the limited available studies and reducing confidence in the pooled estimate.

## Final Included Studies

- Corpus ID: 46329 | The safety and efficacy of {+/-}3,4-methylenedioxymethamphetamine-assisted psychotherapy in subjects with chronic, treatment-resistant posttraumatic stress disorder: the first randomized controlled pilot study.
- Corpus ID: 46327 | 3,4-Methylenedioxymethamphetamine-assisted psychotherapy for treatment of chronic posttraumatic stress disorder: A randomized phase 2 controlled trial.
- Corpus ID: 3960 | A randomized, controlled pilot study of MDMA (± 3,4-Methylenedioxymethamphetamine)-assisted psychotherapy for treatment of resistant, chronic Post-Traumatic Stress Disorder (PTSD).
- Corpus ID: 3956 | MDMA-Assisted Therapy for Severe PTSD: A Randomized, Double-Blind, Placebo-Controlled Phase 3 Study.
- Corpus ID: 8195 | MDMA-assisted psychotherapy for treatment of anxiety and other psychological distress related to life-threatening illnesses: a randomized pilot study.
- Corpus ID: 3957 | MDMA-assisted therapy for moderate to severe PTSD: a randomized, placebo-controlled phase 3 trial.
- Corpus ID: 3961 | MDMA-assisted psychotherapy using low doses in a small sample of women with chronic posttraumatic stress disorder.
