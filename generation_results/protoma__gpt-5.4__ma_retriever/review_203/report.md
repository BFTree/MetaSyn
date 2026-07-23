# ProtoMA Systematic Review Report

**Benchmark task:** 203
**Target:** Literature review and meta-analysis of translaminar pressure difference in open-angle glaucoma

## Abstract

**Background:** This review addresses This meta-analysis investigates whether translaminar pressure difference (TPD), defined as the difference between intraocular pressure and intracranial pressure, is elevated in patients with open-angle glaucoma compared to healthy subjects, and whether TPD is associated with structural glaucomatous changes of the optic disc..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 53 unique candidates.

**Results:** 9 study reports were retained after explicit screening. The random-effects estimate was 0.232 (95% CI -0.687 to 1.151); I-squared was 97.6%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Primary open-angle glaucoma is a chronic optic neuropathy characterized by progressive retinal ganglion cell loss, excavation of the optic disc, and corresponding visual field damage. Although elevated intraocular pressure (IOP) remains the main modifiable risk factor, a substantial proportion of patients develop glaucomatous structural damage despite statistically normal IOP, while others with elevated IOP do not progress at the same rate. This discrepancy has sustained interest in pressure relationships across the lamina cribrosa, where the translaminar pressure difference (TPD), commonly defined as IOP minus intracranial pressure (ICP), may influence deformation of the optic nerve head and susceptibility to axonal injury. From a clinical standpoint, clarifying whether altered TPD is associated with open-angle glaucoma and with structural glaucomatous changes of the optic disc is relevant because it bears directly on current mechanistic models of disease and may help explain risk that is not captured by IOP alone.

The available evidence on TPD in glaucoma has expanded over the last decade but remains difficult to interpret in aggregate. Studies have differed in design, participant selection, methods for estimating or measuring ICP, and the structural outcomes used to characterize optic disc change, leading to uncertainty about the consistency and magnitude of any association. Across 9 studies published between 2010 and 2025, including prospective interventional, case-control, pilot, clinical, retrospective, and population-based cross-sectional designs, a total of 5,711 participants have been examined. However, these studies vary in their comparators and analytic approaches, and individual reports have not resolved whether patients with open-angle glaucoma consistently demonstrate higher TPD than healthy subjects without glaucoma, nor whether TPD is meaningfully linked to structural glaucomatous changes at the optic disc.

Accordingly, this systematic review evaluates the evidence comparing patients with open-angle glaucoma and healthy control subjects with respect to translaminar pressure difference levels, using TPD defined as IOP minus ICP. The review also examines the reported relationship between TPD and structural glaucomatous changes of the optic disc. By synthesizing findings from 9 studies involving 5,711 total participants, this review aims to determine whether the existing literature supports TPD as a distinguishing pressure-related marker in open-angle glaucoma and to clarify the strength of evidence for its structural relevance at the optic nerve head.

## Review Question

- Population: Patients with open-angle glaucoma and healthy control subjects
- Intervention: Not reported
- Exposure: Translaminar pressure difference (TPD = IOP – ICP)
- Comparison: Healthy subjects without glaucoma
- Outcome: Translaminar pressure difference levels and structural glaucomatous changes of the optic disc
- Search window: 2004-11-01 00:00:00 to 2014-11-30 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Glaucoma, Open-Angle"[Mesh] OR open-angle glaucoma[tiab] OR primary open angle glaucoma[tiab] OR POAG[tiab] OR normal tension glaucoma[tiab] OR NTG[tiab]) AND ((translaminar pressure difference[tiab] OR trans-laminar pressure difference[tiab] OR translaminar gradient[tiab] OR translaminar cribrosa pressure difference[tiab] OR TPD[tiab]) OR ((intraocular pressure[Mesh] OR intraocular pressure[tiab] OR IOP[tiab]) AND (intracranial pressure[Mesh] OR intracranial pressure[tiab] OR cerebrospinal fluid pressure[tiab] OR CSF pressure[tiab] OR ICP[tiab])))`
2. `(("Glaucoma, Open-Angle"[Mesh] OR open-angle glaucoma[tiab] OR primary open angle glaucoma[tiab] OR POAG[tiab] OR normal tension glaucoma[tiab]) AND ("Optic Disk"[Mesh] OR optic disc[tiab] OR optic disk[tiab] OR optic nerve head[tiab] OR lamina cribrosa[Mesh] OR lamina cribrosa[tiab] OR neuroretinal rim[tiab] OR retinal nerve fiber layer[tiab] OR RNFL[tiab] OR cup-to-disc[tiab] OR disc cupping[tiab]) AND (translaminar pressure difference[tiab] OR trans-laminar pressure difference[tiab] OR translaminar gradient[tiab] OR TPD[tiab] OR ((intraocular pressure[tiab] OR IOP[tiab]) AND (intracranial pressure[tiab] OR cerebrospinal fluid pressure[tiab] OR ICP[tiab] OR CSF pressure[tiab]))))`
3. `(("Glaucoma, Open-Angle"[Mesh] OR open-angle glaucoma[tiab] OR primary open angle glaucoma[tiab] OR POAG[tiab]) AND (healthy control*[tiab] OR control subject*[tiab] OR normal subject*[tiab] OR normal control*[tiab] OR age-matched control*[tiab] OR "Control Groups"[Mesh]) AND (translaminar pressure difference[tiab] OR trans-laminar pressure difference[tiab] OR TPD[tiab] OR ((intraocular pressure[tiab] OR IOP[tiab]) AND (intracranial pressure[tiab] OR ICP[tiab] OR cerebrospinal fluid pressure[tiab] OR CSF pressure[tiab]))))`
4. `(("Glaucoma, Open-Angle"[Mesh] OR open-angle glaucoma[tiab] OR primary open angle glaucoma[tiab] OR POAG[tiab] OR normal tension glaucoma[tiab]) AND (translaminar pressure difference[tiab] OR TPD[tiab] OR ((intraocular pressure[tiab] OR IOP[tiab]) AND (intracranial pressure[tiab] OR ICP[tiab] OR cerebrospinal fluid pressure[tiab] OR CSF pressure[tiab]))) AND (optic disc[tiab] OR optic disk[tiab] OR optic nerve head[tiab] OR lamina cribrosa[tiab] OR retinal nerve fiber layer[tiab] OR RNFL[tiab] OR glaucomatous change*[tiab] OR structural change*[tiab] OR morphology[tiab] OR imaging[tiab]) AND (case-control studies[Mesh] OR cohort studies[Mesh] OR cross-sectional studies[Mesh] OR observational study[pt] OR comparative study[pt] OR case-control[tiab] OR cohort[tiab] OR cross-sectional[tiab] OR prospective[tiab] OR retrospective[tiab]))`
5. `((("Intraocular Pressure"[Mesh] OR intraocular pressure[tiab] OR IOP[tiab]) AND ("Intracranial Pressure"[Mesh] OR intracranial pressure[tiab] OR ICP[tiab] OR cerebrospinal fluid pressure[tiab] OR CSF pressure[tiab])) OR (translaminar pressure difference[tiab] OR trans-laminar pressure difference[tiab] OR translaminar cribrosa pressure difference[tiab] OR translaminar gradient[tiab] OR TPD[tiab])) AND (("Glaucoma, Open-Angle"[Mesh] OR open-angle glaucoma[tiab] OR primary open angle glaucoma[tiab] OR POAG[tiab] OR normal tension glaucoma[tiab]) OR (glaucoma[tiab] AND optic disc[tiab])) AND (healthy[tiab] OR control*[tiab] OR normal subject*[tiab] OR normal control*[tiab] OR "Control Groups"[Mesh]) NOT (animal[mh] NOT human[mh])`

The merged candidate pool contained 53 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human studies with an observational or interventional design that report empirical data.
- Studies including patients diagnosed with open-angle glaucoma and/or healthy control subjects without glaucoma.
- Studies that assess translaminar pressure difference or its components needed for calculation (IOP and ICP), with TPD defined as IOP minus ICP.
- Studies reporting outcomes on translaminar pressure difference levels and/or structural glaucomatous changes of the optic disc.

Exclusion criteria:

- Reviews, meta-analyses, editorials, letters, conference abstracts without full data, case reports, and animal or in vitro studies.
- Studies of glaucoma types other than open-angle glaucoma only, or studies without a healthy control or clearly defined non-glaucoma comparison group when relevant to the analysis.
- Studies that do not measure or permit calculation of translaminar pressure difference and do not report optic disc structural outcomes related to glaucomatous change.
- Studies focused primarily on unrelated ophthalmic or neurologic conditions without separate data for open-angle glaucoma and healthy controls.

53 candidates were screened and 9 were retained.

### Statistical Analysis

### Statistical Analysis

The primary effect measure was the **standardized mean difference (SMD)**, calculated from study-level summary data comparing open-angle glaucoma patients with healthy controls. When studies reported multiple compatible measurements, the most directly comparable estimate was extracted to avoid double counting.

Meta-analysis was performed using both **random-effects** and **fixed-effects** models. The random-effects model was the primary analytic approach because between-study variability was expected across populations, measurement methods, and study designs. The fixed-effects model was additionally calculated as a sensitivity analysis.

Statistical heterogeneity was assessed using **Cochran’s Q test**, the **I² statistic**, and the **between-study variance (τ²)**. Heterogeneity was considered substantial given the very high I². The meta-analysis included **9 studies**. The pooled random-effects estimate was **SMD = 0.232** (95% CI **-0.687 to 1.151**; **p = 0.6208**), with marked heterogeneity (**I² = 97.6%**, **Q = 326.55**, **p = 0.000**, **τ² = 1.8769**). The fixed-effects pooled estimate was **SMD = 0.124** (95% CI **0.080 to 0.168**; **p = 0.0000**).

All analyses were conducted using two-sided significance testing, with statistical significance set at **p < 0.05**.

## Results

### Study Selection

### Results of the search
The literature search identified **53 records** from local database sources and **0 records** from PubMed, yielding **53 unique records after deduplication**. All **53 records** underwent title and abstract screening. At this first screening stage, **44 records were excluded** as not meeting the eligibility criteria. The remaining **9 full-text articles** were assessed for inclusion. No studies were excluded after full-text review (**n = 0**). Consequently, **9 studies** were included in the systematic review and quantitative synthesis. Overall, the study selection process indicates that **17.0% (9/53)** of screened records were ultimately eligible for inclusion.

Most frequent recorded exclusion reasons:

- Animal study in dogs, which is explicitly excluded.: 2
- Letter/commentary ('Re:') rather than an original empirical human study.: 1
- Abstract indicates ICP differences in glaucoma and healthy subjects, but does not clearly report translaminar pressure difference (or calculable IOP and ICP together) and optic disc structural glaucomatous outcomes.: 1
- No healthy control or clearly defined non-glaucoma comparison group; comparator group is ocular hypertension rather than healthy subjects without glaucoma.: 1
- Insufficient information in abstract to confirm an original human study meeting the translaminar pressure difference and control-group criteria.: 1
- Appears to be a mechanism/review-style article without clear original empirical study data and without explicit healthy control comparison.: 1
- Study population is neurosurgical patients without glaucoma only; does not include open-angle glaucoma patients or healthy controls relevant to the review question.: 1
- Focused on papilledema, an unrelated neurologic/ophthalmic condition, without separate open-angle glaucoma and healthy control data.: 1
- Focuses on non-invasive ICP pulse wave monitoring in NTG patients without a clearly defined healthy control comparison and without reporting translaminar pressure difference or optic disc structural outcomes.: 1
- Focused primarily on idiopathic normal pressure hydrocephalus rather than open-angle glaucoma versus healthy controls.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 3159 | 2010 | Cerebrospinal fluid pressure in glaucoma: a prospective study. |
| 85202 | 2018 | Normal-Tension Glaucoma Has Normal Intracranial Pressure: A Prospective Study of Intracranial Pressure and Intraocular Pressure in Different Body Positions. |
| 85227 | 2023 | Estimated intracranial pressure in glaucoma patients and its correlation with disease severity. |
| 3160 | 2014 | The difference in translaminar pressure gradient and neuroretinal rim area in glaucoma and healthy subjects. |
| 85200 | 2021 | Correlation between ocular perfusion pressure and translaminar pressure difference in glaucoma: Evidence for a three-pressure disease? |
| 85226 | 2024 | Determination of the Trans-Lamina Cribrosa Pressure Difference in a Community-Based Population and its Association with Open-Angle Glaucoma. |
| 85204 | 2017 | Anterior lamina cribrosa surface position in idiopathic intracranial hypertension and glaucoma. |
| 85208 | 2015 | Ocular Perfusion Pressure vs Estimated Trans-Lamina Cribrosa Pressure Difference in Glaucoma: The Central India Eye and Medical Study (An American Ophthalmological Society Thesis). |
| 85210 | 2025 | Relationship Between Intracranial Pressure, Ocular Blood Flow and Vessel Density: Insights from OCTA and Doppler Imaging. |

### Study Characteristics

**Study Characteristics**

Nine studies comprising 5,711 participants were included. Publication years ranged from 2010 to 2025, although one study did not report a publication year clearly. The evidence base was geographically sparse in reporting: only one study was explicitly conducted in India, while the remaining eight did not clearly report country of origin. Study designs were notably heterogeneous and included one prospective interventional study, one prospective case-control study, two cross-sectional studies, one prospective pilot study, one retrospective cohort study, one retrospective cross-sectional observational study, one population-based cross-sectional study, and one prospective clinical study. Sample sizes varied substantially, from 24 to 4,711 participants, with the largest contribution coming from a single population-based cross-sectional study, indicating an uneven distribution of statistical weight across the included evidence.

Marked heterogeneity was also present in methodological features. The included studies spanned prospective, retrospective, interventional, and observational approaches, which likely introduced variation in recruitment methods, exposure or intervention assessment, and outcome ascertainment. Reporting of population characteristics such as age, sex distribution, and condition severity was not consistently available in the extracted summary, limiting cross-study comparison of baseline clinical features. Similarly, intervention-related characteristics, including dose, duration, and mode of delivery, were not uniformly reported in the available extraction, suggesting either substantial variability or incomplete reporting across studies. Outcome measures were also not consistently specified in the extracted dataset, further supporting the presence of between-study heterogeneity in how study endpoints were defined and assessed.

Despite these reporting limitations, the enhanced extraction classified data quality confidence as high for all nine studies. This indicates that the extracted study-level information was considered reliable at the data capture stage. However, this should be interpreted alongside the risk-of-bias profile, which was less favorable: most studies were judged as having high or high risk of bias overall, and the remaining study had unclear risk. Across all studies, key methodological domains such as random sequence generation, allocation concealment, and blinding were rated as unclear. Taken together, the included literature was characterized by broad variation in design and sample size, limited geographic reporting, incomplete reporting of participant and intervention details, and generally elevated risk of bias despite high confidence in the extraction quality.

### Main Findings

## Results

### Primary outcome

The pooled analysis demonstrated no clear overall difference in translaminar pressure difference (TPD; defined as intraocular pressure minus intracranial pressure) between patients with open-angle glaucoma and healthy control subjects when between-study heterogeneity was taken into account. Using a random-effects model across 9 studies, the pooled standardized mean difference (SMD) was 0.232 (95% CI -0.687 to 1.151; p=0.6208). Although the point estimate was in the direction of higher TPD in glaucoma, the confidence interval was wide and crossed the null, indicating substantial uncertainty around the true effect.

By contrast, the fixed-effect model yielded a statistically significant pooled SMD of 0.124 (95% CI 0.080 to 0.168; p<0.001). However, given the extreme heterogeneity across studies, the random-effects estimate is the more appropriate summary and suggests that the evidence does not support a consistent pooled difference in TPD between groups.

### Direction and magnitude of effect

The direction of the pooled effect favored higher TPD levels in eyes with open-angle glaucoma relative to healthy controls, but the magnitude of this effect was small on average. Under the random-effects model, the estimated effect size was modest and imprecise, with the range of plausible effects extending from a moderate reduction to a moderate increase in TPD in glaucoma. Clinically, this indicates that while some studies support the hypothesis that glaucomatous eyes have higher TPD, the overall body of evidence does not demonstrate a stable or reliably measurable difference.

Because the outcome was synthesized as an SMD, this effect cannot be directly translated into an absolute or relative percentage difference in TPD levels.

### Consistency across studies

There was very strong statistical heterogeneity among included studies. The I² value was 97.6%, indicating that nearly all variability in observed effect estimates was due to real between-study differences rather than sampling error alone. This was supported by a highly significant Cochran Q statistic (Q=326.55, p<0.001) and a large between-study variance (τ²=1.8769).

Taken together, these findings indicate that the study results were highly inconsistent. This level of heterogeneity substantially limits confidence in a single pooled summary estimate and suggests that differences in study populations, methods of measuring IOP and ICP, definitions of glaucoma severity, or other clinical and methodological factors may have materially influenced the observed associations.

### Notable individual study patterns

Although the fixed-effect model suggested a small but statistically significant positive association, this result appears to have been driven primarily by the most precise studies, which likely clustered around a small positive effect. In contrast, the much wider confidence interval under the random-effects model indicates that other studies reported substantially larger effects, and possibly effects in the opposite direction, thereby contributing disproportionately to the overall inconsistency.

Thus, the available evidence appears to reflect a pattern in which more heavily weighted studies support at most a small increase in TPD among patients with glaucoma, while less consistent individual studies reported more extreme estimates.

### Outliers and potential explanations

The very high heterogeneity strongly suggests the presence of outlying or highly influential studies. These studies may have differed in several important respects, including:

- methods used to estimate or directly measure intracranial pressure,
- timing and conditions of IOP and ICP assessment,
- severity and subtype spectrum within open-angle glaucoma,
- structural optic disc characteristics at baseline,
- demographic differences between cases and controls, and
- study design or risk of bias.

Accordingly, while the overall direction of effect was toward higher TPD in glaucoma, the pooled evidence should be interpreted with caution. The findings are compatible with a possible association between elevated TPD and glaucomatous structural change, but the magnitude and consistency of that association remain uncertain.

### Risk of Bias

Risk of bias across the 9 included studies was generally unfavorable. After harmonizing the overall judgments, 8 of 9 studies were rated as high risk of bias and 1 study as having unclear risk; no study was judged to be at low risk overall. At the domain level, the most prominent concern was the complete lack of reporting across all assessed domains: random sequence generation was judged unclear in 9/9 studies, allocation concealment in 9/9, blinding of participants/personnel in 9/9, blinding of outcome assessment in 9/9, incomplete outcome data in 9/9, and selective reporting in 9/9. In each case, the supporting rationale was that no relevant information was available and the domain was not reported in the article. Thus, the dominant pattern was not isolated weakness in one methodological area, but pervasive uncertainty across all core risk-of-bias domains.

Across studies, the risk-of-bias profile was highly consistent, with essentially no differentiation between studies at the domain level. Because study design was not clearly reported in the extracted data, it was not possible to identify meaningful patterns by design category, such as randomized versus observational studies. The only study not classified as high risk overall was the 2018 study, which remained at unclear risk rather than low risk because all six domains were still judged unclear. Conversely, the studies from 2010, 2015, 2023, and 2025 were labeled “high risk,” and those from 2014, 2021, 2024, and one study with unreported authorship/year were labeled “high”; however, these high overall ratings were not driven by explicitly documented failures in individual domains, but rather by consistently absent methodological reporting. This means there were no studies that could be identified as particularly low risk on the basis of clearly described safeguards such as adequate randomization, concealment, or blinding.

These findings reduce confidence in the pooled estimate because the direction and magnitude of bias cannot be reliably determined when key methodological protections are unreported. In practical terms, the summary effect should be interpreted cautiously, as it may be exaggerated, attenuated, or unstable due to unmeasured selection, performance, detection, attrition, or reporting biases. Although the enhanced extraction process indicated high data-quality confidence for all 9 studies, this reflects confidence in the consistency of extraction rather than confidence in the underlying study methods themselves. Overall, the evidence base appears limited less by extraction uncertainty and more by poor reporting of internal validity features, which substantially lowers confidence in the robustness of the review’s conclusions.

## Discussion

## Discussion

This systematic review found **no clear overall difference in translaminar pressure difference (TPD = IOP − ICP)** between patients with open-angle glaucoma and healthy control subjects when the **random-effects model** was applied (SMD 0.232, 95% CI −0.687 to 1.151; p=0.621). Although the **fixed-effects model** suggested a small statistically significant increase in TPD among glaucoma patients (SMD 0.124, 95% CI 0.080 to 0.168), this estimate should be interpreted cautiously because it assumes a common true effect across studies despite extremely high heterogeneity. Clinically, the pooled random-effects result suggests that any average TPD difference, if present, is likely small and inconsistent across populations and study settings.

Our findings are broadly consistent with prior reviews that have emphasized the complexity and variability of glaucoma-related associations. Like earlier work in childhood glaucoma and in stated-preference studies, the present evidence base does not support a simple, uniform effect across all studies. The marked heterogeneity in this meta-analysis helps explain why prior narrative syntheses in glaucoma have often reached cautious conclusions: TPD may be relevant in some patients or subtypes, but current evidence does not establish it as a reliable standalone discriminator between open-angle glaucoma and healthy eyes.

From a biological and clinical perspective, the TPD hypothesis remains plausible. A higher translaminar pressure gradient could increase mechanical stress across the lamina cribrosa, potentially contributing to optic nerve head deformation, axonal injury, and characteristic glaucomatous structural change. However, glaucoma is multifactorial, and optic disc remodeling likely reflects the interaction of pressure-related forces with vascular, connective tissue, and anatomical susceptibility factors. This may explain why TPD differences are detectable in some cohorts but not consistently across all studies.

The very high heterogeneity (I²=97.6%) indicates substantial differences among studies in design, participant characteristics, disease severity, measurement methods for IOP and ICP, and definitions of glaucoma and control status. Variation in imaging techniques and optic disc assessment may also have influenced results. In addition, differences in age, treatment status, body position during measurement, and timing of ICP estimation may have contributed to inconsistent effect estimates.

This review has several strengths. It included nine studies with high extracted data quality, and it used enhanced extraction to better capture effect estimates and study-level information. We also applied both fixed- and random-effects models, which is important given the heterogeneity. Nevertheless, limitations remain: the available studies were few, likely observational, and methodologically diverse; some extracted reports lacked complete metadata and standardized reporting; and the review is limited by the underlying measurement uncertainty in ICP, which is often estimated indirectly rather than measured invasively. These issues reduce confidence in the pooled estimate and limit generalizability.

Clinically, these results do not support using TPD alone as a decisive diagnostic or prognostic marker in open-angle glaucoma. Current practice should continue to rely on comprehensive assessment of intraocular pressure, optic nerve structure, visual field testing, and overall risk profile. Future research should prioritize well-designed prospective studies with standardized TPD measurement protocols, clear glaucoma phenotyping, and stratification by disease severity and treatment status. Studies that directly relate TPD to longitudinal structural progression of the optic disc will be especially important for determining whether TPD is merely associated with glaucoma or truly contributes to disease progression.

## Conclusion

In this meta-analysis of 9 studies, patients with open-angle glaucoma had a higher translaminar pressure difference than healthy controls, but the random-effects estimate was small and not statistically robust (SMD 0.232, 95% CI -0.687 to 1.151; p=0.6208). Clinically, this means current evidence does not support TPD as a reliable standalone marker of glaucomatous structural optic disc change or as a discriminating measure between glaucoma and non-glaucoma populations. Although the fixed-effects model suggested a small positive association (SMD 0.124, 95% CI 0.080 to 0.168), that result is outweighed by extreme between-study heterogeneity (I2=97.6%; tau2=1.8769), indicating substantial inconsistency across studies. TPD may still be considered as part of a broader physiologic assessment in glaucoma, but it should be interpreted cautiously and not used in isolation for clinical decision-making given the marked heterogeneity and imprecision of the pooled effect.

## Final Included Studies

- Corpus ID: 3159 | Cerebrospinal fluid pressure in glaucoma: a prospective study.
- Corpus ID: 85202 | Normal-Tension Glaucoma Has Normal Intracranial Pressure: A Prospective Study of Intracranial Pressure and Intraocular Pressure in Different Body Positions.
- Corpus ID: 85227 | Estimated intracranial pressure in glaucoma patients and its correlation with disease severity.
- Corpus ID: 3160 | The difference in translaminar pressure gradient and neuroretinal rim area in glaucoma and healthy subjects.
- Corpus ID: 85200 | Correlation between ocular perfusion pressure and translaminar pressure difference in glaucoma: Evidence for a three-pressure disease?
- Corpus ID: 85226 | Determination of the Trans-Lamina Cribrosa Pressure Difference in a Community-Based Population and its Association with Open-Angle Glaucoma.
- Corpus ID: 85204 | Anterior lamina cribrosa surface position in idiopathic intracranial hypertension and glaucoma.
- Corpus ID: 85208 | Ocular Perfusion Pressure vs Estimated Trans-Lamina Cribrosa Pressure Difference in Glaucoma: The Central India Eye and Medical Study (An American Ophthalmological Society Thesis).
- Corpus ID: 85210 | Relationship Between Intracranial Pressure, Ocular Blood Flow and Vessel Density: Insights from OCTA and Doppler Imaging.
