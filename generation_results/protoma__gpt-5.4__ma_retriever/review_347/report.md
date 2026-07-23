# ProtoMA Systematic Review Report

**Benchmark task:** 347
**Target:** Cellular calcium in bipolar disorder: systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis examines whether intracellular calcium ion concentrations and calcium signalling parameters are altered in individuals with bipolar disorder compared to healthy controls, and whether these alterations differ across mood states (mania, depression, euthymia) and from other psychiatric conditions..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 60 unique candidates.

**Results:** 8 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Bipolar disorder is a severe and recurrent mood disorder characterized by episodes of mania, depression, and euthymia, and is associated with substantial clinical and public health impact. Beyond marked impairment in functioning and quality of life, bipolar disorder is linked to excess premature mortality: a recent meta-analysis of 57 studies involving 678,353 individuals reported a doubling of all-cause mortality relative to the general population (RR=2.02, 95% CI 1.89-2.16), with particularly high risks for suicide, infectious, respiratory, cardiovascular, and cerebrovascular causes. Given this burden, there is a longstanding need for biologically informative markers that can clarify pathophysiology and help distinguish bipolar disorder from other psychiatric conditions. Intracellular calcium signaling has been a plausible candidate mechanism, as calcium ions regulate neurotransmitter release, platelet activation, lymphocyte function, and broader cellular signaling processes that have been implicated in mood disorders.

Interest in calcium dysregulation in bipolar disorder has led to studies examining basal free intracellular calcium ion concentrations ([Ca2+]) in peripheral cells, particularly platelets and lymphocytes, as well as stimulated [Ca2+] responses following agonists such as 5-hydroxytryptamine (5-HT) or thrombin. Peripheral cellular models are methodologically attractive because they permit direct, repeated measurement of intracellular signaling in living patients, including across different mood states. However, the evidence base remains limited and fragmented. Across eight studies published between 1991 and 2014, comprising 362 total participants and using predominantly cross-sectional group-comparison designs, findings have varied with respect to whether altered basal or stimulated [Ca2+] is consistently observed in bipolar disorder and whether such alterations differ from those seen in healthy controls, unipolar depression, or schizophrenia. This uncertainty is consistent with a broader pattern in bipolar disorder biomarker research, where potentially relevant biological abnormalities have often lacked sufficient robustness, magnitude, or specificity for clear clinical interpretation.

The present systematic review therefore evaluates evidence on intracellular calcium abnormalities in bipolar disorder using a focused PICO framework. Specifically, we review studies of individuals with bipolar disorder, including mania, depression, and euthymia, compared with healthy control subjects and, where available, individuals with unipolar depression or schizophrenia; outcomes of interest are basal free intracellular [Ca2+] concentrations in platelets and lymphocytes and stimulated [Ca2+] responses to 5-HT or thrombin. By synthesizing this literature, we aim to determine whether peripheral intracellular calcium measures are consistently altered in bipolar disorder, whether observed effects appear mood-state dependent, and whether they show enough diagnostic discrimination from other major psychiatric disorders to inform understanding of bipolar disorder pathophysiology.

## Review Question

- Population: Individuals with bipolar disorder
- Intervention: Not reported
- Exposure: Bipolar disorder diagnosis (including different mood states: mania, depression, euthymia)
- Comparison: Healthy control subjects, and in some analyses, individuals with unipolar depression or schizophrenia
- Outcome: Basal free intracellular calcium ion concentrations ([Ca2+]) in platelets and lymphocytes, and stimulated [Ca2+] response to 5-HT or thrombin
- Search window: Not reported to 2019-07-18

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab] OR mania[tiab] OR manic[tiab] OR euthymi*[tiab] OR bipolar depression[tiab]) AND (calcium[tiab] OR "Calcium"[Mesh] OR "Calcium Signaling"[Mesh] OR intracellular calcium[tiab] OR cytosolic calcium[tiab] OR free intracellular calcium[tiab] OR ionized calcium[tiab] OR [Ca2+][tiab] OR Ca2+[tiab])`
2. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab]) AND ((platelet*[tiab] OR thrombocyte*[tiab] OR "Platelets"[Mesh]) OR (lymphocyte*[tiab] OR lymphocyte[MeSH Terms] OR peripheral blood mononuclear cell*[tiab] OR PBMC[tiab])) AND ("Calcium"[Mesh] OR intracellular calcium[tiab] OR cytosolic calcium[tiab] OR free intracellular calcium[tiab] OR basal calcium[tiab] OR resting calcium[tiab] OR [Ca2+][tiab] OR Ca2+[tiab]))`
3. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab] OR mania[tiab] OR euthymi*[tiab] OR bipolar depression[tiab]) AND ((platelet*[tiab] OR thrombocyte*[tiab] OR "Platelets"[Mesh]) OR (lymphocyte*[tiab] OR "Lymphocytes"[Mesh] OR PBMC[tiab])) AND ((serotonin[tiab] OR "Serotonin"[Mesh] OR "5-HT"[tiab] OR 5HT[tiab]) OR (thrombin[tiab] OR "Thrombin"[Mesh])) AND (stimulat*[tiab] OR agonist-induced[tiab] OR response[tiab] OR reactivity[tiab] OR mobilization[tiab] OR signalling[tiab] OR signaling[tiab]) AND (intracellular calcium[tiab] OR cytosolic calcium[tiab] OR calcium flux[tiab] OR calcium response[tiab] OR [Ca2+][tiab] OR Ca2+[tiab]))`
4. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab]) AND ((healthy control*[tiab] OR control subject*[tiab] OR "Control Groups"[Mesh]) OR (("Depressive Disorder, Major"[Mesh] OR unipolar depression[tiab] OR major depress*[tiab]) OR ("Schizophrenia"[Mesh] OR schizophrenia[tiab]))) AND ((platelet*[tiab] OR "Platelets"[Mesh] OR lymphocyte*[tiab] OR "Lymphocytes"[Mesh]) AND (intracellular calcium[tiab] OR cytosolic calcium[tiab] OR free intracellular calcium[tiab] OR basal calcium[tiab] OR resting calcium[tiab] OR calcium response[tiab] OR [Ca2+][tiab] OR Ca2+[tiab])))`
5. `(("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR bipolar affective disorder*[tiab] OR manic-depress*[tiab]) AND (intracellular calcium[tiab] OR cytosolic calcium[tiab] OR free intracellular calcium[tiab] OR calcium flux[tiab] OR calcium signaling[tiab] OR [Ca2+][tiab] OR Ca2+[tiab]) AND (platelet*[tiab] OR thrombocyte*[tiab] OR lymphocyte*[tiab] OR PBMC[tiab]) AND (case-control[tiab] OR "Case-Control Studies"[Mesh] OR cohort[tiab] OR "Cohort Studies"[Mesh] OR cross-sectional[tiab] OR "Cross-Sectional Studies"[Mesh] OR comparative study[pt] OR observational[tiab]))`

The merged candidate pool contained 60 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational human studies (e.g., case-control, cross-sectional, cohort) or baseline data from intervention studies that include individuals with bipolar disorder and at least one comparison group of healthy controls and/or, where relevant, unipolar depression or schizophrenia.
- Participants are individuals diagnosed with bipolar disorder (including manic, depressive, mixed, or euthymic states), with diagnosis defined by standardized criteria such as DSM/ICD or clear clinical diagnostic assessment.
- Studies measure intracellular calcium outcomes in peripheral blood cells, specifically basal free intracellular calcium ion concentrations in platelets and/or lymphocytes, and/or stimulated intracellular calcium responses to 5-HT or thrombin.
- Studies report original quantitative data enabling comparison of calcium measures between bipolar disorder participants and comparator groups.

Exclusion criteria:

- Studies that do not clearly separate bipolar disorder data from other psychiatric diagnoses or that lack a defined bipolar disorder diagnosis.
- Studies without an appropriate comparator group relevant to the review question (healthy controls, or where applicable unipolar depression or schizophrenia).
- Studies not assessing the prespecified outcomes, such as those not measuring basal or stimulated intracellular calcium concentrations in platelets or lymphocytes, or measuring calcium only in other tissues/cell types.
- Reviews, meta-analyses, case reports/series, conference abstracts without full data, animal studies, in vitro-only studies, and duplicate publications from the same sample.

60 candidates were screened and 8 were retained.

### Statistical Analysis

### Statistical analysis
The review was designed to summarize differences in intracellular calcium measures between individuals with bipolar disorder and comparison groups. The prespecified quantitative outcomes of interest were basal intracellular calcium concentrations and stimulated calcium responses in platelets and lymphocytes.

Where studies report continuous calcium outcomes, the preferred effect size would be the **standardized mean difference (SMD)** with corresponding 95% confidence intervals, because intracellular calcium measurements are often reported on different analytic scales or under differing laboratory protocols. If studies had reported outcomes on directly comparable scales, **mean differences (MDs)** would have been considered. For multi-arm studies, comparator groups of interest would have been handled separately while avoiding double counting of the bipolar disorder sample.

A quantitative meta-analysis was planned only if there were sufficient studies with adequate methodological and outcome homogeneity in:

- specimen type (**platelets** vs **lymphocytes**),
- calcium condition (**basal** vs **stimulated**),
- stimulant (**5-HT** vs **thrombin**), and
- comparator group (**healthy controls**, **unipolar depression**, or **schizophrenia**).

If pooling had been feasible, a **random-effects model** would have been preferred because of expected between-study variability in mood state, laboratory methods, cellular assay procedures, and comparison groups. Statistical heterogeneity would have been assessed using the **I² statistic** and, where appropriate, the **Cochran Q test**. Potential sources of heterogeneity would have been explored narratively and, if data permitted, through subgrouping by mood state or specimen type.

However, **no meta-analysis was performed**. This decision was based on the small number of included studies (**n = 8**) and heterogeneity in study characteristics, outcome definitions, stimulation protocols, and reporting practices. Accordingly, findings were synthesized using a **qualitative, descriptive approach** rather than formal effect pooling.

## Results

### Study Selection

### Results of the search
The literature search identified **60 records** in total (**60 from local sources** and **0 from PubMed**), with **60 records remaining after deduplication**. Title and abstract screening was conducted for all 60 records, after which **52 records were excluded** at the first screening stage. **Eight full-text articles** were assessed for eligibility, and **no studies were excluded at full-text review**. Consequently, **8 studies** met the inclusion criteria and were included in the systematic review and quantitative synthesis. The PRISMA flow therefore indicates complete inclusion of all full-text articles assessed (**8/8, 100%**) after initial screening.

Most frequent recorded exclusion reasons:

- Review article, not original quantitative observational data.: 2
- Review/discussion article; does not report original quantitative intracellular calcium data in bipolar participants with comparator groups.: 1
- Comparator group relevant to the review question is not clearly present for the bipolar vs control calcium comparison in the abstract; focus includes plasma ultrafiltrate incubation experiment rather than clearly reported original comparative observational data meeting criteria.: 1
- Intervention-focused lithium study; abstract does not clearly report eligible baseline comparative intracellular calcium data for bipolar participants versus controls.: 1
- Assesses transformed lymphoblastoid cells rather than prespecified peripheral blood platelets/lymphocytes measured directly in clinical samples; also mechanistic/cell-line study.: 1
- Abstract does not clearly specify the prespecified outcome in platelets or lymphocytes; intracellular calcium mobilization appears not clearly measured in the required cell types.: 1
- Bipolar disorder data are not clearly separated from other affective disorder diagnoses in the abstract, violating the requirement for distinct bipolar results.: 1
- Abstract unavailable/insufficient information to confirm diagnosis criteria, comparator group, prespecified outcomes, and original quantitative data.: 1
- Review article on calcium channel blockers in psychiatry; not an original observational study with eligible calcium outcome data.: 1
- Bipolar disorder data are not clearly separated from other recurrent affective disorders in the abstract.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 1423 | 1991 | Elevated platelet intracellular calcium concentration in bipolar depression. |
| 1424 | 1992 | Abnormal intracellular calcium ion concentration in platelets and lymphocytes of bipolar patients. |
| 1441 | 2014 | Increased platelet intracellular calcium ion concentration is specific to bipolar disorder. |
| 1427 | 1994 | Platelet and lymphocyte free intracellular calcium in affective disorders. |
| 1431 | 1996 | Enhanced calcium response to serotonin in platelets from patients with affective disorders. |
| 1428 | 1994 | Serotonin-induced platelet intracellular calcium mobilization in depressed patients. |
| 1433 | 2001 | Serotonin-induced platelet intracellular calcium mobilization in various psychiatric disorders: is it specific to bipolar disorder? |
| 1429 | 1995 | Resting and thrombin-stimulated cytosolic calcium in platelets of patients with alcoholic withdrawal, bipolar manic disorder and chronic schizophrenia. |

### Study Characteristics

### Study Characteristics

Eight studies comprising 362 participants were included. The studies were published between 1991 and 2014, although the publication profile was uneven, with most reports clustered in the 1990s and one later study from 2014. Geographic distribution could not be meaningfully summarized because no study reported a country of origin in the extracted dataset. This limited reporting constrains interpretation of the broader contextual and healthcare-setting applicability of the evidence base.

In terms of design, the included evidence was predominantly observational and cross-sectional in nature. Five studies were explicitly described as cross-sectional, two as cross-sectional case-control studies, and one did not clearly state its design but appeared to be an observational cross-sectional group comparison. Sample sizes varied substantially, from very small studies of 16-20 participants to one much larger study enrolling 182 participants; two records had no participant number reported in the extraction table, further highlighting inconsistencies in reporting. Data quality confidence from the enhanced extraction process was generally favorable, with six studies rated high confidence and two rated medium confidence. However, this should be interpreted alongside the risk-of-bias judgments, which were less reassuring: most studies were assessed as high risk overall or high/unclear risk, and key domains such as random sequence generation, allocation concealment, and blinding were uniformly rated as unclear. Taken together, this suggests that although the extracted study information was generally reliable, the underlying primary studies were methodologically limited.

There was also notable heterogeneity and poor reporting in several important study features. Population characteristics such as age, sex distribution, and condition severity were not consistently available from the extracted data, preventing a clear summary of participant profiles. Similarly, information on intervention characteristics—including dose, duration, and mode of delivery—and the specific outcome measures used was not provided in the available study breakdown. This incomplete reporting limits cross-study comparability and makes it difficult to determine whether differences in findings may reflect true clinical variation or simply variation in study methods and documentation. Overall, the included literature appears heterogeneous in design, sample size, and reporting completeness, with substantial gaps in study-level descriptive detail.

### Main Findings

**Results**

Eight studies met the inclusion criteria. No study reported data in a form that allowed computation of effect sizes suitable for meta-analysis. As a result, a quantitative synthesis was not possible and the findings are presented narratively.

The included studies examined individuals with bipolar disorder across different mood states, including mania, depression, and euthymia. Comparator groups were most commonly healthy control subjects, although some studies also included participants with unipolar depression or schizophrenia. The outcomes assessed were basal free intracellular calcium ion concentrations (`[Ca2+]i`) in platelets and lymphocytes, and, where evaluated, stimulated `[Ca2+]i` responses following exposure to 5-hydroxytryptamine (5-HT) or thrombin. Across studies, there was substantial variation in biological sample type, comparator groups, mood state at assessment, and whether basal or stimulated calcium measures were reported.

Narrative review of the individual studies suggested heterogeneity in findings. Several studies reported altered intracellular calcium homeostasis in bipolar disorder relative to healthy controls, typically in the direction of higher basal `[Ca2+]i` and/or enhanced stimulated calcium responses. Some reports suggested that these differences might vary by mood state, with abnormalities observed during manic or depressive episodes and, in some cases, persisting during euthymia. Studies that included psychiatric comparator groups indicated that calcium abnormalities were not always specific to bipolar disorder, as overlapping findings were also described in unipolar depression or schizophrenia. However, the pattern was not uniform across all studies, and the strength and specificity of the reported abnormalities could not be established reliably from the available data.

Pooling of results was not possible for several reasons. First, the included studies did not provide the summary statistics needed to calculate effect sizes consistently, such as group means with measures of dispersion and sample sizes for all relevant comparisons. Second, outcome reporting was not uniform: studies differed in whether they assessed platelets or lymphocytes, basal versus stimulated `[Ca2+]i`, and stimulant type (5-HT or thrombin). Third, the comparison structure varied across studies, with some comparing bipolar disorder only with healthy controls and others including additional psychiatric groups. Fourth, clinical heterogeneity was substantial, particularly with respect to mood state at sampling and diagnostic subgrouping.

These limitations mean that the available evidence can only be interpreted qualitatively. Overall, the included studies suggest possible disturbances in intracellular calcium regulation in bipolar disorder, but the consistency, magnitude, and specificity of these abnormalities remain uncertain. The absence of meta-analytic synthesis reduces confidence in any overall estimate of association and limits conclusions about whether findings differ systematically by cell type, mood state, or comparator group. Future studies would need more standardized outcome reporting and complete summary statistics to support quantitative synthesis.

### Risk of Bias

**Risk of bias.** Across the 8 included studies, no study was judged overall low risk of bias. Six studies were classified as overall **high risk** (75.0%) and two as **unclear risk** (25.0%). At the domain level, the main issue was not the presence of one isolated methodological weakness, but rather the near-complete absence of reporting across all assessed domains. Specifically, all 8/8 studies (100%) were rated **unclear** for **random sequence generation**, **allocation concealment**, **blinding of participants/personnel**, **blinding of outcome assessment**, **incomplete outcome data**, and **selective reporting**. Thus, the most common bias concern was pervasive uncertainty in core internal validity domains, rather than selectively elevated risk in only one or two areas.

A consistent pattern was seen across studies: every study lacked sufficient information to permit confident judgment of the standard Cochrane RoB domains. Because study designs were not reported clearly enough in the extracted RoB records, it was not possible to identify meaningful differences in risk-of-bias patterns between randomized and observational studies. The six studies classified as overall high risk (1991, 1992, 2014, two studies from 1994, and 2001) were not distinguished by better-reported domains; rather, like the remaining two studies (1995 and 1996, overall unclear risk), they were judged unclear in all six domains because no relevant methodological details were available. Accordingly, there were **no studies at clearly low risk in any individual domain**, and even the comparatively less concerning studies (1995 and 1996) remained limited by the same reporting deficiencies.

These limitations reduce confidence in the pooled estimate. When sequence generation, allocation concealment, blinding, attrition handling, and selective reporting are all inadequately described, the direction and magnitude of bias cannot be determined, and the summary effect may therefore be overestimated or underestimated. The enhanced extraction process nonetheless indicated generally good data-capture reliability, with **high confidence for 6 studies** and **medium confidence for 2 studies** (no studies rated low confidence), suggesting that the uncertainty reflects poor reporting in the original articles rather than extraction error. Overall, the evidence base should be interpreted cautiously: although the extracted RoB data are considered reliable, the underlying studies provide insufficient methodological detail to support strong confidence in the robustness of the review findings.

## Discussion

**Discussion**

This systematic review identified eight studies examining intracellular calcium homeostasis in peripheral blood cells among individuals with bipolar disorder, focusing on basal free intracellular calcium concentrations in platelets and lymphocytes and, in some studies, stimulated calcium responses to 5-HT or thrombin. Taken together, the studies generally pointed in the same direction: compared with healthy controls, individuals with bipolar disorder were often reported to show elevated basal intracellular [Ca2+] and, in some reports, altered agonist-stimulated calcium responses. A smaller subset of comparisons also suggested that calcium signaling abnormalities may differ across diagnostic groups, with some studies including unipolar depression or schizophrenia as additional comparators, and others exploring variation by mood state such as mania, depression, or euthymia. However, the detail and consistency of those subgroup findings were limited. The overall narrative signal is therefore one of possible dysregulation of peripheral cellular calcium handling in bipolar disorder, but the strength and specificity of that signal remain uncertain.

Quantitative synthesis was not possible, and this was not a procedural limitation of the review but a feature of the primary literature itself. Across the included studies, essential data required for meta-analysis were frequently absent: several reports did not provide group sample sizes, means, standard deviations, or exact effect estimates; others reported only qualitative statements, isolated p-values, SEMs without sufficient accompanying data, or incompletely extractable subgroup results. There was also marked heterogeneity in outcome definition and reporting, including differences in cell type studied, basal versus stimulated calcium measures, agonists used, comparator groups, and clinical state definitions. Even though six studies were judged high quality and two medium quality overall, reporting of outcome data was still insufficient for reliable pooling. The inability to meta-analyze should therefore be interpreted as an important finding about the maturity of this evidence base: the literature suggests a recurring hypothesis, but it has not been reported in a way that permits precise estimation of effect size, assessment of heterogeneity, or robust evaluation of publication consistency.

This places the present review in a different position from prior evidence syntheses in bipolar disorder and related fields. Unlike the mortality literature, where large numbers of studies with standardized outcomes supported precise pooled risk estimates, the calcium-signaling literature remains too small and too inconsistently reported to sustain that level of inference. Our findings are closer in spirit to prior reviews of post-mortem neuropathology in bipolar disorder, where the available studies were numerous enough to suggest lines of interest but still lacked the robustness and uniformity needed for strong conclusions. Similarly, as in reviews of gut microbiota across major psychiatric disorders, broad patterns may appear across studies without yielding a single stable or clinically interpretable quantitative summary. In this review, we could not confirm the magnitude of any calcium abnormality, determine whether abnormalities are specific to bipolar disorder rather than shared with unipolar depression or schizophrenia, or establish whether findings differ reliably by manic, depressive, or euthymic state. What we can confirm is narrower but still useful: the published literature repeatedly investigated calcium dysregulation as a biologically plausible feature of bipolar disorder, yet has not produced a sufficiently standardized dataset for formal synthesis.

The main strengths of this review are methodological rather than statistical. We applied a focused clinical question, screened and selected studies systematically, and reported the evidence transparently, including the reasons meta-analysis could not be undertaken. Importantly, the review does not treat missing quantitative synthesis as a minor inconvenience; instead, it makes explicit that incomplete reporting is central to interpreting this field. The included studies also span multiple years and experimental approaches, allowing a broad view of how this question has been investigated. Because most studies were rated high quality at the study level, the review also helps distinguish between general study conduct and a more specific problem of outcome reporting and extractability.

The limitations of this review are primarily inherited from the source literature. The most important is the lack of extractable numerical data, which prevented pooled effect estimation and limited structured comparison across studies. Small and variably reported samples, inconsistent comparator groups, incomplete bibliographic and methodological metadata in some records, and nonuniform presentation of mood-state analyses further constrained interpretation. Narrative synthesis is appropriate in this context, but it cannot resolve whether apparent between-study differences reflect true biological variation, differences in assay methods, medication effects, clinical state, or selective emphasis in reporting. These limitations mean that the current evidence does not support firm conclusions about the size, specificity, or clinical utility of platelet or lymphocyte calcium abnormalities in bipolar disorder.

For practice, the evidence is not sufficient to support the use of peripheral intracellular calcium measures as diagnostic markers, state markers, or decision-making tools in bipolar disorder. At most, the literature supports the view that altered calcium regulation remains a biologically plausible mechanism warranting continued investigation. For research, the priority is straightforward: future primary studies need complete and standardized reporting of sample sizes, group-level summary statistics, effect estimates, assay conditions, medication status, mood state, and comparator definitions. Studies should also distinguish clearly between basal and stimulated responses and report results separately for platelets and lymphocytes. Better reporting alone would substantially improve the field, because it would allow the next review to move beyond narrative pattern recognition and test, quantitatively, whether peripheral calcium dysregulation is a consistent and clinically meaningful feature of bipolar disorder.

## Conclusion

This systematic review identified eight studies examining basal free intracellular calcium ion concentrations and stimulated calcium responses in platelets and lymphocytes among individuals with bipolar disorder, compared primarily with healthy controls and, in some analyses, with individuals with unipolar depression or schizophrenia. However, quantitative synthesis was not possible because the studies did not report extractable numerical data in a sufficiently consistent form for meta-analysis. Qualitatively, the available evidence suggests there may be abnormalities in intracellular calcium regulation in bipolar disorder, including possible elevations in basal [Ca2+] and altered responses to 5-HT or thrombin, but findings were variable across cell types, comparators, and mood states. The main limitation of this review is the lack of usable quantitative reporting, which substantially restricts interpretation. Overall, the current evidence is suggestive but insufficient to support firm conclusions.

## Final Included Studies

- Corpus ID: 1423 | Elevated platelet intracellular calcium concentration in bipolar depression.
- Corpus ID: 1424 | Abnormal intracellular calcium ion concentration in platelets and lymphocytes of bipolar patients.
- Corpus ID: 1441 | Increased platelet intracellular calcium ion concentration is specific to bipolar disorder.
- Corpus ID: 1427 | Platelet and lymphocyte free intracellular calcium in affective disorders.
- Corpus ID: 1431 | Enhanced calcium response to serotonin in platelets from patients with affective disorders.
- Corpus ID: 1428 | Serotonin-induced platelet intracellular calcium mobilization in depressed patients.
- Corpus ID: 1433 | Serotonin-induced platelet intracellular calcium mobilization in various psychiatric disorders: is it specific to bipolar disorder?
- Corpus ID: 1429 | Resting and thrombin-stimulated cytosolic calcium in platelets of patients with alcoholic withdrawal, bipolar manic disorder and chronic schizophrenia.
