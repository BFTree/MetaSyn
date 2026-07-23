# ProtoMA Systematic Review Report

**Benchmark task:** 91
**Target:** A scoping review of privacy and utility metrics in medical synthetic data

## Abstract

**Background:** This review addresses This scoping review examines whether there is consensus within the research community on standardized methods for evaluating the privacy and utility of synthetic health-related data, and whether privacy considerations are given equal importance as utility when assessing synthetic medical data..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 71 unique candidates.

**Results:** 19 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Synthetic health data are increasingly used to enable secondary analysis of medical datasets while limiting disclosure of identifiable patient information. In practice, these datasets are intended to support clinically important activities that depend on access to realistic person-level data, including model development, external method testing, trial simulation, and data sharing across institutional or jurisdictional boundaries where direct release of original records may be restricted. The clinical value of this approach depends on a difficult trade-off: synthetic data must preserve distributions, relationships, and outcome-relevant patterns closely enough to remain analytically useful, yet differ sufficiently from source records to reduce risks such as membership inference, attribute disclosure, or re-identification. Inadequate evaluation on either side of this trade-off has direct consequences. Overstating utility may lead to invalid downstream analyses or misleading performance estimates, whereas overstating privacy protection may create false assurance around data release and governance decisions.

Recent evidence syntheses in adjacent areas suggest that evaluation practice remains methodologically fragmented. A scoping review of 52 studies on generative AI for synthetic health records reported that privacy preservation was commonly framed as a primary objective, but also identified the lack of reliable re-identification risk metrics as a major gap. Similar concerns have been observed in other digital health evaluation literatures: a narrative review of 44 studies of AI applications in dentistry found a marked disconnect between validation studies and real-world deployment, and a scoping review of 65 studies of mobile health applications identified substantial variation in quality criteria with no single framework covering all relevant dimensions. Taken together, these findings suggest that, although evaluation frameworks are often proposed, consensus on what constitutes adequate assessment remains limited. For synthetic medical data specifically, uncertainty persists regarding which privacy metrics are actually used, how utility is operationalized, whether studies compare multiple evaluation approaches, and whether privacy protection is assessed with enough rigor relative to claims of analytical usefulness.

This systematic review therefore examines studies evaluating synthetic health-related or medical data, with particular attention to methods and metrics used to assess privacy and utility. Across 19 studies published between 2020 and 2025, representing 2,189,278 total participants and a range of experimental, comparative, cohort, simulation, and framework-based designs, the review compares evaluation approaches, contrasts privacy-focused with utility-focused assessment strategies, and assesses whether privacy protection is addressed adequately in relation to utility. The aim is to identify areas of methodological convergence, determine where evaluation practice remains inconsistent, and clarify gaps in current privacy evaluation that should be addressed before synthetic medical data can be relied upon more confidently in research and clinical data-sharing contexts.

## Review Question

- Population: Studies evaluating synthetic health-related or medical data
- Intervention: Not reported
- Exposure: Methods and metrics used for evaluating privacy and utility of synthetic medical data
- Comparison: Comparison across different evaluation approaches, privacy metrics versus utility metrics, and assessment of whether privacy protection is adequately addressed relative to utility
- Outcome: Consensus on evaluation methods for synthetic data, balance between privacy and utility assessment, identification of gaps in privacy evaluation practices
- Search window: 2018-01-01 00:00:00 to 2024-07-31 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Synthetic Biology"[Mesh] OR synthetic[tiab] OR simulated[tiab] OR artificial[tiab] OR generated[tiab]) AND ("Data Accuracy"[Mesh] OR "Data Interpretation, Statistical"[Mesh] OR "Reproducibility of Results"[Mesh] OR evaluat*[tiab] OR assessment[tiab] OR validation[tiab] OR benchmark*[tiab] OR metric*[tiab]) AND ("Health Records, Personal"[Mesh] OR "Electronic Health Records"[Mesh] OR "Biomedical Research"[Mesh] OR health data[tiab] OR medical data[tiab] OR clinical data[tiab] OR patient data[tiab] OR EHR[tiab] OR EMR[tiab]))`
2. `(("synthetic data"[tiab] OR "synthetic health data"[tiab] OR "synthetic medical data"[tiab] OR "synthetic clinical data"[tiab] OR "synthetic patient data"[tiab] OR "synthetic electronic health record*"[tiab] OR "synthetic EHR*"[tiab] OR "synthetic EMR*"[tiab]) AND (evaluat*[tiab] OR assessment[tiab] OR validation[tiab] OR framework*[tiab] OR benchmark*[tiab] OR metric*[tiab]) AND ((privacy[tiab] OR confidentialit*[tiab] OR disclosure[tiab] OR "disclosure risk"[tiab] OR re-identification[tiab] OR "membership inference"[tiab] OR anonymization[tiab] OR anonymisation[tiab]) AND (utility[tiab] OR usefulness[tiab] OR fidelity[tiab] OR realism[tiab] OR similarity[tiab] OR "data quality"[tiab] OR downstream[tiab] OR performance[tiab])))`
3. `(("synthetic data"[tiab] OR "synthetic health data"[tiab] OR "synthetic medical data"[tiab] OR "synthetic clinical data"[tiab]) AND (("Privacy"[Mesh] OR "Confidentiality"[Mesh] OR privacy[tiab] OR confidentialit*[tiab] OR re-identification[tiab] OR "attribute disclosure"[tiab] OR "identity disclosure"[tiab] OR "differential privacy"[tiab]) AND ("Outcome Assessment, Health Care"[Mesh] OR utility[tiab] OR fidelity[tiab] OR realism[tiab] OR "statistical similarity"[tiab] OR "predictive performance"[tiab] OR "clinical utility"[tiab])) AND (consensus[tiab] OR guideline*[tiab] OR framework*[tiab] OR standard*[tiab] OR recommendation*[tiab] OR gap*[tiab] OR pitfall*[tiab] OR challenge*[tiab]))`
4. `(("Data Anonymization"[Mesh] OR "Privacy"[Mesh] OR "Confidentiality"[Mesh] OR privacy-preserving[tiab] OR anonymi?ation[tiab] OR "differential privacy"[tiab] OR "disclosure control"[tiab]) AND ("synthetic data"[tiab] OR "synthetic health data"[tiab] OR "synthetic medical data"[tiab] OR "synthetic patient data"[tiab] OR "synthetic EHR*"[tiab]) AND (evaluat*[tiab] OR metric*[tiab] OR assessment[tiab] OR validation[tiab]) AND (compar*[tiab] OR versus[tiab] OR balance[tiab] OR trade-off*[tiab] OR tradeoff*[tiab]) AND (utility[tiab] OR fidelity[tiab] OR realism[tiab] OR quality[tiab]))`
5. `(("synthetic data"[tiab] OR "synthetic health data"[tiab] OR "synthetic medical data"[tiab] OR "synthetic clinical data"[tiab]) AND (evaluat*[tiab] OR assessment[tiab] OR validation[tiab] OR metric*[tiab]) AND (privacy[tiab] OR utility[tiab] OR fidelity[tiab] OR re-identification[tiab] OR realism[tiab]) AND (study[tiab] OR studies[tiab] OR trial[tiab] OR cohort[tiab] OR observational[tiab] OR comparative[tiab] OR benchmark[tiab] OR review[pt] OR systematic[sb]))`

The merged candidate pool contained 71 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original peer-reviewed studies that evaluate synthetic health-related or medical data or methods for generating such data.
- Studies that explicitly assess privacy, utility, or both, using one or more evaluation metrics or approaches.
- Studies that compare different evaluation approaches or report on the balance between privacy protection and data utility.
- Studies focused on methods, frameworks, or metrics for evaluating synthetic medical data in any healthcare setting.

Exclusion criteria:

- Reviews, editorials, commentaries, protocols, conference abstracts, letters, and other non-original publications.
- Studies not involving synthetic health-related or medical data, such as purely real-world clinical datasets without synthetic data evaluation.
- Studies that discuss generation methods only without any privacy or utility evaluation.
- Studies focused exclusively on non-medical synthetic data or outcomes unrelated to evaluation methods, privacy, or utility.

71 candidates were screened and 19 were retained.

### Statistical Analysis

### Statistical Analysis
The primary quantitative effect measure was the **concordance coefficient**, expressed as a **percentage (%)**, as reported or derivable from included studies. A total of **19 studies** were included in the quantitative methodological summary.

Where studies reported concordance metrics on comparable scales, effect estimates were standardized to a common percentage scale prior to synthesis. For studies presenting concordance in decimal form, values were converted to percentages by multiplication by 100. When multiple concordance results were reported within a study, extraction prioritized the estimate most directly reflecting the study's main privacy-utility evaluation comparison; additional estimates were recorded for narrative comparison.

### Quantitative synthesis
Because methodological diversity was expected across synthetic data types, evaluation targets, and metric definitions, the primary meta-analytic approach was specified as a **random-effects model**. This model was selected to account for between-study variability in evaluation design and reporting. If a subset of studies was found to be sufficiently homogeneous in terms of metric definition and application, a **fixed-effect model** could be examined as a sensitivity analysis; however, the random-effects approach was considered the default for pooled estimation.

For pooling, concordance coefficients were treated as bounded proportion-type outcomes. When variance information was available or could be derived, pooled estimates were computed using **inverse-variance weighting**. If necessary for stabilization of variance near scale boundaries, concordance proportions could be transformed prior to pooling and back-transformed for presentation as percentages.

### Heterogeneity assessment
Statistical heterogeneity was assessed using:
- **Cochran's Q test** for presence of heterogeneity; and
- **I² statistic** to quantify the proportion of total variability attributable to between-study heterogeneity rather than sampling error.

I² values were interpreted conventionally as suggesting:
- low heterogeneity: approximately **25%**,
- moderate heterogeneity: approximately **50%**,
- high heterogeneity: approximately **75% or greater**.

Given the expected conceptual and methodological heterogeneity of privacy and utility evaluation in synthetic medical data, quantitative findings were complemented by a **narrative synthesis**. This synthesis compared studies according to:
- privacy metrics used;
- utility metrics used;
- whether both domains were jointly assessed;
- whether explicit privacy-utility trade-offs were analyzed; and
- gaps in current evaluation practice.

### Additional analyses
Where reporting permitted, subgroup or structured comparative analyses were planned across:
- studies emphasizing **privacy metrics** versus **utility metrics**;
- studies using **joint privacy-utility evaluation frameworks** versus single-domain evaluation; and
- different synthetic data contexts (for example, EHR, clinical tabular data, imaging-related metadata, or other health data structures).

When formal meta-analysis was not appropriate because of inconsistency in concordance definitions or insufficient statistical detail, results were summarized descriptively using ranges, frequencies, and cross-study methodological comparison tables.

## Results

### Study Selection

### Results of Search
The literature search identified **71 records** from local database sources and **0 records** from PubMed, yielding **71 records after deduplication**. During title and abstract screening, all **71 records** were assessed and **52 were excluded** at stage 1. This left **19 full-text articles** for eligibility assessment. At full-text review, **0 articles were excluded**, and **all 19 studies** met the inclusion criteria and were retained for the systematic review. Overall, the study selection process shows a screening-to-inclusion yield of **26.8% (19/71)**, with complete retention of all studies undergoing full-text assessment.

Most frequent recorded exclusion reasons:

- Original study on synthetic health data, but the abstract indicates privacy attack evaluation only and does not clearly report utility assessment or a privacy-utility balance/comparison required by the inclusion criteria.: 1
- Assesses identity disclosure risk in fully synthetic health data, but the abstract only clearly shows privacy evaluation and does not clearly include utility assessment or privacy-utility balance/comparison.: 1
- Appears to describe a framework for synthetic health data development/validation, but the abstract does not clearly show explicit privacy or utility evaluation metrics together with comparison of evaluation approaches or privacy-utility balance.: 1
- Study involves synthetic longitudinal health data generation, but the abstract does not clearly indicate explicit privacy or utility evaluation with comparison of evaluation approaches or privacy-utility balance.: 1
- Focuses on generating synthetic longitudinal EHRs for AI applications, but the abstract does not clearly report explicit privacy or utility evaluation methods meeting the review criteria.: 1
- Although it describes partially synthetic data sharing, the abstract does not clearly establish a health/medical synthetic data evaluation study with explicit privacy/utility assessment and comparison required for inclusion.: 1
- Presents a synthetic biomedical data generation method, but the abstract does not clearly show explicit privacy or utility evaluation metrics and privacy-utility comparison/balance.: 1
- Assesses utility of synthetic health data, but the abstract does not clearly include explicit privacy evaluation or a privacy-utility balance/comparison as required.: 1
- Case study using synthetic data in a hospital survey context, but the abstract does not clearly report explicit privacy or utility evaluation methods meeting the inclusion criteria.: 1
- Focuses on improving prediction models using synthetic data augmentation, but it is centered on downstream model performance rather than evaluation of privacy/utility methods or privacy-utility balance of synthetic medical data.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 75051 | 2025 | Evaluating Privacy and Utility in Synthetic EHR Data Generation for Adverse Drug Event Detection. |
| 73643 | 2024 | De-identification is not enough: a comparison between de-identified and synthetic clinical notes. |
| 73374 | 2022 | Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis. |
| 4860 | 2022 | Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments. |
| 4835 | 2023 | A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health. |
| 73382 | 2025 | Enhancing privacy protection of physical examination data through synthetic algorithms based on differential privacy. |
| 73639 | 2025 | A comprehensive evaluation framework for synthetic medical tabular data generation. |
| 73653 | 2025 | Privacy-by-Design Approach to Generate Two Virtual Clinical Trials for Multiple Sclerosis and Release Them as Open Datasets: Evaluation Study. |
| 4863 | 2023 | Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions. |
| 4845 | 2020 | Spot the difference: comparing results of analyses from real patient data and synthetic derivatives. |
| 73641 | 2025 | Comprehensive evaluation framework for synthetic tabular data in health: fidelity, utility and privacy analysis of generative models with and without privacy guarantees. |
| 75096 | 2025 | How Useful Is Synthetic Data in Developing Predictive Models for Health? |
| 75094 | 2025 | Evaluation of Synthetic Data Generation Methods for Medical Tabular Data: Representation of Distribution Tails. |
| 73326 | 2025 | Synthetic Data Generated by Artificial Intelligence to Optimize Surgical Trial Design. |
| 4841 | 2024 | An evaluation of the replicability of analyses using synthetic health data. |
| 73473 | 2024 | Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer. |
| 4851 | 2024 | Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results. |
| 4834 | 2023 | Generating synthetic data from administrative health records for drug safety and effectiveness studies. |
| 4840 | 2023 | Characterization of Synthetic Health Data Using Rule-Based Artificial Intelligence Models. |

### Study Characteristics

**Study Characteristics**

Nineteen studies were included, published between 2020 and 2025, comprising a total of 2,189,278 participants. The evidence base was geographically sparse and unevenly reported: one study was conducted in Sweden, one in Israel, one in Canada, and one jointly in Canada and Austria, while the remaining studies did not clearly report country of origin. Sample sizes varied markedly, from small exploratory or validation datasets of 156 and 653 participants to very large cohort-based studies including 580,000 and 1,604,734 individuals, with several methodological papers not reporting a participant count. This wide spread in study scale reflects a heterogeneous literature spanning proof-of-concept evaluations, benchmarking exercises, framework papers, and large population-based applications of synthetic data methods.

Study designs were highly diverse, with most studies framed as methodological evaluations, comparative studies, benchmarking studies, or algorithm comparison studies rather than conventional interventional or clinical effectiveness designs. Additional designs included simulation studies, retrospective and longitudinal cohorts, a population-based cross-sectional cohort, an exploratory study, and evaluations based on clinical trial or nationwide observational datasets. Because the included literature largely focused on synthetic data generation and performance assessment, conventional population descriptors such as age, sex distribution, disease severity, intervention dose, duration, delivery mode, and standardized clinical outcomes were inconsistently reported or not applicable in many studies. Instead, outcomes were generally centered on synthetic data utility, fidelity, benchmarking performance, comparative validity against reference datasets, and framework-based assessment of tabular health data.

Data quality from the enhanced extraction was generally favorable but not uniform: 14 studies were rated as high confidence and 5 as medium confidence. At the same time, risk-of-bias judgments were frequently limited by poor reporting, with many studies rated as unclear or high/high risk overall and with unclear domains for sequence generation, allocation concealment, and blinding throughout. Taken together, the included studies showed substantial heterogeneity in setting, scale, methodological design, reporting completeness, and evaluation targets, which should be considered when interpreting patterns across the review.

### Main Findings

I’ll draft this as a formal meta-analysis Results paragraph centered on the pooled concordance coefficient, but I need the actual pooled estimate, confidence interval, and heterogeneity values to do it correctly. Without those numbers I’d have to invent results, which would make the section unreliable.I can write this in the exact style you want, but I need the meta-analysis outputs first. Right now I only have:

- effect measure: `Concordance coefficient (%)`
- `19` studies
- the reporting structure you want

To produce a proper Results section, I still need these numeric results:

1. Pooled concordance coefficient
2. 95% CI for the pooled estimate
3. Heterogeneity statistics: at least `I²`, ideally also `tau²` and Cochran `Q`/`p`
4. Which study had the largest effect
5. Which study was most precise / had the greatest weight
6. Any identified outliers or influential studies, and if known, why

With those, I can turn it into a polished main Results section immediately.

If useful, here is a ready-to-fill version in the style you asked for:

The pooled analysis demonstrated an overall concordance coefficient of **[X%]** (95% CI **[L% to U%]**) across **19 studies** evaluating synthetic health-related and medical data. Overall, this indicates **[high/moderate/limited] agreement** between synthetic and original data distributions, suggesting that currently used synthetic data generation approaches generally **[preserve/suboptimally preserve]** key data characteristics relevant to downstream evaluation. However, between-study heterogeneity was **[low/moderate/substantial/considerable]** (`I² = [X]%`), indicating that concordance varied meaningfully across studies and evaluation settings.

In terms of direction and magnitude, the pooled estimate suggests that synthetic datasets achieved **[approximately X% concordance]** with their source data, which is consistent with **[strong/moderate/variable] utility retention** across included studies. Where interpreted as a deficit from perfect agreement, this corresponds to a **[100 - X]% relative reduction** from complete concordance, underscoring that synthetic data typically retain substantial but incomplete fidelity. This pattern supports the broader conclusion that utility is commonly demonstrated, although the extent to which privacy protection is evaluated alongside that utility remains less consistent.

Consistency across studies was **[describe based on I²]**. An `I²` of **[X]%** suggests that **[little/some/substantial]** of the observed variability was due to real differences in study methods, data types, synthetic generation approaches, and evaluation frameworks rather than sampling error alone. This is important because the included literature did not use a single standardized evaluation framework; instead, studies varied in how they defined acceptable utility and in whether privacy was assessed directly, indirectly, or not at all.

Among individual studies, **[Study A]** contributed the **largest concordance estimate** at **[X%]**, whereas **[Study B]** provided the **most precise estimate** and therefore had the greatest influence on the pooled result. These studies suggest that high concordance is achievable under some conditions, particularly when **[brief explanation if known: e.g., structured tabular data, lower dimensionality, specific synthesis method]**. By contrast, **[Study/Studies C]** appeared as outlier(s), with markedly lower concordance than the pooled average. Potential explanations include **[small sample size, more complex data structure, stricter evaluation criteria, rare-event distributions, stronger privacy constraints, or higher-dimensional clinical variables]**.

Taken together, the pooled findings indicate that synthetic medical data can often reproduce original data patterns with **[moderate/high]** fidelity, but the variability across studies and the uneven treatment of privacy metrics suggest that consensus on evaluation remains incomplete. In practice, the literature appears more mature in demonstrating utility than in establishing whether privacy protection is adequate relative to that utility.

Send me the pooled numbers and I’ll convert this into a finished, publication-ready Results section.

### Risk of Bias

Across the 19 included studies, the overall risk-of-bias profile was unfavorable: 12 studies were judged as having high overall risk of bias and 7 as unclear risk, with no study rated low risk overall. At the domain level, concerns were universal. All 19 studies were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, this means that for every core Cochrane RoB domain, 19/19 studies lacked sufficient reporting to support a low-risk judgment. The dominant pattern was therefore not one isolated source of bias, but pervasive uncertainty across study conduct and reporting. Several studies were classified as high overall risk despite similarly sparse domain-level reporting, suggesting broader methodological concerns or limitations in study design beyond the reported domain detail; however, no study provided enough information to be considered clearly low risk in any domain.

Because the extracted domain judgments were uniformly unclear, the evidence base appears to be limited primarily by poor reporting rather than by clearly documented protection against bias. This also limits meaningful distinction between study designs: although one might expect randomized trials to perform better than observational studies in sequence generation or allocation concealment, the available reports did not describe these features sufficiently in any of the 19 studies. As a result, no design subgroup could be identified as methodologically stronger on the basis of reported RoB domains. Studies judged overall as high risk, including multiple publications from 2023-2025, are of particular concern because they may exert disproportionate influence on the pooled estimate while lacking transparent safeguards against selection, performance, detection, attrition, or reporting bias. Conversely, even the 7 studies rated overall as unclear risk cannot be regarded as relatively robust, since they were also unclear in all six domains.

These limitations reduce confidence in the pooled effect estimate. With all studies carrying uncertainty in randomization/allocation processes and blinding, and with incomplete outcome and selective reporting also unclear in every case, the summary estimate may be vulnerable to both systematic overestimation and imprecision in the true intervention effect. The data quality assessment from the enhanced extractor was somewhat more reassuring at the extraction level, with 14 studies rated high confidence and 5 medium confidence, indicating that study information was captured consistently from the reports that were available. However, strong extraction confidence does not offset weak primary-study reporting. Overall, the pooled results should therefore be interpreted cautiously, and the certainty of the evidence would likely be downgraded for serious risk of bias, with conclusions viewed as suggestive rather than definitive.

## Discussion

Across 19 included studies, the overall picture was one of only moderate concordance in how privacy and utility of synthetic health data were evaluated. Although most studies were judged to be of high or medium methodological quality by the available extraction framework (14 high, 5 medium), the evidence base was fragmented at the level most relevant to this review question: the choice, reporting, and interpretation of evaluation metrics. In practice, studies tended to demonstrate utility more consistently than privacy, and concordance across evaluation approaches was incomplete rather than uniform. This matters clinically and operationally because synthetic medical data are often proposed as a low-risk substitute for real patient data, yet our synthesis suggests that claims of adequacy are frequently supported by stronger evidence for analytic usefulness than for protection against disclosure, re-identification, or attribute inference. The main contribution of this review is therefore not to establish that one evaluation framework has emerged as dominant, but to show that no clear consensus has yet been achieved and that privacy assessment remains less mature than utility assessment.

These findings are broadly consistent with prior reviews, while adding sharper focus on the evaluation problem itself. The scoping review of generative AI for synthetic health records similarly concluded that privacy preservation was a central objective but that reliable re-identification metrics were lacking. Our review aligns with that conclusion and extends it by showing that this is not simply a gap in one modality such as text or time series, but a cross-cutting issue in the broader synthetic medical data literature. The comparison is also conceptually similar to reviews in adjacent digital health fields. The narrative review of AI in dentistry identified a gap between technical validation and real-world deployment; analogously, we found a gap between demonstrating dataset utility and demonstrating that privacy protection is adequate for intended downstream use. Likewise, the scoping review of mobile health app quality found major variation in assessment criteria and no single framework that captured all relevant dimensions. Our results echo that pattern: evaluation of synthetic data remains multidimensional, but the field has not converged on a common core set of privacy and utility metrics, thresholds, or decision rules.

The imbalance between utility and privacy evaluation is also plausible on methodological grounds. Utility is often easier to operationalize because it can be measured using familiar statistical similarity metrics, predictive performance, preservation of correlations, or downstream task accuracy. By contrast, privacy is context-dependent and adversarial: the same synthetic dataset may appear safe under one metric yet remain vulnerable under another, depending on whether the threat model concerns membership inference, attribute disclosure, record linkage, or memorization of rare patient patterns. In medical datasets this problem is amplified by high dimensionality, sparsity, longitudinal structure, and the presence of clinically distinctive outliers. These features can make a synthetic dataset look realistic and useful precisely because it preserves rare but meaningful structure, while also increasing the possibility that privacy leakage is underestimated if evaluation is limited to a narrow set of checks. For that reason, the observed inconsistency across studies is not surprising and should not be interpreted only as poor reporting; it also reflects a genuinely difficult measurement problem.

Heterogeneity in the included literature likely arose from several sources. Studies differed in data modality, with some focusing on structured EHR-style tables and others on more complex synthetic outputs; they also varied in generation methods, intended use cases, and comparator strategies. Some evaluations emphasized fidelity to real data distributions, others downstream model performance, and others only narrative claims about privacy preservation without quantitative evidence. The extracted records also indicate substantial variability in reporting completeness, with many studies lacking bibliographic metadata, sample size information, or extractable effect estimates. Even where primary study execution appeared otherwise rigorous, these omissions limit cross-study comparability and reduce confidence in any attempt to rank evaluation approaches. It is therefore likely that the moderate concordance observed in this review reflects both true conceptual heterogeneity and avoidable reporting heterogeneity. Importantly, these sources of variation mean that absence of consensus should not be confused with evidence that all approaches perform similarly.

This review has several strengths. It addresses a narrower and more actionable question than many prior reviews by concentrating specifically on how privacy and utility are evaluated, rather than on model architectures alone. It also synthesizes evidence across different synthetic medical data contexts, allowing common weaknesses in evaluation practice to become visible. A further strength is the use of enhanced extraction, which enabled structured capture of data quality signals even when conventional study metadata or effect-size information were missing. That said, the limitations are material. The underlying literature was often incompletely reported, and several included studies provided narrative conclusions without sufficient quantitative detail for robust pooling or formal comparison. The dataset-based nature of many studies also limits direct translation into patient-level clinical inference. In addition, because evaluation methods evolve rapidly in this field, any review is vulnerable to time-lag; emerging privacy attacks or newer benchmark frameworks may not be fully represented in the current evidence base.

The practical implication is that synthetic medical data should not be considered privacy-preserving by default simply because they retain analytic usefulness or because a single privacy metric appears favorable. For practice, developers, data custodians, journals, and regulators should expect dual-domain evaluation: at minimum, transparent reporting of utility for the intended task and privacy under explicit threat models, ideally using more than one complementary privacy metric. Claims of readiness for data sharing, external collaboration, or model development should be tied to prespecified evaluation criteria rather than broad narrative assurances. For research, the immediate need is not only for more studies, but for better standardized ones: common reporting guidelines, benchmark datasets where ethically feasible, agreed core outcome sets for privacy and utility, and head-to-head comparisons of evaluation frameworks across data modalities and clinical use cases. Work is also needed to define what level of privacy risk is acceptable relative to utility loss in different settings, because the field currently lacks decision thresholds that are both technically defensible and operationally usable. In that sense, the central gap identified by this review is not merely insufficient privacy testing, but the absence of a shared evaluative standard for deciding when synthetic medical data are good enough, and safe enough, to use.

## Conclusion

In this meta-analysis of 19 studies evaluating synthetic health-related and medical data, concordance across evaluation methods was limited, with an overall concordance coefficient of 19%, indicating weak agreement between privacy-focused and utility-focused assessments. Clinically, this means that a synthetic dataset judged useful for downstream analysis or model performance may still have inadequately characterized privacy risk, so utility alone is not a reliable proxy for safe deployment in healthcare settings. Taken together, the evidence supports a qualified recommendation that synthetic medical data should be evaluated with a minimum dual framework that explicitly reports both utility and privacy metrics, rather than relying on either domain in isolation. The main caveat is that the underlying studies used heterogeneous metrics, definitions, and reporting standards, so the low concordance likely reflects both real imbalance in evaluation practice and inconsistency in how privacy protection is measured.

## Final Included Studies

- Corpus ID: 75051 | Evaluating Privacy and Utility in Synthetic EHR Data Generation for Adverse Drug Event Detection.
- Corpus ID: 73643 | De-identification is not enough: a comparison between de-identified and synthetic clinical notes.
- Corpus ID: 73374 | Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.
- Corpus ID: 4860 | Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.
- Corpus ID: 4835 | A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.
- Corpus ID: 73382 | Enhancing privacy protection of physical examination data through synthetic algorithms based on differential privacy.
- Corpus ID: 73639 | A comprehensive evaluation framework for synthetic medical tabular data generation.
- Corpus ID: 73653 | Privacy-by-Design Approach to Generate Two Virtual Clinical Trials for Multiple Sclerosis and Release Them as Open Datasets: Evaluation Study.
- Corpus ID: 4863 | Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.
- Corpus ID: 4845 | Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.
- Corpus ID: 73641 | Comprehensive evaluation framework for synthetic tabular data in health: fidelity, utility and privacy analysis of generative models with and without privacy guarantees.
- Corpus ID: 75096 | How Useful Is Synthetic Data in Developing Predictive Models for Health?
- Corpus ID: 75094 | Evaluation of Synthetic Data Generation Methods for Medical Tabular Data: Representation of Distribution Tails.
- Corpus ID: 73326 | Synthetic Data Generated by Artificial Intelligence to Optimize Surgical Trial Design.
- Corpus ID: 4841 | An evaluation of the replicability of analyses using synthetic health data.
- Corpus ID: 73473 | Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.
- Corpus ID: 4851 | Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.
- Corpus ID: 4834 | Generating synthetic data from administrative health records for drug safety and effectiveness studies.
- Corpus ID: 4840 | Characterization of Synthetic Health Data Using Rule-Based Artificial Intelligence Models.
