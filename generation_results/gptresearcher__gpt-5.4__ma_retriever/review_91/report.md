# Systematic Review Report: Evaluation Consensus for Privacy and Utility in Synthetic Health Data

## Abstract

This scoping review examined whether the synthetic health data literature shows consensus on standardized methods for evaluating privacy and utility, and whether privacy is treated with equal importance relative to utility. Using only the provided local MetaSyn PubMed corpus search results and retrieved records, I screened candidate studies published between January 1, 2018 and July 31, 2024 against the stated eligibility criteria. The included evidence indicates partial convergence, not full consensus. Across recent health-tabular studies, researchers increasingly organize evaluation around three recurring dimensions: fidelity or resemblance, utility, and privacy. However, there is still no field-wide standardized benchmark, and privacy evaluation remains materially less consistent and often less developed than utility evaluation. Utility is commonly assessed using descriptive similarity and downstream analytic performance, while privacy is more variably measured through disclosure risk, membership inference, nearest-record distance, and identity disclosure frameworks. Several studies report that fully synthetic data are less vulnerable than partially synthetic data, but they also show that privacy conclusions depend strongly on the attack model and disclosure definition. Newer framework papers add usability, computational complexity, outlier behavior, and domain-constraint validation, suggesting that narrow resemblance metrics can miss clinically important failures such as duplicate-row amplification and out-of-range values. My overall judgment is that the literature has reached agreement on the *dimensions* that should be assessed, but not on a standardized *methodological protocol* or a balanced *privacy-first evaluation practice*. Privacy is still treated as necessary but not yet as consistently or rigorously as utility.

## Introduction

Synthetic health data are increasingly proposed as a mechanism for sharing sensitive clinical data while reducing barriers to research access. Yet the value of synthetic data depends on two linked requirements: the data must remain useful for intended analyses, and they must not expose unacceptable privacy risk. The review question asks whether the field has reached consensus on standardized evaluation methods for these goals, and whether privacy is assessed on equal footing with utility.

The recent literature strongly suggests movement toward multidimensional evaluation frameworks rather than reliance on one-dimensional statistical similarity checks. Framework-oriented work argues that evaluation should include fidelity or quality, utility or usability, and privacy, with some newer proposals extending this to computational complexity and fidelity-utility tradeoff analysis ([A comprehensive evaluation framework for synthetic medical tabular data generation, 2025](metasyn://corpus/73639); [Comprehensive evaluation framework for synthetic tabular data in health, 2025](metasyn://corpus/73641); [Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions, 2023](metasyn://corpus/4863)). At the same time, reviews of longitudinal and time-series health data report fragmented evaluation practice, sparse privacy assessment, and limited reporting of differential privacy parameters, reinforcing the concern that consensus remains incomplete ([Synthetic data generation methods for longitudinal and time series health data: a systematic review, 2025](metasyn://corpus/57829)).

Because the eligibility criteria exclude reviews, this report centers on primary studies that generated synthetic health data and evaluated output quality, utility, and/or privacy.

## Methods

### Retrieval Source

Only the local MetaSyn corpus search output supplied in the prompt was used as the retrieval source. No external databases or web search were used.

### Search Queries Used

The report is based on the following local corpus search queries present in the provided retrieval material:

1. `synthetic health data evaluation benchmark tabular longitudinal fidelity utility privacy fairness computational cost clinical realism standardized framework review 2023 2024`
2. `synthetic medical data reporting standard differential privacy epsilon delta membership inference subgroup fairness rare event tail fidelity health data 2023 2024 2025 2026`

These searches returned ranked candidate records with Corpus IDs and abstracts. Additional evidence came from the supplied hierarchical research summaries tied to specific Corpus IDs.

### Eligibility Criteria

**Inclusion criteria**
- Publications describing research that uses synthetic data generation methods and evaluates their outputs.
- Health-related or medical synthetic data.
- Published between 2018-01-01 and 2024-07-31.

**Exclusion criteria**
- Surveys, systematic reviews, and scoping reviews.
- Non-English documents.
- Publications with no evaluation of generated output.
- Unstructured data only (e.g., images, free text).
- Poster abstracts.

### Screening Logic

I screened all candidate records shown in the provided searches. I preserved exact Corpus ID values from the results. Records published after July 31, 2024 were excluded from the final included-study set even if they contained useful contextual evidence for interpreting the trajectory of the field.

## Retrieval and Screening Results

### Candidate Studies Screened

The two search outputs substantially overlapped. After deduplication by Corpus ID and title, the most relevant candidates for screening included:

- 4863
- 4849
- 73343
- 4851
- 4850
- 4845
- 73473
- 4841
- 4861
- 4837
- 4867
- 4868
- 4982
- 73639
- 73641
- 57829
- 73412
- 73502
- 75094
- 75096
- 73382
- 72694

### Excluded After Screening

The following were excluded for the reasons shown:

| Corpus ID | Title | Exclusion Reason |
|---|---|---|
| 4863 | *Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions* | Method/framework paper focused on evaluation pipeline and benchmarking; not clearly a primary synthesis-and-evaluation study in the sense of a substantive synthetic data application sample for this review |
| 4837 | *The Problem of Fairness in Synthetic Healthcare Data* | Focused on fairness analysis of synthetic datasets rather than core privacy/utility evaluation of a generation study |
| 73639 | *A comprehensive evaluation framework for synthetic medical tabular data generation* | Published 2025, outside date range |
| 73641 | *Comprehensive evaluation framework for synthetic tabular data in health* | Published 2025, outside date range |
| 57829 | *Synthetic data generation methods for longitudinal and time series health data: a systematic review* | Review article |
| 73412 | *Synthetic data production for biomedical research* | Published 2025, outside date range |
| 73502 | *Synthetic Data Generation Methods for Longitudinal and Time Series Health Data* | Review article, 2025 |
| 75094 | *Evaluation of Synthetic Data Generation Methods for Medical Tabular Data: Representation of Distribution Tails* | Published 2025, outside date range |
| 75096 | *How Useful Is Synthetic Data in Developing Predictive Models for Health?* | Published 2025, outside date range |
| 73382 | *Enhancing privacy protection of physical examination data through synthetic algorithms based on differential privacy* | Published 2025, outside date range |
| 72694 | *Attention-based synthetic data generation for calibration-enhanced survival analysis* | Published 2025, outside date range |

### Included Studies

Nine studies met the date and content criteria and were included:

| Corpus ID | Year | Study Type | Data Type | Output Evaluation Present | Full-text Availability |
|---|---:|---|---|---|---|
| 4849 | 2024 | Primary model development/validation | Longitudinal health data | Utility + privacy discussion | Full-text sections available |
| 4851 | 2024 | Primary synthesis evaluation | Longitudinal cohort data | In-depth quality + reproduction of analyses | Full-text sections available |
| 4841 | 2024 | Simulation/evaluation study | Heterogeneous health datasets | Replicability + privacy | Full-text sections available |
| 73473 | 2024 | Primary actionability study | Rare/heterogeneous oncology cohort | Veracity + utility + privacy concealment | Full-text sections available |
| 73343 | 2023 | Primary synthesis feasibility study | Administrative longitudinal health data | Utility + privacy | Full-text sections available |
| 4982 | 2023 | Primary model study | Synthetic EHR trajectories | Realism + privacy | Full-text sections available |
| 4861 | 2022 | Primary method study | Time-to-event cancer data | Fidelity + identifiability risk | Full-text sections available |
| 4868 | 2022 | Primary method study | Time-varying correlated clinical data | Utility + disclosure risk | Partial full-text sections available |
| 4867 | 2022 | Primary privacy attack study | Synthetic health data | Membership inference privacy evaluation | Full-text sections available |
| 4850 | 2021 | Primary model comparison | Tabular health data | Statistics + ML tasks + disclosure risk | Abstract-only in provided material |
| 4845 | 2020 | Primary use-case evaluation | Synthetic derivatives of patient data | Statistical/ML/spatial analytic agreement | Full-text sections available |

## Findings

## 1. There Is Convergence on Core Evaluation Dimensions, but Not Standardization

The most consistent cross-study pattern is not a standardized metric set, but a repeated conceptual structure: studies tend to evaluate some combination of resemblance/fidelity, analytic utility, and privacy. This is already visible in 2020-2024 primary studies and becomes explicit in later framework papers. For example, 2023 and 2024 application studies assessed distributional similarity, ability to reproduce analyses, or model performance, then paired these with disclosure-oriented privacy checks such as attribution risk or membership disclosure ([73343](metasyn://corpus/73343); [4841](metasyn://corpus/4841); [4868](metasyn://corpus/4868)).

However, the metric implementations vary substantially. Some studies emphasize descriptive similarity and inferential replication, others use machine learning discrimination tasks, and privacy is assessed with heterogeneous concepts such as attribution disclosure, membership inference, exact-record similarity, or broader qualitative claims. This variation supports the conclusion that the field has a shared *evaluation vocabulary* but not a standardized *evaluation protocol*.

This interpretation is reinforced by the 2023 health-domain benchmarking pipeline, which explicitly states that the literature lacked a standardized and objective evaluation and benchmarking strategy and therefore proposed an orchestrated pipeline around resemblance, utility, and privacy ([Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions, 2023](metasyn://corpus/4863)). Although excluded from the formal included-study set because it functions more as a framework paper, it is highly relevant contextual evidence.

## 2. Utility Assessment Is More Mature and More Consistently Reported Than Privacy

Across included studies, utility evaluation is generally richer and more consistently operationalized than privacy evaluation.

Common utility approaches included:
- distributional similarity measures such as Hellinger distance,
- preservation of dependency structure or transitions,
- replication of downstream regression or survival analyses,
- agreement in model estimates, confidence intervals, power, and bias,
- cohort- or population-level agreement across use cases.

For example, the 2023 administrative health data study (Corpus ID 73343) reported Hellinger distance for event types, attributes, and higher-order transitions, then compared Cox regression hazard ratios between real and synthetic data, achieving a mean 68% confidence interval overlap for adjusted hazard ratios ([A method for generating synthetic longitudinal health data, 2023](metasyn://corpus/73343)). The 2024 replicability study (Corpus ID 4841) evaluated eight separate replicability metrics and found that sequential synthesis, when combining at least ten same-sized synthetic datasets, achieved high decision and estimate agreement, low bias, and nominal confidence interval coverage, while single-dataset analysis could be misleading ([An evaluation of the replicability of analyses using synthetic health data, 2024](metasyn://corpus/4841)).

By contrast, privacy evaluations were often narrower. Some studies relied on a single disclosure metric or a narrative assertion that direct patient linkage had been removed. The 2025 review of temporal health SDG, while outside the eligibility window, sharply summarizes the imbalance: only 30% of studies included any privacy metric and only about 6% implemented differential privacy, often without parameter disclosure ([Synthetic data generation methods for longitudinal and time series health data: a systematic review, 2025](metasyn://corpus/57829)). This later synthesis is consistent with what is visible in the included 2020-2024 primary studies.

My judgment is that privacy is not given equal methodological weight relative to utility in the pre-July-2024 literature. It is usually acknowledged as essential, but often measured with less depth, less variety, and less reporting discipline.

## 3. Privacy Risk Depends Strongly on the Type of Synthetic Data and the Attack Model

The included studies show that privacy cannot be treated as a binary property of “synthetic versus real.” It depends on whether the release is fully or partially synthetic, how the generator works, and how risk is tested.

The strongest privacy-specific evidence comes from Corpus ID 4867, a 2022 study of membership inference attacks against synthetic health data. It found that partially synthetic data were vulnerable to membership inference at a very high rate, whereas fully synthetic data were only marginally susceptible in most cases ([Membership inference attacks against synthetic health data, 2022](metasyn://corpus/4867)). This is a critical result because it demonstrates that one of the field’s most common implicit assumptions, that synthetic data are broadly privacy-protective by construction, does not hold uniformly.

Other privacy evidence uses disclosure-risk formulations rather than direct attack simulation. The 2023 longitudinal administrative data study concluded that attribution disclosure risk was substantially below a commonly accepted 0.09 threshold ([73343](metasyn://corpus/73343)). The supplied hierarchical evidence also notes a 2020 validation study of meaningful identity disclosure risk with values of 0.0198 and 0.0086, below the same 0.09 threshold, and lower than the original data ([metasyn://corpus/4842](metasyn://corpus/4842)). That specific record was not surfaced in the candidate list provided for this screening workflow, so I do not count it as an included study, but it supports the broader pattern that identity-disclosure style metrics can yield reassuring results in fully synthetic settings.

A related privacy test from the supplied deeper research summary is nearest-record distance: if synthetic records are no closer to training records than to holdout records, that supports learning of population structure rather than memorization ([metasyn://corpus/4856](metasyn://corpus/4856)). Again, this was not part of the candidate set screened here, but it is a useful example of the expanding privacy toolkit.

## 4. Differential Privacy Is Seen as Valuable but Commonly Underspecified

The included date window contains limited primary evidence on differential privacy in health synthetic data evaluation, but the broader retrieved context shows a recurring pattern: differential privacy is treated as a meaningful privacy enhancement, yet often at the cost of fidelity and utility, and many studies either assess only a single privacy budget or omit detailed DP parameter reporting altogether ([73641](metasyn://corpus/73641); [57829](metasyn://corpus/57829)). Because these are 2025 papers, they serve as trajectory evidence rather than included primary evidence.

The implication for the review question is direct: even where privacy is foregrounded, the field has not yet normalized transparent privacy-accounting practice. A literature that does not routinely report epsilon, delta, multiple privacy budgets, and the resulting privacy-utility frontier cannot reasonably claim strong standardization.

## 5. Newer Evaluation Thinking Exposes Failures Missed by Traditional Similarity Metrics

A major conceptual advance emerging from the deeper research branch is the argument that simple resemblance metrics can miss clinically material problems. The 2025 framework paper in *Journal of Biomedical Informatics* states that multidimensional evaluation can reveal duplicate-row amplification, out-of-range values, outlier behavior, and domain-specific constraint violations ([73639](metasyn://corpus/73639)). Although this paper is outside the review window, it clarifies why earlier studies that rely mainly on descriptive similarity and downstream prediction may overestimate synthetic data quality.

This matters because health data are clinically constrained. A synthetic dataset can preserve marginal distributions yet still generate impossible lab values, implausible code combinations, or unstable tails. The 2025 tail-focused study likewise argues that abnormal values are more critical than normal values in medical datasets and that evaluation must attend to distribution tails ([75094](metasyn://corpus/75094)). Taken together, these later studies deepen the interpretation of earlier evidence: the field has likely under-evaluated domain realism in many 2020-2024 studies.

## Limitations

This review has several important limitations.

First, retrieval was limited to the local MetaSyn candidate lists and the hierarchical research summaries included in the prompt. I did not run new corpus fetches beyond the provided material.

Second, several relevant records are abstract-only in the supplied evidence. In particular, Corpus ID 4850 (*Application of Bayesian networks to generate synthetic health data*) was screened and included based on abstract-level evidence because no full-text sections were available in the provided material. Conclusions drawn from such studies are less secure than those supported by accessible methods and results sections.

Third, this is a scoping-style synthesis, not a quantitative meta-analysis in the statistical pooling sense. Outcome heterogeneity across utility and privacy metrics is too high to support meaningful pooled effect estimates from the provided material.

Fourth, some influential contextual studies surfaced only through higher-level synthesis summaries rather than the candidate set used for formal screening. I referenced them cautiously as contextual evidence, not as part of the included-study core.

## Conclusion

The synthetic health data literature up to July 31, 2024 does **not** show consensus on a standardized method for evaluating privacy and utility. It does show a growing consensus on the **dimensions** that matter: fidelity or resemblance, utility, and privacy. That distinction is crucial.

Utility evaluation is currently more mature, more detailed, and more consistently reported than privacy evaluation. Privacy is rarely ignored outright, but it is often assessed with fewer metrics, less transparent reporting, and weaker standardization. The strongest privacy evidence also shows that synthetic data are not uniformly safe: partially synthetic data can be highly vulnerable to membership inference, while fully synthetic data generally appear safer but still require explicit testing.

My concrete assessment is that the field is in a transitional state. It has moved beyond naive similarity checks and now recognizes the need for multidimensional evaluation. But it has not yet operationalized that recognition into a stable, standardized benchmark or a privacy evaluation culture equal in rigor to utility testing. The most credible path forward is a required minimum evaluation bundle: descriptive fidelity, downstream analytic utility, at least one attack-based privacy test, at least one disclosure-risk test, explicit reporting of whether data are fully or partially synthetic, and transparent accounting of any differential privacy parameters. Without that, claims of privacy-preserving usefulness remain too model-specific and too weakly comparable across studies.

## Included Study List

1. *Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation* — Corpus ID **4849**
2. *Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results* — Corpus ID **4851**
3. *An evaluation of the replicability of analyses using synthetic health data* — Corpus ID **4841**
4. *Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer* — Corpus ID **73473**
5. *A method for generating synthetic longitudinal health data* — Corpus ID **73343**
6. *Synthetic electronic health records generated with variational graph autoencoders* — Corpus ID **4982**
7. *Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility* — Corpus ID **4861**
8. *DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations* — Corpus ID **4868**
9. *Membership inference attacks against synthetic health data* — Corpus ID **4867**
10. *Application of Bayesian networks to generate synthetic health data* — Corpus ID **4850** *(abstract-only evidence in provided material)*
11. *Spot the difference: comparing results of analyses from real patient data and synthetic derivatives* — Corpus ID **4845**

## References

- A comprehensive evaluation framework for synthetic medical tabular data generation. [metasyn://corpus/73639](metasyn://corpus/73639)
- A method for generating synthetic longitudinal health data. [metasyn://corpus/73343](metasyn://corpus/73343)
- Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer. [metasyn://corpus/73473](metasyn://corpus/73473)
- An evaluation of the replicability of analyses using synthetic health data. [metasyn://corpus/4841](metasyn://corpus/4841)
- Application of Bayesian networks to generate synthetic health data. [metasyn://corpus/4850](metasyn://corpus/4850)
- Comprehensive evaluation framework for synthetic tabular data in health: fidelity, utility and privacy analysis of generative models with and without privacy guarantees. [metasyn://corpus/73641](metasyn://corpus/73641)
- Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation. [metasyn://corpus/4849](metasyn://corpus/4849)
- DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations. [metasyn://corpus/4868](metasyn://corpus/4868)
- Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility. [metasyn://corpus/4861](metasyn://corpus/4861)
- Membership inference attacks against synthetic health data. [metasyn://corpus/4867](metasyn://corpus/4867)
- Spot the difference: comparing results of analyses from real patient data and synthetic derivatives. [metasyn://corpus/4845](metasyn://corpus/4845)
- Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results. [metasyn://corpus/4851](metasyn://corpus/4851)
- Synthetic data generation methods for longitudinal and time series health data: a systematic review. [metasyn://corpus/57829](metasyn://corpus/57829)
- Synthetic electronic health records generated with variational graph autoencoders. [metasyn://corpus/4982](metasyn://corpus/4982)
- Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions. [metasyn://corpus/4863](metasyn://corpus/4863)
