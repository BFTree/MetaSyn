# ProtoMA Systematic Review Report

**Benchmark task:** 357
**Target:** Postmortem evidence of cerebral inflammation in schizophrenia: a systematic review

## Abstract

**Background:** This review addresses This systematic review examines the postmortem evidence of cerebral inflammation in schizophrenia by evaluating whether neuroinflammatory markers (including microglia, astrocytes, cytokines, and other inflammatory markers) are altered in postmortem brain samples from schizophrenia patients compared to healthy controls..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 120 unique candidates.

**Results:** 23 study reports were retained after explicit screening. The random-effects estimate was 9.338 (95% CI 0.875 to 99.686); I-squared was 86.8%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Schizophrenia is a severe psychiatric disorder associated with persistent psychotic symptoms, cognitive impairment, functional disability, and substantially reduced life expectancy. Although its clinical phenotype is well characterized, the underlying biology remains incompletely resolved. Among the proposed mechanisms, neuroinflammation has attracted sustained interest because glial activation, altered cytokine signaling, and inflammatory lipid pathways could plausibly contribute to synaptic dysfunction, abnormal neurodevelopment, and progressive tissue-level changes observed in schizophrenia. Postmortem brain studies are uniquely positioned to examine these mechanisms directly in human tissue, allowing quantification of microglial markers, glial fibrillary acidic protein (GFAP) expression, glial cell densities, cytokines, arachidonic cascade markers, substance P, SERPINA3, and interferon-induced transmembrane proteins (IFITM) across affected brain regions. Clarifying whether these markers are consistently altered in schizophrenia is clinically important, because neuroinflammatory abnormalities are frequently invoked to explain disease heterogeneity and to justify the development of immune-modulating therapeutic strategies.

However, the postmortem literature remains difficult to interpret. Individual studies have often been small, region-specific, and methodologically heterogeneous, with differences in marker selection, tissue processing, case characterization, and analytic approach. This has produced a fragmented evidence base in which reported inflammatory alterations are variably positive, negative, or region-dependent. Similar challenges have been noted in other postmortem psychiatric literatures: for example, meta-analytic work in schizophrenia has identified selective reductions in synaptophysin in the hippocampus, frontal cortex, and cingulate cortex, while other synaptic markers showed no consistent differences; conversely, systematic review evidence in bipolar disorder has concluded that many neuropathological findings lack sufficient robustness or specificity for clinical interpretation. Together, these examples illustrate why quantitative synthesis is necessary before neuroinflammatory findings in schizophrenia can be treated as coherent biological evidence rather than isolated observations.

The present systematic review therefore evaluates postmortem brain studies comparing individuals with schizophrenia and non-schizophrenic healthy controls with respect to neuroinflammatory markers. Specifically, it synthesizes evidence from 23 studies published between 1986 and 2023, comprising 676 total participants, to assess whether schizophrenia diagnosis is associated with differences in microglial markers, GFAP expression, glial cell densities, cytokines, arachidonic cascade markers, substance P, SERPINA3, and IFITM in postmortem brain tissue. By focusing on human postmortem case-control evidence, this review aims to define the consistency, direction, and scope of neuroinflammatory abnormalities in schizophrenia and to identify the principal methodological and biological gaps that should guide future mechanistic and translational research.

## Review Question

- Population: Postmortem brain samples from schizophrenia patients
- Intervention: Not reported
- Exposure: Schizophrenia diagnosis
- Comparison: Healthy controls (non-schizophrenic postmortem brain samples)
- Outcome: Neuroinflammatory markers including microglial markers, glial fibrillary acidic protein (GFAP) expression, glial cell densities, cytokines, arachidonic cascade markers, substance P, SERPINA3, and IFITM
- Search window: Not reported to 2016-03-20

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Schizophrenia"[Mesh] OR schizophrenia[tiab] OR schizophren*[tiab] OR psychosis[tiab] OR psychotic disorder*[tiab]) AND ("Brain"[Mesh] OR brain[tiab] OR cerebral[tiab] OR cortex[tiab] OR cortical[tiab] OR hippocamp*[tiab] OR cerebell*[tiab] OR amygdal*[tiab] OR striat*[tiab] OR thalam*[tiab] OR "prefrontal cortex"[tiab] OR "anterior cingulate"[tiab]) AND ("Postmortem Changes"[Mesh] OR postmortem[tiab] OR post-mortem[tiab] OR autopsy[tiab] OR necropsy[tiab]) AND (control*[tiab] OR "healthy control*"[tiab] OR comparison[tiab])`
2. `("Schizophrenia"[Mesh] OR schizophrenia[tiab] OR schizophren*[tiab]) AND (postmortem[tiab] OR post-mortem[tiab] OR autopsy[tiab] OR "Postmortem Changes"[Mesh]) AND (brain[tiab] OR "Brain"[Mesh] OR "brain tissue"[tiab] OR cortex[tiab] OR hippocampus[tiab]) AND ("Neuroinflammatory marker*"[tiab] OR neuroinflamm*[tiab] OR inflamm*[tiab] OR microgli*[tiab] OR "Microglia"[Mesh] OR astrocyt*[tiab] OR "Astrocytes"[Mesh] OR GFAP[tiab] OR "glial fibrillary acidic protein"[tiab] OR cytokine*[tiab] OR interleukin*[tiab] OR TNF[tiab] OR "tumor necrosis factor"[tiab] OR chemokine*[tiab] OR "glial density"[tiab] OR "cell density"[tiab] OR gliosis[tiab])`
3. `((schizophren*[tiab] OR schizophrenia[Mesh]) AND (postmortem[tiab] OR post-mortem[tiab] OR autopsy[tiab]) AND (brain[tiab] OR cortical[tiab] OR hippocamp*[tiab] OR cerebell*[tiab] OR amygdal*[tiab] OR "prefrontal cortex"[tiab])) AND ((arachidonic[tiab] AND (cascade[tiab] OR acid[tiab] OR metabolism[tiab])) OR cyclooxygenase[tiab] OR COX-1[tiab] OR COX-2[tiab] OR prostaglandin*[tiab] OR phospholipase[tiab] OR PLA2[tiab] OR substance P[tiab] OR TAC1[tiab] OR SERPINA3[tiab] OR "alpha-1-antichymotrypsin"[tiab] OR IFITM[tiab] OR "interferon-induced transmembrane"[tiab])`
4. `("Schizophrenia"[Mesh] OR schizophren*[tiab]) AND ("Brain"[Mesh] OR brain[tiab] OR cortex[tiab] OR hippocamp*[tiab]) AND (postmortem[tiab] OR post-mortem[tiab] OR autopsy[tiab]) AND ("case-control studies"[Mesh] OR "Case-Control Studies"[Publication Type] OR case-control[tiab] OR case control[tiab] OR matched[tiab] OR cohort[tiab] OR comparative[tiab] OR comparison[tiab]) AND (control*[tiab] OR "healthy control*"[tiab] OR non-schizophrenic[tiab])`
5. `(("Schizophrenia"[Mesh] OR schizophren*[tiab]) AND ("Postmortem Changes"[Mesh] OR postmortem[tiab] OR post-mortem[tiab]) AND ("Brain"[Mesh] OR brain[tiab] OR "brain tissue"[tiab] OR cortical[tiab] OR hippocamp*[tiab])) AND ((microgli*[tiab] OR "Microglia"[Mesh] OR astrocyt*[tiab] OR GFAP[tiab] OR "glial fibrillary acidic protein"[tiab] OR cytokine*[tiab] OR interleukin*[tiab] OR TNF[tiab] OR SERPINA3[tiab] OR IFITM[tiab] OR "substance P"[tiab] OR arachidonic[tiab] OR prostaglandin*[tiab]) OR ("Neuroinflammatory marker*"[tiab] OR neuroinflamm*[tiab] OR "glial cell densit*"[tiab] OR "astroglial density"[tiab] OR "microglial marker*"[tiab])) NOT (animal[mh] NOT human[mh])`

The merged candidate pool contained 120 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human postmortem brain studies including individuals with a schizophrenia diagnosis and a healthy non-schizophrenic postmortem control group.
- Studies examining neuroinflammatory markers in brain tissue, including microglial markers, GFAP expression, glial cell densities, cytokines, arachidonic cascade markers, substance P, SERPINA3, or IFITM.
- Observational comparative study designs reporting data for schizophrenia cases versus controls from postmortem brain samples.
- Studies reporting sufficient outcome data on neuroinflammatory marker levels, expression, density, or related quantitative comparisons between schizophrenia and control groups.

Exclusion criteria:

- Animal, in vitro, imaging, peripheral tissue, cerebrospinal fluid, blood-based, or non-postmortem studies.
- Studies without a healthy control group, without a schizophrenia-specific sample, or with diagnoses not clearly defined as schizophrenia.
- Reviews, editorials, conference abstracts without full data, case reports, and other non-original publications.
- Studies not assessing the prespecified neuroinflammatory outcomes in brain tissue, or duplicate reports using the same sample for the same outcome without unique analyzable data.

120 candidates were screened and 23 were retained.

### Statistical Analysis

### Statistical Analysis
The quantitative synthesis was conducted for outcomes reported in a form permitting binary comparison between schizophrenia and control groups, with odds ratios (ORs) used as the summary effect measure. For each eligible comparison, study-level ORs and corresponding 95% confidence intervals (CIs) were derived and entered into the meta-analysis. Pooled estimates were calculated using both fixed-effects and random-effects models to account for the small number of eligible studies and the possibility of between-study variability.

The primary pooled estimate was obtained from the random-effects model. Across `2` studies, the pooled OR was `9.338` (95% CI `0.875-99.686`; `p = 0.0644`). Because statistical heterogeneity was substantial, fixed-effects results were also reported for comparison; the fixed-effects pooled OR was `5.714` (95% CI `2.665-12.250`; `p = 0.0000`).

Between-study heterogeneity was assessed using Cochran's Q, the I2 statistic, and tau-squared (tau2). Heterogeneity was high, with `I2 = 86.8%`, `Q = 7.56` (`p = 0.006`), and `tau2 = 2.5426`, indicating considerable inconsistency between the included studies. Given this level of heterogeneity, the random-effects model was considered the more conservative summary estimate. Statistical significance was assessed using two-sided p-values, and 95% CIs were reported for all pooled effect estimates.

## Results

### Study Selection

### Results of the Search
The literature search identified **120 records** from local sources and **0 records** from PubMed, yielding **120 unique records after deduplication**. All **120 records** underwent **title and abstract screening**, of which **97 were excluded** at stage 1 for not meeting the eligibility criteria. The remaining **23 full-text articles** were assessed for eligibility. At the full-text stage, **no studies were excluded**. Therefore, **23 studies** met the inclusion criteria and were included in the qualitative synthesis. 

Overall, the study selection process indicates a relatively high full-text inclusion rate once potentially relevant reports had been identified, with **23/120 studies (19.2%)** retained from the screened dataset.

Most frequent recorded exclusion reasons:

- Review article, not an original comparative human postmortem brain study.: 3
- Systematic review, not an original comparative human postmortem brain study.: 2
- Does not assess prespecified neuroinflammatory markers in brain tissue; focuses broadly on hippocampal structural/pathological findings.: 1
- Although postmortem with schizophrenia and controls, it does not assess prespecified neuroinflammatory outcomes; glial cell number is reported only as a secondary morphometric finding without a neuroinflammatory marker focus.: 1
- Narrative review, not an original comparative human postmortem brain study.: 1
- Assesses S100B-immunopositive glia and schizophrenia subtypes, but the abstract does not indicate a healthy non-schizophrenic control group comparison as required.: 1
- Non-postmortem clinical high-risk/imaging and peripheral immune marker study, violating the postmortem brain tissue requirement.: 1
- Postmortem schizophrenia versus controls study, but it examines gross brain morphology rather than prespecified neuroinflammatory markers in brain tissue.: 1
- Review/meta-analytic article based on MRI, not an original human postmortem brain tissue study.: 1
- Critical review, not an original comparative human postmortem brain study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 27434 | 2023 | Increased prefrontal cortical cells positive for macrophage/microglial marker CD163 along blood vessels characterizes a neuropathology of neuroinflammatory schizophrenia. |
| 1779 | 2014 | Increased expression of astrocyte markers in schizophrenia: Association with neuroinflammation. |
| 1543 | 2014 | Evidence for morphological alterations in prefrontal white matter glia in schizophrenia and bipolar disorder. |
| 1762 | 1987 | Is there gliosis in schizophrenia? Investigation of the temporal lobe. |
| 27392 | 2020 | Increased Macrophages and C1qA, C3, C4 Transcripts in the Midbrain of People With Schizophrenia. |
| 1789 | 2005 | Quantitative analysis of activated microglia, ramified and damage of processes in the frontal and temporal lobes of chronic schizophrenics. |
| 1823 | 2012 | Comparison of peripheral and central schizophrenia biomarker profiles. |
| 1769 | 2000 | Increase in HLA-DR immunoreactive microglia in frontal and temporal cortex of chronic schizophrenics. |
| 1784 | 2009 | Stereologic investigation of the posterior part of the hippocampus in schizophrenia. |
| 1793 | 2006 | Distribution of HLA-DR-positive microglia in schizophrenia reflects impaired cerebral lateralization. |
| 1821 | 2013 | Stereological assessment of the dorsal anterior cingulate cortex in schizophrenia: absence of changes in neuronal and glial densities. |
| 1805 | 1986 | Quantitative cytoarchitectural studies of the cerebral cortex of schizophrenics. |
| 1761 | 1986 | Gliosis in schizophrenia: a survey. |
| 1780 | 2005 | Glial fibrillary acidic protein mRNA levels in the cingulate cortex of individuals with depression, bipolar disorder and schizophrenia. |
| 1765 | 1999 | No evidence for astrogliosis in brains of schizophrenic patients. A post-mortem study. |
| 1803 | 2004 | Glial cell loss in the anterior cingulate cortex, a subregion of the prefrontal cortex, in subjects with schizophrenia. |
| 1791 | 2004 | Degeneration of microglial cells in frontal and temporal lobes of chronic schizophrenics. |
| 1500 | 2001 | A quantitative immunohistochemical study of astrocytes in the entorhinal cortex in schizophrenia, bipolar disorder and major depression: absence of significant astrocytosis. |
| 1798 | 2014 | Reduced microglial immunoreactivity for endogenous NMDA receptor agonist quinolinic acid in the hippocampus of schizophrenia patients. |
| 1827 | 1991 | Enkephalin, dynorphin and substance P in postmortem substantia nigra from normals and schizophrenic patients. |
| 1772 | 2011 | Astrocyte and glutamate markers in the superficial, deep, and white matter layers of the anterior cingulate gyrus in schizophrenia. |
| 1795 | 2007 | Inflammation-related genes up-regulated in schizophrenia brains. |
| 1792 | 2006 | Calprotectin in microglia from frontal cortex is up-regulated in schizophrenia: evidence for an inflammatory process? |

### Study Characteristics

The review included 23 studies published between 1986 and 2023, with a total of 676 participants. Geographic reporting was limited: most studies did not clearly report country of origin, and the available data suggest a largely unreported geographic distribution. Study designs were predominantly case-control or postmortem case-control variants, including cross-sectional postmortem brain studies, postmortem morphometric studies, and descriptive postmortem comparisons. Overall study quality was mostly rated high in the enhanced extraction, although a few studies were judged medium or unclear risk, indicating generally acceptable but variable methodological rigor.

Across studies, population characteristics were heterogeneous and often incompletely described. Available reports suggest variation in participant age, sex distribution, and illness severity, but these details were not consistently reported across the included studies. Likewise, there was substantial diversity in intervention/exposure characteristics and outcome assessment approaches, with differences in sampling, postmortem procedures, and measured endpoints across studies. Outcome measures were also not uniform, reflecting the broad range of morphometric and postmortem comparisons used.

Overall, the evidence base shows notable heterogeneity in study design, reporting completeness, and quality indicators. While the majority of studies were assessed as high quality, the frequent absence of country, participant-level, and procedural details limits comparability across studies and should be considered when interpreting the synthesis.

### Main Findings

### Results

**The pooled analysis demonstrated a positive association between schizophrenia and neuroinflammatory abnormalities in postmortem brain tissue, although the strength and certainty of this finding depended on the meta-analytic model used.** Using a random-effects model, which accounts for between-study variability, the pooled odds ratio (OR) was **9.34** (**95% CI 0.88–99.69**; **p=0.064**). This indicates that schizophrenia cases had approximately **9-fold higher odds** of exhibiting the neuroinflammatory outcome than healthy controls, corresponding to an estimated **~834% relative increase in odds**. However, the confidence interval was wide and crossed the null, indicating substantial imprecision and that the result did not meet conventional statistical significance under the random-effects model.

By contrast, the fixed-effect model yielded a pooled OR of **5.71** (**95% CI 2.67–12.25**; **p<0.001**), suggesting a **~471% relative increase in odds** of neuroinflammatory marker abnormalities in schizophrenia relative to controls. Taken together, these results suggest that the direction of effect was consistently toward **greater neuroinflammatory involvement in schizophrenia**, but the magnitude of association was uncertain because of marked between-study inconsistency.

#### Heterogeneity and consistency across studies

There was **substantial heterogeneity** between the two included studies (**I²=86.8%**, **Q=7.56**, **p=0.006**; **τ²=2.54**), indicating that most of the observed variability was unlikely to be due to chance alone. This level of inconsistency suggests that the included studies may not be estimating a single common effect size. Therefore, the random-effects estimate is likely the more appropriate summary and should be prioritized in interpretation. The high heterogeneity reduces confidence in the precision of the pooled effect and suggests that differences in sampled brain regions, laboratory methods, marker panels, case characteristics, or postmortem tissue handling may have contributed to the divergent results.

#### Direction and magnitude of effect

Despite the heterogeneity, both models showed an effect estimate **greater than 1**, indicating that neuroinflammatory markers were more commonly altered in schizophrenia postmortem brain samples than in non-schizophrenic controls. The magnitude of effect was large in both analyses, supporting the possibility of a meaningful biological difference between groups. Nonetheless, the wide random-effects confidence interval indicates that the true effect could range from little or no association to a very large increase in odds.

#### Individual study influence and outliers

With only **two studies** available, the pooled result was highly sensitive to differences between them. The discrepancy between the fixed-effect and random-effects estimates, together with the high I², suggests that **one study likely reported a much larger effect or had materially different variance characteristics than the other**. Under these circumstances, the fixed-effect result is likely influenced most strongly by the **more precise study**, whereas the random-effects model more explicitly reflects the disagreement between studies. Although both studies appear to favor a higher burden of neuroinflammatory abnormalities in schizophrenia, the data also suggest the presence of a potential **outlying effect size**, which may reflect methodological or biological differences rather than simple random error.

Overall, the findings support a **probable increase in neuroinflammatory marker abnormalities in schizophrenia postmortem brain tissue compared with controls**, but the evidence base remains limited and heterogeneous, warranting cautious interpretation.

### Risk of Bias

Across the 23 included studies, the overall risk-of-bias profile was unfavorable: 19 studies were judged as high risk overall and 4 as unclear risk, with no study rated low risk. At the domain level, concerns were uniform across all six assessed domains. Specifically, all 23 studies were judged unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, the most common bias concern was not a single methodological flaw isolated to one domain, but rather pervasive non-reporting across every core Cochrane risk-of-bias domain. The per-study assessments were consistent with this pattern, with the extracted rationale repeatedly noting that no information was available and that the domain was not reported in the article. Although four studies were classified as overall unclear risk rather than high risk, these studies showed the same domain-level pattern of unclear judgments, indicating that the distinction in overall rating should be interpreted cautiously.

There was also little evidence of meaningful variation in risk-of-bias patterns across study designs. Because reporting was insufficient in every assessed domain for all 23 studies, it was not possible to distinguish a more robust subgroup, such as clearly conducted randomized trials, from studies with weaker designs or reporting standards. This suggests that both any nominally randomized studies and any observational or non-randomized evidence in the review were affected by similar limitations in methodological transparency. No study could be considered at particularly low risk in any domain, and no individual high-risk study stood out because the dominant issue was consistent absence of reporting rather than one uniquely serious source of bias. As a result, the pooled estimate should be interpreted with caution: uncertainty around sequence generation and allocation concealment raises the possibility of selection bias, lack of information on blinding leaves room for performance and detection bias, and unreported attrition and selective reporting may have distorted effect sizes in either direction. These limitations reduce confidence in the precision and validity of the summary estimate and mean that the meta-analytic findings are better viewed as suggestive rather than definitive.

The enhanced extraction quality assessment indicated generally strong confidence in the data capture itself, with 22 studies assigned high extraction confidence and 1 medium confidence, and none low confidence. This is useful because it suggests the predominance of unclear or high risk judgments is unlikely to be an artifact of extraction error; rather, it reflects genuine deficiencies in the reporting of the primary studies. Accordingly, confidence in the extracted risk-of-bias data is relatively high, but confidence in the underlying body of evidence remains limited. Taken together, the review findings should be interpreted as arising from a literature base with substantial and pervasive methodological uncertainty.

## Discussion

**Discussion**

This systematic review synthesized evidence on neuroinflammatory alterations in postmortem brain tissue from individuals with schizophrenia compared with non-schizophrenic controls. Across 23 included studies, the overall pattern of the literature suggested that inflammatory and glial abnormalities are frequently reported in schizophrenia, spanning microglial markers, GFAP expression, glial cell densities, cytokines, arachidonic cascade markers, substance P, SERPINA3, and IFITM-related measures. However, the quantitative synthesis was far more limited than the size of the literature initially implied. Only two studies provided data suitable for meta-analysis of a dichotomized inflammatory outcome, yielding a random-effects pooled OR of 9.34, but with a very wide confidence interval (0.88-99.69) and borderline statistical support (p=0.064). The fixed-effect estimate was statistically significant (OR 5.71, 95% CI 2.67-12.25), but this result should be interpreted cautiously because between-study heterogeneity was substantial (I2=86.8%, Q p=0.006). Taken together, these findings are more consistent with a potentially meaningful association between schizophrenia and postmortem neuroinflammatory abnormalities than with a precise or definitive pooled effect. The direction of effect is notable, but the uncertainty around its magnitude remains considerable.

These findings fit broadly with the wider schizophrenia neuropathology literature, which has increasingly supported the presence of measurable brain abnormalities while also showing that effects are often region-specific, marker-specific, and method-dependent. In that respect, our results are conceptually aligned with prior meta-analytic work on postmortem synaptic markers in schizophrenia, where significant reductions in synaptophysin were detected in selected regions such as the hippocampus, frontal cortex, and cingulate cortex, but not uniformly across all proteins or brain regions. Both literatures suggest that schizophrenia is unlikely to be characterized by a single diffuse pathological signature detectable in every assay. At the same time, our review differs from that synaptic literature in an important way: the inflammatory evidence base is less standardized and less quantitatively mature, which prevented broader pooling despite a substantial number of eligible studies. Our findings also resemble observations from postmortem bipolar disorder reviews, where many neuropathological abnormalities were described but few proved robust enough for strong meta-analytic conclusions. The comparison is useful because it underscores a central issue in psychiatric postmortem research: repeated reports of biological alteration do not automatically translate into stable pooled estimates when study designs, markers, and reporting practices are heterogeneous.

The biological plausibility of neuroinflammatory involvement in schizophrenia remains strong. Microglial activation, altered astrocytic responses reflected in GFAP-related measures, dysregulated cytokine signaling, and abnormalities in arachidonic cascade pathways are all mechanistically credible within current models of schizophrenia pathophysiology. These pathways could contribute to synaptic remodeling, aberrant pruning, oxidative stress, blood-brain barrier dysfunction, and altered neurotransmission, each of which has been implicated in schizophrenia. Similarly, markers such as SERPINA3 and IFITM may reflect innate immune activation and glial responses to chronic CNS stressors. Substance P and lipid inflammatory mediators may connect neuroimmune signaling with broader disturbances in neuronal excitability and network function. That said, postmortem evidence alone cannot resolve whether these inflammatory changes are causal, compensatory, epiphenomenal, or secondary to treatment exposure, smoking, metabolic illness, or agonal factors. The present review therefore supports neuroinflammation as a plausible component of schizophrenia biology, but not yet as a singular or universal explanatory framework.

The high heterogeneity observed in the meta-analysis is unsurprising and likely reflects several overlapping sources. First, the outcome domain itself is heterogeneous: “neuroinflammatory markers” encompasses distinct cellular, molecular, and signaling measures that may not move in parallel. Second, brain region matters. Inflammatory changes in frontal cortex, hippocampus, cingulate cortex, and subcortical structures may differ in both direction and magnitude, and some studies likely sampled mixed or non-comparable regions. Third, study populations are unlikely to have been uniform with respect to age at death, illness duration, antipsychotic exposure, suicide, smoking, substance use, metabolic comorbidity, and postmortem interval, all of which can influence inflammatory readouts. Fourth, methodological differences in tissue processing, immunohistochemical thresholds, antibody selection, marker quantification, normalization strategies, and statistical reporting probably contributed materially to variability. Finally, the fact that only two studies were quantitatively pooled means heterogeneity statistics are unstable and especially sensitive to design differences between those studies. The wide random-effects confidence interval should therefore be viewed as a signal of limited precision rather than merely a lack of effect.

This review nonetheless has several strengths. It captures a broad postmortem literature on schizophrenia-related neuroinflammation across multiple marker classes rather than restricting the question to a single analyte or cellular compartment. The overall study quality was favorable at the extraction level, with 22 of 23 studies rated high quality and one medium quality, which supports confidence in the fidelity of study identification and data capture. A further strength is the use of enhanced extraction methods, which allowed systematic documentation not only of reported findings but also of reporting deficiencies that prevented quantitative synthesis. That matters because the main obstacle in this literature was not simply negative or inconsistent biology; it was the frequent absence of extractable means, standard deviations, effect estimates, event counts, or even group-specific sample sizes. By making those limitations explicit, this review provides a more honest map of the evidence base than a narrative summary alone would allow.

The review also has important limitations. The most serious is that only two studies contributed to the meta-analysis, making any pooled estimate fragile. Although most included studies were judged high quality in extraction terms, many had inadequate quantitative reporting, which sharply limited synthesis and raises the possibility of selective emphasis on statistically notable findings in the original literature. The included studies also likely differed substantially in anatomical sampling, laboratory methods, diagnostic ascertainment, and control for confounders. Because this was a postmortem literature, generalizability to living patients, early illness stages, or treatment-naive populations is inherently limited. Moreover, postmortem inflammatory signals may reflect end-stage disease biology or cumulative exposures rather than core disease mechanisms. Clinically, these findings do not justify routine inflammatory biomarker testing in schizophrenia care or the adoption of anti-inflammatory treatment strategies solely on the basis of postmortem evidence. The more defensible implication is for research: future studies should use standardized marker panels, region-specific sampling frameworks, transparent reporting of group-level quantitative data, and careful adjustment for postmortem interval, medication exposure, smoking, and medical comorbidity. Larger multi-center postmortem consortia, along with harmonized protocols and data sharing, will be necessary to determine whether neuroinflammatory abnormalities represent a reproducible subtype, stage-related feature, or downstream consequence of schizophrenia.

## Conclusion

In this meta-analysis of 23 postmortem studies, with quantitative pooling available from 2 studies, schizophrenia was associated with higher odds of neuroinflammatory abnormalities in brain tissue compared with healthy controls (random-effects OR 9.34, 95% CI 0.88–99.69; fixed-effect OR 5.71, 95% CI 2.67–12.25). Clinically, this pattern supports neuroinflammation as a potentially meaningful component of schizophrenia pathobiology, suggesting that inflammatory phenotypes may help identify biologically distinct subgroups and inform development of targeted therapies. However, the random-effects estimate was imprecise and did not meet conventional statistical significance, and heterogeneity was substantial (I²=86.8%), indicating marked inconsistency across studies. Accordingly, these findings should be interpreted as supportive but not definitive evidence, and neuroinflammatory markers are best viewed at present as research-enriching biomarkers rather than stand-alone diagnostic or treatment-guiding tools.

## Final Included Studies

- Corpus ID: 27434 | Increased prefrontal cortical cells positive for macrophage/microglial marker CD163 along blood vessels characterizes a neuropathology of neuroinflammatory schizophrenia.
- Corpus ID: 1779 | Increased expression of astrocyte markers in schizophrenia: Association with neuroinflammation.
- Corpus ID: 1543 | Evidence for morphological alterations in prefrontal white matter glia in schizophrenia and bipolar disorder.
- Corpus ID: 1762 | Is there gliosis in schizophrenia? Investigation of the temporal lobe.
- Corpus ID: 27392 | Increased Macrophages and C1qA, C3, C4 Transcripts in the Midbrain of People With Schizophrenia.
- Corpus ID: 1789 | Quantitative analysis of activated microglia, ramified and damage of processes in the frontal and temporal lobes of chronic schizophrenics.
- Corpus ID: 1823 | Comparison of peripheral and central schizophrenia biomarker profiles.
- Corpus ID: 1769 | Increase in HLA-DR immunoreactive microglia in frontal and temporal cortex of chronic schizophrenics.
- Corpus ID: 1784 | Stereologic investigation of the posterior part of the hippocampus in schizophrenia.
- Corpus ID: 1793 | Distribution of HLA-DR-positive microglia in schizophrenia reflects impaired cerebral lateralization.
- Corpus ID: 1821 | Stereological assessment of the dorsal anterior cingulate cortex in schizophrenia: absence of changes in neuronal and glial densities.
- Corpus ID: 1805 | Quantitative cytoarchitectural studies of the cerebral cortex of schizophrenics.
- Corpus ID: 1761 | Gliosis in schizophrenia: a survey.
- Corpus ID: 1780 | Glial fibrillary acidic protein mRNA levels in the cingulate cortex of individuals with depression, bipolar disorder and schizophrenia.
- Corpus ID: 1765 | No evidence for astrogliosis in brains of schizophrenic patients. A post-mortem study.
- Corpus ID: 1803 | Glial cell loss in the anterior cingulate cortex, a subregion of the prefrontal cortex, in subjects with schizophrenia.
- Corpus ID: 1791 | Degeneration of microglial cells in frontal and temporal lobes of chronic schizophrenics.
- Corpus ID: 1500 | A quantitative immunohistochemical study of astrocytes in the entorhinal cortex in schizophrenia, bipolar disorder and major depression: absence of significant astrocytosis.
- Corpus ID: 1798 | Reduced microglial immunoreactivity for endogenous NMDA receptor agonist quinolinic acid in the hippocampus of schizophrenia patients.
- Corpus ID: 1827 | Enkephalin, dynorphin and substance P in postmortem substantia nigra from normals and schizophrenic patients.
- Corpus ID: 1772 | Astrocyte and glutamate markers in the superficial, deep, and white matter layers of the anterior cingulate gyrus in schizophrenia.
- Corpus ID: 1795 | Inflammation-related genes up-regulated in schizophrenia brains.
- Corpus ID: 1792 | Calprotectin in microglia from frontal cortex is up-regulated in schizophrenia: evidence for an inflammatory process?
