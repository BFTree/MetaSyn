# Systematic Review Report: Deep Learning–Based AI Assistance for Clinician Diagnosis of Skin Cancer

## Review Question

Among clinicians diagnosing skin lesions for skin cancer, does deep learning–based AI assistance improve diagnostic accuracy—specifically sensitivity and specificity—compared with the same clinicians performing the same diagnostic task without AI assistance?

## Scope and Methods

### Retrieval source and date limits

The evidence base was restricted to the local MetaSyn PubMed corpus only. No external databases or web searches were used. Retrieval was limited to records dated from **2017-01-01 through 2022-11-08**.

### Eligibility criteria applied

Studies were screened using the following criteria:

**Inclusion**
- Primary studies directly comparing clinicians diagnosing skin cancer **with AI assistance versus without AI assistance**
- Diagnosis based on **images of skin lesions** or **in-person visits**
- Any clinician expertise level
- Any study design, sample size, reference standard, or skin diagnosis, provided at least one skin malignancy was included
- Data from non-physician medical professionals only if physicians were also included

**Exclusion**
- Diagnosis based on material other than skin lesion images or in-person visits, such as pathology slides
- Studies comparing clinicians only against AI, without a clinician-with-AI versus clinician-without-AI comparison
- Non–deep learning techniques
- Editorials, reviews, and case reports

### Search queries used in the local corpus

The following focused searches were run against the local MetaSyn PubMed corpus:

1.  
`(skin cancer OR melanoma OR skin lesion) AND (artificial intelligence OR deep learning OR neural network) AND (clinician OR dermatologist OR physician OR general practitioner) AND (assistance OR aided OR support) AND (diagnostic accuracy OR sensitivity OR specificity) AND date:[2017-01-01 TO 2022-11-08]`

2.  
`(skin lesion OR melanoma OR skin neoplasm) AND (AI-assisted OR artificial intelligence-assisted OR augmented OR human-computer collaboration OR decision support) AND (dermatologist OR physician OR trainee OR clinician) AND (sensitivity OR specificity OR accuracy) AND date:[2017-01-01 TO 2022-11-08]`

3.  
`(dermatology resident OR dermatologist OR trainee OR physician) AND (skin neoplasm OR skin cancer OR melanoma) AND (AI-assisted OR CNN support OR augmented intelligence OR decision support) AND (randomized OR prospective OR survey OR trial) AND date:[2017-01-01 TO 2022-11-08]`

### Records retrieved from the local corpus

The searches returned the following candidate records:

- **Corpus ID 114492** — *Skin cancer classification via convolutional neural networks: systematic review of studies involving human experts*
- **Corpus ID 35140** — *Artificial intelligence for melanoma diagnosis*
- **Corpus ID 2299** — *Human-computer collaboration for skin cancer recognition*
- **Corpus ID 2580** — *Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks*
- **Corpus ID 2582** — *Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study*
- **Corpus ID 114506** — *Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial*
- **Corpus ID 114484** — *Diagnostic performance of augmented intelligence with 2D and 3D total body photography and convolutional neural networks in a high-risk population for melanoma under real-world conditions: A new era of skin cancer screening?*
- **Corpus ID 2581** — *Performance of a deep neural network in teledermatology: a single-centre prospective diagnostic study*

## Screening and Study Selection

### Included studies

Three studies clearly met the review question and eligibility criteria based on the available local corpus records:

1. [Human-computer collaboration for skin cancer recognition](local://corpus/2299) [1]  
   **Corpus ID:** 2299

2. [Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks](local://corpus/2580) [2]  
   **Corpus ID:** 2580

3. [Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study](local://corpus/2582) [3]  
   **Corpus ID:** 2582

### Excluded candidate studies and reasons

- [Skin cancer classification via convolutional neural networks: systematic review of studies involving human experts](local://corpus/114492) [4]  
  **Corpus ID:** 114492  
  **Reason for exclusion:** systematic review, not a primary study.

- [Artificial intelligence for melanoma diagnosis](local://corpus/35140) [5]  
  **Corpus ID:** 35140  
  **Reason for exclusion:** the retrieved record did not establish a direct clinician-with-AI versus clinician-without-AI primary comparison; likely commentary/review-oriented rather than an eligible primary intervention study based on the available corpus information.

- [Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial](local://corpus/114506) [6]  
  **Corpus ID:** 114506  
  **Reason for exclusion:** potentially relevant, but the available retrieved evidence from the local corpus abstract was insufficient here to confirm all eligibility details and extract the required comparative sensitivity/specificity data reliably. It therefore could not be confidently included.

- [Diagnostic performance of augmented intelligence with 2D and 3D total body photography and convolutional neural networks in a high-risk population for melanoma under real-world conditions: A new era of skin cancer screening?](local://corpus/114484) [7]  
  **Corpus ID:** 114484  
  **Reason for exclusion:** title suggests augmented intelligence in screening, but no retrieved local-corpus text was available here to confirm a direct clinician-with-AI versus clinician-without-AI comparison.

- [Performance of a deep neural network in teledermatology: a single-centre prospective diagnostic study](local://corpus/2581) [8]  
  **Corpus ID:** 2581  
  **Reason for exclusion:** appears to assess AI performance in teledermatology rather than a direct within-task comparison of clinicians with versus without AI assistance.

## Characteristics of the Included Evidence

## Study 1: Human-computer collaboration for skin cancer recognition

[Human-computer collaboration for skin cancer recognition](local://corpus/2299) [1] was included because it is a primary study evaluating AI-supported clinician decision-making for skin cancer recognition using image-based diagnosis.

### Why it was included
- Primary study
- Deep learning–based AI support
- Direct comparison of clinician performance with AI support versus without AI support
- Skin cancer recognition from lesion images
- Physician participants included

### Evidence availability
- **Abstract-only evidence in the local corpus**

### Key findings available from the abstract
The abstract states that:
- good-quality AI-based support improved diagnostic accuracy beyond either AI alone or physicians alone
- less experienced clinicians benefited most
- poor-quality AI could mislead clinicians across expertise levels

### Sensitivity and specificity
- **No numeric sensitivity or specificity values were available in the local corpus abstract**
- The study therefore supports the direction of effect—improved accuracy with AI support—but does **not** contribute extractable sensitivity/specificity estimates from the available local corpus content

## Study 2: Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks

[Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks](local://corpus/2580) [2] examined whether CNN output improves physician detection of acral lentiginous melanoma from dermoscopic images.

### Why it was included
- Primary study
- Deep-learning CNN intervention
- Physician participants
- Direct staged comparison of decisions without AI and with AI-provided prediction/probability
- Skin malignancy included: acral lentiginous melanoma

### Evidence availability
- **Abstract-only evidence in the local corpus**

### Study design details available from the abstract
- CNN trained on **1,072 dermoscopic images**
- **60 physicians** completed a three-stage survey
- Stage I: dermoscopic images only
- Stage II: images plus clinical information
- Stage III: images plus clinical information plus CNN diagnosis/probability

### Reported diagnostic performance
The abstract reports overall **accuracy**, not sensitivity/specificity:
- Stage I: **74.7%** (95% CI 72.6–76.8)
- Stage II: **79.0%** (95% CI 76.7–81.2)
- Stage III: **86.9%** (95% CI 85.3–88.4)

This implies an increase of:
- **+12.2 percentage points** from Stage I to Stage III
- **+7.9 percentage points** from Stage II to Stage III

Concordance also increased:
- Fleiss κ 0.436 in Stage I
- Fleiss κ 0.506 in Stage II
- Fleiss κ 0.684 in Stage III

### Sensitivity and specificity
- **No numeric sensitivity or specificity values were available in the local corpus abstract**
- The study indicates improved overall diagnostic performance with AI support, but it does not provide extractable sensitivity/specificity from the accessible record

## Study 3: Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study

[Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study](local://corpus/2582) [3] was the most information-rich included study because methods, results, and discussion sections were available in the local corpus.

### Why it was included
- Primary prospective controlled before-and-after study
- Deep learning–based CNN assistance
- Real-world skin lesion diagnosis
- Direct clinician comparison with and without AI support
- Physician participants included

### Evidence availability
- **Full-text sections available in the local corpus**: methods, results, discussion

### Study design and population
The local corpus record reports:
- prospective study at **two tertiary care centers in Korea**
- conducted from **February 1, 2020 to November 7, 2020**
- included adults with skin neoplasms suspected of malignancy by patient or physician
- final analysis used **270 pathologically diagnosed** cases and **15 clinically diagnosed** cases
- participants included:
  - **10 attending physicians**
  - **11 dermatology trainees**
  - **7 intern doctors**

The AI system:
- was trained on **721,749 image crops** across **178 disease classes**
- used transfer learning with ImageNet-pretrained CNN models
- combined **SE-Net** and **SE-ResNeXt-50**
- produced top-three diagnoses and a malignancy score

### Comparator structure
- A trainee took history, examined the patient, took photographs, and generated diagnoses
- In the AI arm, the trainee uploaded an image and received AI output
- The study directly assessed diagnosis with versus without AI assistance

### Findings relevant to the review question
The retrieved findings clearly indicate that AI assistance was intended to augment clinician performance in real-world diagnosis of suspected skin neoplasms. However, the findings available here did **not** provide extracted numeric sensitivity and specificity values in the research record supplied for synthesis.

### Sensitivity and specificity
- **Numeric sensitivity and specificity values were not available in the extracted findings provided here**
- Because those outcome numbers were not present in the accessible corpus text used for this report, this study also could not contribute extractable sensitivity/specificity estimates for meta-analysis

## Synthesis of Findings on Sensitivity and Specificity

## Main result

The local MetaSyn PubMed corpus retrieval identified **three eligible primary studies** showing that deep learning–based AI assistance can improve clinician diagnostic performance for skin cancer or suspicious skin neoplasms compared with clinician diagnosis without AI support [1][2][3]. However, the available local-corpus evidence was **insufficient to extract paired sensitivity and specificity data** required for a quantitative meta-analysis.

## What the included studies do show

Across the three included studies:

- AI assistance was used as a **decision-support tool**, not merely as a stand-alone comparator
- The task involved diagnosis from **skin lesion images** or a **real-world clinical workflow**
- The direction of effect was generally favorable:
  - improved diagnostic accuracy [1][2][3]
  - greater benefit among less experienced clinicians [1]
  - improved inter-rater concordance [2]

## What the included studies do not provide, based on available local corpus text

For the specific review outcomes of **sensitivity** and **specificity**:
- [Human-computer collaboration for skin cancer recognition](local://corpus/2299) [1]: no numeric sensitivity/specificity available
- [Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks](local://corpus/2580) [2]: no numeric sensitivity/specificity available
- [Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study](local://corpus/2582) [3]: no numeric sensitivity/specificity available in the extracted record used here

## Implications for meta-analysis

A formal meta-analysis of sensitivity and specificity requires study-level 2×2 data or reported sensitivity/specificity for:
- clinicians without AI
- clinicians with AI
- ideally under the same test set or comparable design

Those data were not recoverable from the local corpus content available for this review. As a result:

- **A quantitative meta-analysis of sensitivity and specificity could not be completed**
- The evidence supports a **qualitative conclusion only**

## Retrieval and Screening Summary

### PRISMA-style narrative summary

**Records identified from local corpus searching:** 8 candidate records  
**Records screened:** 8  
**Records excluded:** 5  
**Studies included in qualitative synthesis:** 3  
**Studies included in quantitative meta-analysis:** 0

### Reasons for exclusion at screening
- Review/systematic review article: 1
- No confirmed clinician-with-AI versus clinician-without-AI comparison from retrieved corpus text: multiple records
- Insufficient retrieved local-corpus detail to confirm eligibility or outcome extractability: multiple records
- Apparent focus on AI-alone performance rather than assisted clinician comparison: at least 1 record

## Interpretation

## Overall direction of evidence

Within the local MetaSyn PubMed corpus and date range searched, the eligible evidence points in a consistent direction: **deep learning–based AI assistance tends to improve clinician diagnostic performance for skin cancer detection tasks**, especially in image-based assessment and among less experienced clinicians [1][2][3].

## Why the answer remains incomplete for the target outcomes

The review question was specifically about **sensitivity and specificity**. The main limitation of the evidence base as retrieved from the local corpus is not only the small number of eligible studies, but also the lack of accessible outcome detail. Two of the three included studies were **abstract-only**, and even the full-text-accessible study did not provide extractable sensitivity/specificity figures in the findings available for this report [1][2][3].

As a result, the review can answer:
- **Does AI assistance appear to improve clinician diagnostic performance?**  
  **Yes, directionally, in the included studies.**

But it cannot answer with precision:
- **By how much does AI assistance change sensitivity?**
- **By how much does AI assistance change specificity?**

## Limitations

### Limitations of the evidence base
- Only **three eligible primary studies** were identified
- Two included studies were **abstract-only** in the local corpus [1][2]
- Included studies were heterogeneous in:
  - lesion types
  - clinician expertise
  - study setting
  - task format
  - comparator structure

### Limitations for the target outcomes
- Numeric **sensitivity and specificity** were not available from the accessible local corpus content
- No study-level 2×2 data were available for quantitative pooling
- Reported outcomes often emphasized **accuracy** rather than sensitivity/specificity

### Retrieval-related limitations
- The review was restricted to the **local MetaSyn PubMed corpus only**
- No external retrieval or full-text supplementation was allowed
- Some potentially relevant records could not be confidently included because eligibility-critical details were not recoverable from the accessible corpus text

### Risk of incomplete classification
- Some excluded records had potentially relevant titles, especially Corpus IDs **114506** and **114484**, but the available retrieved text was not sufficient here to verify eligibility and extract the required outcomes with confidence [6][7]

## Conclusion

Using only the local MetaSyn PubMed corpus and the specified date range, the evidence indicates that **deep learning–based AI assistance generally improves clinicians’ skin cancer diagnostic performance compared with clinician diagnosis without AI assistance** [1][2][3]. This favorable direction is supported by improved overall diagnostic accuracy and, in one study, improved agreement among clinicians [2].

However, the review question specifically targeted **sensitivity and specificity**, and the available local-corpus records did **not** provide sufficient numeric sensitivity/specificity data to support a formal meta-analysis. Therefore, the evidence supports a **qualitative conclusion of likely benefit**, but not a pooled quantitative estimate for sensitivity or specificity.

## Included-Study List

1. **Human-computer collaboration for skin cancer recognition** — **Corpus ID 2299**  
2. **Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks** — **Corpus ID 2580**  
3. **Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study** — **Corpus ID 2582**

### Sources

[1] Human-computer collaboration for skin cancer recognition: local://corpus/2299  
[2] Augmented decision-making for acral lentiginous melanoma detection using deep convolutional neural networks: local://corpus/2580  
[3] Augmenting the accuracy of trainee doctors in diagnosing skin lesions suspected of skin neoplasms in a real-world setting: A prospective controlled before-and-after study: local://corpus/2582  
[4] Skin cancer classification via convolutional neural networks: systematic review of studies involving human experts: local://corpus/114492  
[5] Artificial intelligence for melanoma diagnosis: local://corpus/35140  
[6] Evaluation of Artificial Intelligence-Assisted Diagnosis of Skin Neoplasms: A Single-Center, Paralleled, Unmasked, Randomized Controlled Trial: local://corpus/114506  
[7] Diagnostic performance of augmented intelligence with 2D and 3D total body photography and convolutional neural networks in a high-risk population for melanoma under real-world conditions: A new era of skin cancer screening?: local://corpus/114484  
[8] Performance of a deep neural network in teledermatology: a single-centre prospective diagnostic study: local://corpus/2581