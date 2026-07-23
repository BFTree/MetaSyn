# Evidence Synthesis Report: Evaluation Methods for Privacy and Utility of Synthetic Health Data

## 1. Overview
This scoping review examined 200 candidate articles to determine whether there is consensus on standardized methods for evaluating the privacy and utility of synthetic health-related data, and whether privacy considerations are given equal importance to utility. After screening against the inclusion and exclusion criteria (focusing on primary studies evaluating synthetic data outputs within the 2018–2024 window, and excluding reviews, protocols, non-English works, and unstructured data applications), 27 primary studies were identified for synthesis.

## 2. Evaluation Methods for Utility
Utility evaluation methods are diverse but generally cluster into three main approaches:
*   **General Fidelity and Resemblance:** Several studies assess how well synthetic data mirrors the statistical properties of the real data. Common metrics include Hellinger distance (013, 077), Wasserstein distance (059), propensity score mean squared error (pMSE) (054), correlation differences (077), and comparisons of marginal/joint distributions (007, 044, 162).
*   **Replicability of Analyses:** A prominent approach evaluates whether analyses conducted on synthetic data yield results comparable to those from the real data. This involves comparing regression coefficients, hazard ratios, confidence interval overlap (001, 003, 004, 011, 013, 016, 037, 064, 115, 143), concordance coefficients (037), and statistical significance or P-values (009).
*   **Predictive/Machine Learning Performance:** The "Train on Synthetic, Test on Real" (TSTR) paradigm is frequently used to evaluate utility for downstream AI tasks. Metrics include AUC, c-statistics, accuracy, and F1-scores (010, 028, 055, 070, 077, 162).
*   **Fairness and Subgroup Representation:** Emerging utility evaluations focus on fairness, using covariate-level disparity metrics to ensure synthetic data represents minority subgroups adequately (005, 055, 146).

## 3. Evaluation Methods for Privacy
Privacy evaluation methods are less convergent and often tailored to specific disclosure risks:
*   **Membership Disclosure/Inference Attacks:** The most common privacy metric involves simulating adversaries attempting to determine if a real individual's data was used to train the generator. Metrics include membership inference attack accuracy or F1 score (001, 016, 020, 028, 077, 162) and contrastive representation learning frameworks (020).
*   **Identity and Attribute Disclosure:** Some studies assess the risk of identifying individuals or learning new attributes from synthetic records. This includes "meaningful identity disclosure risk" models (006), ϵ-identifiability metrics (059), re-identification probabilities (115, 143), and attribution disclosure risk (013, 028).
*   **Distance-Based Metrics:** Privacy is assessed by measuring the distance between synthetic records and the closest real records, ensuring synthetic records are not too similar to any specific real individual (004, 054).
*   **Basic Privacy Checks:** Simple checks for exact duplicate rows (003) or one-to-one links (044) are also employed.
*   **Differential Privacy Mechanisms:** Some studies rely on differential privacy (DP) as a formal privacy guarantee rather than empirical output evaluation (036, 055), though 055 also assesses fairness trade-offs.

## 4. Consensus on Standardized Methods
There is **no consensus** on a standardized evaluation framework for synthetic health data. Several included studies explicitly note this gap; for instance, 007 states there is a "lack of standardized and objective evaluation and benchmarking strategy" and proposes its own orchestrated pipeline. Similarly, 006 develops a bespoke "meaningful identity disclosure risk model," 020 introduces a novel membership inference framework, 054 proposes a holdout-based empirical assessment framework, and 055 presents a training/evaluation framework for utility and fairness. While utility evaluation practices are somewhat convergent around replicability and TSTR, privacy evaluation remains fragmented across various bespoke attack models and risk thresholds (e.g., the 0.09 threshold used in 013 and 028).

## 5. Balance Between Privacy and Utility Assessment
Privacy considerations are **not given equal importance** to utility in the assessment of synthetic medical data:
*   **Omission of Privacy Metrics:** Several studies evaluate synthetic data solely on utility dimensions (replicability, ML performance, statistical resemblance) without reporting any empirical privacy metrics (009, 011, 037, 064, 070, 146). This suggests utility is often the primary, and sometimes only, driver of validation.
*   **Asymmetry in Metric Depth:** Even in studies evaluating both, utility is typically assessed across multiple dimensions (resemblance, replicability, predictive performance) with numerous metrics, whereas privacy is often reduced to a single summary metric or threshold (e.g., a membership F1 score or a binary "low risk" statement in 001, 016, 028).
*   **Trade-off Dynamics:** Studies that rigorously evaluate both often reveal a trade-off where higher utility/fidelity correlates with increased privacy risk. For example, 010 notes that larger synthetic sample sizes increase veracity but generally increase privacy risks; 054 and 077 similarly highlight that synthetic records close to real data pose higher disclosure risks. Privacy is frequently treated as a constraint to be minimized below an acceptable threshold rather than a property optimized in tandem with utility.

## 6. Identified Gaps
*   **Lack of Standardization:** The field lacks a universally adopted evaluation pipeline, leading to incomparable results across studies.
*   **Privacy Evaluation Depth:** Privacy assessments are often limited to specific attack scenarios (like membership inference) and do not comprehensively cover all disclosure risks (identity, attribute, inference).
*   **Fairness Integration:** While fairness is recognized as important (005), it is not yet a standard component of utility/privacy evaluation frameworks.
*   **Empirical Validation of DP Trade-offs:** Although differential privacy is used, empirical evaluation of the utility/privacy trade-off under varying DP budgets is limited (055).

---

## Included Primary Studies

1.  An evaluation of the replicability of analyses using synthetic health data. (Corpus ID: 4841)
2.  Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology. (Corpus ID: 4838)
3.  Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis. (Corpus ID: 4847)
4.  The Problem of Fairness in Synthetic Healthcare Data. (Corpus ID: 4837)
5.  Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation. (Corpus ID: 4842)
6.  Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions. (Corpus ID: 4863)
7.  Spot the difference: comparing results of analyses from real patient data and synthetic derivatives. (Corpus ID: 4845)
8.  Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer. (Corpus ID: 73473)
9.  Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results. (Corpus ID: 4851)
10. A method for generating synthetic longitudinal health data. (Corpus ID: 73343)
11. A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health. (Corpus ID: 4835)
12. Membership inference attacks against synthetic health data. (Corpus ID: 4867)
13. Evaluating the utility of synthetic COVID-19 case data. (Corpus ID: 4843)
14. Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis. (Corpus ID: 73374)
15. Collaborative learning from distributed data with differentially private synthetic data. (Corpus ID: 4857)
16. Generating synthetic data from administrative health records for drug safety and effectiveness studies. (Corpus ID: 4834)
17. Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation. (Corpus ID: 4849)
18. Holdout-Based Empirical Assessment of Mixed-Type Synthetic Data. (Corpus ID: 4856)
19. Assessment of differentially private synthetic data for utility and fairness in end-to-end machine learning pipelines for tabular data. (Corpus ID: 4855)
20. Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments. (Corpus ID: 4860)
21. Using Synthetic Data to Replace Linkage Derived Elements: A Case Study. (Corpus ID: 4859)
22. Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research. (Corpus ID: 4846)
23. Synthetic Data Improve Survival Status Prediction Models in Early-Onset Colorectal Cancer. (Corpus ID: 4862)
24. Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility. (Corpus ID: 4861)
25. DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations. (Corpus ID: 4868)
26. An evaluation of synthetic data augmentation for mitigating covariate bias in health data. (Corpus ID: 4836)
27. Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications. (Corpus ID: 75141)
