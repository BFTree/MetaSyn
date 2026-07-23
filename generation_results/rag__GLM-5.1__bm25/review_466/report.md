### Systematic Review and Evidence Synthesis Report

**Review Target**
Research Question: This meta-analysis investigates whether automated alerting systems for sepsis detection improve clinical outcomes, particularly mortality and length of stay (LOS), in patients with sepsis compared to usual care, and further examines whether effectiveness varies by clinical setting (ICU, emergency department, ward) and prediction method (rule-based vs. machine learning).
Population: Hospitalized patients with sepsis (or at risk for sepsis)
Intervention: Automated alerting system for sepsis detection integrated into electronic healthcare records (rule-based or machine learning-based)
Comparison: Usual care (standard clinical practice without automated alerting system)
Outcomes: Mortality and Length of Stay (LOS)
Search Window: 1917-01-01 to 2021-12-31

**Screening Summary**
The fixed candidate pool of 200 articles was screened against the inclusion and exclusion criteria. Studies were excluded if they were reviews, protocols, conference abstracts, editorials, animal studies, case reports, pediatric populations (age < 16), non-relevant interventions (e.g., dietary supplements, telemedicine carts, nurse-driven checklists without EHR integration), prediction model development/validation studies without comparative effectiveness evaluation against usual care, or published after the search end date of 2021-12-31. Ten primary studies met all eligibility criteria and were included in the evidence synthesis.

---

### Evidence Synthesis

**Overall Impact on Mortality**
The evidence regarding the impact of automated sepsis alerting systems on mortality is mixed. Of the ten included studies, only one demonstrated a statistically significant reduction in sepsis mortality. Candidate 018 reported a 53% decrease in sepsis mortality (P = 0.03) following the implementation of a computerized surveillance algorithm coupled with mobile decision support. Candidate 118 observed a 30% improvement in the risk of adverse outcomes (a composite typically including mortality and ICU transfer) from baseline to year-end following the implementation of a two-stage Clinical Decision Support (CDS) system. Candidate 020 reported a suggestion of reduced mortality, though this finding did not reach statistical significance. Conversely, six studies—Candidates 001, 003, 004, 008, 027, and 061—found no significant effect on in-hospital or ICU mortality following the introduction of automated sepsis alerts or monitoring systems. Candidate 009 did not explicitly report a mortality effect but noted improvements in other outcomes.

**Overall Impact on Length of Stay (LOS)**
The impact on hospital or ICU LOS is similarly heterogeneous. Two studies reported significant reductions in LOS associated with the alerting intervention. Candidate 001 found a 16% decrease in LOS in the emergency department following the introduction of an EHR-based sepsis alert, and Candidate 009 observed decreased SICU and hospital LOS with the use of a real-time automated bedside dashboard and visual sepsis screen. However, the majority of studies found no significant impact on LOS. Candidates 003, 004, 008, and 018 reported no difference in LOS (or ICU-free days) between the intervention and usual care groups. Candidate 027 did not report LOS outcomes. Candidate 061 noted reductions in time to fluids and antibiotics but did not report a statistically significant difference in mortality or overall LOS days.

**Effectiveness by Clinical Setting**
*   **Intensive Care Unit (ICU):** Three studies evaluated alerting systems specifically in ICU settings (Candidates 003, 004, 009). None of the ICU-focused studies demonstrated a mortality benefit. Only Candidate 009 showed a benefit in LOS and process measures (time to antibiotics), whereas Candidates 003 and 004 found no improvement in clinical outcomes or guideline compliance.
*   **Emergency Department (ED):** Two studies focused on the ED (Candidates 001, 061). Neither demonstrated a significant reduction in mortality. Candidate 001, however, did find a significant reduction in LOS. Candidate 061 improved process times (time to fluids/antibiotics) but did not improve mortality.
*   **Inpatient Wards:** Four studies evaluated alerting systems on general inpatient wards or mixed non-ICU settings (Candidates 008, 018, 020, 118). The strongest mortality benefit was observed in this setting, specifically in Candidate 018, which utilized a mobile alert and decision support system. Candidate 118 also showed benefit for a composite adverse outcome. Conversely, Candidate 008 (an RCT of an EHR alert) found no mortality or LOS benefit. Candidate 020 showed a non-significant mortality reduction.

**Effectiveness by Prediction Method**
*   **Rule-Based Methods:** Nine of the ten included studies utilized rule-based algorithms (triggered by vital sign abnormalities, SIRS criteria, or specific logic rules). The results for rule-based systems are largely negative regarding mortality, with the notable exception of Candidate 018, which combined rule-based surveillance with a mobile decision support application and change management, yielding a significant mortality reduction. Candidate 118 also utilized a two-stage rule-based CDS and showed composite benefit. LOS benefits were seen in Candidates 001 and 009. The remaining rule-based studies (003, 004, 008, 020, 061) did not demonstrate significant mortality improvements, and some attributed the lack of effect to alert fatigue or low positive predictive value (e.g., Candidates 001, 008).
*   **Machine Learning (ML) Methods:** Only one study evaluated an ML-based approach (Candidate 027). This retrospective observational study of a real-time ML advisory embedded in the EMR found that the use of the tool did not improve sepsis mortality rates, noting that its real-world performance characteristics (sensitivity and clinical utility) were lower than previously described in retrospective validations.

**Summary of Findings**
The synthesized evidence suggests that automated sepsis alerting systems integrated into EHRs do not consistently improve mortality or LOS compared to usual care. Most randomized controlled trials and quasi-experimental studies in this pool—particularly those relying on simple rule-based EHR alerts in the ICU and ED—failed to demonstrate a significant clinical benefit, often citing alert fatigue, low specificity, or lack of actionable decision support as limitations. The most promising mortality outcome was observed in a ward-based study that paired rule-based surveillance with mobile decision support and robust change management (Candidate 018). Evidence for ML-based alerting systems is currently sparse in this pool and does not yet show a mortality benefit. Effectiveness may vary by setting, with ward-based implementations showing more potential for mortality reduction than ICU or ED implementations, though the evidence is limited.

---

### Included Primary-Study Articles

*   **Title:** Impact of an emergency department electronic sepsis surveillance system on patient mortality and length of stay.
    **Corpus ID:** 118963

*   **Title:** Randomized trial of automated, electronic monitoring to facilitate early detection of sepsis in the intensive care unit*.
    **Corpus ID:** 2937

*   **Title:** An Electronic Tool for the Evaluation and Treatment of Sepsis in the ICU: A Randomized Controlled Trial.
    **Corpus ID:** 2939

*   **Title:** Electronic health record-based clinical decision support alert for severe sepsis: a randomised evaluation.
    **Corpus ID:** 2936

*   **Title:** Sooner is better: use of a real-time automated bedside dashboard improves sepsis care.
    **Corpus ID:** 2934

*   **Title:** Evaluating the impact of a computerized surveillance algorithm and decision support system on sepsis mortality.
    **Corpus ID:** 2946

*   **Title:** Development, implementation, and impact of an automated early warning and response system for sepsis.
    **Corpus ID:** 2940

*   **Title:** Retrospective Observational Study of the Clinical Performance Characteristics of a Machine Learning Approach to Early Sepsis Identification.
    **Corpus ID:** 119005

*   **Title:** Triage sepsis alert and sepsis protocol lower times to fluids and antibiotics in the ED.
    **Corpus ID:** 2945

*   **Title:** A Multidisciplinary Sepsis Program Enabled by a Two-Stage Clinical Decision Support System: Factors That Influence Patient Outcomes.
    **Corpus ID:** 137298
