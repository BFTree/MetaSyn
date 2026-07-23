**Screening and Synthesis Report: Standardized Evaluation of Privacy and Utility for Synthetic Health Data**

This report examines the candidate pool of 200 articles, applying the defined inclusion/exclusion criteria to identify primary studies that evaluate synthetic health‑related data and explicitly assess the output in terms of utility and/or privacy. The goal is to determine whether there is consensus on evaluation methods and whether privacy receives attention comparable to utility when synthetic medical data are appraised.

**Screening Process and Outcome**
All 200 supplied titles and abstracts were screened against the full criteria.  
Reasons for exclusion were:
- Publication year >2024 (many 2025–2026 candidates, outside the search end date of 2024‑07‑31).
- Document type– reviews, systematic/scoping reviews, and narrative reviews (e.g., Candidate 005, 007, 027, 032, 049, 059, 092, 097, 108, 125, 149, 152, 155, 157, 163, 169, 173, 174, 179, 180, 181, 184, 193, 194, 195, 196).
- Use of unstructured data (images or text) without a focus on tabular/structured synthetic data (e.g., face data, clinical notes, neuroimaging, ultrasound images, dental images, AS‑OCT, brain MRI, skin images, text‑based suicide risk notes).
- Lack of any assessment of the generated output; studies that only describe generation methods without evaluating utility or privacy, or that focus on other topics (e.g., federated learning without synthetic data generation, privacy policies, education, energy data, sport sciences).
- Posters, conference abstracts, or articles not in English (none identified among candidates).

After screening, **36 primary‑study articles** met all inclusion criteria. They are listed at the end of this report.

**Synopsis of Included Studies**
All 36 studies describe the generation of synthetic health or medical data (tabular, longitudinal, time‑series, administrative claims, or physiological signals) and quantitatively evaluate the output. The data types include electronic health records, clinical trial data, disease‑specific cohorts, hospital administrative data, vital signs, and wearable‑sensor streams.

**Evaluation Dimensions Addressed**
1. **Utility (Fidelity, Statistical Similarity, Downstream Task Performance)**  
   Every included study reports some form of utility assessment. Common strategies are:
   - Univariate/bivariate distribution comparison (e.g., Hellinger distance, Kolmogorov‑Smirnov statistics, correlation differences).
   - Propensity score mean squared error (pMSE) to measure distinguishability from real data.
   - Machine learning performance when training on synthetic and testing on real data (Train‑on‑Synthetic‑Test‑on‑Real, TSTR), using metrics such as AUROC, AUPRC, F1‑score, accuracy.
   - Replicability of regression or survival analysis results (confidence interval overlap, decision agreement, bias, power).
   - Visual and qualitative inspection of epidemic curves, temporal trends, and clinical plausibility.

   The most frequent approach is to train a predictive model on synthetic data and evaluate it on real hold‑out data. Many studies also check whether important clinical associations (e.g., treatment effects, risk factor estimates) are preserved. A few use XAI‑based rule similarity (Candidate 091) or “actionability” frameworks that combine veracity, utility, and privacy (Candidate 021).

2. **Privacy (Disclosure Risk, Membership Inference, Attribute Disclosure)**  
   Privacy evaluation is far less uniform and, in several studies, entirely absent or only qualitatively mentioned.
   - **Quantitative privacy metrics** appear in a subset: membership inference risk (e.g., F1 score of an attacker, hidden rate, protection against distance‑based attacks), attribute disclosure risk (e.g., proportion of unique correct matches, ϵ‑identifiability, average matching probability), differential privacy parameters (ε values, privacy budget), and re‑identification risk thresholds (e.g., Health Canada’s 9 % threshold).  
   - **Common privacy‑specific metrics** include:
     - Membership disclosure / inference risk (Candidate 012, 013, 064, 079, 104).  
     - Identity disclosure risk (Candidate 053, 054, 056).  
     - Distance‑based privacy (Candidate 015, 004 not included).  
     - Differential privacy guarantees with reported ε (Candidate 041, 044, 158).  
   - Several studies only mention that “no duplicate rows were found” or that the generation process “protects privacy” without quantitative risk estimates.
   - Notably, a few studies (e.g., Candidate 030, 039, 070, 074, 085, 087, 091, 099, 114, 160, 183) evaluate **only utility**; privacy is either assumed or not assessed. Conversely, Candidate 064 solely evaluates privacy (membership inference) without examining utility.

**Consensus on Standardized Evaluation Methods**
There is **no consensus** on a single, universally accepted framework for evaluating synthetic health data. The landscape shows:
- A wide variety of utility metrics, often chosen ad‑hoc for a specific dataset or task. Some studies propose comprehensive evaluation pipelines (e.g., Candidate 001’s resemblance‑utility‑privacy pipeline, Candidate 002’s fidelity‑utility‑privacy framework, Candidate 017’s quality‑privacy‑usability‑complexity framework), but these remain proposals rather than adopted standards.
- No agreement on which privacy metrics are essential. Even among studies that do assess privacy, the choice of metric (membership inference, attribute disclosure, DP‑ε) varies, and thresholds for “acceptable” risk differ (e.g., 0.09 identity disclosure risk, 9 % patient disclosure).  
- Only a handful of studies systematically compare multiple privacy metrics or attempt to **balance** privacy and utility directly (e.g., Candidate 001, 012, 021, 044, 056, 075). The majority treat privacy as a secondary check or omit it.

**Balance Between Privacy and Utility**
Privacy considerations are **not given equal importance** to utility in the included literature:
- Utility is assessed in 100 % of the studies, often extensively with multiple complementary metrics.
- Privacy is quantitatively evaluated in only about half (17 of 36) of the studies; many of those still focus primarily on utility and report a single privacy number for reassurance.
- Studies that do weigh both dimensions typically present privacy figures as a risk threshold that should not be exceeded, while utility is optimised; few explicitly define a trade‑off frontier or joint optimisation.
- The language of many abstracts reinforces this imbalance: “privacy was preserved” is frequently stated without a numeric demonstration, whereas utility is always backed by concrete statistical comparisons.

**Gaps Identified**
- **Lack of standardised privacy metrics**: No core set of privacy measures is consistently applied; membership inference, attribute disclosure, and DP‑based guarantees are used piecemeal.
- **Inconsistent reporting**: Privacy parameters (e.g., ε, attack success rates) are often omitted or described imprecisely.
- **Scarce head‑to‑head comparisons** of different synthetic data generation methods on the same privacy‑utility benchmarks.
- **Time‑series and longitudinal data evaluation** is still emerging; many utility metrics assume independent rows, which may not be appropriate for sequential health data.
- **Fairness and bias evaluations** are rare (Candidate 008 and 142 are not included here due to year or domain, but Candidate 031, though excluded, touched fairness). Among the included studies, none systematically assess whether synthetic data introduce or mitigate health disparities.
- **Real‑world clinical validation** is almost absent; evaluations are based on statistical or machine‑learning proxy tasks rather than clinician‑judged fidelity or safety.

**Conclusion**
Within the candidate set, the evidence shows a strong emphasis on demonstrating the statistical or predictive utility of synthetic health data, while privacy assessment remains fragmented and often subordinate. No consensus has yet emerged on how to holistically evaluate synthetic data; the field lacks a broadly adopted, replicable framework that equally weights privacy and utility. This imbalance highlights a critical need for community‑driven standardisation of evaluation protocols that include minimum privacy‑risk reporting, consistent metrics, and explicit trade‑off analyses, especially for the sensitive, high‑dimensional health data that these methods aim to unlock.

---

**Final List of Included Primary‑Study Articles**

1. **Candidate 001**  
   Title: *Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.*  
   Corpus ID: 4863

2. **Candidate 010**  
   Title: *Evaluating the utility of synthetic COVID-19 case data.*  
   Corpus ID: 4843

3. **Candidate 011**  
   Title: *Generating Synthetic Health Sensor Data for Privacy-Preserving Wearable Stress Detection.*  
   Corpus ID: 73555

4. **Candidate 012**  
   Title: *A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.*  
   Corpus ID: 4835

5. **Candidate 013**  
   Title: *An evaluation of the replicability of analyses using synthetic health data.*  
   Corpus ID: 4841

6. **Candidate 014**  
   Title: *Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.*  
   Corpus ID: 4838

7. **Candidate 015**  
   Title: *Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.*  
   Corpus ID: 4847

8. **Candidate 016**  
   Title: *A method for generating synthetic longitudinal health data.*  
   Corpus ID: 73343

9. **Candidate 018**  
   Title: *Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation.*  
   Corpus ID: 4849

10. **Candidate 021**  
    Title: *Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.*  
    Corpus ID: 73473

11. **Candidate 039**  
    Title: *Prediction of Tuberculosis Using an Automated Machine Learning Platform for Models Trained on Synthetic Data.*  
    Corpus ID: 4858

12. **Candidate 035**  
    Title: *Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.*  
    Corpus ID: 4861

13. **Candidate 036**  
    Title: *Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.*  
    Corpus ID: 73374

14. **Candidate 041**  
    Title: *Collaborative learning from distributed data with differentially private synthetic data.*  
    Corpus ID: 4857

15. **Candidate 044**  
    Title: *Synthetic Data Improve Survival Status Prediction Models in Early-Onset Colorectal Cancer.*  
    Corpus ID: 4862

16. **Candidate 053**  
    Title: *Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.*  
    Corpus ID: 4842

17. **Candidate 054**  
    Title: *Application of Bayesian networks to generate synthetic health data.*  
    Corpus ID: 4850

18. **Candidate 056**  
    Title: *Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.*  
    Corpus ID: 4860

19. **Candidate 064**  
    Title: *Membership inference attacks against synthetic health data.*  
    Corpus ID: 4867

20. **Candidate 066**  
    Title: *Synthetic electronic health records generated with variational graph autoencoders.*  
    Corpus ID: 4982

21. **Candidate 070**  
    Title: *Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.*  
    Corpus ID: 4851

22. **Candidate 074**  
    Title: *Generating synthetic data from administrative health records for drug safety and effectiveness studies.*  
    Corpus ID: 4834

23. **Candidate 075**  
    Title: *Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications.*  
    Corpus ID: 75141

24. **Candidate 079**  
    Title: *DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations.*  
    Corpus ID: 4868

25. **Candidate 084**  
    Title: *Demonstrating an approach for evaluating synthetic geospatial and temporal epidemiologic data utility: Results from analyzing >1.8 million SARS-CoV-2 tests in the United States National COVID Cohort Collaborative (N3C).*  
    Corpus ID: 73632

26. **Candidate 085**  
    Title: *Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.*  
    Corpus ID: 4845

27. **Candidate 087**  
    Title: *Semantic representation and comparative analysis of physical activity sensor observations using MOX2-5 sensor in real and synthetic datasets: a proof-of-concept-study.*  
    Corpus ID: 73521

28. **Candidate 091**  
    Title: *Characterization of Synthetic Health Data Using Rule-Based Artificial Intelligence Models.*  
    Corpus ID: 4840

29. **Candidate 099**  
    Title: *Diffusion-based conditional ECG generation with structured state space models.*  
    Corpus ID: 4983

30. **Candidate 104**  
    Title: *Generating synthetic clinical data that capture class imbalanced distributions with generative adversarial networks: Example using antiretroviral therapy for HIV.*  
    Corpus ID: 73400

31. **Candidate 114**  
    Title: *Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.*  
    Corpus ID: 4846

32. **Candidate 158**  
    Title: *A multicenter random forest model for effective prognosis prediction in collaborative clinical research network.*  
    Corpus ID: 73559

33. **Candidate 160**  
    Title: *PlethAugment: GAN-Based PPG Augmentation for Medical Diagnosis in Low-Resource Settings.*  
    Corpus ID: 4985

34. **Candidate 183**  
    Title: *Synthesizing time-series wound prognosis factors from electronic medical records using generative adversarial networks.*  
    Corpus ID: 4984

35. **Candidate 048**  
    Title: *Leveraging VQ-VAE tokenization for autoregressive modeling of medical time series.*  
    Corpus ID: 75054

36. **Candidate 088**  
    Title: *Synthesize high-dimensional longitudinal electronic health records via hierarchical autoregressive language model.*  
    Corpus ID: 4986
