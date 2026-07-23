Based on the specified review target and inclusion/exclusion criteria, the candidate pool was screened to identify primary studies assessing the diagnostic accuracy of AI-based methods for detecting pathological myopia (PM) using colour fundus images. Studies were excluded if they utilized imaging modalities other than colour fundus photography (e.g., OCT), targeted conditions other than PM (e.g., glaucoma, DR), were published after the search end date (2022-05-05), were reviews or conference abstracts, or lacked sufficient data in the abstract to report on algorithm performance via sensitivity, specificity, or AUROC for the PM diagnosis (specifically failing the exclusion criterion regarding the inability to form a 2×2 contingency table for meta-analysis from the provided data).

Three primary studies met all eligibility criteria. These studies consistently demonstrate that deep learning algorithms achieve high diagnostic accuracy for pathological myopia on colour fundus images, often performing comparably or superiorly to expert ophthalmologists.

**Evidence Synthesis**

The included studies evaluated deep learning (DL) architectures, primarily convolutional neural networks (CNNs), for the automated detection of pathological myopia and myopic maculopathy (MM) lesions. All studies utilized colour fundus photographs and validated their models against expert clinical diagnosis or reference standards.

1.  **Algorithm Performance**: The diagnostic accuracy of the AI models was consistently high across the studies.
    *   **Candidate 002** reported the highest performance for binary PM identification using their AI-model (Algorithm I), achieving an Area Under the Receiver Operating Characteristic Curve (AUROC) of 0.995, with a sensitivity of 93.92% and specificity of 98.19% in five-fold cross-validation, and comparable performance on an external validation dataset.
    *   **Candidate 003** utilized a dual-stream DCNN (DCNN-DS) model to classify PM among other MM categories. In two external testing datasets, the model achieved sensitivities of 93.3% and 91.0%, specificities of 99.6% and 98.7%, and AUROCs of 0.998 and 0.994 for detecting PM.
    *   **Candidate 001** developed DL models for specific MM lesions and a META-PM categorizing system. While it reported high sensitivity and specificity for individual lesions (e.g., 84.44% sensitivity for diffuse atrophy), it reported the overall performance for detecting PM as a "rate of correct predictions" (accuracy) of 92.08%, rather than explicit sensitivity/specificity values for the binary PM diagnosis, which limits direct 2×2 table construction for meta-analysis from the abstract alone.

2.  **Comparison with Experts**: The studies frequently benchmarked AI performance against human experts.
    *   **Candidate 003** compared its DCNN-DS model to four ophthalmologists on a sampled dataset. The AI model achieved higher sensitivity (90.8% vs. 88.3–95.8% range for doctors) and specificity (99.1% vs. 95.9–99.2%) for PM detection than the individual experts.
    *   **Candidate 002** noted that their algorithm's performance metrics in the external validation dataset were comparable to those of experts.
    *   **Candidate 001** validated its system against ground truth determined by a reference center (Advanced Clinical Center for Myopia).

3.  **Validation Strategy**: All included studies employed validation sets meeting the size criterion (at least 10% of the training set). **Candidate 002** utilized a large dataset (32,010 images) with cross-validation and a 1,000-image external validation set. **Candidate 003** used 36,515 images for development and a substantial external test set of 14,986 images. **Candidate 001** used 5,176 images for training and 1,844 for evaluation (approx. 35% of training size).

**Conclusion**
The evidence suggests that deep learning algorithms can detect pathological myopia from colour fundus images with high sensitivity and specificity, often exceeding or matching the diagnostic capabilities of ophthalmologists. These AI tools hold significant potential for large-scale screening and clinical decision support in identifying PM. However, variability in reporting metrics (e.g., accuracy vs. sensitivity/specificity for the main outcome) may pose challenges for quantitative meta-analysis pooling.

***

**Final Included Primary-Study Articles**

1.  **Title**: Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.
    **Corpus ID**: 3096

2.  **Title**: AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images.
    **Corpus ID**: 3095

3.  **Title**: Automated detection of myopic maculopathy from color fundus photographs using deep convolutional neural networks.
    **Corpus ID**: 3097
