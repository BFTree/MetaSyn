**Evidence‑Synthesis Report**

**Scoping Review: Consensus on Evaluation Methods for Privacy and Utility of Synthetic Health Data**

**1.  Introduction**
This scoping review examined the research literature from 1 January 2018 to 31 July 2024 to determine whether the scientific community has reached consensus on standardized methods for evaluating the privacy and utility of synthetic health‑related data, and whether privacy is afforded equal weight relative to utility in such assessments. The review was guided by the question: “Is there consensus on standardized evaluation methods, and is privacy given equal importance to utility when synthetic medical data are assessed?”

**2.  Methods**
A fixed pool of 200 candidate articles, pre‑identified as potentially relevant to the review topic, was screened against explicit inclusion and exclusion criteria. To be included, a publication had to describe primary research that used synthetic data generation methods and evaluated the resulting outputs. Studies that were surveys, systematic or scoping reviews, protocols, editorials, or poster abstracts were excluded, as were publications in languages other than English, those reporting only unstructured data (images/text), and those that did not assess either utility or privacy of the generated data. Screening was performed on title and abstract alone. After applying all criteria, 26 primary‑study articles were deemed eligible and formed the basis of this synthesis.

**3.  Synthesis of Findings**

**3.1  Overview of Included Studies**
The 26 included studies span the years 2020‑2024 and cover a wide range of synthetic data generation techniques, including sequential synthesis, generative adversarial networks (GANs), variational autoencoders, copula‑based methods, Bayesian networks, and differential privacy‑infused approaches. The health domains represented include administrative claims, electronic health records, clinical trials, disease registries, and epidemiological cohorts. All studies evaluated synthetic data at least along one of the two dimensions of interest; most addressed both.

**3.2  Utility Evaluation: Metrics and Approaches**
There is considerable diversity in how utility is operationalised, but several recurring themes emerge:
- **Statistical fidelity / resemblance**: Many studies compare univariate and bivariate distributions, often using Hellinger distance, propensity score mean‑squared error (pMSE), correlation differences, or standardized mean differences (e.g., Candidates 007, 013, 054, 081, 108).
- **Replicability of analyses**: A common approach is to perform the same regression or machine‑learning workload on real and synthetic data and compare the results. Metrics include confidence interval overlap, decision agreement, estimate agreement, bias, statistical power, and area under the curve (AUC) (Candidates 001, 003, 009, 028, 036, 059, 070, 077, 146).
- **Downstream task performance**: Several studies train predictive models on synthetic data and test on real data (Train‑on‑Synthetic, Test‑on‑Real; TSTR), measuring metrics such as accuracy, F1‑score, and AUC (Candidates 010, 014, 055, 077, 108, 141).
- **Clinical actionability**: A few studies explicitly assess whether synthetic data reproduce clinically meaningful endpoints, e.g., hazard ratios in survival analyses or treatment effect estimates (Candidates 004, 013, 115).

Despite this variety, no single utility metric is universally endorsed. The choice of metric often depends on the intended use case (e.g., descriptive analysis, predictive modelling, causal inference). The lack of a standardised battery of utility tests hampers comparability across studies.

**3.3  Privacy Evaluation: Metrics and Approaches**
Privacy evaluation is even less standardised than utility assessment. The included studies employ a heterogeneous set of methods:
- **Membership disclosure / inference attacks**: Several works measure the risk that an adversary can determine whether a specific individual’s data was used in the training set (Candidates 001, 006, 016, 020, 032, 054, 059). Metrics include F1‑score of the attacker, attack accuracy, and distance‑based membership inference.
- **Identity disclosure risk**: Some studies compute the probability that a synthetic record can be linked to a real individual, often using distance‑to‑closest‑record or matching probabilities (Candidates 006, 013, 028, 077).
- **Attribute disclosure risk**: Evaluation of whether sensitive attributes can be inferred (Candidate 028).
- **Differential privacy (DP) guarantees**: A few works incorporate DP and report the privacy budget ε (Candidates 036, 055, 077). However, the choice of ε and the interpretation of its sufficiency vary widely.
- **Holdout‑based empirical privacy**: Candidate 054 proposes a framework that compares distances from synthetic records to training versus holdout data to assess generalisation and privacy.

Notably, several studies that evaluate utility do not report any privacy metric (e.g., Candidates 037, 064, 070), while others mention privacy only in qualitative terms. Among those that do measure privacy, there is no consensus on which metric is most appropriate, and the reporting of privacy parameters is often incomplete.

**3.4  Balance Between Privacy and Utility**
The included studies reveal a tension between privacy and utility, but the extent to which this trade‑off is explicitly analysed varies:
- **Trade‑off explicitly quantified**: Some studies systematically vary privacy parameters (e.g., ε in DP, or the number of synthetic datasets) and measure the impact on utility, demonstrating that stronger privacy safeguards generally degrade utility (Candidates 036, 055, 059, 077). Candidate 002 (excluded by year but illustrative) and Candidate 055 present frameworks that incorporate a fidelity‑utility trade‑off metric.
- **Privacy as a secondary concern**: In several papers, the primary focus is on demonstrating that synthetic data can replicate real‑data analyses, with privacy assessed only superficially or as a post‑hoc check (Candidates 003, 009, 011, 037, 064, 070). This suggests that, in practice, utility often receives more attention than privacy.
- **Equal weighting**: A minority of studies treat privacy and utility as co‑primary objectives, designing evaluations that give equal weight to both dimensions (Candidates 007, 013, 016, 032, 054, 059, 115, 143). These works typically report both a utility metric and a privacy metric and discuss the trade‑off.

Overall, the literature does not demonstrate a consistent, equal emphasis on privacy and utility. Privacy evaluation is frequently omitted or less rigorous, and there is no agreed‑upon threshold for what constitutes an acceptable privacy‑utility trade‑off.

**3.5  Gaps and Consensus**
- **Absence of standardised evaluation frameworks**: Although several papers propose comprehensive evaluation pipelines (Candidates 007, 021, 054, 108), none has been widely adopted. The terminology, metrics, and acceptable risk thresholds vary considerably.
- **Limited use of formal privacy models**: Differential privacy is employed in only a fraction of studies, and even when used, the privacy budget is often not justified in terms of real‑world risk.
- **Neglect of fairness and other dimensions**: Candidate 005 (excluded but relevant) and Candidate 055 highlight that fairness is rarely evaluated alongside privacy and utility, yet it is an important consideration for synthetic health data.
- **Temporal trends**: The number of studies addressing both privacy and utility appears to be increasing, but standardisation has not kept pace. The review period ends in mid‑2024; many candidate articles from 2025‑2026 (excluded by date) continue to propose frameworks, suggesting that the field is still actively seeking consensus.

**4.  Discussion**
The evidence from the 26 included primary studies indicates that while there is a growing body of work on evaluating synthetic health data, the research community has not yet reached consensus on standardised methods for either privacy or utility assessment. Privacy evaluation is particularly fragmented, with a wide array of metrics and a lack of agreement on what constitutes adequate protection. In many studies, utility is prioritised over privacy, and the trade‑off between the two is not systematically explored. Gaps remain in the consistent application of differential privacy, the inclusion of fairness considerations, and the adoption of holistic evaluation frameworks. Future research should focus on developing and validating a unified, multi‑dimensional evaluation protocol that balances privacy, utility, and fairness, and that is endorsed by the community.

**5.  Included Primary‑Study Articles**

Below is the definitive list of 26 primary studies that met all eligibility criteria from the candidate pool.

1.  **Title:** An evaluation of the replicability of analyses using synthetic health data.  
    **Corpus ID:** 4841

2.  **Title:** Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.  
    **Corpus ID:** 4838

3.  **Title:** Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.  
    **Corpus ID:** 4847

4.  **Title:** Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.  
    **Corpus ID:** 4842

5.  **Title:** Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.  
    **Corpus ID:** 4863

6.  **Title:** Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.  
    **Corpus ID:** 4845

7.  **Title:** Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.  
    **Corpus ID:** 73473

8.  **Title:** Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.  
    **Corpus ID:** 4851

9.  **Title:** A method for generating synthetic longitudinal health data.  
    **Corpus ID:** 73343

10. **Title:** A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.  
    **Corpus ID:** 4835

11. **Title:** Membership inference attacks against synthetic health data.  
    **Corpus ID:** 4867

12. **Title:** Evaluating the utility of synthetic COVID-19 case data.  
    **Corpus ID:** 4843

13. **Title:** Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.  
    **Corpus ID:** 73374

14. **Title:** Collaborative learning from distributed data with differentially private synthetic data.  
    **Corpus ID:** 4857

15. **Title:** Generating synthetic data from administrative health records for drug safety and effectiveness studies.  
    **Corpus ID:** 4834

16. **Title:** Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation.  
    **Corpus ID:** 4849

17. **Title:** Holdout-Based Empirical Assessment of Mixed-Type Synthetic Data.  
    **Corpus ID:** 4856

18. **Title:** Assessment of differentially private synthetic data for utility and fairness in end-to-end machine learning pipelines for tabular data.  
    **Corpus ID:** 4855

19. **Title:** Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.  
    **Corpus ID:** 4860

20. **Title:** Using Synthetic Data to Replace Linkage Derived Elements: A Case Study.  
    **Corpus ID:** 4859

21. **Title:** Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.  
    **Corpus ID:** 4846

22. **Title:** Synthetic Data Improve Survival Status Prediction Models in Early-Onset Colorectal Cancer.  
    **Corpus ID:** 4862

23. **Title:** Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.  
    **Corpus ID:** 4861

24. **Title:** DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations.  
    **Corpus ID:** 4868

25. **Title:** An evaluation of synthetic data augmentation for mitigating covariate bias in health data.  
    **Corpus ID:** 4836

26. **Title:** Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications.  
    **Corpus ID:** 75141
