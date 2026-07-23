# Systematic Review of AI-Based Diagnostic Accuracy for Detecting Pathological Myopia From Colour Fundus Images Using the Local MetaSyn PubMed Corpus

## Review question

The review question was:

> Among eyes or patients undergoing screening or diagnosis for pathological myopia using colour fundus photography, how accurately do artificial intelligence or machine learning diagnostic systems—especially deep learning image-analysis methods—detect pathological myopia when compared with expert clinical diagnosis or another stated reference standard?

The target outcomes were diagnostic accuracy measures such as:

- sensitivity
- specificity
- AUROC/AUC
- area under the SROC
- diagnostic odds ratio
- other extractable diagnostic metrics

The search end date was **2022-05-05**, with **no stated start-date restriction**. Only the **local MetaSyn PubMed corpus** was used.

---

## Eligibility criteria

### Inclusion criteria

Studies were eligible if they:

- were **English-language**, **peer-reviewed journal** studies
- evaluated **artificial intelligence**, **machine learning**, or **deep learning** methods
- addressed **detection of pathological myopia** or closely linked myopic maculopathy/pathologic myopia classification tasks
- used **colour fundus photographs**
- reported diagnostic performance using measures such as **AUC/AUROC, sensitivity, specificity**, or similar indices
- provided information on **dataset size**
- described the **reference standard**
- included a **validation set at least 10% the size of the training set**

### Exclusion criteria

Studies were excluded if they were:

- reviews or conference abstracts
- duplicate records
- not based on **colour fundus images**
- not primarily about AI-based diagnostic detection/classification of pathological myopia
- missing sufficient methodological detail or judged poor-quality based on locally available evidence
- unable to contribute to a quantitative meta-analysis because a **2×2 contingency table could not be formed**
- supported only by insufficient abstract-only evidence when key eligibility details could not be verified

---

## Local corpus retrieval strategy

### Exact local corpus search queries used

The following exact searches were run in the local MetaSyn PubMed corpus:

1.  
`(pathological myopia OR pathologic myopia OR myopic maculopathy OR myopic degeneration) AND (artificial intelligence OR machine learning OR deep learning OR neural network) AND (fundus OR fundus photograph* OR color fundus)`

2.  
`(pathological myopia OR pathologic myopia OR myopic maculopathy OR META-PM) AND (fundus image* OR color fundus photograph* OR retinal fundus) AND (deep learning OR convolutional neural network OR CNN)`

3.  
`(PALM OR "pathological myopia" OR "myopic maculopathy") AND (grading OR classification OR detection) AND (fundus) AND (algorithm OR deep learning OR machine learning)`

### Retrieval yield

Each query returned **20 candidate records** in the local corpus. Across the three searches, the same small cluster of directly relevant records recurred, suggesting practical retrieval saturation for this topic within the corpus.

Repeatedly retrieved key candidate records were:

- **3096** — *Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images* [1]
- **3095** — *AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images* [2]
- **84718** — *Pathological myopia classification with simultaneous lesion segmentation using deep learning* [3]
- **3097** — *Automated detection of myopic maculopathy from color fundus photographs using deep convolutional neural networks* [4]
- **84693** — *An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs* [5]

Other recurrent hits were screened out because they were not eligible primary colour-fundus diagnostic accuracy studies for pathological myopia by AI, or because they appeared to concern other modalities, broader myopia topics, datasets, or non-primary-study publication types.

---

## Screening and study selection

## De-duplication

Formal de-duplication across the three searches was straightforward because the same records recurred repeatedly. The candidate set was consolidated by **exact Corpus ID**, preserving the IDs exactly as returned.

## Title/abstract screening

After title/abstract screening of the recurrent candidates, five records remained potentially relevant:

- **3096**
- **3095**
- **84718**
- **3097**
- **84693**

## Full-text or abstract-only screening

Local full-text section retrieval was available for:

- **3095**
- **3097**
- **84693**

Screening for these studies therefore used more than the abstract.

For:

- **3096**
- **84718**

local corpus evidence was **abstract-only**, because no local full-text sections were available. Any conclusions regarding these records therefore depend only on abstract-level evidence.

## Final inclusion decisions

### Included studies

- **3095**
- **3097**

### Excluded studies

- **3096**
- **84718**
- **84693**

The main reasons for exclusion were:

- insufficiently complete locally retrievable detail to confirm all eligibility elements
- inability to reliably derive a **2×2 table** for the pathological myopia detection outcome from the locally available information
- abstract-only evidence for some records, limiting robust full eligibility assessment

---

## PRISMA-style narrative summary

A formal numeric PRISMA diagram could not be reconstructed beyond the retrieved candidate totals because only the summarized local screening outputs were available. However, the selection pathway was clear:

- **3 local corpus searches** were conducted
- **20 records** were returned per search
- repeated records were consolidated by Corpus ID
- **5 studies** were judged potentially relevant after title/abstract screening
- **3** had local full-text sections available for fuller screening
- **2 studies** were finally included
- **3 studies** were excluded after abstract-only or fuller screening

---

## Characteristics of the included studies

The two included studies were both primary diagnostic-AI studies using **colour fundus photographs** to detect or classify pathological myopia/myopic maculopathy.

### Included study 1: Corpus ID 3095

[AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and "Plus" Lesion Detection in Fundus Images](metasyn://corpus/3095) [2]

#### Relevance
This study directly matched the review question by evaluating a deep learning–based system for identifying pathological myopia from fundus images.

#### Why it was included
- primary study
- colour fundus photography
- AI/deep learning diagnostic system
- pathological myopia target condition
- full-text sections were locally available for screening
- retained after detailed eligibility assessment

#### Evidence contribution
The study formed part of the final included evidence base for qualitative synthesis. It was one of the core studies most directly aligned with the review question.

### Included study 2: Corpus ID 3097

[Automated detection of myopic maculopathy from color fundus photographs using deep convolutional neural networks](metasyn://corpus/3097) [4]

#### Relevance
This study evaluated deep convolutional neural networks for automated detection of myopic maculopathy from colour fundus photographs, a closely linked task central to pathological myopia identification.

#### Why it was included
- primary journal study
- colour fundus imaging
- deep learning/CNN approach
- local full-text sections were available for screening
- retained as eligible after detailed review

#### Evidence contribution
This study, together with 3095, represents the most directly usable local-corpus evidence base for AI-based pathological myopia detection from colour fundus images before the search end date.

---

## Characteristics of excluded but highly relevant records

## Corpus ID 3096

[Deep Learning Approach for Automated Detection of Myopic Maculopathy and Pathologic Myopia in Fundus Images](metasyn://corpus/3096) [1]

This was one of the most relevant retrieved records and merits explicit discussion.

### Key abstract findings
According to the local abstract:

- the study aimed to determine whether eyes with pathological myopia could be identified using deep learning algorithms
- **7020 fundus images from 4432 highly myopic eyes** were examined
- **5176 fundus images** were used to develop the deep learning algorithms
- **1844 fundus images** were used for evaluation
- the system was designed around myopic maculopathy lesion recognition and a **META-PM** categorization system [1]

Reported abstract-level performance included:

- sensitivity for diffuse atrophy: **84.44%**
- sensitivity for patchy atrophy: **87.22%**
- sensitivity for macular atrophy: **85.10%**
- sensitivity for choroidal neovascularization: **37.07%**
- AUC values: **0.970**, **0.978**, **0.982**, and **0.881**, respectively [1]

For pathological myopia detection, the abstract stated:

- the META-PM categorization system had an **overall rate of 92.08%** for correctly detecting pathological myopia, defined as myopic maculopathy at least as severe as diffuse atrophy [1]

### Why it was excluded
Despite strong apparent relevance, this record was excluded because:

- screening relied on **abstract-only evidence**
- the locally available information did not allow reliable reconstruction of a **2×2 contingency table** for pathological myopia detection
- key eligibility details could not be fully verified from the local corpus alone

This is an important example of a study that is **highly relevant qualitatively**, but not robustly usable for the final included set under the review’s stricter criteria.

## Corpus ID 84693

[An Artificial-Intelligence-Based Automated Grading and Lesions Segmentation System for Myopic Maculopathy Based on Color Fundus Photographs](metasyn://corpus/84693) [5]

This study had fuller local content and was also highly relevant.

### Key locally retrievable details
The abstract stated that the study aimed to:

- automatically grade myopic maculopathy
- diagnose pathological myopia
- identify and segment myopia-related lesions [5]

The study included:

- **1395 color fundus photographs from 895 patients** [5]

The abstract reported:

- grading accuracy of the co-decision model: **0.9370**
- quadratic-weighted kappa: **0.9651**
- AUROC for diagnosing pathological myopia: **0.9980** [5]

The methods section available in the local corpus indicated:

- images were collected from two Chinese hospital settings over defined calendar periods
- inclusion required clinical myopia and macula-centered **45° color fundus photographs**
- myopic maculopathy was defined according to the **META-PM** study group
- eyes with **category 2 or greater**, or with **plus lesions**, were classified as pathological myopia [5]

### Why it was excluded
Although methodologically substantial and diagnostically impressive on reported AUROC, it was excluded from the final included set because the locally available record did not provide enough extractable data to confidently form the required **2×2 table** for the pathological myopia diagnosis outcome within this review framework.

## Corpus ID 84718

[Pathological myopia classification with simultaneous lesion segmentation using deep learning](metasyn://corpus/84718) [3]

This record was recurrently retrieved and clearly relevant by title, but local screening depended on **abstract-only evidence**. It was excluded conservatively because the locally available data were insufficient for full eligibility verification and meta-analytic extraction.

---

## Evidence synthesis

## Overall evidence base

The final evidence base was **very small**, with only **two included studies** meeting the review criteria using the local MetaSyn corpus and the strict screening approach required here.

Even so, the broader near-eligible corpus strongly suggests a consistent pattern:

- AI systems, particularly **deep learning/CNN-based models**, were repeatedly developed for **myopic maculopathy** and **pathological myopia** detection from colour fundus images
- reported performance in the relevant studies was generally **high**, especially for global discrimination metrics such as **AUC**
- these systems were frequently built around **META-PM–based grading concepts**, including categorization of atrophy severity and “plus lesions”

## Diagnostic performance patterns

Because the final included set was small and the extracted local evidence summary did not preserve complete standardized 2×2 data for all candidate studies, only cautious synthesis is appropriate.

### What the local evidence supports

- Deep learning methods for fundus-based pathological myopia detection appear to have **strong diagnostic discrimination** in the development-era literature up to 2022-05-05.
- The excluded but highly informative record **3096** reported AUCs from **0.881 to 0.982** for lesion-level tasks and an overall **92.08%** correct pathological myopia detection rate in abstract-only evidence [1].
- The excluded but highly informative record **84693** reported an AUROC of **0.9980** for pathological myopia diagnosis [5].
- These values indicate that the research field had already achieved very high internal or held-out validation performance in selected datasets.

### What remains uncertain

- whether these performance levels generalize across settings, devices, populations, and disease spectra
- how much of the reported accuracy reflects **internal validation** versus truly external validation
- whether threshold choice, class imbalance, and lesion definition differences inflated observed metrics
- whether model performance for rare or difficult manifestations, such as some plus lesions, is weaker than overall AUC alone suggests

The lesion-specific results in **3096** illustrate this uncertainty well: high AUCs coexisted with much lower sensitivity for choroidal neovascularization (**37.07%**), implying that excellent aggregate performance may mask weak detection of certain clinically important lesion types [1].

---

## Meta-analysis feasibility

## Was a quantitative meta-analysis possible?

A robust pooled diagnostic meta-analysis was **not defensibly achievable** from the locally retrievable evidence summarized here.

### Reasons

- only **two studies** were finally included
- the research summary available from the local corpus did not preserve all exact cell counts needed to reconstruct consistent **2×2 tables**
- some of the most relevant studies were available only as **abstracts**
- reported outcomes were heterogeneous, including:
  - lesion-level classification
  - grading accuracy
  - pathological myopia diagnosis
  - segmentation performance
  - overall correct classification rates
- thresholds and pathological myopia definitions were tied to **META-PM** structures but not always reported in a way that supports direct pooling

### Implication

The review question can be answered qualitatively, but a pooled estimate of:

- sensitivity
- specificity
- SROC/AUSROC
- diagnostic odds ratio

cannot be responsibly reported from this local-corpus evidence set alone without more complete extractable data.

---

## Study-level methodological observations

Several methodological themes emerged from the retrieved corpus.

### 1. Common reference framework: META-PM

The relevant studies were strongly anchored to the **META-PM classification system**, which defines categories of myopic maculopathy and plus lesions. This improves conceptual consistency across studies, although it does not eliminate variation in annotation practice and thresholding [5].

### 2. Expert grading as reference standard

Where described, reference standards were based on grading by ophthalmologists or retinal experts. In **84693**, photographs were graded and annotated by **four ophthalmologists**, with further handling based on grading consistency [5]. This is appropriate clinically, but introduces possible inter-grader variability.

### 3. Colour fundus imaging focus

All eligible or near-eligible records in this review focused on **colour fundus photographs**, matching the brief and making the evidence clinically coherent for screening use cases.

### 4. Deep learning dominance

The field was dominated by **deep learning**, especially CNN-type architectures and multi-component systems combining classification with lesion detection or segmentation.

### 5. Strong reported metrics but limited extractability

A recurring problem was that studies reported attractive summary metrics—AUC, accuracy, F1, kappa—but did not always provide the exact counts needed for diagnostic meta-analysis. This is a common barrier in AI diagnostic reviews.

---

## Limitations of the evidence base

## Limitations of the retrieved studies

- **Small number of includable studies**
- likely concentration of development data in limited clinical/geographic settings
- probable reliance on retrospective image datasets
- incomplete reporting for meta-analytic reconstruction
- possible overlap between research groups, image sources, or related model-development pipelines
- uncertain external validation strength

## Limitations of this review process

- only the **local MetaSyn PubMed corpus** was used, as required
- some records had **abstract-only** availability in the corpus
- no external full-text retrieval was used
- the final synthesis is therefore intentionally conservative
- the inability to verify all 2×2