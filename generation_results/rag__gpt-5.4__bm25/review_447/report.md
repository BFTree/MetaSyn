## Title/abstract screening result

Using only the supplied 200-candidate pool and applying the full eligibility criteria at title/abstract level, **2 primary studies were eligible** for inclusion.

A large number of candidates were excluded because they were:
- outside the date window (after 2023-09-01),
- reviews, platforms, or methods papers without an eligible oncology evaluation,
- not focused on breast, lung, or prostate cancer,
- not clearly using federated learning in an eligible clinical oncology task, or
- **did not report a qualifying comparison framework** against centralized/single-centre baselines.

Notably, some lung-cancer FL papers in the pool appeared relevant to privacy-preserving collaboration, but their abstracts did **not clearly report the required FL-versus-centralized/single-centre comparison**, so they were not retained.

---

## Included evidence at a glance

### 1) Breast cancer
This evidence came from one 2023 multicentre TNBC study using federated learning on whole-slide images and clinical data.

- The abstract states that **local ML models could predict response**, but **collaborative federated training further improved performance**.
- The study addresses a clinically relevant precision-oncology task: **prediction of histological response to neoadjuvant chemotherapy**.

### 2) Prostate cancer
This evidence came from one 2023 multicentre MRI study.

- The abstract reports that FL produced **significant improvements in cross-site generalization** with **negligible intra-site performance degradation**.
- Quantitatively, cross-site performance improved by:
  - **100% for lesion segmentation IoU**
  - **9.5–14.8% for lesion classification overall accuracy**

### 3) Lung cancer
From the supplied pool, **no lung-cancer paper met all criteria at abstract level**. Relevant lung FL studies mainly described infrastructure, feasibility, or distributed model development, but the abstracts did not clearly provide the required centralized/single-centre comparator framework.

---

## Narrative evidence synthesis

### Overall direction of findings
Among the included studies, the evidence points in a **consistent positive direction**: federated learning was associated with better cross-site or multicentre model behavior than non-federated single-site/local alternatives.

Across breast and prostate cancer:
- FL was used to train models on **distributed multi-centre data without sharing raw patient data**.
- The main apparent benefit was **improved generalizability across sites** rather than simply higher within-site performance.
- The included studies both target clinically meaningful oncology tasks:
  - treatment-response prediction in triple-negative breast cancer,
  - lesion detection/segmentation/classification in prostate MRI.

### What the included abstracts support
From title/abstract information alone, the strongest supported conclusions are:
1. **Federated learning is feasible in real multicentre cancer settings** for breast and prostate cancer.
2. **Performance gains appear to come mainly from access to broader distributed data**, improving cross-site robustness/generalizability.
3. **Privacy-preserving collaboration is a central motivation** in both studies.

### What remains uncertain
Because this synthesis is restricted to abstracts:
- exact model architectures, sample splits, and bias controls are incompletely reported;
- breast-cancer effect sizes are described directionally, but **not numerically in the abstract**;
- direct FL-versus-fully centralized pooled-data comparisons were not always explicit; in the included studies, the practical comparison was chiefly against **local/single-centre models**.

So, the evidence suggests benefit, but it is still **limited and methodologically heterogeneous**.

---

## Main limitations of the evidence base

1. **Very small eligible evidence base**
   - Only 2 studies met all criteria from the supplied pool.

2. **Cancer-type imbalance**
   - Included evidence covered **breast** and **prostate**, but not **lung** under the review’s strict comparator rule.

3. **Comparator inconsistency**
   - Many otherwise relevant FL oncology papers did not clearly compare against centralized or single-centre baselines in the abstract.

4. **Abstract-only constraints**
   - Risk of bias, dataset overlap, exact performance metrics, and implementation details cannot be reliably assessed beyond what the abstracts state.

---

## Bottom-line conclusion

Based on the eligible studies in the supplied pool, **federated learning shows promising evidence of improving multicentre model generalizability and/or performance in breast and prostate cancer applications while preserving data privacy**. The clearest reported gain is in **cross-site generalization**, especially in prostate MRI. However, the evidence base is **small, lacks eligible lung-cancer studies under the review criteria, and is limited by incomplete abstract reporting**. Therefore, the conclusion is **supportive but preliminary**.

---

## Final included primary studies

1. **Corpus ID: 2655**  
   **Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.**

2. **Corpus ID: 2666**  
   **Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.**
