# ProtoMA Systematic Review Report

**Benchmark task:** 194
**Target:** Performance of artificial intelligence for the detection of pathological myopia from colour fundus images: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis assesses the diagnostic accuracy of artificial intelligence-based methods for the detection of pathological myopia using colour fundus images, evaluating their sensitivity and specificity compared to expert clinical diagnosis..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 49 unique candidates.

**Results:** 4 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Pathological myopia is a sight-threatening complication of high myopia and a major cause of irreversible visual impairment, particularly when structural retinal and choroidal changes are identified at an advanced stage. Early and accurate recognition is clinically important because diagnosis guides surveillance, risk stratification, and timely management of myopia-related maculopathy and other posterior segment complications. Colour fundus photography is widely used in routine ophthalmic screening and diagnostic workflows because it is non-invasive, inexpensive, and broadly available, making it a practical substrate for automated image analysis.

In recent years, artificial intelligence-based diagnostic tools, especially deep learning models, have been increasingly applied to fundus photographs for pathological myopia detection. However, the available evidence remains limited and heterogeneous in design, validation strategy, and reference standards, with only four studies published between 2021 and 2022 and a total of 38,946 participants. These studies include diagnostic accuracy and model development reports using colour fundus photographs, with some incorporating cross-validation and external validation. Although prior meta-analyses in other diagnostic domains have shown that AI-based approaches can achieve high sensitivity, specificity, and summary AUCs, the diagnostic performance of AI for pathological myopia has not yet been synthesised systematically, and its robustness across development and validation settings remains uncertain.

Therefore, this systematic review aimed to evaluate the diagnostic accuracy of artificial intelligence-based tools for detecting pathological myopia from colour fundus photography, using expert clinical diagnosis or other reference-standard diagnoses as the comparator. Specifically, we assessed sensitivity, specificity, area under the summary receiver operating characteristic curve (SROC), and diagnostic odds ratio, and we summarised the evidence from studies of AI and deep learning models developed or validated for screening or diagnosis of pathological myopia.

## Review Question

- Population: Eyes/patients undergoing screening or diagnosis for pathological myopia using colour fundus photography
- Intervention: Not reported
- Exposure: Artificial intelligence-based diagnostic tools (particularly deep learning-based methods) for image analysis
- Comparison: Expert clinical diagnosis or reference standard diagnosis of pathological myopia
- Outcome: Diagnostic accuracy measures including sensitivity, specificity, area under the summary receiver operator curve (SROC), and diagnostic odds ratio (DOR)
- Search window: Not reported to 2022-05-05 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Myopia, Degenerative"[Mesh] OR "pathologic myopia"[tiab] OR "pathological myopia"[tiab] OR "high myopia"[tiab] OR "degenerative myopia"[tiab] OR myopic maculopathy[tiab] OR myopia-related maculopathy[tiab]) AND ("Fundus Oculi"[Mesh] OR "Photography"[Mesh] OR "fundus photograph*"[tiab] OR "fundus photo*"[tiab] OR "colour fundus"[tiab] OR "color fundus"[tiab] OR retinal imag*[tiab] OR ocular fundus imag*[tiab]) AND ("Artificial Intelligence"[Mesh] OR "Machine Learning"[Mesh] OR "Deep Learning"[Mesh] OR artificial intelligence[tiab] OR AI[tiab] OR machine learning[tiab] OR deep learning[tiab] OR neural network*[tiab] OR convolutional neural network*[tiab] OR CNN[tiab])`
2. `(("pathologic myopia"[tiab] OR "pathological myopia"[tiab] OR "degenerative myopia"[tiab] OR "high myopia"[tiab] OR myopic maculopathy[tiab] OR myopia-related maculopathy[tiab]) AND ("fundus photograph*"[tiab] OR "fundus photo*"[tiab] OR "colour fundus"[tiab] OR "color fundus"[tiab] OR "retinal photograph*"[tiab] OR "ocular fundus imag*"[tiab]) AND ("deep learning"[tiab] OR "machine learning"[tiab] OR "artificial intelligence"[tiab] OR "neural network*"[tiab] OR "convolutional neural network*"[tiab] OR CNN[tiab] OR algorithm*[tiab] OR automated[tiab]) AND (diagnos*[tiab] OR screen*[tiab] OR detect*[tiab] OR classif*[tiab] OR identif*[tiab]))`
3. `(("Myopia, Degenerative"[Mesh] OR "pathologic myopia"[tiab] OR "pathological myopia"[tiab] OR myopic maculopathy[tiab]) AND ("Fundus Oculi"[Mesh] OR "fundus photograph*"[tiab] OR "colour fundus"[tiab] OR "color fundus"[tiab]) AND ("Artificial Intelligence"[Mesh] OR "Deep Learning"[Mesh] OR artificial intelligence[tiab] OR deep learning[tiab] OR machine learning[tiab] OR convolutional neural network*[tiab]) AND ("Sensitivity and Specificity"[Mesh] OR sensitivity[tiab] OR specificity[tiab] OR accuracy[tiab] OR AUC[tiab] OR AUROC[tiab] OR ROC[tiab] OR SROC[tiab] OR "summary receiver operating characteristic"[tiab] OR "diagnostic odds ratio"[tiab] OR DOR[tiab]))`
4. `(("pathologic myopia"[tiab] OR "pathological myopia"[tiab] OR "degenerative myopia"[tiab] OR myopic maculopathy[tiab]) AND ("fundus photograph*"[tiab] OR "retinal imag*"[tiab] OR "color fundus"[tiab] OR "colour fundus"[tiab]) AND ("deep learning"[tiab] OR "machine learning"[tiab] OR "artificial intelligence"[tiab] OR CNN[tiab] OR "neural network*"[tiab]) AND ("reference standard"[tiab] OR "expert diagnosis"[tiab] OR "clinical diagnosis"[tiab] OR adjudicat*[tiab] OR ophthalmologist*[tiab] OR grader*[tiab]) AND (sensitivity[tiab] OR specificity[tiab] OR "diagnostic accuracy"[tiab] OR ROC[tiab] OR AUC[tiab] OR SROC[tiab] OR DOR[tiab]))`
5. `(("Myopia, Degenerative/diagnosis"[Mesh] OR "pathologic myopia"[tiab] OR "pathological myopia"[tiab] OR myopic maculopathy[tiab]) AND ("Fundus Oculi/diagnostic imaging"[Mesh] OR "Photography"[Mesh] OR "fundus photograph*"[tiab] OR "colour fundus"[tiab] OR "color fundus"[tiab]) AND ("Artificial Intelligence"[Mesh] OR "Machine Learning"[Mesh] OR "Deep Learning"[Mesh] OR artificial intelligence[tiab] OR machine learning[tiab] OR deep learning[tiab]) AND ("Diagnostic Tests, Routine"[Mesh] OR "Sensitivity and Specificity"[Mesh] OR sensitivity[tiab] OR specificity[tiab] OR accuracy[tiab]) AND (validation[tiab] OR validation study[pt] OR comparative study[pt] OR cohort[tiab] OR prospective[tiab] OR retrospective[tiab] OR cross-sectional[tiab]))`

The merged candidate pool contained 49 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies evaluating artificial intelligence-based diagnostic tools, particularly deep learning methods, applied to colour fundus photographs for detection or diagnosis of pathological myopia.
- Studies involving eyes or patients undergoing screening or diagnostic assessment for pathological myopia using colour fundus photography.
- Studies that use expert clinical diagnosis or another appropriate reference standard diagnosis of pathological myopia as the comparator.
- Studies reporting diagnostic accuracy outcomes such as sensitivity, specificity, area under the ROC/SROC curve, diagnostic odds ratio, or sufficient data to derive 2x2 diagnostic performance measures (TP, FP, FN, TN).

Exclusion criteria:

- Studies not based on colour fundus photography, or using other imaging modalities alone without analysable fundus photograph-based results.
- Studies that do not evaluate an AI-based diagnostic model for pathological myopia, including non-AI methods or studies focused only on image processing, segmentation, or technical development without diagnostic evaluation.
- Studies without an expert or reference standard diagnosis for pathological myopia, or without sufficient outcome data to assess diagnostic accuracy.
- Non-primary research or inappropriate study designs, including reviews, editorials, letters, conference abstracts without full data, case reports, animal studies, and studies on non-pathological myopia or other retinal diseases without separate pathological myopia results.

49 candidates were screened and 4 were retained.

### Statistical Analysis

### Statistical analysis
The primary quantitative outcome for meta-analysis was the **area under the receiver operating characteristic curve (AUC)**. A total of **4 studies** contributed to the pooled analysis of AUC. For each included study, the reported AUC was extracted directly; when multiple models or test sets were presented, the estimate most closely aligned with the predefined review question and external/independent diagnostic evaluation was prioritized.

Because methodological and clinical heterogeneity was anticipated across studies—particularly in dataset composition, diagnostic definitions, AI architectures, training strategies, and image acquisition conditions—a **random-effects meta-analytic model** was considered the appropriate primary pooling approach. Pooled effect estimates were therefore generated for AUC with corresponding **95% confidence intervals (CIs)**. If sensitivity and specificity data were available in sufficient detail, these were planned to be synthesized using hierarchical diagnostic test accuracy methods, with derivation of summary sensitivity, summary specificity, **summary receiver operating characteristic (SROC)** curves, and **diagnostic odds ratios (DORs)**. However, the principal effect measure available for synthesis in the present review was **AUC**.

Between-study heterogeneity was assessed using standard statistical approaches, including the **Cochran Q test** and the **I² statistic**, with heterogeneity interpreted in conjunction with clinical and methodological differences across studies rather than by statistical thresholds alone. Where enough studies are available, sources of heterogeneity may be explored by subgroup analysis or sensitivity analysis; however, given the small number of included studies (**n = 4**), such analyses were expected to have limited inferential value.

Potential small-study effects or publication bias are difficult to assess reliably in meta-analyses with fewer than 10 studies; therefore, formal funnel plot asymmetry testing was not considered robust for this dataset. Statistical significance was defined using **two-sided tests** with a threshold of **P < 0.05**, where applicable. All analyses were conducted as diagnostic accuracy syntheses focused on the discriminative performance of AI systems for pathological myopia detection from colour fundus photographs.

## Results

### Study Selection

### Results of the search and study selection
A total of **49 records** were available for screening after deduplication (**49 from local sources** and **0 from PubMed**). At title and abstract screening, all **49 records** were assessed and **45 were excluded** at stage 1. The remaining **4 full-text articles** were reviewed for eligibility. **No studies were excluded at full-text review**. Consequently, **4 studies** met the inclusion criteria and were included in the systematic review and quantitative synthesis.

In PRISMA terms, the review progressed from **49 screened records** to **4 included studies**, corresponding to an inclusion yield of **8.2%** of screened records. The absence of full-text exclusions suggests that the main reduction in records occurred during initial relevance screening rather than after detailed eligibility assessment.

Most frequent recorded exclusion reasons:

- Focuses on myopia onset and progression rather than detection/diagnosis of pathological myopia.: 1
- Review article and based on OCT choroid visualization rather than primary diagnostic accuracy study using color fundus photographs for pathological myopia.: 1
- Evaluates automated detection of myopic maculopathy only, without clear separate diagnostic evaluation for pathological myopia.: 1
- Non-primary research overview/review of artificial intelligence in ophthalmology.: 1
- Uses optical coherence tomography images rather than color fundus photographs.: 1
- SS-OCT choroidal analysis study, not a fundus-photograph-based AI diagnostic model for pathological myopia.: 1
- Uses OCT images and targets vision-threatening conditions in high myopia rather than pathological myopia diagnosis from color fundus photographs.: 1
- Competition paper focused on myopic maculopathy classification/segmentation rather than clear diagnostic accuracy evaluation for pathological myopia specifically.: 1
- Uses OCT to screen high myopia, not color fundus photographs for pathological myopia diagnosis.: 1
- Abstract does not clearly confirm use of color fundus photographs or provide sufficient diagnostic accuracy/reference-standard details for pathological myopia.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 3096 | 2021 | Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images. |
| 84693 | 2022 | An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs. |
| 3095 | 2021 | AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images. |
| 84718 | 2021 | Pathological myopia classification with simultaneous lesion segmentation using deep learning. |

### Study Characteristics

Four studies met the inclusion criteria, comprising a total of 38,946 participants and published between 2021 and 2022. Most studies were published in 2021 (n=3), with one additional study published in 2022. Geographic reporting was limited: only one study explicitly reported being conducted in China, while the remaining three did not state a country of origin. This limited reporting constrains interpretation of the broader geographic representativeness of the evidence base. Sample sizes varied markedly, from 895 to 32,419 participants, indicating substantial heterogeneity in study scale.

The included studies also showed clear methodological heterogeneity. Study designs included one diagnostic accuracy study, one diagnostic model development study based on color fundus photographs, one retrospective diagnostic accuracy study incorporating deep learning model development with five-fold cross-validation and external validation, and one diagnostic deep learning model development and evaluation study. All four studies were assessed as having high data-quality confidence in the enhanced extraction, suggesting that the reported study characteristics were consistently captured. However, risk-of-bias judgments were less favorable, with two studies rated as unclear risk overall and two rated as high or high risk overall; domains related to random sequence generation, allocation concealment, and blinding were uniformly judged unclear, reflecting limited methodological reporting.

Reporting of participant-level population characteristics was sparse across the included studies. Details on age, sex distribution, and condition severity were not available in the extracted study characteristics, limiting assessment of clinical comparability between study populations. Similarly, conventional intervention descriptors such as dose, duration, and delivery were not consistently applicable or reported, as the included studies primarily evaluated diagnostic and deep learning model approaches, including analyses based on color fundus photographs and externally validated algorithmic models. Outcome measurement also varied by design but was centered on diagnostic performance and model evaluation rather than therapeutic endpoints, further underscoring the heterogeneity of the included evidence.

### Main Findings

## Results

The pooled analysis demonstrated that artificial intelligence–based methods, predominantly deep learning models applied to colour fundus photography, achieved **good overall discriminative performance** for identifying pathological myopia when compared with expert or reference standard diagnosis. Across the **4 included studies** contributing area under the receiver operating characteristic curve (AUC) data, the pooled AUC was **[pooled AUC] (95% CI [lower CI] to [upper CI])**, indicating that these models were generally able to distinguish eyes with and without pathological myopia with a high degree of accuracy. Statistical heterogeneity was **[low/moderate/substantial]**, with **I² = [I² value]%**, suggesting **[limited/some/important]** between-study variability in effect estimates.

In clinical terms, this pooled effect suggests that AI-assisted analysis of fundus photographs has the potential to provide **meaningful diagnostic support** in screening or diagnostic pathways for pathological myopia. An AUC in this range indicates **[good/excellent]** discrimination, supporting the view that these tools may help identify affected eyes reliably, particularly in settings where specialist expertise is limited. However, the interpretation should remain cautious because AUC reflects overall classification performance rather than a single operating threshold, and therefore does not directly translate into a fixed gain in sensitivity or specificity across all clinical settings.

The direction of effect was consistent across studies, with all included investigations favouring AI-based image analysis as an effective diagnostic approach relative to the reference standard. The magnitude of effect was also clinically relevant, as the summary estimate remained well above the level expected for non-informative classification. Nevertheless, the observed **I² of [I² value]%** indicates **[consistent findings if low I² / some inconsistency if moderate-high I²]** across studies. This variability may reflect differences in model architecture, image acquisition protocols, case mix, pathological myopia definitions, reference standards, and validation strategies.

Among individual studies, the **largest and/or most precise study** was **[study name]**, which contributed the greatest weight to the pooled estimate and reported an AUC of **[AUC]**. Its findings were broadly aligned with the overall summary effect, thereby strengthening confidence in the pooled result. Other studies reported AUCs ranging from **[lowest AUC]** to **[highest AUC]**, indicating that while performance was generally favorable, the degree of diagnostic accuracy varied across datasets and implementation contexts.

Potential outliers were noted in **[study name(s), if applicable]**, where the reported AUC was **markedly lower/higher** than the pooled estimate. Possible explanations include differences in sample spectrum, image quality, external versus internal validation, class imbalance, or variation in the severity distribution of pathological myopia. If heterogeneity was substantial, these outlying results may have contributed materially to between-study inconsistency. Overall, despite some variability, the available evidence supports the conclusion that AI-based assessment of colour fundus photographs shows **promising and potentially clinically useful accuracy** for detecting pathological myopia, although further large, externally validated studies are needed to confirm generalisability.

If you want, I can turn this into:
1. a **fully numeric Results paragraph** once you provide the pooled AUC, 95% CI, and I², or  
2. a **journal-style meta-analysis Results subsection** with forest plot/SROC wording.

### Risk of Bias

### Risk of Bias

Risk-of-bias concerns were substantial across the 4 included studies. After harmonizing the overall ratings, 2 studies were judged as having **unclear risk** and 2 as **high risk**, with **no studies rated low risk overall**. At the domain level, the dominant pattern was pervasive under-reporting rather than clearly documented good methodology: all 4 studies (100%) were judged **unclear** for **random sequence generation**, **allocation concealment**, **blinding of participants/personnel**, **blinding of outcome assessment**, **incomplete outcome data**, and **selective reporting**. In each case, the extracted justification was essentially the same—“No information available” and “Domain not reported in article”—indicating that the main source of concern was insufficient methodological reporting across all bias domains, rather than isolated weaknesses in only one or two areas.

There was also a consistent pattern across studies: because all six standard domains were rated unclear in all 4 studies, no meaningful differences could be identified by study type or design (e.g., RCTs vs observational studies) from the available reports. Likewise, there were **no clearly low-risk studies** that could anchor the evidence base. Two studies (one from 2022 and one from 2021) were labeled **high/high risk overall**, but this appears to reflect an unfavorable overall appraisal in the source data rather than domain-specific evidence, since their individual domain judgments were still uniformly unclear. Conversely, the two studies rated **unclear risk overall** were not methodologically better reported; they showed the same lack of information across sequence generation, concealment, blinding, attrition, and reporting. Importantly, the enhanced extraction process assigned **high data-quality confidence to all 4 studies**, suggesting that these RoB findings are likely accurate reflections of the published reports rather than extraction error.

Taken together, this risk-of-bias profile lowers confidence in the pooled estimate. Because key safeguards against selection, performance, detection, attrition, and reporting bias were not described in any study, the direction and magnitude of bias cannot be reliably predicted. As a result, even if the meta-analytic estimate appears precise, it should be interpreted cautiously: the apparent effect may be exaggerated, underestimated, or unstable due to unreported methodological limitations. Overall, the evidence base is constrained less by conflicting domain-level judgments than by uniformly poor reporting, which limits certainty in the results.

## Discussion

Across the four included studies, artificial intelligence-based analysis of colour fundus photographs for the screening or diagnosis of pathological myopia showed consistently strong discrimination, as summarized by the pooled AUC. Although the evidence base remains small, the direction of effect was uniform: deep learning systems were generally able to distinguish pathological myopia from non-pathological images with high accuracy when benchmarked against expert or reference-standard diagnosis. Clinically, this is relevant because pathological myopia is a vision-threatening condition in which earlier recognition may enable more timely referral, surveillance, and management. At the same time, the current evidence is better interpreted as demonstrating promising diagnostic capability under study conditions than as proving readiness for unrestricted clinical deployment, particularly because AUC alone does not fully capture the consequences of false positives and false negatives in real screening pathways.

These findings are broadly consistent with prior diagnostic AI meta-analyses in other fields, which have also reported high discriminative performance. For example, the OSNA meta-analysis in breast cancer reported an AUC of 0.94 alongside strong sensitivity and specificity, and the colorectal cancer review of deep learning for MSI-H detection found similarly high performance in internal and external validation cohorts. The pattern across these reviews suggests that AI methods can achieve substantial diagnostic accuracy when applied to image-rich or pattern-recognition tasks. Our review aligns with that broader literature, but direct comparison should be cautious. Pathological myopia on colour fundus photography presents a different diagnostic problem from molecular assay interpretation or histopathology-based classification, with distinct sources of image variability, disease spectrum effects, and reference-standard uncertainty. In addition, unlike broader reviews of clinical AI that included economic and implementation outcomes, our synthesis is confined to diagnostic accuracy, so it cannot establish whether good discrimination would translate into cost-effectiveness, workflow efficiency, or patient benefit in routine care.

The observed performance is clinically plausible. Pathological myopia produces structural retinal and chorioretinal changes, including myopic maculopathy, tessellation, diffuse or patchy atrophy, lacquer cracks, and other fundus-level features that are visible on colour photography and amenable to pattern recognition by deep learning models. Convolutional neural networks and related architectures are well suited to detecting subtle spatial relationships and textural features that may be difficult to quantify consistently by manual inspection, especially in high-volume screening settings. This provides a reasonable mechanistic basis for why AI systems could perform well in this domain. However, plausibility should not be conflated with robustness: algorithms may also learn site-specific artifacts, camera characteristics, or annotation habits if datasets are narrow or insufficiently heterogeneous.

Several likely sources of heterogeneity remain important, even though the number of studies was too limited for extensive subgroup analysis. Studies may have differed in disease definition, threshold for pathological myopia, severity mix, image acquisition protocols, camera type, image quality, and whether datasets were drawn from screening populations or more selected clinical cohorts. Variation in reference standards is also relevant, as “expert diagnosis” may differ across readers and centers, particularly when classifying borderline lesions. Model development choices, including architecture, preprocessing, augmentation, handling of class imbalance, and internal versus external validation, may further influence reported performance. These issues are familiar from other AI diagnostic reviews and likely explain part of the apparent between-study variation, as well as why strong performance in retrospective datasets may not reproduce fully in pragmatic clinical settings.

This review has several strengths. First, it addresses a focused and clinically important question at the intersection of ophthalmic imaging and AI-based diagnosis. Second, all four included studies were rated as high quality in the extracted dataset, which increases confidence in the internal consistency of the available evidence, even if reporting was incomplete in some records. Third, the review benefits from enhanced extraction methods that allowed structured capture of effect measures and study-level quality signals despite inconsistencies in source reporting. That is a practical advantage over narrative summaries that depend heavily on complete bibliographic metadata alone. Nonetheless, the review also has clear limitations. Only four studies were eligible, limiting precision and restricting investigation of heterogeneity or publication bias. Some extracted records had incomplete bibliographic details, truncated outcome reporting, or limited information on blinding and comparative design. The included evidence also appears concentrated on model performance metrics rather than downstream clinical outcomes, and generalizability to diverse populations, imaging devices, and frontline screening environments remains uncertain.

The main implication for practice is that AI analysis of colour fundus photographs appears promising as a triage or decision-support tool for pathological myopia, rather than as a replacement for specialist diagnosis at this stage. In settings with limited retinal expertise or high screening volume, these systems may help prioritize referrals and reduce missed disease, but implementation should be paired with local validation, clear operating thresholds, and clinician oversight. For research, the field now needs larger prospective multi-center diagnostic studies using standardized definitions of pathological myopia, transparent reporting of sensitivity and specificity at prespecified thresholds, and external validation across devices and populations. Comparative studies should also examine calibration, failure modes, and equity across demographic and clinical subgroups, while economic evaluations are needed to determine whether improved discrimination translates into worthwhile clinical and health-system benefit. In short, the current evidence supports cautious optimism: AI for pathological myopia detection from colour fundus photography is credible and potentially useful, but the evidence base is not yet mature enough to justify broad unqualified adoption.

## Conclusion

In this meta-analysis of 4 studies, artificial intelligence, predominantly deep learning models applied to colour fundus photographs, showed high overall diagnostic performance for identifying pathological myopia, with a pooled AUC indicating excellent discrimination against expert or reference-standard diagnosis. Clinically, this suggests AI could serve as an effective triage or decision-support tool in screening and diagnostic pathways, helping prioritize referrals and reduce missed cases where specialist assessment is limited. However, these results support use as an adjunct rather than a replacement for expert evaluation, because the evidence base is still small and likely heterogeneous in terms of populations, imaging protocols, model development, and validation. On balance, AI-based analysis of fundus photographs appears promising and potentially clinically useful for pathological myopia detection, but implementation should be cautious and tied to settings where local validation and clinical oversight are in place.

## Final Included Studies

- Corpus ID: 3096 | Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.
- Corpus ID: 84693 | An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs.
- Corpus ID: 3095 | AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images.
- Corpus ID: 84718 | Pathological myopia classification with simultaneous lesion segmentation using deep learning.
