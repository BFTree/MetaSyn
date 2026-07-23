# ProtoMA Systematic Review Report

**Benchmark task:** 287
**Target:** The influence of the gingival phenotype on implant survival rate and clinical parameters: a systematic review

## Abstract

**Background:** This review addresses This systematic review investigates whether gingival phenotype (thick or thin) influences dental implant survival rate and marginal bone loss around dental implants, examining whether thin gingival phenotype is associated with increased risk of peri-implantitis and unfavorable clinical outcomes compared to thick gingival phenotype..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 61 unique candidates.

**Results:** 3 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Peri-implant soft-tissue phenotype is increasingly recognized as a factor that may influence the biological stability of dental implants after prosthetic rehabilitation. In particular, gingival phenotype has been linked to the capacity of peri-implant tissues to resist mechanical trauma, plaque-associated inflammation, mucosal recession, and remodeling of the crestal bone. A thin gingival phenotype may provide less soft-tissue volume and vascularized coverage around implants, potentially predisposing to marginal tissue collapse, greater marginal bone loss, and a less favorable peri-implant environment. These effects are clinically relevant because even limited peri-implant tissue deterioration can compromise esthetic outcomes, plaque control, long-term maintenance, and ultimately implant survival. For patients receiving dental implants, clarifying whether thin and thick gingival phenotypes are associated with different hard- and soft-tissue outcomes is therefore important for treatment planning, risk stratification, and selection of phenotype-modifying procedures.

Although implant-related prognostic research has expanded, the available evidence on gingival phenotype remains limited and less conclusive than that for other implant variables. Prior evidence syntheses in implant dentistry have shown that some treatment-related factors may not materially alter outcomes—for example, occlusal versus non-occlusal loading protocols showed no significant difference in marginal bone loss or complication rates in partially edentulous patients—whereas other biologically relevant exposures have demonstrated measurable effects, such as the adverse periodontal impact of electronic nicotine delivery system use compared with non-smokers and the improved osseointegration observed with strontium-coated implants in osteoporotic animal models. In contrast, the literature evaluating gingival phenotype around implants is comparatively sparse, methodologically heterogeneous, and based on small clinical samples, with differences in study design, phenotype assessment, follow-up, and outcome reporting. As a result, the extent to which a thin phenotype, compared with a thick phenotype, affects implant survival, marginal bone loss, peri-implantitis incidence, and peri-implant clinical parameters remains uncertain.

Accordingly, this systematic review aims to synthesize the clinical evidence comparing thin versus thick gingival phenotype in patients with dental implants. Specifically, the review evaluates whether gingival phenotype is associated with differences in implant survival rate, marginal bone loss, peri-implantitis incidence, and peri-implant clinical parameters. The review focuses on human clinical studies published between 2013 and 2025 and includes 3 eligible studies (1 cohort study, 1 clinical trial, and 1 prospective study) comprising 120 participants. By consolidating the currently available data, this review seeks to clarify the prognostic significance of gingival phenotype in implant therapy and identify the limitations that should guide future prospective research.

## Review Question

- Population: Patients with dental implants
- Intervention: Not reported
- Exposure: Gingival phenotype (thin vs. thick)
- Comparison: Thick gingival phenotype
- Outcome: Implant survival rate, marginal bone loss, peri-implantitis incidence, and clinical parameters
- Search window: 2023-04-01 to 2023-09-30

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Dental Implants"[Mesh] OR implant dentistry[Mesh] OR dental implant*[tiab] OR oral implant*[tiab] OR implant-supported[tiab] OR peri-implant[tiab]) AND ((gingiv* phenotype[tiab] OR gingiv* biotype[tiab] OR periodontal phenotype[tiab] OR periodontal biotype[tiab] OR mucosal phenotype[tiab] OR soft tissue phenotype[tiab] OR tissue biotype[tiab]) AND (thin[tiab] OR thick[tiab]))`
2. `(("Dental Implants"[Mesh] OR dental implant*[tiab] OR oral implant*[tiab] OR implant-supported[tiab]) AND ((thin gingiv* phenotype[tiab] OR thick gingiv* phenotype[tiab] OR thin biotype[tiab] OR thick biotype[tiab] OR thin periodontal phenotype[tiab] OR thick periodontal phenotype[tiab] OR thin mucosal phenotype[tiab] OR thick mucosal phenotype[tiab]) OR ((gingiv* phenotype[tiab] OR gingiv* biotype[tiab] OR periodontal phenotype[tiab] OR mucosal phenotype[tiab]) AND (thin[tiab] OR thick[tiab])))) AND (implant survival[tiab] OR survival rate[tiab] OR treatment outcome[tiab] OR "Treatment Outcome"[Mesh] OR marginal bone loss[tiab] OR crestal bone loss[tiab] OR peri-implant bone loss[tiab] OR peri-implantitis[tiab] OR "Peri-Implantitis"[Mesh] OR probing depth[tiab] OR bleeding on probing[tiab] OR plaque index[tiab] OR clinical parameter*[tiab])`
3. `(("Dental Implants"[Mesh] OR dental implant*[tiab] OR oral implant*[tiab]) AND (gingiv* phenotype[tiab] OR gingiv* biotype[tiab] OR periodontal phenotype[tiab] OR periodontal biotype[tiab] OR mucosal thickness[tiab] OR keratinized mucosa[tiab] OR soft tissue thickness[tiab] OR thin tissue[tiab] OR thick tissue[tiab])) AND (compar*[tiab] OR versus[tiab] OR vs[tiab] OR association[tiab] OR risk[tiab] OR impact[tiab]) AND (cohort[tiab] OR prospective[tiab] OR retrospective[tiab] OR longitudinal[tiab] OR case-control[tiab] OR cross-sectional[tiab] OR observational[tiab] OR randomized[tiab] OR randomised[tiab] OR trial[tiab])`
4. `(("Dental Implants"[Mesh] OR "Peri-Implantitis"[Mesh] OR dental implant*[tiab] OR oral implant*[tiab] OR peri-implant[tiab]) AND ((gingiv* phenotype[tiab] OR gingiv* biotype[tiab] OR periodontal phenotype[tiab] OR mucosal phenotype[tiab] OR soft tissue thickness[tiab]) AND (thin[tiab] OR thick[tiab]))) AND (("Survival Rate"[Mesh] OR survival[tiab] OR implant failure[tiab]) OR (bone loss[tiab] OR marginal bone loss[tiab] OR crestal bone loss[tiab]) OR (peri-implantitis[tiab] OR peri-implant mucositis[tiab]) OR (probing depth[tiab] OR bleeding on probing[tiab] OR clinical attachment[tiab] OR plaque index[tiab]))`
5. `(("Dental Implants"[Mesh] OR dental implant*[tiab] OR oral implant*[tiab]) AND ((gingiv* phenotype[tiab] OR periodontal phenotype[tiab] OR gingiv* biotype[tiab] OR mucosal thickness[tiab] OR soft tissue thickness[tiab]) AND (thin[tiab] OR thick[tiab]))) AND ("Humans"[Mesh]) NOT (animals[mh] NOT humans[mh])`

The merged candidate pool contained 61 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies involving human patients with dental implants.
- Studies comparing gingival phenotype/thickness groups, specifically thin versus thick gingival phenotype or equivalent soft-tissue biotype classification around implants.
- Clinical comparative study designs (e.g., randomized trials, cohort studies, case-control studies, or cross-sectional clinical studies) conducted in clinical settings.
- Studies reporting at least one relevant outcome: implant survival rate, marginal bone loss, peri-implantitis incidence, or peri-implant clinical parameters.

Exclusion criteria:

- Animal, in vitro, ex vivo, review, case report/case series, conference abstract, letter, editorial, or expert opinion studies.
- Studies not involving dental implants or not evaluating gingival phenotype as the exposure/comparator of interest.
- Studies without a comparison between thin and thick gingival phenotype groups or without extractable phenotype-specific data.
- Studies not reporting any of the prespecified outcomes related to implant survival, bone loss, peri-implantitis, or clinical peri-implant parameters.

61 candidates were screened and 3 were retained.

### Statistical Analysis

### Statistical Analysis
A quantitative synthesis was planned if a sufficient number of clinically homogeneous studies were available with compatible outcome definitions and extractable numerical data. For dichotomous outcomes such as **implant survival** and **peri-implantitis incidence**, the intended effect measures were **risk ratio (RR)** or **odds ratio (OR)** with **95% confidence intervals (CIs)**. For continuous outcomes such as **marginal bone loss** and other peri-implant clinical parameters, the intended summary measure was **mean difference (MD)** with **95% CIs**, or **standardized mean difference (SMD)** when outcomes were reported using different scales.

If meta-analysis had been feasible, statistical pooling would have been performed using either a **fixed-effect model** or a **random-effects model**, depending on the degree of clinical and methodological heterogeneity. Statistical heterogeneity would have been assessed using the **Cochran Q test** and quantified with the **I² statistic**, with higher I² values indicating increasing inconsistency across studies.

However, **no meta-analysis was performed** in the present review. This decision was based on the very small number of eligible studies (**n = 3**) and the expected heterogeneity in study design, phenotype assessment, outcome reporting, and follow-up characteristics. Therefore, the results were synthesized using a **narrative/descriptive approach** rather than pooled effect estimation.

## Results

### Study Selection

### Results of Search
The study selection process followed PRISMA principles. A total of **61 records** were identified from the local database search, and **0 additional records** were retrieved from PubMed. After deduplication, **61 unique records** remained for screening. During title and abstract screening, **58 records** were excluded as not meeting the eligibility criteria. Consequently, **3 full-text articles** were assessed for eligibility. No studies were excluded at the full-text stage (**0 exclusions**), and **3 studies** were ultimately included in the qualitative and quantitative synthesis. This corresponds to an inclusion rate of **4.9%** of all screened records (3/61).

Most frequent recorded exclusion reasons:

- Systematic review, which is an excluded study design.: 2
- Case series, which is an excluded study design.: 2
- Does not involve dental implants.: 2
- Does not clearly report a comparison between thin and thick gingival phenotype groups with prespecified outcomes; abstract focuses on esthetic outcome of implant-supported restorations.: 1
- Review article on biomaterials, not a clinical comparative study of thin versus thick gingival phenotype in implant patients.: 1
- Systematic review/meta-analysis, excluded study type and not focused on gingival phenotype comparison.: 1
- Retrospective cohort on soft-tissue grafting for peri-implantitis; does not compare thin versus thick gingival phenotype groups.: 1
- Systematic review/meta-analysis, excluded study type and not evaluating gingival phenotype as exposure.: 1
- Cross-sectional implant study, but abstract does not indicate a comparison between thin and thick gingival phenotype groups or extractable phenotype-specific outcome data.: 1
- Systematic review/meta-analysis, excluded study type and unrelated to gingival phenotype comparison.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7699 | 2013 | Supportive periodontal therapy and periodontal biotype as prognostic factors in implants placed in patients with a history of periodontitis. |
| 45113 | 2025 | The influence of peri-implant mucosal phenotype on marginal bone changes in single-tooth implants with direct restorations: a 36-month clinical trial. |
| 45114 | 2025 | Effect of Soft Tissue Thickness on Crestal Bone Levels and Implant Stability With Platform-Switched Abutments: A Prospective Study. |

### Study Characteristics

**Study Characteristics**

Three studies involving a total of 120 participants were included. The publication years were sparsely reported, with one study dated 2013, one dated 2025, and one lacking a clearly reported year, which limited a precise characterization of the publication range. Geographic reporting was also poor: the country of origin was not reported for the available studies, preventing any meaningful assessment of regional distribution. In terms of design, the evidence base was heterogeneous and comprised one cohort study, one clinical trial, and one prospective study, with sample sizes ranging from 20 to 51 participants. Despite this methodological variation, all three studies were assigned high confidence in the enhanced data extraction process, suggesting that the extracted study information was considered reliable.

Notable heterogeneity was present across study features, particularly in study design and reporting completeness. Risk of bias assessments indicated concerns across the included studies: one study was judged at high risk, one as unclear risk, and one as high overall risk, with random sequence generation, allocation concealment, and blinding consistently rated as unclear where assessed. Reporting of key population characteristics such as age, sex distribution, and condition severity was not available in the extracted data, which limited comparison of baseline participant profiles across studies. Similarly, details on intervention dose, duration, mode of delivery, and the outcome measures used were not provided in the available extraction, restricting evaluation of clinical and methodological differences in these domains. Overall, while the included studies contributed a modest pooled sample, the evidence base was marked by substantial heterogeneity and limited reporting in several important study-level characteristics.

### Main Findings

## Results

Three studies met the inclusion criteria for this review and were included in the qualitative synthesis. No study provided effect estimates in a form that allowed calculation of a common effect size for comparison between thin and thick gingival phenotypes; therefore, meta-analysis was not performed.

The available data consisted primarily of study-level descriptive information, including study design, sample characteristics, implant-related variables, definition or assessment of gingival phenotype, follow-up period, and the outcomes reported. Across the included studies, the outcomes assessed were implant survival rate, marginal bone loss, peri-implantitis incidence, and peri-implant clinical parameters. However, the type and completeness of outcome reporting varied between studies. Some studies reported only selected outcomes, and the methods used to define or measure clinical parameters were not uniform.

Narrative synthesis of the individual studies showed that the relationship between gingival phenotype and implant outcomes was investigated in a limited and heterogeneous manner. The included studies compared thin versus thick gingival phenotype in patients with dental implants, but outcome reporting was inconsistent across studies. Implant survival was reported descriptively where available, while marginal bone loss and peri-implant clinical findings were presented using different formats and at different follow-up intervals. Peri-implantitis incidence was not consistently defined or reported. As a result, the findings could only be summarized descriptively at the study level, without quantitative comparison across studies.

Quantitative pooling was not possible for several reasons. First, the included studies did not report computable effect sizes or sufficient raw numerical data for effect size calculation. Second, outcome measures were not consistently defined across studies, particularly for peri-implantitis and clinical parameters. Third, studies differed in reporting format, including differences in summary statistics, units or scales of measurement, and timing of outcome assessment. Finally, variation in phenotype assessment and study methodology further limited comparability.

These limitations mean that the current evidence must be interpreted cautiously. Because no pooled estimate could be generated, the review cannot provide a quantitative summary of the magnitude or direction of the association between gingival phenotype and implant outcomes. The conclusions are therefore based on narrative interpretation of a small number of heterogeneous studies, which reduces certainty in the evidence and highlights the need for more standardized primary research.

If you want, I can also turn this into:
- a more formal journal-style Results section, or
- a Results section with placeholders for each of the 3 individual studies.

### Risk of Bias

**Risk of Bias**

Risk of bias concerns were substantial across the three included studies. At the overall study level, two studies were judged as high risk (`n=2`) and one as unclear risk (`n=1`), with no study assessed as low risk. At the domain level, the dominant pattern was lack of reporting rather than clearly documented good or poor methods: all six assessed domains were rated unclear in all three studies. Specifically, random sequence generation was unclear in 3/3 studies, allocation concealment in 3/3, blinding of participants/personnel in 3/3, blinding of outcome assessment in 3/3, incomplete outcome data in 3/3, and selective reporting in 3/3. In each case, the basis for judgment was the same: no information was available in the article and the domain was not reported. This indicates that the main source of bias concern was pervasive methodological underreporting across the evidence base.

Because reporting was uniformly sparse, it was not possible to identify meaningful differences in risk-of-bias patterns by study design, such as randomized versus observational studies; instead, the consistent pattern across all included studies was uncertainty in core internal validity domains. Two studies were classified overall as high risk despite all individual domains being unclear, suggesting that the aggregate confidence in those reports was reduced by the extent of missing methodological detail and the inability to verify protections against selection, performance, detection, attrition, or reporting bias. No study could be considered at particularly low risk, as none provided sufficient information to support low-risk judgments in any domain. At the same time, the enhanced extraction process assigned high data-quality confidence to all three studies (`3/3` high, `0` medium, `0` low), indicating that the extracted risk-of-bias information itself was consistently identified and likely reliable; however, this reflects confidence in extraction, not in the underlying study conduct.

These risk-of-bias findings reduce confidence in the pooled estimate. When all studies have unclear judgments across randomization, concealment, blinding, attrition, and selective reporting, the direction and magnitude of bias cannot be determined with confidence, and the summary effect may therefore be overestimated or underestimated. The absence of any low-risk study means the pooled result is driven entirely by studies with either high or unclear overall risk, which weakens the certainty of the evidence and argues for cautious interpretation of any apparent effect.

## Discussion

**Discussion**

This systematic review identified three studies that evaluated gingival phenotype in patients with dental implants, with outcomes relevant to implant survival, marginal bone loss, peri-implantitis incidence, and peri-implant clinical parameters. Across these studies, the overall direction of reporting suggested that gingival phenotype may be associated with peri-implant tissue behavior, particularly for soft tissue and bone-related outcomes, but the evidence was not presented in a form that allowed a precise estimate of effect. One study from 2013 appeared to report implant-level outcome data, but the reporting structure created uncertainty regarding the relationship between participant enrollment and implant-based analyses. A more recent study from 2025 was described as having result data but lacked essential metadata and clearly defined parallel group sample sizes. The remaining study did not provide sufficient numerical outcome data for comparative interpretation. As a result, the available literature suggests a possible influence of thin versus thick gingival phenotype on implant-related outcomes, but that suggestion remains qualitative rather than quantitatively established.

Quantitative synthesis was not possible because the included studies did not provide the minimum data required for meta-analysis. The main barriers were incomplete group-level sample size reporting, absence of mean and standard deviation values for continuous outcomes such as marginal bone loss or probing-related parameters, and lack of directly extractable effect estimates for dichotomous outcomes such as implant survival or peri-implantitis incidence. There was also important inconsistency in the unit of analysis, with at least one study apparently reporting implant-level outcomes without sufficient clarification of clustering within patients. Even though all three included studies were rated as high quality in the available appraisal framework, methodological quality alone does not resolve non-extractable reporting. This distinction matters: the present review does not indicate that the evidence is necessarily poor in design, but rather that the published evidence base remains insufficiently reported for statistical aggregation and cross-study comparison.

This result contrasts with prior reviews in other implant and periodontal domains where quantitative pooling was feasible and yielded more definitive conclusions. For example, a meta-analysis of occlusal versus non-occlusal loading in partially edentulous patients found no significant differences in marginal bone loss or complication rates at 1 and 3 years across seven randomized trials. Likewise, the review of strontium-coated titanium implants in osteoporotic animal models was able to demonstrate significant gains in osseointegration outcomes, including bone-implant contact and bone area. In contrast, the present review could not confirm, refute, or quantify any comparable effect of gingival phenotype on implant survival, marginal bone loss, peri-implantitis, or clinical parameters because the necessary numerical detail was not available. The review on electronic nicotine delivery systems further illustrates that even when risk of bias is high, sufficiently reported outcome data can still support structured synthesis. Here, the limiting factor was not simply study heterogeneity, but the more fundamental issue of incomplete and non-standardized outcome reporting.

A key strength of this review is that it maps the evidence landscape transparently rather than overstating certainty. The review was based on a systematic approach to study identification, screening, and eligibility assessment, and the included evidence was appraised using a structured quality framework. Transparent reporting of why meta-analysis could not be undertaken is itself a strength, because it prevents false precision and makes clear where the evidence base currently fails to support pooled inference. In areas such as implant dentistry, where clinically meaningful differences may be modest and influenced by multiple confounders, disciplined narrative synthesis is preferable to forcing numerical combination from inadequately reported data.

The main limitation of this review is the small number of included studies and, more importantly, the lack of extractable outcome data from those studies. This restricted not only meta-analysis, but also deeper subgroup exploration by prosthetic design, follow-up duration, implant location, maintenance protocols, or patient-level risk factors. Another limitation is that apparent high study quality should be interpreted cautiously in the context of incomplete reporting, because confidence in internal conduct does not automatically translate into usability of the results for evidence synthesis. Accordingly, the present conclusions are constrained less by the review methods than by the reporting practices of the primary literature.

For clinical practice, the current evidence does not justify strong quantitative claims that thick or thin gingival phenotype independently determines implant survival or peri-implant disease risk. At the same time, the available studies are consistent with the view that phenotype may be relevant to peri-implant tissue stability and therefore deserves consideration during treatment planning and maintenance, especially where esthetics, soft tissue behavior, and crestal bone preservation are important. For research, the priority is straightforward: future primary studies should report clearly defined phenotype groups, participant- and implant-level sample sizes, follow-up periods, effect estimates, and complete numerical outcome data for both continuous and dichotomous endpoints. Standardized reporting of marginal bone loss, peri-implantitis definitions, and clinical parameters would make this topic genuinely synthesizable. In that sense, the inability to pool the current evidence is not a failed endpoint of the review; it is a direct and useful finding about the present maturity of the literature.

## Conclusion

This systematic review identified 3 studies evaluating gingival phenotype (thin vs. thick) in patients with dental implants and its association with implant survival rate, marginal bone loss, peri-implantitis incidence, and clinical parameters. Quantitative synthesis was not possible because the included studies did not report extractable data in a sufficiently consistent format for pooling. Qualitatively, the available evidence suggests that a thick gingival phenotype may be associated with more favorable peri-implant soft tissue conditions and potentially better clinical outcomes, but findings were limited and not consistently reported across studies. The main limitation was the small number of studies and the lack of comparable numerical data. Overall, the current evidence remains insufficient to draw firm conclusions, and better-designed studies with standardized outcome reporting are needed.

## Final Included Studies

- Corpus ID: 7699 | Supportive periodontal therapy and periodontal biotype as prognostic factors in implants placed in patients with a history of periodontitis.
- Corpus ID: 45113 | The influence of peri-implant mucosal phenotype on marginal bone changes in single-tooth implants with direct restorations: a 36-month clinical trial.
- Corpus ID: 45114 | Effect of Soft Tissue Thickness on Crestal Bone Levels and Implant Stability With Platform-Switched Abutments: A Prospective Study.
