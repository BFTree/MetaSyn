## Review aim

This screening targets **primary diagnostic-accuracy studies** of **AI/machine learning for detecting pathological myopia (PM) from colour fundus photographs**, using a clinical/expert reference standard and reporting metrics such as sensitivity, specificity, and/or AUC.

I screened the supplied candidate titles/abstracts only. I did **not** search beyond this fixed pool and do **not** assume information not stated in the abstracts.

---

## Screening summary

### Clearly ineligible on topic/modality/date/design grounds
Most candidates were excluded because they were:
- not about pathological myopia,
- not based on **colour fundus images**,
- reviews/meta-analyses/protocols,
- focused on OCT or other imaging rather than colour fundus photography,
- or published after the source review’s search end and therefore out of scope.

Examples:
- OCT-only myopia studies: Candidates 066, 074, 112
- Reviews or non-primary studies: 005, 016, 029, 030, 080, 089, 103, 111, 162, 173
- Post-search-end PM/MM studies: 001, 002, 072, 177, 185
- Non-PM ophthalmic or non-ophthalmic topics: many others

### Borderline but excluded
- **Candidate 027** reported PM classification from fundus images, but the abstract does not clearly establish all required inclusion elements for this review, especially a journal-style validation structure meeting the stated review criterion and sufficiently explicit reference-standard detail. Given the instruction to screen against the full criteria using title/abstract only, I did **not** include it.

---

## Included evidence

Based on the available title/abstract information, **3 studies** appear eligible.

### 1) Corpus ID: 3096  
**Title:** *Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.*

**Why included**
- Primary study
- AI/deep learning for **pathologic myopia / myopic maculopathy**
- Uses **fundus images** (colour fundus photography implied in abstract)
- Reports diagnostic metrics including **AUC, sensitivity, specificity**
- Includes dataset sizes and a held-out evaluation set
- Relevant outcome: PM detection performance

**Key abstract details**
- 7020 fundus images from 4432 highly myopic eyes
- 5176 images used for model development; 1844 for evaluation
- PM defined as myopic maculopathy at least as severe as diffuse atrophy
- Reported lesion-level sensitivities and AUCs; overall PM detection correctness 92.08%

**Limitations from abstract-only assessment**
- The abstract is less explicit than some others about the exact reference-standard process, though manual lesion categorization is strongly implied.

---

### 2) Corpus ID: 3095  
**Title:** *AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images.*

**Why included**
- Primary diagnostic study
- Focused directly on **identifying pathologic myopia**
- Uses **color retinal fundus images**
- Reports **AUC, sensitivity, specificity, accuracy**
- Provides dataset size and **external validation**
- Explicit comparison with experts

**Key abstract details**
- 32,010 manually graded color retinal fundus images for training/cross-validation
- External validation dataset: 1,000 images from 732 patients from 3 other hospitals
- Five-fold cross-validation: AUC 0.995, sensitivity 93.92%, specificity 98.19% for algorithm I
- External validation performance comparable to experts

**Strengths apparent from abstract**
- Large dataset
- External validation
- Explicit expert comparison
- Uses META-PM classification framework

---

### 3) Corpus ID: 84693  
**Title:** *An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs.*

**Why included**
- Primary study
- Uses **color fundus photographs**
- Directly addresses **diagnose pathologic myopia**
- Reports diagnostic accuracy including **AUC**
- Dataset size and reference-standard grading are described
- Relevant to automated PM/MM detection from fundus images

**Key abstract details**
- 1395 color fundus photographs from 895 patients
- Images graded and annotated by four ophthalmologists
- Co-decision model grading accuracy 0.9370; quadratic-weighted kappa 0.9651
- AUC for diagnosing pathologic myopia: **0.9980**
- Also reports lesion segmentation performance

**Limitations from abstract-only assessment**
- Sensitivity/specificity for PM are not explicitly quoted in the abstract, though diagnostic AUC is.

---

## Evidence synthesis

### Overall picture
The included abstracts consistently suggest that **AI, particularly deep learning applied to colour fundus photographs, can detect pathological myopia or its defining myopic maculopathy features with high accuracy**.

### Study characteristics
Across the included studies:
- All used **fundus photographs / color retinal fundus images**
- All addressed **pathologic myopia identification** directly or through automated grading of myopic maculopathy
- All used ophthalmologist/expert-based grading frameworks as the practical reference standard
- All reported standard discrimination metrics, especially **AUC**, and two clearly reported **sensitivity/specificity**

### Performance patterns
- Reported AUCs were very high where stated:
  - Candidate 007: **AUC 0.995**
  - Candidate 033: **AUC 0.9980**
  - Candidate 006: lesion AUCs **0.881 to 0.982**
- Sensitivity/specificity were also strong where explicitly reported:
  - Candidate 007: **sensitivity 93.92%, specificity 98.19%**
- Candidate 006 additionally suggests that performance varied by lesion subtype, with notably lower sensitivity for **choroidal neovascularization** than for atrophic lesions, indicating that not all PM-associated findings are equally easy for AI to detect.

### Clinical interpretation
From the abstracts alone, these studies support the idea that AI systems could function as:
- **screening tools** for PM/MM,
- **decision-support systems** for grading lesion severity,
- and possibly aids for **large-scale or resource-limited screening**.

### Important caveats
Using only title/abstract screening, several limitations remain:
1. **Reference standards** are not equally detailed across abstracts.
2. Not every abstract provides a full **2×2 table** or enough raw data for meta-analysis.
3. External validation is strongest in Candidate 007; the others appear promising but are less fully described in abstract.
4. Performance may differ by **specific lesion type**, so pooled “PM detection” can mask clinically relevant heterogeneity.

---

## Bottom-line conclusion

From the fixed candidate pool, the abstract-level evidence supports that **deep learning systems using colour fundus photographs can detect pathological myopia with high discriminative performance**, often approaching expert-level grading and, in at least one study, validating externally. The evidence base identified here is small but consistent in direction.

---

## Final included primary-study articles

1. **Corpus ID: 3096**  
   **Title:** *Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.*

2. **Corpus ID: 3095**  
   **Title:** *AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images.*

3. **Corpus ID: 84693**  
   **Title:** *An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs.*
