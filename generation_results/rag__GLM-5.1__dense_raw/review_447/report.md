**Evidence Synthesis Report: Federated Learning in Breast, Lung, and Prostate Cancer**

**1. Review Scope and Methodology**
This systematic review examines whether federated learning (FL) approaches improve machine learning (ML) model generalizability and performance in breast, lung, and prostate cancer research compared to traditional centralized or single-centre ML methods, while preserving privacy. The review screened titles and abstracts from a fixed candidate pool of 200 articles against predefined inclusion criteria: peer-reviewed empirical studies published between January 1, 2020, and September 1, 2023; focusing on FL techniques for breast, lung, or prostate cancer; involving a comparative evaluation of FL models against centralized or single-centre baselines; and reporting quantitative clinical or diagnostic outcomes. Reviews, editorials, non-English publications, studies outside the specified cancer types, and studies lacking the required comparative framework were excluded.

**2. Screening Results**
Of the 200 candidates, the vast majority were excluded for being published outside the target date range (especially 2024-2026 publications), being reviews or non-empirical commentaries, focusing on cancer types other than breast, lung, or prostate (e.g., melanoma, colorectal, pancreatic), or employing distributed infrastructures without training an FL model against a centralized/single-centre baseline. Several FL studies in the target cancers were excluded because their abstracts indicated comparisons only against other FL variants (e.g., FedAvg vs. custom FL) rather than against centralized or single-institution models, or they merely reported the performance of an FL model without a baseline comparison. Only two primary studies met all stringent inclusion criteria, both published in 2023.

**3. Synthesis of Included Evidence**

*   **Model Generalizability and Performance vs. Centralized/Local Baselines:** The included evidence supports the premise that FL improves model generalizability and diagnostic performance over single-centre (local) models and can achieve performance on par with centralized approaches. 
    *   In prostate cancer (Candidate 001), a cross-site FL framework trained on over 1,400 heterogeneous multi-parametric MRI exams from two university hospitals demonstrated significant improvements in cross-site generalization. Compared to single-institution models, the FL model improved cross-site lesion segmentation intersection-over-union (IoU) by 100% and cross-site lesion classification accuracy by 9.5–14.8%, with negligible degradation in intra-site performance.
    *   In breast cancer (Candidate 010), an FL framework was used to predict histological response to neoadjuvant chemotherapy (NACT) in triple-negative breast cancer (TNBC) across multiple centers. The study found that while local ML models could predict response, collaborative FL training further improved performance, reaching parity with the best current centralized approaches that rely on time-consuming expert annotations and pooled data.

*   **Privacy-Preserving Collaborative Training:** Both studies explicitly highlight the privacy advantages of FL. Candidate 001 notes that FL improves generalization while protecting patient health information and institution-specific code and data. Candidate 010 emphasizes that FL allows collaborative training on real-world multicentric datasets without aggregating patient data behind a single firewall, overcoming the biases of small-scale local studies while respecting data privacy.

*   **Cancer-Type Specific Findings:** Eligible evidence was found for prostate and breast cancers. Despite several candidates discussing distributed learning infrastructures or FL applications for lung cancer (e.g., AusCAT network candidates), these either lacked the required comparative performance evaluation against centralized baselines in their abstracts or focused solely on infrastructure feasibility rather than FL model performance. Consequently, no eligible primary studies evaluating FL against centralized baselines specifically for lung cancer were identified in this candidate pool.

**4. Limitations and Gaps**
The evidence base within the specified timeframe and candidate pool is limited to two studies. Both studies demonstrate FL's superiority or parity compared to local/single-centre models, but the evidence for FL consistently outperforming fully pooled, centralized models trained on the same aggregated data is less direct—Candidate 010 achieves parity with centralized approaches, while Candidate 001 focuses on cross-site generalization gains over local models. Furthermore, the lack of eligible lung cancer studies representing FL vs. centralized comparisons prevents conclusions being drawn for that specific cancer type within this review. Future research should prioritize explicit head-to-head comparisons between FL and centralized pooled-data models across all three cancer types, particularly lung cancer.

---

**Included Primary-Study Articles**

*   Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology. (Corpus ID: 2666)
*   Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer. (Corpus ID: 2655)
