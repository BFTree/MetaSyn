# Systematic Review of Federated Learning vs Centralized Machine Learning in Breast, Lung, and Prostate Cancer Using the Local MetaSyn PubMed Corpus

## Review Question

Among peer-reviewed English-language studies published from 2020-01-01 through 2023-09-01 in the local MetaSyn PubMed corpus, the evidence was assessed to determine whether federated learning (FL) approaches used on distributed multi-centre datasets involving breast, lung, or prostate cancer improve:

- machine-learning generalizability,
- diagnostic or predictive performance, and
- clinical applicability

compared with traditional centralized machine-learning approaches trained on single-centre or aggregated data.

## Executive Summary

The local MetaSyn PubMed corpus yielded a **small and methodologically heterogeneous evidence base**. After focused retrieval and screening, **two studies met the core comparative intent of the review**, and **one additional breast-cancer FL study was relevant but only indirectly informative for the central FL-vs-centralized question**.

### Bottom-line findings

- **Prostate cancer evidence was the strongest.** One multi-centre MRI study showed that FL substantially improved **cross-site generalizability** compared with institution-specific local models, with:
  - **~100% improvement in cross-site lesion segmentation IoU**, and
  - **9.5% to 14.8% improvement in cross-site lesion classification accuracy**, while preserving local-site performance with only small degradation  
  ([Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.](local-metaSyn://corpus/2666) [1]).

- **Breast cancer evidence was promising but weaker.** One multicentric triple-negative breast cancer (TNBC) study reported that **collaborative FL training improved prediction of histological response to neoadjuvant chemotherapy beyond local models**, but the local corpus record was **abstract-only** and did **not report extractable effect sizes**  
  ([Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.](local-metaSyn://corpus/2655) [2]).

- **Direct evidence in lung cancer was not found** under the review’s comparator requirements. Relevant distributed-learning lung-cancer papers were retrieved, but they did not clearly report an FL-versus-centralized comparison in the available local corpus records  
  ([Infrastructure platform for privacy-preserving distributed machine learning development of computer-assisted theragnostics in cancer.](local-metaSyn://corpus/2654) [3]; [Implementation of the Australian Computer-Assisted Theragnostics (AusCAT) network for radiation oncology data extraction, reporting and distributed learning.](local-metaSyn://corpus/2656) [4]).

- **A formal meta-analysis was not feasible** because:
  - too few directly eligible comparative studies were found,
  - outcome measures were highly heterogeneous,
  - at least one included study was abstract-only and lacked numerical detail,
  - one otherwise relevant breast-cancer FL study compared FL variants rather than clearly comparing FL with centralized ML in the retrieved record  
    ([Memory-aware curriculum federated learning for breast cancer classification.](local-metaSyn://corpus/2665) [5]).

Overall, the local corpus supports the conclusion that **FL can improve cross-institution generalizability and can preserve privacy while enabling collaborative oncology model development**, but the evidence is **limited, uneven across cancer types, and not yet sufficient for pooled quantitative inference**.

---

## Methods

## Data Source

Only the **local MetaSyn PubMed corpus** was used, as required. No external databases were searched, and no source meta-analysis title was searched for or inferred.

## Search Strategy

Focused search queries were formulated directly from the research question and PI/ECO elements. The following exact local corpus queries were used:

1. `(federated learning) AND (breast cancer OR lung cancer OR prostate cancer) AND (2020[Date] : 2023/09/01[Date])`

2. `(federated learning OR distributed learning) AND (breast cancer OR triple-negative breast cancer OR mammography OR histopathology) AND (2020[Date] : 2023/09/01[Date])`

3. `(federated learning OR distributed learning) AND (prostate cancer OR lung cancer OR NSCLC) AND (MRI OR imaging OR radiotherapy OR histopathology) AND (2020[Date] : 2023/09/01[Date])`

### Retrieval Yield

- Query 1 returned **20 candidate records**
- Query 2 returned **20 candidate records**
- Query 3 returned **20 candidate records**

From these searches, the candidate records repeatedly identified as most relevant within scope were:

- **2666**
- **2655**
- **2665**
- **2660**
- **2659**
- **2654**
- **2656**

## Screening and Eligibility Criteria

### Inclusion criteria applied

- Peer-reviewed articles
- English-language
- Publication date from **2020-01-01 through 2023-09-01**
- Focus on **federated learning** in **breast, lung, or prostate cancer**
- Multi-centre/distributed clinical oncology relevance
- Comparative framework evaluating FL against:
  - centralized ML on the same data, or
  - local/single-centre models, or
  - literature-based comparator values if clearly used as comparison
- Quantitative oncology-relevant outcomes such as classification, segmentation, detection, regression, prognosis, or treatment-response prediction

### Exclusion criteria applied

- Non-English publications
- Reviews, editorials, commentaries, or other non-empirical papers
- Not focused on breast, lung, or prostate cancer
- Not using FL methods
- No clinical/quantitative oncology-relevant outcomes
- No sufficiently relevant comparative framework to address the review question

## Screening Process

Screening was performed on the **retrieved local corpus records only**. Where available, local corpus sections beyond the abstract were used. This mattered particularly for Corpus ID **2666**, for which methods, results, and conclusion sections were available. For several other records, only the abstract was available, limiting certainty.

---

## Candidate Studies and Eligibility Judgments

## Screening Table

| Corpus ID | Title | Cancer type | Comparator relevance | Eligibility judgment | Decision rationale |
|---|---|---|---|---|---|
| **2666** | *Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.* | Prostate | Direct local-vs-FL comparison | **Included** | Multi-centre prostate MRI FL study with quantitative comparison against locally trained models; strong relevance to generalizability and clinical applicability [1] |
| **2655** | *Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.* | Breast (TNBC) | Local models vs collaborative FL training | **Included** | Multicentric TNBC study; predictive oncology task; abstract reports improvement beyond local ML models, though numerical data are limited [2] |
| **2665** | *Memory-aware curriculum federated learning for breast cancer classification.* | Breast | FL variant vs conventional FL, not clearly centralized ML | **Borderline / indirect evidence** | Relevant breast-cancer FL paper with quantitative gains, but the retrieved record does not clearly satisfy the review’s core centralized-comparator requirement [5] |
| **2660** | *Customized Federated Learning for Multi-Source Decentralized Medical Image Classification.* | Prostate + non-target domain | No clear centralized comparator in retrieved record | **Excluded** | Cancer-relevant, but available abstract did not show the required FL-vs-centralized/local comparator framework [6] |
| **2659** | *Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data.* | Prostate | Compared to horizontal FL, not centralized ML | **Excluded** | Relevant FL methodology, but not the required comparison for this review question [7] |
| **2654** | *Infrastructure platform for privacy-preserving distributed machine learning development of computer-assisted theragnostics in cancer.* | Lung / NSCLC | No clear centralized comparator | **Excluded** | Infrastructure/feasibility paper with oncology relevance, but insufficient FL-vs-centralized comparison in the retrieved record [3] |
| **2656** | *Implementation of the Australian Computer-Assisted Theragnostics (AusCAT) network for radiation oncology data extraction, reporting and distributed learning.* | Lung / NSCLC | No clear centralized comparator | **Excluded** | Distributed learning implementation study, but not clearly a comparative FL-vs-centralized study in the available record [4] |

### Final inclusion set for core synthesis

The **core included comparative studies** were:

- **Corpus ID 2666**
- **Corpus ID 2655**

### Additional supportive but indirect study

- **Corpus ID 2665**

---

## Characteristics of the Included Evidence

## Included Study 1: Prostate Cancer

### [Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.](local-metaSyn://corpus/2666) [1]

- **Corpus ID:** **2666**
- **Year:** 2023
- **Cancer:** Prostate cancer
- **Clinical task:** MRI-based lesion segmentation and lesion-wise classification of clinically significant prostate cancer
- **Setting:** Multi-centre, two university hospitals
- **Data scale:** The record reports **1400+** heterogeneous multiparametric prostate MRI exams in the abstract and **1800+** exams in methods/conclusion text
- **Modeling approach:** FL for cross-site training of a custom 3D UNet (“UCNet”)
- **Comparator:** Local models trained independently at each institution
- **Available local corpus content:** Methods, results, and conclusion were available; this is **not abstract-only** [1]

### Main findings

This was the clearest direct study answering the review question.

The study reported that local models performed well on their own institution’s test data but generalized poorly to the external institution. FL improved external performance substantially:

- **Segmentation generalizability**
  - Cross-site lesion segmentation performance improved dramatically
  - The record reports **~100% improvement in cross-site IoU**
  - Local models could fail completely across sites, with one reported cross-site segmentation IoU of **0.000** for a local model [1]

- **Classification generalizability**
  - Cross-site lesion classification accuracy improved by **9.5% to 14.8%**
  - One local model achieved only **47.9% accuracy** on the other institution’s data
  - Another cross-site local result was **53.3% accuracy**, still far below within-site performance
  - FL increased true positive and true negative rates in the external site setting, making the model more practically usable across institutions [1]

- **Local performance trade-off**
  - The study reported **negligible or small decreases in local-site performance**, indicating that the improvement in generalizability did not come at a major cost to in-site utility [1]

### Interpretation

This study provides the strongest local-corpus evidence that FL can materially improve **cross-institution transportability**, which is a core practical dimension of clinical ML generalizability. It also directly supports the privacy-preserving value proposition of FL, because the collaboration occurred without centralizing patient data.

---

## Included Study 2: Breast Cancer

### [Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.](local-metaSyn://corpus/2655) [2]

- **Corpus ID:** **2655**
- **Year:** 2023
- **Cancer:** Triple-negative breast cancer
- **Clinical task:** Predicting histological response to neoadjuvant chemotherapy at diagnosis
- **Inputs:** Whole-slide images plus clinical information
- **Setting:** Multicentric TNBC study
- **Comparator:** Local ML models vs collaborative FL training
- **Available local corpus content:** **Abstract only** [2]

### Main findings

The abstract states that:

- local ML models using whole-slide images could predict response to neoadjuvant chemotherapy,
- **collaborative FL training further improved performance** over local models,
- the resulting approach was **on par with the best current approaches** that depend on time-consuming expert annotations,
- the model was described as **interpretable** and sensitive to specific histological patterns [2].

### Interpretation

This study is clinically important because treatment-response prediction in TNBC is directly relevant to therapy planning. However, because the local corpus record was **abstract-only**, the evidence is limited by the absence of:

- exact performance metrics,
- confidence intervals,
- details of the central/local comparator implementation,
- detailed external-validation structure.

It still contributes supportive evidence that FL may outperform isolated site-level learning in breast-cancer prediction tasks.

---

## Supportive but Indirect Evidence

## [Memory-aware curriculum federated learning for breast cancer classification.](local-metaSyn://corpus/2665) [5]

- **Corpus ID:** **2665**
- **Year:** 2023
- **Cancer:** Breast cancer
- **Available local corpus content:** **Abstract only**
- **Relevance:** Multi-site breast-cancer classification using three clinical datasets from different vendors
- **Reported outcomes:** Improved average ROC-AUC and PR-AUC over a conventional federated setting [5]

### Why it was not counted as core comparative evidence

This record appears relevant to FL optimization in breast-cancer classification, but the available record did **not clearly compare FL with centralized ML** or local single-centre models. Instead, it appears to compare one FL strategy with another FL setup. That makes it useful as contextual evidence for FL methodology, but not as a direct answer to the review’s main comparison.

---

## Evidence by Cancer Type

## Prostate Cancer

The local corpus provides the **best evidence** in prostate cancer.

- The included MRI-based study showed that FL improved both segmentation and classification generalizability across institutions [1].
- Two additional prostate-related FL studies were retrieved but excluded because the available records did not clearly provide the required comparator framework:
  - [Customized Federated Learning for Multi-Source Decentralized Medical Image Classification.](local-metaSyn://corpus/2660) [6]
  - [Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data.](local-metaSyn://corpus/2659) [7]

### Overall assessment for prostate cancer

Evidence supports a **positive effect of FL on out-of-site generalization**, particularly where institutional heterogeneity is large and local-only models degrade substantially on external data.

## Breast Cancer

Breast-cancer evidence is **promising but less complete**.

- The TNBC response-prediction study suggests FL improves predictive performance compared with local models [2].
- The memory-aware curriculum FL study supports the broader idea that FL design choices can improve breast-cancer classification performance across sites, but it does not directly resolve the centralized-comparator question in the retrieved record [5].

### Overall assessment for breast cancer

The local corpus suggests FL may be beneficial for **multicentre predictive and classification tasks**, but the evidence is limited by **abstract-only reporting** and insufficient detail for quantitative synthesis.

## Lung Cancer

Lung-cancer records were retrieved, but none met the review’s comparative requirement strongly enough to be included in the core synthesis.

Relevant retrieved records included:

- [Infrastructure platform for privacy-preserving distributed machine learning development of computer-assisted theragnostics in cancer.](local-metaSyn://corpus/2654) [3]
- [Implementation of the Australian Computer-Assisted Theragnostics (AusCAT) network for radiation oncology data extraction, reporting and distributed learning.](local-metaSyn://corpus/2656) [4]

### Overall assessment for lung cancer

The local corpus supports the **feasibility and infrastructure relevance** of distributed learning in lung-cancer/radiation-oncology settings, but does **not provide clear direct evidence** within the eligibility framework that FL outperforms centralized or local ML.

---

## Comparative Findings: FL vs Centralized or Local ML

## 1. Generalizability

This was the outcome with the clearest signal.

- In prostate MRI, FL markedly improved **cross-site generalization**, turning models that performed poorly or failed externally into models with materially better external-site utility [1].
- In TNBC, the multicentric FL framework was explicitly motivated as a way to overcome bias and limited scale while preserving data privacy; the abstract states that collaborative training improved performance over local models [2].

### Overall judgment

The local corpus evidence supports the proposition that FL can improve **generalizability across institutions**, especially where site-specific data distributions differ.

## 2. Diagnostic and Predictive Performance

The evidence is favorable but limited.

- Prostate MRI classification and segmentation both improved under FL in external-site testing [1].
- TNBC treatment-response prediction reportedly improved with FL relative to local modeling, but the lack of reported metrics prevents estimation of effect magnitude [2].

### Overall judgment

FL appears capable of improving diagnostic/predictive performance in multicentre oncology tasks, but only one study provided sufficiently detailed numerical evidence.

## 3. Clinical Applicability

Clinical applicability depends not just on internal performance but on whether a model remains useful outside the development site.

- In the prostate study, the record explicitly described local cross-site performance as low enough to limit usability, whereas FL improved performance enough to make the model “usable in practice” at another institution [1].
- In the TNBC study, the task itself—predicting histological response before neoadjuvant chemotherapy—is clinically actionable, and the reported interpretability adds translational relevance [2].

### Overall judgment

FL’s strongest clinical value in this corpus is **not merely higher average performance**, but better **practical cross-site deployability**.

## 4. Privacy-Preserving Collaborative Training

This was a consistent strength across the included and near-eligible literature.

- The prostate study explicitly emphasized protection of patient health information and institution-specific code/data during collaboration [1].
- The TNBC study stated that patient data remained behind hospital firewalls [2].
- The lung/radiation-oncology platform papers, though excluded from the core comparative synthesis, reinforce the operational importance of privacy-preserving distributed learning infrastructure [3][4].

### Overall judgment

Across the local corpus, privacy-preserving collaboration is a major rationale for FL and a likely enabler of larger, more representative oncology training datasets.

---

## Meta-analysis Feasibility

A meta-analysis was **not feasible**.

### Reasons

1. **Too few directly eligible studies**
   - Only **two core included studies