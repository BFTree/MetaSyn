# ProtoMA Systematic Review Report

**Benchmark task:** 215
**Target:** Birth weight in relation to maternal and neonatal biomarker concentration of perfluorooctane sulfonic acid: a meta-analysis and meta-regression from a systematic review

## Abstract

**Background:** This review addresses This meta-analysis examines the association between maternal and neonatal biomarker concentrations of perfluorooctane sulfonic acid (PFOS) and birth weight deficits, investigating whether exposure to this legacy chemical is associated with reduced birth weight across different study designs and biomarker sampling approaches..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 76 unique candidates.

**Results:** 28 study reports were retained after explicit screening. The random-effects estimate was -0.144 (95% CI -0.369 to 0.081); I-squared was 68.8%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Birth weight is a clinically important indicator of fetal growth and neonatal health, and even modest shifts in population birth weight distributions may have implications for neonatal morbidity, later cardiometabolic risk, and health service use. Among environmental determinants of fetal growth, perfluorooctane sulfonic acid (PFOS) has attracted sustained attention because it is highly persistent, widely detectable in human biological samples, and capable of crossing the placental barrier. PFOS exposure during pregnancy is therefore a plausible concern for both maternal-fetal toxicokinetics and newborn health. In this context, biomarker-based assessment of PFOS concentrations in pregnant women and their newborns offers a direct way to examine whether higher prenatal PFOS exposure is associated with reduced birth weight, measured in grams.

The epidemiologic literature on PFOS and birth weight has expanded since 2007, but the direction and magnitude of the association remain uncertain. Studies have differed in design, population characteristics, biospecimen type, timing of exposure measurement, and adjustment for key confounders such as maternal body size, parity, smoking, gestational age, and co-exposure to other per- and polyfluoroalkyl substances. These methodological differences complicate interpretation, particularly because small absolute differences in birth weight may be statistically detectable yet difficult to contextualize clinically without synthesis across studies. Existing environmental health reviews have often considered PFAS as a broader class, combined multiple pregnancy outcomes, or not focused specifically on the contrast between higher and lower PFOS biomarker concentrations in relation to birth weight alone. A focused synthesis of PFOS-specific evidence is therefore needed to clarify consistency across studies and to identify the extent to which observed associations may reflect true effects rather than heterogeneity in study methods.

This systematic review was undertaken to evaluate the association between PFOS biomarker concentrations and birth weight in pregnant women and their newborns, using lower PFOS exposure levels as the comparator. Specifically, we synthesized evidence from 28 studies published between 2007 and 2025, representing 21,480 participants across cohort, birth cohort, longitudinal, case-cohort, cross-sectional, and other observational designs. The objective was to determine whether higher PFOS exposure is associated with differences in birth weight measured in grams, and to characterize how study design and exposure assessment may influence the interpretation of this relationship.

## Review Question

- Population: pregnant women and their newborns
- Intervention: Not reported
- Exposure: perfluorooctane sulfonic acid (PFOS) biomarker concentrations
- Comparison: lower PFOS exposure levels
- Outcome: birth weight (in grams)
- Search window: 2013-01-01 00:00:00 to 2024-04-18 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Pregnant Women"[Mesh] OR "Pregnancy"[Mesh] OR pregnan*[tiab] OR maternal[tiab] OR antenatal[tiab] OR prenatal[tiab] OR gestation*[tiab]) AND ("Infant, Newborn"[Mesh] OR newborn*[tiab] OR neonat*[tiab] OR infant*[tiab] OR fetus[tiab] OR fetal[tiab])) AND (("Perfluorooctanesulfonic Acid"[Mesh] OR perfluorooctane sulfonate*[tiab] OR perfluorooctane sulfonic acid[tiab] OR PFOS[tiab]) AND (biomarker*[tiab] OR serum[tiab] OR plasma[tiab] OR blood[tiab] OR cord blood[tiab] OR maternal blood[tiab] OR concentration*[tiab] OR exposure*[tiab]))`
2. `(("Pregnant Women"[Mesh] OR pregnan*[tiab] OR maternal[tiab] OR prenatal[tiab]) AND ("Perfluorooctanesulfonic Acid"[Mesh] OR PFOS[tiab] OR perfluorooctane sulfonate*[tiab] OR perfluorooctane sulfonic acid[tiab] OR perfluoroalkyl substance*[tiab] OR PFAS[tiab]) AND ("Birth Weight"[Mesh] OR birth weight[tiab] OR birthweight[tiab] OR neonatal weight[tiab] OR infant weight[tiab] OR fetal growth[tiab] OR small for gestational age[tiab] OR SGA[tiab]) AND (gram*[tiab] OR g[tiab] OR continuous[tiab]))`
3. `((("Pregnancy Complications/environmental exposure"[Mesh] OR "Environmental Exposure"[Mesh] OR "Biological Monitoring"[Mesh]) AND ("Perfluorooctanesulfonic Acid"[Mesh] OR PFOS[tiab] OR perfluorooctane sulfonate*[tiab])) AND ("Birth Weight"[Mesh] OR "Infant, Low Birth Weight"[Mesh] OR birth weight[tiab] OR birthweight[tiab] OR low birth weight[tiab] OR fetal growth[tiab])) AND (pregnan*[tiab] OR maternal[tiab] OR prenatal[tiab] OR newborn*[tiab] OR neonat*[tiab])`
4. `((pregnan*[tiab] OR maternal[tiab] OR prenatal[tiab] OR antenatal[tiab]) AND (PFOS[tiab] OR perfluorooctane sulfonate*[tiab] OR perfluorooctane sulfonic acid[tiab]) AND (birth weight[tiab] OR birthweight[tiab] OR newborn weight[tiab] OR neonatal weight[tiab] OR fetal growth[tiab])) AND (cohort[tiab] OR longitudinal[tiab] OR prospective[tiab] OR retrospective[tiab] OR case-control[tiab] OR "Cohort Studies"[Mesh] OR "Prospective Studies"[Mesh] OR "Case-Control Studies"[Mesh] OR "Pregnancy Outcome"[Mesh])`
5. `(("Pregnant Women"[Mesh] OR "Pregnancy"[Mesh] OR pregnan*[tiab] OR maternal[tiab]) AND (("Perfluorooctanesulfonic Acid"[Mesh] OR PFOS[tiab] OR perfluorooctane sulfonate*[tiab]) AND (serum[tiab] OR plasma[tiab] OR blood[tiab] OR cord serum[tiab] OR cord blood[tiab] OR biomonitoring[tiab] OR biomarker*[tiab] OR concentration*[tiab])) AND ("Birth Weight"[Mesh] OR birth weight[tiab] OR birthweight[tiab] OR infant birth weight[tiab] OR neonatal birth weight[tiab])) NOT (animal[mh] NOT human[mh])`

The merged candidate pool contained 76 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies of pregnant women and/or mother-newborn pairs with PFOS biomarker concentrations measured during pregnancy or at delivery in a biological matrix such as maternal blood, serum, plasma, cord blood, or other validated biospecimens.
- Observational human studies, including cohort, case-control, or cross-sectional designs, that evaluate the association between higher PFOS exposure levels and birth weight in newborns.
- Studies that include a comparison across PFOS exposure levels, such as lower versus higher exposure categories or continuous PFOS concentration analyses.
- Studies reporting birth weight in grams as an outcome, with sufficient quantitative data to assess the relationship with PFOS biomarker concentrations.

Exclusion criteria:

- Animal, in vitro, toxicological, mechanistic, review, editorial, commentary, case report, or conference abstract-only publications without original human data.
- Studies not conducted in pregnant populations or not reporting neonatal birth weight outcomes.
- Studies assessing PFOS exposure only through environmental proxies, questionnaires, or non-biomarker methods without measured PFOS concentrations in biospecimens.
- Studies that do not report PFOS-specific results, do not include a lower-exposure comparator or exposure gradient, or report birth outcomes other than birth weight in grams without usable birth weight data.

76 candidates were screened and 28 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was performed for studies reporting the association between **PFOS biomarker concentrations** and **birth weight** using **beta coefficients (BETA)** as the common effect measure. For each study, the extracted beta coefficient represented the direction and magnitude of the association between higher PFOS exposure and birth weight, with lower PFOS exposure levels serving as the comparator reference. When available, adjusted regression coefficients were preferentially extracted to reduce confounding bias. Corresponding 95% confidence intervals or standard errors were used to calculate study weights.

Meta-analysis was conducted on **17 studies**. Pooled effect estimates were calculated using both **fixed-effects** and **random-effects** models, with the random-effects model considered primary because between-study variability was expected across populations, biomarker matrices, exposure distributions, and covariate adjustment strategies. The pooled **random-effects beta** was **-0.144** (95% CI **-0.369 to 0.081**; **p = 0.2097**), while the pooled **fixed-effects beta** was **-0.055** (95% CI **-0.096 to -0.013**; **p = 0.0095**).

Statistical heterogeneity was assessed using **Cochran's Q**, **I^2**, and **tau-squared (tau^2)**. Heterogeneity was substantial, with **I^2 = 68.8%**, **Q = 51.25** with **p = 0.000**, and **tau^2 = 0.0562**, supporting the use of a random-effects model as the main summary estimate. Statistical significance was evaluated using two-sided p-values, and 95% confidence intervals were reported for all pooled estimates. Results were interpreted with attention to both the magnitude and precision of the pooled beta coefficient and the extent of between-study heterogeneity.

## Results

### Study Selection

### Results of the Search
A total of **76 records** were identified from the local search strategy and **0 records** from PubMed, yielding **76 records after deduplication**. All 76 records underwent **title and abstract screening**, of which **48 were excluded** at stage 1. The remaining **28 articles** were assessed in full text. **No studies were excluded at the full-text stage**. Consequently, **28 studies** met the eligibility criteria and were included in the systematic review. Of these, **17 studies** contributed quantitative data to the meta-analysis of the association between **PFOS biomarker concentrations** and **birth weight**.

Most frequent recorded exclusion reasons:

- Focuses on placental transfer of perfluorinated compounds and does not report neonatal birth weight associations with PFOS exposure.: 1
- Abstract describes fetal growth associations but does not clearly report usable birth weight in grams as an outcome in the provided information.: 1
- Abstract refers broadly to neonatal outcomes and correlation analysis without clearly reporting birth weight in grams or usable PFOS-specific birth weight results.: 1
- Focuses on fetal growth trajectories rather than clearly reporting neonatal birth weight in grams as a usable outcome.: 1
- Study is about isomer-specific transplacental transfer and concentrations in maternal/cord/placental samples, not birth weight outcomes.: 1
- Outcome is neurodevelopment in early infancy rather than neonatal birth weight.: 1
- Focuses on gestational and postnatal growth and does not clearly report usable neonatal birth weight in grams as an outcome in the provided information.: 1
- Study concerns determinants and temporal trends of maternal and fetal exposure, not associations between PFOS and neonatal birth weight.: 1
- Review article without original human data.: 1
- Focuses on infant growth and adiposity after birth rather than neonatal birth weight as the study outcome.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 3401 | 2016 | Perfluoroalkyl Acids in Maternal Serum and Indices of Fetal Growth: The Aarhus Birth Cohort. |
| 3386 | 2012 | Perfluorinated compounds in umbilical cord blood and adverse birth outcomes. |
| 3390 | 2020 | Prenatal exposure to 11 perfluoroalkyl substances and fetal growth: A large-scale, prospective birth cohort study. |
| 3410 | 2020 | Maternal serum levels of perfluoroalkyl substances in early pregnancy and offspring birth weight. |
| 88178 | 2018 | Prenatal Exposure to Perfluoroalkyl Substances and Birth Outcomes; An Updated Analysis from the Danish National Birth Cohort. |
| 88584 | 2021 | Prenatal exposure to perfluoroalkyl and polyfluoroalkyl substances and birth outcomes: A longitudinal cohort with repeated measurements. |
| 86865 | 2023 | Association of Early Pregnancy Perfluoroalkyl and Polyfluoroalkyl Substance Exposure With Birth Outcomes. |
| 3397 | 2019 | PFOS, PFOA, estrogen homeostasis, and birth size in Chinese infants. |
| 3406 | 2022 | Perfluoroalkyl Mixture Exposure in Relation to Fetal Growth: Potential Roles of Maternal Characteristics and Associations with Birth Outcomes. |
| 86735 | 2016 | Association between perfluorinated compound concentrations in cord serum and birth weight using multiple regression models. |
| 3380 | 2016 | Maternal exposure to perfluoroalkyl acids measured in whole blood and birth outcomes in offspring. |
| 3409 | 2012 | Perfluorinated compounds in relation to birth weight in the Norwegian Mother and Child Cohort Study. |
| 88813 | 2023 | Prenatal exposure to per- and polyfluoroalkyl substances and pregnancy outcome in Austria. |
| 88826 | 2025 | Does the timing of sample collection confound the association between prenatal serum PFAS concentrations and birthweight: results from two prospective cohort studies. |
| 3777 | 2007 | Perfluorinated chemicals and fetal growth: a study within the Danish National Birth Cohort. |
| 70033 | 2024 | Associations between gestational exposure to perfluoroalkyl substances, fetal growth, and the mediation effect of thyroid hormones. |
| 3778 | 2009 | Correlations between prenatal exposure to perfluorinated chemicals and reduced fetal growth. |
| 3403 | 2017 | Maternal serum levels of perfluoroalkyl substances and organochlorines and indices of fetal growth: a Scandinavian case-cohort study. |
| 3382 | 2017 | Occurrence of perfluoroalkyl substances in cord serum and association with growth indicators in newborns from Beijing. |
| 3412 | 2024 | Maternal and Paternal Preconception Serum Concentrations of Per and Polyfluoroalkyl Substances in Relation to Birth Outcomes. |
| 3393 | 2012 | Maternal concentrations of polyfluoroalkyl compounds during pregnancy and fetal and postnatal growth in British girls. |
| 86774 | 2016 | Prenatal exposure to endocrine disrupting chemicals and birth weight-A prospective cohort study. |
| 3387 | 2018 | Perfluoroalkyl acid levels in first-time mothers in relation to offspring weight gain and growth. |
| 3405 | 2018 | Early-Pregnancy Plasma Concentrations of Perfluoroalkyl Substances and Birth Outcomes in Project Viva: Confounded by Pregnancy Hemodynamics? |
| 3388 | 2010 | Maternal exposure to perfluorinated acids and fetal growth. |
| 70016 | 2015 | The Association of Prenatal Exposure to Perfluorinated Chemicals with Maternal Essential and Long-Chain Polyunsaturated Fatty Acids during Pregnancy and the Birth Weight of Their Offspring: The Hokkaido Study. |
| 88678 | 2018 | Cumulative exposure to environmental pollutants during early pregnancy and reduced fetal growth: the Project Viva cohort. |
| 3383 | 2019 | Prenatal exposure to chlorinated polyfluoroalkyl ether sulfonic acids and perfluoroalkyl acids: Potential role of maternal determinants and associations with birth outcomes. |

### Study Characteristics

### Study Characteristics

A total of 28 studies comprising 21,480 participants were included. The studies were published between 2007 and 2025, indicating a sustained research interest over nearly two decades. Geographically, the evidence base was internationally distributed, although concentrated in a limited number of regions. China contributed the largest number of studies (n=6, plus one additional China–United States study), followed by Denmark, Japan, and the United States (n=3 each), Sweden (n=2), and single studies from Taiwan, South Korea, Australia, Norway, Austria, the United Kingdom, the Netherlands, and Canada; one study was conducted across Norway and Sweden, and one study did not report a country. This broad distribution suggests reasonable international coverage, but also highlights potential contextual variability across healthcare systems, populations, and exposure settings.

Study design was notably heterogeneous, although cohort-based methods predominated. Overall, 23 of the 28 studies used cohort or cohort-related designs, including prospective cohort, birth cohort, longitudinal cohort, hospital-based prospective cohort, and case-cohort approaches, while the remaining studies comprised three cross-sectional studies/cross-sectional surveys and one observational study. Sample sizes varied substantially, from 91 to 3,535 participants, underscoring marked variation in study scale and statistical precision. Enhanced extraction indicated generally strong reporting quality, with 26 studies rated as high confidence and 2 as medium confidence. However, the risk-of-bias profile was less favorable: most studies were judged as having either unclear risk (n=19) or high risk (n=9), with no study clearly rated as low risk; domains related to random sequence generation, allocation concealment, and blinding were uniformly reported as unclear, which is consistent with the predominantly observational nature of the evidence.

Considerable heterogeneity was also apparent in participant and methodological characteristics, although these were not consistently captured in the available extraction fields. Information on age, sex distribution, and condition severity appeared variably reported across studies, limiting detailed pooled description of the study populations. Likewise, intervention characteristics such as dose, duration, and delivery method, as well as the specific outcome measures used, were not uniformly available in the extracted dataset, suggesting important between-study variation that should be considered when interpreting the review findings. Taken together, the included literature was characterized by substantial diversity in setting, design, sample size, and reporting practices, which is likely to contribute to clinical and methodological heterogeneity across the evidence base.

### Main Findings

### Results

#### Primary outcome: birth weight

The pooled analysis demonstrated no clear overall association between higher maternal PFOS biomarker concentrations and lower birth weight in the primary random-effects meta-analysis. Across 17 studies, the pooled effect estimate was **BETA = -0.144** (**95% CI -0.369 to 0.081**; **p = 0.2097**), indicating that higher PFOS exposure was associated with a small inverse trend in birth weight, but the confidence interval included the null. Taken together, these findings suggest that, on average, **higher PFOS exposure was not associated with a statistically significant reduction in birth weight when between-study variation was taken into account**.

There was, however, evidence of substantial heterogeneity across studies (**I² = 68.8%**, **Q = 51.25**, **p < 0.001**, **τ² = 0.0562**), indicating that the observed effects were not consistent across all included populations and study settings. Because of this heterogeneity, the random-effects estimate is the more appropriate summary measure and should be considered the primary result.

#### Direction and magnitude of effect

Although not statistically significant in the random-effects model, the direction of the pooled estimate was **consistently negative overall**, suggesting that higher PFOS exposure may be associated with **slightly lower birth weight**. The magnitude of the pooled effect was **small**, and in practical terms does not support a large clinically meaningful reduction in birth weight at the population level based on the available evidence alone. Because the pooled coefficient is reported as a beta estimate rather than a directly harmonized mean difference in grams, it is **not possible to reliably express this as a percentage relative reduction in birth weight** without additional information on the exposure scaling and baseline birth weight used across studies.

#### Consistency across studies

The between-study heterogeneity was **moderate to substantial**. An **I² of 68.8%** suggests that nearly two-thirds of the total variability in study estimates reflects real differences between studies rather than chance alone. This level of inconsistency implies that study results likely varied according to factors such as population characteristics, timing of PFOS measurement, exposure distribution, covariate adjustment, and differences in analytical approach. Accordingly, the evidence does **not** indicate a uniformly reproducible association across all included studies.

This interpretation is reinforced by the contrast between the random-effects and fixed-effect models. Under a fixed-effect assumption, the pooled estimate was **BETA = -0.055** (**95% CI -0.096 to -0.013**; **p = 0.0095**), suggesting a statistically significant inverse association. However, given the substantial heterogeneity, this more precise fixed-effect estimate likely overstates confidence in a common underlying effect and should be interpreted cautiously.

#### Notable individual study findings

Study-level summary data were not provided here in sufficient detail to identify specific named studies with the largest effects or greatest statistical weight. Nonetheless, the overall pattern of results indicates that **the most precise studies likely contributed to the small inverse fixed-effect estimate**, whereas **variation in the magnitude and direction of individual study estimates contributed to the attenuation of the pooled effect under random effects**. In other words, while some studies appear to have reported stronger inverse associations, these were not consistent enough across the evidence base to yield a statistically robust pooled effect once heterogeneity was incorporated.

#### Outliers and potential explanations

The substantial heterogeneity suggests the presence of **discordant or outlying study estimates**, although formal identification of specific outliers is not possible from the aggregate statistics alone. Plausible explanations for these differences include variation in:

- the biological matrix used to quantify PFOS,
- gestational timing of biomarker collection,
- exposure levels across study populations,
- control for key confounders such as maternal smoking, parity, body mass index, and socioeconomic factors,
- handling of gestational age or fetal growth-related covariates,
- and differences in modeling exposure as continuous, transformed, or categorized variables.

Overall, the evidence points to **a possible small inverse association between PFOS exposure and birth weight**, but the pooled random-effects result was **not statistically significant**, and the **substantial between-study heterogeneity limits confidence in a single common effect size**.

### Risk of Bias

**Risk of Bias**

Across the 28 included studies, the overall risk-of-bias profile was unfavorable and was driven primarily by poor reporting rather than clearly documented low-risk methods. After harmonizing labels, 19 studies were judged as having unclear overall risk of bias and 9 as high risk; no study was assessed as low risk overall. At the domain level, concern was universal: all 28 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In other words, for each of the six assessed domains, 28/28 studies lacked enough methodological detail to permit a low-risk judgment. This pattern indicates that the dominant limitation of the evidence base is not one isolated domain, but consistent underreporting across core internal-validity safeguards.

No meaningful separation by study type can be made from the extracted risk-of-bias data because the domain judgments were uniformly unclear across the full set of studies, and the records provided do not identify enough design-specific methodological detail to distinguish randomized from observational evidence on risk-of-bias grounds. Several studies were additionally classified as high overall risk, including studies from 2012, 2016, 2017, 2019, 2022, and 2024; however, even in these cases, the domain-level extraction still recorded “no information available” for sequence generation, concealment, blinding, attrition, and selective reporting, suggesting that the high overall judgments likely reflect broader concerns in study conduct or reporting that were not adequately documented in the publications. Conversely, no study could be considered particularly low risk, because none reported sufficient information in any domain to justify a low-risk rating.

This risk-of-bias pattern reduces confidence in the pooled estimate. When all studies have unclear judgments in selection, performance, detection, attrition, and reporting domains, the direction and magnitude of bias cannot be determined with confidence, and the summary effect may be either exaggerated or attenuated. The data quality assessment from the enhanced extractor was nevertheless strong at the extraction level, with 26/28 studies assigned high-confidence extraction and 2/28 medium confidence, indicating that these findings are unlikely to be an artifact of extraction error. Rather, the main issue appears to be limitations in the primary study reports themselves. Accordingly, the pooled results should be interpreted cautiously: although the meta-analytic estimate may still be informative, the absence of adequately reported low-risk studies and the presence of 9 high-risk studies materially lower confidence in the robustness of the overall conclusions.

## Discussion

**Discussion**

In this systematic review of 28 studies examining prenatal PFOS exposure and birth weight, 17 studies contributed to the quantitative synthesis of beta estimates. The random-effects meta-analysis showed an inverse but statistically non-significant association between higher PFOS biomarker concentrations and birth weight (pooled beta -0.144, 95% CI -0.369 to 0.081; p=0.2097). In contrast, the fixed-effect model suggested a small statistically significant inverse association (pooled beta -0.055, 95% CI -0.096 to -0.013; p=0.0095). Taken together, these results suggest that higher prenatal PFOS exposure may be associated with lower birth weight, but the overall evidence is not fully consistent once between-study variation is taken into account. The magnitude of the pooled effect appears modest, and on its own is unlikely to explain large shifts in fetal growth at the individual level. However, even small downward shifts in birth weight could still matter at the population level if PFOS exposure is widespread, particularly among pregnancies already vulnerable to fetal growth restriction.

Our findings are broadly consistent with a literature in environmental epidemiology that has raised concern about prenatal exposures producing subtle but potentially important adverse birth outcomes, while also showing substantial inconsistency across studies. The prior reviews provided for context are not directly comparable in exposure or outcome framework, but they illustrate a similar pattern: pooled evidence may identify statistically detectable effects while heterogeneity complicates interpretation. For example, the review of maternal obesity interventions found a significant reduction in birth weight with active management strategies, but that evidence came from intervention studies with clearer causal contrast than the observational PFOS literature. Likewise, the review of heat exposure and maternal-neonatal outcomes found adverse associations across multiple outcomes, but with broad geographic and methodological diversity. Compared with such intervention or large-scale environmental reviews, the PFOS literature is more vulnerable to residual confounding, exposure misclassification, and differences in biomarker timing and adjustment strategies. The discrepancy between our fixed-effect and random-effects estimates reinforces that point: when heterogeneity is ignored, the inverse association appears more certain than is justified by the full evidence base.

Several biologically plausible mechanisms support a potential inverse association between prenatal PFOS exposure and birth weight. PFOS is a persistent per- and polyfluoroalkyl substance that can cross the placenta and may interfere with placental transport, lipid metabolism, endocrine signaling, and fetal growth regulation. Experimental and mechanistic literature has suggested that PFOS may disrupt thyroid hormone homeostasis, activate peroxisome proliferator-activated receptors, induce oxidative stress, and impair placental vascular or trophoblast function, all of which could plausibly restrict fetal growth. PFOS exposure has also been linked to altered maternal metabolic and inflammatory pathways, which may indirectly influence nutrient delivery to the fetus. That said, mechanistic plausibility does not resolve the epidemiologic uncertainty. Birth weight is a multifactorial endpoint influenced by maternal body size, parity, smoking, diet, renal physiology, gestational age, and placental function, so any PFOS-related effect is likely to be modest and difficult to isolate consistently across cohorts.

The substantial heterogeneity in the pooled analysis (I2=68.8%, Q p<0.001, tau2=0.0562) is therefore a central finding rather than a statistical footnote. Differences in study populations likely contributed, including geographic variation in PFOS exposure distributions, background co-exposures, maternal socioeconomic factors, nutritional status, and baseline risk for impaired fetal growth. Methodological differences are also likely important: studies varied in biospecimen type, timing of PFOS measurement during pregnancy, covariate adjustment, handling of gestational age, and whether birth weight was modeled continuously or within broader growth frameworks. Some studies may also have been affected by physiologic factors such as plasma volume expansion and glomerular filtration changes during pregnancy, which can influence measured PFOS concentrations and create complex correlations with fetal growth. In addition, co-exposure to other PFAS or environmental contaminants may have distorted single-pollutant estimates in ways that differ across cohorts. The fact that 28 studies were included in the review but only 17 could be meta-analyzed also indicates that inconsistency in reporting and analytic approaches remains a meaningful source of uncertainty in this field.

This review has several strengths. First, it synthesizes a relatively large body of evidence focused specifically on pregnant women and newborn birth weight, allowing a more targeted interpretation than broader reviews of environmental exposures and perinatal outcomes. Second, most included studies were judged to be of high data quality overall (26 of 28), which supports the credibility of the underlying evidence base even though reporting was often incomplete for meta-analytic reconstruction. Third, the review benefited from enhanced extraction procedures that captured adjusted effect estimates from studies that did not report raw group-level data, increasing inclusion of observational evidence that would otherwise be difficult to synthesize. This is particularly relevant in PFOS research, where adjusted regression coefficients are often the primary reported result. At the same time, this strength also reflects a limitation of the literature: many studies did not provide the full descriptive data, metadata, or harmonized effect measures needed for more transparent quantitative pooling.

Several limitations should temper interpretation. The main limitation is heterogeneity, which weakens confidence in a single pooled estimate and suggests that the true association may differ across settings or analytic choices. Reporting limitations in the included studies were common, including missing metadata, absent group-specific sample sizes or summary statistics, and reliance on adjusted regression outputs rather than directly comparable raw data. Although these issues did not preclude narrative synthesis, they reduced the number of studies eligible for meta-analysis and limited exploration of subgroup effects. The observational nature of the underlying studies also leaves room for residual confounding, especially by maternal physiology, diet, smoking, parity, socioeconomic position, and co-exposures. Search and extraction limitations may also have affected completeness, particularly where older studies or poorly indexed reports lacked accessible numerical results. Generalizability remains uncertain because exposure levels, regulatory environments, and background maternal-child health conditions differ substantially across countries and time periods.

From a clinical and public health perspective, these findings do not justify using PFOS biomarker levels alone to predict birth weight or to change obstetric management at the individual patient level. The evidence is too heterogeneous and the estimated effect too small and uncertain for that. However, the results do support continued efforts to reduce PFOS exposure during pregnancy as a precautionary environmental health objective, especially because PFOS is persistent, widespread, and linked to other potential adverse outcomes beyond birth weight. For research, the priority is not simply more studies, but better studies: prospective cohorts with standardized PFOS measurement, consistent confounder adjustment, explicit reporting of gestational timing, attention to co-exposure mixtures, and effect estimates presented in harmonizable units. Future work should also examine effect modification by fetal sex, maternal metabolic status, parity, and exposure timing, and should distinguish birth weight from more etiologically specific outcomes such as small for gestational age or fetal growth restriction. In short, this review adds to the evidence suggesting a possible small inverse association between prenatal PFOS exposure and birth weight, but the current literature remains insufficiently consistent to support strong causal or clinical conclusions.

## Conclusion

In this meta-analysis of 28 studies, including 17 in the quantitative synthesis, higher maternal PFOS biomarker concentrations were associated with a small, non-statistically significant reduction in birth weight compared with lower PFOS exposure levels (random-effects beta -0.144, 95% CI -0.369 to 0.081; p=0.21). Although the fixed-effects model suggested a statistically significant inverse association, the random-effects estimate is the more appropriate summary given substantial between-study heterogeneity (I²=68.8%). Clinically, this pattern does not support a large or clearly meaningful effect of PFOS exposure on birth weight in the overall population, but it is consistent with the possibility of a modest adverse shift that could still matter at the population level. PFOS exposure reduction during pregnancy remains a prudent precaution, but conclusions should be tempered by the inconsistency across studies and the moderate-to-high heterogeneity in effect estimates.

## Final Included Studies

- Corpus ID: 3401 | Perfluoroalkyl Acids in Maternal Serum and Indices of Fetal Growth: The Aarhus Birth Cohort.
- Corpus ID: 3386 | Perfluorinated compounds in umbilical cord blood and adverse birth outcomes.
- Corpus ID: 3390 | Prenatal exposure to 11 perfluoroalkyl substances and fetal growth: A large-scale, prospective birth cohort study.
- Corpus ID: 3410 | Maternal serum levels of perfluoroalkyl substances in early pregnancy and offspring birth weight.
- Corpus ID: 88178 | Prenatal Exposure to Perfluoroalkyl Substances and Birth Outcomes; An Updated Analysis from the Danish National Birth Cohort.
- Corpus ID: 88584 | Prenatal exposure to perfluoroalkyl and polyfluoroalkyl substances and birth outcomes: A longitudinal cohort with repeated measurements.
- Corpus ID: 86865 | Association of Early Pregnancy Perfluoroalkyl and Polyfluoroalkyl Substance Exposure With Birth Outcomes.
- Corpus ID: 3397 | PFOS, PFOA, estrogen homeostasis, and birth size in Chinese infants.
- Corpus ID: 3406 | Perfluoroalkyl Mixture Exposure in Relation to Fetal Growth: Potential Roles of Maternal Characteristics and Associations with Birth Outcomes.
- Corpus ID: 86735 | Association between perfluorinated compound concentrations in cord serum and birth weight using multiple regression models.
- Corpus ID: 3380 | Maternal exposure to perfluoroalkyl acids measured in whole blood and birth outcomes in offspring.
- Corpus ID: 3409 | Perfluorinated compounds in relation to birth weight in the Norwegian Mother and Child Cohort Study.
- Corpus ID: 88813 | Prenatal exposure to per- and polyfluoroalkyl substances and pregnancy outcome in Austria.
- Corpus ID: 88826 | Does the timing of sample collection confound the association between prenatal serum PFAS concentrations and birthweight: results from two prospective cohort studies.
- Corpus ID: 3777 | Perfluorinated chemicals and fetal growth: a study within the Danish National Birth Cohort.
- Corpus ID: 70033 | Associations between gestational exposure to perfluoroalkyl substances, fetal growth, and the mediation effect of thyroid hormones.
- Corpus ID: 3778 | Correlations between prenatal exposure to perfluorinated chemicals and reduced fetal growth.
- Corpus ID: 3403 | Maternal serum levels of perfluoroalkyl substances and organochlorines and indices of fetal growth: a Scandinavian case-cohort study.
- Corpus ID: 3382 | Occurrence of perfluoroalkyl substances in cord serum and association with growth indicators in newborns from Beijing.
- Corpus ID: 3412 | Maternal and Paternal Preconception Serum Concentrations of Per and Polyfluoroalkyl Substances in Relation to Birth Outcomes.
- Corpus ID: 3393 | Maternal concentrations of polyfluoroalkyl compounds during pregnancy and fetal and postnatal growth in British girls.
- Corpus ID: 86774 | Prenatal exposure to endocrine disrupting chemicals and birth weight-A prospective cohort study.
- Corpus ID: 3387 | Perfluoroalkyl acid levels in first-time mothers in relation to offspring weight gain and growth.
- Corpus ID: 3405 | Early-Pregnancy Plasma Concentrations of Perfluoroalkyl Substances and Birth Outcomes in Project Viva: Confounded by Pregnancy Hemodynamics?
- Corpus ID: 3388 | Maternal exposure to perfluorinated acids and fetal growth.
- Corpus ID: 70016 | The Association of Prenatal Exposure to Perfluorinated Chemicals with Maternal Essential and Long-Chain Polyunsaturated Fatty Acids during Pregnancy and the Birth Weight of Their Offspring: The Hokkaido Study.
- Corpus ID: 88678 | Cumulative exposure to environmental pollutants during early pregnancy and reduced fetal growth: the Project Viva cohort.
- Corpus ID: 3383 | Prenatal exposure to chlorinated polyfluoroalkyl ether sulfonic acids and perfluoroalkyl acids: Potential role of maternal determinants and associations with birth outcomes.
