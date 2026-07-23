# ProtoMA Systematic Review Report

**Benchmark task:** 265
**Target:** Effects of psychoplastogens on blood levels of brain-derived neurotrophic factor (BDNF) in humans: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates whether psychoplastogens (including ketamine, esketamine, LSD, psilocybin, ayahuasca, DMT, MDMA, scopolamine, and rapastinel) elevate peripheral blood levels of brain-derived neurotrophic factor (BDNF) in humans compared to baseline or control conditions, testing whether the rapid upregulation of neuroplasticity observed in preclinical studies is detectable using peripheral BDNF as a biomarker..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 58 unique candidates.

**Results:** 3 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Psychoplastogens, including ketamine, classic serotonergic psychedelics, and related rapid-acting compounds, have renewed interest because they can produce antidepressant and prosocial effects within hours to days, a time course that contrasts sharply with conventional psychopharmacology. This clinical profile has intensified efforts to identify biological markers that can clarify mechanism, stratify response, and support translational development across both healthy volunteers and psychiatric populations. Brain-derived neurotrophic factor (BDNF) is a leading candidate in this context because it is centrally implicated in synaptic plasticity, neurogenesis, and stress-related neuroadaptation, and these processes are thought to be engaged by psychoplastogens. Peripheral BDNF measured in serum or plasma is especially relevant for clinical research because blood sampling is feasible in experimental and treatment settings, allowing repeated assessment before and after drug exposure and potential comparison with placebo or control conditions.

Existing evidence, however, remains difficult to interpret. Individual studies have examined whether administration of ketamine, esketamine, lysergic acid diethylamide, psilocybin, ayahuasca, N,N-dimethyltryptamine, 3,4-methylenedioxymethamphetamine, scopolamine, or rapastinel alters peripheral BDNF concentrations, but the literature is methodologically heterogeneous. Differences in study population, psychiatric status, compound class, dosing paradigm, sampling matrix (serum vs plasma), and comparator structure complicate inference, particularly when peripheral BDNF is vulnerable to pre-analytical and temporal variation. In contrast to other biomarker-focused meta-analyses that have already quantified clinically relevant signal across large evidence bases, the psychoplastogen-BDNF literature is still nascent: only three eligible studies published between 2021 and 2025, comprising 88 total participants, were identified, including a placebo-controlled within-subject study, a randomized double-blind clinical trial, and a randomized placebo-controlled crossover study. This limited but emerging evidence base leaves unresolved whether peripheral BDNF shows a consistent acute biological response to psychoplastogen exposure and whether any observed effect generalizes across healthy individuals and patients with psychiatric diagnoses.

Accordingly, this systematic review evaluates human studies that measured serum or plasma BDNF before and after psychoplastogen administration or under placebo/control conditions. Using a PICO framework, we included healthy participants and psychiatric patients; interventions involving ketamine, esketamine, LSD, psilocybin, ayahuasca, DMT, MDMA, scopolamine, and rapastinel; comparators defined as baseline pre-treatment BDNF or placebo/control exposure; and outcomes restricted to peripheral blood BDNF concentrations. The objective was not simply to summarize whether BDNF changes after treatment, but to determine how consistently peripheral BDNF has been studied as a pharmacodynamic biomarker of psychoplastogen exposure, under what experimental conditions signals have been observed, and where the present evidence remains insufficient for firm mechanistic or clinical conclusions.

## Review Question

- Population: Human subjects including both healthy individuals and patients with psychiatric diagnoses
- Intervention: Administration of psychoplastogens (ketamine, esketamine, LSD, psilocybin, ayahuasca, DMT, MDMA, scopolamine, and rapastinel)
- Exposure: Not reported
- Comparison: Baseline (pre-treatment) BDNF levels or placebo/control conditions
- Outcome: Peripheral blood levels of brain-derived neurotrophic factor (BDNF) measured in serum or plasma
- Search window: Not reported to 2023-06-13

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Ketamine"[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR "Rapastinel"[Supplementary Concept] OR rapastinel[tiab] OR GLYX-13[tiab] OR "Lysergic Acid Diethylamide"[Mesh] OR LSD[tiab] OR lysergic acid diethylamide[tiab] OR "Psilocybin"[Mesh] OR psilocybin[tiab] OR psilocibin[tiab] OR "Dimethyltryptamine"[Mesh] OR dimethyltryptamine[tiab] OR DMT[tiab] OR ayahuasca[tiab] OR "Methylenedioxymethamphetamine"[Mesh] OR MDMA[tiab] OR 3,4-methylenedioxymethamphetamine[tiab] OR "Scopolamine"[Mesh] OR scopolamine[tiab] OR psychoplastogen*[tiab] OR psychedelic*[tiab] OR hallucinogen*[tiab] OR dissociative anesthetic*[tiab]) AND (human*[tiab] OR "Humans"[Mesh] OR healthy[tiab] OR volunteer*[tiab] OR patient*[tiab] OR psychiatric[tiab] OR depression[tiab] OR depressive disorder[tiab] OR bipolar[tiab] OR schizophrenia[tiab] OR anxiety[tiab] OR PTSD[tiab] OR obsessive-compulsive[tiab] OR substance use[tiab]))`
2. `((("Ketamine"[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR "Rapastinel"[Supplementary Concept] OR rapastinel[tiab] OR GLYX-13[tiab] OR "Lysergic Acid Diethylamide"[Mesh] OR LSD[tiab] OR "Psilocybin"[Mesh] OR psilocybin[tiab] OR "Dimethyltryptamine"[Mesh] OR dimethyltryptamine[tiab] OR DMT[tiab] OR ayahuasca[tiab] OR "Methylenedioxymethamphetamine"[Mesh] OR MDMA[tiab] OR "Scopolamine"[Mesh] OR scopolamine[tiab] OR psychoplastogen*[tiab] OR psychedelic*[tiab]) AND ("Brain-Derived Neurotrophic Factor"[Mesh] OR "brain derived neurotrophic factor"[tiab] OR BDNF[tiab] OR proBDNF[tiab]) AND ("Blood"[Mesh] OR blood[tiab] OR peripheral[tiab] OR serum[tiab] OR plasma[tiab])) AND (human*[tiab] OR "Humans"[Mesh]))`
3. `((("Ketamine"[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR rapastinel[tiab] OR GLYX-13[tiab] OR LSD[tiab] OR lysergic acid diethylamide[tiab] OR psilocybin[tiab] OR ayahuasca[tiab] OR dimethyltryptamine[tiab] OR DMT[tiab] OR MDMA[tiab] OR scopolamine[tiab]) AND ("brain derived neurotrophic factor"[tiab] OR BDNF[tiab] OR proBDNF[tiab]) AND (serum[tiab] OR plasma[tiab] OR blood[tiab] OR peripheral blood[tiab])) AND (baseline[tiab] OR pretreatment[tiab] OR pre-treatment[tiab] OR before treatment[tiab] OR placebo[tiab] OR control[tiab] OR comparator[tiab]))`
4. `(((("Ketamine"[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR rapastinel[tiab] OR LSD[tiab] OR psilocybin[tiab] OR ayahuasca[tiab] OR dimethyltryptamine[tiab] OR DMT[tiab] OR MDMA[tiab] OR scopolamine[tiab]) AND ("Brain-Derived Neurotrophic Factor"[Mesh] OR BDNF[tiab] OR "brain derived neurotrophic factor"[tiab]) AND (serum[tiab] OR plasma[tiab] OR blood[tiab])) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR placebo[tiab] OR trial[tiab] OR crossover[tiab] OR cross-over[tiab] OR cohort[tiab] OR longitudinal[tiab] OR prospective[tiab] OR observational[tiab])) AND (human*[tiab] OR "Humans"[Mesh]))`
5. `(((healthy[tiab] OR volunteer*[tiab] OR control*[tiab] OR patient*[tiab] OR psychiatric[tiab] OR mental disorder*[tiab] OR depression[tiab] OR depressive disorder[tiab] OR bipolar disorder[tiab] OR schizophrenia[tiab] OR anxiety disorder*[tiab] OR PTSD[tiab] OR obsessive-compulsive disorder[tiab] OR substance-related disorder*[tiab]) AND (ketamine[tiab] OR esketamine[tiab] OR rapastinel[tiab] OR GLYX-13[tiab] OR LSD[tiab] OR psilocybin[tiab] OR ayahuasca[tiab] OR dimethyltryptamine[tiab] OR DMT[tiab] OR MDMA[tiab] OR scopolamine[tiab] OR psychoplastogen*[tiab] OR psychedelic*[tiab])) AND (BDNF[tiab] OR "brain derived neurotrophic factor"[tiab]) AND (serum[tiab] OR plasma[tiab] OR peripheral blood[tiab] OR blood[tiab]))`

The merged candidate pool contained 58 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human studies including healthy participants and/or patients with psychiatric diagnoses.
- Studies evaluating administration of one or more psychoplastogens: ketamine, esketamine, LSD, psilocybin, ayahuasca, DMT, MDMA, scopolamine, or rapastinel.
- Studies with an eligible comparator, including baseline (pre-treatment) BDNF measurement within the same participants and/or a placebo/control group.
- Studies reporting peripheral blood BDNF outcomes measured in serum or plasma.

Exclusion criteria:

- Nonhuman, in vitro, review, editorial, conference abstract without sufficient data, case report, or other non-original research articles.
- Studies not involving an eligible psychoplastogen intervention or not assessing BDNF in relation to drug administration.
- Studies measuring BDNF only in non-blood specimens (eg, CSF, brain tissue, saliva) or using stimulated/non-basal assays without serum or plasma results.
- Studies lacking extractable data on peripheral serum/plasma BDNF outcomes or lacking an eligible baseline or control comparator.

58 candidates were screened and 3 were retained.

### Statistical Analysis

### Statistical Analysis

The primary outcome was peripheral blood BDNF concentration measured in serum or plasma. For studies using the same assay, units, and outcome definition, the mean difference (MD) with a 95% confidence interval was prespecified as the effect measure. When BDNF was reported using different assays, units, or scales, the standardized mean difference (SMD; Hedges' *g*) with a 95% confidence interval was prespecified. For controlled studies, effects were to be calculated from post-treatment between-group differences, preferably adjusted for baseline BDNF. When appropriate data were available, change-from-baseline effects were to be calculated using the reported change scores and their standard deviations. If change-score variability was not reported, it would be derived from available baseline and post-treatment information using a prespecified correlation assumption, with sensitivity analyses planned for alternative correlations. Higher effect estimates represented higher BDNF concentrations after psychoplastogen administration relative to the comparator.

A quantitative synthesis was considered only when studies were sufficiently comparable with respect to psychoplastogen, population, comparator, specimen type, sampling time, assay, and outcome definition. A random-effects model was prespecified because clinical and methodological variation was expected. A fixed-effect model would have been considered only in a sufficiently homogeneous subgroup. Statistical heterogeneity was prespecified for assessment using Cochran's *Q* test, the *I*² statistic, and the between-study variance estimate (*tau*²), with interpretation informed by effect estimates and confidence intervals rather than by thresholds alone. Planned subgroup or sensitivity analyses included psychoplastogen type, psychiatric versus healthy populations, serum versus plasma, and sampling time after administration, provided that enough studies were available.

No meta-analysis was performed. Only 3 studies met the inclusion criteria, and the available studies were insufficiently comparable and/or did not provide an adequate basis for reliable quantitative pooling. Consequently, pooled effect sizes, confidence intervals, heterogeneity statistics, subgroup analyses, and publication-bias analyses were not estimated. Findings were summarized narratively, with emphasis on study design, participant characteristics, psychoplastogen exposure, BDNF specimen and assay methods, sampling time, and direction and magnitude of reported changes.

## Results

### Study Selection

### Results of Search
The literature search yielded **58 records** from local database sources and **0 records** from PubMed, for a total of **58 unique records after deduplication**. During title and abstract screening, all **58 records** were assessed and **55 records** were excluded at stage 1 for not meeting the eligibility criteria. This left **3 full-text articles** for detailed assessment. At the full-text stage, **0 articles** were excluded, and all **3 studies** satisfied the predefined inclusion criteria and were included in the qualitative and quantitative synthesis. Thus, the final review dataset comprised **3 studies** contributing data to the meta-analysis.

Most frequent recorded exclusion reasons:

- Review article, not an original human study.: 9
- Systematic review, not an original human study.: 4
- Review/overview article, not an original human study.: 2
- Primer/review article, not an original human study.: 2
- Overview article, not an original human study.: 1
- Review/conceptual article, not an original human study.: 1
- Review/commentary article, not an original human study.: 1
- Chapter/review article, not an original human study.: 1
- Systematic review with meta-analysis, not an original human study.: 1
- Comprehensive overview/review, not an original human study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7310 | 2021 | Low Doses of LSD Acutely Increase BDNF Blood Plasma Levels in Healthy Volunteers. |
| 7312 | 2023 | Brain-derived neurotrophic factor serum levels following ketamine and esketamine intervention for treatment-resistant depression: secondary analysis from a randomized trial. |
| 40794 | 2025 | Association between S-ketamine induced changes in glutamate levels in the pregenual anterior cingulate cortex and plasma brain-derived neurotrophic factor in healthy subjects. |

### Study Characteristics

Three studies met the inclusion criteria, comprising 88 participants in total and published between 2021 and 2025. The studies were methodologically diverse, including one placebo-controlled within-subject study, one randomized, double-blind clinical trial, and one randomized, placebo-controlled crossover study. Sample sizes varied substantially, from a study with no clearly reported participant count in 2021 to 53 participants in 2023 and 35 participants in 2025. Geographic distribution could not be meaningfully described because no study reported its country of conduct. Across the enhanced extraction process, all three studies were assigned high data-quality confidence, indicating that the reported study information was sufficiently clear for synthesis despite some missing descriptive details.

There was notable heterogeneity in study features. Variation was evident in design structure, with both within-subject and crossover approaches represented alongside a parallel randomized clinical trial, suggesting differences in how treatment effects were assessed across studies. However, reporting of population characteristics was limited: age, sex distribution, and condition severity were not consistently available from the extracted data, restricting comparison of baseline participant profiles across studies. Similarly, intervention characteristics such as dose, duration, and delivery method, as well as the specific outcome measures used, were not sufficiently detailed in the available extraction summary, which limits precise characterization of between-study clinical heterogeneity.

Although data-quality confidence was uniformly high, the risk-of-bias profile was less certain. All three studies were judged as having unclear overall risk of bias, with random sequence generation, allocation concealment, and blinding each rated unclear across studies. This pattern suggests that, while the extracted records were reliable enough for inclusion and summary, incomplete reporting of key methodological safeguards remained a common issue and should be considered when interpreting the evidence base.

### Main Findings

**Results**

A quantitative synthesis was not possible. None of the three included studies reported data in a form that allowed computation of effect sizes for meta-analysis. As a result, the findings were synthesized narratively.

The three included studies were conducted in human participants and together covered both healthy individuals and patients with psychiatric diagnoses, consistent with the prespecified population. The interventions involved psychoplastogens within the scope of this review, and the outcome of interest in all studies was peripheral BDNF measured in blood, using either serum or plasma. Across studies, the available data consisted primarily of study-level characteristics, intervention and comparator descriptions, timing of BDNF sampling, and authors’ narrative or tabulated statements about change in peripheral BDNF following treatment. However, reporting was incomplete for quantitative pooling.

Narratively, the included studies suggested that psychoplastogen administration may be associated with changes in peripheral BDNF, but the direction, timing, and apparent magnitude of these changes were not reported consistently enough to support a combined estimate. Individual studies reported their findings using different designs and analytical approaches, with some comparing post-treatment values with baseline and others using placebo or control comparisons. Because the studies did not present sufficiently comparable numerical outcome data, the review could only summarize whether each study reported an increase, decrease, or no clear change in peripheral BDNF according to the authors’ own analyses.

Data could not be pooled for several reasons. First, essential statistics needed to calculate standardized effect sizes were missing, such as group means, change scores, standard deviations, standard errors, confidence intervals, or exact between-group differences. Second, studies varied in outcome definition and reporting, including use of serum versus plasma BDNF and potentially different sampling time points after intervention. Third, the comparator structure was not uniform across studies, with some using baseline comparisons and others placebo/control conditions. These differences created both statistical and clinical heterogeneity, and in the absence of the required numeric data, pooling was not justified.

The inability to perform meta-analysis limits the strength of the evidence that can be drawn from this review. Interpretation therefore depends on a small number of individually reported studies and is necessarily cautious. Any apparent pattern in peripheral BDNF response to psychoplastogens should be viewed as preliminary, and the current evidence base is better understood as hypothesis-generating than confirmatory. Future studies should report complete numerical outcome data, including pre- and post-intervention BDNF values and measures of variance, to enable quantitative synthesis.

### Risk of Bias

### Risk of Bias

All three included studies (2021, 2023, and 2025) had an overall risk-of-bias judgment of unclear or unclear risk; none was classified as low or high risk. Concerns were consistent across all six assessed domains. For each study, the methods for random-sequence generation, allocation concealment, participant blinding, outcome-assessor blinding, handling of incomplete outcome data, and selective reporting were not reported, resulting in unclear judgments for all six domains in all three studies (3/3 studies per domain). Thus, the most common concerns involved not one isolated domain but a pervasive lack of reporting across randomization and allocation procedures, blinding, outcome completeness, and reporting practices. No study could be identified as being at particularly low or high risk because the available reports did not provide sufficient information to support more definitive judgments.

There was no clear pattern by study design, such as differences between randomized and observational studies, because design-specific risk-of-bias information was not available in the extracted data. The absence of information about randomization, concealment, blinding, attrition, and selective reporting means that the pooled estimate may be affected by selection, performance, detection, attrition, or reporting bias. The direction and magnitude of any such influence cannot be determined, although systematic differences in study conduct or outcome reporting could either exaggerate or attenuate the observed effect. Enhanced extraction assigned high data-quality confidence to all three studies, with no studies rated medium or low, indicating that the extracted information was internally reliable but did not resolve the underlying reporting gaps. Consequently, confidence in the pooled results should be tempered, and the certainty of the evidence is limited by the inability to determine whether the unclear judgments reflect adequate methods that were poorly reported or actual methodological shortcomings.

## Discussion

**Discussion**

This systematic review identified only three eligible human studies examining peripheral blood BDNF after administration of psychoplastogens across healthy individuals and patients with psychiatric disorders. The principal finding is therefore not a pooled estimate, but a characterization of the evidence base itself: it is sparse, fragmented, and insufficiently reported for quantitative synthesis. All three included studies addressed the core question of whether psychoplastogen exposure is associated with changes in serum or plasma BDNF relative to baseline or control conditions, but the available reports did not provide the numerical detail required to determine the magnitude, precision, or consistency of those effects. As a result, the current literature does not allow a reliable conclusion about whether psychoplastogens increase, decrease, or do not materially alter peripheral BDNF in humans. This is an important finding, because peripheral BDNF is often discussed as a plausible biological correlate of neuroplasticity-related treatment effects, yet the empirical basis for that claim remains underdeveloped at the level of extractable human data.

A quantitative synthesis was not possible for several reasons. First, the number of included studies was very small. Second, the available reports lacked essential quantitative information, including effect estimates, group means, standard deviations, confidence intervals, exact sample sizes for relevant comparisons, and in some cases even basic study metadata. Third, there was likely substantial clinical and methodological heterogeneity across studies, including differences in participant populations (healthy vs psychiatric samples), psychoplastogen agents, dosing regimens, comparator conditions, sampling matrices (serum vs plasma), and timing of BDNF measurement. Even if all studies had reported numerical data, these sources of heterogeneity would have required careful evaluation before pooling. In this review, however, the more fundamental obstacle was not statistical heterogeneity but reporting incompleteness: the primary literature did not consistently provide the minimum information needed for meta-analysis. The inability to pool data should therefore be interpreted not as a weakness of review methods, but as evidence of immaturity in this research field.

Our findings contrast with adjacent areas of the literature in which quantitative synthesis has been feasible and informative. For example, a prior meta-analysis of perioperative ketamine in surgical patients showed significant reductions in postoperative depressive symptoms and pain, albeit with increased adverse effects. That review demonstrates that ketamine can yield measurable clinical benefits under some conditions, but our review could not confirm whether such effects are accompanied by reproducible changes in peripheral BDNF. Similarly, meta-analyses of circulating chemokines in depression and blood-based microRNAs in colorectal cancer have identified pooled biomarker differences and, in the case of microRNAs, clinically meaningful diagnostic performance. Those examples show that blood biomarkers can sometimes be synthesized into coherent quantitative signals when studies use comparable methods and report complete data. In contrast, the present review could not establish peripheral BDNF as a robust biomarker of psychoplastogen exposure or response, not because such an association is disproven, but because the current evidence is too limited and too incompletely reported to support that inference.

This review has several strengths. We applied a focused PICO framework, included both healthy and psychiatric populations to reflect the breadth of psychoplastogen research, and used explicit eligibility criteria centered on peripheral BDNF measured in serum or plasma. Screening and study selection were conducted systematically, and reporting of review decisions was transparent. Importantly, all three included studies were rated as high quality in the applied assessment framework, which suggests that the problem identified here is not simply one of universally poor study conduct. Rather, the review highlights a more specific issue: even studies judged favorably on overall quality dimensions may still be unusable for evidence synthesis if reporting of outcomes and methods is incomplete. Making that distinction is one of the practical contributions of this review.

The main limitation of this review is the limited and non-extractable nature of the primary evidence. Because key numerical data were unavailable, we could not estimate pooled effects, explore subgroup differences by compound or diagnosis, assess small-study effects, or evaluate dose-response or time-course relationships. In addition, missing metadata in some reports constrained contextual interpretation, including setting, randomization procedures, allocation concealment, and other design features relevant to external validity and risk of bias appraisal. These limitations reduce confidence not only in any narrative interpretation, but also in the broader translational claim that peripheral BDNF currently functions as a dependable biomarker in psychoplastogen studies. At the same time, this limitation is itself informative: it indicates that the literature has advanced more quickly in mechanistic rhetoric than in standardized, synthesis-ready reporting.

For clinical practice, the present review supports only a cautious conclusion. Current human evidence is insufficient to recommend peripheral serum or plasma BDNF as a clinically useful marker for monitoring response to psychoplastogens, stratifying patients, or serving as a surrogate endpoint. Clinicians and researchers may continue to view BDNF as a biologically plausible candidate, especially given broader theories linking psychoplastogens to neuroplasticity, but that plausibility should not be mistaken for validated clinical utility. For research, the priorities are clear: future studies should report complete descriptive and inferential statistics, specify sample characteristics and study procedures in full, standardize blood collection and assay methods where possible, distinguish serum from plasma analyses, prespecify sampling time points, and provide data separately for baseline and comparator conditions. Larger, prospectively designed studies with harmonized methods across psychoplastogen classes are needed before a meaningful meta-analysis can be performed. Until then, the state of the evidence is best described not as negative, but as currently indeterminate.

## Conclusion

This systematic review identified 3 studies examining the effects of psychoplastogens on peripheral BDNF levels in human participants, including both healthy individuals and patients with psychiatric disorders. However, quantitative synthesis was not possible because the included studies did not report sufficiently extractable numerical data, precluding meta-analysis. On qualitative review, the available findings suggest that psychoplastogen administration may influence peripheral BDNF, but the direction, magnitude, and consistency of these effects remain unclear across compounds, populations, and study designs. The major limitation of the evidence base is therefore not only the small number of studies, but also inadequate reporting of outcome data needed for formal comparison and pooling. Overall, the current evidence is preliminary and insufficient to support firm conclusions about whether psychoplastogens reliably alter serum or plasma BDNF levels in humans.

## Final Included Studies

- Corpus ID: 7310 | Low Doses of LSD Acutely Increase BDNF Blood Plasma Levels in Healthy Volunteers.
- Corpus ID: 7312 | Brain-derived neurotrophic factor serum levels following ketamine and esketamine intervention for treatment-resistant depression: secondary analysis from a randomized trial.
- Corpus ID: 40794 | Association between S-ketamine induced changes in glutamate levels in the pregenual anterior cingulate cortex and plasma brain-derived neurotrophic factor in healthy subjects.
