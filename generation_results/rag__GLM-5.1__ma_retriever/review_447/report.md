## Evidence-Synthesis Report

### Overview
This systematic review aimed to examine whether federated learning (FL) approaches improve machine learning (ML) model generalizability and performance in breast, lung, and prostate cancer research compared to traditional centralized or single-centre ML methods, while preserving privacy on multi-centre data. Based on the supplied candidate pool and the strict application of the inclusion and exclusion criteria, two primary studies met all eligibility requirements. Both eligible studies focus on prostate and breast cancer; no eligible studies concerning lung cancer were identified that both utilized FL and explicitly compared it against centralized or single-centre baselines within the specified timeframe.

### Evidence Synthesis
The two included studies provide empirical support that federated learning enhances model generalizability and diagnostic performance in multi-centre oncology settings compared to traditional single-centre training, while successfully addressing privacy constraints.

**Prostate Cancer:** 
Candidate 002 evaluated an FL framework for cross-site training and validation of deep learning algorithms for prostate cancer detection using multi-parametric MRI from over 1,400 heterogeneous exams across two university hospitals. The study demonstrated significant improvements in cross-site generalization compared to single-centre baselines, with cross-site lesion segmentation Intersection-over-Union (IoU) improving by 100% and per-lesion binary classification accuracy improving by 9.5–14.8%. Crucially, these cross-site gains were achieved with negligible degradation in intra-site performance, underscoring FL's capacity to protect patient health information while delivering models that generalize robustly across institutions.

**Breast Cancer:**
Candidate 005 applied FL to predict histological response to neoadjuvant chemotherapy (NACT) in triple-negative breast cancer (TNBC) using multicentric whole-slide images and clinical data. The authors reported that while local single-centre ML models could predict NACT response, collaborative FL training further improved performance. Specifically, the FL model's performance was found to be on par with the best current centralized approaches that rely on large, time-consuming expert annotations. This highlights FL's utility not only in overcoming small-scale single-centre biases and preserving data privacy but also in achieving diagnostic performance comparable to centralized models trained on pooled data.

**Lung Cancer:**
Although several candidates discussed lung nodules or lung cancer in the context of FL or distributed learning (e.g., Candidates 019, 023, 035), none met the strict inclusion criteria requiring a direct comparative evaluation of an FL model against centralized or single-centre ML baselines on the same datasets, alongside a clear focus on FL methodology within the 2020–2023 window.

### Conclusions
The synthesized evidence suggests that federated learning is an effective paradigm for improving ML model generalizability and diagnostic accuracy in breast and prostate cancer tasks compared to single-centre models. FL achieves performance levels comparable to or better than centralized training without the need to aggregate sensitive patient data across institutions. However, the lack of eligible lung cancer studies in this specific candidate pool meeting the comparative framework criterion indicates a current gap in the explicitly reported FL-vs-centralized literature for lung cancer within the reviewed timeframe. Future research should continue to prioritize standardized comparative evaluations against centralized baselines to validate FL's clinical applicability across all three cancer types.

---

### Included Primary-Study Articles

1. **Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.**
   Corpus ID: 2666

2. **Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.**
   Corpus ID: 2654
