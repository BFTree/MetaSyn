### Evidence Synthesis Report: Evaluation of Privacy and Utility in Synthetic Health Data

#### Overview of Included Studies
Based on the screening criteria (publications from 2018 to July 2024, evaluating outputs of synthetic data generation methods for health-related data, excluding reviews, unstructured image/text data, and non-English documents), 39 primary studies were included. The studies predominantly evaluated tabular or structured longitudinal electronic health records (EHRs), administrative claims, clinical trial data, and time-series physiological signals (e.g., ECG, PPG). 

#### Consensus on Standardized Evaluation Methods
There is currently **no consensus** within the research community on a single, standardized method or framework for evaluating synthetic health data. While the dimensions of evaluation are consistently recognized—typically categorized as resemblance/fidelity, utility, and privacy—the specific metrics chosen within each dimension vary widely across studies. A few studies propose comprehensive evaluation pipelines (e.g., Candidate 001 suggests orchestrating metrics into categories of "Excellent," "Good," and "Poor"; Candidate 013 proposes a replicability framework), but these are individual proposals rather than community-adopted standards. The heterogeneity in metrics makes cross-study comparison difficult and prevents a unified benchmarking standard.

#### Methods and Metrics for Utility Assessment
Utility assessment is universally conducted and is the primary focus of most synthetic data generation studies. The metrics fall into three main categories:
1. **Statistical Similarity/Fidelity**: Common metrics include Hellinger distance, Wasserstein distance, correlation matrix differences, propensity score mean-squared error (pMSE), and standardized differences. These measure how well the synthetic data reproduces the marginal and joint distributions of the real data.
2. **Downstream Machine Learning Performance**: The "Train on Synthetic, Test on Real" (TSTR) approach is highly prevalent. Utility is measured by comparing the performance (AUROC, AUC, accuracy, F1-score) of predictive models (e.g., Random Forests, XGBoost, neural networks) trained on synthetic data versus real data.
3. **Analytical Replicability**: Several studies evaluate whether the synthetic data replicates the results of regression analyses, hazard ratios, or epidemiological trends observed in the real data, using metrics like confidence interval overlap and agreement in effect direction (e.g., Candidates 013, 085, 086).

#### Methods and Metrics for Privacy Assessment
Privacy evaluation practices are significantly less standardized than utility practices and are often less rigorously applied. The included studies utilize several distinct approaches:
1. **Membership Inference Attacks (MIA)**: Simulating adversaries who attempt to determine if a specific individual's data was used in the training set (e.g., Candidates 064, 012). This is emerging as a robust empirical privacy metric, though implementations and thresholds vary.
2. **Identity and Attribute Disclosure Risk**: Calculating the probability that an adversary can link a synthetic record to a real individual or learn new sensitive attributes. Metrics include distance to closest record (DCR), epsilon-identifiability, and meaningful identity disclosure risk (e.g., Candidates 053, 056).
3. **Differential Privacy (DP) Guarantees**: Several frameworks generate data with formal DP guarantees (specifying an epsilon budget) and treat the DP bound itself as the privacy evaluation (e.g., Candidates 011, 041, 044).
4. **Basic Heuristics**: Some studies rely on simpler checks, such as verifying the absence of exact duplicate rows between real and synthetic datasets (Candidate 014) or measuring classification performance in distinguishing real from synthetic records (Candidate 054).

#### Balance Between Privacy and Utility
**Privacy considerations are frequently not given equal importance relative to utility.** While every included study evaluated utility, a subset either omitted rigorous privacy metrics entirely (evaluating privacy only in terms of general "preservation" without quantifiable risk) or focused solely on utility (e.g., Candidates 030, 039, 091, 114, 158, 183). 
When both are evaluated, a trade-off is consistently reported: methods that maximize utility and fidelity (such as complex GANs) often exhibit higher privacy risks (e.g., vulnerability to membership inference), whereas methods with strong privacy guarantees (like differential privacy or heavy suppression) often suffer a loss in utility or fidelity (e.g., Candidates 011, 056). Several studies highlight that optimizing for privacy is the most challenging aspect of synthesis, often resulting in a secondary compromise rather than a co-equal design objective. Studies focused on adversarial privacy attacks (Candidate 064) demonstrate that high-utility synthetic data can leak substantial membership information, further indicating that utility is often prioritized at the expense of robust privacy protection.

#### Gaps in Privacy Evaluation Practices
- **Inconsistency**: There is no universal threshold for "acceptable" privacy risk; studies use differing baselines (e.g., a 0.09 risk threshold vs. epsilon-identifiability vs. MIA accuracy).
- **Lack of Empirical Attacks**: Many studies rely on distance-based metrics (DCR) rather than realistic adversarial attacks like MIA, which may overestimate privacy protection.
- **Under-exploration of Privacy-Utility Trade-offs**: Few studies systematically vary privacy parameters (like epsilon) to map the explicit trade-off curve, often treating privacy as a binary "safe/unsafe" post-hoc check.

---

### Included Primary-Study Articles

*   **Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.** Corpus ID: 4863
*   **Evaluating the utility of synthetic COVID-19 case data.** Corpus ID: 4843
*   **Generating Synthetic Health Sensor Data for Privacy-Preserving Wearable Stress Detection.** Corpus ID: 73555
*   **A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.** Corpus ID: 4835
*   **An evaluation of the replicability of analyses using synthetic health data.** Corpus ID: 4841
*   **Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.** Corpus ID: 4838
*   **Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.** Corpus ID: 4847
*   **A method for generating synthetic longitudinal health data.** Corpus ID: 73343
*   **Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation.** Corpus ID: 4849
*   **Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.** Corpus ID: 73473
*   **Using Synthetic Data to Replace Linkage Derived Elements: A Case Study.** Corpus ID: 4859
*   **The Problem of Fairness in Synthetic Healthcare Data.** Corpus ID: 4837
*   **Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.** Corpus ID: 4861
*   **Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.** Corpus ID: 73374
*   **Prediction of Tuberculosis Using an Automated Machine Learning Platform for Models Trained on Synthetic Data.** Corpus ID: 4858
*   **Collaborative learning from distributed data with differentially private synthetic data.** Corpus ID: 4857
*   **Synthetic Data Improve Survival Status Prediction Models in Early-Onset Colorectal Cancer.** Corpus ID: 4862
*   **Leveraging VQ-VAE tokenization for autoregressive modeling of medical time series.** Corpus ID: 75054
*   **Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.** Corpus ID: 4842
*   **Application of Bayesian networks to generate synthetic health data.** Corpus ID: 4850
*   **Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.** Corpus ID: 4860
*   **Synthesize Extremely High-dimensional Longitudinal Electronic Health Records via Hierarchical Autoregressive Language mOdel.** Corpus ID: 113332
*   **Membership inference attacks against synthetic health data.** Corpus ID: 4867
*   **Synthetic electronic health records generated with variational graph autoencoders.** Corpus ID: 4982
*   **Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.** Corpus ID: 4851
*   **Generating synthetic data from administrative health records for drug safety and effectiveness studies.** Corpus ID: 4834
*   **Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications.** Corpus ID: 75141
*   **DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations.** Corpus ID: 4868
*   **Demonstrating an approach for evaluating synthetic geospatial and temporal epidemiologic data utility: Results from analyzing >1.8 million SARS-CoV-2 tests in the United States National COVID Cohort Collaborative (N3C).** Corpus ID: 73632
*   **Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.** Corpus ID: 4845
*   **Demonstrating an approach for evaluating synthetic geospatial and temporal epidemiologic data utility: results from analyzing >1.8 million SARS-CoV-2 tests in the United States National COVID Cohort Collaborative (N3C).** Corpus ID: 73631
*   **Semantic representation and comparative analysis of physical activity sensor observations using MOX2-5 sensor in real and synthetic datasets: a proof-of-concept-study.** Corpus ID: 73521
*   **Synthesize high-dimensional longitudinal electronic health records via hierarchical autoregressive language model.** Corpus ID: 4986
*   **Characterization of Synthetic Health Data Using Rule-Based Artificial Intelligence Models.** Corpus ID: 4840
*   **Diffusion-based conditional ECG generation with structured state space models.** Corpus ID: 4983
*   **Generating synthetic clinical data that capture class imbalanced distributions with generative adversarial networks: Example using antiretroviral therapy for HIV.** Corpus ID: 73400
*   **Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.** Corpus ID: 4846
*   **A multicenter random forest model for effective prognosis prediction in collaborative clinical research network.** Corpus ID: 73559
*   **PlethAugment: GAN-Based PPG Augmentation for Medical Diagnosis in Low-Resource Settings.** Corpus ID: 4985
*   **Synthesizing time-series wound prognosis factors from electronic medical records using generative adversarial networks.** Corpus ID: 4984
