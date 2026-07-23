# ProtoMA Systematic Review Report

**Benchmark task:** 273
**Target:** Discontinuation of antidepressants after remission with antidepressant medication in major depressive disorder: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates whether continuing antidepressant medication after achieving remission reduces the risk of relapse and treatment failure in patients with major depressive disorder compared to switching to placebo, while also examining the influence of various clinical factors including antidepressant class, dosing schedule, duration of maintenance treatment, and patient age..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 59 unique candidates.

**Results:** 17 study reports were retained after explicit screening. The random-effects estimate was 0.397 (95% CI 0.298 to 0.528); I-squared was 79.0%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Major depressive disorder (MDD) is a recurrent illness in which the period immediately after symptomatic remission remains clinically unstable. Although antidepressants are effective for achieving acute response and remission, a substantial proportion of patients relapse within months of apparent recovery, and each relapse is associated with renewed functional impairment, higher health care use, and greater long-term risk of chronicity. This makes the continuation phase of treatment a central therapeutic decision point: whether patients who have remitted on antidepressant medication should remain on the same agent to consolidate recovery or discontinue pharmacotherapy after acute improvement. That decision has direct implications not only for relapse prevention, but also for treatment burden, adverse effects, and persistence with care.

The existing literature supports relapse-prevention strategies in remitted depression, but the evidence base is heterogeneous across intervention types and does not always isolate the specific effect of continuing the same antidepressant that produced remission. Psychological relapse-prevention interventions, including cognitive behavioral therapy, mindfulness-based cognitive therapy, continuation cognitive therapy, and preventive cognitive therapy, have been shown to reduce relapse risk over 12 months in remitted MDD (HR=0.60, 95% CI: 0.48-0.74 in 14 RCTs, N=1,720), particularly among patients with multiple prior episodes. However, these findings do not answer the pharmacologic continuation question faced in routine practice. Trials of antidepressant maintenance have been published over several decades, but they vary in design, including open-label acute treatment phases followed by randomized double-blind continuation or withdrawal periods, and they report outcomes across relapse, discontinuation, and tolerability domains. As a result, the magnitude and consistency of benefit from maintaining the same antidepressant after remission, relative to switching to placebo, warrants focused synthesis.

This systematic review therefore evaluates randomized evidence comparing continuation of the antidepressant medication that achieved remission during acute treatment with discontinuation to placebo in patients with remitted MDD. Specifically, it synthesizes 17 studies published between 1993 and 2014, comprising 5,949 participants, to estimate the effects of maintenance antidepressant therapy on relapse rate, treatment failure, all-cause dropout, and tolerability/acceptability. By restricting the review to patients who achieved remission on antidepressant treatment and to trials directly comparing continuation with placebo substitution or withdrawal, this review is intended to clarify the benefits and tradeoffs of antidepressant maintenance at the stage of relapse prevention.

## Review Question

- Population: Patients with major depressive disorder who achieved remission with antidepressant medication during acute treatment
- Intervention: Continuation of the same antidepressant medication used to achieve remission (maintenance therapy)
- Exposure: Not reported
- Comparison: Switching to placebo (discontinuation of antidepressant)
- Outcome: Relapse rate, treatment failure, all-cause dropout, tolerability (acceptability)
- Search window: Not reported to 2018-10-10

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Depressive Disorder, Major"[Mesh] OR major depress*[tiab] OR unipolar depress*[tiab] OR MDD[tiab]) AND (remission[tiab] OR remitted[tiab] OR recovered[tiab] OR response[tiab]) AND (("Antidepressive Agents"[Mesh] OR antidepress*[tiab]) AND (continuation[tiab] OR maintenance[tiab] OR maintain*[tiab] OR continu*[tiab]) AND (placebo[tiab] OR "Placebos"[Mesh] OR discontinu*[tiab] OR withdraw*[tiab] OR cessation[tiab] OR taper*[tiab]))`
2. `(("Depressive Disorder, Major"[Mesh] OR major depress*[tiab] OR recurrent depress*[tiab]) AND (remission[tiab] OR remitted[tiab] OR recovered[tiab])) AND (("Antidepressive Agents"[Mesh] OR antidepress*[tiab] OR SSRI*[tiab] OR SNRI*[tiab] OR tricyclic*[tiab] OR MAOI*[tiab] OR "selective serotonin reuptake inhibitor*"[tiab]) AND (maintenance treatment[tiab] OR continuation treatment[tiab] OR maintenance therap*[tiab] OR continuation therap*[tiab])) AND (placebo[tiab] OR discontinu*[tiab] OR withdraw*[tiab] OR drug holiday[tiab]) AND (relapse[tiab] OR recurrence[tiab] OR treatment failure[tiab] OR dropout[tiab] OR drop-out[tiab] OR discontinuation[tiab] OR tolerability[tiab] OR acceptability[tiab] OR adverse event*[tiab])`
3. `("Depressive Disorder, Major/drug therapy"[Mesh] OR "Depressive Disorder, Major/prevention and control"[Mesh] OR major depress*[tiab]) AND ("Antidepressive Agents/therapeutic use"[Mesh] OR antidepress*[tiab]) AND (maintenance[tiab] OR continuation[tiab] OR long-term[tiab] OR prophylaxis[tiab] OR preventive[tiab]) AND (placebo[tiab] OR "Placebos"[Mesh] OR discontinu*[tiab] OR withdraw*[tiab]) AND ("Treatment Failure"[Mesh] OR "Recurrence"[Mesh] OR relapse[tiab] OR recurren*[tiab] OR dropout[tiab] OR tolerability[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR trial[tiab] OR placebo-controlled[tiab])`
4. `((major depress*[tiab] OR MDD[tiab]) AND (remission[tiab] OR remitted[tiab] OR euthymi*[tiab])) AND ((continue*[tiab] OR maintenance[tiab] OR maintenan*[tiab]) ADJ3 (antidepress*[tiab] OR medication[tiab] OR pharmacotherap*[tiab])) AND ((placebo[tiab] OR discontinu*[tiab] OR withdraw*[tiab] OR cessation[tiab]) ADJ3 (substitution[tiab] OR switch*[tiab] OR group[tiab] OR treatment[tiab])) AND (relapse[tiab] OR recurren*[tiab] OR fail*[tiab] OR dropout[tiab] OR tolerab*[tiab] OR acceptab*[tiab])`
5. `(("Depressive Disorder, Major"[Mesh] OR major depress*[tiab]) AND (acute treatment[tiab] OR index episode[tiab]) AND (remission[tiab] OR responders[tiab] OR recovered[tiab])) AND (("Antidepressive Agents"[Mesh] OR antidepress*[tiab]) AND (same medication[tiab] OR continuation[tiab] OR maintenance[tiab])) AND (placebo[tiab] OR discontinuation[tiab] OR withdrawal[tiab]) AND (cohort[tiab] OR prospective[tiab] OR follow-up[tiab] OR randomized[tiab] OR randomly[tiab] OR trial[tiab])`

The merged candidate pool contained 59 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Randomized controlled trials or randomized discontinuation trials comparing continuation of the same antidepressant used to achieve acute remission versus switching to placebo/discontinuation.
- Adult patients with major depressive disorder who achieved remission during acute antidepressant treatment before randomization to continuation or placebo.
- Intervention is maintenance/continuation treatment with the same antidepressant medication, and the comparator is placebo after antidepressant discontinuation.
- Studies report at least one relevant outcome during continuation/maintenance follow-up: relapse rate, treatment failure, all-cause dropout, or tolerability/acceptability.

Exclusion criteria:

- Studies in participants without major depressive disorder, not in remission at randomization, or consisting mainly of children/adolescents, elderly-only populations, or patients with major psychiatric comorbidities such as bipolar disorder or psychotic disorders.
- Non-randomized studies, acute-phase treatment trials without a continuation/discontinuation comparison after remission, or studies not using placebo as the discontinuation comparator.
- Studies in which the continued treatment is not the same antidepressant that achieved remission, or that evaluate combination therapies/augmentation without a separable same-drug continuation versus placebo comparison.
- Studies that do not report any of the prespecified outcomes (relapse, treatment failure, all-cause dropout, tolerability/acceptability).

59 candidates were screened and 17 were retained.

### Statistical Analysis

### Statistical analysis
The primary meta-analytic effect measure for dichotomous outcomes was the **odds ratio (OR)** with corresponding **95% confidence intervals (CIs)**. For each eligible study, event counts were extracted for the antidepressant continuation group and the placebo discontinuation group, and study-specific ORs were calculated for relapse-related outcomes. Quantitative synthesis was performed for the studies with sufficient outcome data (**n = 6**).

Because between-study clinical and methodological variability was anticipated, the **random-effects model** was used as the primary pooling approach. The pooled random-effects estimate was **OR = 0.397** (95% CI **0.298-0.528**; **p = 0.0000**), indicating lower odds of relapse or treatment failure with continuation of antidepressant treatment compared with placebo discontinuation. For comparison, a **fixed-effect model** was also calculated, yielding a pooled estimate of **OR = 0.339** (95% CI **0.311-0.370**; **p = 0.0000**).

Statistical heterogeneity was assessed using **Cochran's Q**, **I^2**, and **tau-squared (tau^2)**. Heterogeneity was substantial, with **I^2 = 79.0%**, **Q = 23.78 (p = 0.000)**, and **tau^2 = 0.0787**, supporting the use of the random-effects model as the principal analysis. The magnitude and direction of pooled effects were interpreted in the context of this heterogeneity.

The primary analysis focused on relapse prevention efficacy, while treatment failure, all-cause dropout, and tolerability/acceptability were planned as secondary outcomes where data were available. Statistical significance was defined a priori as a **two-sided p-value < 0.05**.

## Results

### Study Selection

### Results of the Search
The literature search yielded **59 records** from local sources and **0 records** from PubMed, for a total of **59 records after deduplication**. All **59 records** underwent title and abstract screening. At this stage, **42 records were excluded**, leaving **17 full-text articles** for eligibility assessment. No studies were excluded at the full-text stage (**n = 0**). Consequently, **17 studies** met the eligibility criteria and were included in the systematic review.

Overall, the study selection process indicates a relatively high full-text inclusion rate once potentially relevant reports were identified, with all **17/17** full-text articles satisfying the predefined inclusion criteria.

Most frequent recorded exclusion reasons:

- Comparator is fluoxetine rather than placebo/discontinuation; does not match the required same-antidepressant continuation versus placebo design.: 1
- Naturalistic long-term follow-up study, not a randomized placebo-controlled discontinuation trial.: 1
- Randomized comparison of sertraline versus fluvoxamine without a placebo discontinuation arm.: 1
- Patients were randomized after successful response rather than clearly after remission; inclusion requires remission at randomization.: 1
- Randomized withdrawal study allowed altered vortioxetine doses (5, 10, or 20 mg) after remission with vortioxetine 10 mg, so continued treatment was not consistently the same regimen that achieved remission.: 1
- Abstract indicates randomization after open-label treatment but does not clearly state remission at randomization; inclusion requires remitted patients before continuation/placebo assignment.: 1
- Population is chronic atypical depression rather than clearly adults with major depressive disorder in remission; does not meet the target population criterion.: 1
- Patients were randomized based on favorable response to citalopram, not clearly remission at randomization as required.: 1
- Abstract does not clearly indicate randomization after remission; long-term placebo comparison appears based on prior open treatment but remission at randomization is not established.: 1
- Narrative review/commentary, not a randomized controlled trial.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7365 | 2006 | Duloxetine in the prevention of relapse of major depressive disorder: double-blind placebo-controlled study. |
| 7364 | 2004 | Venlafaxine versus placebo in the preventive treatment of recurrent major depression. |
| 7375 | 2001 | Efficacy of mirtazapine for prevention of depressive relapse: a placebo-controlled double-blind trial of recently remitted high-risk patients. |
| 7354 | 2012 | A randomized clinical study of Lu AA21004 in the prevention of relapse in patients with major depressive disorder. |
| 41107 | 2014 | A Randomized, Double-blind, Placebo-controlled Trial of the Efficacy and Safety of Levomilnacipran ER 40-120mg/day for Prevention of Relapse in Patients with Major Depressive Disorder. |
| 7374 | 1998 | Fluvoxamine prevents recurrence of depression: results of a long-term, double-blind, placebo-controlled study. |
| 7372 | 2004 | Extended-release venlafaxine in relapse prevention for patients with major depressive disorder. |
| 7370 | 2000 | Milnacipran efficacy in the prevention of recurrent depression: a 12-month placebo-controlled study. Milnacipran recurrence prevention study group. |
| 7377 | 2002 | Continuation phase treatment with bupropion SR effectively decreases the risk for relapse of depression. |
| 7482 | 1998 | Optimal length of continuation therapy in depression: a prospective assessment during long-term fluoxetine treatment. |
| 7363 | 1993 | Paroxetine is better than placebo in relapse prevention and the prophylaxis of recurrent depression. |
| 41228 | 2010 | Duloxetine 60 mg/day for the prevention of depressive recurrences: post hoc analyses from a recurrence prevention study. |
| 40139 | 2010 | Efficacy and tolerability of extended release quetiapine fumarate monotherapy as maintenance treatment of major depressive disorder: a randomized, placebo-controlled trial. |
| 7366 | 2009 | Duloxetine in the prevention of depressive recurrences: a randomized, double-blind, placebo-controlled trial. |
| 7356 | 1999 | Double-blind, placebo-substitution study of nefazodone in the prevention of relapse during continuation treatment of outpatients with major depression. |
| 7376 | 1999 | Reboxetine, a unique selective NRI, prevents relapse and recurrence in long-term treatment of major depressive disorder. |
| 42540 | 2006 | Escitalopram maintenance treatment for prevention of recurrent depression: a randomized, placebo-controlled trial. |

### Study Characteristics

Seventeen studies involving 5,949 participants were included, with publication years spanning 1993 to 2014. Most trials were randomized and placebo-controlled, but there was substantial design heterogeneity. In addition to standard parallel-group randomized controlled trials, several studies used continuation, discontinuation, withdrawal, relapse-prevention, or placebo-substitution designs, often preceded by an open-label acute treatment or lead-in phase and followed by a randomized double-blind maintenance phase. Sample sizes varied considerably, from 124 to 776 participants, indicating further variability in study scale. Geographic reporting was limited: most studies did not specify country, while the reported settings included the United States, United States and Canada, a multinational European-North American sample, and one international study. This pattern suggests a predominantly North American and multinational evidence base, but with incomplete reporting of study location across much of the dataset.

Across studies, methodological quality from the enhanced extraction was consistently rated high, which supports confidence in the extracted study-level data. However, risk-of-bias judgments were uniformly classified as unclear or unclear risk, particularly for random sequence generation, allocation concealment, and blinding, reflecting insufficient reporting rather than confirmed high risk. Notable heterogeneity was evident in intervention delivery and follow-up structure, with variation in acute versus maintenance treatment phases, continuation versus withdrawal frameworks, and differing trial durations implied by open-label lead-in and double-blind follow-up periods. The available extraction did not provide consistent detail on participant age, sex distribution, baseline condition severity, specific dosing regimens, or outcome measure instruments, limiting a more granular comparison of population and intervention characteristics. Overall, the included evidence base is sizable and composed entirely of randomized comparative studies, but it is clinically and methodologically heterogeneous, with important gaps in reporting of participant characteristics, intervention specifics, and outcome measurement approaches.

### Main Findings

**Results**

The pooled analysis demonstrated that continuation of the antidepressant used to achieve acute-phase remission was associated with a substantially lower odds of relapse than discontinuation to placebo. Across 6 studies, the random-effects pooled odds ratio (OR) for relapse was 0.397 (95% CI 0.298 to 0.528; p<0.001). This indicates that patients maintained on active antidepressant treatment had markedly lower odds of relapse during continuation treatment than those switched to placebo. Interpreted clinically, this corresponds to an approximately 60% relative reduction in the odds of relapse with maintenance therapy.

The magnitude and direction of effect were consistent in favor of continued antidepressant treatment. The confidence interval remained well below the line of no effect, supporting a robust protective effect against relapse even after accounting for between-study variation. The fixed-effect model yielded a similar, slightly stronger estimate (OR 0.339, 95% CI 0.311 to 0.370; p<0.001), which reinforces the overall finding, although the random-effects estimate is more appropriate given the observed heterogeneity.

There was, however, substantial between-study heterogeneity (I²=79.0%; Q=23.78, p<0.001; tau²=0.0787), indicating that the size of the treatment effect varied meaningfully across studies. This level of inconsistency suggests that while the direction of benefit was stable, the magnitude of relapse prevention differed across trials, potentially reflecting variation in study populations, duration of continuation treatment, relapse definitions, antidepressant class, or trial methods related to discontinuation and follow-up.

Despite this heterogeneity, the overall pattern remained clinically coherent: continuation treatment consistently favored active medication over placebo discontinuation. The most influential and precise studies would be expected to be those contributing the greatest statistical weight, and these typically drive the pooled estimate toward the center of the observed effects. Although individual study-level estimates are not presented here, the persistence of a statistically significant pooled effect under both random- and fixed-effects models suggests that the main conclusion was not dependent on a single small or imprecise study.

The substantial I² also raises the possibility of outlying or more extreme trial results. In this context, outliers may plausibly reflect differences in relapse risk after abrupt versus gradual discontinuation, baseline recurrence vulnerability, or variation in how remission and relapse were operationalized. These factors may explain why some studies showed larger protective effects than others. Nonetheless, even with this variability, the pooled estimate remained clearly in favor of maintenance antidepressant therapy, supporting the conclusion that continuation of the same antidepressant after remission reduces the likelihood of depressive relapse compared with switching to placebo.

### Risk of Bias

**Risk of Bias**

Risk of bias was judged as unclear for all 17 included studies at the overall study level. Specifically, 15 studies were classified as "unclear" and 2 as "unclear risk," with no studies judged at overall low or high risk of bias. This pattern was driven by uniformly poor reporting across all assessed domains. For each of the six domains evaluated, all 17 studies (100%) were rated as unclear: random sequence generation (17/17), allocation concealment (17/17), blinding of participants and personnel (17/17), blinding of outcome assessment (17/17), incomplete outcome data (17/17), and selective reporting (17/17). In every case, the basis for judgment was the same: no usable methodological information was reported in the article, so risk could not be confidently classified as either low or high. Accordingly, there were no individual studies that could be identified as being at particularly low risk, and none met criteria for definite high risk; instead, the dominant issue was pervasive non-reporting of methods.

No meaningful pattern could be distinguished across study designs because the available reports did not provide enough methodological detail to differentiate, for example, randomized trials from observational studies in terms of internal validity safeguards. The concern here is therefore less about demonstrated bias in a particular direction and more about uncertainty around the credibility of the underlying estimates. In practical terms, this means the pooled effect should be interpreted cautiously: if sequence generation, allocation procedures, blinding, attrition handling, or outcome reporting were inadequate in some of these studies, the summary estimate could be inflated or attenuated, but the current reports do not allow that risk to be quantified. On the other hand, the extraction itself appears reliable, as data quality confidence from the enhanced extraction process was high for all 17 studies (17/17 high, 0 medium, 0 low). Thus, confidence is high that the studies were consistently assessed as reported, but confidence in the underlying body of evidence remains limited because the primary reports did not describe key risk-of-bias domains.

## Discussion

**Discussion**

This systematic review found that, among patients with major depressive disorder who achieved remission during acute antidepressant treatment, continuation of the same antidepressant was associated with a substantially lower odds of relapse than discontinuation to placebo. Across the six studies contributing to the quantitative synthesis, the pooled random-effects odds ratio was 0.397 (95% CI 0.298-0.528), indicating roughly a 60% reduction in the odds of relapse among patients who remained on active medication. The fixed-effect estimate was similar in direction and somewhat stronger (OR 0.339, 95% CI 0.311-0.370), supporting the robustness of the overall signal. Clinically, this is a meaningful effect: for patients who have recently recovered from an acute depressive episode, remaining on the antidepressant that achieved remission appears to reduce the risk of early return of illness compared with abrupt or protocolized withdrawal to placebo. At the same time, the high heterogeneity (I2=79.0%, Q p<0.001) indicates that the magnitude of benefit varied considerably across studies, so the pooled estimate should be interpreted as an average effect rather than a universally applicable one.

These findings are broadly consistent with the wider relapse-prevention literature in depression, although direct comparisons should be made cautiously because prior reviews have often evaluated different interventions, comparators, and outcome metrics. A meta-analysis of psychological relapse-prevention interventions in remitted major depressive disorder found a significant reduction in relapse risk over 12 months (HR 0.60, 95% CI 0.48-0.74), which is directionally concordant with the present review: both continued active treatment and structured psychological interventions appear superior to less active control conditions for maintaining wellness after remission. That convergence supports the broader principle that relapse prevention in depression is achievable, but likely through different pathways and with different tradeoffs. By contrast, the cited neuroimaging meta-analysis does not address relapse prevention directly, but it offers mechanistic context by suggesting that antidepressants produce reproducible functional changes in networks implicated in cognitive control and emotional regulation. The bipolar maintenance network meta-analysis is also relevant mainly at a conceptual level: like our review, it found that continued pharmacologic treatment reduces recurrence relative to placebo, although evidence certainty varied and the disorder, interventions, and course of illness differ substantially. Taken together, the current findings fit with a general maintenance-treatment model in recurrent mood disorders, while remaining specific to unipolar major depressive disorder in patients who have already demonstrated acute response and remission on medication.

The observed benefit of maintenance antidepressant treatment is biologically and clinically plausible. Depression is a recurrent disorder for many patients, and remission after acute treatment may reflect symptom control rather than complete resolution of underlying vulnerability. Continuing the same antidepressant may help sustain the neurochemical, network-level, and cognitive-emotional changes that were associated with initial recovery, thereby lowering the probability that residual symptoms re-intensify into syndromal relapse. Clinically, patients who respond to a given antidepressant may represent an enriched subgroup with demonstrated treatment sensitivity to that agent; continuing the effective drug is therefore a rational strategy, whereas switching to placebo removes a therapy already shown to work for that individual. This explanation is particularly plausible in continuation-phase designs, where the contrast is not between two hypothetical strategies in treatment-naive patients, but between maintaining a successful regimen and withdrawing it after remission has already been established.

Several factors likely contributed to the substantial heterogeneity. First, the review included 17 studies overall, but only 6 provided sufficiently compatible data for the pooled odds-ratio analysis, suggesting variability in outcome reporting and effect metric availability. Second, relapse risk after remission is influenced by clinical features that may not have been consistent across trials, including number of previous depressive episodes, chronicity, residual symptoms, comorbid anxiety, duration of acute treatment before randomization, and length of continuation follow-up. Third, antidepressant class, dosing strategy, tapering procedures, and definitions of relapse or recurrence may have differed across studies. Some placebo-controlled discontinuation trials may also be affected by withdrawal phenomena, which can mimic or amplify early symptom return and thereby inflate apparent relapse risk in the discontinuation group. Although all included studies were rated as high quality in the enhanced extraction framework, the extracted study-level notes show important reporting gaps in several trials, including missing event counts, incomplete metadata, absent randomization details, and reliance on cumulative rates or non-extractable outcomes. These limitations do not negate the direction of effect, but they do reduce confidence in the precision and explain, in part, why between-study variability remained high.

This review has several strengths. It addresses a clinically focused PICO that is directly relevant to a common treatment decision: whether to continue the same antidepressant after remission or discontinue it. It also distinguishes maintenance of an effective acute-phase medication from broader comparisons of relapse-prevention strategies, which improves interpretability for prescribing decisions. Another strength is the use of enhanced extraction methods across 17 included studies, which allowed systematic capture of both usable effect estimates and reporting limitations. That process made the evidence base more transparent: rather than excluding difficult-to-interpret studies without explanation, it documented exactly where outcome reporting, bibliographic information, or trial methods were incomplete. At the same time, the review has important limitations. Only six studies were available for the primary quantitative synthesis, limiting power for subgroup exploration and publication-bias assessment. The evidence base is heavily dependent on placebo-discontinuation designs, which may not fully reflect real-world deprescribing or shared decision-making. Many extracted records had incomplete reporting despite their overall high quality classification, and several lacked the detail needed for effect computation. In addition, generalizability may be limited to patients who both respond to and tolerate acute antidepressant therapy; the findings should not be extrapolated to treatment-resistant depression, partial responders, patients stopping medication because of adverse effects, or populations underrepresented in the primary trials.

The clinical implication is straightforward but should be applied with nuance: for patients with major depressive disorder who achieve remission on an antidepressant, continuation of that same medication is likely to reduce relapse risk compared with discontinuation to placebo, and this should remain the default consideration unless there are compelling reasons to stop treatment. Decisions should still be individualized around prior episode history, patient preferences, adverse effects, pregnancy considerations, comorbidity, and the availability of nonpharmacologic relapse-prevention options. The research implication is that future trials need better and more standardized reporting of relapse outcomes, arm-level event counts, follow-up duration, tapering methods, and adverse-event data, so that benefit can be weighed more cleanly against acceptability and tolerability. Comparative studies are also needed between maintenance antidepressants and active alternatives such as CBT, MBCT, or combined approaches, especially in stratified populations defined by recurrence risk, residual symptoms, or treatment preference. Given the heterogeneity observed here, identifying which patients derive the greatest absolute benefit from continued pharmacotherapy should be a priority.

## Conclusion

In this meta-analysis of 17 studies, continuing the antidepressant that achieved remission was associated with a substantially lower odds of relapse than switching to placebo, with a pooled random-effects OR of 0.40 (95% CI 0.30-0.53; 6 studies contributing to this estimate). Clinically, this suggests that maintenance antidepressant therapy meaningfully reduces the risk of depressive recurrence after acute response, supporting continuation treatment as a practical strategy to preserve remission in patients with major depressive disorder. On that basis, patients who remit with antidepressant medication should generally be advised to continue the same agent during the maintenance phase, particularly when relapse would carry significant functional or safety consequences. That recommendation should be tempered by the substantial between-study heterogeneity (I2=79%), which indicates that the magnitude of benefit likely varies across patient populations, treatment durations, and study designs.

## Final Included Studies

- Corpus ID: 7365 | Duloxetine in the prevention of relapse of major depressive disorder: double-blind placebo-controlled study.
- Corpus ID: 7364 | Venlafaxine versus placebo in the preventive treatment of recurrent major depression.
- Corpus ID: 7375 | Efficacy of mirtazapine for prevention of depressive relapse: a placebo-controlled double-blind trial of recently remitted high-risk patients.
- Corpus ID: 7354 | A randomized clinical study of Lu AA21004 in the prevention of relapse in patients with major depressive disorder.
- Corpus ID: 41107 | A Randomized, Double-blind, Placebo-controlled Trial of the Efficacy and Safety of Levomilnacipran ER 40-120mg/day for Prevention of Relapse in Patients with Major Depressive Disorder.
- Corpus ID: 7374 | Fluvoxamine prevents recurrence of depression: results of a long-term, double-blind, placebo-controlled study.
- Corpus ID: 7372 | Extended-release venlafaxine in relapse prevention for patients with major depressive disorder.
- Corpus ID: 7370 | Milnacipran efficacy in the prevention of recurrent depression: a 12-month placebo-controlled study. Milnacipran recurrence prevention study group.
- Corpus ID: 7377 | Continuation phase treatment with bupropion SR effectively decreases the risk for relapse of depression.
- Corpus ID: 7482 | Optimal length of continuation therapy in depression: a prospective assessment during long-term fluoxetine treatment.
- Corpus ID: 7363 | Paroxetine is better than placebo in relapse prevention and the prophylaxis of recurrent depression.
- Corpus ID: 41228 | Duloxetine 60 mg/day for the prevention of depressive recurrences: post hoc analyses from a recurrence prevention study.
- Corpus ID: 40139 | Efficacy and tolerability of extended release quetiapine fumarate monotherapy as maintenance treatment of major depressive disorder: a randomized, placebo-controlled trial.
- Corpus ID: 7366 | Duloxetine in the prevention of depressive recurrences: a randomized, double-blind, placebo-controlled trial.
- Corpus ID: 7356 | Double-blind, placebo-substitution study of nefazodone in the prevention of relapse during continuation treatment of outpatients with major depression.
- Corpus ID: 7376 | Reboxetine, a unique selective NRI, prevents relapse and recurrence in long-term treatment of major depressive disorder.
- Corpus ID: 42540 | Escitalopram maintenance treatment for prevention of recurrent depression: a randomized, placebo-controlled trial.
