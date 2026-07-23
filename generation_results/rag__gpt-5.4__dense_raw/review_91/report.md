Below is a title/abstract-only screening and evidence synthesis using only the supplied candidate pool.

## Screening result

I screened all 200 candidates against the stated criteria.

### Included in scope
I included **24 primary-study articles** that, based on title/abstract alone:

- are within the date range **2018-01-01 to 2024-07-31**
- concern **synthetic health-related/medical data**
- are **primary research**, not reviews/protocols/editorials
- evaluate the generated synthetic outputs on **utility and/or privacy**
- do **not** focus on excluded unstructured data types like images/text

### Common reasons for exclusion
Candidates were excluded because they were:

- **reviews/scoping reviews/systematic reviews/protocols/viewpoints/editorials**
- **outside the date range** (mostly 2025/2026, or pre-2018)
- about **public attitudes, governance, consent, app privacy, or AI ethics** rather than evaluation of synthetic medical data
- about **unstructured synthetic data** such as **clinical notes/text** (for example, Candidate 026)
- about synthetic data generation **without clear output evaluation** in the abstract
- not clearly about **health-related synthetic data evaluation**

---

## Evidence synthesis

## Overall answer to the review question

Based on these included abstracts, there is **not a clear community-wide consensus on a standardized method** for evaluating privacy and utility of synthetic health-related data.

What does appear is a **recurring set of evaluation families**:

- **Utility/fidelity**
  - replication of real-data analyses
  - predictive model performance
  - coefficient/hazard ratio agreement
  - confidence interval overlap
  - distributional similarity and correlation structure
  - descriptive/statistical resemblance
- **Privacy**
  - membership disclosure/inference risk
  - identity disclosure/re-identification risk
  - attribute disclosure risk
  - distance-based privacy metrics
  - duplicate-row checks
  - differential privacy parameters or privacy-preserving configurations

However, the abstracts suggest that these are **used variably and inconsistently**, rather than as a standard core set adopted across the field.

## Is there consensus on standardized evaluation methods?

### Short answer
**No strong consensus is evident.**

### Why
Several included studies themselves imply fragmentation:

- **Candidate 007** explicitly states that a **lack of standardized and objective evaluation and benchmarking strategy** has been found in the health-domain literature.
- Multiple studies propose their own **frameworks**, **pipelines**, or **new privacy metrics**, which usually indicates that the field is still converging rather than settled.
- The included studies use quite different endpoint mixes:
  - some are **utility-heavy**
  - some are **privacy-heavy**
  - some attempt a more balanced multidimensional evaluation

### What looks most common
Across the included abstracts, the most common utility approaches were:

1. **Replication of substantive analyses**
   - logistic regression
   - Cox regression
   - hazard ratios
   - treatment-effect estimates
   - readmission/complication prediction

2. **Predictive-performance transfer**
   - AUROC/AUPRC
   - c-statistic
   - F1/accuracy
   - train-on-synthetic/test-on-real style comparisons

3. **Statistical resemblance**
   - marginal distributions
   - dependency/correlation structure
   - Hellinger distance
   - Wasserstein distance
   - concordance
   - propensity-style resemblance measures

The most common privacy approaches were:

1. **Membership disclosure/inference**
2. **Identity disclosure / re-identification risk**
3. **Attribute disclosure**
4. **Distance-based privacy measures**
5. **Simple empirical checks**, such as duplicate-row detection

This pattern suggests **partial convergence at the level of metric categories**, but **not standardization at the level of a fixed evaluation protocol**.

---

## Are privacy considerations given equal importance as utility?

### Overall pattern
**Usually no.** Based on abstracts alone, privacy is often **present but not equally developed**.

### Typical imbalance
In many included studies, utility is assessed with **multiple detailed metrics**, while privacy is assessed with:

- a **single metric**
- a brief disclosure-risk check
- or a more general privacy claim

Examples of this general pattern include studies where:
- several utility measures are reported in detail
- privacy is summarized by one membership or disclosure statistic

### More balanced exceptions
Some studies appear more balanced or intentionally holistic, especially those that:
- evaluate **utility, fidelity, and privacy** together
- compare multiple generators
- propose a benchmarking framework/pipeline

Examples include:
- **Candidate 001**
- **Candidate 007**
- **Candidate 010**
- **Candidate 013**
- **Candidate 016**
- **Candidate 028**
- **Candidate 032**
- **Candidate 077**
- **Candidate 162**

### Privacy-focused exceptions
A smaller subset centers mainly on privacy evaluation:
- **Candidate 006**
- **Candidate 020**

These are valuable for the scoping question because they show active privacy-method development, but they also underscore that **privacy work is often siloed**, rather than integrated routinely into broader synthetic-data evaluation.

---

## What evaluation gaps emerge?

### 1. No universally adopted benchmark set
The included studies do not point to a common minimum reporting standard.

### 2. Utility is operationalized more richly than privacy
Utility often gets:
- multiple metrics
- task-based evaluations
- inferential replication tests

Privacy often gets:
- one metric
- one attack model
- one threshold

### 3. Privacy metrics are heterogeneous
Different papers use:
- membership disclosure
- identity disclosure
- attribute disclosure
- distance-based privacy
- re-identification-type metrics
- duplicate checks

This makes cross-study comparison difficult.

### 4. Task-specific utility dominates
Many papers evaluate whether synthetic data can reproduce a **specific downstream analysis**. Useful, but this limits comparability across studies.

### 5. Framework papers indicate immaturity of the field
The presence of papers building new pipelines/frameworks suggests the field is still trying to define what “good evaluation” should look like.

### 6. Some studies assess only one side of the trade-off
Several included studies are primarily:
- utility-only or utility-dominant
- privacy-only or privacy-dominant

That weakens direct assessment of privacy-utility balance.

---

## What can reasonably be concluded from these abstracts?

From the supplied abstracts alone, the literature appears to support the following conclusions:

1. **There is no settled consensus** on a standardized evaluation method for synthetic health-related data.
2. There is **some recurring agreement on broad dimensions** to assess:
   - utility/fidelity/resemblance
   - privacy/disclosure risk
3. **Utility is more consistently and more extensively measured than privacy**.
4. Privacy evaluation is present, but often **narrower, less standardized, and less comprehensive**.
5. A minority of studies propose or apply **more holistic evaluation frameworks**, suggesting movement toward standardization, but not yet consensus.

---

## Cautions and limitations

This synthesis is based **only on the supplied titles and abstracts**. I am **not claiming access to full texts** or any methods/details not stated in the abstracts. Some inclusion decisions are therefore necessarily based on the abstract’s apparent focus and reported evaluation content.

---

## Final included primary-study articles

- **An evaluation of the replicability of analyses using synthetic health data.**  
  **Corpus ID: 4841**

- **Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.**  
  **Corpus ID: 4838**

- **Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.**  
  **Corpus ID: 4847**

- **Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.**  
  **Corpus ID: 4842**

- **Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.**  
  **Corpus ID: 4863**

- **Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.**  
  **Corpus ID: 4845**

- **Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.**  
  **Corpus ID: 73473**

- **Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.**  
  **Corpus ID: 4851**

- **A method for generating synthetic longitudinal health data.**  
  **Corpus ID: 73343**

- **A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.**  
  **Corpus ID: 4835**

- **Membership inference attacks against synthetic health data.**  
  **Corpus ID: 4867**

- **Evaluating the utility of synthetic COVID-19 case data.**  
  **Corpus ID: 4843**

- **Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.**  
  **Corpus ID: 73374**

- **Collaborative learning from distributed data with differentially private synthetic data.**  
  **Corpus ID: 4857**

- **Generating synthetic data from administrative health records for drug safety and effectiveness studies.**  
  **Corpus ID: 4834**

- **Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation.**  
  **Corpus ID: 4849**

- **Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.**  
  **Corpus ID: 4860**

- **Using Synthetic Data to Replace Linkage Derived Elements: A Case Study.**  
  **Corpus ID: 4859**

- **Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.**  
  **Corpus ID: 4846**

- **Synthetic Data Improve Survival Status Prediction Models in Early-Onset Colorectal Cancer.**  
  **Corpus ID: 4862**

- **Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.**  
  **Corpus ID: 4861**

- **DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations.**  
  **Corpus ID: 4868**

- **An evaluation of synthetic data augmentation for mitigating covariate bias in health data.**  
  **Corpus ID: 4836**

- **Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications.**  
  **Corpus ID: 75141**

If you want, I can also turn this into a compact **PRISMA-style included/excluded table** with one-line reasons for each borderline candidate.
