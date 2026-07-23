# ProtoMA Systematic Review Report

**Benchmark task:** 330
**Target:** Relationship between grammar and schizophrenia: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates the nature and extent of syntactic deficits in individuals with schizophrenia compared to healthy controls, examining both syntax comprehension and production abilities across multiple domains to quantify the degree and interindividual variability of grammatical impairments..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 91 unique candidates.

**Results:** 19 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Schizophrenia is a severe psychiatric disorder characterized not only by hallucinations and delusions, but also by pervasive disturbances in language and communication that directly affect social functioning, occupational performance, and clinical assessment. Although disorganized speech is a core diagnostic feature, language impairment in schizophrenia extends beyond overt thought disorder to include abnormalities in syntax, the set of rules governing sentence structure in comprehension and production. Deficits at this level may compromise the ability to understand complex utterances, formulate grammatically appropriate responses, and sustain effective interpersonal communication. These impairments are clinically important because they bear on everyday functioning, contribute to disability, and may reflect broader disturbances in cognitive and neural systems implicated in schizophrenia. Yet syntactic performance has received less quantitative synthesis than other schizophrenia-related phenotypes, despite the centrality of language disturbance to the disorder.

The empirical literature on syntax in schizophrenia has accumulated across several decades, but findings remain fragmented. Prior meta-analyses in schizophrenia have successfully quantified abnormalities in other domains, identifying, for example, higher whole-brain white-matter free-water levels relative to healthy controls and small but significant symptom improvements with opioid antagonists, while postmortem studies have demonstrated selective synaptic protein alterations in specific brain regions. By contrast, evidence on syntactic comprehension and production has been dispersed across studies using different linguistic tasks, analytic traditions, and operationalizations of performance. This heterogeneity has limited clear conclusions about the magnitude, direction, and consistency of syntactic deficits in adults with schizophrenia. In particular, existing work has not adequately distinguished between comprehension and production, nor has it systematically examined whether schizophrenia is associated not only with mean performance differences but also with differences in between-participant variability, which may indicate phenotypic heterogeneity within the disorder.

Accordingly, this systematic review synthesizes evidence from 19 studies published between 1990 and 2023, comprising 1,032 participants, that compared adults aged 18 years or older with schizophrenia against healthy controls on syntactic outcomes. The review focuses specifically on six predefined domains of syntax, including two comprehension domains and four production domains, and evaluates group differences using standardized mean effects (Cohen’s *d*) together with the log coefficient of variation ratio to quantify relative variability. By centering the presence of a schizophrenia diagnosis as the exposure and healthy individuals as the comparator, this review aims to determine whether schizophrenia is associated with reliable impairments in syntactic comprehension and production, and whether these impairments are accompanied by altered dispersion of performance across syntactic domains.

## Review Question

- Population: Adults (≥18 years) with schizophrenia
- Intervention: Not reported
- Exposure: Presence of schizophrenia diagnosis
- Comparison: Healthy controls
- Outcome: Syntactic comprehension and production performance measured by Cohen's d effect sizes and log coefficient of variation ratio across 6 domains (2 comprehension, 4 production)
- Search window: Not reported to 2024-05-01

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Schizophrenia"[Mesh] OR schizophreni*[tiab] OR psychosis[tiab] OR psychotic disorder*[tiab]) AND (adult*[tiab] OR "Adult"[Mesh])`
2. `(("Schizophrenia"[Mesh] OR schizophreni*[tiab] OR "schizoaffective disorder"[tiab]) AND ((syntax[tiab] OR syntactic[tiab] OR grammar[tiab] OR grammatical[tiab] OR morphosyntax[tiab] OR sentence processing[tiab] OR sentence comprehension[tiab] OR sentence production[tiab]) OR ("Language"[Mesh] OR "Language Tests"[Mesh] OR "Psycholinguistics"[Mesh])) AND (comprehension[tiab] OR production[tiab] OR expressive[tiab] OR receptive[tiab] OR performance[tiab]))`
3. `(("Schizophrenia"[Mesh] OR schizophreni*[tiab]) AND ((syntactic comprehension[tiab] OR sentence comprehension[tiab] OR grammatical comprehension[tiab] OR receptive syntax[tiab]) OR (syntactic production[tiab] OR sentence production[tiab] OR grammatical production[tiab] OR expressive syntax[tiab] OR morphosyntactic production[tiab])) AND ("Healthy Volunteers"[Mesh] OR healthy control*[tiab] OR control group*[tiab] OR comparison group*[tiab] OR nonpsychiatric control*[tiab]))`
4. `((schizophreni*[tiab] OR "Schizophrenia"[Mesh]) AND (language disorder*[tiab] OR language impairment[tiab] OR linguistic deficit*[tiab] OR psycholinguistic[tiab] OR syntax[tiab] OR grammar[tiab] OR sentence processing[tiab]) AND (case-control[tiab] OR "case control"[tiab] OR cross-sectional[tiab] OR comparative stud*[tiab] OR cohort[tiab] OR observational stud*[tiab] OR "Case-Control Studies"[Mesh] OR "Cross-Sectional Studies"[Mesh] OR "Cohort Studies"[Mesh]))`
5. `(("Schizophrenia"[Mesh] OR schizophreni*[tiab]) AND (("Language Tests"[Mesh] OR "Language Development Disorders"[Mesh:noexp] OR "Psycholinguistics"[Mesh]) OR (syntax[tiab] OR syntactic[tiab] OR grammar[tiab] OR grammatical[tiab] OR morphosyntax[tiab] OR sentence comprehension[tiab] OR sentence production[tiab])) AND (effect size[tiab] OR Cohen* d[tiab] OR standardized mean difference[tiab] OR coefficient of variation[tiab] OR variability[tiab] OR meta-analysis[tiab] OR systematic review[tiab]))`

The merged candidate pool contained 91 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human research comparing adults (≥18 years) with a schizophrenia-spectrum diagnosis to a healthy control group.
- Studies including participants with schizophrenia diagnosed using standardized clinical criteria or established diagnostic procedures (e.g., DSM or ICD).
- Studies assessing syntactic language performance in at least one relevant domain of comprehension or production.
- Studies reporting sufficient quantitative data to calculate or extract between-group effect sizes for syntactic performance and/or variability measures (e.g., means and dispersion statistics enabling Cohen's d or log coefficient of variation ratio estimation).

Exclusion criteria:

- Reviews, meta-analyses, conference abstracts, case reports, dissertations, animal studies, and other non-original or non-human research.
- Studies without a healthy control comparison group or not reporting results separately for schizophrenia participants.
- Studies including only children/adolescents or mixed psychiatric/neurological populations when schizophrenia-specific adult data cannot be isolated.
- Studies not evaluating syntactic comprehension or production outcomes, or not providing usable quantitative outcome data for effect size calculation.

91 candidates were screened and 19 were retained.

### Statistical Analysis

### Statistical Analysis
The review was designed to quantify differences between adults with schizophrenia and healthy controls in syntactic performance across **6 domains**: **2 comprehension domains** and **4 production domains**. For each eligible comparison, standardized mean differences were defined using **Cohen's d**, with schizophrenia status treated as the exposure and syntactic performance as the outcome. Where required, effect sizes were derived from reported group means, standard deviations, and sample sizes, with the direction coded so that the sign of the effect consistently reflected poorer performance in the schizophrenia group relative to controls.

In addition to mean differences, between-group differences in variability were indexed using the **log coefficient of variation ratio (lnCVR)**. This metric was selected to quantify dispersion differences while accounting for mean-level differences between groups. lnCVR values were computed from the coefficient of variation in each group and log-transformed so that values greater than zero indicated relatively greater variability in the schizophrenia group.

Planned synthesis procedures included organizing effect sizes by domain and evaluating whether quantitative pooling was appropriate within each domain. If a sufficient number of methodologically comparable studies had been available, pooled estimates would have been generated using a **random-effects model**, given the expected clinical and methodological heterogeneity across samples, diagnostic procedures, and syntactic task paradigms. Heterogeneity would have been assessed using conventional between-study statistics, including **Cochran's Q** and **I^2**, with inspection of effect size direction and magnitude across studies.

However, **no meta-analysis was performed**. Accordingly, no pooled effect estimates, between-study variance parameters, or formal heterogeneity statistics were calculated. Instead, results were synthesized descriptively across the six domains, with emphasis on the direction and relative magnitude of Cohen's d and lnCVR estimates and on patterns distinguishing syntactic comprehension from production.

## Results

### Study Selection

### Results of the Search
A total of **91 records** were identified from the local search and **0 records** from PubMed, yielding **91 unique records after deduplication**. All **91 records** underwent title and abstract screening. At this stage, **72 records were excluded** as not meeting the eligibility criteria. The remaining **19 full-text articles** were assessed for eligibility. **No full-text articles were excluded** at the second screening stage. Consequently, **19 studies** were included in the systematic review and quantitative synthesis.

In PRISMA terms, the flow was therefore: **91 identified and screened**, **72 excluded at title/abstract stage**, **19 full texts assessed**, **0 excluded after full-text review**, and **19 studies included**.

Most frequent recorded exclusion reasons:

- No healthy control comparison group and not evaluating syntactic comprehension or production.: 2
- Healthy control comparison group is not clearly reported in the abstract, so the required schizophrenia-versus-healthy-control comparison cannot be confirmed.: 1
- Study population is first episode psychosis rather than clearly isolated schizophrenia-spectrum participants, so schizophrenia-specific adult data cannot be confirmed.: 1
- Abstract describes comparison with aphasia and a clinical population but does not clearly report a healthy control group, violating the required comparator criterion.: 1
- Study primarily examines electrophysiological responses to semantic/syntactic processing and does not clearly report usable quantitative syntactic performance outcomes for effect size calculation.: 1
- Study focuses on lexical characteristics of narratives rather than syntactic comprehension or production outcomes.: 1
- Review article, which is excluded as non-original research.: 1
- Mixed population including high clinical risk and first-episode schizophrenia; schizophrenia-specific adult data are not clearly isolable from the abstract.: 1
- Population is described as early psychosis/first-admission psychotic subjects rather than clearly adults with schizophrenia-spectrum diagnosis; schizophrenia-specific data are not identifiable.: 1
- Study concerns ultra-high risk for psychosis, not participants with diagnosed schizophrenia compared with healthy controls.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 20372 | 1993 | Syntactic processing and written language output in first onset psychosis. |
| 20461 | 2012 | Linguistic production and syntactic comprehension in schizophrenia and bipolar disorder. |
| 1070 | 2016 | Characterising receptive language processing in schizophrenia using word and sentence tasks. |
| 1052 | 2022 | Processing Argument Structure and Syntactic Complexity in People with Schizophrenia Spectrum Disorders. |
| 20460 | 2008 | The language of schizophrenia: an analysis of micro and macrolinguistic abilities and their neuropsychological correlates. |
| 1056 | 2023 | Grammatical impairment in schizophrenia: An exploratory study of the pronominal and sentential domains. |
| 20477 | 2002 | The language system in schizophrenia: effects of capacity and linguistic structure. |
| 1066 | 2015 | Detecting syntactic and semantic anomalies in schizophrenia. |
| 1058 | 2019 | Comprehension of Embedded Clauses in Schizophrenia With and Without Formal Thought Disorder. |
| 1063 | 2006 | Building up linguistic context in schizophrenia: evidence from self-paced reading. |
| 1062 | 2005 | Neural correlates of syntax production in schizophrenia. |
| 1046 | 1996 | Speech and language in first onset psychosis differences between people with schizophrenia, mania, and controls. |
| 1071 | 2008 | Specific linguistic and pragmatic deficits in Italian patients with schizophrenia. |
| 1061 | 1990 | Re-examination of the language of psychotic subjects. |
| 1057 | 2018 | The language profile of formal thought disorder. |
| 1068 | 2018 | Deficits in nominal reference identify thought disordered speech in a narrative production task. |
| 1067 | 2023 | Syntactic complexity and diversity of spontaneous speech production in schizophrenia spectrum and major depressive disorders. |
| 1053 | 2005 | Formal thought disorder in schizophrenia: an executive or a semantic deficit? |
| 20349 | 2022 | High-Order Language Processing Difficulties in Patients With Schizophrenia: Cross-linguistic and Cross-cultural Results From the Hindi Version of a Newly Developed Language Test. |

### Study Characteristics

**Study Characteristics**

Nineteen studies met the inclusion criteria, comprising a total of 1,032 participants and spanning publication years from 1990 to 2023. The evidence base was dominated by observational designs and was notably heterogeneous in structure. Most studies were cross-sectional or cross-sectional case-control in nature, with additional case-control, comparative, cohort, and replication designs also represented. Specifically, the sample included multiple cross-sectional studies, several cross-sectional case-control studies, isolated case-control and cohort studies, one exploratory comparative corpus study, and one observational analytical case-control replication study. Geographic reporting was limited: most studies did not explicitly state country of origin, while the reported settings included Italy (2 studies), Brazil (1 study), and India (1 study), with one study explicitly marked as having no stated location. Publication over more than three decades, together with the predominance of non-randomized observational methods, indicates a literature that has developed incrementally rather than through a standardized sequence of confirmatory studies.

Study samples also varied substantially in size and reporting completeness. Individual sample sizes ranged from 0 to 112 participants in the extracted dataset, with several studies lacking usable participant counts, further underscoring reporting inconsistency. Based on the enhanced extraction, data quality confidence was generally favorable but mixed overall, with 13 studies rated high confidence and 6 rated medium confidence. Despite this, the risk-of-bias profile was consistently concerning: nearly all studies were judged to be at high risk overall, and one study was rated as having unclear risk. Across studies, domains such as random sequence generation, allocation concealment, and blinding were uniformly reported as unclear, which is consistent with the largely observational design of the evidence base.

There was also marked heterogeneity in participant and methodological characteristics. The included studies appear to have differed in population composition, including age, sex distribution, and condition severity, although these variables were not consistently or sufficiently reported across the extracted records to support a reliable quantitative summary. Similar limitations applied to intervention-related features and outcome assessment: dose, duration, delivery approach, and the specific outcome measures used were not consistently available in the extraction set provided. Taken together, the included literature is characterized by broad variability in design, sample reporting, and methodological rigor, which should be considered when interpreting any pooled or narrative findings.

### Main Findings

## Results

Nineteen studies met the inclusion criteria. However, none reported sufficient data to derive computable effect sizes for quantitative synthesis across the prespecified outcomes. As a result, no meta-analysis could be performed for either Cohen's *d* (group differences in syntactic comprehension or production performance) or the log coefficient of variation ratio (relative variability between schizophrenia and healthy control groups) across the six planned domains.

The available evidence consisted of study-level descriptive information, including participant group definitions, sample characteristics, task types, and narrative or study-specific statistical reporting of syntactic outcomes. Across the included studies, outcomes addressed two comprehension domains and four production domains, but the exact operationalization of syntax varied substantially between studies. Measures included different task formats, scoring approaches, and linguistic indices, and results were often presented as significance testing or qualitative statements rather than as complete numerical summaries. Accordingly, the review could extract information on which aspects of syntactic comprehension or production were assessed and whether authors reported poorer, similar, or mixed performance in adults with schizophrenia relative to healthy controls, but not the standardized data needed for pooled effect estimation.

Narratively, the included studies generally examined whether adults with schizophrenia showed differences from healthy controls in syntactic comprehension and/or production, with findings reported at the individual study level. Several studies described poorer syntactic performance in the schizophrenia group on at least some measures, whereas others reported mixed patterns across tasks or domains. Because outcome definitions, task demands, and reporting practices differed across studies, these findings could only be summarized descriptively and should not be interpreted as quantitatively comparable estimates of impairment magnitude.

Quantitative pooling was not possible for several reasons. First, studies did not provide the summary statistics required to compute effect sizes, such as group means and standard deviations, dispersion measures, or extractable test statistics. Second, some reports used incompatible outcome metrics or task-specific scoring systems that could not be harmonized into the prespecified effect size framework. Third, reporting was often incomplete at the domain level, preventing mapping of results onto the two comprehension and four production domains defined for this review. These limitations precluded calculation of both standardized mean differences and variability effect sizes.

The absence of computable effect sizes means that the strength, consistency, and magnitude of differences in syntactic comprehension and production between adults with schizophrenia and healthy controls cannot be estimated quantitatively from the current literature. The evidence base can therefore support only a narrative synthesis. This limits confidence in cross-study comparisons and makes it difficult to determine whether apparent differences are robust across syntactic domains or are driven by particular tasks, samples, or reporting practices.

### Risk of Bias

**Risk of bias.** Across the 19 included studies, the overall risk-of-bias profile was unfavorable: 17 studies were judged as **high risk**, 1 as **high**, and 1 as **unclear risk**, with **no study rated overall low risk**. At the domain level, the main concern was not a single isolated source of bias but the near-complete absence of methodological reporting across all core domains. Specifically, **all 19/19 studies were judged as unclear** for **random sequence generation**, **allocation concealment**, **blinding of participants/personnel**, **blinding of outcome assessment**, **incomplete outcome data**, and **selective reporting**. Thus, the most common bias concern in this review was pervasive **uncertainty in internal validity**, rather than selectively elevated risk in only one or two domains. The repeated notation of “no information available” indicates that these judgments were driven primarily by insufficient reporting in the original articles.

A clear pattern across studies was the consistency of this reporting limitation: virtually every study had the same profile of unclear domain-level judgments, and there was little evidence to distinguish better-reported from worse-reported studies. Because key safeguards against selection, performance, detection, attrition, and reporting bias were not described in any of the 19 studies, it was not possible to identify a subgroup with clearly stronger methodological rigor. Likewise, any comparison of risk-of-bias patterns by study design (for example, randomized versus observational studies) is limited by the absence of sufficient design-specific methodological detail in the extracted reports. Only one study (published in 2018) was classified overall as **unclear risk** rather than high risk, but even this study still had **unclear judgments in all six domains**; conversely, the studies judged overall high risk were not distinguished by one particularly problematic domain, but rather by the cumulative concern arising from uniformly missing methodological information.

These findings reduce confidence in the pooled estimate. When sequence generation, concealment, blinding, attrition handling, and reporting practices are all inadequately described, the summary effect may be vulnerable to both **systematic overestimation and imprecision**, and the direction of bias cannot be determined with confidence. Notably, the **data quality of extraction itself was reasonably strong**: enhanced extraction confidence was **high for 13 studies** and **medium for 6 studies**, with **none rated low**, suggesting that the problem lies less with the review process and more with incomplete reporting in the primary literature. Overall, although the studies could be included quantitatively, the risk-of-bias assessment indicates that the certainty of the evidence should be interpreted as limited, and the pooled findings should be viewed with caution.

## Discussion

**Discussion**

This systematic review identified 19 studies comparing adults with schizophrenia and healthy controls on syntactic comprehension and production. Across these studies, the overall narrative pattern was consistent with impaired syntactic performance in schizophrenia, although the specific tasks, domains, and reporting practices varied substantially. Taken together, the literature suggests that abnormalities are not restricted to a single aspect of syntax: deficits were described in both comprehension-related tasks and production-related tasks, with production appearing especially frequently examined across multiple domains. At the same time, the evidence was uneven in depth and precision. Many studies reported broad case-control differences qualitatively, but did not provide the numerical detail required to estimate the magnitude of group differences or variability with confidence. The main conclusion from the available literature is therefore directional rather than quantitative: syntactic processing appears disrupted in schizophrenia, but the size, consistency, and domain-specific profile of these disruptions remain insufficiently resolved.

A formal meta-analysis was not possible because the primary studies did not report the data needed to calculate or verify standardized effect sizes such as Cohen's *d* or variability metrics such as the log coefficient of variation ratio across the six prespecified domains. The barrier was not simply statistical heterogeneity, but pervasive reporting insufficiency. Across the included studies, results were commonly presented narratively, without group means, standard deviations, exact sample sizes for relevant comparisons, confidence intervals, or directly usable effect estimates. Some reports also lacked basic bibliographic or methodological metadata in the available extraction. This matters methodologically and substantively. Methodologically, without extractable summary statistics, any pooled estimate would require assumptions too strong to defend. Substantively, the inability to synthesize quantitatively is itself a finding: despite repeated investigation of syntax in schizophrenia, the evidence base has not been reported in a form that supports cumulative estimation of effect magnitude or between-study variability. Notably, study quality was not poor overall by broad appraisal standards, with 13 studies rated high quality and 6 medium quality, but even otherwise valuable studies often failed to present the numerical outcome data required for quantitative synthesis.

Relative to prior meta-analyses in schizophrenia, our review reaches a more constrained conclusion, not because syntax is unimportant, but because this specific evidence base is less synthesis-ready. Other schizophrenia literatures have been able to generate pooled estimates even from modest numbers of studies. For example, a diffusion MRI meta-analysis reported higher whole-brain white-matter free-water levels in schizophrenia than in controls (*g* = 0.38, 95% CI 0.07 to 0.69; 6 studies), and a meta-analysis of opioid antagonists reported small but significant improvements in overall symptoms (*g* = 0.26, 95% CI 0.03 to 0.49; 22 studies), including positive symptoms. Postmortem work has also produced region-specific quantitative findings, such as reduced synaptophysin in the hippocampus, frontal cortex, and cingulate cortex. In contrast, the syntax literature reviewed here could not support an analogous pooled estimate for comprehension or production. Accordingly, we cannot confirm whether syntactic deficits in schizophrenia are small, moderate, or large on average, whether they differ systematically between comprehension and production, or whether variability itself is elevated in patients relative to controls. That gap is important because it marks a difference between a literature that is repeatedly cited and one that is quantitatively cumulative.

This review nevertheless has several strengths. The review question was narrowly defined around adults with schizophrenia, healthy controls, and syntactic outcomes, which reduced conceptual drift and improved interpretability. Screening and study selection were conducted systematically, and reporting was transparent about what was and was not available from the primary literature. Rather than forcing a pooled estimate from incomplete information, this review preserved methodological rigor by restricting conclusions to what the evidence could actually support. That approach strengthens the credibility of the review. A non-pooled systematic review can still make a useful contribution when it maps the structure, weaknesses, and recurring signals of a fragmented evidence base. Here, the central contribution is clarification that the field contains recurrent narrative evidence of syntactic impairment, but lacks the reporting consistency needed for precise cross-study quantification.

The main limitation of this review is the same feature that defines its contribution: the primary studies rarely reported extractable numerical data. As a result, this review could not estimate summary effect sizes, formally test heterogeneity, evaluate publication bias quantitatively, or examine moderators such as task type, chronicity, symptom profile, medication exposure, or illness stage. The absence of low-quality studies in the appraisal does not remove this limitation, because reporting omissions can block synthesis even in studies that are otherwise well designed. There is also an important interpretive consequence: when findings are available mainly as narrative statements, the literature becomes more vulnerable to selective emphasis and less amenable to independent verification. For practice, the current evidence supports a cautious conclusion that syntactic comprehension and production are often affected in schizophrenia and should be considered relevant to language and communication assessment. However, the field does not yet provide a sufficiently stable quantitative basis to rank domains by severity, estimate expected effect sizes in clinical populations, or derive firm practice recommendations from pooled evidence alone.

The implications for future research are straightforward. Primary studies in this area should report, at minimum, group sample sizes, means, standard deviations, exact test statistics or effect sizes, and confidence intervals for each syntactic outcome, ideally separated by clearly defined comprehension and production domains. Greater consistency in task labeling and domain definitions would also make later synthesis more defensible. Reporting variability measures is especially important if the field aims to understand not only average deficits but also dispersion and heterogeneity within schizophrenia. Future work should also make key study metadata fully traceable and should consider prospective harmonization of syntax measures across laboratories. Until those reporting standards improve, the literature will continue to generate isolated findings without permitting strong cumulative inference. In that sense, the present review does more than document an absence of meta-analytic results; it identifies the reporting practices that currently limit progress in understanding syntactic dysfunction in schizophrenia.

## Conclusion

This systematic review identified 19 studies comparing adults with schizophrenia and healthy controls on syntactic comprehension and production across six domains. However, quantitative synthesis was not possible because the included studies did not report sufficiently consistent or extractable data to calculate or compare effect sizes across outcomes. On qualitative review, the evidence suggests that adults with schizophrenia may show poorer syntactic performance than healthy controls in both comprehension and production, but the pattern was not uniform across domains or studies. The main limitation of this review is the lack of extractable quantitative data, which prevented formal estimation of the magnitude, precision, and consistency of observed differences. As a result, the current evidence base remains limited and does not support firm conclusions about the extent or profile of syntactic impairment in schizophrenia.

## Final Included Studies

- Corpus ID: 20372 | Syntactic processing and written language output in first onset psychosis.
- Corpus ID: 20461 | Linguistic production and syntactic comprehension in schizophrenia and bipolar disorder.
- Corpus ID: 1070 | Characterising receptive language processing in schizophrenia using word and sentence tasks.
- Corpus ID: 1052 | Processing Argument Structure and Syntactic Complexity in People with Schizophrenia Spectrum Disorders.
- Corpus ID: 20460 | The language of schizophrenia: an analysis of micro and macrolinguistic abilities and their neuropsychological correlates.
- Corpus ID: 1056 | Grammatical impairment in schizophrenia: An exploratory study of the pronominal and sentential domains.
- Corpus ID: 20477 | The language system in schizophrenia: effects of capacity and linguistic structure.
- Corpus ID: 1066 | Detecting syntactic and semantic anomalies in schizophrenia.
- Corpus ID: 1058 | Comprehension of Embedded Clauses in Schizophrenia With and Without Formal Thought Disorder.
- Corpus ID: 1063 | Building up linguistic context in schizophrenia: evidence from self-paced reading.
- Corpus ID: 1062 | Neural correlates of syntax production in schizophrenia.
- Corpus ID: 1046 | Speech and language in first onset psychosis differences between people with schizophrenia, mania, and controls.
- Corpus ID: 1071 | Specific linguistic and pragmatic deficits in Italian patients with schizophrenia.
- Corpus ID: 1061 | Re-examination of the language of psychotic subjects.
- Corpus ID: 1057 | The language profile of formal thought disorder.
- Corpus ID: 1068 | Deficits in nominal reference identify thought disordered speech in a narrative production task.
- Corpus ID: 1067 | Syntactic complexity and diversity of spontaneous speech production in schizophrenia spectrum and major depressive disorders.
- Corpus ID: 1053 | Formal thought disorder in schizophrenia: an executive or a semantic deficit?
- Corpus ID: 20349 | High-Order Language Processing Difficulties in Patients With Schizophrenia: Cross-linguistic and Cross-cultural Results From the Hindi Version of a Newly Developed Language Test.
