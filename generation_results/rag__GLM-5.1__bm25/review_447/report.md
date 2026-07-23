Based on the screening of the supplied candidate pool against the inclusion and exclusion criteria, two primary studies were identified as eligible for this systematic review. Both studies focus on federated learning (FL) applications in breast or prostate cancer, employ FL methods on multi-centre data, and explicitly evaluate their models against single-centre (local) or centralized baselines as required by the comparative framework criterion.

**Evidence Synthesis**

The included studies investigate federated learning (FL) as a privacy-preserving mechanism to improve machine learning (ML) model generalizability and performance in oncology, specifically addressing the challenges of data silos and inter-institutional variability.

**Breast Cancer Application**
One study (Candidate 006) applied FL to predict histological response to neoadjuvant chemotherapy (NACT) in triple-negative breast cancer (TNBC) using whole-slide images and clinical data. The study demonstrated that while local ML models trained on single-institution data could predict response, collaborative training via FL significantly improved performance. Crucially, the FL model's performance was found to be on par with the best current centralized approaches that rely on time-consuming expert annotations, achieving this without sharing patient data across hospitals. This supports the premise that FL can match centralized benchmark performance while overcoming privacy barriers and data scarcity inherent in rare cancer subtypes like TNBC.

**Prostate Cancer Application**
Another study (Candidate 011) introduced a flexible FL framework for cross-site training and validation of deep learning algorithms for prostate cancer detection using multi-parametric MRI. The study evaluated a custom 3D UNet (UCNet) across two university hospitals using heterogeneous data. The results indicated that FL led to significant improvements in cross-site generalization performance (intersection-over-union improved by 100% for segmentation; accuracy improved by 9.5-14.8% for classification) with negligible degradation in intra-site performance compared to models trained on single-centre data. This finding highlights FL's utility in enhancing model robustness and transferability across institutions with diverse imaging protocols and histopathology definitions, a common hurdle in prostate MRI interpretation.

**General Findings**
Both studies confirm that FL enables collaborative model training on distributed oncology data without compromising patient privacy. They provide empirical evidence that FL models generalize better across institutions than single-centre models and can achieve performance levels comparable to or exceeding centralized baselines, thereby addressing the dual challenges of data privacy and model generalizability in multi-centre cancer research.

---

**Included Primary-Study Articles**

1. **Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.**
   Corpus ID: 2655

2. **Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.**
   Corpus ID: 2666
