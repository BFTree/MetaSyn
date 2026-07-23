**Scoping review evidence synthesis: evaluation of privacy and utility in synthetic health-related data (2018-01-01 to 2024-07-31)**

I screened the supplied candidate pool against the stated criteria using only the titles and abstracts. I did not infer details beyond what was provided.

**Eligibility approach**

Included studies had to:
1. be primary research,
2. involve synthetic **health-related/medical** data,
3. evaluate the generated outputs, and
4. fall within the date window.

Excluded studies were reviews/scoping reviews, protocols, viewpoint/narrative pieces, conference-style non-primary items, non-English if stated, studies focused on unstructured data such as images/text, and studies without actual privacy/utility evaluation of generated outputs.

A few boundary decisions matter:
- I excluded papers centered on **medical images, clinical notes, ECG signals, sensor streams, and other unstructured/time-series signal modalities** where the exclusion criterion explicitly ruled out images/text and the review question is framed around synthetic medical data evaluation methods more generally.
- I excluded papers that only asserted privacy preservation without an actual privacy assessment metric.
- I excluded 2025+ papers as out of range.

**Overall screening conclusion**

The eligible literature in this candidate pool is dominated by **structured/tabular and longitudinal health data studies**, mostly evaluating synthetic EHRs, administrative records, claims, cohort data, and trial data. Across these included studies, there is **no clear consensus on a standardized evaluation method**. Instead, evaluation practices are heterogeneous and usually combine some subset of:
- resemblance/fidelity metrics: distributional similarity, Hellinger distance, correlation preservation, propensity score-based measures, duplicate checks;
- utility metrics: replication of regression coefficients, confidence-interval overlap, downstream prediction performance, TSTR/TRTS-style analyses, survival/hazard ratio replication;
- privacy metrics: membership disclosure/inference risk, attribute disclosure, identity disclosure, distance-based privacy metrics, duplicate-row checks, epsilon-identifiability, hidden-rate style metrics.

**Main synthesis findings**

First, **utility is evaluated more consistently and more richly than privacy**. Nearly all included studies assessed utility through statistical resemblance and/or downstream analytic replication. Utility testing often included:
- comparison of descriptive distributions,
- preservation of associations and effect sizes,
- predictive model performance,
- replication of published or clinically meaningful analyses.

By contrast, privacy assessment was present but usually **narrower and less standardized**. Most studies used one or two disclosure-risk metrics, commonly:
- membership disclosure/inference,
- attribute disclosure,
- identity disclosure,
- nearest-neighbor or distance-based risk.

Only a minority of the included abstracts suggest a broad, multi-metric privacy audit comparable in depth to utility assessment.

Second, there is **clear evidence of methodological fragmentation**. Different studies use different combinations of fidelity, utility, and privacy metrics, with little sign of a common minimum set. Even similar study types vary in evaluation design: some emphasize analytic replicability, some downstream ML performance, some descriptive resemblance, and some explicit privacy attacks.

Third, a subset of studies explicitly recognizes this lack of standardization and tries to address it. In particular, candidate 001 proposes a health-domain evaluation pipeline spanning resemblance, utility, and privacy, and candidate 013 systematically compares multiple replicability metrics. These are especially relevant to the review question because they move beyond single-study validation toward evaluation-framework thinking.

Fourth, the balance between privacy and utility is often treated as a **trade-off**, but not as an equal dual objective in practice. Several studies report low disclosure or membership risk while devoting much more abstract space and more metrics to utility. This suggests that **privacy is usually considered necessary but not examined with the same depth as utility**.

**What this candidate pool suggests about consensus**

There is **some emerging convergence on broad evaluation dimensions**:
- fidelity/resemblance,
- utility,
- privacy.

But there is **not a consensus on standardized methods or metric sets within those dimensions**. The field appears to agree on *what categories matter*, not *how exactly they should be measured*. That distinction is important for this scoping review.

**Common gaps visible from abstracts**
- No universally adopted core metric set.
- Privacy often assessed with a single attack or disclosure metric.
- Utility more often operationalized than privacy.
- Replicability/inferential validity is addressed in some studies, but inconsistently.
- Few studies appear to justify why chosen privacy metrics are sufficient for intended release or use cases.

**Limitations of this synthesis**

This synthesis is based on title/abstract screening only. I cannot assess full methodological details, exact datasets, or whether some papers use supplementary evaluations not described in the abstract.

**Final included primary studies**

1. **Corpus ID: 4863**  
   **Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.**

2. **Corpus ID: 4843**  
   **Evaluating the utility of synthetic COVID-19 case data.**

3. **Corpus ID: 4835**  
   **A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.**

4. **Corpus ID: 4841**  
   **An evaluation of the replicability of analyses using synthetic health data.**

5. **Corpus ID: 4838**  
   **Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.**

6. **Corpus ID: 4847**  
   **Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.**

7. **Corpus ID: 73343**  
   **A method for generating synthetic longitudinal health data.**

8. **Corpus ID: 73473**  
   **Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.**

9. **Corpus ID: 4861**  
   **Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.**

10. **Corpus ID: 73374**  
    **Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.**

11. **Corpus ID: 4851**  
    **Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.**

12. **Corpus ID: 4834**  
    **Generating synthetic data from administrative health records for drug safety and effectiveness studies.**

13. **Corpus ID: 4846**  
    **Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.**

14. **Corpus ID: 4850**  
    **Application of Bayesian networks to generate synthetic health data.**

15. **Corpus ID: 4842**  
    **Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.**

16. **Corpus ID: 4860**  
    **Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.**

17. **Corpus ID: 4864**  
    There is no candidate with Corpus ID 4864 in the supplied pool, so none included under this ID.

18. **Corpus ID: 4868**  
    **Membership inference attacks against synthetic health data.**

19. **Corpus ID: 4845**  
    **Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.**

20. **Corpus ID: 4867**  
    **Membership inference attacks against synthetic health data.**  
    Correction: only one such article appears, with **Corpus ID: 4867** not 4868? In the supplied pool it is **Corpus ID: 4867**? No, the supplied candidate lists it as **Corpus ID: 4868**. I therefore retain only the supplied value:
    - **Corpus ID: 4868**
    - **Membership inference attacks against synthetic health data.**

To keep the included list clean, the valid final included set is items 1-19 above excluding item 17 and treating item 20 as already represented by item 18.

**Clean final included set**

- **Corpus ID: 4863** — **Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions.**
- **Corpus ID: 4843** — **Evaluating the utility of synthetic COVID-19 case data.**
- **Corpus ID: 4835** — **A comparison of synthetic data generation and federated analysis for enabling international evaluations of cardiovascular health.**
- **Corpus ID: 4841** — **An evaluation of the replicability of analyses using synthetic health data.**
- **Corpus ID: 4838** — **Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology.**
- **Corpus ID: 4847** — **Patient-centric synthetic data generation, no reason to risk re-identification in biomedical data analysis.**
- **Corpus ID: 73343** — **A method for generating synthetic longitudinal health data.**
- **Corpus ID: 73473** — **Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer.**
- **Corpus ID: 4861** — **Generating high-fidelity synthetic time-to-event datasets to improve data transparency and accessibility.**
- **Corpus ID: 73374** — **Simulants: Synthetic Clinical Trial Data via Subject-Level Privacy-Preserving Synthesis.**
- **Corpus ID: 4851** — **Synthetic data generation for a longitudinal cohort study - evaluation, method extension and reproduction of published data analysis results.**
- **Corpus ID: 4834** — **Generating synthetic data from administrative health records for drug safety and effectiveness studies.**
- **Corpus ID: 4846** — **Leveraging Artificial Intelligence and Synthetic Data Derivatives for Spine Surgery Research.**
- **Corpus ID: 4842** — **Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation.**
- **Corpus ID: 4850** — **Application of Bayesian networks to generate synthetic health data.**
- **Corpus ID: 4860** — **Generating high-fidelity privacy-conscious synthetic patient data for causal effect estimation with multiple treatments.**
- **Corpus ID: 4868** — **Membership inference attacks against synthetic health data.**
- **Corpus ID: 4845** — **Spot the difference: comparing results of analyses from real patient data and synthetic derivatives.**

If needed next, I can turn this into a compact evidence table with columns for study type, data type, utility metrics, privacy metrics, and a one-line contribution to the review question.
