**Systematic Review Evidence Synthesis: Federated Learning for Breast, Lung, and Prostate Cancer Models**

**Review question:** Does federated learning (FL) improve model generalizability and performance compared to centralized machine learning in breast, lung, and prostate cancer research, while preserving privacy in multi‑centre data?

**Methods**  
A pool of 200 candidate articles (supplied) was screened against predefined inclusion and exclusion criteria. Studies were required to be peer‑reviewed empirical articles published between 2020‑01‑01 and 2023‑09‑01, focusing on FL in breast, lung, or prostate cancer, with a comparative framework evaluating FL against a centralized (single‑centre or aggregated) baseline, and reporting clinical/quantitative oncology outcomes. Reviews, editorials, non‑English publications, and studies not employing FL or not addressing the target cancers were excluded. Titles and abstracts were assessed independently; full texts were not available beyond the supplied information.

**Results of screening**  
After applying the date and topic filters, 198 of the 200 candidates were excluded. The vast majority fell outside the 2020–2023 publication window, were reviews or non‑empirical, addressed other diseases or non‑medical domains, or did not implement federated learning with a comparative centralized baseline. Only two primary studies met all inclusion criteria: one in breast cancer and one in prostate cancer. No lung‑cancer FL study within the pool satisfied the criteria.

These two studies employ FL to train models across multiple institutions without sharing patient data and directly compare the resulting federated model to single‑centre (local) models, providing evidence on generalizability and performance.

**Synthesis of included evidence**

1. **Breast cancer – Federated learning for predicting histological response to neoadjuvant chemotherapy in triple‑negative breast cancer (Corpus ID: 2655, 2023)**  
   This multi‑centre study used whole‑slide images and clinical data to predict pathological complete response to neoadjuvant chemotherapy in early triple‑negative breast cancer. Local models trained at individual centres achieved some predictive ability, but collaboratively training the same model architecture via FL further improved performance. The federated model reached accuracy comparable to the best published approaches that require time‑consuming expert annotations. The study demonstrates that FL can leverage real‑world, multi‑institutional data without compromising privacy, yielding a model that is sensitive to specific histological patterns and interpretable. The comparison between local (single‑centre) and FL models directly addresses the review question, showing a clear gain in generalizability.

2. **Prostate cancer – Federated Learning with Research Prototypes: Application to Multi‑Center MRI‑based Detection of Prostate Cancer with Diverse Histopathology (Corpus ID: 2666, 2023)**  
   This work developed a flexible FL framework for cross‑site training of a custom 3D U‑Net (UCNet) for prostate cancer detection and segmentation on multiparametric MRI. Using over 1400 exams from two university hospitals, the authors compared models trained only on single‑site data with those trained via FL. The federated model significantly improved cross‑site generalization: lesion segmentation IoU doubled, and per‑lesion classification accuracy for clinically significant cancer increased by 9.5–14.8 percentage points, while intra‑site performance remained stable. The study highlights that FL can overcome domain shift between institutions and protect patient health information, directly addressing the review’s interest in generalizability and privacy.

**Limitations of the evidence base**  
Only two studies from the supplied pool were eligible, both published in 2023. Neither study included a lung cancer FL application that met the criteria, and no prostate or breast study compared FL to a pooled centralized model (the comparisons were to single‑site models). The small number of studies precludes formal meta‑analysis. The evidence is encouraging but remains limited; larger, multi‑cancer FL studies with rigorous centralized baselines are needed.

**Conclusion**  
The available evidence from the fixed candidate pool indicates that federated learning can improve model generalizability and performance over single‑centre models in breast and prostate cancer imaging tasks, while maintaining data privacy. These findings align with the review’s hypothesis, but the evidence base is narrow and should be interpreted with caution.

**Included primary‑study articles**

1. **Federated learning for predicting histological response to neoadjuvant chemotherapy in triple‑negative breast cancer.**  
   Corpus ID: 2655

2. **Federated Learning with Research Prototypes: Application to Multi‑Center MRI‑based Detection of Prostate Cancer with Diverse Histopathology.**  
   Corpus ID: 2666

No other candidate in the pool was eligible for inclusion.
