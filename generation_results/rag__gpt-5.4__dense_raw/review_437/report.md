## Screening summary

I screened the supplied 200 candidates against the full eligibility criteria:

- **Population:** clinicians diagnosing **skin lesions / skin cancer**
- **Intervention:** **deep learning-based** AI assistance
- **Comparison:** the **same clinicians/tasks without AI assistance**
- **Setting/task:** diagnosis from **skin lesion images or in-person skin lesion assessment**
- **Exclude:** studies that only compare clinicians vs AI, non-deep-learning methods, pathology-slide-only tasks, reviews/editorials/case reports, and studies outside the target review scope

## Eligibility decision

### Included based on title/abstract
I identified **4 eligible primary studies**.

### Common reasons for exclusion
Most other candidates were excluded because they were:
- **reviews, narrative reviews, protocols, editorials, or perspectives**
- **not skin cancer**
- **AI-vs-clinician comparisons only**, with **no clinician with-AI vs without-AI comparison**
- **stand-alone model development/validation** without clinician assistance
- **outside the search window** or otherwise not aligned with the target review

---

## Evidence synthesis

### Overall evidence base
The eligible evidence is **small** and consists of a handful of **primary studies from 2020-2022** evaluating whether deep learning assistance improves clinician skin-cancer diagnosis.

### What the included studies suggest
Across the included abstracts, the direction of effect is **consistently favorable to AI assistance**, with several recurring themes:

1. **AI assistance tends to improve clinician diagnostic performance**
   - All four included abstracts report improved clinician performance with AI support, whether in real-world or reader-study settings.

2. **Benefit appears greatest for less-experienced clinicians**
   - This is explicit in multiple studies:
     - trainee doctors / nondermatologists improved
     - nonexpert physicians improved
     - the least experienced clinicians gained the most

3. **Experts may benefit less**
   - One randomized trial reports improvement mainly in **nondermatology trainees**, not clearly in dermatology residents.
   - This suggests AI may narrow expertise gaps more than improve already-strong specialist performance.

4. **AI can increase differential-diagnosis breadth**
   - At least two studies report that clinicians generated **more differential diagnoses** after AI assistance.

5. **AI can also mislead clinicians when wrong**
   - Included abstracts explicitly warn that faulty or incorrect AI predictions can reduce clinician accuracy.
   - This is important for implementation and indicates that augmentation is not uniformly safe across all cases.

### Important limitations from title/abstract screening
Because I am restricted to the supplied title/abstract text:

- I **cannot confirm full 2×2 diagnostic data** for sensitivity and specificity from abstracts alone.
- Several included abstracts report **top-1 accuracy**, overall accuracy, concordance, or qualitative improvement rather than explicit sensitivity/specificity.
- The eligible evidence appears to be **heterogeneous** in design:
  - prospective controlled before-after
  - randomized controlled trial
  - reader/experimental collaboration studies
- Generalizability may be limited:
  - some studies are from **single centers**
  - some involve **Asian populations only**
  - some use simulated or image-based workflows rather than broad routine practice

### Implication for this review question
Based on title/abstract screening alone, the available primary-study evidence supports the conclusion that **deep learning-based AI assistance probably improves clinician accuracy in skin cancer diagnosis compared with unaided diagnosis**, especially among **less-experienced clinicians**. However, the evidence base is **small**, and the abstracts do not consistently provide the sensitivity/specificity data needed for a robust quantitative synthesis from abstract alone.

---

## Study-by-study notes

### 1) Prospective controlled before-after trainee study
This study appears directly eligible:
- clinicians: **trainee doctors / nondermatologists**
- task: diagnosing **skin neoplasms suspected of malignancy**
- comparison: **with AI assistance vs control/without AI assistance**
- modality: routine exam with photographic review
- result: improved top-1 accuracy after AI assistance

### 2) Randomized controlled trial in skin neoplasms
This is one of the strongest matches to the review question:
- clinicians: nonexpert physicians, including trainees/residents
- task: diagnosis of suspicious skin lesions in real-world setting
- intervention: CNN-based AI assistance
- comparison: AI-assisted vs unaided groups
- result: higher accuracy in AI-assisted group, strongest in less-experienced clinicians

### 3) Human-computer collaboration study
This abstract clearly evaluates clinician performance with AI support:
- clinicians of varying expertise
- skin cancer recognition task
- multiple workflows
- reports improved diagnostic accuracy with good AI support
- also highlights harm from faulty AI

### 4) Acral lentiginous melanoma physician augmentation study
This is directly relevant though narrower in disease scope:
- task focused on **acral lentiginous melanoma detection**
- physicians assessed images in stages, including a final stage with CNN predictions
- clinician performance improved after AI output was added

---

## Final included primary studies

1. **Corpus ID: 2582**  
   **Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study.**

2. **Corpus ID: 114506**  
   **Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial.**

3. **Corpus ID: 2299**  
   **Human-computer collaboration for skin cancer recognition.**

4. **Corpus ID: 2580**  
   **Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks.**

## Bottom line
Using only the supplied candidate pool and only title/abstract information, **4 primary studies were eligible**. Collectively, they suggest that **deep learning-based AI assistance improves clinician skin-cancer diagnostic accuracy versus unaided clinicians**, with the **largest gains in less-experienced clinicians**, but with an important caveat that **incorrect AI can mislead users**.
