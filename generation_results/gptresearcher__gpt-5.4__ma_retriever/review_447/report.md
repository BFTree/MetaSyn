# Systematic Review Report: Federated Learning for Breast, Lung, and Prostate Cancer Imaging/ML in the Local MetaSyn PubMed Corpus

## Abstract

This report evaluates whether federated learning (FL) improves model generalizability and performance in breast, lung, and prostate cancer research relative to traditional centralized or single-center machine learning, while preserving privacy in multi-center settings. Using only the local MetaSyn PubMed corpus retrieval results provided, I screened candidate studies against prespecified eligibility criteria: peer-reviewed English-language empirical studies published between January 1, 2020 and September 1, 2023; focused on breast, lung, or prostate cancer; using FL; and reporting a comparative framework against centralized/single-center baselines with quantitative clinical ML outcomes.  

The retrieval strongly identified a prostate cancer FL literature and a smaller breast cancer FL literature, but very limited lung cancer evidence in the visible candidate set. After screening, **one study was clearly eligible based on the visible retrieved metadata and reported outcomes**: **Corpus ID 2666**, a 2023 multicenter prostate MRI study showing large cross-site generalization gains from FL with minimal intra-site penalty. Several additional records were highly relevant but were excluded because they were reviews, outside the date window, lacked a qualifying comparator, involved non-target cancers, or had insufficient visible metadata to verify eligibility. Because only one study was formally includable from the retrieved evidence, **a quantitative meta-analysis was not feasible**.  

My overall judgment is concrete: **the local corpus supports a strong, specific conclusion that FL can materially improve cross-site generalization in prostate cancer MRI compared with site-local training, but it does not yet support a broad cross-cancer conclusion across breast, lung, and prostate under the strict review criteria used here**. Breast cancer evidence is promising but mostly methodologically non-comparable or outside the time/comparator window; lung cancer evidence was not retrieved in a form that met eligibility.  

---

## Introduction

Federated learning has become attractive in oncology AI because multi-center data are valuable for generalization, yet patient privacy, institutional governance, and technical silos often prevent raw data pooling. In principle, FL allows collaborative model training without transferring patient-level data. The key review question here is not merely whether FL is feasible, but whether it improves **generalizability and performance** relative to traditional centralized or single-center machine learning in **breast, lung, and prostate cancer**.

The local MetaSyn corpus contains several relevant FL studies in cancer imaging, especially prostate MRI and breast pathology/imaging. Across broader summaries in the retrieved material, FL repeatedly appears to improve out-of-site performance while preserving privacy, although heterogeneity, communication overhead, convergence issues, and standardization remain major barriers ([“Federated learning in computational pathology: a literature review,” 2025](metasyn://corpus/75033)). However, this review applies **stricter inclusion criteria** than a narrative overview: target cancers only, specified publication window, empirical FL, and a comparator against centralized or site-local training.

---

## Methods

### Review Question

Does federated learning improve machine-learning model generalizability and performance in breast, lung, and prostate cancer research compared with traditional centralized or site-local machine learning methods, while enabling privacy-preserving collaborative training on multi-center data?

### Eligibility Criteria

#### Inclusion
- Peer-reviewed articles
- Published between **2020-01-01** and **2023-09-01**
- English language
- Breast, lung, or prostate cancer
- Federated learning intervention
- Comparative framework versus centralized aggregated ML or single-center/local baseline
- Quantitative clinical oncology ML outcome(s): classification, detection, segmentation, regression, etc.

#### Exclusion
- Reviews, editorials, commentaries
- Non-oncology or non-target cancers
- No FL method
- No quantitative oncology outcome
- No qualifying comparator
- Outside date range
- Insufficient retrieved metadata to verify eligibility

### Local Corpus Search Queries Used

The report is based on the local MetaSyn corpus searches shown in the retrieval record. The queries used were:

1. **`federated learning medical imaging prostate breast multicenter pooled baseline centralized comparison local baseline same architecture test set cross-site robustness`**
2. **`multicenter federated learning medical imaging heterogeneity mitigation personalization domain adaptation harmonization curriculum learning differential privacy cross-institution robustness modality comparison`**

No external retrieval source was used.

---

## Retrieval and Screening

### Retrieval Summary

The provided local corpus search outputs returned **20 candidate records per search**, with substantial overlap. The visible set was dominated by:
- prostate cancer FL studies,
- breast cancer FL studies,
- FL reviews/systematic reviews,
- methodological FL papers not necessarily meeting the comparator requirement,
- and some non-target or out-of-window records.

### Screening Logic

I screened the visible candidate records and the directly supplied corpus summaries for:
1. target cancer,
2. date window,
3. empirical FL,
4. comparator relevance,
5. oncology outcome reporting,
6. and sufficient bibliographic/abstract detail.

### Screening Results Table

| Corpus ID | Year | Target cancer | FL used | Comparator meets review question? | Decision | Main reason |
|---|---:|---|---|---|---|---|
| 2666 | 2023 | Prostate | Yes | Yes, versus site-local/single-institution training | **Included** | Clear multicenter prostate MRI study with quantitative cross-site outcomes |
| 2662 | 2021 | Cancer imaging, but tumor site unclear in visible excerpt | Yes | Yes vs institutional models | Excluded | Population not verifiably limited to breast/lung/prostate from visible metadata |
| 2659 | 2021 | Prostate | Yes | No, mainly FL variant vs standard FL | Excluded | No direct centralized/site-local comparator meeting criteria |
| 2660 | 2022 | Prostate / skin lesion | Yes | No, personalized FL vs shared global FL | Excluded | Comparator not traditional centralized/site-local ML |
| 2665 | 2023 | Breast | Yes | Unclear; abstract emphasizes comparison to conventional FL | Excluded | Qualifying centralized/site-local comparator not clearly established |
| 98564 | 2025 | Prostate | Yes | Yes | Excluded | Outside date window |
| 115530 | 2024 | Breast | Yes | Yes vs standalone and FL without adaptation | Excluded | Outside date window |
| 73950 | 2025 | Breast MRI | Yes | Yes | Excluded | Outside date window |
| 75033 | 2025 | Mixed | Review | N/A | Excluded | Review article |
| 75030 | 2026 | Histopathology | Review | N/A | Excluded | Review article |
| 73558 | 2022 | Histopathology, not target cancer-specific | Yes | Yes | Excluded | Non-target population / simulated distributed setup |
| 2658 | 2024 | Breast | Yes | FL vs centralized | Excluded | Outside date window |
| 2655 | Unclear from visible retrieval excerpt | Breast (TNBC) | Yes | Yes vs local models | **Not formally included** | Highly relevant, but retrieved excerpt lacked title/year needed for eligibility verification |

### PRISMA-Style Narrative

- **Records retrieved from local corpus searches:** 40 candidate records reported across two searches (with overlap).
- **Records screened from visible retrieved set:** all visible, relevant oncology FL records in the provided outputs.
- **Excluded after screening:** most records, due to review status, out-of-window publication date, missing qualifying comparator, or unverifiable tumor/site eligibility.
- **Studies included in qualitative synthesis:** **1**
- **Studies included in quantitative meta-analysis:** **0** (not feasible)

---

## Included Study

## 1. Multicenter Prostate MRI FL Study

### Study
**Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology** (Corpus ID **2666**), published in *Academic Radiology* in 2023 ([“Federated Learning with Research Prototypes…,” 2023](metasyn://corpus/2666)).

### Why It Was Included
This study clearly met all major criteria:
- prostate cancer population,
- empirical FL,
- peer-reviewed,
- within date window,
- quantitative oncology outcomes,
- multicenter clinical imaging,
- and explicit comparison against site-specific/local training with held-out cross-site evaluation.

### Study Design and Outcomes
The study trained prostate cancer detection models using **1400+ heterogeneous mpMRI exams from two university hospitals**. It reported:
- **100% relative improvement** in cross-site lesion segmentation IoU,
- **9.5%–14.8% improvement** in cross-site lesion classification accuracy,
- with **negligible intra-site degradation** ([“Federated Learning with Research Prototypes…,” 2023](metasyn://corpus/2666)).

### Interpretation
This is strong evidence that FL can reduce institution-specific overfitting in prostate MRI. The most important point is not just that FL improved average performance, but that the gain was concentrated in **cross-site robustness**, exactly the outcome most relevant to clinical deployment in multi-center oncology AI. The study therefore supports the idea that collaborative decentralized training creates a more transportable model than isolated site-local training ([“Federated Learning with Research Prototypes…,” 2023](metasyn://corpus/2666)).

---

## Findings From Excluded but Informative Contextual Evidence

Although not formally included, several retrieved records help interpret the broader landscape.

### Prostate Cancer: Strongest Support for FL, but Comparator Designs Vary

A later 2025 prostate MRI simulation study (Corpus ID **98564**) found that FL configuration matters substantially: optimized FL improved prostate segmentation Dice from **0.73 to 0.88** and csPCa detection PI-CAI score from **0.63 to 0.74** relative to the average of local client models; FedMedian worked best for segmentation and FedAdagrad for detection ([“Optimizing Federated Learning Configurations for MRI Prostate Segmentation and Cancer Detection,” 2025](metasyn://corpus/98564)). This is outside the review window, so it was excluded, but it deepens interpretation of the included 2023 prostate finding: **FL effectiveness is not binary; configuration and aggregation strategy materially affect results**.

Other prostate FL papers emphasized heterogeneity management rather than centralized comparison. Variation-Aware FL (Corpus ID **2659**) used privacy-preserving synthetic images and CycleGAN-based harmonization into a common image space, stably outperforming standard horizontal FL for clinically significant prostate cancer classification ([“Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data,” 2021](metasyn://corpus/2659)). Customized FL (Corpus ID **2660**) showed that personalized local models can outperform a single shared global model when client data are heterogeneous ([“Customized Federated Learning for Multi-Source Decentralized Medical Image Classification,” 2022](metasyn://corpus/2660)). These studies were excluded because their comparators were mainly **FL-versus-FL** rather than FL versus centralized/site-local baselines, but they explain *why* the included prostate study likely succeeded: cross-client heterogeneity is a core bottleneck, and personalization/harmonization may be crucial for the next generation of clinical FL.

### Breast Cancer: Promising, but Formal Eligibility Was Harder to Satisfy

The breast cancer FL literature in the local corpus is promising but less cleanly aligned with the review question.

A 2023 breast cancer classification study (Corpus ID **2665**) reported that a memory-aware curriculum FL method improved AUC and PR-AUC by about **5% and 6%**, respectively, relative to a conventional federated setting across three vendor datasets ([“Memory-aware curriculum federated learning for breast cancer classification,” 2023](metasyn://corpus/2665)). However, the visible abstract did not clearly establish the required centralized/site-local baseline.

A 2024 federated transfer learning breast cancer study (Corpus ID **115530**) reported **98.8% accuracy** and better generalization than both standalone training and FL without domain adaptation across three centers ([“Privacy-Preserving Breast Cancer Classification: A Federated Transfer Learning Approach,” 2024](metasyn://corpus/115530)). This is highly relevant conceptually but outside the date window.

The supplied contextual summary for Corpus ID **2655** described a real-world multicentric FL setup for **triple-negative breast cancer** using whole-slide images and clinical data, where collaborative FL outperformed local models and achieved performance comparable to approaches requiring costly expert annotations ([Source summary for Corpus ID 2655](metasyn://corpus/2655)). This is exactly the kind of study that could matter clinically, especially for rare, fragmented cohorts. However, because the retrieval excerpt available here did not expose the study title and year, I could not verify it against the formal date/title requirements, so I did **not** count it as included. Still, it meaningfully suggests that FL may be especially useful for rare breast cancer subtypes where no single center has sufficient data.

### Lung Cancer: Evidence Gap in the Retrieved Set

Within the visible local corpus retrieval provided here, I did **not** identify a clearly eligible lung cancer FL study meeting the date, disease, comparator, and quantitative outcome criteria. That absence matters. It means the present local-corpus evidence base cannot support any disease-wide inference that includes lung cancer.

---

## Synthesis and Interpretation

### What the Included Evidence Actually Supports

Under strict screening, the most defensible conclusion is:

1. **For prostate cancer MRI, FL improves cross-site generalization compared with site-local training.**
2. The benefit appears concentrated in **out-of-site robustness**, with little penalty to within-site performance.
3. FL’s success is likely moderated by **heterogeneity management**, **personalization**, and **aggregation strategy**.

This is more specific and more credible than claiming that FL is uniformly superior across all oncology contexts.

### Why the Evidence Is Not Yet Broad Enough

Despite many promising FL papers, the local corpus shows a recurring problem: studies often compare
- one FL variant to another FL variant,
- or FL to local training only,
- or are outside the date window,
- or do not provide a disease-restricted population matching the review question.

That means the evidence base remains **methodologically fragmented**. Reviews in the corpus also emphasize persistent barriers: data heterogeneity, communication overhead, slow convergence, interoperability, and limited standardization ([“Federated learning in computational pathology: a literature review,” 2025](metasyn://corpus/75033); [“Federated Learning for Histopathology Image Classification: A Systematic Review,” 2026](metasyn://corpus/75030)).

### Concrete Opinion

My opinion, based strictly on the retrieved local corpus and screening rules, is this:

> **Federated learning is already convincing as a privacy-preserving strategy for improving cross-site generalization in prostate cancer MRI, but the current eligible evidence in this review is too thin to justify a generalized superiority claim across breast, lung, and prostate cancer.**  

That is not a weak conclusion; it is a precise one. The strongest trustworthy signal is prostate MRI. Breast cancer is promising but not yet sufficiently captured by eligible head-to-head studies in the retrieved time window. Lung cancer is an evidence gap here.

---

## Limitations

1. **Local retrieval only:** This report was intentionally limited to the provided MetaSyn local corpus retrieval outputs.
2. **Visible metadata constraints:** Some potentially eligible studies, especially Corpus ID **2655**, lacked enough exposed metadata in the provided retrieval excerpt to verify title/year.
3. **Abstract-only evidence:** Several relevant studies were abstract-only in the local corpus snapshot, including Corpus IDs **2659**, **2660**, **2665**, and **98564**. Their interpretation is therefore more limited.
4. **No feasible meta-analysis:** Only one study was clearly includable, and outcome measures were heterogeneous across the broader literature.
5. **Comparator inconsistency:** Many FL papers compare against local baselines or alternative FL methods rather than a true pooled centralized model, limiting direct causal comparison.

---

## Conclusion

Using the local MetaSyn corpus alone and applying the stated eligibility criteria, the review identified **one clearly eligible study**: a 2023 multicenter prostate MRI investigation showing that federated learning substantially improved cross-site lesion segmentation and classification with negligible intra-site loss. This supports FL as a practical privacy-preserving route to better generalization in prostate cancer imaging.

However, the broader claim that FL improves model generalizability and performance across **breast, lung, and prostate cancer** compared with traditional centralized approaches is **not yet established by the eligible local-corpus evidence retrieved here**. The breast literature is encouraging but either out of window, comparator-incomplete, or insufficiently verifiable in the provided excerpt. Lung cancer evidence was not retrieved in eligible form. Accordingly, the evidence is **strong but narrow**, not broad.

---

# Clearly Identified Included-Study List

1. **Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology** — **Corpus ID: 2666**

---

## References

- *Customized Federated Learning for Multi-Source Decentralized Medical Image Classification.* [metasyn://corpus/2660](metasyn://corpus/2660)
- *Federated Learning for Histopathology Image Classification: A Systematic Review.* [metasyn://corpus/75030](metasyn://corpus/75030)
- *Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.* [metasyn://corpus/2666](metasyn://corpus/2666)
- *Federated learning improves site performance in multicenter deep learning without data sharing.* [metasyn://corpus/2662](metasyn://corpus/2662)
- *Federated learning in computational pathology: a literature review.* [metasyn://corpus/75033](metasyn://corpus/75033)
- *Memory-aware curriculum federated learning for breast cancer classification.* [metasyn://corpus/2665](metasyn://corpus/2665)
- *Optimizing Federated Learning Configurations for MRI Prostate Segmentation and Cancer Detection: A Simulation Study.* [metasyn://corpus/98564](metasyn://corpus/98564)
- *Privacy-Preserving Breast Cancer Classification: A Federated Transfer Learning Approach.* [metasyn://corpus/115530](metasyn://corpus/115530)
- *Source summary for triple-negative breast cancer multicentric FL study.* [metasyn://corpus/2655](metasyn://corpus/2655)
- *Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data.* [metasyn://corpus/2659](metasyn://corpus/2659)