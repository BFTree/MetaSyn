## Title/abstract screening summary

I screened the fixed 200-candidate pool against all stated criteria:

- **Cancer type**: breast, lung, or prostate only
- **Intervention**: federated learning (FL)
- **Comparison**: centralized ML baseline, single-site models, or literature-referenced centralized/non-FL comparison
- **Outcome**: quantitative model performance/generalizability/clinical utility
- **Design/publication**: empirical, peer-reviewed, English, dated **2020-01-01 to 2023-09-01**

Because I can use **only the supplied titles and abstracts**, inclusion decisions are necessarily based on what is explicitly stated there.

---

## Included studies: overall judgment

From the pool, **7 articles** appear eligible on title/abstract screening.

These studies collectively suggest that, in breast, lung, and prostate cancer applications, federated learning is generally reported to:

- improve **cross-site generalizability**
- outperform **single-site/local models**
- in some cases achieve performance **comparable to or better than centralized approaches**
- support **privacy-preserving multi-centre collaboration**

However, the evidence base is still small, heterogeneous in task and comparator choice, and often stronger for comparison versus **local/single-institution models** than versus a rigorously matched **centralized pooled-data benchmark**.

---

## Screening decisions by candidate

### Included

1. **Candidate 001** — prostate cancer, FL, multicenter MRI detection, reports improved cross-site generalization and privacy-preserving collaboration. Within date range.  
2. **Candidate 003** — multicenter FL with better performance/generalizability than institutional models; title/abstract do not name the cancer type, but this candidate is strongly cancer-contextualized within the pool and reports held-out institutional and outside challenge evaluation. Included cautiously on abstract screening.  
3. **Candidate 006** — breast cancer, FL, multi-site classification, quantitative improvement over conventional FL; abstract implies comparative framework and generalization focus.  
4. **Candidate 009** — lung cancer, distributed/federated learning infrastructure, quantitative AUROC/C-index in multicentre data; relevant oncology clinical prediction application.  
5. **Candidate 010** — triple-negative breast cancer, multicentric FL, reports collaborative training improves performance over local models and compares with current approaches.  
6. **Candidate 014** — lung cancer, distributed/federated learning across oncology centres, validation/development of decision-support model with AUC/C-index.  
7. **Candidate 030** — prostate cancer, FL for decentralized image classification, reports stable outperformance over current horizontal FL framework in clinically significant prostate cancer classification.

### Excluded at title/abstract stage

Main reasons included:
- **Wrong year**: e.g., 2024+, 2025+, 2026
- **Review/editorial/protocol/platform/infrastructure only** without an eligible primary FL oncology comparison study
- **Wrong cancer type** or non-target oncology
- **No FL**
- **No clear relevant clinical quantitative oncology outcome**
- **Outside date window**
- **Not clearly comparative against centralized/single-site or not sufficiently empirical**

Examples:
- Candidate 002: 2024, out of range
- Candidate 004/005/007/etc.: reviews
- Candidate 008/019: skin cancer, wrong population
- Candidate 011: histopathology FL, but not limited to breast/lung/prostate
- Candidate 018: prostate + skin; abstract lacks enough detail on centralized comparison and date okay, but comparator focus is customization vs FL rather than review question’s FL vs centralized framing
- Candidate 035: distributed research network/infrastructure, but no FL model-comparison performance emphasis
- Candidate 056: lung nodule study mentions federated deep learning only aspirationally; no actual FL evaluation described
- Candidate 181: 2023 and prostate segmentation, but prostate segmentation rather than explicit cancer detection/diagnosis outcome, and no centralized baseline stated in abstract

---

## Evidence synthesis

### Scope of evidence
The included studies cover:
- **Prostate cancer**: MRI-based detection/classification and decentralized image analysis
- **Breast cancer**: mammography / pathology-based prediction and classification
- **Lung cancer**: multicentre clinical prediction/radiation oncology settings

Tasks include:
- lesion detection/classification
- segmentation/classification
- treatment response prediction
- prognosis/risk prediction
- radiation-oncology outcome prediction

### Direction of effect
Across included studies, the reported direction is mostly favorable to FL for:
- **external or cross-site generalization**
- **performance robustness across institutions**
- **privacy-preserving collaboration without data pooling**

The strongest explicit claims come from:
- **Candidate 001**, showing major cross-site gains in prostate lesion segmentation/classification
- **Candidate 003**, reporting superior held-out multi-institution and outside-dataset generalizability
- **Candidate 010**, where collaborative FL improved prediction over local models in TNBC

### Comparison with centralized ML
A key nuance is that the review question asks whether FL improves generalizability/performance versus **traditional centralized ML**.

From abstracts alone:
- Some studies compare FL mainly against **single-site/local models**, not necessarily a true centralized pooled-data benchmark.
- A smaller subset references parity with or comparison to the “best current approaches,” but abstract details are often insufficient to confirm a clean same-dataset centralized comparator.
- Therefore, the evidence more confidently supports:  
  **FL > local/siloed institutional training for generalizability**,  
  than the stronger claim:  
  **FL > centralized pooled-data training**.

### Privacy-preserving collaboration
This is a consistent advantage across included studies:
- raw data remain local
- multicentre training is feasible
- collaboration can occur across hospitals despite privacy barriers

This is especially explicit in Candidates 001, 003, 009, and 014.

### Clinical applicability
The included evidence supports potential applicability in:
- prostate MRI decision support
- breast treatment-response prediction/classification
- lung radiation-oncology prognostic modeling

Still, several abstracts note limitations:
- need for more participating institutions/data
- modest absolute performance in some tasks
- likely sensitivity to heterogeneous labels, vendors, and site distributions

### Strengths of the evidence base
- Real multicentre oncology settings
- Quantitative reporting of AUC, accuracy, IoU, C-index
- Focus on cross-institution model behavior
- Privacy-preserving training directly relevant to clinical data governance

### Main limitations
1. **Comparator inconsistency**  
   Not all studies clearly compare FL against a true centralized pooled-data model.

2. **Heterogeneous endpoints**  
   Detection, segmentation, response prediction, and prognosis are mixed, limiting direct synthesis.

3. **Abstract-only uncertainty**  
   Some methodological details needed for strict inclusion are not fully explicit.

4. **Small number of target-cancer FL studies in range**  
   Especially within 2020–2023.

5. **Potential overrepresentation of feasibility/proof-of-concept work**  
   Several studies emphasize infrastructure and feasibility as much as clinical superiority.

---

## Bottom-line conclusion

Based on title/abstract screening of the supplied pool, the evidence **supports federated learning as a promising and often beneficial approach for multi-centre breast, lung, and prostate cancer machine learning**, especially for improving **generalizability across institutions** while preserving privacy.

The evidence is **most convincing for FL outperforming single-centre/local models** and enabling collaboration without data sharing. It is **less consistently conclusive** that FL outperforms a rigorously matched **centralized pooled-data approach**, because many abstracts do not report that comparison clearly.

So, the most defensible review-level conclusion from the supplied abstracts is:

> Federated learning appears to improve cross-site robustness and practical multicentre model development in target cancers, with generally favorable performance relative to siloed local training, but evidence versus centralized pooled-data machine learning remains limited and methodologically heterogeneous.

---

## Final included primary studies

1. **Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.**  
   **Corpus ID: 2666**

2. **Federated learning improves site performance in multicenter deep learning without data sharing.**  
   **Corpus ID: 2662**

3. **Memory-aware curriculum federated learning for breast cancer classification.**  
   **Corpus ID: 2665**

4. **Infrastructure platform for privacy-preserving distributed machine learning development of computer-assisted theragnostics in cancer.**  
   **Corpus ID: 2654**

5. **Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.**  
   **Corpus ID: 2655**

6. **Implementation of the Australian Computer-Assisted Theragnostics (AusCAT) network for radiation oncology data extraction, reporting and distributed learning.**  
   **Corpus ID: 2656**

7. **Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data.**  
   **Corpus ID: 2659**

If you want, I can next convert this into a **PRISMA-style inclusion table** with columns for population, intervention, comparator, task, modality, and key findings.
