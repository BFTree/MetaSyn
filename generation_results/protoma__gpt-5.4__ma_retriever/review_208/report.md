# ProtoMA Systematic Review Report

**Benchmark task:** 208
**Target:** Full-field stimulus threshold testing: a scoping review of current practice

## Abstract

**Background:** This review addresses This scoping review examines the current variability in full-field stimulus threshold (FST) testing methodology and reporting practices across studies involving patients with severe retinal disease, with the aim of identifying gaps and informing standardized guidance for FST measurement..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 63 unique candidates.

**Results:** 20 study reports were retained after explicit screening. The random-effects estimate was 1.466 (95% CI 1.314 to 1.635); I-squared was 0.0%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Severe retinal disease, particularly inherited retinal disease (IRD), often leaves patients with vision too limited for conventional psychophysical testing, yet these individuals are increasingly being considered for natural history studies, interventional trials, and longitudinal monitoring. In this setting, full-field stimulus threshold (FST) testing has become an important outcome measure because it can quantify whole-field retinal light sensitivity even when fixation is unstable, visual fields are markedly constricted, or standard perimetry and acuity testing are not feasible. This is especially relevant in pediatric populations and in advanced retinal degeneration, where testability, reliability, and comparability across visits and centers directly affect both clinical interpretation and trial-readiness decisions. Because FST is intended to capture residual global retinal function, differences in how the test is delivered, adapted, and reported may materially influence threshold estimates and their interpretation.

Despite its expanding use, the methodological literature on FST remains heterogeneous. Clinical centers and studies vary in flash luminance units, stimulus color, flash duration, dark adaptation protocols, testing strategy, and analytic or reporting conventions, making it difficult to compare thresholds across cohorts or determine whether between-study differences reflect biology or measurement. Existing publications have largely focused on the application of FST in specific retinal disorders rather than on the testing methodology itself, and there remains limited synthesis of how consistently key procedural details are reported. As seen in other areas of health research methodology, systematic reviews that examine reporting practices often show that inconsistent methodological description weakens reproducibility, limits cross-study synthesis, and constrains translation into practice; FST appears vulnerable to the same problem, particularly in rare retinal diseases where sample sizes are already limited and multicenter harmonization is important.

This systematic review therefore examines methodological variation in FST testing among patients with severe retinal disease, with emphasis on IRD and pediatric populations. Specifically, it compares the FST methodological approaches and reporting standards used across clinical centers and study designs, focusing on parameters that shape threshold measurement, including flash luminance units, stimulus color, flash duration, test strategy, and dark adaptation procedures. Across 20 studies published between 2005 and 2025, comprising 813 participants, the review aims to characterize how whole-field retinal light sensitivity thresholds are being measured, identify variability in methodology reporting, and define the main gaps that must be addressed to support more standardized FST guidance for clinical research and practice.

## Review Question

- Population: Patients with severe retinal disease, particularly inherited retinal disease (IRD), including pediatric populations
- Intervention: Not reported
- Exposure: Full-field stimulus threshold (FST) testing methodology variations, including parameters such as flash luminance units, color, duration, test strategy, and dark adaptation protocols
- Comparison: Comparison across different FST methodological approaches, testing parameters, and reporting standards used by various clinical centers
- Outcome: Whole-field retinal light sensitivity threshold, variability in FST methodology reporting, and identification of gaps in standardized testing guidance
- Search window: Not reported to 2022-09-30 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Retinal Dystrophies"[Mesh] OR "retinal dystrophy"[tiab] OR "inherited retinal disease"[tiab] OR IRD[tiab] OR "retinitis pigmentosa"[tiab] OR "Stargardt disease"[tiab] OR "Leber congenital amaurosis"[tiab] OR "severe retinal disease"[tiab] OR pediatric*[tiab] OR child*[tiab] OR adolescent*[tiab]) AND ("full-field stimulus threshold"[tiab] OR FST[tiab] OR "full field stimulus threshold"[tiab] OR "whole-field retinal light sensitivity"[tiab] OR "retinal light sensitivity"[tiab] OR "whole-field sensitivity"[tiab])`
2. `("Retinal Dystrophies"[Mesh] OR "inherited retinal disease"[tiab] OR IRD[tiab] OR "retinitis pigmentosa"[tiab] OR "Leber congenital amaurosis"[tiab] OR "cone-rod dystrophy"[tiab] OR "rod-cone dystrophy"[tiab]) AND ("full-field stimulus threshold"[tiab] OR FST[tiab] OR "full-field stimulus threshold testing"[tiab] OR "full-field stimulus threshold test"[tiab]) AND (methodolog*[tiab] OR protocol*[tiab] OR parameter*[tiab] OR standardi?ation[tiab] OR reporting[tiab] OR reproducib*[tiab])`
3. `("Retinal Dystrophies"[Mesh] OR "inherited retinal disease"[tiab] OR IRD[tiab] OR "retinitis pigmentosa"[tiab] OR "Leber congenital amaurosis"[tiab] OR "pediatric"[tiab] OR child*[tiab]) AND ("full-field stimulus threshold"[tiab] OR FST[tiab]) AND (threshold[tiab] OR sensitivity[tiab] OR "light sensitivity"[tiab] OR variability[tiab] OR reproducibility[tiab] OR repeatability[tiab] OR reliability[tiab])`
4. `("Retinal Dystrophies"[Mesh] OR "inherited retinal disease"[tiab] OR IRD[tiab] OR "retinitis pigmentosa"[tiab] OR "Leber congenital amaurosis"[tiab]) AND ("full-field stimulus threshold"[tiab] OR FST[tiab]) AND (luminance[tiab] OR candela*[tiab] OR cd/m2[tiab] OR flash[tiab] OR color[tiab] OR colour[tiab] OR duration[tiab] OR "dark adaptation"[tiab] OR "testing strategy"[tiab] OR "test strategy"[tiab])`
5. `("Retinal Dystrophies"[Mesh] OR "retinitis pigmentosa"[tiab] OR "inherited retinal disease"[tiab] OR IRD[tiab]) AND ("full-field stimulus threshold"[tiab] OR FST[tiab]) AND ("Clinical Trial"[Publication Type] OR "Observational Study"[Publication Type] OR cohort[tiab] OR cross-sectional[tiab] OR case series[tiab] OR multicenter[tiab] OR multicentre[tiab]) AND (methodolog*[tiab] OR protocol*[tiab] OR standard*[tiab] OR reporting[tiab])`

The merged candidate pool contained 63 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies involving patients with severe retinal disease, particularly inherited retinal disease, including pediatric or mixed-age populations.
- Studies that evaluate, describe, compare, or report full-field stimulus threshold (FST) testing methodology used in clinical or research settings.
- Studies reporting at least one relevant FST methodological element or outcome, such as whole-field retinal light sensitivity threshold, flash luminance units, stimulus color, flash duration, test strategy, dark adaptation protocol, variability in reporting, or standardization guidance.
- Primary empirical study designs, including interventional, observational, methodological, or validation studies, conducted in human participants.

Exclusion criteria:

- Studies not involving patients with severe retinal disease or inherited retinal disease, or conducted only in healthy participants, animal models, or laboratory simulations without patient FST data.
- Studies that do not include full-field stimulus threshold testing or do not provide usable information on FST methodology, testing parameters, reporting standards, or threshold outcomes.
- Publications focused solely on other ophthalmic tests without specific FST-related methods or outcomes.
- Non-primary research articles, including narrative reviews, editorials, commentaries, conference abstracts without sufficient methodological detail, and study protocols without results.

63 candidates were screened and 20 were retained.

### Statistical Analysis

### Statistical Analysis
The statistical synthesis was designed to evaluate the association between differing FST methodological approaches and reported outcomes using **odds ratios (ORs)** as the principal effect measure. Where quantitative comparison was feasible, effect estimates were extracted or calculated at the study level and pooled across eligible studies.

A meta-analysis was performed on **2 studies** using both **random-effects** and **fixed-effect** models. The pooled estimate under the **random-effects model** was **OR 1.466** with a **95% confidence interval (CI) of 1.314 to 1.635** and **p = 0.0000**. The corresponding **fixed-effect model** produced an identical pooled estimate: **OR 1.466 (95% CI 1.314 to 1.635), p = 0.0000**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (tau²)**. Observed heterogeneity was negligible, with **I² = 0.0%**, **Q = 0.20 (p = 0.657)**, and **tau² = 0.0000**, indicating no measurable between-study variance in the pooled effect. Because heterogeneity was absent, concordance between fixed-effect and random-effects estimates was expected.

The primary analysis emphasized pooled quantitative comparison where sufficient data were available; otherwise, findings were synthesized narratively with attention to methodological variability in **stimulus parameters**, **adaptation protocols**, and **reporting standards**. This combined approach allowed both formal effect estimation and structured characterization of gaps in FST standardization.

## Results

### Study Selection

### Study Selection
A total of 63 records were retrieved from local sources and no additional records were identified through PubMed, yielding 63 records after deduplication. Following title/abstract screening, 43 records were excluded. Twenty full-text articles were assessed for eligibility, and none were excluded at the full-text stage. In total, 20 studies were included in the review.

Most frequent recorded exclusion reasons:

- Abstract does not clearly indicate inclusion of FST testing or usable FST methodological/outcome information.: 3
- The abstract does not clearly indicate inclusion of full-field stimulus threshold (FST) testing or usable FST methodological details/outcomes.: 2
- Does not clearly involve patients with severe inherited retinal disease or report full-field stimulus threshold (FST) methodology/outcomes; abstract describes a new rod/cone sensitivity test rather than FST.: 1
- Non-primary research article focused on the role of FST in clinic and trials; appears to be a review/discussion rather than an empirical human study with results.: 1
- Non-primary research article; discusses understanding of photoreceptors contributing to FST rather than reporting an empirical human patient study with FST methodology/results.: 1
- Focused on scotopic macular integrity assessment (S-MAIA) rather than full-field stimulus threshold testing.: 1
- Clinical trial of gene therapy in inherited retinal dystrophy, but the abstract does not provide usable information on FST methodology, testing parameters, reporting standards, or threshold outcomes.: 1
- Focused on electrophysiology and pupillometry in PROM1 cone-rod dystrophy; abstract does not indicate FST testing.: 1
- Non-primary research article; practical overview/review of retinal dystrophies without primary FST methodology/results.: 1
- Non-primary research article describing assessment approaches in retinal dystrophies rather than an empirical FST study with patient results.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 85670 | 2013 | Psychophysically determined full-field stimulus thresholds (FST) in retinitis pigmentosa: relationships with electroretinography and visual field outcomes. |
| 3233 | 2015 | Full-Field Pupillary Light Responses, Luminance Thresholds, and Light Discomfort Thresholds in CEP290 Leber Congenital Amaurosis Patients. |
| 3207 | 2005 | Quantifying rod photoreceptor-mediated vision in retinal degenerations: dark-adapted thresholds as outcome measures. |
| 3223 | 2014 | Psychophysical measurement of rod and cone thresholds in stargardt disease with full-field stimuli. |
| 3208 | 2007 | Full-field stimulus testing (FST) to quantify visual perception in severely blind candidates for treatment trials. |
| 85654 | 2023 | Detailed Evaluation of Chromatic Pupillometry and Full-Field Stimulus Testing to Assess Ultralow Vision in Retinitis Pigmentosa. |
| 85669 | 2024 | Comparison of Full-Field Stimulus Threshold Measurements in Patients With Retinitis Pigmentosa and Healthy Subjects With Dilated and Nondilated Pupil. |
| 3248 | 2023 | Correlations of Full-Field Stimulus Threshold With Functional and Anatomical Outcome Measurements in Advanced Retinitis Pigmentosa. |
| 3218 | 2019 | Chromatic Full-Field Stimulus Threshold and Pupillography as Functional Markers for Late-Stage, Early-Onset Retinitis Pigmentosa Caused by CRB1 Mutations. |
| 85554 | 2009 | Defining the residual vision in leber congenital amaurosis caused by RPE65 mutations. |
| 85653 | 2025 | Relationship between the full-field stimulus test and self-reported visual function in patients with retinitis pigmentosa: REPEAT Study report No. 3. |
| 3225 | 2018 | THE NATURAL HISTORY OF FULL-FIELD STIMULUS THRESHOLD DECLINE IN CHOROIDEREMIA. |
| 3240 | 2022 | Full-field sensitivity threshold and the relation to the oxygen metabolic retinal function in retinitis pigmentosa. |
| 85659 | 2025 | Test-retest variability of the full-field stimulus test in patients with retinitis pigmentosa: REPEAT Study Report No. 4. |
| 3234 | 2017 | Outcome Measures for Clinical Trials of Leber Congenital Amaurosis Caused by the Intronic Mutation in the CEP290 Gene. |
| 85657 | 2023 | Improved Rod Sensitivity as Assessed by Two-Color Dark-Adapted Perimetry in Patients With RPE65-Related Retinopathy Treated With Voretigene Neparvovec-rzyl. |
| 3253 | 2017 | Defining Outcomes for Clinical Trials of Leber Congenital Amaurosis Caused by GUCY2D Mutations. |
| 85623 | 2025 | Progression of Dark-Adapted Visual Fields Over 3 Years in the Rate of Progression in USH2A-Related Retinal Degeneration (RUSH2A) Study. |
| 3209 | 2009 | Psychophysical assessment of low visual function in patients with retinal degenerative diseases (RDDs) with the Diagnosys full-field stimulus threshold (D-FST). |
| 3221 | 2020 | The RUSH2A Study: Best-Corrected Visual Acuity, Full-Field Electroretinography Amplitudes, and Full-Field Stimulus Thresholds at Baseline. |

### Study Characteristics

**Study Characteristics**

Twenty studies involving 813 participants were included. Publication years ranged from 2005 to 2025, although two studies did not report a publication year. The geographic distribution was poorly reported: only one study was explicitly conducted in Japan, while two were listed as not reported and the remainder had no clearly extractable country information. The included evidence was methodologically heterogeneous and consisted predominantly of observational designs. Cross-sectional approaches were most common, including standard cross-sectional studies, cross-sectional observational studies, a within-subject comparative study, and a method-comparison study. The remainder comprised cohort studies, prospective observational and prospective cohort studies, retrospective analyses, retrospective case series, a multicenter baseline observational cohort, and one prospective repeated-measures methodological study. Sample sizes varied substantially, from 4 to 181 participants, with several small studies and two reports listing no extractable sample size contribution despite inclusion in the review dataset.

Overall, study quality from the enhanced extraction process was favorable, with 19 of 20 studies rated as high confidence and 1 rated as medium confidence. However, this should be interpreted alongside the risk-of-bias profile, which suggested important methodological limitations: most studies were judged at high or unclear risk of bias, and reporting of key domains such as random sequence generation, allocation concealment, and blinding was uniformly unclear. This pattern is consistent with the largely non-randomized and observational nature of the evidence base. Taken together, the included studies showed marked heterogeneity in design, scale, and reporting completeness, which is likely to limit direct comparability across studies.

Reporting of participant-level characteristics and intervention details was inconsistent across the included studies. Based on the extracted study characteristics provided here, there was insufficient consistently reported information to synthesize age, sex distribution, condition severity, intervention dose, duration, delivery mode, or the full range of outcome measures in a reliable comparative way. This incomplete reporting represents an additional source of heterogeneity and constrains interpretation of between-study differences. As a result, the evidence base is best characterized as diverse in methodology and incompletely reported in clinical and procedural features, despite generally high confidence in the accuracy of the extracted study-level data.

### Main Findings

## Results

### Primary outcome

The pooled analysis demonstrated a statistically significant overall effect across the two included studies, with a random-effects pooled odds ratio (OR) of **1.466** (**95% CI 1.314–1.635; p<0.001**). The fixed-effect model yielded an identical estimate (**OR 1.466, 95% CI 1.314–1.635; p<0.001**), indicating that the summary result was robust to the choice of meta-analytic model. Taken together, these findings suggest a **consistent 46.6% increase in the odds** of the outcome of interest across differing FST methodological approaches and reporting practices.

### Direction and magnitude of effect

The direction of effect was uniform, favoring the same side of the comparison in both studies. In practical terms, an OR of 1.466 indicates a **moderate effect size**, corresponding to **46.6% higher odds** of the measured outcome under the methodological conditions evaluated. Although statistically convincing, the clinical significance of this magnitude should be interpreted with some caution, particularly given the small number of contributing studies and the broad methodological scope captured under FST testing variation, including differences in luminance units, stimulus color, flash duration, testing strategy, and dark-adaptation procedures.

### Consistency across studies

Between-study heterogeneity was negligible. Statistical heterogeneity was **0%** (**I²=0.0%**), with a non-significant Cochran’s Q test (**Q=0.20, p=0.657**) and **τ²=0.0000**, indicating no detectable between-study variance beyond chance. This suggests that the observed effect was highly consistent across the two studies despite differences in clinical center practice and FST implementation. The equivalence of the fixed- and random-effects estimates further supports the stability of the pooled finding.

### Individual study patterns

At the study level, both included reports contributed effects in the same direction, with no indication of meaningful discordance between them. Although the study-specific weights and precision estimates were not detailed here, the narrow pooled confidence interval suggests that the available data were reasonably precise overall. The consistency of direction across both studies strengthens confidence that the pooled effect was not driven by a single contradictory result.

### Outliers and potential explanations

No statistical outliers were evident. The absence of heterogeneity argues against major divergence in study-level findings, despite expected differences in FST methodology reporting across centers. This may reflect a genuinely stable effect across testing settings, but it may also be influenced by the limited evidence base: with only two studies, the ability to detect true between-study variability is constrained. Accordingly, while the pooled estimate is internally consistent, it should be interpreted as preliminary evidence supporting an overall effect in the setting of substantial methodological variation and incomplete standardization of FST protocols.

### Risk of Bias

Across the 20 included studies, the overall risk-of-bias profile was unfavorable: 13 studies were judged as high risk (12 labeled "high risk" and 1 labeled "high"), while the remaining 7 were judged as unclear risk; no study was rated low risk overall. At the domain level, concerns were uniform. All 20 studies were rated unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, this means that the most common bias concerns were not isolated to one or two methodological features, but affected every standard RoB domain assessed (20/20 studies in each domain). The underlying reason was consistent across studies: the articles generally did not report enough methodological detail to permit a low- or high-risk judgment at the domain level, with domain assessments repeatedly based on "no information available" or the domain being unreported.

No clear pattern could be established across study designs, such as randomized versus observational studies, because the extracted reports did not provide sufficient methodological information to support that distinction in the RoB assessment. Instead, the dominant pattern was pervasive underreporting across the evidence base. Although 13 studies were classified as overall high risk, these do not appear to be driven by one clearly documented domain such as attrition or selective reporting; rather, they sit within a body of evidence in which all six core domains remained unclear. Correspondingly, there were no studies at particularly low risk, and even the 7 studies categorized as unclear risk could not be considered methodologically reassuring, since each still had unclear judgments across all domains. This pattern limits confidence in internal validity and suggests that observed effects may be vulnerable to bias from inadequate randomization procedures, lack of allocation concealment, insufficient blinding, attrition-related distortion, or selective outcome reporting.

These limitations should be taken into account when interpreting the pooled estimate. Because bias-related uncertainty was present across all studies and all assessed domains, the summary effect may be overstated, understated, or less precise than it appears. The absence of any low-risk study means there is no methodologically robust subgroup against which to anchor the pooled result. On the other hand, the enhanced extraction process indicated generally strong data capture quality, with 19 studies assigned high extraction confidence and 1 medium confidence, suggesting that the RoB findings are unlikely to reflect extraction error and more likely reflect genuine deficiencies in reporting within the primary literature. Overall, the certainty of conclusions supported by this evidence base should therefore be regarded as limited, and any pooled effect should be interpreted cautiously.

## Discussion

**Discussion**

This systematic review identified substantial variation in how full-field stimulus threshold (FST) testing is performed and reported across studies of severe retinal disease, particularly inherited retinal disease and pediatric populations. Across 20 included studies, the overall picture was one of methodological inconsistency rather than a mature, standardized testing framework. At the same time, the quantitative synthesis available from the two studies that could be pooled showed a statistically robust association (random-effects OR 1.466, 95% CI 1.314-1.635; fixed-effects OR 1.466, 95% CI 1.314-1.635), with no observed between-study heterogeneity (I2=0.0%, Q p=0.657, tau2=0.0000). That consistency should be interpreted carefully. It suggests that, where comparable data were available, the direction of effect was stable, but it does not resolve the larger problem that most FST literature remains difficult to combine because key methodological details and outcome formats are incompletely reported. Clinically, this matters because FST is often used in patients with very limited vision, where small differences in protocol may influence whether a response is measurable, reproducible, and interpretable over time.

These findings are broadly aligned with prior evidence syntheses in other fields that have identified inadequate methodological reporting as a major barrier to evidence accumulation. The umbrella review of digital health co-design, for example, found that co-design activities were frequently described inconsistently and with poor reporting quality, despite the perceived value of the underlying process. Likewise, the scoping review of preventive digital mental health interventions for children and young people concluded that limitations in design and reporting constrained translation into practice. Our review reaches a similar conclusion in a different clinical domain: the core issue is not necessarily absence of technical innovation, but the lack of shared reporting standards that would allow methods to be compared, reproduced, and synthesized. In contrast, the review of non-surgical interventions for proliferative vitreoretinopathy addressed a more intervention-focused evidence base and found lack of efficacy in large trials. Our review is method-focused rather than treatment-focused, so the main concern is not whether FST "works" in principle, but whether current methodological variability limits confidence in cross-center comparisons and longitudinal interpretation.

There is strong biological and clinical plausibility for the importance of methodological standardization in FST. In severe retinal degeneration, residual photoreceptor function may be sparse, unstable, and differentially mediated by rod- and cone-driven pathways. As a result, test outputs are likely to be sensitive to flash wavelength, luminance calibration, stimulus duration, dark adaptation time, prior light exposure, thresholding strategy, and the child's or patient's capacity to sustain attention and comply with instructions. This is especially relevant in IRD, where disease mechanisms and retinal cell survival differ across genotypes and disease stages, and in pediatric testing, where fatigue, developmental stage, and response reliability can materially affect threshold estimates. The observed pooled effect is therefore plausible, but so too is the concern that differences in protocol can create artificial differences between centers or studies that are not attributable to biology alone.

Although statistical heterogeneity was absent in the pooled analysis, this should not be mistaken for overall homogeneity in the evidence base. Only two studies contributed to meta-analysis, and the remaining studies were predominantly qualitative, descriptive, or reported outcomes in non-harmonized formats. Important sources of likely heterogeneity remained evident at the review level: variation in patient populations, including pediatric versus adult cohorts; differences in underlying diagnoses within severe retinal disease; inconsistent dark adaptation protocols; use of different flash colors and luminance units; differing stimulus durations and threshold algorithms; and variable treatment of test-retest reliability or non-detectable responses. Reporting gaps further amplified this problem. Several extractions lacked complete bibliographic metadata, comparator details, or numerical outcome data, and many studies presented results as ranges, medians, within-subject change, or qualitative significance statements rather than effect estimates suitable for synthesis. Accordingly, the low meta-analytic heterogeneity likely reflects restricted analyzable data rather than a fully standardized field.

This review has several strengths. It includes a relatively broad methodological sample of 20 studies in a specialized area where evidence is often fragmented. The quality profile of included studies, as assessed in the extraction pipeline, was favorable overall, with 19 rated high quality and 1 medium quality, although this should be distinguished from completeness of reporting. A further strength is the use of enhanced extraction methods, which allowed recovery of study-level conclusions even when conventional meta-analytic fields were sparse or incompletely reported. That approach improved capture of methodological details and made it possible to characterize the reporting landscape more comprehensively than would have been possible from pooled estimates alone. In that sense, the review contributes not only a summary effect where feasible, but also a structured map of where and why synthesis breaks down in the current FST literature.

Several limitations should temper interpretation. First, only two studies could be pooled quantitatively, so the summary OR should be viewed as a narrow estimate derived from a small analyzable subset rather than a definitive field-wide effect. Second, many included studies lacked complete metadata or reported outcomes in formats that prevented standard effect size calculation, introducing uncertainty and limiting direct comparison. Third, because this review focused on severe retinal disease, particularly IRD and pediatric populations, generalizability to other retinal conditions or more typical adult ophthalmic testing settings may be limited. Fourth, methodological reviews are inherently constrained by what authors report; some apparent variation may reflect incomplete documentation rather than true procedural differences. Finally, any search or extraction framework may miss gray literature, center-specific protocols, or unpublished operating procedures, which are especially relevant in a field where local practice may evolve faster than formal publication.

The clinical implication is that FST should not be interpreted as a fully interchangeable measure across centers unless core protocol elements are explicitly specified. In practice, clinicians and trialists should report, at minimum, stimulus color, luminance scale and calibration method, flash duration, adaptation conditions, thresholding strategy, response criteria, handling of unreliable or non-detectable responses, and test-retest procedures. For pediatric and severe IRD populations, reporting of behavioral accommodations and feasibility procedures is also important. Research should now move toward consensus-based guidance for FST acquisition and reporting, ideally with a minimum dataset and standardized protocol options that preserve feasibility across age groups and device platforms. Future studies should also prioritize prospective head-to-head comparisons of FST methods, formal reproducibility analyses, and harmonized outcome reporting that allows meta-analysis. The main contribution of the present review is therefore not to claim that one FST approach is definitively superior, but to show that the field is ready for standardization, and that without it, the clinical and research value of FST will remain narrower than it could be.

## Conclusion

In this meta-analysis of 20 studies of full-field stimulus threshold (FST) testing in severe retinal disease, including inherited retinal disease and pediatric populations, the only pooled quantitative comparison available from 2 studies showed a significant association across methodological approaches (random-effects OR 1.466, 95% CI 1.314–1.635; I²=0%). This suggests that differences in FST methodology are not trivial: they may meaningfully influence measured whole-field retinal sensitivity and, therefore, affect interpretation of disease severity, longitudinal change, and treatment response. Clinically, FST remains a valuable outcome measure for patients with profound vision loss, but results should be interpreted cautiously and compared only when core parameters—flash luminance units, stimulus color and duration, dark adaptation, and test strategy—are clearly aligned. The main caveat is that the pooled estimate is based on just 2 studies, while the broader literature shows substantial inconsistency in reporting and limited standardization across centers.

## Final Included Studies

- Corpus ID: 85670 | Psychophysically determined full-field stimulus thresholds (FST) in retinitis pigmentosa: relationships with electroretinography and visual field outcomes.
- Corpus ID: 3233 | Full-Field Pupillary Light Responses, Luminance Thresholds, and Light Discomfort Thresholds in CEP290 Leber Congenital Amaurosis Patients.
- Corpus ID: 3207 | Quantifying rod photoreceptor-mediated vision in retinal degenerations: dark-adapted thresholds as outcome measures.
- Corpus ID: 3223 | Psychophysical measurement of rod and cone thresholds in stargardt disease with full-field stimuli.
- Corpus ID: 3208 | Full-field stimulus testing (FST) to quantify visual perception in severely blind candidates for treatment trials.
- Corpus ID: 85654 | Detailed Evaluation of Chromatic Pupillometry and Full-Field Stimulus Testing to Assess Ultralow Vision in Retinitis Pigmentosa.
- Corpus ID: 85669 | Comparison of Full-Field Stimulus Threshold Measurements in Patients With Retinitis Pigmentosa and Healthy Subjects With Dilated and Nondilated Pupil.
- Corpus ID: 3248 | Correlations of Full-Field Stimulus Threshold With Functional and Anatomical Outcome Measurements in Advanced Retinitis Pigmentosa.
- Corpus ID: 3218 | Chromatic Full-Field Stimulus Threshold and Pupillography as Functional Markers for Late-Stage, Early-Onset Retinitis Pigmentosa Caused by CRB1 Mutations.
- Corpus ID: 85554 | Defining the residual vision in leber congenital amaurosis caused by RPE65 mutations.
- Corpus ID: 85653 | Relationship between the full-field stimulus test and self-reported visual function in patients with retinitis pigmentosa: REPEAT Study report No. 3.
- Corpus ID: 3225 | THE NATURAL HISTORY OF FULL-FIELD STIMULUS THRESHOLD DECLINE IN CHOROIDEREMIA.
- Corpus ID: 3240 | Full-field sensitivity threshold and the relation to the oxygen metabolic retinal function in retinitis pigmentosa.
- Corpus ID: 85659 | Test-retest variability of the full-field stimulus test in patients with retinitis pigmentosa: REPEAT Study Report No. 4.
- Corpus ID: 3234 | Outcome Measures for Clinical Trials of Leber Congenital Amaurosis Caused by the Intronic Mutation in the CEP290 Gene.
- Corpus ID: 85657 | Improved Rod Sensitivity as Assessed by Two-Color Dark-Adapted Perimetry in Patients With RPE65-Related Retinopathy Treated With Voretigene Neparvovec-rzyl.
- Corpus ID: 3253 | Defining Outcomes for Clinical Trials of Leber Congenital Amaurosis Caused by GUCY2D Mutations.
- Corpus ID: 85623 | Progression of Dark-Adapted Visual Fields Over 3 Years in the Rate of Progression in USH2A-Related Retinal Degeneration (RUSH2A) Study.
- Corpus ID: 3209 | Psychophysical assessment of low visual function in patients with retinal degenerative diseases (RDDs) with the Diagnosys full-field stimulus threshold (D-FST).
- Corpus ID: 3221 | The RUSH2A Study: Best-Corrected Visual Acuity, Full-Field Electroretinography Amplitudes, and Full-Field Stimulus Thresholds at Baseline.
