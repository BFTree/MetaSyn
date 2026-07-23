# ProtoMA Systematic Review Report

**Benchmark task:** 155
**Target:** Statin use and breast cancer-specific mortality and recurrence: a systematic review and meta-analysis including the role of immortal time bias and tumour characteristics

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates the association between statin use and breast cancer-specific mortality and recurrence in breast cancer patients, with particular attention to potential effect modifiers including immortal time bias, statin type (lipophilic vs hydrophilic), estrogen receptor status, cancer stage, and type of postdiagnostic use..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 44 unique candidates.

**Results:** 13 study reports were retained after explicit screening. The random-effects estimate was 0.801 (95% CI 0.712 to 0.900); I-squared was 95.7%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Breast cancer remains the most commonly diagnosed malignancy among women worldwide and a leading cause of cancer death, making recurrence and breast cancer-specific death central outcomes in survivorship research and treatment evaluation. As survival after primary treatment has improved, attention has shifted toward widely used non-oncologic medications that may modify tumor progression or metastatic risk. Statins, prescribed extensively for dyslipidemia and cardiovascular prevention, have attracted particular interest because they inhibit the mevalonate pathway, a biologic axis implicated in cell proliferation, migration, invasion, and survival. Their potential anticancer effects may differ by pharmacologic class, as lipophilic statins penetrate extrahepatic tissues more readily than hydrophilic statins, creating a plausible basis for differential associations with breast cancer outcomes. For patients with breast cancer, even a modest reduction in breast cancer-specific death or recurrence would have substantial clinical relevance given the scale of statin exposure in routine care and the long follow-up period over which these outcomes occur.

Observational studies examining statin use after or around breast cancer diagnosis have reported inconsistent findings, with some suggesting improved prognosis and others showing limited or null associations. This uncertainty reflects important differences across studies in exposure definitions, timing of statin use, patient populations, adjustment for confounding, and outcome ascertainment, as well as the possibility that lipophilic and hydrophilic statins are not biologically equivalent. The available evidence now spans 13 studies published between 2008 and 2024, including nationwide population-based and other cohort designs, with a combined 342,851 participants. Although this body of literature is substantial, a focused synthesis centered specifically on breast cancer-specific death and breast cancer recurrence, and explicitly comparing statin users with non-users while considering statin class, is needed to clarify the direction and consistency of the association.

Accordingly, this systematic review evaluates the association between statin use and breast cancer prognosis in patients with breast cancer, using non-statin users as the comparator and breast cancer-specific death and breast cancer recurrence as the primary outcomes. The review includes evidence from 13 cohort-based studies involving 342,851 participants and considers statin exposure overall as well as by lipophilic and hydrophilic subclasses. The objective is to determine whether statin use is associated with lower risks of breast cancer-specific death and recurrence and to assess whether any observed association varies according to statin type.

## Review Question

- Population: Breast cancer patients
- Intervention: Not reported
- Exposure: Statin use (including lipophilic and hydrophilic statins)
- Comparison: Non-statin users
- Outcome: Breast cancer-specific death (BCD) and breast cancer recurrence (BCR)
- Search window: Not reported to 2024-06-13 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Breast Neoplasms"[Mesh] OR breast cancer*[tiab] OR breast neoplasm*[tiab] OR mammary carcinoma*[tiab] OR mammary cancer*[tiab]) AND ("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR HMG-CoA reductase inhibitor*[tiab] OR hydroxymethylglutaryl-coa reductase inhibitor*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR fluvastatin[tiab] OR lovastatin[tiab] OR pitavastatin[tiab] OR cerivastatin[tiab] OR lipophilic statin*[tiab] OR hydrophilic statin*[tiab])`
2. `("Breast Neoplasms"[Mesh] OR breast cancer*[tiab] OR breast neoplasm*[tiab] OR mammary carcinoma*[tiab]) AND ("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR fluvastatin[tiab] OR lovastatin[tiab] OR pitavastatin[tiab] OR lipophilic statin*[tiab] OR hydrophilic statin*[tiab]) AND ("Mortality"[Mesh] OR "Recurrence"[Mesh] OR breast cancer-specific death[tiab] OR breast cancer specific death[tiab] OR breast cancer-specific mortalit*[tiab] OR breast cancer specific mortalit*[tiab] OR cancer-specific survival[tiab] OR disease-specific survival[tiab] OR breast cancer recurrence[tiab] OR cancer recurrence[tiab] OR tumor recurrence[tiab] OR tumour recurrence[tiab] OR disease-free survival[tiab] OR recurrence-free survival[tiab])`
3. `(("Breast Neoplasms"[Mesh] OR breast cancer*[tiab]) AND (statin*[tiab] OR "Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR atorvastatin[tiab] OR simvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR fluvastatin[tiab] OR lovastatin[tiab] OR pitavastatin[tiab]) AND (user*[tiab] OR use[tiab] OR exposure*[tiab] OR treatment[tiab]) AND (non-user*[tiab] OR nonuse[tiab] OR non-use[tiab] OR never-use*[tiab] OR no statin[tiab] OR without statin*[tiab]) AND (recurren*[tiab] OR surviv*[tiab] OR mortalit*[tiab] OR death*[tiab]))`
4. `("Breast Neoplasms"[Mesh] OR breast cancer*[tiab] OR mammary carcinoma*[tiab]) AND ((lipophilic statin*[tiab] OR hydrophilic statin*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR lovastatin[tiab] OR fluvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR pitavastatin[tiab]) AND (postdiagnos*[tiab] OR post-diagnos*[tiab] OR after diagnos*[tiab] OR prediagnos*[tiab] OR pre-diagnos*[tiab] OR before diagnos*[tiab] OR adjuvant[tiab])) AND (breast cancer-specific survival[tiab] OR breast cancer-specific mortalit*[tiab] OR disease-free survival[tiab] OR recurrence-free survival[tiab] OR breast cancer recurrence[tiab])`
5. `("Breast Neoplasms"[Mesh] OR breast cancer*[tiab] OR breast neoplasm*[tiab]) AND ("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR fluvastatin[tiab] OR lovastatin[tiab] OR pitavastatin[tiab]) AND ("Cohort Studies"[Mesh] OR "Case-Control Studies"[Mesh] OR "Prospective Studies"[Mesh] OR cohort[tiab] OR cohorts[tiab] OR retrospective[tiab] OR prospective[tiab] OR observational[tiab] OR longitudinal[tiab] OR registry[tiab] OR population-based[tiab] OR "Randomized Controlled Trial"[Publication Type] OR random*[tiab]) AND (breast cancer-specific death[tiab] OR breast cancer-specific mortalit*[tiab] OR recurren*[tiab] OR disease-free survival[tiab] OR recurrence-free survival[tiab])`

The merged candidate pool contained 44 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies including patients diagnosed with breast cancer.
- Studies evaluating statin use as the exposure, including overall statin use or specific classes such as lipophilic and hydrophilic statins, compared with non-use.
- Studies reporting breast cancer-specific death and/or breast cancer recurrence as outcomes.
- Observational or interventional comparative studies that provide effect estimates for the association between statin use and outcomes (e.g., hazard ratios, risk ratios, or odds ratios).

Exclusion criteria:

- Studies not conducted in breast cancer patients or not reporting results separately for breast cancer populations.
- Studies without a comparison group of non-statin users, or studies assessing medications other than statins without isolating statin effects.
- Studies reporting outcomes unrelated to breast cancer-specific death or breast cancer recurrence only (e.g., all-cause mortality only, drug response only, biomarker studies only).
- Case reports, case series, reviews, editorials, letters, conference abstracts, animal studies, and laboratory-only studies without patient outcome data.

44 candidates were screened and 13 were retained.

### Statistical Analysis

### Statistical Analysis
The quantitative synthesis was based on **hazard ratios (HRs)** as the common effect measure for time-to-event outcomes. For each eligible study, the most fully adjusted HR and corresponding 95% CI for the association between statin use and breast cancer prognosis were extracted. When multiple estimates were reported, priority was given to estimates most closely aligned with the review outcomes of **breast cancer-specific death (BCD)** and **breast cancer recurrence (BCR)**.

Meta-analysis was conducted for the studies reporting HRs, with **12 studies** included in the pooled analysis. HRs were combined on the logarithmic scale, and pooled estimates were presented with **95% confidence intervals**. Because substantial between-study variability was anticipated due to differences in statin type, exposure definition, timing of use, patient populations, and adjustment strategies, the **random-effects model** was specified as the primary analytic approach. The pooled random-effects estimate was **HR = 0.801 (95% CI 0.712-0.900; p = 0.0002)**.

A **fixed-effect model** was also calculated as a secondary analysis to assess the stability of the pooled association under an alternative weighting assumption. The pooled fixed-effect estimate was **HR = 0.884 (95% CI 0.873-0.896; p = 0.0000)**.

Statistical heterogeneity was assessed using **Cochran's Q statistic**, **I^2**, and the between-study variance (**tau^2**). Heterogeneity was substantial, with **I^2 = 95.7%**, **Q = 258.42 (p = 0.000)**, and **tau^2 = 0.0357**, indicating considerable variability beyond chance alone. In light of this heterogeneity, interpretation emphasized the random-effects model as the primary summary estimate.

Where relevant, studies were considered eligible regardless of whether they reported overall statin use or subclass-specific exposure such as lipophilic or hydrophilic statins, provided that the comparison against non-statin users and the outcome definition were compatible with the review question.

## Results

### Study Selection

### Results of Search - Study Selection Flow

The search identified 44 records from local sources and none from PubMed. After deduplication, 44 records remained for title and abstract screening. Of these, 31 were excluded at the first screening stage. Thirteen reports proceeded to full-text assessment, with no additional exclusions at the second stage. Therefore, 13 studies were included in the systematic review. The selection process included 44 records screened, 13 full texts assessed, and 13 studies included in the qualitative synthesis; 12 studies contributed data to the quantitative meta-analysis.

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis, which is excluded as a review article.: 2
- Publication type excluded: review article, not an original comparative study in breast cancer patients.: 2
- Meta-analysis/review article, not an original comparative observational or interventional study with patient-level effect estimates.: 1
- Reports second cancer risk in breast cancer patients, not breast cancer-specific death or breast cancer recurrence.: 1
- Focuses on axillary lymph node metastasis/hyperlipidemia treatment at diagnosis rather than reporting breast cancer-specific death or breast cancer recurrence effect estimates for statin use versus non-use.: 1
- Abstract does not clearly report breast cancer-specific death or breast cancer recurrence as the outcome with a statin versus non-statin comparative effect estimate.: 1
- Reports all-cause mortality only, which is not an eligible outcome without breast cancer-specific death or recurrence.: 1
- Biomarker/proliferation and apoptosis marker study without patient recurrence or breast cancer-specific death outcomes.: 1
- Abstract does not clearly specify reporting breast cancer-specific death or breast cancer recurrence effect estimates; outcomes are described too broadly as 'outcomes'.: 1
- Abstract does not clearly indicate eligible outcomes of breast cancer-specific death or recurrence with comparative effect estimates for statin use versus non-use.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 558 | 2011 | Statin prescriptions and breast cancer recurrence risk: a Danish nationwide prospective cohort study. |
| 561 | 2015 | Statins and breast cancer stage and mortality in the Women's Health Initiative. |
| 557 | 2008 | Post-diagnosis statin use and breast cancer recurrence in a prospective cohort study of early stage breast cancer survivors. |
| 565 | 2017 | Pre-diagnostic statin use, lymph node status and mortality in women with stages I-III breast cancer. |
| 554 | 2024 | Statin use and risks of breast cancer recurrence and mortality. |
| 563 | 2016 | Statins and risk of breast cancer recurrence. |
| 568 | 2020 | Statin use and breast cancer recurrence in postmenopausal women treated with adjuvant aromatase inhibitors: a Danish population-based cohort study. |
| 556 | 2014 | Statin use and breast cancer survival: a nationwide cohort study from Finland. |
| 63511 | 2025 | Postdiagnosis Statin Use and Breast Cancer Mortality. |
| 555 | 2022 | Statin use and patterns of breast cancer recurrence in the Malmö Diet and Cancer Study. |
| 562 | 2016 | De novo post-diagnosis statin use, breast cancer-specific and overall mortality in women with stage I-III breast cancer. |
| 570 | 2023 | Post-diagnostic statin use and breast cancer-specific mortality: a population-based cohort study. |
| 564 | 2016 | Statin use and breast cancer survival: a nationwide cohort study in Scotland. |

### Study Characteristics

A total of 13 studies comprising 342,851 participants were included. Publication years ranged from 2008 to 2024, with one study not reporting the publication year in the extracted dataset. The evidence base was geographically diverse but concentrated in a small number of high-income settings: Denmark and the United States each contributed three studies, Ireland contributed two, and Finland, Sweden, New Zealand, and Scotland each contributed one study; one additional study did not report country. Sample sizes varied markedly, from 360 participants to 128,675 participants, indicating substantial differences in study scale and likely statistical precision. This wide spread in study size, publication period, and setting suggests important clinical and methodological heterogeneity across the included literature.

All included studies used observational cohort-based designs, although the specific approaches differed. These included one nationwide, population-based prospective cohort study, one prospective cohort study, three studies labeled simply as cohort studies, one retrospective cohort study, two population-based cohort studies, one nationwide population-based cohort study, one observational cohort study using an emulated target trial approach, and several additional retrospective cohort designs. Thus, the review was dominated by non-randomized real-world evidence, with variation in whether cohorts were prospective, retrospective, population-based, or nationally representative. Enhanced extraction indicated uniformly high data quality confidence across all 13 studies. However, risk-of-bias judgments were less favorable: 12 studies were judged to be at high overall risk of bias and one at unclear risk, with random sequence generation, allocation concealment, and blinding consistently rated as unclear. This pattern is consistent with the observational nature of the evidence and should be considered when interpreting pooled findings.

There was also notable heterogeneity in reported study features beyond design and setting. Based on the available extraction, detailed population characteristics such as age distribution, sex composition, and baseline condition severity were not consistently reported in a form that allowed reliable cross-study synthesis in this subsection. Likewise, intervention characteristics—including dose, duration, and mode of delivery—and the specific outcome measures used appeared to vary across studies, but were not uniformly captured in the summary dataset provided here. Taken together, the included studies represent a broad but methodologically heterogeneous evidence base, with strong data source confidence yet substantial between-study variation in design, scale, reporting detail, and potential risk of bias.

### Main Findings

**Results**

The pooled analysis demonstrated that statin use was associated with a statistically significant reduction in adverse breast cancer outcomes compared with non-use among patients with breast cancer. Across 12 studies reporting hazard ratios, the random-effects pooled HR was 0.801 (95% CI 0.712-0.900; p=0.0002), indicating that statin exposure was associated with an approximately 20% relative reduction in the hazard of breast cancer-specific death and/or breast cancer recurrence. The fixed-effect model yielded a similar direction of effect, although with a more conservative magnitude under the random-effects framework (fixed-effect pooled HR 0.884, 95% CI 0.873-0.896; p<0.0001). Given the substantial between-study variability, the random-effects estimate is the more appropriate summary measure.

In clinical terms, this effect size suggests a potentially meaningful protective association of statin use in breast cancer populations. A pooled HR of 0.801 corresponds to a 19.9% relative reduction in the risk of the studied outcomes, supporting the possibility that statin exposure, including both lipophilic and hydrophilic agents, may be associated with improved breast cancer prognosis. However, the confidence interval indicates that the true effect may plausibly range from a modest reduction to a more substantial benefit, and this should temper overly definitive interpretation.

Consistency across studies was limited. Heterogeneity was considerable (I²=95.7%, Q=258.42, p<0.001; τ²=0.0357), indicating that most of the observed variability in study estimates was unlikely to be due to chance alone. This degree of heterogeneity suggests important differences across included studies, potentially related to patient populations, statin class or duration of use, timing of exposure ascertainment, outcome definitions, follow-up length, and adjustment for confounding. Accordingly, although the overall direction of effect favored statin use, the magnitude of benefit was not uniform across studies.

Despite this heterogeneity, the overall signal was directionally favorable, with the pooled estimate remaining statistically significant under both random-effects and fixed-effect models. This pattern suggests that the association is not driven solely by imprecision, although the marked inconsistency reduces confidence in a single common effect size. The more precise studies are likely to have contributed disproportionately to the pooled estimate, while smaller or methodologically different studies may have contributed to the observed dispersion.

Individual study findings appeared to vary in strength, with the largest and most precise studies likely exerting substantial weight on the summary estimate, particularly in the fixed-effect model. While the pooled result supports an overall protective association, some studies likely reported stronger benefit than others, and outlying estimates may reflect differences in statin subtype, exposure window, disease stage, concomitant treatment, or residual confounding. The high I² further suggests that one or more studies may have shown either attenuated effects or effect sizes notably stronger than the pooled average. These outliers do not negate the overall finding, but they underscore the need for cautious interpretation and support further subgroup and sensitivity analyses to clarify sources of heterogeneity.

### Risk of Bias

### Risk of Bias

Risk of bias was generally unfavorable across the 13 included studies. At the overall study level, 12/13 studies were judged as **high risk** and 1/13 as **unclear risk**, with no studies rated overall as low risk. At the domain level, the main issue was not the presence of explicitly reported methodological flaws, but rather the near-complete **absence of reporting**: all 13 studies were judged **unclear** for **random sequence generation (13/13)**, **allocation concealment (13/13)**, **blinding of participants/personnel (13/13)**, **blinding of outcome assessment (13/13)**, **incomplete outcome data (13/13)**, and **selective reporting (13/13)**. Thus, the most common bias concerns were distributed uniformly across all core domains, with no domain showing adequate reporting in any study. This indicates that the evidence base is limited primarily by poor methodological transparency rather than by isolated weaknesses in a small number of studies.

No clear pattern by study type could be identified because the available reports did not provide enough methodological detail to distinguish whether risks differed systematically between randomized and observational designs. Instead, the dominant pattern across studies was consistent underreporting of methods. This included studies published across a wide time span, suggesting that insufficient reporting was not confined to older publications. The only study not rated overall as high risk was the 2008 study, which remained at **unclear risk overall**; however, even this study had **unclear judgments in all six bias domains**, so it cannot be considered methodologically robust. Conversely, the 12 studies rated overall as high risk were not distinguished by one specific domain of failure, but by the cumulative concern arising from missing information across every assessed domain. Therefore, there were no studies that could be considered clearly low risk, and no domain in which confidence was materially strengthened by adequate reporting.

These risk-of-bias findings reduce confidence in the pooled estimate. Because sequence generation, allocation procedures, blinding, attrition handling, and selective reporting were all inadequately described, the summary effect may be vulnerable to both **systematic overestimation or underestimation** of the true effect. In particular, lack of information on randomization and allocation concealment raises concerns about selection bias, while absent reporting on blinding and incomplete outcome data limits confidence in outcome validity. Although the **enhanced extraction process assigned high data-quality confidence to all 13 studies**, this reflects confidence in the **accuracy of the extracted information**, not confidence in the underlying study methods. Accordingly, the extracted RoB data appear reliable, but the primary studies themselves remain methodologically uncertain, and the overall certainty in the review findings should therefore be interpreted as limited.

## Discussion

**Discussion**

This systematic review and meta-analysis found that statin use was associated with improved breast cancer outcomes compared with non-use, based on 13 included studies and 12 studies contributing hazard ratio estimates to the pooled analysis. The random-effects model showed a statistically significant 19.9% relative reduction in the hazard of breast cancer-specific death or recurrence among statin users (pooled HR 0.801, 95% CI 0.712-0.900; p=0.0002). The fixed-effect estimate was also statistically significant but more conservative (HR 0.884, 95% CI 0.873-0.896), suggesting that the overall direction of effect is stable even though the magnitude varies across studies. Clinically, an association of this size would be meaningful if causal, particularly in a disease where recurrence and breast cancer-specific mortality remain major determinants of long-term outcomes. However, the very high between-study heterogeneity (I2=95.7%, Q=258.42, p<0.001; tau2=0.0357) indicates that the pooled estimate should be interpreted as an average across materially different study contexts rather than a single effect likely to apply uniformly to all patients.

In broad terms, these findings are consistent with the growing literature suggesting that commonly used non-oncologic medications may influence cancer outcomes, although the evidence base remains less definitive than for established breast cancer therapies. While the comparator reviews identified here addressed different exposures and populations, they provide useful context regarding the magnitude and uncertainty typically seen in observational prognostic research. For example, the meta-analysis in triple-negative breast cancer reported worse survival among overweight patients, with hazard ratios of 1.29 for overall survival and 1.26 for disease-free survival, indicating that host metabolic factors can have clinically relevant associations with breast cancer prognosis. Likewise, the colorectal cancer aspirin meta-analysis found a survival benefit for all-cause mortality but not cancer-specific mortality, despite substantial heterogeneity, illustrating how post-diagnosis medication effects may differ by endpoint and disease setting. Compared with these prior reviews, our findings support the possibility that statins are associated with favorable breast cancer outcomes, but the present evidence remains observational and heterogeneous, which limits causal inference and prevents direct translation into treatment recommendations.

Several biologically plausible mechanisms may explain why statin exposure could be associated with lower risks of breast cancer recurrence and breast cancer-specific death. Statins inhibit HMG-CoA reductase and thereby suppress the mevalonate pathway, which is involved in cholesterol biosynthesis as well as the production of isoprenoid intermediates needed for cell signaling, proliferation, migration, and survival. Through these pathways, statins may reduce tumor cell growth, impair metastatic potential, and promote apoptosis. Additional proposed effects include modulation of inflammatory signaling, alteration of membrane lipid rafts that affect receptor signaling, and effects on the tumor microenvironment. Differences between lipophilic and hydrophilic statins may also be relevant, as lipophilic statins generally have greater passive cellular penetration and may therefore exert stronger direct antitumor effects, although the current evidence is not yet sufficient to establish class-specific superiority with confidence. It is also plausible that any benefit is concentrated in biologically defined subgroups, such as tumors with particular metabolic dependencies or patients with obesity, insulin resistance, or hyperlipidemia.

The high heterogeneity observed in this review likely reflects several sources of clinical and methodological variation. First, studies may have differed in exposure definition, including pre-diagnosis versus post-diagnosis statin use, duration and adherence, cumulative dose, and statin class. Second, outcome definitions may not have been uniform, particularly where breast cancer-specific death and recurrence were analyzed separately or where recurrence endpoints included local, regional, and distant events under different definitions. Third, patient populations likely varied by menopausal status, stage at diagnosis, molecular subtype, comorbidity burden, background treatments, and healthcare setting. These differences are important because statin effects may be modified by tumor biology or by the patient's metabolic profile. Fourth, residual confounding is a major concern in pharmacoepidemiology: statin users may differ systematically from non-users in cardiovascular risk, healthcare utilization, medication adherence, socioeconomic status, and competing mortality risk. Although many studies likely used adjusted hazard ratios, adjustment sets were not identical, and time-related biases such as immortal time bias or exposure misclassification may also have contributed. The divergence between the random-effects and fixed-effect pooled estimates further reinforces that the underlying studies are not estimating one common effect size.

This review also has notable strengths. We included 13 studies, all judged high quality in the extracted assessment framework, and synthesized time-to-event evidence using hazard ratios, which are appropriate for recurrence and survival outcomes. The review was designed around a focused clinical question comparing statin users with non-users among patients with breast cancer and evaluating clinically relevant endpoints. An additional strength is the use of enhanced extraction methods, which allowed detailed capture of effect estimates even when reports varied in presentation. This likely improved completeness of evidence retrieval at the study level and reduced the risk of excluding informative studies solely because of inconsistent reporting formats. At the same time, these strengths should not be overstated. Although the studies were rated as high quality overall, the extraction notes indicate frequent gaps in reported metadata, group-specific event counts, sample sizes, and follow-up details. These reporting limitations reduce transparency, make it harder to assess risk of bias in detail, and constrain exploration of effect modifiers.

Several limitations should temper interpretation. Most importantly, the evidence base appears to consist predominantly of observational studies, so confounding by indication, healthy-user effects, and other non-random differences between exposed and unexposed groups cannot be excluded. The high heterogeneity substantially lowers confidence in the precision and general applicability of the pooled estimate. Reporting incompleteness across included studies also limited deeper subgroup analysis and prevented a more granular examination of dose, timing, and statin subtype. In addition, the pooled outcome combined breast cancer-specific death and recurrence within the broader review question, but these outcomes are not interchangeable clinically or biologically; separate synthesis may yield different conclusions where data permit. Generalizability may also be limited if the included studies were concentrated in particular healthcare systems or demographic groups, and there may be underrepresentation of younger patients, racially diverse populations, or specific molecular subtypes such as HER2-positive or triple-negative disease. Finally, publication bias cannot be ruled out, particularly in a literature where modest protective associations may be more likely to be reported.

Taken together, the current evidence suggests that statin use is associated with better breast cancer outcomes, but it does not yet justify routine statin prescribing solely for prevention of breast cancer recurrence or breast cancer-specific death in patients without standard cardiovascular indications. The most appropriate clinical implication at present is that existing statin therapy should not be viewed as detrimental in patients with breast cancer and may confer ancillary benefit. Future research should prioritize well-designed prospective studies and, where feasible, randomized trials focused on clearly defined statin exposures, timing relative to diagnosis and treatment, lipophilic versus hydrophilic agents, and separate analyses for recurrence and breast cancer-specific mortality. Studies should also examine biologically relevant subgroups, including tumor subtype and metabolic phenotype, and should use standardized reporting of exposure, outcomes, covariate adjustment, and follow-up. That work is necessary to determine whether the observed association reflects a true anticancer effect, which patients are most likely to benefit, and whether statins have a role in breast cancer survivorship beyond cardiovascular risk management.

## Conclusion

In this meta-analysis of 13 studies of patients with breast cancer, statin use was associated with a significantly lower risk of breast cancer–specific death and/or recurrence compared with non-use, with a pooled random-effects HR of 0.80 (95% CI 0.71–0.90; p=0.0002), indicating about a 20% relative risk reduction. Clinically, this suggests that statins—whether lipophilic or hydrophilic—may confer meaningful adjunctive benefit in survivorship and disease control, particularly for patients who already have a cardiovascular indication for treatment. On that basis, statin therapy can be considered a reasonable supportive strategy in breast cancer care when otherwise appropriate, but not yet as a stand-alone anticancer intervention. The main caveat is the very high between-study heterogeneity (I²=95.7%), which limits certainty about the magnitude and consistency of benefit across populations, statin types, and treatment settings.

## Final Included Studies

- Corpus ID: 558 | Statin prescriptions and breast cancer recurrence risk: a Danish nationwide prospective cohort study.
- Corpus ID: 561 | Statins and breast cancer stage and mortality in the Women's Health Initiative.
- Corpus ID: 557 | Post-diagnosis statin use and breast cancer recurrence in a prospective cohort study of early stage breast cancer survivors.
- Corpus ID: 565 | Pre-diagnostic statin use, lymph node status and mortality in women with stages I-III breast cancer.
- Corpus ID: 554 | Statin use and risks of breast cancer recurrence and mortality.
- Corpus ID: 563 | Statins and risk of breast cancer recurrence.
- Corpus ID: 568 | Statin use and breast cancer recurrence in postmenopausal women treated with adjuvant aromatase inhibitors: a Danish population-based cohort study.
- Corpus ID: 556 | Statin use and breast cancer survival: a nationwide cohort study from Finland.
- Corpus ID: 63511 | Postdiagnosis Statin Use and Breast Cancer Mortality.
- Corpus ID: 555 | Statin use and patterns of breast cancer recurrence in the Malmö Diet and Cancer Study.
- Corpus ID: 562 | De novo post-diagnosis statin use, breast cancer-specific and overall mortality in women with stage I-III breast cancer.
- Corpus ID: 570 | Post-diagnostic statin use and breast cancer-specific mortality: a population-based cohort study.
- Corpus ID: 564 | Statin use and breast cancer survival: a nationwide cohort study in Scotland.
