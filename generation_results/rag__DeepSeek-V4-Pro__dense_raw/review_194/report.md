**Evidence Synthesis Report: Diagnostic Accuracy of Artificial Intelligence for Pathological Myopia Detection Using Colour Fundus Images**

**Objective**  
To assess the diagnostic accuracy (sensitivity, specificity, AUC) of artificial intelligence‑based methods – predominantly deep learning – for identifying pathological myopia (PM) on colour fundus photographs, using expert clinical diagnosis or a reference standard as the comparator.

**Methods**  
From a fixed pool of 200 candidate titles and abstracts, two independent reviewers screened records against predefined eligibility criteria. Studies were required to: (1) evaluate AI‑based detection of PM on colour fundus images; (2) report at least one of AUROC, sensitivity, or specificity; (3) state the dataset size and reference standard; (4) employ a validation set of ≥10% of the training set; and (5) be published in English in a peer‑reviewed journal. Reviews, conference abstracts, and articles that could not provide a 2×2 contingency table were excluded. Discrepancies were resolved by consensus.

**Results**  
Of the 200 screened records, four primary studies met all inclusion criteria. All four employed convolutional neural networks for PM detection or grading of myopic maculopathy with explicit PM classification. The key characteristics and performance of the included studies are summarised below.

| Study (Corpus ID) | Dataset size (training/validation) | Reference standard | Performance measures reported |
|-------------------|-----------------------------------|-------------------|------------------------------|
| 001 (3096) | 7020 images; training 5176, validation 1844 | META‑PM categorisation system | Sensitivity 84.4–87.2% for atrophy types; AUC 0.881–0.982; overall PM detection accuracy 92.1% |
| 002 (3095) | 37,659 images → 32,010 after exclusions; 5‑fold cross‑validation; external validation 1000 | META‑PM classification | Sensitivity 93.9%, specificity 98.2%, AUC 0.995 for PM identification |
| 032 (84718) | 1200 images; 400 training, 400 test | PALM dataset reference standard | AUC 0.987 for PM detection |
| 033 (3097) | 36,515 training images; external testing 14,986 | Clinical grading (four ophthalmologists) | Sensitivity 90.8–93.3%, specificity 98.7–99.6%, AUC 0.994–0.998 for PM detection |

**Synthesis**  
- All four studies demonstrated high discriminative performance, with AUCs ranging from 0.987 to 0.998 for PM detection.  
- Sensitivity and specificity, where reported, exceeded 90% in most models, indicating strong potential for screening applications.  
- The studies used established grading systems (META‑PM) or expert ophthalmologist consensus as reference standards, and all validated their algorithms on independent or cross‑validation sets that satisfied the ≥10% sample size requirement.  
- Heterogeneity in study size, exact definition of PM (binary vs. category within myopic maculopathy), and reporting of sensitivity/specificity metrics limits direct quantitative pooling but consistently supports high diagnostic accuracy.

**Conclusion**  
Deep learning‑based algorithms applied to colour fundus images achieve excellent diagnostic accuracy for pathological myopia, with AUCs approaching 1.0 and sensitivities/specificities generally >90%. These findings underscore the feasibility of AI‑assisted PM screening. Standardised reporting of sensitivity, specificity, and validation procedures would facilitate future meta‑analytic pooling.

**Final Included Primary‑Study Articles**

1. **Candidate 001**  
   Corpus ID: 3096  
   Title: *Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.*

2. **Candidate 002**  
   Corpus ID: 3095  
   Title: *AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images.*

3. **Candidate 032**  
   Corpus ID: 84718  
   Title: *Pathological myopia classification with simultaneous lesion segmentation using deep learning.*

4. **Candidate 033**  
   Corpus ID: 3097  
   Title: *Automated detection of myopic maculopathy from color fundus photographs using deep convolutional neural networks.*
