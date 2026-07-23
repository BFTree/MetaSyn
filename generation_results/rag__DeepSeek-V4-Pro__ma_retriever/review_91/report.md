# Evidence Synthesis Report: Standardized Methods for Evaluating Privacy and Utility of Synthetic Health Data

## 1. Introduction
This scoping review examines the research landscape from January 2018 to July 2024 to determine whether consensus exists on standardized methods for evaluating the privacy and utility of synthetic health-related data. A secondary objective is to assess whether privacy considerations receive equal importance relative to utility in the evaluation of synthetic medical data. The review analyzes primary studies that both generate synthetic health data and evaluate the resulting outputs.

## 2. Methods
From a fixed pool of 200 candidates, titles and abstracts were screened against predefined inclusion and exclusion criteria. Inclusion required studies describing synthetic data generation methods for health-related data and evaluating the outputs. Studies were excluded if they were reviews, non-English, lacked utility/privacy assessments, used unstructured data (images/text), were poster abstracts, or fell outside the 2018–2024 publication window.

A total of **35 primary studies** met all criteria and were included in the synthesis (see Section 5 for the complete list).

## 3. Results

### 3.1 Characteristics of Included Studies
The 35 included studies span 2020 to 2024, reflecting a rapidly growing field. Data types evaluated include:
- Electronic health records (EHRs) and administrative claims (e.g., candidates 011, 017, 020, 046, 078, 086, 181, 186)
- Clinical trial data (e.g., candidates 012, 019, 060)
- Disease-specific registries (e.g., candidates 037, 050, 053, 135, 159)
- Longitudinal and time-series health data (e.g., candidates 011, 020, 040, 078, 103, 137)
- Wearable sensor data (e.g., candidate 068)

Generative models employed include GANs, VAEs, Bayesian networks, sequential synthesis, diffusion models, and autoregressive language models, with some studies incorporating differential privacy (DP) guarantees.

### 3.2 Evaluation of Utility
Utility assessment is a near-universal component of the included studies. However, the specific metrics and approaches vary considerably:

- **Statistical fidelity** is the most common approach, using comparisons of marginal distributions, bivariate correlations, and propensity score metrics (e.g., candidates 002, 003, 011, 040, 121).
- **Machine learning utility** (Train-on-Synthetic, Test-on-Real, or TSTR) is frequently employed to assess whether models trained on synthetic data achieve comparable performance to those trained on real data (e.g., candidates 007, 022, 050, 053, 076, 092, 159).
- **Replicability of analyses** (e.g., regression coefficients, hazard ratios, confidence interval overlap) is another key utility dimension, particularly for clinical research workloads (e.g., candidates 007, 009, 013, 028, 035).
- **Domain-specific clinical validity** checks, such as rule-based constraints or outlier detection, are less common but appear in some framework-oriented studies (e.g., candidates 004, 092).

Despite the diversity, no single utility metric or set of metrics has been universally adopted. The field lacks a standardized benchmark or evaluation protocol.

### 3.3 Evaluation of Privacy
Privacy evaluation is present in the majority of included studies, but the depth and rigor vary widely:

- **Membership inference attacks (MIAs)** are a frequently used privacy metric, assessing whether an adversary can determine if a specific record was used in training (e.g., candidates 006, 007, 013, 034).
- **Identity disclosure risk** (e.g., meaningful identity disclosure, re-identification risk) is evaluated in several studies, often using distance-based metrics or matching against holdout datasets (e.g., candidates 003, 005, 011, 017, 035).
- **Attribute disclosure risk** and **differential privacy (DP) budgets** are reported in studies that explicitly integrate DP mechanisms (e.g., candidates 010, 022, 044, 050, 068).
- Some studies propose **privacy risk frameworks** that combine multiple measures (e.g., candidates 002, 005, 034), while others rely on simpler heuristics such as the absence of exact duplicates or the Hellinger distance between real and synthetic distributions (e.g., candidates 009, 016).

Crucially, several studies note that privacy evaluation is often incomplete, ad-hoc, or absent. For example, candidate 018 (a systematic review, excluded) reports that only 30% of studies in its sample included any privacy metric, and candidate 002 explicitly states a “lack of standardized and objective evaluation and benchmarking strategy.” This observation is consistent with the primary studies included here: privacy assessment is not uniformly applied, and the choice of metrics lacks standardization.

### 3.4 Balance between Privacy and Utility
A recurring theme across the included studies is the **trade-off between privacy and utility**. Studies that incorporate differential privacy or other formal privacy guarantees consistently report a degradation in utility (e.g., candidates 001, 010, 022, 044, 050, 068). However, the assessment of this trade-off is often qualitative, and only a few studies (e.g., candidates 002, 003, 022) propose explicit trade-off metrics or frameworks.

The evidence suggests that **utility is more frequently and systematically evaluated than privacy**. Many studies emphasize fidelity and downstream task performance, while privacy is assessed as a secondary or supplementary concern. For instance, candidate 022 notes that “marginal-based synthetic data generators surpass GAN-based ones regarding model training utility,” but the fairness and privacy analysis is presented as an additional layer. Candidate 018 (excluded review) confirms that privacy assessments are “sparse and inconsistently reported.”

### 3.5 Consensus on Evaluation Methods
The included studies reveal **no consensus on a standardized evaluation methodology**. While several studies propose comprehensive frameworks (e.g., candidates 002, 004, 020, 022), these frameworks differ in their dimensions, metrics, and aggregation methods. The field remains fragmented, with researchers selecting metrics based on the specific generative model, data type, and application domain. This fragmentation hinders comparability and benchmarking across studies.

## 4. Discussion
The findings of this scoping review indicate that, while the evaluation of synthetic health data is an active and maturing research area, three critical gaps persist:

1. **Lack of standardization**: There is no agreed-upon set of metrics or evaluation protocols for either utility or privacy. The heterogeneity of approaches limits the ability to compare results across studies and to build cumulative knowledge.

2. **Imbalanced attention to privacy**: Privacy evaluation is often less rigorous and less consistently applied than utility evaluation. The privacy–utility trade-off is acknowledged but seldom quantified in a systematic way, and privacy is rarely treated as an equally weighted dimension in the assessment of synthetic data quality.

3. **Limited real-world clinical validation**: Most utility assessments are based on statistical similarity or machine learning performance, with few studies involving clinician-led evaluations or testing in real clinical workflows.

These gaps highlight the need for community-driven efforts to develop standardized benchmarks, privacy metrics, and reporting guidelines that ensure synthetic health data is evaluated holistically and transparently.

## 5. Included Primary Studies

The following 35 articles met all inclusion criteria and form the evidence base for this synthesis.

1. **Candidate 002**  
   Corpus ID: 4863  
   Title: Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.

2. **Candidate 003**  
   Corpus ID: 4856  
   Title: Holdout-Based Empirical Assessment of Mixed-Type Synthetic Data.

3. **Candidate 005**  
   Corpus ID: 4842  
   Title: Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.

4. **Candidate 006**  
   Corpus ID: 4867  
   Title: Membership inference attacks against synthetic health data.

5. **Candidate 007**  
   Corpus ID: 4841  
   Title: An evaluation of the replicability of analyses using synthetic health data.

6. **Candidate 009**  
   Corpus ID: 4838  
   Title: Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.

7. **Candidate 011**  
   Corpus ID: 73343  
   Title: A method for generating synthetic longitudinal health data.

8. **Candidate 012**  
   Corpus ID: 4847  
   Title: Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.

9. **Candidate 013**  
   Corpus ID: 4835  
   Title: A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.

10. **Candidate 016**  
    Corpus ID: 4850  
    Title: Application of Bayesian networks to generate synthetic health data.

11. **Candidate 017**  
    Corpus ID: 4868  
    Title: DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations.

12. **Candidate 019**  
    Corpus ID: 73374  
    Title: Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.

13. **Candidate 020**  
    Corpus ID: 4849  
    Title: Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation.

14. **Candidate 021**  
    Corpus ID: 73473  
    Title: Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.

15. **Candidate 022**  
    Corpus ID: 4855  
    Title: Assessment of differentially private synthetic data for utility and fairness in end-to-end machine learning pipelines for tabular data.

16. **Candidate 028**  
    Corpus ID: 4845  
    Title: Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.

17. **Candidate 035**  
    Corpus ID: 4859  
    Title: Using Synthetic Data to Replace Linkage Derived Elements: A Case Study.

18. **Candidate 037**  
    Corpus ID: 4861  
    Title: Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.

19. **Candidate 038**  
    Corpus ID: 4848  
    Title: Generating Enriched Synthetic German Hospital Claims Data - A Use Case Driven Approach.

20. **Candidate 040**  
    Corpus ID: 4851  
    Title: Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.

21. **Candidate 044**  
    Corpus ID: 4857  
    Title: Collaborative learning from distributed data with differentially private synthetic data.

22. **Candidate 046**  
    Corpus ID: 4982  
    Title: Synthetic electronic health records generated with variational graph autoencoders.

23. **Candidate 050**  
    Corpus ID: 4862  
    Title: Synthetic Data Improve Survival Status Prediction Models in Early-Onset Colorectal Cancer.

24. **Candidate 053**  
    Corpus ID: 4843  
    Title: Evaluating the utility of synthetic COVID-19 case data.

25. **Candidate 060**  
    Corpus ID: 4860  
    Title: Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.

26. **Candidate 068**  
    Corpus ID: 73555  
    Title: Generating Synthetic Health Sensor Data for Privacy-Preserving Wearable Stress Detection.

27. **Candidate 078**  
    Corpus ID: 75141  
    Title: Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications.

28. **Candidate 086**  
    Corpus ID: 4834  
    Title: Generating synthetic data from administrative health records for drug safety and effectiveness studies.

29. **Candidate 092**  
    Corpus ID: 4840  
    Title: Characterization of Synthetic Health Data Using Rule-Based Artificial Intelligence Models.

30. **Candidate 103**  
    Corpus ID: 4983  
    Title: Diffusion-based conditional ECG generation with structured state space models.

31. **Candidate 135**  
    Corpus ID: 73559  
    Title: A multicenter random forest model for effective prognosis prediction in collaborative clinical research network.

32. **Candidate 137**  
    Corpus ID: 75054  
    Title: Leveraging VQ-VAE tokenization for autoregressive modeling of medical time series.

33. **Candidate 147**  
    Corpus ID: 4846  
    Title: Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.

34. **Candidate 159**  
    Corpus ID: 4858  
    Title: Prediction of Tuberculosis Using an Automated Machine Learning Platform for Models Trained on Synthetic Data.

35. **Candidate 181**  
    Corpus ID: 75142  
    Title: Synthesize Extremely High-dimensional Longitudinal Electronic Health Records via Hierarchical Autoregressive Language Model.

36. **Candidate 186**  
    Corpus ID: 4986  
    Title: Synthesize high-dimensional longitudinal electronic health records via hierarchical autoregressive language model.

(Note: Candidates 181 and 186 appear to describe the same underlying study; both are included as they were listed separately in the candidate pool.)
