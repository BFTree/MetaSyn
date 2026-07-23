# Evidence‑Synthesis Report  
**Diagnostic accuracy of artificial intelligence for pathological myopia detection on colour fundus images**

## 1. Background and Review Question  
This systematic review assessed the diagnostic accuracy of artificial intelligence (AI)-based methods—particularly deep learning—for detecting pathological myopia (PM) from colour fundus photographs. The target condition was PM as defined by expert clinical diagnosis or a recognised reference standard (e.g., the META‑PM classification). Performance was to be measured by sensitivity, specificity, area under the summary receiver operator curve (SROC), and diagnostic odds ratio (DOR).

## 2. Methods  
### 2.1 Search and Candidate Pool  
A fixed candidate pool of 200 records (the “source‑review‑disjoint top‑200”) was supplied. No additional searches were conducted. The search end date was **5 May 2022**; therefore, any record published after that date was excluded. Only English‑language, peer‑reviewed primary studies were eligible.

### 2.2 Inclusion and Exclusion Criteria  
**Inclusion criteria**  
- Evaluated machine‑learning or AI algorithms for the detection of PM.  
- Used colour fundus images.  
- Reported performance indices suitable for a meta‑analysis of diagnostic accuracy (e.g., area under the receiver‑operator curve [AUROC], sensitivity, specificity).  
- Provided information on the dataset size and the reference standard.  
- Included a validation set that was at least 10% of the size of the training set.  

**Exclusion criteria**  
- Reviews, editorials, protocols, conference abstracts.  
- Studies that did not focus on PM detection.  
- Studies using imaging modalities other than colour fundus photography (e.g., OCT, OCTA, anterior‑segment OCT).  
- Studies that did not report sensitivity and specificity for PM detection.  
- Articles published after 5 May 2022 (the search end date).  

### 2.3 Screening  
Titles and abstracts of all 200 candidates were screened against the above criteria. Full texts were not available; screening relied solely on the supplied abstracts.

## 3. Results of Screening  
The screening process eliminated the vast majority of records for the following reasons:  
- **Publication date**: 143 candidates had publication years of 2022 (without month information) or later and were excluded, because they could not be confirmed to have been published before the May 2022 cut‑off.  
- **Not PM detection**: Many studies addressed other ocular diseases (glaucoma, diabetic retinopathy, age‑related macular degeneration, keratoconus, etc.) or general multi‑disease classification without specific PM performance metrics.  
- **Wrong imaging modality**: Several candidates used OCT, OCT‑angiography, fluorescein angiography, or anterior‑segment imaging rather than colour fundus photographs.  
- **Insufficient diagnostic accuracy data**: Some PM‑related papers reported only AUROC or lesion‑level sensitivity/specificity without providing overall sensitivity and specificity for PM detection, rendering them unsuitable for the required meta‑analytic framework.  

After applying all criteria, **one primary study** was eligible for inclusion.

## 4. Characteristics of the Included Study  

**Candidate 002**  
*Title*: **AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and “Plus” Lesion Detection in Fundus Images**  
*Corpus ID*: 3095  
*Publication year*: 2021  

### 4.1 Study Design and Population  
- Retrospective development and external validation study.  
- Training dataset: 32,010 colour fundus images manually graded according to the META‑PM classification.  
- External validation set: 1,000 images from three other hospitals.  
- The reference standard was expert manual grading.

### 4.2 AI Intervention  
- A series of deep learning algorithms (algorithm I, II, III) were developed.  
- Algorithm I provided a binary PM/no‑PM classification; algorithm II performed multi‑class myopic maculopathy grading; algorithm III detected “plus” lesions.  
- Performance was evaluated using five‑fold cross‑validation, ensuring that the validation set in each fold was ≥20% of the training data, satisfying the ≥10% requirement.

### 4.3 Diagnostic Accuracy  
For **algorithm I** (detection of PM):  
- Sensitivity: 93.92% (95% CI, 93.33–94.51)  
- Specificity: 98.19% (95% CI, 97.87–98.52)  
- Area under the receiver operating characteristic curve (AUC): 0.995 (95% CI, 0.9933–0.9967)  
- Accuracy: 97.36%  

The external validation performance was slightly inferior to the cross‑validation results but was comparable to experts.

## 5. Synthesis and Discussion  
Only a single study fulfilled all eligibility criteria. The included study demonstrated very high sensitivity and specificity for PM detection using a deep learning system trained on a large, manually graded dataset. The five‑fold cross‑validation and external validation suggest robustness; however, the evidence base is limited to one investigation. Several potentially relevant studies were excluded because they did not report the necessary sensitivity and specificity for PM, used imaging modalities other than colour fundus photography, or were published after the search end date.

The small number of eligible studies precludes a quantitative meta‑analysis. The high reported accuracy must be interpreted cautiously; no independent replication was available within the eligible pool, and no study provided a direct comparison with a clinical reference standard in a fully independent prospective cohort (the external validation set was retrospective). Future updates to this review should incorporate studies published after May 2022 that meet the inclusion criteria and, ideally, include prospective validation in screening populations.

## 6. Included Primary Study  
The following article was included in the evidence synthesis:

- **AI-Model for Identifying Pathologic Myopia Based on Deep Learning Algorithms of Myopic Maculopathy Classification and “Plus” Lesion Detection in Fundus Images**  
  *Corpus ID: 3095*  

No other candidate met the full set of inclusion criteria.
