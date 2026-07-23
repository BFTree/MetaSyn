# ProtoMA Systematic Review Report

**Benchmark task:** 272
**Target:** The relationship between immune and cognitive dysfunction in mood and psychotic disorder: a systematic review and a meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates the association between blood-based immune markers (including inflammatory cytokines, kynurenine metabolites, and markers of microglial activation) and cognitive dysfunction in patients with psychotic and mood disorders, including schizophrenia spectrum disorder, bipolar disorder, and major depressive disorder..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 86 unique candidates.

**Results:** 31 study reports were retained after explicit screening. The random-effects estimate was 0.196 (95% CI -0.116 to 0.509); I-squared was 0.0%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Cognitive impairment is a core determinant of disability across schizophrenia spectrum disorder, bipolar disorder, and major depressive disorder. Deficits in global cognition and in specific domains such as attention, processing speed, working memory, verbal and visual memory, executive functioning, language, and social cognition are associated with poorer educational attainment, reduced occupational participation, impaired independent living, and diminished treatment response. These impairments often persist beyond acute symptom episodes and are only partly explained by mood or psychotic symptoms, suggesting that cognitive dysfunction reflects a clinically meaningful dimension of illness in its own right. In parallel, converging evidence implicates immune dysregulation in severe mental disorders, including altered pro-inflammatory and anti-inflammatory signaling, disturbances in kynurenine pathway metabolism, and abnormalities linked to microglial activation. Because these biological pathways may affect neuroplasticity, neurotransmission, and fronto-limbic as well as cortico-subcortical circuit function, they have emerged as plausible correlates of the cognitive deficits observed across major psychiatric disorders.

However, the evidence linking peripheral immune abnormalities to cognition in psychiatric populations remains difficult to interpret. Much of the literature has focused on case-control comparisons of biomarker levels between patients and healthy individuals, an approach that is informative for disease association but less suited to determining whether variation in immune markers tracks variation in cognitive performance within affected individuals. For clinical translation, within-patient correlational evidence is particularly important because it addresses whether patients with relatively greater inflammatory disturbance also show worse global or domain-specific cognition. Existing studies are heterogeneous with respect to diagnosis, illness phase, biomarker panels, cognitive batteries, and analytic methods, and findings have been inconsistent across inflammatory cytokines, composite inflammatory indices, kynurenine metabolites, and candidate markers of microglial activation. To date, no synthesis has specifically centered the evidence on within-sample associations across schizophrenia spectrum disorder, bipolar disorder, and major depressive disorder while examining both global cognition and individual cognitive domains.

Accordingly, this systematic review synthesizes 31 studies published between 2012 and 2026, comprising 11,013 participants with schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder. The review is designed to evaluate, within patient samples and without requiring a separate control comparison, whether blood-based immune markers—including pro-inflammatory and anti-inflammatory indices, inflammatory cytokines, kynurenine metabolites, and markers related to microglial activation—are associated with global cognitive performance and with domain-specific cognitive functioning across eight cognitive domains. By adopting a transdiagnostic framework while preserving diagnostic specificity where possible, this review aims to clarify the consistency, direction, and clinical relevance of immune-cognition associations in severe mental illness and to identify priorities for biomarker-informed mechanistic and therapeutic research.

## Review Question

- Population: Patients with schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder
- Intervention: Not reported
- Exposure: Blood-based immune markers including pro-inflammatory and anti-inflammatory indices, inflammatory cytokines, kynurenine metabolites, and markers of microglial activation
- Comparison: Within-patient correlational analysis (no separate control group; associations examined within patient samples)
- Outcome: Global cognitive performance and domain-specific cognitive functioning across eight cognitive domains
- Search window: Not reported to 2021-11-08

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Schizophrenia Spectrum and Other Psychotic Disorders"[Mesh] OR "Schizophrenia"[Mesh] OR schizophreni*[tiab] OR psychosis[tiab] OR psychotic disorder*[tiab] OR schizoaffective[tiab]) OR ("Bipolar Disorder"[Mesh] OR bipolar disorder*[tiab] OR manic-depress*[tiab]) OR ("Depressive Disorder, Major"[Mesh] OR major depressi*[tiab] OR MDD[tiab] OR unipolar depress*[tiab])) AND (("Inflammation Mediators"[Mesh] OR "Cytokines"[Mesh] OR "Biomarkers"[Mesh] OR inflamm*[tiab] OR immune marker*[tiab] OR immune biomarker*[tiab] OR cytokine*[tiab] OR interleukin*[tiab] OR TNF[tiab] OR "tumor necrosis factor"[tiab] OR CRP[tiab] OR "C-reactive protein"[tiab] OR chemokine*[tiab] OR kynurenine[tiab] OR tryptophan[tiab] OR kynurenic acid[tiab] OR quinolinic acid[tiab] OR neopterin[tiab] OR microglia*[tiab] OR sTREM2[tiab] OR YKL-40[tiab]))`
2. `(("Schizophrenia"[Mesh] OR schizophreni*[tiab] OR schizoaffective[tiab] OR psychosis[tiab]) OR ("Bipolar Disorder"[Mesh] OR bipolar[tiab]) OR ("Depressive Disorder, Major"[Mesh] OR major depressi*[tiab] OR unipolar depress*[tiab])) AND (("Blood"[Mesh] OR blood[tiab] OR serum[tiab] OR plasma[tiab] OR peripheral[tiab]) AND (cytokine*[tiab] OR interleukin*[tiab] OR IL-6[tiab] OR IL-1beta[tiab] OR TNF-alpha[tiab] OR CRP[tiab] OR "C-reactive protein"[tiab] OR inflammatory marker*[tiab] OR pro-inflammatory[tiab] OR anti-inflammatory[tiab] OR kynurenine[tiab] OR kynurenine pathway[tiab] OR tryptophan catabolite*[tiab] OR microglial activation[tiab])) AND (("Cognition"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR cognit*[tiab] OR neuropsychological test*[tiab] OR neurocognit*[tiab]) OR (memory[tiab] OR attention[tiab] OR executive function*[tiab] OR processing speed[tiab] OR verbal learning[tiab] OR working memory[tiab] OR reasoning[tiab] OR problem solving[tiab] OR social cognition[tiab] OR visuospatial[tiab]))`
3. `((schizophreni*[tiab] OR schizoaffective[tiab] OR psychotic disorder*[tiab] OR bipolar disorder*[tiab] OR major depressi*[tiab] OR mood disorder*[tiab]) AND (immune[tiab] OR inflamm*[tiab] OR cytokine*[tiab] OR kynurenine[tiab] OR microglia*[tiab] OR "C-reactive protein"[tiab] OR CRP[tiab]) AND (global cognition[tiab] OR cognitive performance[tiab] OR cognitive functioning[tiab] OR cognition[tiab] OR neurocognit*[tiab] OR cognitive domain*[tiab] OR attention[tiab] OR memory[tiab] OR executive function*[tiab] OR processing speed[tiab] OR working memory[tiab] OR verbal learning[tiab] OR social cognition[tiab])) AND (correlat*[tiab] OR associat*[tiab] OR relationship*[tiab] OR regression[tiab] OR predict*[tiab] OR "cross-sectional"[tiab] OR longitudinal[tiab] OR cohort[tiab]) NOT (animal[mh] NOT human[mh])`
4. `((("Schizophrenia"[Mesh] OR "Bipolar Disorder"[Mesh] OR "Depressive Disorder, Major"[Mesh]) OR (schizophreni*[tiab] OR bipolar[tiab] OR major depressi*[tiab])) AND (("Kynurenine"[Mesh] OR kynurenine[tiab] OR kynurenic acid[tiab] OR quinolinic acid[tiab] OR tryptophan[tiab] OR indoleamine 2,3-dioxygenase[tiab] OR IDO[tiab]) OR ("Cytokines"[Mesh] OR cytokine*[tiab] OR interleukin*[tiab] OR interferon-gamma[tiab] OR TNF-alpha[tiab]) OR (microglia*[tiab] OR microglial activation[tiab] OR sTREM2[tiab] OR YKL-40[tiab])) AND ("Cognition"[Mesh] OR "Neuropsychological Tests"[Mesh] OR cognit*[tiab] OR neuropsychological[tiab] OR MATRICS[tiab] OR MCCB[tiab]))`
5. `(("schizophrenia spectrum"[tiab] OR schizophreni*[tiab] OR schizoaffective[tiab] OR bipolar disorder*[tiab] OR major depressive disorder[tiab] OR MDD[tiab]) AND (serum[tiab] OR plasma[tiab] OR blood[tiab] OR peripheral blood[tiab]) AND (immune marker*[tiab] OR inflammatory biomarker*[tiab] OR cytokine*[tiab] OR chemokine*[tiab] OR pro-inflammatory[tiab] OR anti-inflammatory[tiab] OR kynurenine metabolite*[tiab] OR tryptophan catabolite*[tiab] OR microglial marker*[tiab]) AND (global cognition[tiab] OR composite cognition[tiab] OR domain-specific cognition[tiab] OR attention[tiab] OR vigilance[tiab] OR verbal memory[tiab] OR visual memory[tiab] OR processing speed[tiab] OR reasoning[tiab] OR executive function*[tiab] OR working memory[tiab] OR social cognition[tiab]) AND (correlat*[tiab] OR associat*[tiab] OR within-patient[tiab] OR patient sample*[tiab] OR longitudinal[tiab] OR cross-sectional[tiab] OR cohort[tiab] OR case-control[tiab]))`

The merged candidate pool contained 86 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational or interventional human studies (including cross-sectional, case-control, cohort, or clinical trials with relevant baseline or within-sample data) that report within-patient correlational analyses rather than requiring a separate healthy control group.
- Participants are patients with schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder, diagnosed using established clinical diagnostic criteria or clinician diagnosis.
- Studies measure blood-based immune markers, including pro-inflammatory or anti-inflammatory indices, inflammatory cytokines, kynurenine metabolites, or markers of microglial activation.
- Studies report associations between immune markers and cognitive outcomes, including global cognitive performance and/or domain-specific cognitive functioning across recognized cognitive domains.

Exclusion criteria:

- Studies that include non-psychiatric or other psychiatric populations only, or do not report data separately for schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder.
- Studies that do not examine within-patient associations between blood-based immune markers and cognition (for example, studies limited to between-group comparisons only).
- Studies that do not assess relevant cognitive outcomes or do not report global cognition or domain-specific cognitive performance data.
- Animal, preclinical, in vitro, case report, review, editorial, conference abstract-only, or other non-original research articles.

86 candidates were screened and 31 were retained.

### Statistical Analysis

### Statistical analysis
The primary quantitative synthesis was based on standardized mean differences (**SMDs**) extracted or derived from eligible studies contributing comparable data. Where study-specific estimates were available in a form suitable for meta-analysis, they were transformed to a common SMD metric to enable pooling across studies that may have used different cognitive scales or biomarker measurement approaches. Positive SMD values were oriented consistently to reflect the same direction of association across studies before synthesis.

Meta-analysis was performed using both **random-effects** and **fixed-effect** models. The random-effects model was prespecified as the principal model because methodological and clinical differences were expected across studies, including variation in psychiatric diagnosis, biomarker panels, assay platforms, and cognitive test batteries. The fixed-effect model was additionally calculated as a sensitivity comparison.

For the pooled analysis, **2 studies** contributed effect size data. The pooled random-effects estimate was **SMD = 0.196** with a **95% confidence interval (CI) of -0.116 to 0.509** and **p = 0.2185**. The fixed-effect model yielded the same pooled estimate: **SMD = 0.196** with **95% CI -0.116 to 0.509** and **p = 0.2185**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (tau²)**. Observed heterogeneity was negligible, with **I² = 0.0%**, **Q = 0.43 (p = 0.514)**, and **tau² = 0.0000**, indicating no detectable between-study variance in the pooled effect. Given the very small number of studies in the meta-analysis, heterogeneity estimates were interpreted cautiously, and the quantitative synthesis was complemented by structured narrative review of the remaining included studies.

## Results

### Study Selection

### Results of Search
The literature search identified **86 records** in total (**86** from local database searching and **0** from PubMed), with **86 records remaining after deduplication**. All **86 records** underwent title and abstract screening, of which **55** were excluded at stage 1. The remaining **31 full-text articles** were assessed for eligibility. No studies were excluded at the full-text stage (**n = 0**), resulting in **31 studies** being included in the systematic review. Thus, the final evidence base comprised **31 eligible studies** examining within-patient associations between blood-based immune markers and cognitive outcomes in individuals with schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder.

Most frequent recorded exclusion reasons:

- Systematic review/meta-analysis, not original human research.: 4
- Review article, not original human research.: 4
- Meta-analysis, not original human research with within-patient immune marker-cognition associations.: 2
- Meta-analysis/review article, not original human research with within-patient immune marker-cognition associations.: 1
- Does not assess cognitive outcomes; examines cytokine associations with stress, HPA axis activity, and disease severity only.: 1
- Does not report associations between immune markers and cognitive outcomes; focuses on inflammation, kynurenine metabolites, and mood state.: 1
- Abstract indicates immune marker levels by hospitalizations/diagnosis, with no cognitive outcomes or within-patient immune-cognition associations reported.: 1
- Does not assess cognitive outcomes; reports associations of cytokines with clinical symptoms only.: 1
- Abstract focuses on inflammatory markers in psychosis/schizophrenia groups and controls, without reporting cognitive outcomes or within-patient immune-cognition associations.: 1
- Measures CRP levels across diagnostic groups only; no cognitive outcomes or within-patient immune-cognition analyses.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7442 | 2018 | Predictors of cognitive performance in bipolar disorder: The role of educational degree and inflammatory markers. |
| 7448 | 2015 | Interleukin-6: the missing element of the neurocognitive deterioration in schizophrenia? The focus on genetic underpinnings, cognitive impairment and clinical manifestation. |
| 42403 | 2024 | Interaction between serum inflammatory cytokines and brain-derived neurotrophic factor in cognitive function among first-episode schizophrenia patients. |
| 42102 | 2021 | C-reactive protein is associated with cognitive performance in a large cohort of euthymic patients with bipolar disorder. |
| 7461 | 2018 | The Relationship between Cytokines and Verbal Memory in Individuals with Schizophrenia and Their Unaffected Siblings. |
| 7473 | 2018 | Interleukin-3, symptoms and cognitive deficits in first-episode drug-naïve and chronic medicated schizophrenia. |
| 7475 | 2013 | Interleukin 18 and cognitive impairment in first episode and drug naïve schizophrenia versus healthy controls. |
| 42186 | 2026 | Processing speed in bipolar disorder and relationship to peripheral inflammation: A 4-year longitudinal study. |
| 27865 | 2025 | White matter hyperintensities, inflammation and cognitive impairments in drug-naïve first episode schizophrenia patients: a cross-sectional study. |
| 7472 | 2018 | Relationship of Interferon-γ to Cognitive Function in Midlife Women with Schizophrenia. |
| 7477 | 2021 | Inflammation, hippocampal volume, and cognition in schizophrenia: results from the Northern Finland Birth Cohort 1966. |
| 7454 | 2021 | Chemokine MCP1 is associated with cognitive flexibility in schizophrenia: A preliminary analysis. |
| 7379 | 2017 | Infection and inflammation in schizophrenia and bipolar disorder. |
| 7458 | 2021 | Association of the kynurenine pathway metabolites with clinical, cognitive features and IL-1β levels in patients with schizophrenia spectrum disorder and their siblings. |
| 7467 | 2022 | Cognition-immune interactions between executive function and working memory, tumour necrosis factor-alpha (TNF-alpha) and soluble TNF receptors (sTNFR1 and sTNFR2) in bipolar disorder. |
| 7478 | 2018 | Cognitive deficit in patients with paranoid schizophrenia: Its clinical and laboratory correlates. |
| 42309 | 2025 | Transdiagnostic features of inflammatory markers and executive function across psychiatric disorders. |
| 42305 | 2025 | Association of Serum SOCS3 and Inflammatory Marker Levels With Cognitive Function in First-Episode Schizophrenia. |
| 42398 | 2012 | Executive dysfunction in euthymic bipolar disorder patients and its association with plasma biomarkers. |
| 7452 | 2020 | Dysregulation of kynurenine metabolism is related to proinflammatory cytokines, attention, and prefrontal cortex volume in schizophrenia. |
| 7445 | 2020 | Type 17 Immune Response Facilitates Progression of Inflammation and Correlates with Cognition in Stable Schizophrenia. |
| 7465 | 2021 | Inflammatory biomarkers and cognitive functioning in individuals with euthymic bipolar disorder: exploratory study. |
| 22431 | 2025 | Abnormal serum IL-10 and IL-19 levels in childhood- and adolescent-onset schizophrenia: associations with negative symptoms and language function. |
| 7446 | 2021 | Quinolinic acid is associated with cognitive deficits in schizophrenia but not major depressive disorder. |
| 7443 | 2013 | Impact of peripheral levels of chemokines, BDNF and oxidative markers on cognition in individuals with schizophrenia. |
| 42395 | 2018 | The relationship between neutrophil-lymphocyte, platelet-lymphocyte ratio and cognitive functions in bipolar disorder. |
| 42218 | 2025 | Association between metabolic syndrome, diabetes mellitus, inflammation and cognitive dysfunctions in schizophrenia: a cross-sectional analysis. |
| 42202 | 2024 | Association of cytokines levels, psychopathology and cognition among CR-TRS patients with metabolic syndrome. |
| 7469 | 2016 | Effect of recombinant erythropoietin on inflammatory markers in patients with affective disorders: A randomised controlled study. |
| 39770 | 2026 | Peripheral inflammation mediates cognitive deficits in drug-naive schizophrenia through hippocampal-thalamo-visual circuitry dysfunction. |
| 20455 | 2018 | Changes in Tryptophan Catabolite (TRYCAT) Pathway Patterning Are Associated with Mild Impairments in Declarative Memory in Schizophrenia and Deficits in Semantic and Episodic Memory Coupled with Increased False-Memory Creation in Deficit Schizophrenia. |

### Study Characteristics

Across the 31 included studies, publication years ranged from 2012 to 2026, although several records did not report a year and some appeared to reflect unpublished or in-press material. The total pooled sample comprised 11,013 participants, but study size varied markedly, from small case-control samples of fewer than 30 participants to a large population-based birth cohort of 5,455 participants. Geographic reporting was notably limited: only four studies explicitly reported location, spanning China, the United States, and Finland, while the large majority did not specify country. This weak reporting of setting limits assessment of contextual comparability and generalizability across populations.

Study design was heterogeneous, although the evidence base was dominated by observational approaches. Most studies were cross-sectional or case-control in design, including several mixed case-control/cross-sectional analyses, one observational comparative study, one burst longitudinal multi-cohort study, one population-based birth cohort, and one randomised controlled study. This distribution indicates that the literature is weighted toward associative rather than longitudinal or interventional evidence. Enhanced extraction suggested generally strong reporting capture, with 29 studies judged to have high data-quality confidence and 2 rated as medium confidence. However, this should be interpreted alongside the risk-of-bias profile, which was less favorable: most studies were judged at high risk of bias, with only a small number rated as unclear risk, and domains such as random sequence generation, allocation concealment, and blinding were typically reported as unclear.

There was also substantial heterogeneity in study features beyond design. Sample composition and participant characteristics were inconsistently reported across the extracted records, limiting clear synthesis of age, sex distribution, and condition severity across studies. Likewise, intervention-related characteristics such as dose, duration, and mode of delivery were not consistently available, suggesting either limited intervention-based evidence or incomplete reporting in the included dataset. Outcome measurement approaches also appeared variable, as reflected by the mix of correlational, comparative, postmortem, cohort, and clinical designs. Overall, the included literature was characterized by pronounced heterogeneity in scale, design, reporting completeness, and methodological rigor, which should be considered when interpreting pooled patterns of evidence.

### Main Findings

### Results

The pooled analysis demonstrated no statistically significant association between blood-based immune markers and cognitive performance across patient samples with schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder. Across the two included studies, the random-effects meta-analysis yielded a pooled standardized mean difference (SMD) of 0.196 (95% CI -0.116 to 0.509; p=0.2185). Because between-study heterogeneity was absent, the fixed-effect estimate was identical (SMD 0.196, 95% CI -0.116 to 0.509; p=0.2185).

In terms of direction and magnitude, the pooled effect was small and positive, suggesting at most a modest association between immune marker profiles and better cognitive performance; however, the confidence interval crossed the null and remained compatible with no meaningful association. As this effect measure is an SMD, it does not translate directly into a relative reduction or increase in risk. Clinically, the observed magnitude is small and should be interpreted cautiously, particularly given the limited number of studies.

Findings were highly consistent across studies. Statistical heterogeneity was nil (I²=0.0%; Q=0.43, p=0.514; τ²=0.0000), indicating that the available studies produced closely aligned effect estimates and that there was no evidence of important between-study variability beyond chance. This consistency strengthens the internal coherence of the pooled estimate, although it should be noted that heterogeneity statistics are imprecise when based on only two studies.

At the individual-study level, the included studies appeared to contribute broadly concordant findings, with no indication that one study reported an effect in the opposite direction sufficient to influence the overall estimate materially. Likewise, there was no evidence of outlier effects, which is consistent with the absence of observed heterogeneity. Any minor differences between studies are therefore more likely to reflect sampling variation than substantive clinical or methodological divergence.

Overall, the available evidence does not support a clear cross-diagnostic within-patient association between blood-based immune markers and global or domain-specific cognitive functioning, although the possibility of a small effect cannot be excluded. The precision of this conclusion is limited by the small evidence base.

### Risk of Bias

**Risk of bias.** Across the 31 included studies, the overall risk-of-bias profile was unfavorable: 28/31 studies (90.3%) were judged as **high risk** overall and the remaining 3/31 (9.7%) as **unclear risk**; **no study** was judged to be at low risk. At the domain level, concerns were universal and driven primarily by **poor reporting rather than clearly described methodological safeguards**. Specifically, all 31 studies (100%) were judged **unclear** for **random sequence generation**, **allocation concealment**, **blinding of participants/personnel**, **blinding of outcome assessment**, **incomplete outcome data**, and **selective reporting**. Thus, the most common bias domains with concerns were not isolated to one aspect of study conduct; instead, every standard domain lacked sufficient information for appraisal across the entire evidence base.

A consistent pattern across studies was the absence of reportable methodological detail, with study records repeatedly indicating “no information available” or that the domain was not reported. Because of this uniform lack of information, it was not possible to identify meaningful differences in risk-of-bias patterns across study designs (e.g., RCTs versus observational studies); if randomized studies were included, essential features such as sequence generation and allocation concealment were still not described in any case. Likewise, no study could be identified as being at particularly low risk in any domain. The three studies classified as overall unclear rather than high risk (one 2016 study and two 2026 studies) were not better reported at the domain level; rather, they remained indeterminate because there was insufficient information to justify either a clearly low-risk or clearly high-risk judgment. Conversely, the 28 studies rated high risk were chiefly limited by pervasive non-reporting across all six domains, which prevents verification of internal validity.

These risk-of-bias findings reduce confidence in the pooled estimate. When all studies have unclear judgments for core domains—especially sequence generation, allocation concealment, blinding, attrition handling, and selective reporting—the summary effect may be vulnerable to both **systematic overestimation or underestimation** of the true effect, and the direction of bias cannot be predicted with confidence. The enhanced extraction process showed **high data-quality confidence for 29/31 studies (93.5%)** and **medium confidence for 2/31 (6.5%)**, with none rated low confidence; importantly, this supports the reliability of the **extracted bias judgments**, not the methodological quality of the underlying studies themselves. Overall, the body of evidence should therefore be interpreted cautiously, and the certainty of conclusions drawn from the pooled results is likely limited by widespread methodological under-reporting and probable risk of bias.

## Discussion

**Discussion**

This systematic review examined within-patient associations between blood-based immune markers and cognitive performance in schizophrenia spectrum disorder, bipolar disorder, and major depressive disorder. Across 31 included studies, the overall literature suggested substantial interest in whether peripheral immune dysregulation relates to global and domain-specific cognition, but the quantitatively synthesizable evidence was very limited. In the meta-analysis, based on only 2 studies, the pooled standardized mean difference was small and not statistically significant (random-effects SMD 0.196, 95% CI -0.116 to 0.509, p=0.2185), with no observed heterogeneity (I²=0.0%, Q=0.43, p=0.514; tau²=0.0000). Fixed- and random-effects estimates were identical, reflecting the small number of studies and absence of measurable between-study variance. Taken together, these findings do not provide convincing evidence for a robust cross-diagnostic association between peripheral immune markers and cognition, but they also do not exclude a modest relationship. The confidence interval remains compatible with both a small adverse association and a small positive association, limiting firm clinical interpretation.

These findings should be interpreted in the context of prior reviews, although direct comparators are limited because most existing syntheses in psychiatry have focused on case-control differences rather than within-patient biomarker-cognition associations. For example, a recent review of gut microbiota in major depressive disorder, bipolar disorder, and schizophrenia found relatively consistent differences in community composition versus healthy controls, despite weak evidence for alpha-diversity differences. That pattern is informative: biological alterations may be detectable at the group level without translating into a clear linear association with cognitive variation within patient samples. Similarly, reviews in adjacent fields, such as immune-mediated inflammatory diseases, have reported significant associations between symptom burden and objective digital or imaging endpoints, suggesting that immune-related pathophysiology can map onto clinically relevant functional outcomes under some conditions. Our more equivocal results may therefore reflect a true difference in the immune-cognition relationship in severe mental illness, but they may also arise from greater phenotypic heterogeneity, less precise biomarker measurement, or weaker alignment between blood-based indices and central nervous system processes than is seen in other conditions.

Biologically, an association between immune dysregulation and cognitive impairment in these disorders remains plausible. Pro-inflammatory cytokines, altered kynurenine pathway metabolites, and microglial activation have each been implicated in mechanisms relevant to cognition, including reduced synaptic plasticity, altered glutamatergic neurotransmission, oxidative stress, endothelial dysfunction, and disruption of fronto-limbic and hippocampal circuits. Anti-inflammatory pathways may also matter, either through insufficient counter-regulation of chronic low-grade inflammation or through more complex nonlinear immune signaling. At the same time, the absence of a clear pooled effect is not surprising. Peripheral blood markers are imperfect proxies for neuroinflammation, immune signaling is dynamic rather than static, and cognitive impairment in schizophrenia, bipolar disorder, and major depressive disorder is itself multifactorial, with contributions from illness chronicity, psychotropic medication exposure, metabolic burden, sleep disturbance, and symptom state. Any true association may therefore be modest, domain-specific, or detectable only in biologically defined subgroups rather than across mixed patient samples.

Several factors likely contributed to inconsistency across the included studies and to the very small meta-analytic evidence base. First, the review covered three diagnostic groupings with partially overlapping but nonidentical cognitive and inflammatory profiles. Second, the exposure definition was broad by necessity, spanning pro-inflammatory and anti-inflammatory cytokines, composite inflammatory indices, kynurenine metabolites, and candidate markers of microglial activation; these markers are unlikely to have equivalent biological meaning. Third, cognitive outcomes varied across global cognition and eight domains, with studies using different neuropsychological batteries and analytic approaches. Fourth, many studies were cross-sectional, limiting inference about temporality and making results vulnerable to confounding by acute symptoms, medication use, body mass index, smoking, cardiometabolic illness, and other lifestyle or treatment-related factors. Finally, although formal heterogeneity in the meta-analysis was zero, that statistic is not very informative here because only two studies could be pooled; the broader qualitative evidence indicates substantial clinical and methodological diversity that is not captured by I² alone.

This review has several strengths. It addresses a clinically relevant question that is narrower and more mechanistic than standard case-control comparisons, focusing specifically on within-patient associations between peripheral immune biology and cognition. It also spans major diagnostic categories, which is useful given increasing interest in transdiagnostic mechanisms of cognitive dysfunction. A further strength is the overall quality of the extracted study data: 29 of 31 studies were rated high quality and 2 medium quality within the extraction workflow. The enhanced extraction approach also allowed us to recover and structure evidence from a literature in which reporting was often incomplete, preserving qualitative findings even when meta-analysis was not possible. That said, the limitations are substantial. Most importantly, only 2 studies contributed to the pooled estimate, and many included reports lacked extractable means, standard deviations, exact effect sizes, or sufficient subgroup data. Metadata were also incompletely reported in several extractions, and selective or qualitative reporting reduced analytic precision. More broadly, the included studies were heterogeneous in diagnosis, biomarker selection, cognitive assessment, and adjustment for confounders, and the reliance on peripheral blood measures constrains inferences about central immune activity. Generalizability may also be limited by small samples, single-center designs, and likely underrepresentation of early illness stages and diverse populations.

The clinical implications are therefore cautious. Current evidence does not support using blood-based immune markers as standalone indicators of cognitive impairment across schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder. At present, clinical assessment of cognition should continue to rely on direct neuropsychological or validated cognitive screening methods rather than peripheral inflammatory profiling. The research implications are clearer. Future studies should use adequately powered, longitudinal designs; prespecify primary biomarkers and cognitive domains; harmonize laboratory and neuropsychological methods; and adjust consistently for key confounders such as age, sex, BMI, smoking, metabolic status, medication exposure, and symptom severity. Greater use of repeated-measures designs, individual participant data meta-analysis, and stratification by diagnosis, illness stage, and inflammatory subtype may help determine whether a meaningful immune-cognition signal exists in specific subgroups. Integrating peripheral biomarkers with neuroimaging, cerebrospinal fluid markers, or multimodal digital phenotyping may also provide a more biologically faithful account of the pathways linking inflammation and cognition in severe mental illness.

## Conclusion

In this meta-analysis of 31 studies, blood-based immune markers were not meaningfully associated with cognitive performance within patients with schizophrenia spectrum disorder, bipolar disorder, or major depressive disorder; the pooled standardized mean difference from the 2 studies contributing to the quantitative synthesis was 0.196 (95% CI, -0.116 to 0.509; p=0.22). Although the point estimate trends toward a small positive association, the confidence interval spans no effect and does not support a clinically important relationship between peripheral immune activity and either global or domain-specific cognition at a level that would justify using these markers alone to guide cognitive assessment or treatment decisions. Clinically, immune biomarkers may still have value as part of broader multimodal profiling, but they should be interpreted cautiously and not as reliable standalone indicators of cognitive dysfunction. The main caveat is that only two studies were meta-analyzed despite 31 eligible studies overall, limiting precision and the strength of any practical inference.

## Final Included Studies

- Corpus ID: 7442 | Predictors of cognitive performance in bipolar disorder: The role of educational degree and inflammatory markers.
- Corpus ID: 7448 | Interleukin-6: the missing element of the neurocognitive deterioration in schizophrenia? The focus on genetic underpinnings, cognitive impairment and clinical manifestation.
- Corpus ID: 42403 | Interaction between serum inflammatory cytokines and brain-derived neurotrophic factor in cognitive function among first-episode schizophrenia patients.
- Corpus ID: 42102 | C-reactive protein is associated with cognitive performance in a large cohort of euthymic patients with bipolar disorder.
- Corpus ID: 7461 | The Relationship between Cytokines and Verbal Memory in Individuals with Schizophrenia and Their Unaffected Siblings.
- Corpus ID: 7473 | Interleukin-3, symptoms and cognitive deficits in first-episode drug-naïve and chronic medicated schizophrenia.
- Corpus ID: 7475 | Interleukin 18 and cognitive impairment in first episode and drug naïve schizophrenia versus healthy controls.
- Corpus ID: 42186 | Processing speed in bipolar disorder and relationship to peripheral inflammation: A 4-year longitudinal study.
- Corpus ID: 27865 | White matter hyperintensities, inflammation and cognitive impairments in drug-naïve first episode schizophrenia patients: a cross-sectional study.
- Corpus ID: 7472 | Relationship of Interferon-γ to Cognitive Function in Midlife Women with Schizophrenia.
- Corpus ID: 7477 | Inflammation, hippocampal volume, and cognition in schizophrenia: results from the Northern Finland Birth Cohort 1966.
- Corpus ID: 7454 | Chemokine MCP1 is associated with cognitive flexibility in schizophrenia: A preliminary analysis.
- Corpus ID: 7379 | Infection and inflammation in schizophrenia and bipolar disorder.
- Corpus ID: 7458 | Association of the kynurenine pathway metabolites with clinical, cognitive features and IL-1β levels in patients with schizophrenia spectrum disorder and their siblings.
- Corpus ID: 7467 | Cognition-immune interactions between executive function and working memory, tumour necrosis factor-alpha (TNF-alpha) and soluble TNF receptors (sTNFR1 and sTNFR2) in bipolar disorder.
- Corpus ID: 7478 | Cognitive deficit in patients with paranoid schizophrenia: Its clinical and laboratory correlates.
- Corpus ID: 42309 | Transdiagnostic features of inflammatory markers and executive function across psychiatric disorders.
- Corpus ID: 42305 | Association of Serum SOCS3 and Inflammatory Marker Levels With Cognitive Function in First-Episode Schizophrenia.
- Corpus ID: 42398 | Executive dysfunction in euthymic bipolar disorder patients and its association with plasma biomarkers.
- Corpus ID: 7452 | Dysregulation of kynurenine metabolism is related to proinflammatory cytokines, attention, and prefrontal cortex volume in schizophrenia.
- Corpus ID: 7445 | Type 17 Immune Response Facilitates Progression of Inflammation and Correlates with Cognition in Stable Schizophrenia.
- Corpus ID: 7465 | Inflammatory biomarkers and cognitive functioning in individuals with euthymic bipolar disorder: exploratory study.
- Corpus ID: 22431 | Abnormal serum IL-10 and IL-19 levels in childhood- and adolescent-onset schizophrenia: associations with negative symptoms and language function.
- Corpus ID: 7446 | Quinolinic acid is associated with cognitive deficits in schizophrenia but not major depressive disorder.
- Corpus ID: 7443 | Impact of peripheral levels of chemokines, BDNF and oxidative markers on cognition in individuals with schizophrenia.
- Corpus ID: 42395 | The relationship between neutrophil-lymphocyte, platelet-lymphocyte ratio and cognitive functions in bipolar disorder.
- Corpus ID: 42218 | Association between metabolic syndrome, diabetes mellitus, inflammation and cognitive dysfunctions in schizophrenia: a cross-sectional analysis.
- Corpus ID: 42202 | Association of cytokines levels, psychopathology and cognition among CR-TRS patients with metabolic syndrome.
- Corpus ID: 7469 | Effect of recombinant erythropoietin on inflammatory markers in patients with affective disorders: A randomised controlled study.
- Corpus ID: 39770 | Peripheral inflammation mediates cognitive deficits in drug-naive schizophrenia through hippocampal-thalamo-visual circuitry dysfunction.
- Corpus ID: 20455 | Changes in Tryptophan Catabolite (TRYCAT) Pathway Patterning Are Associated with Mild Impairments in Declarative Memory in Schizophrenia and Deficits in Semantic and Episodic Memory Coupled with Increased False-Memory Creation in Deficit Schizophrenia.
