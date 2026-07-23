# Deep Learning–Based AI Assistance for Clinician Skin Cancer Diagnosis: A Systematic Review of the Local MetaSyn PubMed Corpus With Meta-analytic Feasibility Assessment

## Abstract

This report systematically reviewed the **local MetaSyn PubMed corpus only** to answer whether **deep learning–based AI assistance improves clinicians’ diagnostic accuracy for skin cancer compared with the same task performed without AI assistance**. Searches were constrained to the user-specified date window (**2017-01-01 to 2022-11-08**) and the stated PI/ECO framework. Two focused corpus searches were available from the retrieval log and were used as the basis for screening. After title/abstract screening against the prespecified criteria, **4 primary studies** were included: one randomized controlled trial, one prospective before-and-after study, and two image-based reader/experimental augmentation studies. Review articles and non-deep-learning diagnostic aids were excluded.

Across included studies, the direction of effect was generally favorable to AI assistance, especially for **less-experienced clinicians**. The strongest real-world evidence came from a South Korean randomized controlled trial showing **higher overall diagnostic accuracy with AI assistance than without it (53.9% vs. 43.8%, p = .019)**, with benefit concentrated in **nondermatology trainees** rather than dermatology residents ([“Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms,” 2022](https://doi.org/10.1016/j.jid.2022.02.003)). A prospective before-and-after study similarly found an increase in trainee top-1 accuracy from **46.5% to 58.3%** after AI support ([“Augmenting the accuracy of trainee doctors…,” 2022](https://doi.org/10.1371/journal.pone.0260895)). Experimental reader studies also suggested that well-performing AI can improve clinician accuracy, but faulty AI can mislead clinicians, including experts ([“Human-computer collaboration for skin cancer recognition,” 2020](https://doi.org/10.1038/s41591-020-0942-0)).

A formal quantitative meta-analysis of **sensitivity and specificity** was **not feasible** from the retrieved local-corpus records alone because the abstracts did not consistently report 2×2 diagnostic tables or paired sensitivity/specificity estimates for aided versus unaided clinicians. My conclusion is that **pre-November 2022 evidence supports AI as a useful decision-support tool for nonexpert clinicians, but not as a substitute for clinicians, and not yet with sufficient evidence to claim a robust pooled sensitivity/specificity benefit across settings**.

---

## Introduction

Deep learning systems for melanoma and skin cancer recognition have often shown strong performance in benchmark image-classification studies. However, a central translational question is narrower and more clinically relevant: **does AI assistance improve clinicians’ own diagnostic performance when embedded into clinical or image-reading workflows?** Review literature from the local MetaSyn corpus consistently warned that high experimental performance does not guarantee real-world clinical benefit and that prospective randomized evidence was sparse by 2021 ([“Artificial intelligence for melanoma diagnosis,” 2021](metasyn://corpus/35140); [“Skin cancer classification via convolutional neural networks,” 2021](metasyn://corpus/114492)).

This report therefore focuses only on **primary studies comparing clinicians with and without deep learning assistance**.

---

## Methods

### Data Source

Only the **local MetaSyn PubMed corpus** was used for retrieval, as required. No external database searching was performed.

### Local Corpus Search Queries Used

The following retrieved search queries were available in the research context and formed the basis of screening:

1. **`pre-2022 melanoma skin cancer AI clinician reader study prospective crossover randomized with and without AI support dermatologist primary care effect size experience level sensitivity specificity biopsy decision`**
2. **`AI-assisted melanoma diagnosis real-world outcomes prospective study design dataset diversity biopsy decisions missed melanomas workflow efficiency external validation multicenter diverse populations dermatology primary care`**

Both searches returned candidate records from the local corpus search tool.

### Eligibility Criteria

#### Inclusion
Studies were included if they:
- compared **clinicians diagnosing skin lesions** **with vs. without deep learning–based AI assistance**;
- used **images of skin lesions or in-person visits**;
- included at least one **skin malignancy**;
- were primary research articles.

#### Exclusion
Studies were excluded if they:
1. used **pathology slides** rather than skin lesion images or in-person lesion assessment;
2. only compared **clinicians vs. AI**, without clinician-with-AI vs. clinician-without-AI data;
3. used **non-deep-learning** methods;
4. were reviews, editorials, or case reports;
5. were outside the date window (**after 2022-11-08** or before 2017).

### Screening Approach

Because the provided retrieval context included mostly title/abstract-level information, screening was conducted at the **record level** using the local corpus search results. Where the corpus indicated that no full-text sections were available, evidence was treated as **abstract-only**. This is important because outcome extraction was limited by the reporting depth of the retrieved records.

---

## Retrieval and Screening Results

### Retrieval Overview

The two local corpus searches surfaced overlapping candidate records. Most high-ranking records were either:
- reviews summarizing AI-vs-clinician performance,
- real-world prospective studies,
- or image-based reader studies involving AI support.

### Screening Table

| Corpus ID | Title | Year | Decision | Reason |
|---|---|---:|---|---|
| **2299** | *Human-computer collaboration for skin cancer recognition* | 2020 | **Include** | Deep learning AI support; clinician performance with vs. without AI; image-based skin cancer diagnosis |
| **2580** | *Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks* | 2020 | **Include** | Deep learning CNN support; physician decisions compared before and after AI assistance |
| **2582** | *Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study* | 2022 | **Include** | Real-world prospective study; clinicians with vs. without AI-assisted workflow |
| **114506** | *Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial* | 2022 | **Include** | Randomized clinician-with-AI vs. clinician-without-AI comparison in real-world practice |
| 118983 | *Effect of adding a diagnostic aid to best practice to manage suspicious pigmented lesions in primary care* | 2012 | Exclude | Outside date range; non-deep-learning diagnostic aid |
| 114494 | *Over-Detection of Melanoma-Suspect Lesions by a CE-Certified Smartphone App…* | 2022 | Exclude | Compared app/device performance vs. dermatologists; not clinician with vs. without AI assistance |
| 114492 | *Skin cancer classification via convolutional neural networks: systematic review of studies involving human experts* | 2021 | Exclude | Review article |
| 35140 | *Artificial intelligence for melanoma diagnosis* | 2021 | Exclude | Review article |
| 114484 | *Diagnostic performance of augmented intelligence with 2D and 3D total body photography…* | 2023 | Exclude | Outside end date |
| 35091 | *Diagnostic accuracy of artificial intelligence compared to family physicians and dermatologists…* | 2025 | Exclude | Outside date range; review/meta-analysis |

### Included Study Count

**4 studies** met the eligibility criteria.

---

## Characteristics of Included Studies

| Corpus ID | Design | Setting | Clinician group | Comparison | Key reported outcome |
|---|---|---|---|---|---|
| **2299** | Experimental human-computer collaboration study | Image-based workflows incl. telemedicine simulations | Multiple expertise levels | Physician alone vs. AI alone vs. physician+AI | Good-quality AI improved accuracy beyond either alone; faulty AI misled clinicians |
| **2580** | Three-stage reader study | Dermoscopic image interpretation | 60 physicians | Image alone / + clinical info / + CNN output | Accuracy improved to 86.9% with CNN support |
| **2582** | Prospective controlled before-and-after | Real-world tertiary centers | Nondermatologist trainees | Before vs. after AI assistance; control photo-review group | Top-1 accuracy rose 46.5% to 58.3% |
| **114506** | Randomized controlled trial | Real-world tertiary institute | Nondermatology trainees and dermatology residents | AI-assisted vs. unaided real-time diagnosis | Overall accuracy 53.9% vs. 43.8%; stronger effect in nondermatology trainees |

---

## Findings

## 1. Real-world evidence favored AI assistance, but mainly for nonexperts

The **strongest included evidence** came from the randomized controlled trial indexed as **Corpus ID 114506**. In 576 consecutive suspicious-lesion cases, the **AI-assisted group achieved 53.9% accuracy compared with 43.8% in the unaided group (p = .019)**. The benefit was concentrated among **nondermatology trainees**, while **dermatology residents did not show a statistically significant gain** ([“Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms,” 2022](https://doi.org/10.1016/j.jid.2022.02.003)).

This pattern matters. It suggests AI may be most useful where baseline dermatologic expertise is limited—such as primary care, emergency medicine, or trainee settings—rather than among already-trained dermatologists. That interpretation is reinforced by the prospective before-and-after study **Corpus ID 2582**, in which trainee doctors improved **Top-1 accuracy from 46.5% before assistance to 58.3% after assistance (p = .008)**, whereas a control workflow involving only photographic review did not significantly improve accuracy ([“Augmenting the accuracy of trainee doctors…,” 2022](https://doi.org/10.1371/journal.pone.0260895)).

### Concrete interpretation
My view is that the best pre-2022 evidence supports a **targeted deployment model**: AI assistance is more likely to produce clinically meaningful benefit for **nondermatologists and novice clinicians** than for dermatology specialists.

---

## 2. AI assistance may broaden diagnostic reasoning, not just top-choice accuracy

Two prospective studies also reported a broader **differential diagnosis list** when AI support was present. In the randomized trial, trainees with AI generated **more differential diagnoses (2.09 vs. 1.95; p = .0005)** ([“Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms,” 2022](https://doi.org/10.1016/j.jid.2022.02.003)). In the before-and-after study, the number increased from **1.9 to 2.2** after AI assistance ([“Augmenting the accuracy of trainee doctors…,” 2022](https://doi.org/10.1371/journal.pone.0260895)).

This is more than a minor educational detail. In skin cancer triage, considering a broader malignant differential can influence biopsy thresholds, referral behavior, and follow-up intensity. While the included studies did not provide pooled biopsy-decision metrics suitable for meta-analysis, the expansion of differentials is a plausible pathway through which AI assistance improves safety for less-experienced clinicians.

---

## 3. Experimental reader studies showed promise, but also exposed a major safety risk

The 2020 Nature Medicine study (**Corpus ID 2299**) reported that **good-quality AI support improved diagnostic accuracy beyond either physicians alone or AI alone**, and that **the least experienced clinicians gained the most**. However, it also found that **faulty AI could mislead clinicians across the full expertise spectrum, including experts** ([“Human-computer collaboration for skin cancer recognition,” 2020](https://doi.org/10.1038/s41591-020-0942-0)).

The randomized trial (**Corpus ID 114506**) documented this failure mode quantitatively: **when all top-three AI predictions were wrong, trainees’ Top-1 accuracy dropped by 12.2%** ([“Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms,” 2022](https://doi.org/10.1016/j.jid.2022.02.003)).

That figure is one of the most practically important numbers in this evidence base. It shows that AI is not merely “sometimes unhelpful”; it can **actively degrade clinician performance** through automation bias. Therefore, any implementation strategy that emphasizes average accuracy gains without accounting for harmful AI failures is incomplete.

### Concrete interpretation
My opinion is that **automation-bias risk is not a side issue; it is central to the benefit-risk balance**. Any clinical deployment lacking confidence display, out-of-distribution detection, or override safeguards is inadequately justified by the pre-2022 evidence.

---

## 4. Image-based augmentation studies support decision support, but clinical generalizability is limited

The acral lentiginous melanoma reader study (**Corpus ID 2580**) found that physician accuracy improved from **74.7%** with dermoscopic images alone and **79.0%** with added clinical information to **86.9%** after CNN support. Inter-reader concordance also increased substantially ([“Augmented decision-making for acral lentiginous melanoma detection…,” 2020](https://doi.org/10.1111/jdv.16185)).

This is encouraging, but it was still a constrained image-based task focused on **acral lentiginous melanoma**, not a broad real-world lesion mix. Its role in the evidence hierarchy is therefore supportive rather than definitive.

---

## Meta-analysis Feasibility Assessment

Although the review question specifies sensitivity and specificity, a **formal pooled meta-analysis was not possible** from the local-corpus records retrieved here. The main reasons were:

1. **Missing 2×2 data** for aided and unaided clinician decisions.
2. **Inconsistent reporting metrics**, with several studies reporting top-1 accuracy rather than sensitivity and specificity.
3. **Heterogeneous designs**, including randomized trials, before-after studies, and staged reader experiments.
4. For several key records, the evidence available in the local corpus context was **abstract-only**.

Therefore, this report provides a **systematic qualitative synthesis with structured quantitative extraction where available**, rather than a statistical pooling of sensitivity and specificity.

---

## Context From Review-Level Evidence

The included primary studies should be interpreted alongside the broader review literature retrieved from the same corpus. The 2021 systematic review of 19 reader studies (**Corpus ID 114492**) concluded that CNN classifiers were generally **superior or equivalent to clinicians**, but emphasized that nearly all studies used **artificial single-image test settings and unrepresentative holdout datasets** ([“Skin cancer classification via convolutional neural networks,” 2021](metasyn://corpus/114492)). Similarly, the 2021 melanoma AI review (**Corpus ID 35140**) stressed that strong experimental performance **does not necessarily translate into good clinical performance** and that reliable prospective randomized trials were largely missing as of that time ([“Artificial intelligence for melanoma diagnosis,” 2021](metasyn://corpus/35140)).

These review-level findings align closely with the primary studies: promising augmentation effects exist, but the evidence base is narrow, trainee-heavy, and methodologically heterogeneous.

---

## Limitations

### Limitations of the review process
- This review was restricted to the **local MetaSyn corpus retrieval results provided**.
- Several important records had **no available full-text sections** in the corpus or were only available as abstract-level retrieval in the provided context.
- No additional corpus fetches were available here to extract fuller outcome tables.

### Limitations of the underlying evidence
- Only **4 eligible studies** were identified.
- Real-world evidence was dominated by **South Korean trainee populations**.
- Outcomes often focused on **accuracy**, not full diagnostic parameters.
- Sensitivity/specificity and biopsy decision outcomes were insufficiently reported for pooled analysis.
- Automation bias and AI failure modes were demonstrated, meaning average gains may conceal clinically important harms.

---

## Conclusion

The local MetaSyn corpus supports a clear but bounded conclusion: **deep learning–based AI assistance improved clinician skin cancer diagnostic performance in the small pre-November 2022 evidence base, especially among less-experienced clinicians, but the evidence is not strong enough to support a general claim of pooled sensitivity/specificity improvement across all clinician groups and workflows**.

The most defensible position is that **AI should be treated as supervised decision support, not autonomous diagnosis**. The randomized and prospective studies suggest real benefit for trainees and nondermatologists, yet the same evidence also shows a meaningful risk of **automation bias when AI is wrong**. In my judgment, the literature available up to November 8, 2022, justifies **careful, guarded clinical adoption for augmentation of nonexperts**, but **does not justify routine reliance without safety layers, clinician oversight, and prospective validation in broader populations**.

---

## Included-Study List

1. **Human-computer collaboration for skin cancer recognition** — **Corpus ID: 2299**
2. **Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks** — **Corpus ID: 2580**
3. **Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study** — **Corpus ID: 2582**
4. **Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial** — **Corpus ID: 114506**

---

## References

- *Artificial intelligence for melanoma diagnosis*. (2021). Italian Journal of Dermatology and Venereology. [metasyn://corpus/35140](metasyn://corpus/35140)
- *Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks*. (2020). Journal of the European Academy of Dermatology and Venereology. [https://doi.org/10.1111/jdv.16185](https://doi.org/10.1111/jdv.16185)
- *Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study*. (2022). PLOS ONE. [https://doi.org/10.1371/journal.pone.0260895](https://doi.org/10.1371/journal.pone.0260895)
- *Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial*. (2022). The Journal of Investigative Dermatology. [https://doi.org/10.1016/j.jid.2022.02.003](https://doi.org/10.1016/j.jid.2022.02.003)
- *Human-computer collaboration for skin cancer recognition*. (2020). Nature Medicine. [https://doi.org/10.1038/s41591-020-0942-0](https://doi.org/10.1038/s41591-020-0942-0)
- *Skin cancer classification via convolutional neural networks: systematic review of studies involving human experts*. (2021). European Journal of Cancer. [metasyn://corpus/114492](metasyn://corpus/114492)