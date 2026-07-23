# Evidence Synthesis Report: Evaluation of Privacy and Utility in Synthetic Health Data

## 1. Scope and Screening Summary

This scoping review targeted primary studies that generate synthetic health-related data and evaluate their outputs (specifically utility and/or privacy), published between January 1, 2018, and July 31, 2024. Studies using unstructured data (images/text), reviews, and non-English documents were excluded.

From the supplied candidate pool of 200 articles, 35 primary studies met all inclusion criteria. The primary reasons for exclusion were: publication year outside the eligible range (especially 2025+ publications), use of unstructured image/text data (e.g., neuroimaging, clinical notes, medical imaging GANs), being reviews/surveys rather than primary research, or lacking an explicit evaluation of the synthetic data's utility or privacy aspects.

## 2. Synthesis of Findings

### 2.1 Consensus on Standardized Evaluation Methods
The reviewed literature indicates **no prevailing consensus** on a single, standardized set of methods or metrics for evaluating synthetic health data. Several authors explicitly acknowledge this gap:

*   **Lack of Standardization:** Multiple studies frame their work as a direct response to the absence of standardized benchmarks. For instance, one study notes a "lack of standardized and objective evaluation and benchmarking strategy" in the health domain and proposes an orchestrated pipeline covering resemblance, utility, and privacy (Candidate 002). Another highlights that traditional statistical similarity metrics overlook critical shortcomings like out-of-range values and duplicate row amplification, proposing a broader multi-dimensional framework instead (Candidate 020).
*   **Heterogeneity in Metrics:** When evaluating **utility**, approaches vary significantly. Common strategies include statistical similarity tests (e.g., Hellinger distance, Wasserstein distance, correlation differences), machine learning predictive performance comparisons (e.g., "Train on Synthetic, Test on Real" [TSTR], AUROC, F1-scores), and the replicability of regression coefficients or hazard ratios on synthetic versus real datasets. When evaluating **privacy**, the landscape is even more fragmented: metrics range from membership inference attacks (MIA) and identity disclosure risk models to distance-based metrics (e.g., Distance to Closest Record) and epsilon-identifiability.

### 2.2 Balance Between Privacy and Utility Assessment
The review reveals a **disparity in the rigorous assessment of privacy relative to utility**. While utility is universally evaluated across all included studies, explicit privacy risk quantification is only present in a subset.

*   **Utility as the Primary Focus:** Approximately half of the studies evaluate utility metrics extensively while treating privacy as an implicit property of the generation process (e.g., asserting that synthetic data has "no one-to-one correspondence" with real data) without quantifying the re-identification risk. These studies prioritize demonstrating that synthetic data can maintain statistical properties, support downstream ML tasks, or replicate clinical analyses (e.g., Candidates 038, 086, 147, 159, 181, 186).
*   **Quantitative Privacy Assessment:** The studies that do quantify privacy often employ bespoke threat models, such as meaningful identity disclosure (Candidate 005), specific MIA frameworks (Candidates 006, 007, 137), or distance-based concealment metrics (Candidate 021). Among these, differential privacy (DP) is increasingly used as a formal guarantee, though its impact on utility is frequently tested.
*   **The Privacy-Utility Trade-off:** Studies that assess both dimensions consistently report a trade-off. The addition of differential privacy mechanisms or stronger privacy constraints generally enhances privacy preservation but reduces fidelity and utility (Candidates 002, 068). However, some specific generative models and configurations demonstrate that high utility and low privacy risk can coexist, reporting low membership disclosure risks alongside high analytical replicability (Candidates 053, 011, 060).

**Conclusion:** The research community has not yet converged on a standardized evaluation methodology for synthetic health data. Utility evaluation is consistently prioritized and more uniformly assessed, whereas privacy evaluation practices are inconsistent, often less rigorous, or omitted entirely in favor of qualitative claims. Where both are assessed, a tension between privacy guarantees and data utility is a recurring finding, underscoring the need for standardized frameworks that holistically balance both dimensions.

***

## 3. Included Primary Studies

1.  **Candidate 002** | Corpus ID: 4863
    *Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.*

2.  **Candidate 005** | Corpus ID: 4842
    *Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.*

3.  **Candidate 006** | Corpus ID: 4867
    *Membership inference attacks against synthetic health data.*

4.  **Candidate 007** | Corpus ID: 4841
    *An evaluation of the replicability of analyses using synthetic health data.*

5.  **Candidate 009** | Corpus ID: 4838
    *Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.*

6.  **Candidate 011** | Corpus ID: 73343
    *A method for generating synthetic longitudinal health data.*

7.  **Candidate 012** | Corpus ID: 4847
    *Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.*

8.  **Candidate 013** | Corpus ID: 4835
    *A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.*

9.  **Candidate 016** | Corpus ID: 4850
    *Application of Bayesian networks to generate synthetic health data.*

10. **Candidate 017** | Corpus ID: 4868
    *DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations.*

11. **Candidate 019** | Corpus ID: 72223
    *Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.*

12. **Candidate 020** | Corpus ID: 4849
    *Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation.*

13. **Candidate 021** | Corpus ID: 73473
    *Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.*

14. **Candidate 024** | Corpus ID: 4837
    *The Problem of Fairness in Synthetic Healthcare Data.*

15. **Candidate 028** | Corpus ID: 4845
    *Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.*

16. **Candidate 035** | Corpus ID: 4859
    *Using Synthetic Data to Replace Linkage Derived Elements: A Case Study.*

17. **Candidate 037** | Corpus ID: 4861
    *Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.*

18. **Candidate 038** | Corpus ID: 4848
    *Generating Enriched Synthetic German Hospital Claims Data - A Use Case Driven Approach.*

19. **Candidate 040** | Corpus ID: 4851
    *Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.*

20. **Candidate 044** | Corpus ID: 4857
    *Collaborative learning from distributed data with differentially private synthetic data.*

21. **Candidate 046** | Corpus ID: 4982
    *Synthetic electronic health records generated with variational graph autoencoders.*

22. **Candidate 050** | Corpus ID: 4862
    *Synthetic Data Improve Survival Status Prediction Models in Early-Onset Colorectal Cancer.*

23. **Candidate 053** | Corpus ID: 4843
    *Evaluating the utility of synthetic COVID-19 case data.*

24. **Candidate 060** | Corpus ID: 4860
    *Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.*

25. **Candidate 068** | Corpus ID: 73555
    *Generating Synthetic Health Sensor Data for Privacy-Preserving Wearable Stress Detection.*

26. **Candidate 078** | Corpus ID: 75141
    *Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications.*

27. **Candidate 086** | Corpus ID: 4834
    *Generating synthetic data from administrative health records for drug safety and effectiveness studies.*

28. **Candidate 092** | Corpus ID: 4840
    *Characterization of Synthetic Health Data Using Rule-Based Artificial Intelligence Models.*

29. **Candidate 103** | Corpus ID: 4981
    *Diffusion-based conditional ECG generation with structured state space models.*

30. **Candidate 135** | Corpus ID: 73559
    *A multicenter random forest model for effective prognosis prediction in collaborative clinical research network.*

31. **Candidate 137** | Corpus ID: 75054
    *Leveraging VQ-VAE tokenization for autoregressive modeling of medical time series.*

32. **Candidate 147** | Corpus ID: 4846
    *Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.*

33. **Candidate 159** | Corpus ID: 4858
    *Prediction of Tuberculosis Using an Automated Machine Learning Platform for Models Trained on Synthetic Data.*

34. **Candidate 181** | Corpus ID: 75142
    *Synthesize Extremely High-dimensional Longitudinal Electronic Health Records via Hierarchical Autoregressive Language Model.*

35. **Candidate 186** | Corpus ID: 4986
    *Synthesize high-dimensional longitudinal electronic health records via hierarchical autoregressive language model.*
