## Systematic Review and Evidence Synthesis

### Screening of Candidate Pool
The 200 supplied titles and abstracts were screened against the predefined inclusion and exclusion criteria. The objective was to identify primary studies that evaluated the diagnostic accuracy of artificial intelligence (AI)-based methods—particularly deep learning models—for detecting pathological myopia (PM) on colour fundus photographs, reporting sensitivity, specificity, area under the receiver operating characteristic curve (AUROC), and/or diagnostic odds ratio, with a reference standard of expert clinical diagnosis.

After screening, **seven** articles met all eligibility criteria. All are original, peer-reviewed studies that developed and validated AI algorithms on colour fundus images to detect PM or myopic maculopathy (the hallmark of PM), and they reported the required diagnostic performance metrics. The remaining 193 candidates were excluded because they were reviews, meta-analyses, conference abstracts, or addressed different diseases, imaging modalities, or non‑diagnostic tasks.

---

### Final Included Primary‑Study Articles

| # | Corpus ID | Title |
|---|-----------|-------|
| 1 | 84729 | Automated detection of myopic maculopathy using five-category models based on vision outlooker for visual recognition. |
| 2 | 84714 | Effective automatic classification methods via deep learning for myopic maculopathy. |
| 3 | 3096 | Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images. |
| 4 | 3095 | AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images. |
| 5 | 84718 | Pathological myopia classification with simultaneous lesion segmentation using deep learning. |
| 6 | 84693 | An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs. |
| 7 | 84762 | A Competition for the Diagnosis of Myopic Maculopathy by Artificial Intelligence Algorithms. |

---

### Evidence Synthesis

All seven included studies employed deep learning models applied to colour fundus images to classify pathological myopia or the severity of myopic maculopathy. Key findings and characteristics are summarised below.

**Study designs and datasets**  
The studies used retrospectively collected colour fundus photographs from clinical cohorts. Dataset sizes ranged from 1,200 images (PALM dataset) to over 32,000 images. All studies used expert‑graded images as the reference standard, and several incorporated the META‑PM classification system. Validation was performed via internal cross‑validation, held‑out test sets, or external multicentre datasets, satisfying the requirement for a validation set of at least 10% of the training set.

**Diagnostic performance for pathological myopia detection**  
- **Candidate 001** (Corpus ID 84729) developed a VOLO‑D2 model and reported an overall accuracy of 96.60% (κ = 0.956) for classifying five categories of myopic maculopathy. Sensitivity, specificity, PPV, and NPV were provided for each lesion category; for example, sensitivity for macular atrophy was 100% and specificity 98.10%.  
- **Candidate 002** (Corpus ID 84714) used an ensemble of five architectures (ResNet50, EfficientNet‑B0, ViT, CLIP, RETFound) and achieved an accuracy of 95.4%, sensitivity 95.4%, specificity 98.9%, and an AUC of 0.995 for myopic maculopathy classification.  
- **Candidate 006** (Corpus ID 3096) trained four DL models on 5,176 images and evaluated them on 1,844 images. The META‑PM categorisation system detected pathologic myopia with an overall accuracy of 92.08%. Sensitivity for diffuse atrophy, patchy atrophy, macular atrophy, and choroidal neovascularisation were 84.44%, 87.22%, 85.10%, and 37.07%, respectively, with AUCs of 0.970–0.982.  
- **Candidate 007** (Corpus ID 3095) developed algorithms for PM identification, MM classification, and “plus” lesion detection on 32,010 images. In five‑fold cross‑validation, the PM detection algorithm achieved sensitivity 93.92%, specificity 98.19%, accuracy 97.36%, and AUC 0.995. External validation in 1,000 images from other hospitals showed comparable but slightly lower performance, yet still comparable to expert graders.  
- **Candidate 027** (Corpus ID 84718) focused on simultaneous PM classification and lesion segmentation using the PALM dataset (400 training, 400 test images). The model achieved an AUC of 0.9867 for PM detection. Dice scores for segmentation of optic disc, retinal atrophy, and retinal detachment were 0.9303, 0.8001, and 0.8073, respectively.  
- **Candidate 033** (Corpus ID 84693) combined a ResNet‑50 classification model with a DeepLabv3+ segmentation model on 1,395 colour fundus photographs. The co‑decision model attained a grading accuracy of 93.70% (quadratic‑weighted κ = 0.9651) and an AUC of 0.9980 for diagnosing pathologic myopia.  
- **Candidate 177** (Corpus ID 84762) reported the results of the Myopic Maculopathy Analysis Challenge (MMAC). Submitted algorithms for MM classification achieved a quadratic‑weighted κ of 0.866–0.901, sensitivity 0.667–0.778, and specificity 0.931–0.945. Model ensembles outperformed individual algorithms and also surpassed ophthalmologists in sensitivity (0.801 vs. 0.727) and specificity (0.946 vs. 0.933).

**Common themes and methodological strengths**  
All studies demonstrated that deep learning models can identify pathological myopia with high sensitivity and specificity, often rivalling or exceeding expert clinicians. The use of the META‑PM grading system, large‑scale training datasets, and both internal and external validation enhanced the reliability of the findings. The integration of segmentation tasks (e.g., **Candidate 027**, **Candidate 033**) provided additional interpretability and may improve classification accuracy.

**Limitations of the included evidence**  
- Most studies were retrospective and used curated datasets from tertiary centres, which may limit generalisability to real‑world screening settings.  
- Only a few studies (**Candidate 007**, **Candidate 177**) included external validation on data from independent institutions.  
- Performance for certain lesion types, particularly choroidal neovascularisation, was substantially lower (e.g., sensitivity 37.07% in **Candidate 006**), indicating that detection of subtle lesions remains challenging.  
- The candidate pool did not contain any prospective, multicentre head‑to‑head comparisons of AI algorithms against standard clinical pathways, which would be desirable for a definitive evidence base.

**Synthesis conclusion**  
The available primary studies consistently show that AI‑based algorithms applied to colour fundus images can detect pathological myopia with high diagnostic accuracy (AUCs 0.97–0.998, sensitivities ~85–95%, specificities ~93–99%). The evidence supports the potential of these tools for screening and assisting clinicians. However, the limited number of externally validated studies and the absence of prospective evaluations mean that the estimates should be interpreted with caution. Future systematic reviews that incorporate full‑text data extraction and meta‑analysis of 2×2 contingency tables would be needed to obtain pooled summary estimates of sensitivity and specificity.
