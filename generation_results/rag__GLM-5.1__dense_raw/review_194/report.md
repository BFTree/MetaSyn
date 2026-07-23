**Systematic Review and Evidence Synthesis Report**

**Review Target:** Diagnostic accuracy of artificial intelligence-based methods for the detection of pathological myopia using colour fundus images, evaluated against expert clinical diagnosis.

**Screening and Selection Process**
Titles and abstracts from the fixed candidate pool of 200 records were screened against the predefined inclusion and exclusion criteria. The criteria required studies to evaluate AI/DL algorithms for pathological myopia (PM) detection using colour fundus images, reporting performance indices (AUROC, sensitivity, specificity), providing dataset and reference standard information, and including a validation set of at least 10% the size of the training set. Studies had to be in English, published in a peer-reviewed journal, and published before the search end date of 2022-05-05. Reviews, conference abstracts, studies using non-fundus imaging modalities (e.g., OCT), and studies focusing on other ocular conditions were excluded.

**Screening Outcomes**
From the provided pool, most candidates were excluded for focusing on other diseases (e.g., glaucoma, diabetic retinopathy, AMD, breast cancer), utilizing non-fundus imaging (OCT, ultrasound), being published after the 2022-05-05 cutoff, or being review articles. Several myopia-related AI studies were excluded for failing to explicitly state a validation set size meeting the ≥10% threshold in the abstract (e.g., Candidate 002 reported an external validation of 1,000 images against a training/cross-validation set of 32,010, which is <10%; Candidate 003 did not report validation set proportions). Three primary studies met all stringent criteria and were included in the final evidence synthesis.

**Evidence Synthesis**
The three included studies evaluated deep learning algorithms for detecting pathological myopia or myopic maculopathy on colour fundus photographs, comparing performance against expert reference standards.

1.  **Algorithm Performance (AUROC):** All included models demonstrated exceptional discriminative ability for detecting PM. The AUROC for PM detection ranged from 0.9867 (using the PALM dataset) to 0.994–0.998 in large multi-hospital external test sets. These values consistently surpassed typical clinical thresholds for excellent diagnostic accuracy and were comparable to or superior to human expert performance.

2.  **Sensitivity and Specificity:** 
    *   **Candidate 033** reported the highest robust sensitivity and specificity for PM detection in external testing, achieving sensitivities of 93.3% and 91.0% and specificities of 99.6% and 98.7% across two datasets. The model outperformed or matched ophthalmologists, whose sensitivities ranged from 88.3% to 95.8% and specificities from 95.9% to 99.2%.
    *   **Candidate 001** reported high sensitivities for detecting specific myopic maculopathy lesions (e.g., 87.22% for patchy atrophy, 85.10% for macular atrophy), though sensitivity for choroidal neovascularization was notably lower (37.07%). The overall system accuracy for detecting PM (defined as myopic maculopathy ≥ diffuse atrophy) was 92.08%.
    *   **Candidate 032** achieved an AUC of 0.9867 for PM classification on the PALM challenge dataset, though explicit sensitivity/specificity values for PM classification were not detailed in the abstract beyond the segmentation and localization metrics.

3.  **Validation Rigor:** All included studies satisfied the criterion of having a validation dataset of at least 10% the size of the training set. Candidate 033 provided the strongest validation evidence, utilizing 14,986 external test images (41% of the 36,515 development set). Candidate 001 used 1,844 evaluation images (35.6% of the 5,176 training set). Candidate 032 used 400 test images (100% of the 400 training images available in the PALM dataset).

**Conclusions**
Current AI-based deep learning algorithms demonstrate high diagnostic accuracy for detecting pathological myopia on colour fundus images, frequently achieving AUROC values above 0.98 and sensitivities/specificities exceeding 90%. The evidence supports their potential utility as screening and diagnostic tools comparable to expert ophthalmologists, provided they are rigorously validated on large, external datasets. Limitations include variable sensitivity for specific "plus" lesions like CNV in earlier models, which may require further architectural optimization.

***

**Final Included Primary-Study Articles**

1.  **Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.** 
    Corpus ID: 3096

2.  **Pathological myopia classification with simultaneous lesion segmentation using deep learning.**
    Corpus ID: 84718

3.  **Automated detection of myopic maculopathy from color fundus photographs using deep convolutional neural networks.**
    Corpus ID: 3097
