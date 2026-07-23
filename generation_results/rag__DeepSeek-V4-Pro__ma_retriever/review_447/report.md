**Systematic Review and Evidence Synthesis Report**

**Research Question:**  
This systematic review examines whether federated learning (FL) approaches improve machine learning model generalizability and performance in breast, lung, and prostate cancer research compared to traditional centralized machine learning methods, while addressing privacy‑preserving collaborative training on multi‑centre data.

**PICO Framework:**  
- **Population:** Patients with breast, lung, or prostate cancer (data from multi‑centre oncology studies).  
- **Intervention:** Federated learning approaches for training machine learning models on distributed, multi‑centre cancer data.  
- **Comparison:** Centralized machine learning models trained on single‑centre or aggregated data.  
- **Outcome:** Model generalizability, diagnostic performance, and clinical applicability in cancer detection, diagnosis, and precision medicine.  

**Search Strategy:**  
A fixed candidate pool of 200 articles (Corpus IDs 115530 to 61763) was supplied. Titles and abstracts were screened against the inclusion and exclusion criteria.

**Inclusion Criteria:**  
- Peer-reviewed articles published between 2020‑01‑01 and 2023‑09‑01.  
- Studies focusing on FL techniques in breast, lung, or prostate cancer.  
- Studies that directly compare the FL model against a centralized ML baseline developed on the same data (either through direct evaluation or by referencing reported literature values).  
- Clinical applications relevant to oncology (classification, segmentation, detection, regression).  

**Exclusion Criteria:**  
- Non‑English publications.  
- Non‑empirical articles (reviews, editorials, commentaries, protocols).  
- Articles not focused on breast, lung, or prostate cancer.  
- Studies not employing FL methods.  
- Studies not reporting clinical outcomes or quantitative assessments.

**Screening Results:**  
Each of the 200 candidates was examined. Many were excluded for a single reason, while others failed on multiple grounds. The main reasons for exclusion were:

- **Wrong publication year:** Candidates published after 2023‑09‑01 (e.g., 2024–2026) were removed.  
- **Irrelevant cancer type:** Numerous studies addressed skin cancer, pancreatic cancer, colorectal cancer, brain tumours, or other malignancies not within the breast/lung/prostate scope.  
- **Not a federated learning study:** The majority of candidates used traditional centralized machine learning, single‑site training, or other distributed learning paradigms (e.g., swarm learning, transfer learning without FL).  
- **Lack of a centralized baseline comparison:** Even when FL was used, the abstract often compared the FL model only to local (single‑site) models or to other FL variants, without referencing a centralized model trained on aggregated data.  
- **Review or non‑empirical article:** Several candidates were systematic reviews, position papers, or platform descriptions.  
- **No specific cancer population:** Some FL studies were applied to general medical data or non‑oncological conditions (e.g., COVID‑19, appendicitis, ECG), not breast, lung, or prostate cancer.

A few candidates superficially appeared relevant but fell short on closer inspection. For example, candidate 005 (federated learning for triple‑negative breast cancer) compared FL to local models and existing literature‑based approaches, but did not explicitly compare against a centralized baseline on the same dataset. Candidate 018 (federated learning improves site performance) did not specify the cancer type. Candidate 040 (FL‑based classification of COVID‑19 and chest diseases including lung cancer) compared FL to transfer learning models, not to a centralized ML baseline. None of these fully satisfied the requirement for a comparative framework against centralized ML.

**Final Included Primary‑Study Articles:**  
After rigorous screening, **no candidate met all inclusion criteria**.  

There is no eligible primary study that simultaneously (a) focuses on breast, lung, or prostate cancer, (b) employs a federated learning approach, (c) compares it against a centralized machine learning baseline, and (d) falls within the specified publication window.  

Therefore, the evidence synthesis cannot draw conclusions regarding the comparative performance of FL versus centralized ML in these cancer domains based on the supplied candidate pool.
