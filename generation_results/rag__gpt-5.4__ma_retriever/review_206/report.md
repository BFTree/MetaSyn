## Title/abstract screening report

I screened the fixed candidate pool against the stated criteria only, without adding any outside records.

### Review question recap
Eligible studies needed to be:
- primary studies in **English**
- published **from January 2020 to 2023-05-25**
- include **glaucoma patients**
- use **AI / machine learning / deep learning** to **diagnose glaucoma** or **predict/detect progression**
- not be reviews, letters, protocols, conference abstracts, or non-human studies

### High-level screening outcome
Most candidates were excluded because they were:
- **published after the review end date** (many 2024-2026 papers)
- **reviews / scoping reviews / editorials / letters / protocols / corrections**
- **not glaucoma-focused**
- **published before 2020**
- or, from the abstract alone, **did not clearly evaluate AI for glaucoma diagnosis/progression** in eligible patients

## Evidence synthesis

### What the eligible literature looks like
Based on title/abstract screening, the included studies are mostly:
- **cross-sectional diagnostic studies** or retrospective development/validation studies
- focused on **glaucoma diagnosis** more often than progression
- using **fundus photographs, OCT, visual fields, OCTA**, or **multimodal combinations**
- evaluating a range of AI methods including **support vector machines, random forest, neural networks, convolutional neural networks, and multimodal deep learning models**

### Main themes across included studies
1. **Diagnosis dominates over progression**
   - Most eligible studies evaluated AI for classifying glaucomatous vs normal eyes or glaucomatous optic neuropathy.
   - Only a minority addressed **progression**, mainly via **visual field progression** or **future progression risk**.

2. **Multimodal models are a recurring direction**
   - Several studies combined structural and functional data, especially **OCT + visual field** or **fundus + OCT**.
   - Abstracts commonly report that multimodal input improved performance over single-modality approaches.

3. **Clinical evaluation depth varies**
   - Some studies appear closer to real-world or clinical deployment, especially the smartphone-based visual field system.
   - Others are more model-development focused, even if they use patient data and clinically relevant comparators.

4. **Abstracts provide limited reporting detail relevant to DECIDE-AI**
   - Since this review target concerns reporting quality against **DECIDE-AI**, it is notable that, from abstracts alone, key implementation/reporting elements are often not described in detail:
     - workflow integration
     - user interaction
     - site/context
     - handling of failures or unusable tests
     - human-AI interaction
     - prospective deployment procedures
   - Therefore, **full-text review would be essential** to judge DECIDE-AI adherence. Title/abstract screening alone cannot determine checklist scores.

### Study-by-study brief notes
- **Visual field progression** was represented by a machine-learning study comparing classifiers for progression detection.
- **Structural OCT-based diagnosis** was represented by several studies using Spectralis OCT features or AI-derived optic nerve head phenotyping.
- **Multimodal diagnosis** appeared in studies combining visual fields with OCT, or fundus photographs with OCT-informed labeling.
- **Clinical deployment** was most explicit in the smartphone-based visual field deep learning system, which included a development phase and a subsequent cloud-based clinical testing phase.
- **Progression risk stratification** was also represented by a prospective cohort in normal tension glaucoma using automated retinal-vessel analysis derived from a deep-learning system.

## Important caution
Because I am restricted to the supplied titles and abstracts:
- I **cannot score DECIDE-AI adherence**
- I **cannot verify full inclusion details** beyond what is stated in the abstract
- I **cannot infer missing design/reporting information** not explicitly described

## Final included primary-study articles

1. **Corpus ID: 85361**  
   **Development and Comparison of Machine Learning Algorithms to Determine Visual Field Progression.**

2. **Corpus ID: 3188**  
   **Comparison of Different Machine Learning Classifiers for Glaucoma Diagnosis Based on Spectralis OCT.**

3. **Corpus ID: 3196**  
   **Multimodal Machine Learning Using Visual Fields and Peripapillary Circular OCT Scans in Detection of Glaucomatous Optic Neuropathy.**

4. **Corpus ID: 3191**  
   **Use of multimodal dataset in AI for detecting glaucoma based on fundus photographs assessed with OCT: focus group study on high prevalence of myopia.**

5. **Corpus ID: 3197**  
   **Development and clinical deployment of a smartphone-based visual field deep learning system for glaucoma detection.**

6. **Corpus ID: 3198**  
   **Deep Learning-Based Classification of Subtypes of Primary Angle-Closure Disease With Anterior Segment Optical Coherence Tomography.**

7. **Corpus ID: 3189**  
   **Glaucoma Detection Using Support Vector Machine Method Based on Spectralis OCT.**

8. **Corpus ID: 3192**  
   **Risk of Normal Tension Glaucoma Progression From Automated Baseline Retinal-Vessel Caliber Analysis: A Prospective Cohort Study.**

9. **Corpus ID: 85372**  
   **Vessel Density Features of Optical Coherence Tomography Angiography for Classification of Glaucoma Using Machine Learning.**

10. **Corpus ID: 3194**  
    **Describing the Structural Phenotype of the Glaucomatous Optic Nerve Head Using Artificial Intelligence.**

## Bottom line
Using only the supplied candidate pool and title/abstract screening, I identified **10 potentially eligible primary studies**. The evidence is weighted toward **diagnostic AI** rather than **progression detection**, with several **multimodal** approaches and only limited abstract-level detail relevant to **DECIDE-AI reporting quality assessment**. Full-text assessment would be necessary for actual DECIDE-AI adherence scoring.
