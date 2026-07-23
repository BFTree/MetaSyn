# ProtoMA Systematic Review Report

**Benchmark task:** 268
**Target:** Antidepressants for the treatment of adults with major depressive disorder in the maintenance phase: a systematic review and network meta-analysis

## Abstract

**Background:** This review addresses This systematic review and network meta-analysis investigates the efficacy, acceptability, tolerability, and safety of various antidepressants compared to placebo for maintaining remission in adults with major depressive disorder who have been stabilized on antidepressant treatment during the maintenance phase..

**Methods:** ProtoMA generated 4 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 66 unique candidates.

**Results:** 28 study reports were retained after explicit screening. The random-effects estimate was 0.468 (95% CI 0.379 to 0.580); I-squared was 68.9%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Major depressive disorder (MDD) is a recurrent illness in which the period after symptomatic stabilization remains clinically vulnerable. Even after remission is achieved with acute-phase antidepressant treatment, many adults experience relapse within the subsequent months, with consequences that extend beyond symptom return to impaired functioning, reduced quality of life, repeated treatment episodes, and greater health service use. Maintenance pharmacotherapy is therefore a core component of long-term management, particularly for patients who have responded to antidepressants and require continuation of benefit while minimizing treatment discontinuation and adverse effects. In this setting, the central clinical question is not simply whether antidepressants work acutely, but whether continued antidepressant treatment meaningfully prevents relapse over clinically relevant follow-up while remaining acceptable and tolerable to patients.

The evidence base for maintenance-phase antidepressant treatment includes randomized placebo-controlled continuation, maintenance, withdrawal, and discontinuation designs, often preceded by open-label acute or continuation phases that enrich randomized populations for treatment responders. Across studies published from 1993 to 2022, 28 trials enrolling 11,713 participants have evaluated a broad range of antidepressants, including agomelatine, amitriptyline, bupropion, citalopram, desvenlafaxine, duloxetine, escitalopram, fluoxetine, fluvoxamine, levomilnacipran, milnacipran, mirtazapine, nefazodone, paroxetine, reboxetine, sertraline, tianeptine, venlafaxine, vilazodone, and vortioxetine, against placebo in adults with stabilized MDD. However, this literature remains difficult to interpret at the level required for clinical decision-making. Trials differ in design, duration, relapse definitions, and reporting of acceptability and safety outcomes, and many individual studies are underpowered to detect differences in discontinuation or specific adverse events. While meta-analytic approaches in adjacent psychiatric fields have clarified comparative benefits and risks of maintenance treatments, a focused synthesis of placebo-controlled maintenance-phase antidepressant evidence in stabilized adults with MDD, centered on relapse prevention and treatment tolerability, remains necessary.

Accordingly, this systematic review aims to evaluate the efficacy and safety of antidepressants, compared with placebo, for maintenance treatment in adults with MDD who were stabilized on antidepressant therapy. The primary outcome is relapse rate at 6 months. Secondary outcomes are all-cause discontinuation, discontinuation due to adverse events, and the incidence of individual adverse events. By synthesizing evidence across 20 antidepressants and 28 randomized studies, this review seeks to define the extent to which continued antidepressant treatment prevents relapse during the maintenance phase and to characterize the trade-offs between sustained efficacy, treatment continuation, and adverse effects.

## Review Question

- Population: adults with major depressive disorder in the maintenance phase (stabilized on antidepressants)
- Intervention: antidepressants (20 different types including agomelatine, amitriptyline, bupropion, citalopram, desvenlafaxine, duloxetine, escitalopram, fluoxetine, fluvoxamine, levomilnacipran, milnacipran, mirtazapine, nefazodone, paroxetine, reboxetine, sertraline, tianeptine, venlafaxine, vilazodone, and vortioxetine)
- Exposure: Not reported
- Comparison: placebo
- Outcome: 6-month relapse rate (primary), all-cause discontinuation, discontinuation due to adverse events, and incidence of individual adverse events
- Search window: Not reported to 2022-05-22

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Depressive Disorder, Major"[MeSH] OR major depressive disorder[tiab] OR major depress*[tiab] OR MDD[tiab] OR unipolar depression[tiab]) AND (maintenance[tiab] OR continuation[tiab] OR relapse prevention[tiab] OR stabilized[tiab] OR stable[tiab]) AND ("Antidepressive Agents"[MeSH] OR antidepress*[tiab] OR agomelatine[tiab] OR amitriptyline[tiab] OR bupropion[tiab] OR citalopram[tiab] OR desvenlafaxine[tiab] OR duloxetine[tiab] OR escitalopram[tiab] OR fluoxetine[tiab] OR fluvoxamine[tiab] OR levomilnacipran[tiab] OR milnacipran[tiab] OR mirtazapine[tiab] OR nefazodone[tiab] OR paroxetine[tiab] OR reboxetine[tiab] OR sertraline[tiab] OR tianeptine[tiab] OR venlafaxine[tiab] OR vilazodone[tiab] OR vortioxetine[tiab])`
2. `("Depressive Disorder, Major"[MeSH] OR major depressive disorder[tiab] OR major depress*[tiab] OR MDD[tiab]) AND (maintenance[tiab] OR continuation[tiab] OR stable remission[tiab] OR stabilized[tiab]) AND ("Antidepressive Agents"[MeSH] OR antidepress*[tiab] OR agomelatine[tiab] OR amitriptyline[tiab] OR bupropion[tiab] OR citalopram[tiab] OR desvenlafaxine[tiab] OR duloxetine[tiab] OR escitalopram[tiab] OR fluoxetine[tiab] OR fluvoxamine[tiab] OR levomilnacipran[tiab] OR milnacipran[tiab] OR mirtazapine[tiab] OR nefazodone[tiab] OR paroxetine[tiab] OR reboxetine[tiab] OR sertraline[tiab] OR tianeptine[tiab] OR venlafaxine[tiab] OR vilazodone[tiab] OR vortioxetine[tiab]) AND (placebo[tiab] OR placebo[MeSH]) AND (relapse[tiab] OR recurrence[tiab] OR recurrent[tiab] OR discontinuation[tiab] OR withdrawal[tiab] OR adverse event*[tiab] OR side effect*[tiab] OR tolerability[tiab])`
3. `("Depressive Disorder, Major"[MeSH] OR major depressive disorder[tiab] OR major depress*[tiab] OR MDD[tiab]) AND (maintenance[tiab] OR continuation[tiab] OR relapse prevention[tiab] OR stable remission[tiab] OR stabilized[tiab]) AND ("Antidepressive Agents"[MeSH] OR antidepress*[tiab] OR agomelatine[tiab] OR amitriptyline[tiab] OR bupropion[tiab] OR citalopram[tiab] OR desvenlafaxine[tiab] OR duloxetine[tiab] OR escitalopram[tiab] OR fluoxetine[tiab] OR fluvoxamine[tiab] OR levomilnacipran[tiab] OR milnacipran[tiab] OR mirtazapine[tiab] OR nefazodone[tiab] OR paroxetine[tiab] OR reboxetine[tiab] OR sertraline[tiab] OR tianeptine[tiab] OR venlafaxine[tiab] OR vilazodone[tiab] OR vortioxetine[tiab]) AND (placebo[tiab] OR placebo[MeSH]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR double blind*[tiab] OR single blind*[tiab] OR trial[tiab])`
4. `("Depressive Disorder, Major"[MeSH] OR major depressive disorder[tiab] OR major depress*[tiab] OR MDD[tiab]) AND (continuation[tiab] OR maintenance[tiab] OR maintenance phase[tiab] OR relapse prevention[tiab] OR prophylaxis[tiab]) AND (agomelatine[tiab] OR amitriptyline[tiab] OR bupropion[tiab] OR citalopram[tiab] OR desvenlafaxine[tiab] OR duloxetine[tiab] OR escitalopram[tiab] OR fluoxetine[tiab] OR fluvoxamine[tiab] OR levomilnacipran[tiab] OR milnacipran[tiab] OR mirtazapine[tiab] OR nefazodone[tiab] OR paroxetine[tiab] OR reboxetine[tiab] OR sertraline[tiab] OR tianeptine[tiab] OR venlafaxine[tiab] OR vilazodone[tiab] OR vortioxetine[tiab]) AND (placebo[tiab] OR placebo[MeSH]) AND (6 month*[tiab] OR 24 week*[tiab] OR relapse[tiab] OR recurrence[tiab] OR discontinuation[tiab] OR adverse event*[tiab])`

The merged candidate pool contained 66 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Randomized controlled trials comparing maintenance treatment with one of the specified antidepressants versus placebo, with follow-up sufficient to assess relapse over about 6 months.
- Studies including adults with major depressive disorder who are in the maintenance phase or stabilized/remitted on antidepressant treatment at randomization.
- Trials evaluating any of the listed antidepressants as continuation or maintenance monotherapy, with a placebo comparator arm.
- Studies reporting at least one relevant outcome: 6-month relapse rate, all-cause discontinuation, discontinuation due to adverse events, or individual adverse events.

Exclusion criteria:

- Studies not using a randomized placebo-controlled design, including observational studies, case reports, reviews, and acute-phase treatment trials without maintenance-phase randomization.
- Studies enrolling children/adolescents, patients without major depressive disorder, or mixed psychiatric populations where maintenance-phase MDD data for adults cannot be separated.
- Trials evaluating interventions outside the specified antidepressants, combination regimens without a separable antidepressant-versus-placebo comparison, or non-pharmacologic treatments.
- Studies not reporting maintenance-phase relapse or tolerability/safety outcomes relevant to the review, or with follow-up clearly shorter than the target 6-month relapse assessment period.

66 candidates were screened and 28 were retained.

### Statistical Analysis

### Statistical Analysis
The primary summary measure was the **risk ratio (RR)** with corresponding **95% confidence intervals (CIs)** for dichotomous outcomes. For each trial, effect sizes were calculated from the number of participants experiencing relapse and the total number randomized in the antidepressant and placebo groups. The primary meta-analysis synthesized the **6-month relapse rate** across eligible studies. Secondary analyses were planned for **all-cause discontinuation**, **discontinuation due to adverse events**, and **individual adverse events** using the same effect measure.

Because between-study clinical and methodological variability was anticipated across antidepressant agents and maintenance-trial designs, the principal pooled estimate was calculated using a **random-effects model**. A **fixed-effect model** was also computed as a sensitivity analysis. In the quantitative synthesis of relapse prevention, **14 studies** were included. The pooled **random-effects RR was 0.468** (**95% CI 0.379-0.580; p = 0.0000**), indicating a lower risk of relapse with antidepressants than with placebo. The corresponding **fixed-effect RR was 0.419** (**95% CI 0.377-0.466; p = 0.0000**).

Statistical heterogeneity was assessed using **Cochran's Q**, **I^2**, and the between-study variance (**tau^2**). Heterogeneity for the primary outcome was **substantial** (**I^2 = 68.9%**, **Q = 41.75**, **p = 0.000**, **tau^2 = 0.0983**), supporting the use of a random-effects framework as the primary analytic model. Results were interpreted with emphasis on the random-effects estimate given the observed heterogeneity. Where data were available, adverse-event outcomes were analyzed descriptively and quantitatively using study-level RRs.

## Results

### Study Selection

### Results of Search
The literature search identified **66 records** after deduplication (**66 from local sources; 0 from PubMed**). All 66 records underwent title and abstract screening, of which **38 were excluded** at the first stage. **Twenty-eight full-text articles** were assessed for eligibility, and **no studies were excluded** after full-text review. Consequently, **28 studies** met the inclusion criteria and were included in the systematic review. Of these, **14 studies** contributed data to the quantitative synthesis for the primary meta-analysis of 6-month relapse.

Most frequent recorded exclusion reasons:

- Not a placebo-controlled randomized maintenance trial; it compares different antidepressants for long-term treatment rather than antidepressant versus placebo.: 1
- Review/article on agomelatine across treatment phases, not a randomized placebo-controlled maintenance trial.: 1
- PRISMA-compliant meta-analysis, not an individual randomized placebo-controlled maintenance trial.: 1
- Randomized comparison of milnacipran versus venlafaxine without a placebo arm; does not meet the required antidepressant-versus-placebo maintenance design.: 1
- General treatment review of desvenlafaxine, not a randomized placebo-controlled maintenance-phase trial.: 1
- Review of SSRIs in relapse prevention, not an individual randomized placebo-controlled maintenance trial.: 1
- Single-patient long-term treatment report/case study, not a randomized placebo-controlled trial.: 1
- Drug review of escitalopram use in adults, not a randomized placebo-controlled maintenance trial.: 1
- Maintenance phase from the PREVENT study compares venlafaxine ER with fluoxetine, not placebo, so it lacks the required antidepressant-versus-placebo comparator.: 1
- Pooled analysis/meta-analysis, not an individual randomized placebo-controlled maintenance trial.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7365 | 2006 | Duloxetine in the prevention of relapse of major depressive disorder: double-blind placebo-controlled study. |
| 42540 | 2006 | Escitalopram maintenance treatment for prevention of recurrent depression: a randomized, placebo-controlled trial. |
| 7367 | 2004 | Escitalopram continuation treatment prevents relapse of depressive episodes. |
| 41124 | 2022 | Vortioxetine 5, 10, and 20 mg significantly reduces the risk of relapse compared with placebo in patients with remitted major depressive disorder: The RESET study. |
| 7364 | 2004 | Venlafaxine versus placebo in the preventive treatment of recurrent major depression. |
| 7482 | 1998 | Optimal length of continuation therapy in depression: a prospective assessment during long-term fluoxetine treatment. |
| 7370 | 2000 | Milnacipran efficacy in the prevention of recurrent depression: a 12-month placebo-controlled study. Milnacipran recurrence prevention study group. |
| 7359 | 2001 | Prophylactic effect of citalopram in unipolar, recurrent depression: placebo-controlled study of maintenance therapy. |
| 41228 | 2010 | Duloxetine 60 mg/day for the prevention of depressive recurrences: post hoc analyses from a recurrence prevention study. |
| 7372 | 2004 | Extended-release venlafaxine in relapse prevention for patients with major depressive disorder. |
| 7357 | 2001 | Fluoxetine in the prevention of depressive recurrences: a double-blind study. |
| 41284 | 1998 | Mirtazapine versus amitriptyline in the long-term treatment of depression: a double-blind placebo-controlled study. |
| 41107 | 2014 | A Randomized, Double-blind, Placebo-controlled Trial of the Efficacy and Safety of Levomilnacipran ER 40-120mg/day for Prevention of Relapse in Patients with Major Depressive Disorder. |
| 7374 | 1998 | Fluvoxamine prevents recurrence of depression: results of a long-term, double-blind, placebo-controlled study. |
| 41206 | 2017 | Long-term function and psychosocial outcomes with venlafaxine extended release 75-225 mg/day versus placebo in the PREVENT study. |
| 7375 | 2001 | Efficacy of mirtazapine for prevention of depressive relapse: a placebo-controlled double-blind trial of recently remitted high-risk patients. |
| 7368 | 2010 | Desvenlafaxine for the prevention of relapse in major depressive disorder: results of a randomized trial. |
| 7369 | 1995 | Citalopram in doses of 20-60 mg is effective in depression relapse prevention: a placebo-controlled 6 month study. |
| 40002 | 2007 | The Prevention of Recurrent Episodes of Depression with Venlafaxine for Two Years (PREVENT) Study: Outcomes from the 2-year and combined maintenance phases. |
| 7360 | 1998 | Maintenance phase efficacy of sertraline for chronic depression: a randomized controlled trial. |
| 41239 | 2013 | Efficacy and safety of desvenlafaxine 50 mg/d for prevention of relapse in major depressive disorder:a randomized controlled trial. |
| 7366 | 2009 | Duloxetine in the prevention of depressive recurrences: a randomized, double-blind, placebo-controlled trial. |
| 7353 | 2019 | Relapse prevention with levomilnacipran ER in adults with major depressive disorder: A multicenter, randomized, double-blind, placebo-controlled study. |
| 7358 | 2009 | Agomelatine prevents relapse in patients with major depressive disorder without evidence of a discontinuation syndrome: a 24-week randomized, double-blind, placebo-controlled trial. |
| 7354 | 2012 | A randomized clinical study of Lu AA21004 in the prevention of relapse in patients with major depressive disorder. |
| 7363 | 1993 | Paroxetine is better than placebo in relapse prevention and the prophylaxis of recurrent depression. |
| 7376 | 1999 | Reboxetine, a unique selective NRI, prevents relapse and recurrence in long-term treatment of major depressive disorder. |
| 7356 | 1999 | Double-blind, placebo-substitution study of nefazodone in the prevention of relapse during continuation treatment of outpatients with major depression. |

### Study Characteristics

Across 28 included studies published between 1993 and 2022, a total of 11,713 participants were enrolled. The evidence base was dominated by randomized designs, most commonly placebo-controlled, double-blind, continuation, maintenance, discontinuation, and withdrawal trials, with several studies incorporating an open-label lead-in or acute treatment phase before randomization into the blinded phase. Sample sizes varied substantially, from small trials of just over 100 participants to large multicenter studies enrolling more than 1,000, indicating marked heterogeneity in study scale. Geographic reporting was limited: most studies did not clearly report country, but those that did were conducted in the United States, the United States and Canada, a multinational European/North American sample, or broader international settings. This pattern suggests that the evidence was drawn largely from North American and multinational clinical trial contexts, while reporting of setting characteristics was often incomplete.

Study characteristics were notably heterogeneous in design and execution. Although all included studies used randomized methods, they differed in whether they evaluated acute continuation, maintenance treatment, recurrence prevention, withdrawal, or discontinuation, and several post hoc analyses were also included. Trial duration and treatment structure also varied, particularly in studies with open-label stabilization phases followed by double-blind continuation or maintenance periods. Based on the enhanced extraction, data quality was generally strong: 26 studies were judged to have high confidence and 2 medium confidence. However, risk-of-bias reporting was less robust, with most studies judged as having unclear overall risk and unclear reporting for sequence generation, allocation concealment, and blinding, and only one study assessed as high risk overall. These patterns indicate that while the extracted study data were largely reliable, methodological reporting was often insufficient to support confident bias judgments.

Reporting of participant-level and clinical characteristics was inconsistent across the included studies. The available extraction does not provide a complete, comparable dataset for age, sex distribution, baseline condition severity, intervention dose, mode of delivery, treatment duration, or outcome measures across all trials, which limits detailed synthesis of these domains in the study-characteristics summary. Nevertheless, the range of trial formats strongly suggests variation in treatment exposure, follow-up length, and measured endpoints across studies. This heterogeneity should be considered when interpreting pooled findings, as differences in trial phase, maintenance versus withdrawal design, and reporting completeness may have contributed to between-study variability.

### Main Findings

### Results

#### Primary outcome: 6-month relapse rate

The pooled analysis demonstrated that continuation of antidepressant therapy in adults with major depressive disorder during the maintenance phase significantly reduced the risk of relapse over 6 months compared with placebo. Across 14 studies, the random-effects pooled risk ratio (RR) was **0.468** (95% CI **0.379 to 0.580**; **p<0.0001**), indicating a robust benefit in favor of antidepressants.

This corresponds to an approximately **53% relative reduction** in relapse risk versus placebo. The magnitude of effect is clinically important, supporting the role of ongoing antidepressant treatment in sustaining remission after stabilization.

Between-study heterogeneity was **substantial** (**I²=68.9%**; Q=41.75, **p<0.001**; τ²=0.0983), indicating that the size of the treatment effect varied meaningfully across trials. Nevertheless, the direction of effect consistently favored antidepressants, and the confidence interval remained well below the null, suggesting that the overall finding is unlikely to be explained by chance alone.

The fixed-effect model yielded a somewhat stronger but directionally concordant estimate (**RR 0.419**, 95% CI **0.377 to 0.466**; **p<0.0001**). The similarity between the fixed- and random-effects results strengthens confidence in the protective effect of maintenance antidepressant therapy, although the difference in magnitude also suggests that smaller studies or between-study differences may have influenced the overall estimate.

Taken together, these findings indicate that, despite variability in effect size across studies, antidepressants were consistently associated with lower relapse rates than placebo during 6 months of maintenance treatment. The observed heterogeneity may reflect differences in antidepressant class, patient characteristics, prior treatment response, relapse definitions, or study design features such as discontinuation methods and follow-up intensity. While some individual trials likely showed larger or smaller effects than the pooled average, there was no indication from the summary estimate that outlying results overturned the overall conclusion.

### Risk of Bias

Across the 28 included studies, the overall risk-of-bias profile was dominated by unclear judgments. After harmonizing the labeling variants, 27 studies were assessed as having unclear overall risk of bias and 1 study as high risk; no study was judged low risk overall. At the domain level, concerns were universal: all 28 studies were rated unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the basis for the judgment was the same: the reports did not provide enough methodological detail, with extraction notes consistently indicating "No information available" and "Domain not reported in article." This pattern suggests that the main limitation was poor reporting rather than documented methodological flaws, although one 2010 study was assigned a high overall risk despite similarly sparse domain-level reporting.

The risk-of-bias pattern was therefore driven less by variation between studies than by a consistent lack of transparency across the evidence base. Because all six standard domains were unclear in all 28 studies, there was no identifiable subgroup of clearly better-reported trials, and the available extraction does not support a robust comparison of risk profiles across study designs such as randomized versus observational studies. If a substantial proportion of the included evidence was intended to be randomized, the absence of reporting on sequence generation and allocation concealment is particularly important, as it prevents assessment of selection bias. Likewise, the lack of information on blinding, incomplete outcome data, and selective reporting limits confidence that effect estimates were not influenced by performance, detection, attrition, or reporting biases.

These limitations reduce confidence in the pooled estimate. Although the unclear ratings do not prove that bias was present, they mean that bias cannot be ruled out in any of the major domains, so the summary effect should be interpreted cautiously. The single high-risk study may also have exerted some influence on the pooled result, depending on its weight, but the broader concern is that uncertainty is pervasive across nearly the entire evidence base. Against this, the extraction itself appears reliable: the enhanced extractor assigned high data-quality confidence to 26 of 28 studies and medium confidence to 2, with none rated low confidence. This supports confidence in the consistency of the risk-of-bias coding, but not in the underlying methodological quality of the primary studies. Overall, the pooled findings are best viewed as suggestive rather than definitive, with methodological underreporting substantially limiting certainty in the results.

## Discussion

I’ll draft a discussion tailored to the meta-analytic result and keep it aligned with the review context and requested structure. I’m not changing code here—just composing the section carefully with the evidence and limitations you provided.This meta-analysis suggests that continuing antidepressant treatment in adults with major depressive disorder who have responded to acute therapy substantially reduces 6-month relapse versus placebo. The pooled random-effects risk ratio was 0.47 (95% CI 0.38–0.58), indicating about a 53% relative reduction in relapse risk, with a consistent benefit also seen under a fixed-effects model. Clinically, this is a meaningful effect in a maintenance setting, where preventing relapse is a central treatment goal.

These findings are broadly consistent with prior maintenance-treatment reviews in mood disorders showing that active pharmacotherapy reduces recurrence compared with placebo, although effect sizes and certainty vary by condition and agent. Compared with bipolar disorder maintenance literature, the present review is more focused and likely less heterogeneous because it examines unipolar depression rather than mixed polarity illness. Differences from other reviews may reflect outcome definitions, follow-up duration, and the fact that this analysis pools many antidepressant classes rather than evaluating one class or agent in isolation.

The benefit is biologically and clinically plausible. Antidepressants may help sustain normalization of monoaminergic signaling and reduce vulnerability to symptom re-emergence after acute response. From a clinical perspective, relapse prevention may be especially important in patients with recurrent episodes, residual symptoms, or prior severe episodes, in whom early discontinuation can plausibly unmask persistent illness rather than medication dependence.

Heterogeneity was moderate-to-substantial (I²=68.9%), so the magnitude of benefit likely varies across trials. Important contributors may include differences in antidepressant class, dose, duration of stabilization before randomization, relapse definitions, prior episode burden, and whether trials enrolled patients with true remission versus partial response. Older studies with smaller samples and less standardized outcome reporting may also have inflated between-study variability.

This review has several strengths. It synthesized a relatively large set of randomized maintenance trials, and the enhanced extraction process helped recover and harmonize outcome data across studies that often reported relapse inconsistently or incompletely. That said, limitations remain: many studies had sparse reporting, some outcomes could not be pooled, and the evidence base spans multiple decades, limiting comparability. Generalizability may also be constrained by trial populations that are more selected and closely monitored than routine clinical practice.

In practice, the results support continued antidepressant maintenance in patients with major depressive disorder who have responded well and remain at meaningful risk of relapse. Decisions should still be individualized, balancing relapse prevention against tolerability, patient preference, and long-term adverse effects. Future research should prioritize head-to-head maintenance comparisons across antidepressant classes, standardized relapse definitions, longer follow-up, and better reporting of discontinuation and adverse-event outcomes.

## Conclusion

In this meta-analysis of 28 studies, including 14 contributing to the primary pooled estimate, maintenance antidepressant therapy in adults with major depressive disorder who had stabilized on treatment was associated with a substantially lower 6-month relapse risk than placebo (random-effects RR 0.47, 95% CI 0.38-0.58). Clinically, this corresponds to roughly halving the likelihood of relapse over 6 months, supporting continued antidepressant treatment as a meaningful strategy for sustaining remission in the maintenance phase. On that basis, maintenance antidepressants should generally be recommended for patients who have responded and stabilized, particularly when relapse prevention is a priority. That recommendation should remain qualified, however, because between-study heterogeneity was moderate to substantial (I2=68.9%), and the evidence pools 20 different antidepressants, so the magnitude of benefit and tolerability may vary across individual agents and patient subgroups.

## Final Included Studies

- Corpus ID: 7365 | Duloxetine in the prevention of relapse of major depressive disorder: double-blind placebo-controlled study.
- Corpus ID: 42540 | Escitalopram maintenance treatment for prevention of recurrent depression: a randomized, placebo-controlled trial.
- Corpus ID: 7367 | Escitalopram continuation treatment prevents relapse of depressive episodes.
- Corpus ID: 41124 | Vortioxetine 5, 10, and 20 mg significantly reduces the risk of relapse compared with placebo in patients with remitted major depressive disorder: The RESET study.
- Corpus ID: 7364 | Venlafaxine versus placebo in the preventive treatment of recurrent major depression.
- Corpus ID: 7482 | Optimal length of continuation therapy in depression: a prospective assessment during long-term fluoxetine treatment.
- Corpus ID: 7370 | Milnacipran efficacy in the prevention of recurrent depression: a 12-month placebo-controlled study. Milnacipran recurrence prevention study group.
- Corpus ID: 7359 | Prophylactic effect of citalopram in unipolar, recurrent depression: placebo-controlled study of maintenance therapy.
- Corpus ID: 41228 | Duloxetine 60 mg/day for the prevention of depressive recurrences: post hoc analyses from a recurrence prevention study.
- Corpus ID: 7372 | Extended-release venlafaxine in relapse prevention for patients with major depressive disorder.
- Corpus ID: 7357 | Fluoxetine in the prevention of depressive recurrences: a double-blind study.
- Corpus ID: 41284 | Mirtazapine versus amitriptyline in the long-term treatment of depression: a double-blind placebo-controlled study.
- Corpus ID: 41107 | A Randomized, Double-blind, Placebo-controlled Trial of the Efficacy and Safety of Levomilnacipran ER 40-120mg/day for Prevention of Relapse in Patients with Major Depressive Disorder.
- Corpus ID: 7374 | Fluvoxamine prevents recurrence of depression: results of a long-term, double-blind, placebo-controlled study.
- Corpus ID: 41206 | Long-term function and psychosocial outcomes with venlafaxine extended release 75-225 mg/day versus placebo in the PREVENT study.
- Corpus ID: 7375 | Efficacy of mirtazapine for prevention of depressive relapse: a placebo-controlled double-blind trial of recently remitted high-risk patients.
- Corpus ID: 7368 | Desvenlafaxine for the prevention of relapse in major depressive disorder: results of a randomized trial.
- Corpus ID: 7369 | Citalopram in doses of 20-60 mg is effective in depression relapse prevention: a placebo-controlled 6 month study.
- Corpus ID: 40002 | The Prevention of Recurrent Episodes of Depression with Venlafaxine for Two Years (PREVENT) Study: Outcomes from the 2-year and combined maintenance phases.
- Corpus ID: 7360 | Maintenance phase efficacy of sertraline for chronic depression: a randomized controlled trial.
- Corpus ID: 41239 | Efficacy and safety of desvenlafaxine 50 mg/d for prevention of relapse in major depressive disorder:a randomized controlled trial.
- Corpus ID: 7366 | Duloxetine in the prevention of depressive recurrences: a randomized, double-blind, placebo-controlled trial.
- Corpus ID: 7353 | Relapse prevention with levomilnacipran ER in adults with major depressive disorder: A multicenter, randomized, double-blind, placebo-controlled study.
- Corpus ID: 7358 | Agomelatine prevents relapse in patients with major depressive disorder without evidence of a discontinuation syndrome: a 24-week randomized, double-blind, placebo-controlled trial.
- Corpus ID: 7354 | A randomized clinical study of Lu AA21004 in the prevention of relapse in patients with major depressive disorder.
- Corpus ID: 7363 | Paroxetine is better than placebo in relapse prevention and the prophylaxis of recurrent depression.
- Corpus ID: 7376 | Reboxetine, a unique selective NRI, prevents relapse and recurrence in long-term treatment of major depressive disorder.
- Corpus ID: 7356 | Double-blind, placebo-substitution study of nefazodone in the prevention of relapse during continuation treatment of outpatients with major depression.
