## Title/abstract screening summary

Using only the fixed candidate pool and the stated eligibility criteria, I identified **2 studies as clearly includable primary studies** on title/abstract information alone.

Because the review search ended on **2022-05-05**, I treated later publications as ineligible and treated some **2022** items as **date-uncertain** when the abstract did not provide a month/day. I also excluded studies that used **OCT rather than colour fundus photography**, studies on **general myopia/high myopia rather than pathological myopia**, and **reviews/challenges/datasets**.

## Brief evidence synthesis

### Overall evidence base
The includable abstract-level evidence is small but consistent: both included studies evaluated **deep learning/artificial intelligence systems on colour fundus photographs** for identifying **pathological myopia (PM)** or PM-defining myopic maculopathy, using human expert grading/META-PM-based grading as the reference framework.

### Study characteristics and main findings
- Both studies were **retrospective image-based diagnostic studies**.
- Both used **large image datasets** and reported standard diagnostic accuracy metrics.
- Both appear to use **expert/manual grading** aligned with **META-PM** classification as the reference standard.
- Both reported **high discrimination** for PM detection from colour fundus images.

### Diagnostic accuracy signal
Across the included studies:
- Reported **AUC** values for PM identification were very high:
  - **0.995** in cross-validation in one study
  - **overall PM detection rate 92.08%** in another study, with lesion-level AUCs **0.970-0.982** for several myopic maculopathy features
- Reported sensitivity/specificity were generally high for PM/MM tasks, though performance varied by lesion type:
  - PM-identification model in one study: **sensitivity 93.92%, specificity 98.19%**
  - Lesion-level sensitivity in the other study was strong for atrophic lesions but notably lower for **choroidal neovascularization (37.07%)**, suggesting harder detection for some lesion subtypes

### What this suggests
From the included abstract-level evidence, AI—especially deep learning—shows **strong potential for PM screening/diagnosis from colour fundus photographs**, with:
- high overall discrimination,
- strong sensitivity/specificity for PM detection,
- but potentially weaker performance for some specific PM-related lesions.

### Important limitations of this synthesis
This synthesis is constrained because:
1. I used **only titles and abstracts**.
2. I could not verify full-text details such as:
   - exact reference-standard procedures,
   - exact 2×2 tables,
   - model-development quality,
   - whether all studies met the review’s validation-size rule in full.
3. Some **2022 studies looked highly relevant** but had **uncertain eligibility relative to the search cutoff date** based on abstract data alone.

## Notable borderline studies not finally included
These looked relevant on topic but were **not included in the final set** because eligibility could not be fully confirmed from the supplied abstract alone, mainly due to **search-date uncertainty** or incomplete abstract-level reporting:
- **Candidate 003**: likely relevant, but **2022 publication timing relative to 2022-05-05 cannot be confirmed**
- **Candidate 004**: likely relevant, but same **date uncertainty**
- **Candidate 007**: topic-relevant, but the abstract does not clearly state the reference-standard details required by the criteria

## Final included primary-study articles

1. **Corpus ID: 3096**  
   **Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images.**

2. **Corpus ID: 3095**  
   **AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images.**

If you want, I can also turn this into a more formal **systematic review table** with columns like population, index test, reference standard, dataset size, and key accuracy results.
