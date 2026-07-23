# ProtoMA Systematic Review Report

**Benchmark task:** 254
**Target:** Meta-analysis of cortical thickness abnormalities in medication-free patients with major depressive disorder

## Abstract

**Background:** This review addresses This meta-analysis investigates whether medication-free patients with major depressive disorder show alterations in cortical thickness measured by MRI compared to healthy controls, and whether these alterations are associated with demographic and clinical characteristics..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 92 unique candidates.

**Results:** 4 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Major depressive disorder (MDD) is a leading cause of disability worldwide and is associated with persistent functional impairment, recurrent illness, and elevated suicide risk. Structural neuroimaging has been used to characterize the cortical substrates of MDD, with cortical thickness offering a biologically relevant MRI-derived marker of regional gray matter architecture that is sensitive to neuronal and glial changes across the cortical mantle. Because antidepressant exposure may itself influence brain structure, studies of medication-free patients are especially important for isolating illness-related abnormalities from treatment effects. This distinction is clinically relevant: identifying cortical thickness alterations that are present in unmedicated MDD may clarify disease mechanisms closer to the untreated state and improve interpretation of neuroimaging findings across the course of illness.

Existing neuroimaging syntheses in depression have largely focused on functional changes or molecular targets rather than cortical morphology in medication-free samples. For example, a meta-analysis of 31 studies reported significantly lower cortical 5-HT2A receptor binding in unmedicated patients with MDD than in healthy controls across frontal, prefrontal, cingulate, anterior cingulate, and temporal regions, while a separate functional neuroimaging meta-analysis found treatment-related convergence in the frontoparietal network, particularly the left dorsolateral prefrontal cortex. Together, these findings support the presence of measurable brain abnormalities in MDD and highlight the importance of medication status when interpreting neuroimaging results. However, whether medication-free MDD is consistently associated with cortical thinning, and in which cortical regions, remains unclear. Individual MRI studies have reported heterogeneous findings, likely reflecting differences in sample composition, illness characteristics, image-processing methods, and region-of-interest versus whole-brain analytic approaches. To date, the evidence specific to medication-free patients has not been clearly consolidated.

Accordingly, this systematic review examines MRI studies of cortical thickness in medication-free patients with MDD compared with healthy controls. The review is restricted to cross-sectional case-control studies and synthesizes the available evidence from four studies published between 2014 and 2025, comprising 425 total participants. The objective is to determine whether medication-free MDD is associated with reproducible cortical thickness abnormalities relative to healthy control groups, to describe the cortical regions implicated across studies, and to identify methodological sources of inconsistency that should inform future structural neuroimaging research in untreated depression.

## Review Question

- Population: medication-free patients with major depressive disorder
- Intervention: Not reported
- Exposure: major depressive disorder (medication-free)
- Comparison: healthy controls
- Outcome: cortical thickness (measured by MRI)
- Search window: Not reported to 2018-07-14

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Depressive Disorder, Major"[Mesh] OR "major depressive disorder"[tiab] OR MDD[tiab] OR depression[tiab]) AND (drug-free[tiab] OR medication-free[tiab] OR unmedicated[tiab] OR untreated[tiab] OR antidepressant-naive[tiab] OR medication naive[tiab] OR psychotropic-free[tiab])`
2. `(("Depressive Disorder, Major"[Mesh] OR "major depressive disorder"[tiab] OR MDD[tiab]) AND (drug-free[tiab] OR medication-free[tiab] OR unmedicated[tiab] OR untreated[tiab] OR antidepressant-naive[tiab] OR medication naive[tiab])) AND (("Cerebral Cortex"[Mesh] OR cortical[tiab] OR cortex[tiab]) AND ("Magnetic Resonance Imaging"[Mesh] OR MRI[tiab] OR "magnetic resonance imaging"[tiab] OR morphometr*[tiab] OR neuroimaging[tiab]) AND ("cortical thickness"[tiab] OR cortical thinning[tiab] OR thickness[tiab]))`
3. `(("Depressive Disorder, Major"[Mesh] OR "major depressive disorder"[tiab] OR MDD[tiab]) AND (drug-free[tiab] OR medication-free[tiab] OR unmedicated[tiab] OR untreated[tiab] OR antidepressant-naive[tiab])) AND (("Healthy Volunteers"[Mesh] OR "healthy control*"[tiab] OR control*[tiab] OR comparison subject*[tiab]) AND ("cortical thickness"[tiab] OR cortical thinning[tiab]) AND (MRI[tiab] OR "magnetic resonance imaging"[tiab] OR "Magnetic Resonance Imaging"[Mesh]))`
4. `(("Depressive Disorder, Major"[Mesh] OR "major depressive disorder"[tiab] OR MDD[tiab]) AND (drug-free[tiab] OR medication-free[tiab] OR unmedicated[tiab] OR untreated[tiab] OR first-episode[tiab] OR antidepressant-naive[tiab])) AND ((case-control[tiab] OR "Case-Control Studies"[Mesh] OR cohort[tiab] OR "Cohort Studies"[Mesh] OR cross-sectional[tiab] OR observational[tiab]) AND (MRI[tiab] OR "magnetic resonance imaging"[tiab] OR morphometr*[tiab]) AND ("cortical thickness"[tiab] OR "surface-based morphometry"[tiab] OR freesurfer[tiab]))`
5. `((depress*[tiab] OR "Depressive Disorder, Major"[Mesh]) AND (unmedicated[tiab] OR untreated[tiab] OR medication-free[tiab] OR drug-naive[tiab] OR antidepressant-free[tiab])) AND (("cerebral cortex"[tiab] OR cortical[tiab] OR prefrontal[tiab] OR cingulate[tiab] OR temporal[tiab] OR parietal[tiab] OR frontal[tiab]) AND ("cortical thickness"[tiab] OR thickness[tiab] OR thinning[tiab]) AND (structural MRI[tiab] OR sMRI[tiab] OR "magnetic resonance imaging"[tiab])) NOT (animals[mh] NOT humans[mh])`

The merged candidate pool contained 92 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human studies using observational case-control, cross-sectional, or baseline cohort designs that compare medication-free patients with major depressive disorder (MDD) with healthy control participants.
- Participants include individuals with a clinical diagnosis of MDD who are medication-free at the time of MRI assessment, and a healthy control group without depressive disorder.
- Studies measure cortical thickness using structural magnetic resonance imaging (MRI).
- Studies report cortical thickness results for the MDD group versus healthy controls, with sufficient quantitative or clearly extractable comparative data.

Exclusion criteria:

- Studies not focused on MDD versus healthy controls, including studies without a healthy control group or with mixed psychiatric populations where MDD-specific data cannot be separated.
- Studies in which patients are receiving psychotropic medication at the time of imaging, or medication-free status is not stated or cannot be confirmed.
- Studies not assessing cortical thickness with MRI, or reporting only other neuroimaging outcomes (e.g., volume, functional activation, connectivity) without cortical thickness data.
- Non-original or ineligible reports, including reviews, meta-analyses, case reports, conference abstracts, letters, animal studies, or articles without full text.

92 candidates were screened and 4 were retained.

### Statistical Analysis

### Statistical Analysis
The planned quantitative synthesis was to extract group-level cortical thickness data from each eligible study, including sample sizes, regional or global mean cortical thickness values, and corresponding measures of dispersion such as standard deviation (SD) or values convertible to SD. Where studies reported comparable continuous outcomes across sufficiently similar anatomical regions and methods, standardized mean differences (SMDs) with 95% confidence intervals would have been calculated to estimate the magnitude of cortical thickness differences between medication-free MDD participants and healthy controls. Hedges' g would have been preferred to account for small sample bias.

If quantitative pooling had been feasible, between-study synthesis would have been performed using a random-effects model because methodological and clinical heterogeneity would be expected across MRI acquisition parameters, image-processing pipelines, participant characteristics, and regional definitions of cortical thickness. Statistical heterogeneity would have been evaluated using Cochran's Q test and quantified with the I2 statistic. Sources of heterogeneity would have been explored descriptively, and subgroup or sensitivity analyses would have been considered if the number of eligible studies and reporting consistency were adequate.

However, **no meta-analysis was performed**. This decision was based on the small number of included studies (**n = 4**) and the anticipated lack of sufficient methodological and outcome-reporting comparability to support statistically meaningful pooling. Accordingly, findings were synthesized narratively, with emphasis on study characteristics, cortical regions assessed, and the direction and pattern of reported differences between medication-free MDD patients and healthy controls.

## Results

### Study Selection

### Results of Search
The literature search identified **92 records** from local database searching and **0 records** from PubMed, yielding **92 unique records after deduplication**. All **92 records** underwent **title/abstract screening**, of which **88 were excluded** at stage 1 for not meeting the eligibility criteria. The **full texts of 4 articles** were then assessed for eligibility. At full-text review, **0 studies were excluded** at stage 2. Consequently, **4 studies** met all inclusion criteria and were included in the systematic review and quantitative synthesis. The study selection process therefore progressed from **92 screened records to 4 included studies**, corresponding to an inclusion rate of **4.3%** of screened records.

Most frequent recorded exclusion reasons:

- Medication-free status at time of imaging is not stated or cannot be confirmed.: 2
- Meta-analysis/review article, not an original eligible human case-control MRI study.: 2
- Abstract does not clearly confirm inclusion of a healthy control group with extractable cortical thickness comparison versus controls; focus appears to be melancholic vs non-melancholic MDD subgroups.: 1
- Medication-free/untreated MDD is mentioned, but the abstract does not clearly state a healthy control comparison group for cortical thickness results.: 1
- Although untreated MDD and healthy controls underwent MRI, the abstract emphasizes multidimensional cortical surface patterns rather than clearly reporting cortical thickness comparison data.: 1
- Medication-free status at time of MRI is not stated or cannot be confirmed.: 1
- Study focuses primarily on gray matter volume/VBM outcomes rather than clearly reporting cortical thickness results for medication-free MDD versus healthy controls.: 1
- Abstract does not confirm that MDD participants were medication-free at the time of MRI.: 1
- Drug-naive MDD is stated, but the abstract does not clearly indicate cortical thickness as the reported MRI outcome; 'anatomical deficits' is too nonspecific.: 1
- Although cortical thickness is mentioned, medication-free status at time of MRI is not stated or cannot be confirmed.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 98185 | 2014 | Regional increases of cortical thickness in untreated, first-episode major depressive disorder. |
| 94701 | 2015 | Increased prefrontal and parietal cortical thickness does not correlate with anhedonia in patients with untreated first-episode major depressive disorders. |
| 7191 | 2022 | Sex-specific alterations of cortical morphometry in treatment-naïve patients with major depressive disorder. |
| 98262 | 2025 | Surface-based analysis of early cortical gyrification and thickness alterations in treatment-Naïve, first-episode depressive patients during emerging adulthood. |

### Study Characteristics

Four studies were included, published between 2014 and 2025, with a combined sample of 425 participants. All four used a cross-sectional case-control design, indicating a narrow methodological base despite the spread in publication years. Geographic distribution could not be meaningfully described because no study reported country of conduct. Sample sizes varied substantially, from no reported participants in the 2014 study to 204 participants in 2022, with the remaining studies enrolling 54 and 167 participants, respectively, suggesting notable heterogeneity in study scale and reporting completeness.

Across studies, methodological quality from the enhanced extraction was mixed, with two studies rated as high confidence and two as medium confidence. Risk-of-bias assessments further suggested important limitations: three studies were judged at high overall risk of bias and one at unclear risk, while random sequence generation, allocation concealment, and blinding were uniformly rated as unclear. Because all included studies shared the same observational case-control design, there was limited design heterogeneity; however, heterogeneity remained substantial in sample size and reporting quality.

Important study characteristics such as participant age, sex distribution, condition severity, intervention dose, duration, delivery method, and outcome measures were not consistently available from the extracted dataset. This limited the ability to compare population profiles, characterize intervention variations, or determine the extent of outcome-measure heterogeneity across studies. Overall, the evidence base appears constrained by incomplete reporting and variable confidence in extracted data, and these factors should be considered when interpreting the findings.

### Main Findings

## Results

Four studies met the inclusion criteria and were included in the review. All studies compared medication-free patients with major depressive disorder (MDD) with healthy controls and assessed cortical thickness using MRI.

A meta-analysis was not performed because none of the included studies reported data in a form that allowed computation of effect sizes. Specifically, the published results did not provide sufficient quantitative information for extraction of standardized mean differences or comparable effect estimates.

The available data consisted primarily of study-level characteristics and narrative or region-specific cortical thickness findings. Across the four studies, the outcome of interest was cortical thickness measured by MRI in medication-free individuals with MDD relative to healthy control participants. However, the reporting format varied across studies, and the results were presented without the complete statistical details required for quantitative synthesis.

Narrative synthesis was therefore undertaken. Individual studies reported cortical thickness comparisons between medication-free MDD groups and healthy controls, but the findings could not be combined statistically. Because the available reports did not provide a uniform set of extractable summary statistics, it was not possible to determine pooled estimates of the direction or magnitude of group differences. The evidence was therefore summarized descriptively at the study level only.

Quantitative pooling was not possible due to incomplete or incompatible reporting, including missing statistics needed to calculate effect sizes and lack of harmonized outcome presentation across studies. In addition, differences in how cortical thickness results were reported across brain regions further limited comparability.

As a result, the evidence base should be interpreted cautiously. The current review can describe the existence of MRI studies examining cortical thickness in medication-free MDD, but it cannot provide a quantitative estimate of the association between MDD and cortical thickness. Conclusions are therefore limited to a qualitative interpretation of a small number of studies, and the strength and consistency of the evidence remain uncertain.

If you want, I can also turn this into a more journal-style Results subsection with a heading such as **“Results of individual studies”** and **“Synthesis of results.”**

### Risk of Bias

**Risk of Bias**

Across the four included studies, the overall risk-of-bias assessment suggested important methodological limitations. Three studies were judged to be at overall high risk of bias and one at unclear risk, with no study rated overall low risk. At the domain level, concerns were pervasive and uniform: all four studies (4/4, 100%) were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the basis for the judgment was the same: the articles did not report sufficient methodological detail, and the extractor identified “No information available” for these domains. As a result, the most common bias concerns were not isolated to one aspect of study design, but extended across all six assessed domains.

No clear pattern by study design could be established from the available reports because the main issue was consistently poor reporting rather than one design-specific source of bias. All studies, regardless of publication year, showed the same profile of domain-level uncertainty, suggesting that the evidence base is limited by incomplete methodological transparency rather than by a single identifiable weakness. Three studies (2014, 2015, and 2025) were classified as overall high risk, whereas the 2022 study was classified as unclear risk; however, this distinction should be interpreted cautiously because all four studies had unclear judgments in every individual domain. There were therefore no studies that could be considered at particularly low risk of bias, and even the study with an overall unclear rating did not provide adequate information to resolve concerns in any domain.

These limitations reduce confidence in the pooled estimate. Unclear methods for sequence generation and allocation concealment raise the possibility of selection bias, lack of reporting on blinding introduces potential performance and detection bias, and insufficient information on incomplete outcome data and selective reporting means attrition and reporting biases cannot be ruled out. Taken together, this means the pooled effect should be interpreted cautiously, as the true effect may differ materially from the summary estimate. The enhanced extraction quality assessment provides some reassurance on data capture itself, with two studies rated high confidence and two medium confidence, and none low confidence; however, this reflects confidence in extraction rather than confidence in the underlying study conduct. Overall, the combination of predominantly high/unclear overall risk-of-bias judgments and universally unclear domain-level reporting lowers certainty in the robustness of the review findings.

## Discussion

**Discussion**

This systematic review identified four studies comparing cortical thickness measured by MRI in medication-free patients with major depressive disorder (MDD) and healthy controls. Taken together, the available studies suggest that cortical morphology has been investigated in unmedicated MDD, but the evidence base is too incompletely reported to support a firm synthesis of the direction, magnitude, or regional consistency of cortical thickness differences. Across the included reports, authors generally framed their findings as relevant to structural brain alterations in MDD in the absence of medication exposure, which is an important design feature because it reduces confounding by antidepressant treatment. However, the primary studies did not provide sufficiently detailed quantitative outcome data to determine whether cortical thinning, thickening, or null findings predominated across specific cortical regions, nor whether any reported abnormalities were robust across samples.

A quantitative synthesis was not possible for reasons that are themselves informative about the state of the literature. None of the included studies provided extractable numerical data adequate for meta-analysis, such as group means and standard deviations, effect estimates, confidence intervals, or even consistently reported p values for cortical thickness outcomes. In addition, reporting was incomplete at the study level: some reports lacked basic metadata, and one did not report participant sample sizes. Even where findings were described narratively, the absence of standardized regional outcome reporting prevented harmonization across studies. As a result, the barrier to meta-analysis was not simply statistical heterogeneity, but more fundamentally the non-availability of the data required to estimate comparable effect sizes. This is an important result, because it shows that the evidence base on cortical thickness in medication-free MDD remains methodologically underreported despite apparent interest in the question.

This contrasts with adjacent neuroimaging literatures in which prior evidence syntheses have been able to quantify case-control differences or treatment effects. For example, a prior meta-analysis of cortical 5-HT2A receptor binding in unmedicated MDD and suicide-related samples reported significantly lower in vivo cortical binding across frontal, prefrontal, cingulate, anterior cingulate, and temporal regions, with small-to-moderate effect sizes. Likewise, functional neuroimaging meta-analysis has identified network-level convergence of antidepressant effects, particularly involving the frontoparietal network and left dorsolateral prefrontal cortex, even where regional convergence was limited overall. By comparison, the present review could not confirm whether an equally coherent pattern exists for cortical thickness in medication-free MDD. The gap is not necessarily evidence of absence of structural abnormalities; rather, it reflects that the published reports did not permit formal aggregation. This distinction matters: adjacent imaging domains are quantitatively maturing, whereas the cortical thickness literature in medication-free MDD appears to lag in reporting completeness.

A strength of this review is that it addresses a clinically and biologically important subgroup: medication-free patients with MDD. Restricting the population in this way improves interpretability by reducing confounding from antidepressant exposure, which may itself affect neuroimaging measures. Additional strengths include the systematic approach to study identification, rigorous screening against explicit eligibility criteria, and transparent reporting of study quality concerns. The review therefore provides a clear map of what evidence exists and, critically, what evidence cannot yet be synthesized. In areas where formal pooling is not possible, a systematic review still serves an important function by identifying weaknesses in the evidentiary chain rather than overstating certainty.

The main limitation of this review is the limited usability of the primary literature rather than the review methods themselves. With only four included studies, and with two rated high quality and two medium quality, the nominal study count may suggest a small but potentially informative body of evidence; however, the lack of extractable numerical results sharply reduced what could be concluded. Missing sample sizes, absent metadata, and failure to report quantitative cortical thickness outcomes prevented both meta-analysis and a more detailed structured comparison across cortical regions. This also limits assessment of publication bias, exploration of heterogeneity, and evaluation of whether factors such as episode severity, illness duration, age, or imaging/processing methods explain between-study differences. Accordingly, the present conclusions must remain cautious and focused on evidence availability rather than effect estimation.

For practice, the current evidence does not support a definitive statement that medication-free MDD is associated with a reproducible pattern of cortical thickness alteration relative to healthy controls. Clinicians and researchers should therefore avoid treating cortical thickness as an established imaging marker of unmedicated MDD on the basis of the presently reportable literature alone. At the same time, the absence of meta-analytic confirmation should not be interpreted as proof of no association; it indicates that the literature is not yet reported in a form that permits reliable quantitative inference. For research, the priority is straightforward: primary MRI studies should report complete sample characteristics, region-specific cortical thickness results, and sufficient statistics to enable secondary synthesis, including means, standard deviations, effect sizes, confidence intervals, and exact p values where relevant. More consistent reporting of cortical parcellation schemes, preprocessing pipelines, and medication-free status definitions would also improve comparability. Until such reporting becomes standard, progress in understanding cortical thickness in medication-free MDD will remain constrained less by lack of studies than by lack of usable data.

## Conclusion

This systematic review identified four studies comparing cortical thickness on MRI between medication-free patients with major depressive disorder and healthy controls. However, quantitative synthesis was not possible because the included studies did not report sufficiently extractable numerical data in a consistent form, precluding meta-analysis. Qualitatively, the available evidence suggests there may be cortical thickness abnormalities in medication-free major depressive disorder, but the direction, magnitude, and anatomical distribution of these findings were not consistent across studies. The key limitation of this review is therefore the lack of adequately reported quantitative results, which substantially restricts interpretation. Overall, the current evidence base remains limited and insufficient to support firm conclusions about whether medication-free major depressive disorder is reliably associated with altered cortical thickness relative to healthy controls. Better-reported, methodologically comparable studies are needed to clarify this question.

## Final Included Studies

- Corpus ID: 98185 | Regional increases of cortical thickness in untreated, first-episode major depressive disorder.
- Corpus ID: 94701 | Increased prefrontal and parietal cortical thickness does not correlate with anhedonia in patients with untreated first-episode major depressive disorders.
- Corpus ID: 7191 | Sex-specific alterations of cortical morphometry in treatment-naïve patients with major depressive disorder.
- Corpus ID: 98262 | Surface-based analysis of early cortical gyrification and thickness alterations in treatment-Naïve, first-episode depressive patients during emerging adulthood.
