## Title/abstract screening summary

Using only the supplied candidate pool and applying the full eligibility criteria, **4 primary-study articles appear eligible** on title/abstract screening.

### Included on title/abstract screening
These studies all appear to:
- involve **clinicians diagnosing skin lesions for skin cancer**,
- use **deep learning / CNN-based AI assistance**,
- compare clinician performance **with vs without AI assistance** on the same or closely matched diagnostic task,
- use **skin lesion images and/or real clinical skin-lesion assessment** rather than pathology-slide diagnosis,
- be **primary studies** within the review period.

### Excluded at title/abstract stage
Most other candidates were excluded because they were:
- **reviews/commentaries/editorials**,
- **AI-vs-clinician comparison studies without an AI-assisted clinician arm**,
- **non-skin-cancer topics**,
- **pathology / histology / other imaging modalities** outside the review question,
- or **published after the search end date**.

Notable near-misses:
- **Candidate 026**: compares AI alone with clinicians and mentions limited clinical usefulness, but the abstract does **not clearly report a clinician with-vs-without-AI accuracy comparison**.
- **Candidate 070**: compares smartphone app/CNNs with dermatologists, but **not clinicians with vs without AI assistance**.
- **Candidate 006**: potentially relevant augmented-intelligence clinical study, but **published in 2023**, outside the search window.

---

## Evidence synthesis

### Overall picture
The eligible abstract-level evidence suggests that **deep learning-based AI assistance can improve clinician diagnostic accuracy in skin cancer diagnosis**, especially for **less experienced or nonexpert clinicians**. Across the included studies, the direction of effect is generally favorable to AI assistance.

### What the included abstracts suggest

#### 1) AI assistance tends to improve overall clinician accuracy
All four included studies report improved clinician performance after adding AI support:
- improved diagnostic accuracy in mixed-expertise clinicians,
- improved trainee/nondermatologist performance in prospective clinical settings,
- improved physician accuracy for acral lentiginous melanoma detection,
- improved nonexpert physician accuracy in a randomized real-world trial.

#### 2) Benefits seem strongest for less experienced clinicians
A recurring pattern is that **junior, trainee, or nonexpert clinicians gain the most** from AI support:
- Candidate 001 explicitly says the **least experienced clinicians gain the most**.
- Candidate 004 focuses on **trainee doctors** and reports improved top-1 accuracy after AI assistance.
- Candidate 007 reports the augmentation was **more significant in nondermatology trainees** and not significant in dermatology residents.

#### 3) AI assistance is not risk-free
The abstracts also indicate that AI can **mislead clinicians when incorrect**:
- Candidate 001 notes that **faulty AI can mislead the entire spectrum of clinicians, including experts**.
- Candidate 007 reports a **12.2% drop in top-1 accuracy** in cases where the algorithm’s top-3 predictions were all wrong.

#### 4) Evidence is more about overall accuracy than sensitivity/specificity
A major limitation for this review question is that, from the abstracts alone, the included studies mainly report:
- **overall accuracy**,
- **top-1 accuracy**,
- or general improvement in diagnostic performance,

rather than the target outcomes of **sensitivity and specificity**.  
So these studies look conceptually eligible, but **abstract-only information is insufficient to extract the review’s primary outcomes reliably**.

---

## Study-by-study notes

### Candidate 001
This appears to be a reader-study type primary study examining **human-computer collaboration** in skin cancer recognition across different expertise levels and workflows. The abstract directly states that **AI-based support improves diagnostic accuracy over either AI or physicians alone**, and that **less experienced clinicians benefit most**. It also warns that **faulty AI can mislead clinicians**.

### Candidate 004
This is a **prospective controlled before-and-after study** in a real-world setting evaluating whether a deep neural network algorithm improves **nondermatologist trainee doctors’** diagnosis of suspicious skin neoplasms. The abstract reports **improved top-1 accuracy** after AI assistance.

### Candidate 005
This study developed a **CNN for acral lentiginous melanoma detection** and tested whether adding its predictions improved physicians’ decisions. In a staged survey, physician accuracy improved from image-only and image-plus-clinical-info stages to the **AI-assisted stage**, supporting benefit from AI augmentation.

### Candidate 007
This is a **single-center randomized controlled trial** evaluating AI-assisted vs unaided diagnosis in real-world dermatology-related clinical practice by trainees/residents. The AI-assisted group had **higher accuracy overall**, with the main benefit in **less experienced nondermatology trainees**. The abstract also clearly highlights the potential harm from **incorrect AI suggestions**.

---

## Limitations of this abstract-based screening
- I am using **only the supplied titles and abstracts**.
- I cannot confirm full-text details such as:
  - exact diagnostic thresholds,
  - whether 2×2 data for sensitivity/specificity are available,
  - lesion-level vs patient-level analysis,
  - exact publication date within 2022,
  - reference standard details,
  - or whether subgroup data are extractable for meta-analysis.
- The review question specifically targets **sensitivity and specificity**, but the included abstracts mostly provide **accuracy-type outcomes**, so full texts would be needed to determine extractability.

---

## Bottom-line conclusion
On title/abstract screening, the available evidence supports inclusion of **4 primary studies**. Collectively, they suggest that **deep learning-based AI assistance probably improves clinician accuracy in skin cancer diagnosis**, with the **largest gains in less experienced clinicians**, but also with a meaningful risk that **incorrect AI advice can worsen decisions**. Based on abstracts alone, however, the evidence is **much stronger for overall accuracy improvement than for directly extractable sensitivity/specificity outcomes**.

---

## Final included primary-study articles

1. **Corpus ID: 2299**  
   **Human-computer collaboration for skin cancer recognition.**

2. **Corpus ID: 2582**  
   **Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study.**

3. **Corpus ID: 2580**  
   **Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks.**

4. **Corpus ID: 114506**  
   **Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial.**
