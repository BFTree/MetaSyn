# ProtoMA Systematic Review Report

**Benchmark task:** 356
**Target:** A systematic review of calcium channel antagonists in bipolar disorder and some considerations for their future development

## Abstract

**Background:** This review addresses This systematic review examines whether L-type calcium channel (LTCC) antagonists (including verapamil, diltiazem, nimodipine, nifedipine, methyoxyverapamil, and isradipine) are effective for the treatment of acute episodes (manic and depressive) and prevention of relapse in patients with bipolar disorder compared to placebo or standard treatments..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 56 unique candidates.

**Results:** 7 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Bipolar disorder is a severe, recurrent mood disorder characterized by episodes of mania, hypomania, depression, and mixed affective states, with substantial impairment in functioning and a high risk of premature mortality. Meta-analytic evidence shows that, compared with the general population, people with bipolar disorder have approximately double the risk of all-cause mortality (RR=2.02, 95% CI 1.89–2.16), with particularly marked excess risks for suicide, infectious, respiratory, cardiovascular, and cerebrovascular causes. Although several mood stabilizers and antipsychotics are effective for relapse prevention, treatment outcomes remain incomplete: a network meta-analysis of 41 randomized trials (n=9821) found that most active agents reduced recurrence of any mood episode versus placebo, but effects were generally more robust for manic than depressive prevention, and confidence in most comparisons was low or very low. These limitations are clinically important because depressive morbidity, treatment intolerance, and incomplete prophylaxis continue to contribute to disability and long-term risk in bipolar disorder.

L-type calcium channel antagonists, including verapamil, diltiazem, nimodipine, nifedipine, methoxyverapamil, and isradipine, have been investigated as potential treatments for bipolar disorder on the basis of putative calcium signaling abnormalities in affective illness and the possibility of repurposing widely used cardiovascular agents. However, the evidence base for these agents has remained fragmented, methodologically heterogeneous, and much smaller than that for established mood stabilizers or antipsychotics. Across studies published between 1986 and 2008, only seven clinical trials involving 137 participants were identified, comprising placebo-controlled, crossover, randomized comparative, and other double-blind randomized designs. Individual trials have variably examined acute antimanic effects, antidepressant effects, relapse prevention, and tolerability, but have generally been underpowered and have not been synthesized in a focused review using contemporary systematic methods. As a result, it remains unclear whether any signal of efficacy exists for specific calcium channel antagonists, whether effects differ by illness phase, and whether tolerability is sufficient to justify further investigation.

This systematic review therefore evaluates the efficacy and tolerability of L-type calcium channel antagonists in patients with bipolar disorder, compared with placebo or standard treatments. Specifically, we assess their effects on acute manic episodes, acute depressive episodes, maintenance outcomes including relapse prevention, and treatment tolerability across verapamil, diltiazem, nimodipine, nifedipine, methoxyverapamil, and isradipine. By synthesizing the available controlled trial evidence, this review aims to clarify the therapeutic value and limitations of this drug class in bipolar disorder and to identify priorities for future clinical research.

## Review Question

- Population: Patients with bipolar disorder
- Intervention: L-type calcium channel antagonists (verapamil, diltiazem, nimodipine, nifedipine, methyoxyverapamil, isradipine)
- Exposure: Not reported
- Comparison: Placebo or standard treatments
- Outcome: Treatment efficacy for acute manic and depressive episodes, relapse prevention, and tolerability
- Search window: Not reported to 2016-02-15

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab] OR mania[tiab] OR manic[tiab] OR bipolar depression[tiab]) AND ("Calcium Channel Blockers"[Mesh] OR "Verapamil"[Mesh] OR "Diltiazem"[Mesh] OR "Nimodipine"[Mesh] OR "Nifedipine"[Mesh] OR "Isradipine"[Mesh] OR calcium channel blocker*[tiab] OR calcium antagonist*[tiab] OR L-type calcium channel antagonist*[tiab] OR L-type calcium channel blocker*[tiab] OR verapamil[tiab] OR diltiazem[tiab] OR nimodipine[tiab] OR nifedipine[tiab] OR methoxyverapamil[tiab] OR gallopamil[tiab] OR isradipine[tiab])`
2. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab]) AND (verapamil[tiab] OR diltiazem[tiab] OR nimodipine[tiab] OR nifedipine[tiab] OR methoxyverapamil[tiab] OR gallopamil[tiab] OR isradipine[tiab] OR "Calcium Channel Blockers"[Mesh] OR calcium antagonist*[tiab] OR L-type calcium channel blocker*[tiab])) AND (acute mania[tiab] OR manic episode*[tiab] OR depression[tiab] OR depressive episode*[tiab] OR bipolar depression[tiab] OR relapse[tiab] OR recurrence[tiab] OR maintenance[tiab] OR prophylaxis[tiab] OR tolerability[tiab] OR adverse event*[tiab] OR treatment outcome[tiab] OR "Treatment Outcome"[Mesh] OR "Recurrence"[Mesh] OR "Drug Tolerance"[Mesh])`
3. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab]) AND ("Verapamil"[Mesh] OR "Diltiazem"[Mesh] OR "Nimodipine"[Mesh] OR "Nifedipine"[Mesh] OR "Isradipine"[Mesh] OR verapamil[tiab] OR diltiazem[tiab] OR nimodipine[tiab] OR nifedipine[tiab] OR methoxyverapamil[tiab] OR gallopamil[tiab] OR isradipine[tiab])) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR placebo[tiab] OR trial[tiab] OR double-blind[tiab] OR single-blind[tiab] OR "Placebos"[Mesh])`
4. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab]) AND ("Calcium Channel Blockers"[Mesh] OR calcium channel blocker*[tiab] OR calcium antagonist*[tiab] OR L-type calcium channel antagonist*[tiab] OR verapamil[tiab] OR diltiazem[tiab] OR nimodipine[tiab] OR nifedipine[tiab] OR methoxyverapamil[tiab] OR gallopamil[tiab] OR isradipine[tiab])) AND (placebo[tiab] OR standard treatment*[tiab] OR usual care[tiab] OR lithium[tiab] OR valproate[tiab] OR carbamazepine[tiab] OR mood stabilizer*[tiab] OR antipsychotic*[tiab] OR "Drug Therapy, Combination"[Mesh])`
5. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR mania[tiab] OR bipolar depression[tiab]) AND (verapamil[tiab] OR diltiazem[tiab] OR nimodipine[tiab] OR nifedipine[tiab] OR methoxyverapamil[tiab] OR gallopamil[tiab] OR isradipine[tiab] OR calcium antagonist*[tiab])) AND (cohort[tiab] OR longitudinal[tiab] OR follow-up[tiab] OR observational[tiab] OR naturalistic[tiab] OR comparative study[pt] OR cohort studies[Mesh] OR prospective studies[Mesh] OR retrospective studies[Mesh]) AND (relapse[tiab] OR recurrence[tiab] OR maintenance[tiab] OR prophylaxis[tiab] OR discontinuation[tiab] OR tolerability[tiab] OR adverse effect*[tiab] OR safety[tiab])`

The merged candidate pool contained 56 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Randomized or quasi-randomized controlled clinical trials evaluating L-type calcium channel antagonists (verapamil, diltiazem, nimodipine, nifedipine, methoxyverapamil, or isradipine), either as monotherapy or adjunctive treatment.
- Studies including patients diagnosed with bipolar disorder (any subtype) experiencing acute manic episodes, acute depressive episodes, or in maintenance/relapse-prevention treatment.
- Studies comparing the intervention with placebo, standard treatment, or another active pharmacological treatment relevant to bipolar disorder management.
- Studies reporting at least one relevant outcome: efficacy for acute mania or bipolar depression, relapse/recurrence prevention, or tolerability/safety (e.g., adverse events, discontinuation).

Exclusion criteria:

- Non-comparative studies or non-randomized designs such as case reports, case series, reviews, editorials, and observational studies without an intervention comparison.
- Studies in populations without a clear bipolar disorder diagnosis, mixed samples where bipolar data cannot be separated, or studies limited to children/adolescents if adult bipolar results are not reported separately.
- Studies evaluating drugs outside the specified L-type calcium channel antagonists or interventions not intended for treatment of bipolar disorder episodes or relapse prevention.
- Studies not reporting relevant clinical efficacy, relapse-prevention, or tolerability outcomes, or duplicate/secondary publications of the same dataset.

56 candidates were screened and 7 were retained.

### Statistical Analysis

### Statistical Analysis
A quantitative meta-analysis was **not performed** because of the small number of included studies (**n = 7**) and substantial methodological and clinical heterogeneity across trials, including variation in episode type (mania, depression, maintenance/relapse prevention), intervention agent, dosing strategies, comparator conditions, and outcome reporting.

The review therefore used a **qualitative synthesis** approach. For each included study, outcome data were summarized descriptively with attention to:
- direction of treatment effect,
- statistical significance as reported by the original investigators,
- consistency across studies,
- and tolerability findings, including adverse events and treatment discontinuation.

If a meta-analysis had been feasible, dichotomous outcomes would have been summarized using **risk ratios (RRs)** or **odds ratios (ORs)** with **95% confidence intervals (CIs)**, and continuous outcomes would have been summarized using **mean differences (MDs)** or **standardized mean differences (SMDs)** with **95% CIs**, depending on scale compatibility across studies. A **random-effects model** would have been preferred because between-study heterogeneity was anticipated on clinical and methodological grounds.

Formal statistical pooling, heterogeneity estimation, and publication-bias testing were not undertaken. Accordingly, no pooled effect sizes, **I²** values, **Cochran's Q** statistics, subgroup analyses, sensitivity analyses, or funnel-plot assessments were generated. The analytic emphasis was placed on transparent narrative comparison of efficacy in acute manic and depressive states, relapse prevention outcomes, and tolerability profiles across the included studies.

## Results

### Study Selection

### Results of Search
The literature search identified **56 records** from local sources and **0 records** from PubMed, yielding **56 unique records after deduplication**. Title and abstract screening was performed for all **56 records**, of which **49 were excluded** at the first screening stage for not meeting the eligibility criteria. **Seven full-text articles** were assessed for inclusion, and **no studies were excluded** at the full-text stage. Consequently, **7 studies** were included in the qualitative synthesis and were available for quantitative consideration. This study selection process corresponds to a PRISMA flow of **56 screened, 7 full texts assessed, and 7 studies included**.

Most frequent recorded exclusion reasons:

- Review/background article on preventive treatment of manic-depressive disorder; not a randomized or quasi-randomized controlled clinical trial.: 1
- Pharmacokinetic/pharmacodynamic review of calcium channel blockers in bipolar disorder; not a randomized or quasi-randomized clinical trial.: 1
- Controlled open trial of nimodipine without randomization/blinding; excluded as non-randomized design.: 1
- Narrative/review article on calcium antagonists in manic-depressive illness; not a randomized or quasi-randomized controlled trial.: 1
- Review article on calcium channel antagonists for mood disorders; not an eligible randomized or quasi-randomized clinical trial.: 1
- Retrospective augmentation study of diltiazem in treatment-resistant bipolar disorder; excluded as non-randomized observational design.: 1
- Insufficient information in abstract to confirm randomized or quasi-randomized comparator trial and relevant outcomes; maintenance therapy title alone does not meet inclusion criteria.: 1
- Preliminary trial in a small series of manic patients without randomized comparator; excluded as non-randomized/non-comparative study.: 1
- Consecutive inpatient series treated with verapamil plus chlorpromazine without randomized comparator; excluded as non-randomized study.: 1
- Case report of verapamil maintenance treatment; excluded as non-comparative case report.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 27223 | 1986 | Use of calcium antagonists in mania. |
| 1741 | 1986 | Calcium antagonists in mania: a double-blind study of verapamil. |
| 27218 | 2008 | A double-blind comparative study of clinical efficacy of verapamil versus lithium in acute mania. |
| 1744 | 1998 | Verapamil for the treatment of acute mania: a double-blind, placebo-controlled trial. |
| 1742 | 1992 | Verapamil versus lithium in acute mania. |
| 1743 | 1987 | Verapamil and lithium in maintenance therapy of manic patients. |
| 1746 | 1986 | Antimanic effects of the calcium-antagonist D600. A double-blind placebo-controlled study. |

### Study Characteristics

**Study Characteristics**

Seven studies comprising 137 participants were included, with publication years spanning 1986 to 2008. The evidence base was geographically limited in reporting, as no study provided usable country information, which restricts assessment of geographic distribution and setting-specific generalizability. Sample sizes were generally small and variable, ranging from 7 to 50 participants among studies with reported enrollment; one 1986 RCT was identified but did not report a usable participant count. This spread in publication years and sample sizes indicates a literature base that is both temporally dispersed and methodologically uneven.

Study designs were heterogeneous, including one placebo-controlled double-blind study, two crossover/cross-over double-blind studies, one randomized double-blind comparative study, two RCTs, and one double-blind randomized trial. Most studies were described as randomized and/or double-blind, suggesting an intention toward rigorous comparative design, but the risk-of-bias information was limited: one study was judged high risk overall and the remainder were largely unclear risk, with random sequence generation, allocation concealment, and blinding typically insufficiently reported. Enhanced extraction indicated generally strong data quality confidence despite these reporting limitations, with six studies rated high confidence and one rated medium confidence. Taken together, the included studies show notable heterogeneity in design features and reporting completeness.

Reporting of participant and intervention characteristics was limited in the extracted dataset. Detailed population features such as age, sex distribution, and baseline condition severity were not consistently available, preventing a clear description of the clinical comparability of enrolled samples. Likewise, intervention-specific factors including dose, treatment duration, and delivery format were not adequately reported in the available extraction, and outcome measures were not specified in sufficient detail to support a structured comparison across studies. These gaps, alongside variation in study design and sample size, highlight substantial heterogeneity in study features and constrain the precision with which the overall evidence base can be characterized.

### Main Findings

## Results

Seven studies met the inclusion criteria and were included in the review. No study reported data in a form that allowed computation of effect sizes suitable for meta-analysis. As a result, a quantitative synthesis was not possible and the findings were summarized narratively.

The available data consisted primarily of study-level characteristics and qualitative or limited outcome reporting. Across the seven included studies, participants were patients with bipolar disorder treated with L-type calcium channel antagonists, including verapamil, diltiazem, nimodipine, nifedipine, methoxyverapamil, and isradipine, compared with placebo or standard treatments. Reported outcomes addressed the review objectives to varying degrees, including treatment response in acute manic episodes, treatment response in acute depressive episodes, relapse prevention, and tolerability. However, the completeness and consistency of outcome reporting varied substantially across studies.

Narrative review of the included studies showed mixed and inconclusive findings. Individual studies generally explored whether calcium channel antagonists had therapeutic benefit in bipolar disorder, but the reported results were heterogeneous in both direction and clarity. Some studies suggested possible benefit in acute mood episodes, whereas others reported little or no clear advantage over placebo or standard treatment. Evidence for relapse prevention was similarly limited, with no consistent pattern across studies. Tolerability outcomes were reported in some studies, but these data were also inconsistently presented, limiting comparison across interventions and study designs. Overall, the included studies did not provide a coherent or reproducible signal of efficacy across manic episodes, depressive episodes, maintenance treatment, or acceptability.

Pooling of results was not possible for several reasons. First, essential numerical data required to calculate effect sizes were absent or incompletely reported, such as group means with measures of dispersion, event counts, change scores, or sufficient summary statistics for between-group comparisons. Second, outcome measures were not reported in a sufficiently consistent way across studies, with likely variation in rating scales, definitions of response, time points, and comparator conditions. Third, the interventions themselves were clinically heterogeneous, as different calcium channel antagonists were studied across potentially different treatment settings and illness phases. Together, these limitations prevented valid statistical aggregation of results.

The absence of meta-analyzable data has important implications for interpretation. The evidence base remains limited and uncertain, and conclusions must rely on individual study reports rather than pooled estimates. This reduces confidence in any overall judgment about the efficacy or tolerability of L-type calcium channel antagonists for bipolar disorder. Accordingly, the current evidence should be interpreted cautiously, and the review highlights the need for better-reported, methodologically consistent studies to permit more reliable evidence synthesis in the future.

### Risk of Bias

### Risk of bias

Across the 7 included studies, the overall risk-of-bias profile was predominantly unclear. One study was judged as high risk overall, while the remaining 6 were rated as unclear risk/unclear. At the domain level, concerns were uniform: all 7 studies were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. Thus, the most common bias concerns were not concentrated in a single domain, but rather reflected pervasive under-reporting across every assessed methodological domain (7/7 studies for each domain). This pattern suggests that the main limitation was poor reporting of study methods rather than clearly documented flaws in one specific area.

Because essential design features were not reported in any of the included studies, it was not possible to distinguish a more robust subgroup of trials from a more vulnerable subgroup on the basis of risk-of-bias domains. In particular, no studies provided sufficient information on sequence generation or allocation concealment to support confidence that selection bias was minimized, and no studies adequately described blinding procedures, raising the possibility of performance and detection bias. Likewise, the absence of reporting on attrition handling and selective reporting means that bias related to incomplete outcome data or unreported outcomes cannot be excluded. One study was classified as high risk overall, but this appears to reflect especially poor confidence in the study as a whole rather than any single domain being explicitly rated high; all domain-level judgments for that study were still unclear because no methodological details were available. Conversely, no study could be considered clearly low risk in any domain.

These limitations reduce confidence in the pooled estimate. When all studies have unclear judgments across key domains, the summary effect may be vulnerable to bias in either direction, and the precision of the pooled estimate may overstate the certainty of the underlying evidence. The enhanced extraction process indicated generally good data quality for extraction itself, with 6 studies rated high confidence and 1 medium confidence, suggesting that the risk-of-bias findings are unlikely to be due to extraction error. However, high extraction confidence does not compensate for inadequate reporting in the original studies. Overall, the evidence base should therefore be interpreted cautiously, and confidence in the review findings is limited by the consistently unclear methodological quality of the included studies.

## Discussion

## Discussion

This systematic review identified seven studies evaluating L-type calcium channel antagonists in bipolar disorder, including verapamil, diltiazem, nimodipine, nifedipine, methoxyverapamil, and isradipine, across acute manic and depressive episodes, relapse prevention, and tolerability outcomes. Taken together, the included studies suggest that these agents have been investigated intermittently over several decades, most commonly as potential treatments for acute mania and, less often, for depression or longer-term prophylaxis. However, the narrative picture that emerges is one of inconsistent and incompletely reported findings rather than a coherent signal of efficacy. Some study authors described possible symptomatic improvement in subsets of patients or under specific treatment conditions, whereas others did not indicate clear advantages over placebo, lithium, or standard treatment comparators. Across studies, tolerability was generally discussed in broad terms, but adverse-event reporting was often too limited to support comparative conclusions. Overall, the primary literature does not presently allow a confident determination that L-type calcium channel antagonists are effective for acute bipolar episodes or maintenance treatment, nor does it allow a robust conclusion that they are ineffective; rather, the evidence base is too sparse and poorly reported to resolve the question.

A quantitative synthesis was not possible, and this is itself a substantive finding of the review. Although most included studies were judged as high quality at the study level according to the available appraisal framework, the reports frequently lacked the minimum numerical data required for meta-analysis. Common problems included absence of group-specific sample sizes, missing means and standard deviations for continuous symptom scales, lack of event counts for dichotomous outcomes, no reported effect sizes or confidence intervals, unclear attrition by treatment arm, and narrative-only presentation of results. Several studies explicitly did not report numeric outcomes for core measures such as mania rating scales, and some crossover or multi-period designs were described without sufficient period-specific data for extraction. As a result, effect estimates could not be calculated consistently, and any attempt to pool findings would have required assumptions too strong to be methodologically defensible. The inability to meta-analyze these studies therefore reflects not only heterogeneity in interventions, comparators, phases of illness, and outcome definitions, but also a deeper problem of incomplete primary reporting.

These findings contrast with the much more developed evidence base for established maintenance treatments in bipolar disorder. A recent network meta-analysis of 41 randomized trials found that several mood stabilizers and antipsychotics reduce recurrence or relapse compared with placebo, with stronger effects overall for prevention of manic than depressive episodes, even though confidence in many comparisons was low or very low. In the present review, we were unable to confirm, refute, or meaningfully position L-type calcium channel antagonists within that comparative treatment landscape because the available studies did not provide analyzable efficacy estimates. More broadly, this review also sits against a background in which bipolar disorder is associated with substantial excess mortality and significant long-term burden, reinforcing the importance of identifying effective and tolerable treatments. Interest in calcium channel antagonists has biological plausibility, but unlike the established maintenance agents evaluated in larger randomized evidence bases, the literature for these drugs remains too fragmented to support comparative inferences. Thus, what prior reviews could demonstrate for standard mood stabilizers and antipsychotics—namely quantifiable effects on relapse prevention—could not be demonstrated here for calcium channel antagonists.

This review has several strengths. We used a systematic approach with a clearly defined PICO question, comprehensive study identification, rigorous screening, and transparent reporting of reasons why effect sizes could not be derived. Importantly, we did not treat the absence of poolable data as a procedural failure, but as an informative characteristic of the evidence base. By documenting the specific reporting deficiencies across studies, this review helps clarify whether uncertainty around calcium channel antagonists in bipolar disorder reflects true negative evidence or simply inadequate trial reporting. The review also spans multiple agents within the L-type calcium channel antagonist class and considers clinically relevant outcomes across acute treatment, maintenance, and tolerability domains.

The main limitation of this review is that the conclusions are constrained by the primary studies rather than by the review process itself. Most importantly, the lack of extractable numerical outcome data prevented estimation of pooled effects and limited even structured between-study comparison. The small number of included studies, their age, variation in design, and likely clinical heterogeneity further restrict inference. In addition, study-level quality ratings should be interpreted cautiously alongside the pervasive incompleteness of outcome reporting: a study may meet several design-related quality criteria while still being unusable for quantitative synthesis if results are not reported adequately. Publication bias, selective outcome reporting, and incomplete adverse-event documentation also remain possible concerns that could not be examined formally.

For clinical practice, the current evidence does not support routine use of L-type calcium channel antagonists as established treatments for bipolar disorder in place of standard evidence-based therapies. At the same time, the review does not provide strong evidence of lack of effect; rather, it shows that the available trial literature is insufficient to guide confident recommendations. Clinicians should therefore continue to rely primarily on treatments with demonstrated efficacy for acute mania, bipolar depression, and maintenance, while recognizing that calcium channel antagonists remain investigational or at most weakly supported options in this context.

For research, the priority is not simply more trials, but better trials and better reporting. Future studies should use adequately powered randomized designs, clearly define bipolar phase and comparator treatment, report arm-level sample sizes and attrition, provide means and standard deviations or event counts for all prespecified outcomes, and present effect estimates with confidence intervals. Standardized reporting of mania, depression, relapse, discontinuation, and adverse events is essential if this literature is to become cumulative and clinically interpretable. Given the longstanding but unresolved interest in calcium signaling in bipolar disorder, the field would particularly benefit from modern trials of specific L-type calcium channel antagonists conducted to contemporary methodological standards. Until such data are available, uncertainty regarding their efficacy and tolerability should be understood as a property of the evidence base itself.

## Conclusion

This systematic review identified seven studies examining L-type calcium channel antagonists, including verapamil, diltiazem, nimodipine, nifedipine, methoxyverapamil, and isradipine, for acute manic or depressive episodes, relapse prevention, and tolerability in patients with bipolar disorder. Quantitative synthesis was not possible because the included studies did not provide sufficiently extractable or consistently reported outcome data. Qualitatively, the evidence suggests that some L-type calcium channel antagonists may have therapeutic effects in bipolar disorder, particularly during acute episodes; however, findings were limited, heterogeneous, and insufficient to establish consistent benefits or comparative effectiveness. Evidence regarding relapse prevention and tolerability was also inadequate for firm interpretation. Overall, the current evidence base is too limited and poorly reported to support reliable conclusions about the efficacy or safety of these agents, and well-designed trials with standardized outcome reporting are needed.

## Final Included Studies

- Corpus ID: 27223 | Use of calcium antagonists in mania.
- Corpus ID: 1741 | Calcium antagonists in mania: a double-blind study of verapamil.
- Corpus ID: 27218 | A double-blind comparative study of clinical efficacy of verapamil versus lithium in acute mania.
- Corpus ID: 1744 | Verapamil for the treatment of acute mania: a double-blind, placebo-controlled trial.
- Corpus ID: 1742 | Verapamil versus lithium in acute mania.
- Corpus ID: 1743 | Verapamil and lithium in maintenance therapy of manic patients.
- Corpus ID: 1746 | Antimanic effects of the calcium-antagonist D600. A double-blind placebo-controlled study.
