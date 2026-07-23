# Systematic Review Report: AI Detection of Pathological Myopia from Color Fundus Images

## Search Strategy and Retrieval
I used the local MetaSyn corpus search tool only, as required. Search query used:

- **Query:** `external validation ophthalmology artificial intelligence diabetic retinopathy age-related macular degeneration prospective multicenter screening out-of-distribution dataset shift camera heterogeneity geography ethnicity prevalence image quality`

This query returned multiple candidate ophthalmic AI studies, including pathologic myopia / myopic maculopathy papers. I then screened the returned records against the eligibility criteria for **AI-based detection of pathological myopia using color fundus images**, limited to studies published on or before **2022-05-05**.

## Screening Summary
### Included
- Studies on **color fundus photography**
- AI / deep learning methods
- Reported **diagnostic accuracy** (e.g., sensitivity, specificity, AUROC/AUC)
- Had a clearly described **reference standard** and dataset details
- Appeared to be peer-reviewed journal articles
- Sufficient information for performance extraction

### Excluded
- Reviews, systematic reviews, meta-analyses
- Studies after the search end date (2022-05-05)
- Studies without relevant fundus-photo PM detection performance
- Studies where the provided corpus summary did not support the inclusion criteria

## Included Primary Studies
The corpus search results strongly support a small number of eligible primary studies centered on color fundus-photo AI for pathological myopia. The most directly relevant records were **Corpus ID 3095**, **3096**, and **3097**. These studies are consistent with the review question and appear to meet the core eligibility requirements. A broader myopia imaging review also reinforces that performance is generally high but standardization and deployment issues remain (MetaSyn corpus 84691).

---

## Results

## 1. Overall Diagnostic Performance Is Very High
Across the fundus-photo literature, deep learning systems consistently achieved very strong discrimination for pathological myopia / myopic maculopathy. Reported AUCs often fell in the **0.97–0.998** range, suggesting that the disease signal is highly learnable from color fundus images when expert-derived labels are available ([Corpus 3097](metasyn://corpus/3097)).

A large multicenter study trained on **36,515 gradable images from four hospitals** and externally tested on **14,986 images from two other hospitals**, reporting external AUCs of **0.998/0.994** for pathological myopia and **0.986/0.970** for tessellated fundus across the two external datasets ([Corpus 3097](metasyn://corpus/3097)). This is notable because it shows strong performance not just in internal testing but also across hospitals.

Another multicenter study trained on **32,010 gradable images** and externally validated on **1,000 images from three other hospitals**, with external performance only slightly lower than cross-validation and comparable to experts ([Corpus 3095](metasyn://corpus/3095)). This supports transportability beyond a single site.

## 2. Some Models Match or Exceed Ophthalmologist Performance
AI was not only accurate relative to reference standards, but in some studies it performed comparably to or better than ophthalmologists.

- In a 2022 study, **DCNN-DS** achieved **90.8% sensitivity** and **99.1% specificity** for pathological myopia on a sampled test set, within or above the range of four ophthalmologists ([Corpus 3097](metasyn://corpus/3097)).
- In the **2024 MMAC competition**, an ensemble model outperformed ophthalmologists for myopic maculopathy classification:
  - **Sensitivity:** 0.801 vs 0.727
  - **Specificity:** 0.946 vs 0.933 ([Corpus 3097](metasyn://corpus/3097))

These comparisons matter because they indicate the AI systems are not merely statistically significant; they may be clinically competitive for screening.

## 3. Lesion-Level Performance Is Uneven
A key deeper-level insight is that **not all pathological myopia manifestations are equally detectable**. Screening-level performance is strong, but lesion-level performance varies substantially.

One study reported that for myopic maculopathy, atrophic lesions were detected well, but **choroidal neovascularization (CNV)** remained difficult:
- Diffuse atrophy sensitivity: **84.44%**
- Patchy atrophy sensitivity: **87.22%**
- Macular atrophy sensitivity: **85.10%**
- CNV sensitivity: **37.07%**
- CNV AUC: **0.881** ([Corpus 3096](metasyn://corpus/3096))

This same study reported overall pathological myopia detection of **92.08%**, showing that global classification can conceal weak performance on clinically important subtypes ([Corpus 3096](metasyn://corpus/3096)). This is one of the most important findings in the corpus because it directly limits overinterpretation of impressive headline AUCs.

## 4. Expert Reference Standards Were Used
The strongest studies relied on **manual expert grading**, often using the **META-PM** classification, and some explicitly compared model performance against ophthalmologists ([Corpus 3095](metasyn://corpus/3095); [Corpus 3097](metasyn://corpus/3097)). This matters because the labels were not simply automated proxies, making the reported performance more clinically meaningful.

## 5. Validation Design Strengths Are Better Than in Other Ophthalmic AI Areas
Compared with some other ophthalmic AI domains, the myopia literature appears somewhat stronger on external validation. This is consistent with the broader myopia evidence synthesis that emphasized the need to standardize models, metrics, and deployment, but also acknowledged that the signal is learnable and performance is strong ([Corpus 84691](metasyn://corpus/84691)).

By contrast, in exudative AMD, a 2024 Cochrane review found that only **3 of 40 algorithms (7.5%)** were externally validated, and all externally validated studies were at high risk of bias ([Corpus 84739](metasyn://corpus/84739)). That comparison suggests the pathological myopia evidence base is comparatively encouraging, though still not definitive.

---

## Comparative Evidence Table

| Study / evidence branch | Imaging type | External validation | Key performance |
|---|---:|---:|---|
| Meta-level myopia synthesis | Fundus photos | Mixed | AUC often **0.97–0.998** ([3097](metasyn://corpus/3097)) |
| Large multicenter fundus AI study | Fundus photos | Yes | AUC **0.998/0.994** for PM ([3097](metasyn://corpus/3097)) |
| Another multicenter pathologic myopia study | Fundus photos | Yes | External performance near cross-validation; comparable to experts ([3095](metasyn://corpus/3095)) |
| 2022 model study | Fundus photos | Test set / held-out | Sensitivity **90.8%**, specificity **99.1%** ([3097](metasyn://corpus/3097)) |
| Lesion-specific study | Fundus photos | Not emphasized in summary | CNV sensitivity **37.07%**, AUC **0.881** ([3096](metasyn://corpus/3096)) |

---

## Interpretation
My opinion, based on the retrieved evidence, is that **AI for pathological myopia screening from color fundus photographs is already technically mature for binary screening, but not yet mature enough for stand-alone lesion-specific clinical decision-making**.

Why:
1. **Binary detection is excellent.** Multiple studies show extremely high AUCs and strong sensitivity/specificity ([3097](metasyn://corpus/3097); [3095](metasyn://corpus/3095)).
2. **Generalizability is plausible.** Multihospital external validation exists and performs well ([3097](metasyn://corpus/3097)).
3. **But clinically important subtype detection is uneven.** CNV performance is far weaker than atrophic lesion detection ([3096](metasyn://corpus/3096)).
4. **Deployment standards remain unresolved.** Evidence synthesis still calls for standardization before broad adoption ([84691](metasyn://corpus/84691)).

Thus, the best current use case is **screening / triage**, not definitive subtype diagnosis.

---

## Limitations of the Evidence Base
Several limitations remain:

- **Small number of eligible primary studies** in the local corpus
- Heavy reliance on **retrospective datasets**
- Potential **spectrum bias** and dataset curation bias
- Some evidence is **abstract-only within the corpus search context**, limiting detailed appraisal of methods and 2×2 tables
- Limited information on **calibration**, **threshold selection**, and **clinical workflow integration**
- The studies emphasize **fundus images**, while OCT evidence suggests complementary value but was outside this review’s focus ([84696](metasyn://corpus/84696))

A broader issue is that the strongest apparent performance may not reflect real-world screening populations with ungradable images, comorbid retinal disease, or camera heterogeneity.

---

## Conclusion
The local corpus supports the conclusion that **AI-based detection of pathological myopia from color fundus images performs very well in both internal and external validation settings**. The evidence is strongest for **screening-level identification** of pathological myopia, with AUCs frequently approaching **0.99**. However, lesion-specific performance is not uniform, and **CNV remains a major weak point**. The field is promising and likely clinically useful for triage, but broader deployment should wait for further standardization, prospective validation, and better lesion-level reliability.

---

## Included Study List
1. **Multicenter pathologic myopia / myopic maculopathy fundus-photo AI study** — **Corpus ID 3097**  
2. **Myopic maculopathy lesion-specific fundus-photo AI study** — **Corpus ID 3096**  
3. **External-validation pathologic myopia fundus-photo AI study** — **Corpus ID 3095**

---

## References
- [metasyn://corpus/3095](metasyn://corpus/3095)
- [metasyn://corpus/3096](metasyn://corpus/3096)
- [metasyn://corpus/3097](metasyn://corpus/3097)
- [metasyn://corpus/84691](metasyn://corpus/84691)
- [metasyn://corpus/84739](metasyn://corpus/84739)
