## Evidence-synthesis report

### Review question
Whether **deep learning-based AI assistance** improves **clinicians’ diagnostic accuracy** for **skin cancer / skin neoplasm diagnosis** compared with the **same clinicians diagnosing without AI assistance**.

### Screening approach used
I screened the supplied candidate titles and abstracts against all stated criteria:

- **Population:** clinicians diagnosing skin lesions / skin cancer
- **Intervention:** **deep learning-based** AI assistance
- **Comparison:** clinicians doing the same task **without AI assistance**
- **Outcome:** diagnostic accuracy data relevant to skin cancer diagnosis
- **Setting/task:** diagnosis from skin lesion images and/or real-world clinical skin-lesion assessment
- **Dates:** 2017-01-01 to 2022-11-08
- **Exclusions:** studies that only compare AI vs clinicians, non-skin-cancer topics, non-deep-learning methods, reviews/editorials/protocols/case reports, pathology-slide-only tasks, or articles outside the date window

### Overall screening result
From the supplied pool, **3 primary-study articles appear eligible** on title/abstract screening.

Most other candidates were excluded because they were:
- outside the date range,
- not about skin cancer,
- not clinician-with-AI vs clinician-without-AI comparisons,
- reviews rather than primary studies,
- or focused on stand-alone algorithm performance only.

---

## Included evidence: study-level summary

### 1) Prospective before-after study in trainee/nondermatologist doctors
This study directly matches the review question well. It evaluated whether an AI algorithm improved the accuracy of **nondermatologists / trainee doctors** diagnosing suspicious skin neoplasms in a **real-world setting**. The abstract explicitly reports a comparison of clinician performance **before and after AI assistance**, with a contemporaneous control group reviewed without AI assistance.

Key abstract-level findings:
- AI-assisted group Top-1 accuracy improved from **46.5% to 58.3%**.
- Control-group change after photographic review alone was not significant.
- Benefit appeared in less-expert clinicians.

Relevance:
- Population and intervention fit closely.
- Deep learning is stated.
- Skin neoplasms suspicious for malignancy are within scope.
- Outcome is clinician diagnostic accuracy, though the abstract does **not provide sensitivity/specificity**.

### 2) Randomized controlled trial of AI-assisted diagnosis of skin neoplasms
This is the strongest design among the eligible studies from the pool. It randomized suspicious skin-lesion cases to AI-assisted versus unaided assessment by nonexpert physicians/trainees and residents in a real-world clinical setting.

Key abstract-level findings:
- AI-assisted overall accuracy: **53.9%**
- Unaided overall accuracy: **43.8%**
- Improvement was especially notable in **nondermatology trainees**
- No significant improvement reported for dermatology residents

Relevance:
- Strong direct fit to the review question
- Deep learning/convolutional neural networks explicitly mentioned
- Clinician-with-AI vs clinician-without-AI comparison is clear
- Outcome again is overall diagnostic accuracy rather than sensitivity/specificity in the abstract

### 3) Human-computer collaboration study for skin cancer recognition
This study also appears eligible from abstract information. It evaluated different forms of AI-based support for skin cancer recognition across clinicians with varying expertise and workflows.

Key abstract-level findings:
- “Good quality AI-based support” improved diagnostic accuracy over either AI or physicians alone.
- Less experienced clinicians benefited most.
- The study also warns that faulty AI could mislead clinicians.

Relevance:
- Directly studies clinician performance **with AI support**
- Skin cancer recognition task
- Deep-learning-based AI support is implied by the framing of image-based AI and multiclass probabilities
- The abstract is less detailed than the two 2022 studies and does not provide sensitivity/specificity figures in the abstract

---

## Synthesis of findings

### Direction of effect
Across the eligible studies, the abstract-level evidence is **consistently favorable** to AI assistance:

- All 3 included studies report that AI assistance **improved clinician diagnostic performance** overall or in at least some clinician groups.
- The benefit was most consistently seen in **less-experienced clinicians** or **nonexperts/trainees**.

### Strength of evidence
Based on title/abstract alone:

- **Most directly informative study designs:** the **randomized controlled trial** and the **prospective controlled before-and-after study**
- **Supporting evidence:** the broader human-computer collaboration study, which also suggests performance gains but provides fewer quantitative abstract details

### Important limitations visible from abstracts
1. **Outcome mismatch with planned meta-analysis metrics**
   - The review question emphasizes **sensitivity and specificity**.
   - The included abstracts mostly report **Top-1 accuracy** or overall diagnostic accuracy, not full 2×2 diagnostic data.

2. **Likely stronger benefit in less-experienced clinicians**
   - The effect may not generalize equally to dermatology specialists; one abstract suggests little or no significant gain among dermatology residents.

3. **Potential harms from incorrect AI**
   - One abstract explicitly notes that incorrect AI predictions can **mislead clinicians**.

4. **Generalizability concerns**
   - At least one study was conducted in South Korea and notes limitations regarding population/region/ethnicity.
   - Real-world diversity of lesions, workflows, and clinician expertise may vary.

5. **Possible overlap**
   - The two 2022 South Korean studies appear closely related in topic and setting; title/abstract alone is insufficient to determine whether populations overlap.

### Bottom-line conclusion from the supplied candidate pool
On title/abstract screening, the available primary-study evidence suggests that **deep learning-based AI assistance can improve clinician diagnostic accuracy in skin cancer/skin neoplasm diagnosis, especially for less-experienced clinicians**, compared with unaided diagnosis. However, the abstracts do **not consistently provide sensitivity and specificity**, so their utility for a sensitivity/specificity meta-analysis would depend on full-text data extraction.

---

## Final included primary-study articles

1. **Corpus ID: 2582**  
   **Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study.**

2. **Corpus ID: 114506**  
   **Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial.**

3. **Corpus ID: 2299**  
   **Human-computer collaboration for skin cancer recognition.**

If you want, I can next convert this into a stricter **PRISMA-style screening table** with include/exclude decisions for the most relevant near-miss candidates.
