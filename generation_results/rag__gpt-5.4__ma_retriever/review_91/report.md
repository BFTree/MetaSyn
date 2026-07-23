Below is a title/abstract-only screening and synthesis using only the supplied 200-candidate pool.

**Bottom line**

The candidate pool does not show consensus on a single standardized evaluation method for synthetic health-related tabular/longitudinal data. Across eligible primary studies, utility evaluation is common and often multi-pronged, but privacy evaluation is more heterogeneous, narrower, and often lighter-weight. Many studies assess both, but utility is typically richer and more application-linked, while privacy is frequently reduced to one or a small number of disclosure-risk proxies. That pattern supports the conclusion that privacy is generally not given equal methodological emphasis to utility.

**Screening approach**

Applied criteria from the prompt to titles/abstracts only:

Included:
- English-language primary studies from 2018-01-01 to 2024-07-31
- Studies on synthetic health-related/medical data
- Studies that evaluate generated outputs on utility and/or privacy

Excluded:
- Reviews, scoping/systematic reviews, viewpoints, editorials, protocols
- Studies on unstructured data only (images/text)
- No evaluation of generated output
- Out of date range
- Non-English

A few 2024/2023 studies discuss synthetic longitudinal or EHR data without fully specifying privacy metrics in the abstract; if the abstract explicitly states that privacy/disclosure risk was assessed, I treated them as eligible primary studies.

**What the included studies collectively show**

Across the included studies, evaluation methods cluster into three broad families:

1. **Resemblance/fidelity/statistical similarity**
- Distributional similarity, marginal/joint comparisons
- Correlation preservation
- Hellinger distance, propensity-score style distinguishability, duplicate-row checks, rare-event preservation

2. **Utility / downstream analytic validity**
- Replication of regression coefficients, hazard ratios, confidence intervals, significance direction
- Train-on-synthetic/test-on-real predictive performance
- Clinical or epidemiologic workload replication
- Sometimes task-specific measures like AUROC, AUPRC, calibration, agreement, power, bias

3. **Privacy / disclosure risk**
- Identity disclosure or “meaningful identity disclosure”
- Membership inference / membership disclosure
- Attribute disclosure
- Distance-to-closest-record / nearest-neighbor style risk
- Duplicate-row or exact-match checks
- Reidentification-oriented thresholds

**Consensus question**

There is partial convergence on the need to evaluate both utility and privacy, and some recurring metric families appear repeatedly:
- analytic replication
- predictive transfer performance
- statistical resemblance
- membership/disclosure-style privacy checks

But there is no clear standardization in:
- which dimensions must always be reported
- which specific privacy metric should be used
- what thresholds define acceptable privacy/utility
- whether privacy should be measured empirically, formally, adversarially, or by simple proximity/duplication heuristics
- how to aggregate multiple metrics into an overall judgment

Some studies explicitly frame the lack of standardization as a motivation for their work, which itself argues against an established consensus.

**Balance between utility and privacy**

The abstracts suggest an imbalance:
- Utility is usually evaluated with multiple methods, often directly tied to intended scientific or ML use.
- Privacy is more often represented by a single metric or a narrow risk family.
- Several studies make strong utility claims while reporting relatively limited privacy assessment details in the abstract.
- Only a subset uses stronger adversarial privacy testing such as membership inference.
- Formal privacy guarantees (for example differential privacy) appear in some studies, but not as a community-wide norm.

So the overall pattern is: privacy is recognized as important, but is not yet assessed as consistently or as comprehensively as utility.

**Evidence synthesis by theme**

**1. Framework-building studies confirm fragmentation**
Several included studies were designed to build evaluation pipelines or frameworks because the field lacked standardized assessment. That is direct evidence against consensus. These studies usually organize metrics into resemblance/fidelity, utility, and privacy, but they do not establish one accepted standard across the field.

**2. Utility assessment is relatively mature**
The most common utility paradigms are:
- replication of statistical analyses from the source data
- downstream ML transfer tests
- agreement on effect estimates, confidence intervals, or classification performance

These are concrete, interpretable, and often aligned to intended use. Utility therefore looks more operationalized than privacy.

**3. Privacy assessment is diverse and uneven**
Privacy evaluation ranges from:
- distance-based or duplicate-row checks
- disclosure risk models
- identity disclosure thresholds
- membership disclosure / membership inference attacks

This diversity suggests the field has not converged on what privacy risk matters most, how to measure it, or what constitutes adequate protection.

**4. Longitudinal/tabular structured health data dominate the eligible pool**
The included set is mostly tabular or longitudinal EHR/administrative/claims/clinical-trial style data, which fits the review question and exclusion criteria. This also means the synthesis mainly reflects structured health data evaluation practices, not imaging or text.

**Key gaps visible from abstracts alone**

- No universally adopted benchmark suite
- No common reporting standard for privacy metrics or thresholds
- Limited evidence that privacy is evaluated as deeply as utility
- Sparse use of adversarial privacy evaluation relative to utility testing
- Inconsistent linkage between privacy results and release decisions
- Limited standardization on combining multiple synthetic datasets or reporting inferential validity

**Main conclusion**

Based on this candidate pool, the research community does not appear to have reached consensus on standardized methods for evaluating privacy and utility of synthetic health-related data. There is some emerging convergence on broad evaluation domains, especially resemblance/fidelity, utility, and privacy, but not on a common metric set or decision framework. Utility assessment is generally more developed and more prominent than privacy assessment. Privacy is frequently considered, but not with equal methodological consistency or depth.

**Included primary studies**

1. **Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.**  
   `Corpus ID: 4863`

2. **Holdout-Based Empirical Assessment of Mixed-Type Synthetic Data.**  
   `Corpus ID: 4856`

3. **Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.**  
   `Corpus ID: 4842`

4. **Membership inference attacks against synthetic health data.**  
   `Corpus ID: 4867`

5. **An evaluation of the replicability of analyses using synthetic health data.**  
   `Corpus ID: 4841`

6. **Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.**  
   `Corpus ID: 4838`

7. **A method for generating synthetic longitudinal health data.**  
   `Corpus ID: 73343`

8. **Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.**  
   `Corpus ID: 4847`

9. **A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.**  
   `Corpus ID: 4835`

10. **Application of Bayesian networks to generate synthetic health data.**  
   `Corpus ID: 4850`

11. **DataSifter II: Partially synthetic data sharing of sensitive information containing time-varying correlated observations.**  
   `Corpus ID: 4868`

12. **Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation.**  
   `Corpus ID: 4849`

13. **Assessment of differentially private synthetic data for utility and fairness in end-to-end machine learning pipelines for tabular data.**  
   `Corpus ID: 4855`

14. **The Problem of Fairness in Synthetic Healthcare Data.**  
   `Corpus ID: 4837`

15. **Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.**  
   `Corpus ID: 4845`

16. **Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.**  
   `Corpus ID: 4851`

17. **Evaluating the utility of synthetic COVID-19 case data.**  
   `Corpus ID: 4843`

18. **An Approach for Generating Realistic Australian Synthetic Healthcare Data.**  
   `Corpus ID: 4839`

19. **Generating synthetic data from administrative health records for drug safety and effectiveness studies.**  
   `Corpus ID: 4834`

20. **Characterization of Synthetic Health Data Using Rule-Based Artificial Intelligence Models.**  
   `Corpus ID: 4840`

21. **Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.**  
   `Corpus ID: 4846`

**Notable exclusions driving the review**
- Review articles/scoping reviews: Candidates 018, 030, 122, 132, 148, 156, 184, 197
- Out of date range: 025, 042, 071, 094, 101, others before 2018
- Unstructured-only data (images/text): 031, 034, 046, 064, 103, 145, 191
- No clear generated-output evaluation in abstract or not really a synthetic-data evaluation study: 015, 038, 084, and similar
- 2025+ papers excluded by date even if otherwise relevant

A useful next step would be to convert this into a structured extraction table with columns for data type, utility metrics, privacy metrics, and whether privacy/utility were both assessed, which would make the imbalance more explicit.
