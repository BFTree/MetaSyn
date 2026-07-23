**Systematic Review and Evidence Synthesis Report**

**Research Question:** Do federated learning (FL) approaches improve model generalizability and diagnostic performance in breast, lung, and prostate cancer research compared with traditional centralized machine learning, while enabling privacy-preserving collaborative training on multi‑centre data?

**Methods**
The candidate pool of 200 articles (published 2020‑01‑01 to 2023‑09‑01) was screened against pre‑defined eligibility criteria. Included studies must (a) be peer‑reviewed primary empirical research; (b) focus on breast, lung, or prostate cancer; (c) employ a federated learning framework for machine‑learning model training; (d) incorporate a comparative evaluation against a centralised (single‑centre or aggregated) baseline, either directly or through referenced literature; and (e) report quantitative, clinically relevant oncology outcomes (detection, diagnosis, prognosis, or treatment response). Reviews, editorials, non‑oncology studies, non‑FL studies, and articles outside the cancer‑type scope were excluded.

**Screening Results**
The 200 abstracts were examined independently. After applying all criteria, **2 primary‑study articles** qualified for inclusion. Common reasons for exclusion were: wrong publication year (after 2023), absence of a federated learning component, lack of a centralised comparator, irrelevance to breast/lung/prostate cancer, or non‑empirical article type (systematic reviews, surveys, protocols). No lung‑cancer FL study with a centralised comparator met all criteria within the permitted date range.

**Synthesis of Included Evidence**
The two included studies address prostate cancer (MRI‑based detection) and triple‑negative breast cancer (pathological response prediction), respectively. Both demonstrate that FL can improve model generalisation over purely local training while maintaining data privacy.

1. **Prostate cancer detection (Candidate 001)**  
   This multi‑centre study trained a custom 3D U‑Net (UCNet) for clinically significant prostate cancer detection and segmentation using 1400+ multiparametric MRI exams from two university hospitals. Federated training significantly enhanced cross‑site generalisation: lesion segmentation intersection‑over‑union doubled, and per‑lesion classification accuracy improved by 9.5–14.8 percentage points compared with models trained solely on single‑site data. Intra‑site performance remained essentially unchanged, indicating that FL effectively broadens model robustness without sacrificing local accuracy.

2. **Breast cancer treatment response prediction (Candidate 010)**  
   In a multicentric study of triple‑negative breast cancer, whole‑slide image features and clinical data were used to predict histological response to neoadjuvant chemotherapy. Local models demonstrated predictive ability, but collaborative FL training further improved performance, bringing it on par with the best current approaches that rely on labour‑intensive expert annotations. This study provides proof‑of‑concept that FL can unlock larger, privacy‑protected datasets to develop interpretable biomarkers in a rare cancer subtype.

Across both studies, FL consistently improved model generalisation to unseen sites. Gains were attributed to exposure to more heterogeneous data distributions during training, while avoiding the transfer of patient‑level data. Neither study identified privacy breaches or performance penalties that would hinder clinical adoption.

**Discussion and Gaps**
The evidence base remains sparse. Within the tightly defined search window, only two empirical comparisons of FL versus centralised training were found for the target cancer types—none for lung cancer. The identified studies are early‑stage proofs of concept with modest institutional participation (two hospitals in the prostate study; the number of centres is not explicitly stated in the breast cancer study but is described as multicentric). Key limitations include the absence of prospective clinical validation, small numbers of collaborating sites, and narrow clinical tasks (segmentation/classification of MRI and prediction of a single chemotherapy response endpoint). Future research should expand to more institutions, additional cancer types (especially lung), and broader endpoints such as survival, recurrence, and treatment selection, while continuing to rigorously compare FL models with centrally trained counterparts.

**Included Primary‑Study Articles**

1. **Candidate 001**  
   *Title:* Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.  
   *Corpus ID: 2666*

2. **Candidate 010**  
   *Title:* Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.  
   *Corpus ID: 2655*
