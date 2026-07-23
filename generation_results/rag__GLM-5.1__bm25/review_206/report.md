Based on the specified research question, inclusion criteria, and exclusion criteria, the titles and abstracts of the 200 candidate articles were screened to identify primary studies reporting early clinical evaluation of AI decision support systems for glaucoma diagnosis or progression detection.

### Screening Summary

The screening process involved evaluating each candidate against the date range (January 2020 to May 25, 2023), population (glaucoma patients), exposure (AI for diagnosis/progression), and publication type (excluding reviews, protocols, letters, and non-human studies).

- **Date Exclusions:** Numerous candidates (e.g., Candidates 144, 178, 189, 191, 156, 127, 57, 65, 88) were excluded because they were published in 2024, 2025, or 2026, which falls outside the specified search end date of May 25, 2023. Older studies (e.g., Candidates 033, 086, 190, 200) published before 2020 were also excluded.
- **Type Exclusions:** Several candidates were systematic reviews, scoping reviews, or narrative reviews (e.g., Candidates 040, 067, 127, 57, 65, 88, 113) and were excluded per the criteria.
- **Topic Exclusions:** Many studies utilized AI for other conditions (e.g., COVID-19, ADHD, breast cancer, stroke) or focused on non-AI glaucoma interventions (e.g., diet, medication adherence, IOP monitoring devices without AI) and were excluded.
- **Specific Glaucoma Exclusions:** Candidate 031 ("Decision Tree Algorithm-Based Prediction of Vulnerability to Depressive and Anxiety Symptoms in Caregivers of Children With Glaucoma") involves glaucoma patients' data but uses AI to predict *caregiver mental health*, not glaucoma diagnosis or progression, and was therefore excluded.

### Included Studies

Two primary studies met all inclusion criteria:

1.  **Candidate 137:** This 2021 study compares different machine learning classifiers for glaucoma diagnosis using Spectralis OCT parameters. It evaluates the diagnostic performance of various algorithms (CIT, LMT, C5.0, RF, XGBoost) against logistic regression in discriminating normal from glaucomatous eyes.
2.  **Candidate 188:** This 2022 study develops a multimodal AI model (Xception-based) for detecting glaucoma in a population with a high prevalence of myopia, using fundus photographs assessed with OCT. It reports on the model's decision support capability and validation performance.

### Evidence Synthesis: Reporting Quality and DECIDE-AI Adherence

The review aimed to assess adherence to the DECIDE-AI checklist standards (which include 17 AI-specific items and 10 generic items) for early clinical evaluation studies. Based on the available abstracts, the reporting quality of the two included studies presents a mixed picture, with significant gaps likely present in adherence to the full DECIDE-AI checklist, particularly regarding AI-specific contextual and interaction items.

**AI-Specific Reporting:**
- **Algorithm Description:** Both studies reported the specific algorithms or architectures used (Candidate 137 lists multiple classifiers; Candidate 188 specifies the Xception model and multimodal approach). This aligns with DECIDE-AI recommendations for transparency regarding the AI intervention.
- **Performance Metrics:** Both studies reported quantitative performance metrics (AUROC, accuracy, sensitivity), a core requirement for evaluating AI systems.
- **Data Inputs:** Both described the input data types (OCT parameters in Candidate 137; fundus photographs and OCT assessments in Candidate 188).

**Generic and Contextual Reporting Gaps:**
- **Human-AI Interaction:** Neither abstract explicitly described the workflow involving human clinicians interacting with the AI system (e.g., how the decision support integrates into clinical decision-making), a key DECIDE-AI item.
- **Study Context and Setting:** While Candidate 188 mentions the specific challenge of a "high prevalence of myopia" population, neither abstract detailed the clinical setting, the users of the system, or the specific early clinical evaluation design (e.g., prospective vs. retrospective) in the manner required by DECIDE-AI for robust context reporting.
- **Error Analysis and Limitations:** Candidate 137 notes that clinicians should "cautiously integrate" results, but detailed error analysis or discussion of algorithmic limitations (DECIDE-AI items) was not evident in the abstract.
- **Terminology:** Candidate 188's title uses the term "focus group study," which typically denotes qualitative research, while the abstract describes a quantitative AI validation study. This discrepancy highlights a potential issue in reporting accuracy or terminology alignment with standardized guidelines like DECIDE-AI.

**Conclusion:**
The identified early clinical evaluation studies for AI decision support in glaucoma (published between 2020 and May 2023) demonstrate capability in reporting technical AI specifications and performance metrics. However, based on abstract content, they likely fall short of full DECIDE-AI adherence, particularly in describing the human-AI interaction workflow, clinical integration context, and comprehensive error analysis. Improved adherence to DECIDE-AI standards would enhance the transparency and clinical interpretability of these AI systems.

***

### Included Primary-Study Articles

- **Comparison of Different Machine Learning Classifiers for Glaucoma Diagnosis Based on Spectralis OCT**
  Corpus ID: 3188

- **Use of multimodal dataset in AI for detecting glaucoma based on fundus photographs assessed with OCT: focus group study on high prevalence of myopia**
  Corpus ID: 3191
