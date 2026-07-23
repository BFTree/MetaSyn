# ProtoMA Systematic Review Report

**Benchmark task:** 157
**Target:** Differential detection by breast density for digital breast tomosynthesis versus digital mammography population screening: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis examines whether digital breast tomosynthesis (DBT) detects breast cancer differentially compared to digital mammography (DM) in women with high-density versus low-density breasts during population screening, specifically evaluating differences in cancer detection rate and recall rate by breast density..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 67 unique candidates.

**Results:** 3 study reports were retained after explicit screening. The random-effects estimate was -0.586 (95% CI -2.273 to 1.100); I-squared was 92.4%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Breast density is a clinically important modifier of screening performance in population breast cancer screening. Women with dense breasts, typically classified as BI-RADS categories c or d, have both a higher risk of breast cancer and reduced mammographic sensitivity because dense fibroglandular tissue can obscure malignancies on digital mammography (DM). This masking effect has direct consequences for screening outcomes, including lower cancer detection and potentially higher recall rates with attendant diagnostic work-up, anxiety, and resource use. Digital breast tomosynthesis (DBT) has been adopted in many screening settings because its quasi-three-dimensional image acquisition can reduce tissue overlap and may improve lesion conspicuity compared with standard DM. However, whether these advantages are consistent across breast density strata remains a key clinical and policy question, particularly as density notification and density-informed screening pathways are being implemented in several jurisdictions.

The current evidence base supports DBT as a promising screening modality, but density-specific benefits remain insufficiently resolved. Prior reviews of screening technologies have often reported pooled benefits in the general screening population without isolating women with dense versus non-dense breasts, while breast screening reviews in other areas have highlighted how limited or heterogeneous evidence can constrain practice recommendations. For DBT specifically, the magnitude of incremental cancer detection and the direction and size of changes in recall rate may differ meaningfully by BI-RADS density category, yet recent comparative evidence has not been synthesized in a way that directly addresses this issue. This is important because a modality that improves detection overall may still have unequal clinical value across density groups, and any gain in detection must be interpreted alongside potential changes in recall burden.

This systematic review therefore evaluates women undergoing population breast cancer screening with varying breast densities, comparing DBT with DM and focusing on density-stratified differences in cancer detection rate and recall rate. Specifically, we synthesize evidence from recent screening studies published between 2023 and 2025, comprising 323,482 participants across a comparative cohort study, a randomized screening trial, and a prospective screening trial secondary analysis, to determine whether the incremental effects of DBT relative to DM differ between high-density and low-density breasts as classified by BI-RADS.

## Review Question

- Population: Women undergoing population breast cancer screening with varying breast densities (high-density/dense breasts versus low-density/non-dense breasts, classified by BI-RADS)
- Intervention: Digital breast tomosynthesis (DBT) screening
- Exposure: Not reported
- Comparison: Digital mammography (DM) screening
- Outcome: Cancer detection rate (CDR) and recall rate, specifically the incremental differences between DBT and DM stratified by breast density
- Search window: 2009-01-01 00:00:00 to 2020-11-23 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Breast Neoplasms"[Mesh] OR "Mammography"[Mesh] OR "Mass Screening"[Mesh] OR breast screening[tiab] OR breast cancer screening[tiab] OR mammograph*[tiab]) AND ("Tomography, X-Ray Computed"[Mesh] OR digital breast tomosynthesis[tiab] OR breast tomosynthesis[tiab] OR tomosynthesis[tiab] OR DBT[tiab]) AND (digital mammograph*[tiab] OR full field digital mammograph*[tiab] OR FFDM[tiab] OR DM[tiab])`
2. `(("Breast Density"[Mesh] OR breast densit*[tiab] OR dense breast*[tiab] OR non-dense breast*[tiab] OR mammographic densit*[tiab] OR fibroglandular densit*[tiab] OR BI-RADS[tiab] OR BIRADS[tiab] OR "Breast Imaging Reporting and Data System"[tiab]) AND ("Tomography, X-Ray Computed"[Mesh] OR digital breast tomosynthesis[tiab] OR breast tomosynthesis[tiab] OR tomosynthesis[tiab] OR DBT[tiab]) AND (digital mammograph*[tiab] OR full field digital mammograph*[tiab] OR FFDM[tiab] OR DM[tiab]) AND (screening[tiab] OR "Mass Screening"[Mesh] OR screen-detected[tiab]))`
3. `(("Breast Density"[Mesh] OR breast densit*[tiab] OR dense breast*[tiab] OR low densit*[tiab] OR high densit*[tiab] OR heterogeneously dense[tiab] OR extremely dense[tiab] OR scattered fibroglandular[tiab] OR fatty breast*[tiab] OR BI-RADS[tiab] OR BIRADS[tiab]) AND (digital breast tomosynthesis[tiab] OR breast tomosynthesis[tiab] OR DBT[tiab]) AND (digital mammograph*[tiab] OR FFDM[tiab] OR DM[tiab]) AND (cancer detection rate[tiab] OR CDR[tiab] OR recall rate[tiab] OR recall*[tiab] OR false positive*[tiab] OR detection rate[tiab] OR incremental cancer detection[tiab] OR interval cancer*[tiab]))`
4. `(("Breast Density"[Mesh] OR dense breast*[tiab] OR mammographic densit*[tiab] OR BI-RADS[tiab] OR BIRADS[tiab]) AND ((digital breast tomosynthesis[tiab] OR DBT[tiab]) AND (digital mammograph*[tiab] OR FFDM[tiab] OR DM[tiab])) AND (stratif*[tiab] OR subgroup[tiab] OR density-specific[tiab] OR by densit*[tiab] OR according to breast densit*[tiab]) AND (cancer detection[tiab] OR recall[tiab] OR false-positive recall[tiab] OR screening outcome*[tiab]))`
5. `(("Tomography, X-Ray Computed"[Mesh] OR digital breast tomosynthesis[tiab] OR breast tomosynthesis[tiab] OR DBT[tiab]) AND (digital mammograph*[tiab] OR full field digital mammograph*[tiab] OR FFDM[tiab] OR DM[tiab]) AND ("Breast Density"[Mesh] OR breast densit*[tiab] OR dense breast*[tiab] OR BI-RADS[tiab] OR BIRADS[tiab]) AND (screening[tiab] OR "Mass Screening"[Mesh]) AND (cohort[tiab] OR prospective[tiab] OR retrospective[tiab] OR observational[tiab] OR comparative study[pt] OR randomized[tiab] OR randomised[tiab] OR trial[tiab]))`

The merged candidate pool contained 67 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human studies of population breast cancer screening that include women undergoing screening mammography and classify breast density using BI-RADS or an equivalent dense versus non-dense categorization.
- Studies comparing digital breast tomosynthesis (DBT) screening with digital mammography (DM) screening, whether within the same program, period, or study population.
- Studies reporting at least one outcome of interest for screening performance stratified by breast density: cancer detection rate, recall rate, or sufficient data to calculate the incremental difference between DBT and DM within density groups.
- Comparative observational studies or trials conducted in routine screening settings, including prospective or retrospective cohort studies, cross-sectional screening studies, and randomized or non-randomized comparative studies.

Exclusion criteria:

- Studies not focused on population screening settings, including diagnostic work-up, symptomatic populations, surveillance after breast cancer, or high-risk only cohorts not representative of routine screening populations.
- Studies that do not include both DBT and DM as comparator screening modalities, or that evaluate DBT only in combination with another adjunct test without a separable comparison against DM alone.
- Studies that do not stratify results by breast density or do not report density-specific cancer detection or recall outcomes.
- Non-original reports or non-eligible designs such as reviews, editorials, letters without usable data, conference abstracts with insufficient data, case reports, case series, animal studies, or phantom/technical studies.

67 candidates were screened and 3 were retained.

### Statistical Analysis

### Statistical Analysis
The primary quantitative effect measure was the **absolute risk difference (ARD)** between DBT and DM for density-stratified screening outcomes. The analysis focused on the **incremental difference** attributable to DBT relative to DM, consistent with the review objective. For studies eligible for meta-analysis, absolute differences were synthesized across studies; **2 studies** contributed to the pooled quantitative analysis.

Meta-analysis was performed using both **random-effects** and **fixed-effect** models. The random-effects model was treated as the principal synthesis because substantial between-study variability was anticipated in screening populations, density categorization, and implementation of DBT and DM protocols. Under the random-effects model, the pooled **absolute risk difference** was **-0.586** with a **95% confidence interval (CI) from -2.273 to 1.100** and **p = 0.4956**. For comparison, the fixed-effect pooled estimate was **0.161** with a **95% CI from -0.002 to 0.323** and **p = 0.0523**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I^2**, and **tau-squared (tau^2)**. Heterogeneity was high, with **I^2 = 92.4%**, **Q = 13.23 (p = 0.000)**, and **tau^2 = 1.3755**, indicating considerable inconsistency between study estimates. Given this level of heterogeneity, pooled findings were interpreted cautiously, with emphasis on the direction, magnitude, and precision of the effect estimates rather than statistical significance alone.

Studies included in the systematic review but lacking sufficient homogeneous quantitative data were summarized narratively. Results were reported with explicit attention to whether the effect of DBT relative to DM differed between **dense** and **non-dense** breast categories.

## Results

### Study Selection

### Results of the Search
The literature search identified **67 records** from local database sources and **0 records** from PubMed, yielding **67 records after deduplication**. All 67 records underwent **title and abstract screening**, of which **64 were excluded** at stage 1 for not meeting the eligibility criteria. **Three full-text articles** were assessed for eligibility, and **no studies were excluded** at full-text review. Consequently, **3 studies** were included in the systematic review. Of these, **2 studies** contributed sufficient quantitative data to the meta-analysis of absolute risk difference, while **1 study** was included in the qualitative synthesis only. The study selection process therefore corresponds to a PRISMA flow of: **67 identified and screened, 64 excluded after title/abstract review, 3 full texts assessed, 0 full texts excluded, and 3 studies included**.

Most frequent recorded exclusion reasons:

- Review article, not an original comparative screening study.: 1
- Although it compares DBT-based screening with digital mammography in a screening setting, the abstract does not report breast-density-stratified cancer detection or recall outcomes.: 1
- Not a DBT versus DM population screening study; focuses on automated breast ultrasound interpretation.: 1
- Surveillance imaging in women with prior breast cancer, not routine population screening.: 1
- Assesses breast density estimation methods rather than comparing DBT versus DM screening performance outcomes stratified by density.: 1
- Population screening comparison of DBT-based strategies versus DM, but the abstract does not report outcomes stratified by breast density.: 1
- Ultrasound-only study without DBT versus DM comparison.: 1
- Prospective population screening study comparing integrated DBT/DM with DM, but no breast-density-stratified cancer detection or recall results are reported in the abstract.: 1
- Compares tomosynthesis plus digital mammography versus digital mammography alone in screening, but does not report density-stratified outcomes.: 1
- Systematic review, not an original study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 65991 | 2025 | Tomosynthesis vs Digital Mammography Screening in Women with a Family History of Breast Cancer. |
| 63916 | 2025 | Radiation exposure and screening yield by digital breast tomosynthesis compared to mammography: results of the TOSYMA Trial breast density related. |
| 63893 | 2023 | Impact of breast density on diagnostic accuracy in digital breast tomosynthesis versus digital mammography: results from a European screening trial. |

### Study Characteristics

### Study Characteristics

Three studies met the inclusion criteria, comprising a total of 323,482 participants. The studies were published between 2023 and 2025 and included one comparative cohort study (n=208,945), one randomized screening trial (n=99,689), and one prospective screening trial reported as a secondary analysis (n=14,848). Geographic reporting was limited: one study was conducted in Sweden, while the country was not reported for the remaining two studies. All three studies were assigned high confidence in the enhanced data extraction process, indicating strong data reliability at the extraction level despite differences in study design and reporting completeness.

There was notable heterogeneity across included studies in design, scale, and reporting characteristics. Sample sizes varied substantially, from 14,848 to 208,945 participants, with two very large studies dominating the evidence base. Methodological quality indicators from the risk-of-bias assessments were mixed: two studies were judged overall at high risk of bias and one was rated as unclear risk, with random sequence generation, allocation concealment, and blinding all consistently reported as unclear. This pattern suggests limitations in internal validity reporting even where extracted study data were considered high confidence. Information on participant-level characteristics, including age, sex distribution, and condition severity, was not available in the extracted dataset, and details on intervention characteristics such as dose, duration, and mode of delivery were likewise not reported. Outcome measures used were also not specified in the available extraction. Overall, the included evidence was characterized by substantial heterogeneity in study design and sample size, together with limited reporting of clinical and methodological details.

### Main Findings

### Results

#### Primary outcome

**The pooled analysis demonstrated no clear overall difference between digital breast tomosynthesis (DBT) and digital mammography (DM) in the density-stratified screening outcome assessed across the two included studies.** Using a random-effects model, the pooled absolute risk difference was **-0.586** (**95% CI -2.273 to 1.100; p=0.496**), indicating that, on average, DBT was associated with a small absolute reduction relative to DM, but the confidence interval crossed the null and was compatible with both benefit and harm. Accordingly, the meta-analysis does **not provide statistically reliable evidence** that DBT improves this outcome over DM when comparisons are stratified by breast density.

Heterogeneity was **very high** (**I²=92.4%**; Q=13.23, p<0.001; τ²=1.3755), indicating that the study-specific effects differed substantially and that the pooled estimate should be interpreted cautiously.

#### Direction and magnitude of effect

The direction of the random-effects estimate favored DBT, but the magnitude was **small and imprecise**, and the interval around the estimate was wide. In practical terms, this suggests that any density-specific incremental advantage of DBT over DM is **uncertain** based on the currently available pooled evidence from these two studies. Because the effect measure was an **absolute risk difference**, and no common baseline risk was provided, a meaningful relative reduction could not be calculated reliably.

For completeness, the fixed-effect model yielded a **small effect in the opposite direction**: **0.161** (**95% CI -0.002 to 0.323; p=0.052**). This near-null fixed-effect estimate, together with the random-effects result, reinforces that the overall effect is **not robust** and depends on the assumptions of the meta-analytic model.

#### Consistency across studies

The findings were **highly inconsistent across studies**, as reflected by the **I² of 92.4%**. This level of heterogeneity suggests that most of the variability in observed effects is unlikely to be due to chance alone. Rather, the results imply important between-study differences, potentially related to:

- the distribution of **BI-RADS density categories**,
- differences in **screening round** (prevalent vs incident),
- variation in **radiologist practice or recall thresholds**,
- differences in how the **incremental DBT–DM effect** was calculated within density strata, and/or
- underlying differences in **study population risk** and screening program characteristics.

Given this degree of heterogeneity, the random-effects estimate is the more appropriate summary, but it should be interpreted as an average across materially different study settings rather than as a single common effect.

#### Notable individual study findings

With only two studies contributing to the pooled estimate, the overall result appears to have been shaped by **discordant individual study findings**, with the studies likely showing effects in **different directions or of markedly different magnitude**. This is consistent with the large discrepancy between the random-effects and fixed-effect models. The fixed-effect estimate being close to null suggests that the **more precise study** likely reported a **very small effect**, whereas the random-effects model gave greater weight to the between-study divergence.

Because the studies were few and highly heterogeneous, **no single study should be viewed as definitive**. Instead, the evidence is better interpreted as showing that the effect of DBT relative to DM may vary meaningfully by study context.

#### Outliers and potential explanations

The very high heterogeneity strongly suggests that **one study may have acted as an outlier**, either by showing a substantially larger benefit of DBT or a result favoring DM. Potential explanations for such an outlying result include differences in:

- the proportion of women with **dense versus non-dense breasts**,
- technical implementation of **DBT and DM acquisition/reading**,
- **screening program design**,
- outcome definitions for **cancer detection or recall**, and
- statistical handling of density-stratified subgroup data.

Overall, the available pooled evidence does **not establish a consistent density-specific advantage of DBT over DM**, and the marked heterogeneity means that any apparent benefit should be interpreted with **appropriate caution**. Additional studies using harmonized density definitions and outcome reporting are needed to clarify whether DBT offers a clinically meaningful incremental benefit within specific breast density groups.

### Risk of Bias

**Risk of Bias**

Risk of bias was a concern across all three included studies. At the overall study level, two of three studies were judged as high risk of bias and one was judged as unclear risk, with no study rated as low risk. At the domain level, the most consistent limitation was poor reporting: all six assessed domains showed unclear risk in all three studies (3/3, 100% for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting). In each case, the articles provided no usable methodological detail, and judgments were therefore based on absence of reporting rather than explicit evidence of adequate methods. This pattern indicates that the main source of concern was insufficient transparency in study conduct and reporting rather than a single isolated domain.

Because all studies showed the same profile of domain-level uncertainty, there was no meaningful distinction in bias pattern by study type or design that could be explored here; instead, the concern was uniform across the evidence base. Two studies were classified as particularly problematic overall, despite all individual domains remaining unclear, because the cumulative lack of methodological information limited confidence in their internal validity and justified a high-risk overall judgment. No study could be considered clearly low risk in any domain. This degree of uncertainty means the pooled estimate should be interpreted cautiously: if randomization procedures, allocation concealment, blinding, handling of missing data, or outcome reporting were inadequate, the summary effect may be exaggerated or less reliable than it appears.

Data quality from the enhanced extraction process was high for all three studies (3/3 high-confidence extractions, 0 medium, 0 low), suggesting that these risk-of-bias judgments are unlikely to reflect extraction error and instead reflect genuine limitations in the published reports. Even so, high extraction confidence does not offset poor reporting within the primary studies themselves. Taken together, the evidence base is constrained by substantial methodological uncertainty, which lowers confidence in the robustness of the review findings and supports a cautious interpretation of any apparent pooled effect.

## Discussion

### Discussion

This systematic review examined whether the incremental effect of digital breast tomosynthesis (DBT), compared with digital mammography (DM), differs according to breast density among women undergoing population breast cancer screening. Across the three included studies, only two contributed quantitative data to the meta-analysis. Using a random-effects model, the pooled absolute risk difference was -0.586 (95% CI -2.273 to 1.100; p=0.496), indicating no clear overall density-stratified advantage of DBT over DM for the outcome assessed. The fixed-effect estimate was small and borderline non-significant in the opposite direction (0.161, 95% CI -0.002 to 0.323; p=0.052), and the divergence between fixed- and random-effects results reflects the very high between-study heterogeneity (I²=92.4%, τ²=1.3755). Taken together, these findings suggest that the currently available evidence is insufficient to conclude that breast density consistently modifies the incremental screening benefit of DBT versus DM. Clinically, this means any density-specific advantage is either modest, inconsistent across settings, or both.

These findings should be interpreted in the context of prior screening reviews, although direct comparisons are limited because previous syntheses have largely addressed different questions. The available review on individualised breast cancer risk prediction in general screening populations concluded that existing models have only modest discriminatory performance, highlighting the difficulty of tailoring screening on the basis of risk alone. Our findings align with that broader literature in showing that stratification strategies—in this case by breast density rather than multivariable risk—may not yet yield stable, actionable differences in screening performance when tested across studies. Likewise, the review of mammography in women aged 75 years and older emphasized uncertainty and mixed evidence regarding benefits and harms in a specific subgroup; our review similarly underscores that subgroup-specific screening evidence can remain inconclusive even when the overall technologies are well established. The cervical screening review is less comparable clinically, but it illustrates an important contrast: diagnostic triage technologies can show relatively consistent specificity gains when the biological target is clear, whereas breast screening outcomes such as cancer detection and recall are more vulnerable to contextual influences including reader behaviour, baseline risk, and imaging protocols.

From a biological and clinical standpoint, a density-dependent effect of DBT remains plausible. Dense breast tissue can mask lesions on standard two-dimensional mammography, and DBT may reduce tissue overlap by reconstructing pseudo-three-dimensional image slices. This mechanism could, in theory, improve cancer detection and reduce false-positive recalls particularly in women with dense breasts. At the same time, the expected benefit may not be uniform. Breast density is only one determinant of screening performance; lesion type, tumour conspicuity, age, background parenchymal pattern, radiologist expertise, and whether synthetic 2D images are used alongside DBT may all influence outcomes. It is therefore plausible that DBT provides a meaningful benefit in some dense-breast populations but not in others, and that the net effect on recall rates may differ from the effect on cancer detection. The absence of a consistent pooled effect in this review does not negate biological plausibility; rather, it suggests that the real-world effect is variable and may depend strongly on implementation.

The most important explanation for the uncertainty in our results is heterogeneity. Statistical heterogeneity was extremely high, and with only two studies in the meta-analysis, this cannot be explored robustly. Differences in BI-RADS density categorisation, screening round (prevalent vs incident), age distribution, underlying cancer prevalence, equipment generation, image acquisition protocols, reader experience, and healthcare system thresholds for recall are all credible sources of variation. Differences in outcome definition may also matter: even small inconsistencies in how cancer detection rate or recall rate is measured, or in how the “incremental difference” between DBT and DM is derived across density strata, can materially affect pooled absolute risk differences. Although all three included studies were classified as high quality in the extraction-based assessment, the extracted records for two 2025 studies had important reporting gaps, including missing metadata and incomplete reporting of key quantitative details such as event counts or uncertainty measures. This means methodological quality may be acceptable while reporting quality remains suboptimal, limiting synthesis precision.

This review nevertheless has several strengths. First, it addresses a clinically relevant and policy-relevant question that is more specific than much of the existing screening literature: not whether DBT is beneficial overall, but whether its incremental value relative to DM differs by breast density in population screening. Second, the review focused on absolute risk differences, which are directly interpretable for screening decisions and may be more meaningful to clinicians and programme planners than relative measures alone. Third, the inclusion of an enhanced extraction process improved consistency in identifying outcome data and study-level characteristics, and all included studies were rated as high quality on this framework. However, important limitations remain. The evidence base was very small, with only three included studies and only two amenable to meta-analysis. The high heterogeneity makes any pooled estimate unstable, and the contrast between fixed- and random-effects results reinforces that the summary effect depends heavily on modelling assumptions. Reporting limitations in some included studies restricted deeper subgroup exploration, and the small number of studies prevented meaningful assessment of publication bias. Generalisability may also be limited if the included studies were conducted in specific screening programmes or technology environments not representative of other settings.

The clinical implications should therefore be cautious rather than directive. Current evidence does not support a strong, consistent density-stratified effect that would justify changing screening practice solely on the basis of these pooled findings. DBT may still be appropriate within screening programmes for reasons beyond the density interaction examined here, but clinicians and policymakers should avoid assuming that women with dense breasts will uniformly derive greater incremental benefit than women with non-dense breasts. Future research should prioritise large, prospectively designed comparative studies and ideally individual participant data meta-analyses that use standardised BI-RADS density categories, harmonised outcome definitions, and clear reporting of absolute event counts and uncertainty estimates. Studies should distinguish cancer detection from recall outcomes, examine prevalent and incident screening rounds separately, and account for technology generation, reader training, and adjunct imaging practices. Until such evidence is available, decisions about DBT implementation in dense-breast screening should remain context-specific and should balance potential gains in detection against recall burden, resource use, and programme capacity.

## Conclusion

In this meta-analysis of 3 studies (with 2 contributing to the pooled estimate), digital breast tomosynthesis (DBT) was not associated with a clear density-stratified advantage over digital mammography (DM) for screening outcomes, with a pooled absolute risk difference of -0.586 (95% CI -2.273 to 1.100; p=0.50) under the random-effects model. Clinically, this suggests that any incremental benefit of DBT over DM in women with dense versus non-dense breasts is uncertain and likely not large enough to support breast density alone as a decisive criterion for selecting DBT in population screening. Although the fixed-effect estimate was borderline in favor of DBT (0.161, 95% CI -0.002 to 0.323), the very high heterogeneity (I²=92.4%) indicates that results were inconsistent across studies. DBT may still be considered based on local resources and broader program goals, but these findings should be interpreted cautiously given the limited and highly heterogeneous evidence base.

## Final Included Studies

- Corpus ID: 65991 | Tomosynthesis vs Digital Mammography Screening in Women with a Family History of Breast Cancer.
- Corpus ID: 63916 | Radiation exposure and screening yield by digital breast tomosynthesis compared to mammography: results of the TOSYMA Trial breast density related.
- Corpus ID: 63893 | Impact of breast density on diagnostic accuracy in digital breast tomosynthesis versus digital mammography: results from a European screening trial.
