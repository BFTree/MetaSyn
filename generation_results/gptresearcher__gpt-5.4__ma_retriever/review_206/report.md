# Systematic Review Report: Early Clinical Evaluation Reporting of AI Decision Support Systems for Glaucoma Diagnosis and Progression Detection in the Local MetaSyn PubMed Corpus

## Abstract

This report systematically reviewed the local MetaSyn PubMed corpus to identify **early clinical evaluation studies** of artificial intelligence (AI) decision support systems for **glaucoma diagnosis** or **progression detection** and to assess whether the available literature would support evaluation against the **DECIDE-AI checklist**. Searches were restricted conceptually to English-language studies from **January 2020 to May 25, 2023**, involving glaucoma patients and AI/machine learning/deep learning for diagnosis or progression prediction. Candidate records retrieved from the local corpus were screened against the protocol’s inclusion and exclusion criteria, with special attention to whether studies were true **early clinical evaluation** investigations rather than retrospective algorithm-development papers.

The search results yielded a relevant cluster of glaucoma AI studies, including OCT-based diagnosis, multimodal diagnosis, visual-field progression classification, and angle-closure classification. However, after screening, **no study met the full eligibility standard for inclusion as an early clinical evaluation study of an AI decision support system suitable for DECIDE-AI adherence assessment**. Most candidate studies were retrospective diagnostic modeling papers, cross-sectional accuracy studies, or algorithm-development reports without prospective clinical workflow evaluation, human-AI interaction analysis, deployment context reporting, or clinician behavior/outcome assessment. This conclusion is reinforced by a recent review noting that direct evidence on AI clinical decision support changing clinician decisions in glaucoma progression is limited and that most studies focus on algorithm performance rather than prospective reader or implementation studies ([Lights and Shadows on Artificial Intelligence in Glaucoma: Transforming Screening, Monitoring, and Prognosis, Corpus ID 85404](metasyn://corpus/85404)).

My concrete conclusion is that, within the local corpus and time window of interest, the glaucoma AI literature was **methodologically mature in model benchmarking but underdeveloped in early clinical evaluation reporting**. In practical terms, this means there is currently **no includable evidence base in the local corpus for a DECIDE-AI adherence meta-analysis focused on early clinical evaluation studies**.

---

## Introduction

Artificial intelligence has been widely investigated in glaucoma for structural diagnosis from optical coherence tomography (OCT), fundus photography analysis, multimodal diagnosis, and visual field progression detection. Within the 2020–2023 literature, model performance is often strong. For example, a large 2021 *Translational Vision Science & Technology* study of **90,713 visual fields from 13,156 eyes** reported machine-learning classifiers with **87%–91% accuracy**, **0.83–0.88 sensitivity**, and **0.92–0.96 specificity** for visual-field progression, with less classification bias than conventional progression rules ([Development and Comparison of Machine Learning Algorithms to Determine Visual Field Progression, Corpus ID 85361](metasyn://corpus/85361)). Likewise, multimodal systems combining structural and functional data have often outperformed single-modality approaches. A 2022 *Ophthalmology* study reported that FusionNet achieved **AUC 0.950** in primary validation and remained superior on internal and external testing compared with VF-only and OCT-only models ([Multimodal Machine Learning Using Visual Fields and Peripapillary Circular OCT Scans in Detection of Glaucomatous Optic Neuropathy, Corpus ID 3196](metasyn://corpus/3196)).

Yet strong discrimination is not equivalent to **early clinical evaluation**. The present review is not asking whether glaucoma AI works in retrospective datasets; it is asking whether published studies reported **early clinical evaluation of AI decision support systems** in ways that can be assessed against the **DECIDE-AI checklist**, which emphasizes implementation context, users, workflow, human-AI interaction, safety, and iterative real-world evaluation.

That distinction is crucial. A 2025 review in the local corpus explicitly states that direct evidence on AI clinical decision support changing clinician decisions in glaucoma progression is limited, because most published studies focus on algorithm performance, risk prediction, or diagnostic/progression classification rather than prospective reader studies or patient outcomes ([Corpus ID 85404](metasyn://corpus/85404)). Although the review itself falls outside the inclusion window and is not an includable primary study, it provides useful context for interpreting the 2020–2023 evidence base.

---

## Methods

### Review Question

This systematic review asked:

> What published studies in the local MetaSyn corpus report **early clinical evaluation** of AI decision support systems for glaucoma diagnosis or progression detection, and how suitable are they for assessment using the **DECIDE-AI** checklist?

### Eligibility Criteria

#### Inclusion
Studies had to:
1. Be in English.
2. Be dated from January 2020 to May 25, 2023.
3. Include glaucoma patients.
4. Use AI, machine learning, or deep learning for glaucoma diagnosis or progression prediction.
5. Report **early clinical evaluation** of an AI decision support system.

#### Exclusion
Studies were excluded if they were:
- Review articles
- Letters
- Protocols
- Conference abstracts
- Non-human studies
- Pure algorithm-development or retrospective diagnostic-performance studies without early clinical evaluation

### Local Corpus Search Queries Used

The review used the local MetaSyn corpus search outputs supplied in the evidence package. The following queries were used:

1. **Query 1**  
   `(glaucoma) AND ((optical coherence tomography OR OCT OR fundus OR visual field OR multimodal)) AND (artificial intelligence OR machine learning OR deep learning) AND (diagnosis OR progression prediction) AND (clinical OR cohort OR external validation OR real-world) AND (2020:2023[pdat])`

2. **Query 2**  
   `2020 2021 2022 2023 early glaucoma pre-perimetric glaucoma detection AI high myopia real-world cohort OCT fundus deep learning sensitivity external validation`

These searches returned candidate records from the local corpus, from which relevant primary studies were screened.

### Screening Approach

I screened candidate studies in two stages:

1. **Topical and date relevance:** glaucoma + AI + diagnosis/progression, within the 2020 to May 2023 window.
2. **Study design relevance:** whether the paper represented an **early clinical evaluation** of an AI decision support system rather than retrospective model development, internal validation, or cross-sectional diagnostic benchmarking.

When full-text sections were unavailable in the local corpus, exclusion decisions were made from the abstract only, and this limitation is stated explicitly.

---

## Results

## Retrieval Summary

The search results identified multiple glaucoma-related AI papers, but only a subset fell within the date window and broad glaucoma-AI topic. The most relevant 2020–2023 candidate primary studies included:

- **85361** – visual field progression detection by machine learning
- **3196** – multimodal VF + OCT detection of glaucomatous optic neuropathy
- **3191** – multimodal AI for glaucoma detection in a high-myopia-heavy cohort
- **3188** – OCT-based machine-learning glaucoma diagnosis
- **3189** – SVM-based Spectralis OCT glaucoma detection
- **3194** – AI description of glaucomatous optic nerve head structure
- **3198** – angle-closure disease subtype classification using anterior segment OCT
- **84867** – broad ophthalmic AI overview/review

Additional 2024–2025 records were retrieved but excluded for date.

## Screening Findings

### Table 1. Screening of Key Candidate Records Against Eligibility Criteria

| Corpus ID | Year | Title (Short) | Topic-Relevant? | Early Clinical Evaluation? | Include? | Main Reason |
|---|---:|---|---|---|---|---|
| 85361 | 2021 | ML Algorithms to Determine Visual Field Progression | Yes | No | No | Large retrospective classifier study; no early clinical workflow evaluation ([85361](metasyn://corpus/85361)) |
| 3196 | 2022 | FusionNet VF + OCT for GON Detection | Yes | No | No | Cross-sectional multimodal diagnostic performance study; abstract-only in local corpus ([3196](metasyn://corpus/3196)) |
| 3191 | 2022 | Multimodal AI in High-Myopia Cohort | Yes | No | No | Screening/diagnostic model study; no human-AI implementation evaluation ([3191](metasyn://corpus/3191)) |
| 3188 | 2021 | ML Classifiers for Glaucoma Diagnosis Based on Spectralis OCT | Yes | No | No | Retrospective classifier comparison; no clinical deployment or user evaluation ([3188](metasyn://corpus/3188)) |
| 3189 | 2022 | SVM Glaucoma Detection Based on Spectralis OCT | Yes | No | No | Diagnostic modeling with need for future real-world validation explicitly noted ([3189](metasyn://corpus/3189)) |
| 3194 | 2022 | Structural Phenotype of the Glaucomatous ONH Using AI | Yes | No | No | Retrospective diagnosis study; abstract-only in local corpus ([3194](metasyn://corpus/3194)) |
| 3198 | 2023 | DL Classification of Primary Angle-Closure Disease | Partial | No | No | Glaucoma-adjacent angle-closure subtype classification, not early clinical evaluation; abstract-only ([3198](metasyn://corpus/3198)) |
| 84867 | 2022 | Overview of AI in Diabetic Retinopathy and Other Ocular Diseases | No | No | No | Review article ([84867](metasyn://corpus/84867)) |
| 85404 | 2025 | Lights and Shadows on AI in Glaucoma | Context only | No | No | Review article; outside date window ([85404](metasyn://corpus/85404)) |

### Included Studies

**No studies were included.**

No candidate study met the combined criteria of:
- glaucoma diagnosis/progression AI,
- 2020 to May 25, 2023,
- primary study,
- and **early clinical evaluation of a decision support system** in a manner assessable under DECIDE-AI.

---

## Narrative Synthesis of the Excluded Evidence Base

Although no studies were includable, the excluded literature still reveals important patterns relevant to the review question.

### 1. Progression detection was technically strong but not clinically evaluated

The strongest progression-related study was the 2021 TVST paper (Corpus ID **85361**). It used a very large dataset—**90,713 visual fields**—and showed that machine-learning classifiers could identify visual field progression with **87%–91% accuracy**, **0.83–0.88 sensitivity**, and **0.92–0.96 specificity**. Importantly, the study also found that conventional progression algorithms had significant class bias, whereas machine-learning classifiers were more balanced ([85361](metasyn://corpus/85361)). This is clinically meaningful because balanced classification may reduce systematic overcalling or undercalling of progression.

However, for DECIDE-AI purposes, this study still fails the core design requirement. It did not evaluate how clinicians used the system, whether it changed management decisions, how outputs were presented, or whether workflow integration was safe or acceptable.

### 2. Multimodal AI consistently outperformed single-modality models

The 2022 *Ophthalmology* FusionNet study (Corpus ID **3196**) provides some of the best evidence that combining structure and function improves glaucoma detection. FusionNet achieved **AUC 0.950** in primary validation and remained superior on internal and external testing versus OCT-only and VF-only models ([3196](metasyn://corpus/3196)). This is also aligned with later real-world-oriented work outside the date window and with broader multimodal trends.

Still, even excellent external validation across devices does not equal early clinical evaluation. The study appears to be a diagnostic technology performance study rather than an implementation study. Because only the abstract was available in the local corpus, that exclusion is necessarily based on abstract-level evidence.

### 3. Early disease and myopic populations remained major weaknesses

The 2022 BMC Medical Imaging study (Corpus ID **3191**) is especially informative because it examined glaucoma AI in a **high-myopia-prevalent population**, a setting known to complicate optic nerve and retinal interpretation. While the model achieved strong overall AUROC, **pre-perimetric glaucoma (PPG) sensitivity was only 30.27%**, despite good performance for normal and manifest glaucoma classes ([3191](metasyn://corpus/3191)). This is one of the most practically important findings in the corpus: headline AUROC can conceal poor early-disease sensitivity.

This point matters for DECIDE-AI because early clinical evaluation should surface precisely these clinically relevant weaknesses. A system that looks strong in aggregate but misses early disease would need careful prospective study before adoption.

### 4. OCT-based diagnostic modeling was common but rarely real-world

The Spectralis OCT studies (Corpus IDs **3188** and **3189**) illustrate the dominant 2021–2022 pattern: retrospective use of structured OCT parameters to build classifiers. In **3188**, random forest performed best, and ganglion cell layer measures were especially important for early glaucoma detection ([3188](metasyn://corpus/3188)). In **3189**, use of all Spectralis OCT features produced **AUC 0.82** overall and higher AUCs with increasing disease severity, while early glaucoma remained harder ([3189](metasyn://corpus/3189)).

Notably, **3189** explicitly stated that further real-world validation was needed. That statement is revealing. It means the authors themselves recognized the gap between diagnostic modeling and clinical evaluation.

### 5. The corpus itself supports the conclusion of an implementation gap

The most direct contextual support comes from the later systematic review (Corpus ID **85404**), which summarized the field and noted that direct evidence on AI clinical decision support changing clinician decisions in glaucoma progression is limited; most work has concentrated on algorithm performance rather than prospective reader studies or patient outcomes ([85404](metasyn://corpus/85404)). Although this review is outside the date window and excluded from the final study set, its interpretation matches the pattern observed across the screened 2020–2023 records.

---

## DECIDE-AI Relevance

The central objective was to identify studies suitable for scoring on:
- **AI-Specific Score**
- **Generic-Item Score**
- **Overall DECIDE-AI Score**

In practice, these candidate studies usually did **not** report the elements needed to score DECIDE-AI adequately:
- intended clinical users,
- placement in workflow,
- human factors,
- iteration during implementation,
- monitoring for unintended consequences,
- impact on clinician decisions,
- patient-facing or service-level outcomes,
- and governance of real-world use.

Because of this, the corpus does not merely show “low reporting quality”; it shows something more fundamental: **the target study type is largely absent**.

My judgment is that performing a quantitative meta-analysis of DECIDE-AI adherence from this corpus and time window would be **methodologically invalid**, because the necessary unit of analysis—early clinical evaluation studies—is missing.

---

## Limitations

### 1. Local-corpus-only constraint
This review used the local MetaSyn corpus search results as the only retrieval source, as required. That improves reproducibility within the corpus but may miss relevant studies absent from local indexing.

### 2. Abstract-only decisions for some studies
Some important records, including **3196**, **3194**, and **3198**, were available only at the abstract level in the local corpus. Exclusion decisions for those studies were therefore based on abstract evidence. I have stated this explicitly to avoid overstating certainty.

### 3. Search outputs included out-of-window records
The candidate lists contained 2024–2025 records despite the search intent. These were screened but excluded by date.

### 4. No full DECIDE-AI scoring was possible
Because no eligible early clinical evaluation study was found, actual DECIDE-AI scoring could not be performed.

---

## Conclusion

The local MetaSyn PubMed corpus contains substantial 2020–2023 literature on AI for glaucoma diagnosis and progression detection, including strong work on visual-field progression modeling, multimodal diagnosis, and OCT-based classification. The technical performance evidence is often impressive: machine learning reduced classification bias in progression detection, multimodal systems outperformed single-modality models, and real diagnostic challenges such as early disease and myopia were clearly exposed ([85361](metasyn://corpus/85361); [3196](metasyn://corpus/3196); [3191](metasyn://corpus/3191)).

However, none of the screened studies met the review’s **true target condition**: **early clinical evaluation** of an AI decision support system suitable for assessment under **DECIDE-AI**. The literature in this period was dominated by retrospective and cross-sectional performance studies rather than implementation-focused clinical evaluations. My concrete opinion is that this is not a mere reporting deficiency but a translational bottleneck: glaucoma AI research in 2020–2023 was strong at proving algorithms can classify disease, but weak at proving that clinicians can safely and effectively use those systems in practice.

Accordingly, **no study was included**, and **no valid DECIDE-AI adherence meta-analysis can be conducted from the eligible local-corpus evidence identified here**.

---

## Included-Study List

**No studies were included after screening.**

---

## References

- Development and Comparison of Machine Learning Algorithms to Determine Visual Field Progression. Corpus ID 85361. [metasyn://corpus/85361](metasyn://corpus/85361)
- Multimodal Machine Learning Using Visual Fields and Peripapillary Circular OCT Scans in Detection of Glaucomatous Optic Neuropathy. Corpus ID 3196. [metasyn://corpus/3196](metasyn://corpus/3196)
- Use of multimodal dataset in AI for detecting glaucoma based on fundus photographs assessed with OCT: focus group study on high prevalence of myopia. Corpus ID 3191. [metasyn://corpus/3191](metasyn://corpus/3191)
- Comparison of Different Machine Learning Classifiers for Glaucoma Diagnosis Based on Spectralis OCT. Corpus ID 3188. [metasyn://corpus/3188](metasyn://corpus/3188)
- Glaucoma Detection Using Support Vector Machine Method Based on Spectralis OCT. Corpus ID 3189. [metasyn://corpus/3189](metasyn://corpus/3189)
- Describing the Structural Phenotype of the Glaucomatous Optic Nerve Head Using Artificial Intelligence. Corpus ID 3194. [metasyn://corpus/3194](metasyn://corpus/3194)
- Deep Learning-Based Classification of Subtypes of Primary Angle-Closure Disease With Anterior Segment Optical Coherence Tomography. Corpus ID 3198. [metasyn://corpus/3198](metasyn://corpus/3198)
- An overview of artificial intelligence in diabetic retinopathy and other ocular diseases. Corpus ID 84867. [metasyn://corpus/84867](metasyn://corpus/84867)
- Lights and Shadows on Artificial Intelligence in Glaucoma: Transforming Screening, Monitoring, and Prognosis. Corpus ID 85404. [metasyn://corpus/85404](metasyn://corpus/85404)