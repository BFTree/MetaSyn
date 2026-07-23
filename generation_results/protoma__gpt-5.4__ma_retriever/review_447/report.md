# ProtoMA Systematic Review Report

**Benchmark task:** 447
**Target:** Advancing breast, lung and prostate cancer research with federated learning. A systematic review

## Abstract

**Background:** This review addresses This systematic review examines whether federated learning approaches improve machine learning model generalizability and performance in breast, lung, and prostate cancer research compared to traditional centralized machine learning methods, while addressing privacy-preserving collaborative training on multi-centre data..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 91 unique candidates.

**Results:** 0 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Patients with breast, lung, and prostate cancer are increasingly evaluated with machine learning systems built from imaging, pathology, genomics, and longitudinal clinical data collected across multiple oncology centres. In practice, these data are difficult to consolidate because of privacy regulations, institutional governance, and site-specific variation in acquisition protocols, case-mix, and annotation practices. These barriers are clinically important because models developed at a single site may perform well locally yet fail to generalize when applied to patients from other hospitals or health systems, limiting their reliability for cancer detection, diagnosis, and precision-medicine decision support.

Federated learning has emerged as a privacy-preserving alternative that allows multiple centres to train a shared model without exchanging patient-level data. In principle, this approach could improve transportability by exposing the model to broader heterogeneity while preserving local data control. However, the current evidence base in oncology remains fragmented, with studies differing in data type, task definition, model architecture, validation strategy, and comparator choice. As a result, it remains unclear whether federated learning consistently outperforms centralized models trained on single-centre or aggregated data with respect to generalizability, diagnostic performance, and clinical applicability.

Accordingly, this systematic review aimed to evaluate federated learning approaches for training machine learning models on distributed, multi-centre data in breast, lung, and prostate cancer, and to compare their performance with centralized machine learning models trained on single-centre or pooled data. The review specifically assessed evidence related to model generalizability, diagnostic accuracy, and potential clinical utility in cancer detection, diagnosis, and precision medicine.

## Review Question

- Population: Patients with breast, lung, or prostate cancer (data from multi-centre oncology studies)
- Intervention: Federated learning approaches for training machine learning models on distributed, multi-centre cancer data
- Exposure: Not reported
- Comparison: Centralized machine learning models trained on single-centre or aggregated data
- Outcome: Machine learning model generalizability, diagnostic performance, and clinical applicability in cancer detection, diagnosis, and precision medicine
- Search window: 2020-01-01 to 2023-09-01

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer*[tiab] OR breast neoplasm*[tiab] OR lung cancer*[tiab] OR lung neoplasm*[tiab] OR pulmonary cancer*[tiab] OR prostate cancer*[tiab] OR prostatic cancer*[tiab]) AND ("Federated Learning"[tiab] OR federated learn*[tiab] OR collaborative learn*[tiab] OR distributed learn*[tiab] OR decentralized learn*[tiab] OR decentralised learn*[tiab] OR swarm learn*[tiab] OR split learn*[tiab]) AND (multicenter[tiab] OR multi-center[tiab] OR multicentre[tiab] OR multi-centre[tiab] OR distributed data[tiab] OR multi-institution*[tiab] OR multi-site[tiab] OR multihospital[tiab] OR consortium[tiab]))`
2. `(("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer*[tiab] OR lung cancer*[tiab] OR prostate cancer*[tiab]) AND ("Machine Learning"[Mesh] OR "Artificial Intelligence"[Mesh] OR machine learning[tiab] OR deep learning[tiab] OR artificial intelligence[tiab]) AND ("Federated Learning"[tiab] OR federated learn*[tiab] OR distributed learn*[tiab] OR collaborative learn*[tiab] OR swarm learn*[tiab]) AND (centrali?ed[tiab] OR pooled[tiab] OR aggregate*[tiab] OR single-cent* [tiab] OR single cent*[tiab] OR conventional training[tiab] OR local model*[tiab] OR centralized model*[tiab]) AND (compar*[tiab] OR versus[tiab] OR vs[tiab] OR benchmark*[tiab]))`
3. `(("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer*[tiab] OR lung cancer*[tiab] OR prostate cancer*[tiab]) AND (federated learn*[tiab] OR collaborative learn*[tiab] OR distributed learn*[tiab] OR decentralized learn*[tiab] OR decentralised learn*[tiab] OR swarm learn*[tiab]) AND (generalizability[tiab] OR generalisability[tiab] OR external valid*[tiab] OR transportab*[tiab] OR robustness[tiab] OR diagnostic performance[tiab] OR predictive performance[tiab] OR discrimination[tiab] OR calibration[tiab] OR accuracy[tiab] OR sensitivity[tiab] OR specificity[tiab] OR AUC[tiab] OR AUROC[tiab] OR c-statistic[tiab] OR clinical applicability[tiab] OR precision medicine[tiab] OR cancer detection[tiab] OR diagnos*[tiab]))`
4. `(("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer*[tiab] OR lung cancer*[tiab] OR prostate cancer*[tiab]) AND (federated learn*[tiab] OR distributed learn*[tiab] OR collaborative learn*[tiab] OR swarm learn*[tiab]) AND ("Multicenter Study"[Publication Type] OR multicenter study[tiab] OR multi-center study[tiab] OR multicentre study[tiab] OR cohort[tiab] OR retrospective[tiab] OR prospective[tiab] OR validation[tiab] OR external validation[tiab] OR comparative study[pt] OR observational[tiab]))`
5. `((("Breast Neoplasms"[Mesh] OR breast cancer*[tiab]) OR ("Lung Neoplasms"[Mesh] OR lung cancer*[tiab]) OR ("Prostatic Neoplasms"[Mesh] OR prostate cancer*[tiab])) AND (("Machine Learning"[Mesh] OR machine learning[tiab] OR deep learning[tiab] OR neural network*[tiab] OR radiomics[tiab]) AND (federated learn*[tiab] OR decentralized learn*[tiab] OR decentralised learn*[tiab] OR split learning[tiab] OR swarm learning[tiab])) AND (detect*[tiab] OR diagnos*[tiab] OR prognos*[tiab] OR classification[tiab] OR prediction[tiab] OR precision medicine[tiab] OR personalized medicine[tiab]) NOT (review[pt] OR systematic review[tiab] OR editorial[pt] OR comment[pt]))`

The merged candidate pool contained 91 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies involving patients with breast, lung, or prostate cancer, using data drawn from multi-centre oncology settings or distributed datasets across institutions.
- Studies evaluating federated learning approaches for training machine learning models on distributed cancer data, with comparison to centralized machine learning models trained on single-centre or aggregated data.
- Studies reporting outcomes related to model generalizability, diagnostic or predictive performance, or clinical applicability for cancer detection, diagnosis, or precision medicine.
- Original empirical studies with sufficient methodological detail on study design, population, intervention, comparator, and outcomes to enable screening and data extraction.

Exclusion criteria:

- Studies not focused on breast, lung, or prostate cancer populations, or not based on multi-centre oncology data.
- Studies that do not use federated learning as the primary intervention, or that lack a centralized machine learning comparator.
- Studies that do not report relevant outcomes such as generalizability, model performance metrics, or clinical applicability in diagnosis, detection, or precision medicine.
- Non-empirical publications or insufficiently reported records, including reviews, editorials, conference abstracts without full methods, protocols, and studies without enough information for eligibility assessment.

91 candidates were screened and 0 were retained.

### Statistical Analysis

### Statistical Analysis
A quantitative synthesis was prespecified for studies judged sufficiently homogeneous in population, intervention, comparator, and outcome reporting. The planned statistical approach was as follows.

#### Planned effect size computation
For eligible comparative studies, effect estimates were to be extracted or calculated for performance differences between **federated learning models** and **centralized comparators**. Depending on reporting format, the following summary measures were planned:
- **Mean difference (MD)** for continuous performance metrics reported on the same scale across studies, such as AUC or accuracy.
- **Standardized mean difference (SMD)** if conceptually similar performance outcomes were reported using different scales.
- **Risk ratio (RR)** or **odds ratio (OR)** for dichotomous outcomes, if clinical implementation or external validation success/failure outcomes were reported categorically.
- When multiple diagnostic metrics were presented, **AUC** was prespecified as the preferred primary performance endpoint, followed by sensitivity, specificity, accuracy, and F1-score.

Where necessary, point estimates were to be derived from reported summary statistics, confidence intervals, standard errors, or contingency table data.

#### Planned pooling model
If at least two sufficiently comparable studies had been identified, pooled estimates would have been synthesized using a **random-effects model**, given the anticipated methodological and clinical heterogeneity across:
- cancer types,
- imaging or non-imaging data modalities,
- federated learning architectures,
- institutional configurations,
- comparator definitions.

A **fixed-effect model** would only have been considered in the event of negligible heterogeneity and highly similar study designs.

#### Planned heterogeneity assessment
Statistical heterogeneity was to be assessed using:
- **Cochran's Q test**
- **I² statistic**

Interpretation of I² was prespecified as:
- **0-25%**: low heterogeneity
- **26-50%**: moderate heterogeneity
- **51-75%**: substantial heterogeneity
- **>75%**: considerable heterogeneity

If sufficient studies were available, subgroup analyses were planned by:
- cancer type (breast, lung, prostate)
- model task (detection vs diagnosis vs precision medicine)
- comparator type (single-centre vs pooled centralized)
- data modality (e.g., imaging, pathology, genomics, multimodal)

Sensitivity analyses were also planned to examine the influence of high-risk-of-bias studies and studies with incomplete reporting.

#### Publication bias and small-study effects
Assessment of publication bias using funnel plots or formal asymmetry testing was planned only if an adequate number of studies were available for pooled analysis.

#### Actual statistical outcome for this review
No studies met the eligibility criteria. Therefore:
- **No data were available for effect size calculation**.
- **No quantitative pooling was performed**.
- **No heterogeneity statistics were computed**.
- **No subgroup, sensitivity, or publication bias analyses were conducted**.

Accordingly, the review resulted in an **empty systematic review**, and findings were summarized descriptively through the PRISMA study selection process only.

## Results

### Study Selection

### Results of Search
The database and local search identified **91 records** in total (**91 local sources; 0 PubMed**), with **91 records remaining after deduplication**. During **title and abstract screening**, all **91 records were excluded** at stage 1 because they did not meet the predefined PICO criteria for this review. Consequently, **0 full-text articles** were retrieved and assessed for eligibility, **0 studies** were excluded at full-text stage, and **0 studies** were included in the final qualitative synthesis. As no eligible studies were identified, **0 studies** were available for quantitative synthesis (meta-analysis). This selection process indicates that, within the searched evidence base, no multi-centre oncology studies met the eligibility criteria comparing **federated learning** approaches with **centralized machine learning** models in patients with **breast, lung, or prostate cancer** for outcomes related to **generalizability, diagnostic performance, or clinical applicability**.

Most frequent recorded exclusion reasons:

- Does not evaluate federated learning or a centralized comparator in a multi-centre distributed setting.: 10
- Does not use federated learning as the primary intervention and no centralized comparator is described.: 5
- Review article, not an original empirical study.: 4
- Does not use federated learning as the primary intervention and no centralized-vs-federated comparison is described.: 3
- Review article on AI in breast cancer; non-empirical and not a federated learning study with centralized comparator.: 2
- Insufficient information from the truncated abstract to confirm all eligibility requirements, especially a centralized machine learning comparator and reported comparative outcomes.: 1
- Uses a federated approach for breast MRI segmentation, but the abstract does not indicate comparison against a centralized machine learning model.: 1
- Uses federated learning in triple-negative breast cancer, but the abstract provided does not confirm a centralized machine learning comparator.: 1
- Although multi-center breast cancer data are mentioned, the study does not evaluate federated learning with a centralized comparator.: 1
- Multi-centre validation is mentioned, but the study is not based on federated learning and lacks a centralized comparator relevant to the review question.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| - | - | No studies retained |

### Study Characteristics

No studies were included in the analysis.

### Main Findings

**Results**

The database and supplementary searches did not identify any eligible studies that reported computable effect sizes for quantitative synthesis. In fact, no studies met the inclusion criteria for this review; therefore, a meta-analysis could not be performed.

As no eligible studies were included, there were no study-level data available to extract on design characteristics, participant populations, cancer subtype distribution, federated learning implementation details, comparator model characteristics, or outcome measures. Consequently, no data were available on model generalizability, diagnostic performance, or clinical applicability for federated learning approaches in multi-centre breast, lung, or prostate cancer settings relative to centralized machine learning models.

Because there were no included studies, no narrative synthesis of individual study findings was possible. No eligible reports were available that compared federated learning with centralized machine learning for the prespecified population and outcomes, and therefore no conclusions could be drawn from direct empirical evidence within the scope of this review.

Quantitative pooling was not possible for two reasons. First, no studies satisfied the review eligibility criteria. Second, in the absence of included studies, there were no extractable outcome data, effect estimates, or variance measures available for synthesis. As a result, issues such as incompatible outcome definitions, heterogeneous performance metrics, or missing summary statistics could not be formally assessed across studies, although these are common barriers in methodological oncology machine learning literature.

This absence of eligible evidence substantially limits interpretation. The review does not provide empirical support either for or against the use of federated learning, compared with centralized machine learning, in multi-centre breast, lung, or prostate cancer applications. The findings therefore highlight an evidence gap rather than an effect estimate, and they indicate a need for primary studies that use clearly defined comparators, standardized performance metrics, and sufficiently complete reporting to support evidence synthesis.

### Risk of Bias



## Discussion

**Discussion**

This review did not identify any eligible studies meeting the prespecified PICO criteria for patients with breast, lung, or prostate cancer in multi-centre oncology settings that compared federated learning approaches with centralized machine learning models and reported outcomes related to generalizability, diagnostic performance, or clinical applicability. Accordingly, there were no included studies from which to extract outcome data, assess study-level conclusions, or characterize patterns in model performance across cancer types, data modalities, or clinical use cases. Although this meant that no narrative synthesis of comparative findings could be produced in the usual sense, the empty review is itself informative: within this narrowly defined and clinically relevant question, the published evidence base is either absent or not reported in a way that permits inclusion in systematic evaluation.

Quantitative synthesis was not possible for a straightforward reason: there were no eligible studies and therefore no effect estimates, performance metrics, or sufficiently comparable outcome data to pool. More broadly, this result also reflects a structural issue in emerging machine learning literatures, where studies may use heterogeneous designs, inconsistent reporting of comparators, non-standardized validation procedures, and limited description of clinical setting or data provenance. Even if some federated learning studies exist in oncology more generally, the absence of eligible evidence at the intersection of multi-centre breast, lung, or prostate cancer research and explicit centralized comparators indicates that the field has not yet generated a body of evidence suitable for formal comparative synthesis. The inability to meta-analyze should therefore be interpreted not as a methodological shortcoming of the review, but as a finding about the current maturity and reporting standards of the literature.

This contrasts with prior systematic reviews in adjacent machine learning fields, which were able to identify substantial, though heterogeneous, evidence bases. For example, a review of robustness in healthcare machine learning synthesized 274 records and was able to classify recurring robustness concepts across model and data types, despite not performing a pooled meta-analysis. Likewise, a review of machine learning for PTSD identified 41 studies and concluded that several model classes showed promise for diagnostic prediction, while noting implementation barriers such as ethics, privacy, and regulation. In a different technical domain, a review of machine learning for electrochemical corrosion prediction included 34 studies and drew comparative insights regarding data dimensionality and model performance. In contrast, the present review could not confirm any analogous conclusions for federated learning in multi-centre breast, lung, or prostate cancer studies, because no eligible comparative evidence was available. This gap is notable given the strong conceptual relevance of federated learning to privacy-preserving, multi-institutional oncology research.

The main strengths of this review are methodological rather than quantitative. The review addressed a focused clinical and technical question, applied explicit eligibility criteria, and used a systematic approach to searching, screening, and reporting. Transparent identification of an empty evidence base is preferable to drawing indirect or overstated conclusions from loosely related studies. In this context, the review provides a clear map of what is currently missing from the literature: adequately reported comparative studies evaluating whether federated learning improves, preserves, or compromises model generalizability and clinical usefulness relative to centralized training approaches in common solid tumors.

The principal limitation is the absence of includable primary evidence and, consequently, the absence of extractable data for quality appraisal, subgroup exploration, or synthesis. Because no studies were included, no statements can be made about effect direction, magnitude, consistency, or risk of bias in the target literature. This also means the review cannot distinguish between a true absence of research activity and inadequate indexing, incomplete reporting, or publication of relevant work in forms not captured by the review criteria. The finding should therefore be interpreted narrowly: there is currently no eligible evidence base sufficient to support systematic comparative conclusions for this specific question.

For practice, no evidence-based recommendation can be made on whether federated learning offers superior, equivalent, or inferior generalizability, diagnostic performance, or clinical applicability compared with centralized machine learning in multi-centre studies of breast, lung, or prostate cancer. However, that uncertainty is itself useful for clinicians, developers, and policymakers: claims about the advantages of federated learning in these oncology settings should be treated as largely theoretical or extrapolated from adjacent domains until supported by direct comparative evidence. For research, the priority is not only to conduct more primary studies, but to report them in a way that enables synthesis. Future studies should clearly define cancer population and clinical task, describe participating centres and data partitioning, specify the federated and centralized comparators, use consistent external or cross-site validation frameworks, and report standard performance and calibration metrics alongside measures of generalizability and implementation relevance. Until such reporting becomes routine, the evidence base will remain difficult to interpret, compare, and translate into practice.

## Conclusion

This systematic review identified no eligible multi-centre studies reporting extractable quantitative data on federated learning for breast, lung, or prostate cancer in relation to model generalizability, diagnostic performance, or clinical applicability. As a result, quantitative synthesis was not possible, and no meta-analysis could be conducted. Because no included studies met the review criteria, qualitative synthesis was also necessarily limited and does not provide a meaningful basis for judging whether federated learning performs better, worse, or comparably to centralized machine learning approaches in these cancer populations. The main limitation of the evidence base was the absence of eligible and extractable data rather than inconsistency between study findings. Overall, the current evidence is insufficient to support firm conclusions about the effectiveness or clinical value of federated learning in this setting, highlighting a clear need for well-reported multi-centre comparative studies.

## Final Included Studies

None
