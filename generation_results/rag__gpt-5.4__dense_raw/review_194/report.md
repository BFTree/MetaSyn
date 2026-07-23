**Screening Summary**

Using only the supplied candidate pool and the stated eligibility criteria, I identified **8 likely eligible primary studies** on AI-based detection of pathological myopia or myopic maculopathy from **color fundus photographs**. I excluded reviews, protocols, non-fundus/OCT-only studies, non-pathological-myopia targets, and records where the abstract did not plausibly match the review scope.

Because I only have titles and abstracts, inclusion judgments below are necessarily based on what those abstracts explicitly report. I do **not** infer missing details such as peer-review status beyond what is implied by the candidate list.

**Eligibility Logic Applied**

Included studies had to plausibly:
- evaluate **AI / deep learning** for **pathological myopia (PM)** or closely aligned **myopic maculopathy** detection/classification;
- use **color fundus photographs/images**;
- report diagnostic performance such as **AUC/AUROC, sensitivity, specificity**;
- compare against human grading / ophthalmologist grading / a reference standard;
- provide enough dataset and validation information in the abstract to look consistent with the review question.

Excluded studies mainly fell into these groups:
- **Review/scoping/systematic review** articles: Candidates 004, 011, 025, 038, 055, etc.
- **Wrong imaging modality**: OCT-only studies such as 012, 018, 019.
- **Wrong target condition**: glaucoma, diabetic retinopathy, breast cancer, colonoscopy, etc.
- **Not clearly within review timeframe/end date**: 2023+ studies would post-date the review search end of 2022-05-05 and should not represent the evidence base of that review even if otherwise relevant.
- **Conference/challenge style or later methodological studies** outside the review window: e.g., 006, 016, 041, 192.
- **General ocular-disease datasets** where pathological myopia was only one class and not clearly the PM-specific detection study targeted by the review: 049.

**Included Evidence**

The likely includable evidence is concentrated in **2021-2022**, and most studies used retrospective datasets of fundus photographs graded by ophthalmologists using PM/MM reference schemes such as **META-PM**. Reported performance is generally high, with AUCs commonly in the **0.97-0.998** range for PM/MM-related tasks, and sensitivities/specificities often in the high 80s to high 90s, though exact thresholds and task definitions vary.

A key source of heterogeneity is that some studies target:
- direct **pathological myopia detection**,
- **myopic maculopathy classification** with PM derivable from class labels,
- or detection of **plus lesions / lesion segmentation** alongside PM diagnosis.

This means the studies are clinically related but not identical in outcome definition. That would matter for any meta-analysis of pooled sensitivity/specificity.

**Study-by-Study Synthesis**

1. **Candidate 001** reports a deep learning approach for identifying PM and MM lesions from fundus images. It used 7020 fundus images from highly myopic eyes, with a separate evaluation set of 1844 images. The abstract explicitly reports AUC, sensitivity, and specificity for lesion models and states an overall **92.08% rate in detecting pathologic myopia correctly**. This is strongly aligned with the review target.

2. **Candidate 002** developed AI models for PM identification, MM classification, and plus-lesion detection from retinal fundus images. It used a very large dataset with both cross-validation and an external validation set from other hospitals. The PM-identification algorithm reported **AUC 0.995**, **sensitivity 93.92%**, and **specificity 98.19%** in cross-validation. This appears highly relevant and one of the strongest candidate studies.

3. **Candidate 003** developed a classification/segmentation co-decision model based on color fundus photographs. It explicitly states that the system could **diagnose pathologic myopia**, with **AUC 0.9980**. The abstract is focused on MM grading, PM diagnosis, and lesion identification; it fits the review scope.

4. **Candidate 032** evaluated CNNs for **PM detection** and lesion segmentation using the PALM fundus-image dataset. It reports **AUC 0.9867** for PM detection on a test set. The abstract is clearly on PM from fundus images and reports an eligible diagnostic metric.

5. **Candidate 033** built a dual-stream DCNN model for classifying no MM, tessellated fundus, and PM from color fundus photographs. External-test performance for PM detection included **sensitivities 93.3% and 91.0%**, **specificities 99.6% and 98.7%**, and **AUCs 0.998 and 0.994**. This is highly relevant, though framed through MM-level classification.

6. **Candidate 191** studied combined automated screening for AMD and DR in primary care, but the abstract states that images with confounding conditions including **high myopia** were excluded. It is therefore **not eligible**.

7. **Candidate 041** and **Candidate 192** are about myopic lesions / tessellation from fundus images, but they are from **2023-2024**, so they are outside the source review’s search end date and should not be included for this synthesis.

8. **Candidate 016** is also outside the review search window.

On balance, the evidence base appears to support **high diagnostic accuracy** of deep learning systems for PM detection on fundus photographs, but it is likely dominated by **retrospective development/validation studies**, often from single-country or limited-center datasets. External validation is present in some studies but not all. The abstracts do not provide enough information to judge whether all studies would contribute a reconstructable **2×2 table**, so some could have been narratively included but excluded from quantitative meta-analysis in the source review.

**Main Patterns Across Included Studies**

- **Imaging modality consistency:** all included studies use color fundus photographs/images.
- **Model family:** predominantly deep learning/CNN-based.
- **Reference standard:** manual grading by ophthalmologists/experts, often using **META-PM** or related myopic maculopathy grading frameworks.
- **Performance:** generally strong discrimination, often with AUCs around or above 0.98.
- **Generalizability concerns:** many studies appear retrospective; only some mention external validation across hospitals.
- **Outcome heterogeneity:** PM detection may be direct or derived from MM severity thresholds, which could complicate pooled synthesis.

**Limits of This Screening**

I only screened titles and abstracts. I cannot confirm from abstracts alone:
- whether every included study was published in an English peer-reviewed journal,
- whether the validation set was always at least 10% of the training set,
- whether a full **2×2 contingency table** could be formed,
- or whether any study would later be excluded for quality reasons in full-text review.

So this is a **title/abstract-level eligibility synthesis**, not a definitive full-text inclusion decision.

**Final Included Primary Studies**

1. **Corpus ID: 3096**  
   **Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.**

2. **Corpus ID: 3095**  
   **AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images.**

3. **Corpus ID: 84693**  
   **An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs.**

4. **Corpus ID: 84718**  
   **Pathological myopia classification with simultaneous lesion segmentation using deep learning.**

5. **Corpus ID: 3097**  
   **Automated detection of myopic maculopathy from color fundus photographs using deep convolutional neural networks.**

**Borderline but not finally included**
- **Corpus ID: 84729**, **Automated detection of myopic maculopathy using five-category models based on vision outlooker for visual recognition.**  
  Excluded on date grounds: 2023, after the review search end.
- **Corpus ID: 84714**, **Effective automatic classification methods via deep learning for myopic maculopathy.**  
  Excluded on date grounds: 2024.
- **Corpus ID: 84728**, **DeepGraFT: A novel semantic segmentation auxiliary ROI-based deep learning framework for effective fundus tessellation classification.**  
  Excluded: fundus tessellation rather than PM detection, and outside date window.

Overall, the abstract-level evidence supports that, by 2021-2022, AI systems based on color fundus images had already shown **high apparent sensitivity, specificity, and AUC** for detecting pathological myopia and related myopic maculopathy, but the evidence base likely remained limited by **retrospective design, heterogeneous task definitions, and incomplete external validation**.
