# ProtoMA Systematic Review Report

**Benchmark task:** 436
**Target:** Meta-analysis of randomized controlled trials of electronic health interventions to reduce medication errors

## Abstract

**Background:** This review addresses This meta-analysis investigates whether electronic health interventions, particularly computerized decision-support systems (CDS), are effective in reducing medication errors compared to usual care in healthcare settings..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 61 unique candidates.

**Results:** 9 study reports were retained after explicit screening. The random-effects estimate was 0.627 (95% CI 0.071 to 5.526); I-squared was 98.2%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Medication errors remain a clinically important source of preventable harm across hospitals, clinics, and pharmacies, occurring at multiple points in the medication-use process, including prescribing, transcribing, dispensing, administration, and monitoring. Their consequences range from intercepted potential errors to actual errors and adverse drug events, with direct implications for patient safety, length of stay, treatment burden, and healthcare resource use. Electronic health interventions such as computerized decision-support systems (CDS), electronic health records (EHR), electronic medication administration records (eMAR), computerized physician order entry (CPOE), and barcode medication administration (BCMA) are designed to standardize workflows, improve medication information availability, and support safer clinical decisions at the point of care.

Despite their widespread adoption, the evidence for their effect on medication safety remains heterogeneous. Prior reviews of digital health technologies and medication-safety tools have shown promise for supporting clinical decision-making and medication management, but they also highlight inconsistent methodologies, limited prospective testing, and uncertainty about whether these systems reliably reduce real-world harm rather than simply changing documentation or detection patterns. In addition, implementation factors such as workflow integration, technical infrastructure, and user acceptance may influence effectiveness, making it difficult to infer benefit from technology presence alone.

Accordingly, this systematic review aimed to evaluate, in healthcare settings, whether electronic health interventions reduce medication errors compared with usual care. Specifically, we assessed effects on potential errors, actual errors, and adverse drug events across CDS, EHR, eMAR, CPOE, and BCMA interventions, using evidence from randomized, quasi-experimental, observational, and validation studies.

## Review Question

- Population: Patients in healthcare settings including hospitals, clinics, and pharmacies
- Intervention: Electronic health interventions including computerized decision-support systems (CDS), electronic health records (EHR), electronic medication administration records (eMAR), computerized physician order entry (CPOE), and barcode medication administration (BCMA)
- Exposure: Not reported
- Comparison: Usual care
- Outcome: Medication errors (including potential errors, actual errors, and adverse drug events)
- Search window: 2023-05-01 to 2024-11-03

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Hospitals"[Mesh] OR "Ambulatory Care Facilities"[Mesh] OR "Pharmacies"[Mesh] OR hospital*[tiab] OR clinic*[tiab] OR ambulatory[tiab] OR inpatient*[tiab] OR outpatient*[tiab] OR pharmac*[tiab] OR "healthcare setting*"[tiab] OR "health care setting*"[tiab]) AND ("Decision Support Systems, Clinical"[Mesh] OR "Medical Order Entry Systems"[Mesh] OR "Electronic Health Records"[Mesh] OR "Medication Systems, Hospital"[Mesh] OR "Barcodes"[Mesh] OR "clinical decision support"[tiab] OR CDS[tiab] OR CDSS[tiab] OR "computeri?ed physician order entry"[tiab] OR CPOE[tiab] OR "electronic health record*"[tiab] OR EHR[tiab] OR EMR[tiab] OR "electronic medical record*"[tiab] OR eMAR[tiab] OR "electronic medication administration record*"[tiab] OR BCMA[tiab] OR "barcode medication administration"[tiab] OR "electronic prescribing"[tiab] OR e-prescrib*[tiab]))`
2. `(("Medication Errors"[Mesh] OR "Medication Systems, Hospital"[Mesh] OR "Drug-Related Side Effects and Adverse Reactions"[Mesh] OR "Patient Safety"[Mesh] OR "medication error*"[tiab] OR "prescribing error*"[tiab] OR "dispensing error*"[tiab] OR "administration error*"[tiab] OR "medication administration error*"[tiab] OR "drug error*"[tiab] OR "potential adverse drug event*"[tiab] OR "actual adverse drug event*"[tiab] OR "adverse drug event*"[tiab] OR ADE[tiab] OR ADEs[tiab] OR "preventable adverse drug event*"[tiab]) AND ("Decision Support Systems, Clinical"[Mesh] OR "Medical Order Entry Systems"[Mesh] OR "Electronic Health Records"[Mesh] OR "Medication Systems, Hospital"[Mesh] OR "Barcodes"[Mesh] OR "clinical decision support"[tiab] OR CDS[tiab] OR CDSS[tiab] OR "computeri?ed decision support"[tiab] OR "computeri?ed physician order entry"[tiab] OR CPOE[tiab] OR "electronic health record*"[tiab] OR EHR[tiab] OR EMR[tiab] OR eMAR[tiab] OR "electronic medication administration record*"[tiab] OR BCMA[tiab] OR "barcode medication administration"[tiab] OR "electronic prescribing"[tiab]))`
3. `(("Hospitals"[Mesh] OR "Ambulatory Care Facilities"[Mesh] OR "Pharmacies"[Mesh] OR hospital*[tiab] OR clinic*[tiab] OR inpatient*[tiab] OR outpatient*[tiab] OR pharmac*[tiab]) AND ("Decision Support Systems, Clinical"[Mesh] OR "Medical Order Entry Systems"[Mesh] OR "Electronic Health Records"[Mesh] OR "clinical decision support"[tiab] OR CDS[tiab] OR CDSS[tiab] OR CPOE[tiab] OR "computeri?ed physician order entry"[tiab] OR EHR[tiab] OR EMR[tiab] OR eMAR[tiab] OR BCMA[tiab] OR "barcode medication administration"[tiab]) AND ("Medication Errors"[Mesh] OR "Drug-Related Side Effects and Adverse Reactions"[Mesh] OR "Patient Safety"[Mesh] OR "medication error*"[tiab] OR "prescribing error*"[tiab] OR "dispensing error*"[tiab] OR "administration error*"[tiab] OR "adverse drug event*"[tiab] OR ADE[tiab] OR "potential error*"[tiab] OR "preventable adverse drug event*"[tiab]))`
4. `(("Decision Support Systems, Clinical"[Mesh] OR "Medical Order Entry Systems"[Mesh] OR "Electronic Health Records"[Mesh] OR "Medication Systems, Hospital"[Mesh] OR "Barcodes"[Mesh] OR "clinical decision support"[tiab] OR CDS[tiab] OR CDSS[tiab] OR CPOE[tiab] OR "computeri?ed physician order entry"[tiab] OR "electronic health record*"[tiab] OR EHR[tiab] OR EMR[tiab] OR eMAR[tiab] OR BCMA[tiab] OR "barcode medication administration"[tiab]) AND ("Medication Errors"[Mesh] OR "Drug-Related Side Effects and Adverse Reactions"[Mesh] OR "medication error*"[tiab] OR "prescribing error*"[tiab] OR "dispensing error*"[tiab] OR "administration error*"[tiab] OR "adverse drug event*"[tiab] OR ADE[tiab]) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR "Randomized Controlled Trial"[Publication Type] OR "Controlled Clinical Trial"[Publication Type] OR cohort[tiab] OR "Cohort Studies"[Mesh] OR "before and after"[tiab] OR pre-post[tiab] OR "interrupted time series"[tiab] OR quasi-experiment*[tiab] OR observational[tiab]))`
5. `((("computerized physician order entry"[tiab] OR CPOE[tiab] OR "Medical Order Entry Systems"[Mesh]) OR ("barcode medication administration"[tiab] OR BCMA[tiab] OR ((barcode*[tiab] OR bar-code*[tiab]) AND medication[tiab] AND administration[tiab])) OR (eMAR[tiab] OR "electronic medication administration record*"[tiab]) OR ("electronic health record*"[tiab] OR EHR[tiab] OR EMR[tiab] OR "Electronic Health Records"[Mesh]) OR ("clinical decision support"[tiab] OR CDS[tiab] OR CDSS[tiab] OR "Decision Support Systems, Clinical"[Mesh])) AND ("medication error*"[tiab] OR "prescribing error*"[tiab] OR "dispensing error*"[tiab] OR "administration error*"[tiab] OR "adverse drug event*"[tiab] OR ADE[tiab] OR "Medication Errors"[Mesh]) AND (patient*[tiab] OR hospital*[tiab] OR clinic*[tiab] OR pharmac*[tiab] OR inpatient*[tiab] OR outpatient*[tiab] OR "Hospitals"[Mesh] OR "Ambulatory Care Facilities"[Mesh] OR "Pharmacies"[Mesh]))`

The merged candidate pool contained 61 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies conducted in healthcare settings such as hospitals, clinics, ambulatory care, long-term care, or pharmacies involving patients or medication-use processes affecting patients.
- Studies evaluating an electronic health intervention intended to improve medication use or safety, including computerized decision-support systems, electronic health records, electronic medication administration records, computerized physician order entry, or barcode medication administration.
- Studies that include a comparison with usual care, pre-implementation practice, or a non-electronic medication management process.
- Studies reporting medication safety outcomes, including potential medication errors, actual medication errors, or adverse drug events.

Exclusion criteria:

- Studies not conducted in healthcare delivery settings or not involving patient care or medication-use processes.
- Studies evaluating non-electronic, purely educational, administrative, or unrelated digital interventions, or technologies outside the specified electronic medication management systems.
- Studies that do not report medication error-related outcomes, such as those limited to workflow efficiency, user satisfaction, or general clinical outcomes without medication safety data.
- Non-original research or insufficiently detailed reports, such as editorials, commentaries, letters, conference abstracts only, case reports, or protocols.

61 candidates were screened and 9 were retained.

### Statistical Analysis

### Statistical Analysis
For quantitative synthesis, the effect measure was the **odds ratio (OR)** for dichotomous medication error outcomes. Four studies contributed to the meta-analysis (**N = 4**). Pooled estimates were calculated under both **random-effects** and **fixed-effect** models.

- **Random-effects model:** pooled OR with 95% CI.
- **Fixed-effect model:** pooled OR with 95% CI.

Statistical heterogeneity was assessed using **Cochran’s Q**, **I²**, and **τ²**. A high level of between-study heterogeneity was observed (**I² = 98.2%**, **Q = 168.88**, **p < 0.001**, **τ² = 4.8297**), supporting use of a random-effects approach as the primary model. Statistical significance was evaluated using two-sided tests with **p < 0.05** considered significant.

## Results

### Study Selection

### Results of Search
The literature search identified **61 records** after deduplication, comprising **61 records from local sources** and **0 records from PubMed**. All **61 records** underwent title and abstract screening, of which **52** were excluded at the first stage for not meeting the eligibility criteria. This left **9 full-text articles** for detailed assessment. No studies were excluded after full-text review (**0 full-text exclusions**). Consequently, **9 studies** met the inclusion criteria and were incorporated into the systematic review. Thus, the review moved from 61 screened records to 9 included studies, consistent with the PRISMA selection process.

Most frequent recorded exclusion reasons:

- Systematic review; non-original research excluded.: 2
- Integrative review; non-original research excluded.: 1
- Appears to describe translation/adaptation of a tool and pharmacist intervention characterization rather than evaluation of an eligible electronic medication-management intervention against a comparison.: 1
- Survey of pharmacy practice processes; does not evaluate an eligible electronic intervention with comparison or report medication error outcomes attributable to the intervention.: 1
- Focuses on costs and process quality in hospitals already using CPOE; abstract does not report medication error-related outcomes or a usual-care/preimplementation comparison.: 1
- Descriptive implementation report with insufficient evidence of a comparison and no clear medication error outcome reporting.: 1
- Evaluates pharmacist interventions, not an eligible electronic medication-management system.: 1
- Assesses prescribing compliance within an electronic medication management system, but abstract does not indicate medication error or adverse drug event outcomes.: 1
- Focuses on discharge prescription accuracy/omissions via EMR advisory, but abstract does not clearly report medication error-related outcomes with sufficient detail.: 1
- Decision-analytic cost-utility model, not original comparative clinical study reporting observed medication error outcomes.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 2574 | 2019 | Integration of a Commercial Barcode-Assisted Medication Dispensing System in a Teaching Hospital. |
| 119610 | 2025 | Comparing safety, performance and user perceptions of a patient-specific indication-based prescribing tool with current practice: a mixed methods randomised user testing study. |
| 114478 | 2018 | Implementation of a new health information technology for the management of cancer chemotherapies. |
| 2579 | 2010 | Unintended effects of a computerized physician order entry nearly hard-stop alert to prevent a drug interaction: a randomized controlled trial. |
| 114471 | 2023 | Improving medication safety in a paediatric hospital: a mixed-methods evaluation of a newly implemented computerised provider order entry system. |
| 139124 | 2022 | Integration of the Codonics Safe Label System® and the Omnicell XT® Anesthesia Workstation into Pediatric Anesthesia Practice: Utilizing Technology to Increase Medication Labeling Compliance and Decrease Medication Discrepancies While Maintaining User Acceptability. |
| 118925 | 2025 | Effectiveness of computerised alerts to reduce drug-drug interactions (DDIs) and DDI-related harm in hospitalised patients: a quasi-experimental controlled pre-post study. |
| 107258 | 2026 | Clinical effectiveness of a cloud-based dual-layer prescription review system: provincial integration across internet and outpatient care. |
| 118928 | 2024 | Evaluation of the Effect of Smart Pump Interoperability on Infusion Errors in the Pediatric Hospital Setting. |

### Study Characteristics

### Study Characteristics

Nine studies involving a total of 319,561 participants were included, with publication years ranging from 2010 to 2026. The evidence base was geographically limited and unevenly distributed: one study was conducted in the United States, one in the United Kingdom, and one in Australia, while the remaining studies did not report country of origin. Sample sizes varied markedly, from a small simulated mixed-methods crossover study with 24 participants to a very large retrospective before-after cohort study including 309,340 participants, indicating substantial variation in study scale and setting.

There was considerable methodological heterogeneity across the included studies. Study designs comprised one controlled randomized study, one randomized clinical trial, one simulated randomised cross-over exploratory mixed-methods study with concurrent triangulation, one quasi-experimental controlled pre-post study, two before-and-after designs, one pre-post mixed-methods observational study, one retrospective and prospective validation study, and one retrospective before-after cohort study. Although most studies were rated as high confidence in the enhanced data extraction process (8/9 studies), one study was rated as medium confidence. In contrast, risk-of-bias assessments suggested important methodological concerns: most studies were judged at high or high risk overall, and one was rated as unclear risk. Across studies, judgments for random sequence generation, allocation concealment, and blinding were uniformly unclear, limiting confidence in internal validity despite generally high extraction confidence.

Notable heterogeneity was also evident in participant and intervention characteristics, although reporting was often incomplete. Beyond total sample size, population details such as age, sex distribution, and condition severity were not consistently reported, preventing a clear description of the clinical comparability of study cohorts. Similarly, intervention characteristics including dose, duration, and mode of delivery varied by study design and context, but were insufficiently detailed in the extracted dataset to support meaningful cross-study comparison. Outcome measurement approaches also appeared diverse, spanning trial-based, observational, audit, validation, and mixed-methods evaluations, which further contributes to between-study heterogeneity. Overall, the included literature represents a broad but methodologically diverse body of evidence with substantial variation in design, scale, reporting completeness, and risk of bias.

### Main Findings

## Results

The pooled analysis demonstrated no statistically significant reduction in medication errors with electronic health interventions compared with usual care. Across four studies, the random-effects pooled odds ratio (OR) was 0.627 (95% CI, 0.071–5.526; p=0.675). This corresponds to an estimated 37.3% relative reduction in the odds of medication errors; however, the confidence interval was extremely wide and included both a substantial reduction and a potentially large increase in errors. Therefore, the pooled estimate does not provide conclusive evidence that electronic health interventions reduce medication errors.

The direction of the random-effects estimate favored electronic interventions, but the magnitude of the observed effect was highly uncertain. The corresponding fixed-effects analysis produced an OR of 0.590 (95% CI, 0.444–0.783; p<0.001), suggesting an estimated 41.0% relative reduction in the odds of medication errors. However, this estimate assumes a common underlying intervention effect across studies and is difficult to interpret in view of the substantial between-study variability. Accordingly, the random-effects result is the more appropriate summary for the primary analysis.

Consistency across studies was very low. Statistical heterogeneity was considerable, with I²=98.2%, Q=168.88 (p<0.001), and τ²=4.8297. This indicates that nearly all of the observed variability in study estimates was attributable to differences between studies rather than sampling error alone. The pooled result should therefore be interpreted as an average across markedly different effects, rather than as an effect that is expected to apply uniformly across healthcare settings or electronic interventions.

The study-level findings appear to have varied substantially, with some studies likely favoring electronic interventions and others showing little benefit or effects in the opposite direction. The available pooled output does not identify which individual study had the largest effect or which provided the most precise estimate; these findings require review of the individual study estimates and confidence intervals. The extreme heterogeneity and wide random-effects confidence interval suggest that one or more studies may have been influential or may have functioned as outliers. Potential explanations include differences in the type and implementation of the electronic intervention, healthcare setting, baseline medication-error rates, outcome definitions, ascertainment methods, duration of follow-up, and the extent to which clinicians actually used the intervention. Overall, although the fixed-effects model suggested a statistically significant reduction, the highly heterogeneous random-effects analysis provides insufficiently precise evidence to establish a consistent reduction in medication errors.

### Risk of Bias

Risk of bias was a consistent concern across the 9 included studies. At the overall study level, 8 studies were judged as high risk of bias and 1 study as unclear risk; no study was judged as low risk. At the domain level, the pattern was even more striking: all 9 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In other words, for each of the six assessed domains, concerns were present in 9/9 studies because the relevant methodological details were not reported. This suggests that the main source of bias was not one isolated weakness, but pervasive underreporting across core design and conduct domains.

Across studies, the risk-of-bias profile was highly uniform rather than study-specific. Because all six domains were unclear in every included study, there was no meaningful separation between studies with stronger versus weaker internal validity on the available information, and no subgroup pattern could be established by study design, including RCTs versus observational studies, from the extracted reports alone. Although one study was classified overall as unclear risk, this appears to reflect uncertainty rather than reassuring methods; conversely, the 8 studies judged overall high risk were not distinguished by one clearly documented problematic domain, but by the same absence of reporting across multiple domains. There were therefore no studies at clearly low risk to anchor the evidence base, and no individual study could be identified as methodologically robust on the reported information.

This risk-of-bias pattern reduces confidence in the pooled estimate. With uncertainty surrounding sequence generation, allocation concealment, blinding, attrition handling, and selective reporting in all 9 studies, the summary effect may be vulnerable to systematic overestimation or underestimation, and the direction and magnitude of any bias cannot be determined reliably. The enhanced extraction quality assessment was relatively strong overall, with 8 studies rated high confidence and 1 medium confidence, indicating that these judgments likely reflect genuine limitations in the source reporting rather than extraction error. Taken together, the evidence base should be interpreted cautiously: while the meta-analytic estimate may describe the available literature, confidence in its validity is limited because the underlying studies lack adequate reporting across all major risk-of-bias domains.

## Discussion

**Discussion**

This systematic review found that electronic health interventions aimed at medication-use processes may reduce medication errors, but the certainty of that conclusion is limited by substantial inconsistency across studies. In the random-effects meta-analysis of four studies, the pooled odds ratio was 0.627 (95% CI 0.071-5.526; p=0.6746), which is compatible with benefit, no effect, or even harm. By contrast, the fixed-effect model suggested a statistically significant reduction in medication errors (OR 0.590, 95% CI 0.444-0.783; p=0.0003). Given the extreme heterogeneity observed (I²=98.2%, Q=168.88, p<0.001; tau²=4.8297), the random-effects estimate is the more appropriate summary and indicates that the overall effect is uncertain. Across the nine included studies, however, the direction of inquiry consistently reflected the expectation that CDS, EHR, eMAR, CPOE, and BCMA can improve medication safety by addressing known vulnerabilities in prescribing, dispensing, transcription, and administration. Clinically, even a modest reduction in medication errors would be important because these errors can lead to preventable adverse drug events, longer hospital stays, and avoidable costs; however, the present evidence does not support a precise estimate of effect size across settings.

These findings are broadly consistent with prior evidence showing promise for digital approaches in medication safety, while also underscoring the gap between technological potential and demonstrated clinical effectiveness. The recent scoping review of generative AI and large language models similarly concluded that such tools may assist with drug-drug interaction detection, clinical decision support, and pharmacovigilance, but that conclusive evidence for reducing real-world medication-related harm remains lacking because of heterogeneity and limited prospective evaluation. Our review aligns with that broader conclusion, although it focuses on more established operational technologies rather than emerging AI tools. Likewise, the umbrella review on barriers and facilitators to digital health adoption helps explain why effectiveness may vary in practice: technical infrastructure, workflow burden, and user acceptance can attenuate the impact of otherwise promising interventions, whereas training and perceived usefulness can strengthen implementation. The review of EHR-based drug repurposing is less directly comparable in terms of outcomes, but it reinforces a common theme in digital health research: data-rich systems have considerable potential, yet translation into measurable clinical benefit depends on data quality, integration into care processes, and local implementation conditions. Thus, disagreement between promising conceptual benefits and mixed pooled effectiveness estimates is not surprising.

There are plausible clinical mechanisms by which these interventions could reduce medication errors. CDS can provide dose checks, allergy alerts, renal dosing recommendations, and drug-drug interaction warnings at the point of prescribing; CPOE can eliminate illegible handwriting and standardize orders; eMAR and BCMA can strengthen the verification of the right patient, drug, dose, route, and time during administration; and EHR integration can improve access to medication histories and laboratory data relevant to safe prescribing. At the same time, these same systems can introduce new risks if poorly designed or implemented. Alert fatigue may cause clinicians to override important warnings, interface complexity can promote workarounds, and incomplete interoperability may create gaps between prescribing, dispensing, and administration records. This dual potential for benefit and harm provides a credible explanation for why some studies may have shown substantial reductions in errors while others showed smaller effects or no clear benefit.

The most important explanation for the statistical heterogeneity in this review is likely clinical and methodological diversity across the included studies. The interventions were not a single technology but a heterogeneous group ranging from CDS and CPOE to BCMA and eMAR, each acting at different stages of the medication-use pathway and with different implementation requirements. Study settings also varied across hospitals, clinics, and pharmacies, where baseline error rates, staffing models, workflow complexity, and patient acuity differ substantially. Outcome definitions were another likely source of variation, because "medication errors" may include potential errors, actual errors, and adverse drug events, which are related but not equivalent outcomes. In addition, differences in study design, follow-up duration, local maturity of digital infrastructure, and comparator conditions grouped under "usual care" likely contributed to effect variation. The contrast between the statistically significant fixed-effect result and the highly uncertain random-effects result strongly suggests that the observed evidence should not be interpreted as a single common treatment effect.

This review has several strengths. First, it synthesizes evidence across a clinically important set of electronic interventions that directly target medication safety in real-world healthcare settings. Second, most included studies were judged to be high quality by the enhanced extraction process (8 high, 1 medium), which supports confidence in the general rigor of the evidence base, even though not all studies contributed usable quantitative data to the meta-analysis. Third, the use of enhanced extraction appears to have improved the capture of study-level methodological and outcome information, making it possible to identify where evidence was robust and where reporting remained insufficient. This is particularly relevant in digital health, where intervention descriptions, implementation details, and outcome definitions are often inconsistently reported. By distinguishing between studies that were eligible for narrative synthesis and those with sufficient data for effect estimation, the review provides a more transparent account of what the available evidence can and cannot support.

Several limitations should temper interpretation. Only four studies contributed to the pooled odds ratio, despite nine studies being included overall, which limits statistical power and makes the quantitative synthesis sensitive to between-study differences. The very high heterogeneity substantially reduces confidence in a single summary effect. In addition, the extracted records indicate important reporting gaps in several studies, including missing bibliographic metadata, absent sample sizes, lack of raw event counts, and insufficient detail on randomization, allocation concealment, or blinding in some cases. Although the enhanced extraction classified most studies as high quality overall, incomplete reporting still constrains appraisal of risk of bias and reproducibility of effect estimates. The included evidence also spans different intervention types and healthcare contexts, which supports breadth but limits direct generalizability to any one system or setting. Finally, as with most systematic reviews in digital health, the review is vulnerable to publication bias, selective outcome reporting, and rapid technological obsolescence, since interventions and implementation practices evolve faster than the evidence base.

From a clinical and policy perspective, these findings support cautious adoption of electronic medication-safety interventions as part of broader quality-improvement strategies, but not the assumption that any digital tool will automatically reduce medication errors. Health systems should prioritize implementation quality, workflow integration, staff training, and ongoing monitoring of unintended consequences such as alert fatigue and workaround behavior. For practice, the implication is to focus less on simple technology acquisition and more on sociotechnical fit. For research, the field needs better-designed comparative studies with standardized outcome definitions, transparent reporting of event counts and denominators, and clearer descriptions of intervention components and implementation context. Future studies should also distinguish effects on potential errors, actual errors, and adverse drug events, since these outcomes differ in both clinical importance and causal proximity to the intervention. Meta-analyses will remain difficult until reporting improves, but that itself is a useful finding: the next generation of digital medication-safety research should aim not only to test effectiveness, but to make results comparable, reproducible, and decision-relevant.

## Conclusion

In this meta-analysis of 9 studies, including 4 in the quantitative synthesis, electronic health interventions (such as CDS, EHR, eMAR, CPOE, and BCMA) were not associated with a statistically reliable reduction in medication errors compared with usual care in the random-effects model (pooled OR 0.627, 95% CI 0.071–5.526; p=0.6746). Although the fixed-effects model suggested benefit (OR 0.590, 95% CI 0.444–0.783), the extremely high heterogeneity (I²=98.2%) indicates that effects varied markedly across settings and technologies. Clinically, this means electronic systems may reduce medication errors in some healthcare environments, but their impact is not consistent enough to assume benefit universally. These interventions should therefore be implemented as part of a broader medication-safety strategy, with attention to local workflow, training, and system design, given the substantial between-study variability and imprecision of the pooled estimate.

## Final Included Studies

- Corpus ID: 2574 | Integration of a Commercial Barcode-Assisted Medication Dispensing System in a Teaching Hospital.
- Corpus ID: 119610 | Comparing safety, performance and user perceptions of a patient-specific indication-based prescribing tool with current practice: a mixed methods randomised user testing study.
- Corpus ID: 114478 | Implementation of a new health information technology for the management of cancer chemotherapies.
- Corpus ID: 2579 | Unintended effects of a computerized physician order entry nearly hard-stop alert to prevent a drug interaction: a randomized controlled trial.
- Corpus ID: 114471 | Improving medication safety in a paediatric hospital: a mixed-methods evaluation of a newly implemented computerised provider order entry system.
- Corpus ID: 139124 | Integration of the Codonics Safe Label System® and the Omnicell XT® Anesthesia Workstation into Pediatric Anesthesia Practice: Utilizing Technology to Increase Medication Labeling Compliance and Decrease Medication Discrepancies While Maintaining User Acceptability.
- Corpus ID: 118925 | Effectiveness of computerised alerts to reduce drug-drug interactions (DDIs) and DDI-related harm in hospitalised patients: a quasi-experimental controlled pre-post study.
- Corpus ID: 107258 | Clinical effectiveness of a cloud-based dual-layer prescription review system: provincial integration across internet and outpatient care.
- Corpus ID: 118928 | Evaluation of the Effect of Smart Pump Interoperability on Infusion Errors in the Pediatric Hospital Setting.
