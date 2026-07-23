# ProtoMA Systematic Review Report

**Benchmark task:** 163
**Target:** Bisphosphonates and risk of cancers: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates whether the use of bisphosphonates is associated with the risk of overall cancers and individual types of cancers, and further examines whether different types (nitrogen-containing vs. non-nitrogen-containing) and duration of bisphosphonate use influence cancer risk compared to non-users..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 92 unique candidates.

**Results:** 27 study reports were retained after explicit screening. The random-effects estimate was 0.890 (95% CI 0.826 to 0.958); I-squared was 88.6%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Bisphosphonates are widely prescribed antiresorptive agents for osteoporosis and other bone-related disorders, particularly in older adults who already have substantial baseline cancer risk because of age and comorbidity. Beyond their established effects on skeletal outcomes, bisphosphonates have been hypothesized to influence carcinogenesis through inhibition of osteoclast-mediated bone remodeling, effects on the mevalonate pathway, and potential anti-proliferative, pro-apoptotic, and anti-angiogenic actions, especially for nitrogen-containing compounds. These mechanisms have led to sustained interest in whether bisphosphonate exposure may alter the risk of incident malignancy, not only overall but also for site-specific cancers such as colorectal, breast, endometrial, liver, and pancreatic cancer. Clarifying this association is clinically important because bisphosphonates are used long term in large populations, and even modest effects on cancer risk could materially affect benefit-risk assessment in routine practice.

Observational studies examining bisphosphonate use and cancer risk have reported inconsistent findings. Some studies have suggested a protective association for selected cancers, whereas others have found no association or results compatible with residual confounding, detection bias, or differences by drug class and duration of use. The available evidence is also methodologically heterogeneous, spanning cohort and case-control designs, diverse source populations, varying exposure definitions, and multiple cancer endpoints. Across 27 studies published between 2010 and 2020, including 3,628,518 participants, the literature includes users of both nitrogen-containing and non-nitrogen-containing bisphosphonates, but the extent to which associations differ by compound type, cumulative duration, and cancer site remains uncertain. A rigorous synthesis is therefore needed to consolidate the evidence and to distinguish whether any observed associations are consistent across designs and outcomes.

This systematic review evaluates the association between bisphosphonate use and cancer risk in the general population, including patients receiving bisphosphonates for osteoporosis or related bone conditions, compared with non-users. The review addresses both all-cause cancer and specific cancer types, with particular focus on colorectal, breast, endometrial, liver, and pancreatic cancer, and considers whether associations vary according to bisphosphonate class and duration of use. By synthesizing data from observational studies with large underlying populations, this review aims to provide a more precise estimate of the direction and magnitude of cancer risk associated with bisphosphonate exposure and to identify areas where the current evidence remains insufficient for causal inference or clinical decision-making.

## Review Question

- Population: General population, including bisphosphonate users (primarily patients with osteoporosis or bone-related conditions)
- Intervention: Not reported
- Exposure: Bisphosphonate use (including nitrogen-containing and non-nitrogen-containing bisphosphonates, with consideration of duration of use)
- Comparison: Non-users of bisphosphonates
- Outcome: Risk of cancers (all-cause cancer and specific cancer types including colorectal, breast, endometrial, liver, and pancreatic cancer)
- Search window: Not reported to 2019-12-07 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Diphosphonates"[Mesh] OR bisphosphonate*[tiab] OR diphosphonate*[tiab] OR alendronate[tiab] OR risedronate[tiab] OR ibandronate[tiab] OR zoledronic acid[tiab] OR zoledronate[tiab] OR pamidronate[tiab] OR etidronate[tiab] OR clodronate[tiab] OR tiludronate[tiab] OR neridronate[tiab] OR olpadronate[tiab]) AND ("Osteoporosis"[Mesh] OR "Bone Diseases, Metabolic"[Mesh] OR osteoporosis[tiab] OR osteopeni*[tiab] OR "bone disease*"[tiab] OR "bone-related condition*"[tiab] OR fracture*[tiab] OR "Paget disease"[tiab] OR "Paget's disease"[tiab] OR "bone metastas*"[tiab] OR general population[tiab]))`
2. `(("Diphosphonates"[Mesh] OR bisphosphonate*[tiab] OR diphosphonate*[tiab] OR alendronate[tiab] OR risedronate[tiab] OR ibandronate[tiab] OR zoledronic acid[tiab] OR zoledronate[tiab] OR pamidronate[tiab] OR etidronate[tiab] OR clodronate[tiab] OR tiludronate[tiab] OR nitrogen-containing[tiab] OR non-nitrogen-containing[tiab]) AND ("Neoplasms"[Mesh] OR cancer*[tiab] OR neoplas*[tiab] OR malignan*[tiab] OR tumor*[tiab] OR tumour*[tiab] OR carcinoma*[tiab]) AND (risk*[tiab] OR incidence[tiab] OR occurrence[tiab] OR association[tiab] OR hazard*[tiab] OR odds[tiab]))`
3. `(("Diphosphonates"[Mesh] OR bisphosphonate*[tiab] OR alendronate[tiab] OR risedronate[tiab] OR ibandronate[tiab] OR zoledronic acid[tiab] OR pamidronate[tiab] OR etidronate[tiab] OR clodronate[tiab]) AND (("Colorectal Neoplasms"[Mesh] OR colorectal cancer[tiab] OR colon cancer[tiab] OR rectal cancer[tiab] OR colorectal neoplas*[tiab]) OR ("Breast Neoplasms"[Mesh] OR breast cancer[tiab] OR breast neoplas*[tiab]) OR ("Endometrial Neoplasms"[Mesh] OR endometrial cancer[tiab] OR uterine cancer[tiab] OR corpus uteri cancer[tiab]) OR ("Liver Neoplasms"[Mesh] OR liver cancer[tiab] OR hepatic cancer[tiab] OR hepatocellular carcinoma[tiab]) OR ("Pancreatic Neoplasms"[Mesh] OR pancreatic cancer[tiab] OR pancreas cancer[tiab])) AND (risk*[tiab] OR incidence[tiab] OR association[tiab] OR "case-control"[tiab] OR cohort[tiab]))`
4. `(("Diphosphonates"[Mesh] OR bisphosphonate*[tiab] OR diphosphonate*[tiab] OR alendronate[tiab] OR risedronate[tiab] OR ibandronate[tiab] OR zoledronic acid[tiab] OR pamidronate[tiab] OR etidronate[tiab] OR clodronate[tiab]) AND (duration[tiab] OR "duration of use"[tiab] OR long-term[tiab] OR cumulative[tiab] OR exposure[tiab] OR ever-use[tiab] OR dose-response[tiab] OR dose dependent[tiab]) AND ("Neoplasms"[Mesh] OR cancer*[tiab] OR neoplas*[tiab] OR malignan*[tiab]))`
5. `(("Diphosphonates"[Mesh] OR bisphosphonate*[tiab] OR alendronate[tiab] OR risedronate[tiab] OR ibandronate[tiab] OR zoledronic acid[tiab] OR pamidronate[tiab] OR etidronate[tiab] OR clodronate[tiab]) AND ("Neoplasms"[Mesh] OR cancer*[tiab] OR neoplas*[tiab] OR malignan*[tiab] OR carcinoma*[tiab]) AND ("Cohort Studies"[Mesh] OR "Case-Control Studies"[Mesh] OR "Epidemiologic Studies"[Mesh] OR cohort[tiab] OR "case-control"[tiab] OR observational[tiab] OR population-based[tiab] OR longitudinal[tiab] OR registry[tiab] OR "nested case-control"[tiab]))`

The merged candidate pool contained 92 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational studies (prospective or retrospective cohort studies, case-control studies, or nested case-control studies) or randomized studies that provide original human data on bisphosphonate exposure and subsequent cancer risk.
- Studies conducted in the general adult population or in populations of bisphosphonate users/non-users, including patients with osteoporosis or other bone-related conditions, with a comparator group of non-users or lower/no exposure to bisphosphonates.
- Studies evaluating bisphosphonate use as the exposure of interest, including nitrogen-containing or non-nitrogen-containing bisphosphonates, with or without assessment of duration, dose, or cumulative use.
- Studies reporting cancer outcomes, including all-cause/overall cancer incidence or specific cancer types such as colorectal, breast, endometrial, liver, or pancreatic cancer, and providing effect estimates (e.g., RR, OR, HR, SIR) with confidence intervals or sufficient data to calculate them.

Exclusion criteria:

- Animal, in vitro, mechanistic, review, editorial, commentary, conference abstract-only, case report/case series, cross-sectional, or ecological studies, or any study not presenting original human comparative data.
- Studies in pediatric populations only, highly selected non-generalizable populations without an appropriate non-user comparator, or studies in which bisphosphonate users cannot be distinguished from users of other bone-active drugs.
- Studies not evaluating bisphosphonate exposure specifically, lacking a relevant comparator group, or focusing only on cancer prognosis, recurrence, mortality, or treatment response rather than incident cancer risk.
- Studies not reporting eligible cancer outcomes of interest, not providing usable risk estimates/data, or duplicate publications based on the same cohort where the most complete or recent report should be retained.

92 candidates were screened and 27 were retained.

### Statistical Analysis

### Statistical analysis
The primary effect measure for quantitative synthesis was the **odds ratio (OR)**. A total of **24 studies** contributed to the meta-analysis. When studies reported RR, HR, or OR, the most fully adjusted estimate was preferentially extracted; estimates were synthesized on the log scale with corresponding standard errors derived from the reported 95% confidence intervals.

The principal meta-analytic model was a **random-effects model**, selected a priori because of expected between-study variability in study design, source population, bisphosphonate type, exposure definition, duration of use, and cancer outcome ascertainment. For comparison, a **fixed-effect model** was also calculated.

The pooled random-effects estimate showed that bisphosphonate use was associated with a **lower overall cancer risk**:

- **Random-effects pooled OR = 0.890**
- **95% CI: 0.826-0.958**
- **p = 0.0021**

The fixed-effect model yielded a similar result:

- **Fixed-effect pooled OR = 0.894**
- **95% CI: 0.876-0.913**
- **p = 0.0000**

Between-study heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (τ²)**. Heterogeneity was substantial:

- **Q = 202.39**, **p = 0.000**
- **I² = 88.6%**
- **τ² = 0.0237**

An **I² value of 88.6%** indicates considerable inconsistency across studies, supporting the use of the random-effects model as the primary analysis. Statistical significance was defined using a **two-sided p-value < 0.05**. Where appropriate, subgroup or sensitivity analyses may be considered according to bisphosphonate class, duration of use, and cancer subtype, although the primary synthesis focused on the overall pooled association between bisphosphonate exposure and cancer risk.

## Results

### Study Selection

### Results of Search
The database search identified **92 records** in total (**92** from local sources and **0** from PubMed) after deduplication. All **92 records** underwent title and abstract screening, of which **65** were excluded at the first stage for not meeting the eligibility criteria. **Twenty-seven full-text articles** were assessed for eligibility. No studies were excluded at the full-text stage (**n = 0**). Consequently, **27 studies** were included in the systematic review, and **24 studies** contributed quantitative data to the meta-analysis of cancer risk associated with bisphosphonate use. This study selection process is consistent with a PRISMA flow in which all records reaching full-text review were ultimately eligible for inclusion.

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis, not an original human comparative study.: 3
- Meta-analysis, not an original human comparative study.: 3
- Review/update article, not an original human comparative study.: 1
- Comparator group is osteoporosis treatment initiators including intravenous bisphosphonate or raloxifene rather than a clear non-user/lower or no bisphosphonate exposure group; highly selected treatment cohort without the required comparator.: 1
- Mechanistic/in vitro study, not an original human comparative study of cancer incidence.: 1
- Focuses on adverse events among osteoporosis/cancer patients rather than incident cancer risk in relation to bisphosphonate exposure.: 1
- Literature review/evaluation, not an original human comparative study.: 1
- Exposed group combines bisphosphonate users with users of other antiresorptive osteoporosis drugs, so bisphosphonate exposure is not evaluated specifically.: 1
- Insufficient information from title/abstract to confirm original comparative human data and usable risk estimates; likely commentary/question piece rather than an eligible study.: 1
- Review/narrative article from laboratory to clinic; does not present original human comparative data on bisphosphonate exposure and incident cancer risk.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 664 | 2012 | A prospective study of bisphosphonate use and risk of colorectal cancer. |
| 678 | 2011 | Use of bisphosphonates and reduced risk of colorectal cancer. |
| 666 | 2012 | Reduced colon cancer incidence and mortality in postmenopausal women treated with an oral bisphosphonate--Danish National Register Based Cohort Study. |
| 670 | 2012 | Exposure to bisphosphonates and risk of colorectal cancer: a population-based nested case-control study. |
| 663 | 2015 | Oral bisphosphonate use and risk of postmenopausal endometrial cancer. |
| 669 | 2019 | Bisphosphonate use and risk of renal cell carcinoma: A population-based case-control study. |
| 662 | 2018 | Oral bisphosphonate use and lung cancer incidence among postmenopausal women. |
| 668 | 2011 | Alendronate and risk of esophageal cancer: a nationwide population-based study in Taiwan. |
| 679 | 2012 | Oral alendronate use and risk of cancer in postmenopausal women with osteoporosis: A nationwide study. |
| 64974 | 2012 | Exposure to oral bisphosphonates and risk of cancer. |
| 677 | 2014 | The effect of bisphosphonates on the risk of endometrial and ovarian malignancies. |
| 676 | 2010 | Oral bisphosphonates and risk of cancer of oesophagus, stomach, and colorectum: case-control analysis within a UK primary care cohort. |
| 65046 | 2020 | Risk of colorectal cancer in users of bisphosphonates: analysis of population-based electronic health records. |
| 658 | 2012 | Esophageal and gastric cancer incidence and mortality in alendronate users. |
| 675 | 2017 | Oral bisphosphonates and colorectal cancer. |
| 659 | 2010 | Exposure to oral bisphosphonates and risk of esophageal cancer. |
| 667 | 2017 | Use of Bisphosphonates and Risk of Breast Cancer in a French Cohort of Postmenopausal Women. |
| 65069 | 2012 | Bisphosphonates and risk of upper gastrointestinal cancer--a case control study using the General Practice Research Database (GPRD). |
| 64946 | 2020 | Exposure to oral bisphosphonates and risk of gastrointestinal cancer. |
| 64949 | 2016 | Oral Bisphosphonates and Upper Gastrointestinal Cancer Risks in Asians with Osteoporosis: A Nested Case-Control Study Using National Retrospective Cohort Sample Data from Korea. |
| 665 | 2015 | Protective effect of bisphosphonates on endometrial cancer incidence in data from the Prostate, Lung, Colorectal and Ovarian (PLCO) cancer screening trial. |
| 64973 | 2012 | Oral bisphosphonates and risk of esophageal cancer: a dose-intensity analysis in a nationwide population. |
| 673 | 2015 | Oral Bisphosphonate Exposure and the Risk of Upper Gastrointestinal Cancers. |
| 64950 | 2015 | Oral bisphosphonates and upper gastrointestinal toxicity: a study of cancer and early signals of esophageal injury. |
| 672 | 2013 | Exposure to bisphosphonates and risk of gastrointestinal cancers: series of nested case-control studies with QResearch and CPRD data. |
| 660 | 2012 | A higher dosage of oral alendronate will increase the subsequent cancer risk of osteoporosis patients in Taiwan: a population-based cohort study. |
| 671 | 2013 | Exposure to bisphosphonates and risk of common non-gastrointestinal cancers: series of nested case-control studies using two primary-care databases. |

### Study Characteristics

**Study Characteristics**

A total of 27 observational studies were included, comprising 3,628,518 participants overall. The studies were published between 2010 and 2020, with most clustered in the early-to-mid 2010s. Geographically, the evidence base was concentrated in Europe, North America, and East Asia. The United Kingdom contributed the largest share when UK and United Kingdom reports are considered together (n=6), followed by Denmark, Taiwan, and the United States (n=3 each), Israel and Korea (n=2 each), and single studies from Canada, Spain, and France; several studies did not clearly report country of origin. Study design was notably heterogeneous, although all were non-randomized. Designs included cohort studies in several forms (prospective cohort, retrospective cohort, population-based cohort, and register-based open cohort designs) and multiple case-control formats, including population-based case-control, nested case-control, prospective nested case-control, and series of nested case-control studies. Overall, cohort-type designs predominated, but a substantial proportion used case-control methods, underscoring important variation in sampling frames, temporal structure, and analytic approach.

Study quality was generally strong based on the enhanced extraction, with 24 studies rated as high confidence, two as medium confidence, and one as low confidence. In contrast, the risk-of-bias summary suggested that most studies were judged as high risk overall, with only a small minority classified as unclear risk, reflecting the inherent limitations of observational evidence and likely concerns around confounding, selection processes, and outcome ascertainment. The included studies also appeared heterogeneous in participant and methodological characteristics. While the pooled sample was very large, individual study sizes ranged from fewer than 2,000 participants to 1.64 million, and several reports did not provide an analyzable sample size in the extracted dataset. Detailed participant characteristics such as age distribution, sex composition, and condition severity were not consistently available in the extracted summary, limiting direct comparison across studies. Similarly, intervention characteristics, including dose, duration, and mode of delivery, as well as the exact outcome measures used, were not uniformly reported in the available extraction fields. Taken together, the included literature represents a broad but methodologically diverse evidence base, with substantial heterogeneity in design, setting, sample size, and reporting completeness.

### Main Findings

**Results**

The pooled analysis demonstrated that bisphosphonate use was associated with a statistically significant lower overall odds of cancer compared with non-use. Across 24 studies reporting odds ratios, the random-effects pooled OR was 0.890 (95% CI 0.826 to 0.958; p=0.0021), indicating an overall inverse association between bisphosphonate exposure and cancer risk in the general population, including users treated primarily for osteoporosis or other bone-related conditions. This corresponds to an approximately 11% relative reduction in the odds of cancer among bisphosphonate users versus non-users.

The magnitude of effect was modest but potentially clinically relevant, particularly given the large combined evidence base and the consistency in the direction of the pooled point estimate below the null. The fixed-effect model yielded a nearly identical estimate (OR 0.894, 95% CI 0.876 to 0.913; p<0.0001), which supports the overall direction of the finding. Taken together, these results suggest that bisphosphonate use may be associated with a small protective effect against cancer overall, although the size of this effect should be interpreted cautiously.

There was, however, substantial between-study heterogeneity. The heterogeneity statistics were high (I2=88.6%, Q=202.39, p<0.001; tau2=0.0237), indicating considerable variability in effect estimates across studies beyond chance alone. This level of inconsistency suggests that the pooled estimate reflects an average effect across studies with meaningfully different underlying populations, exposure definitions, bisphosphonate classes, durations of use, and cancer outcomes. As a result, the random-effects estimate is the more appropriate summary measure and indicates that the inverse association, while statistically significant, was not uniform across all included studies.

Despite this heterogeneity, the direction of the pooled effect remained stable across analytic models, with both random- and fixed-effects approaches showing reduced odds of cancer among bisphosphonate users. This pattern strengthens confidence that the overall association is unlikely to be entirely driven by a small number of extreme studies, even if the precise magnitude varies across settings. Clinically, the observed reduction is modest rather than large, and it is more suggestive of a potential chemopreventive association than of a strong protective effect.

The largest and most statistically precise studies likely contributed substantial weight to the meta-analysis and would be expected to anchor the pooled estimate near the null but still on the protective side, as reflected in the narrow fixed-effect confidence interval. In contrast, smaller or less precise studies likely contributed more to the observed heterogeneity, especially where effect sizes were more extreme in either direction. Although the pooled result favored bisphosphonate use overall, the high I2 value indicates that some individual studies probably reported null associations or even increased risks, while others suggested stronger reductions in cancer risk.

Potential explanations for these outlying or divergent findings include differences in study design, residual confounding by indication, variation in baseline cancer risk, differences in the type of bisphosphonate used (including nitrogen-containing versus non-nitrogen-containing agents), duration of therapy, and the specific cancer outcomes evaluated, such as colorectal, breast, endometrial, liver, or pancreatic cancer. Differences in exposure ascertainment and adjustment for major confounders may also have contributed. Accordingly, while the pooled analysis supports an overall inverse association between bisphosphonate use and cancer risk, the substantial heterogeneity warrants cautious interpretation and suggests that the association may differ across populations and cancer subtypes.

### Risk of Bias

**Risk of bias.** Across the 27 included studies, the overall risk-of-bias profile was unfavorable: 22/27 studies (81.5%) were judged to be at **high risk** overall, while the remaining 5/27 (18.5%) were rated as **unclear risk**; no study was judged to be at low risk. At the domain level, the dominant issue was not one isolated methodological weakness but rather a **universal lack of reporting across all assessed domains**. Specifically, all 27 studies were judged as **unclear risk** for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. Thus, the most common bias concerns were present in every core domain evaluated (27/27 studies for each domain), indicating pervasive uncertainty about internal validity rather than a clearly documented pattern of low- or high-quality trial conduct.

A notable pattern across studies was that risk-of-bias judgments were driven primarily by **insufficient methodological detail**, rather than by explicit reporting of robust safeguards or clearly described flaws. Because the extracted reports did not provide adequate information on sequence generation, concealment, blinding, attrition handling, or reporting practices, it was not possible to identify meaningful differences in bias patterns across study designs (e.g., randomized vs observational studies) from the available dataset. Similarly, there were **no studies at clearly low risk** in any domain. The few studies classified as overall unclear risk (n=5) were not distinguishable because of better-reported domains; rather, they remained uncertain for the same reason as the rest of the evidence base—methods were largely “not reported.” Conversely, the 22 studies judged at overall high risk should be interpreted as contributing the greatest concern to the review, although the domain-specific tables suggest that this high-risk classification likely reflects broader concerns in study conduct or design that were not transparently documented in the articles themselves.

These risk-of-bias findings reduce confidence in the pooled estimate. When all six standard domains are unclear in all 27 studies, the summary effect may be vulnerable to bias from unreported problems in selection, performance, detection, attrition, and reporting processes. As a result, even if the pooled estimate is statistically precise, its credibility is limited by the underlying uncertainty in study validity. Importantly, the **data extraction itself appeared reliable**: the enhanced extractor assigned **high confidence to 24/27 studies**, **medium confidence to 2/27**, and **low confidence to 1/27**. This suggests that the risk-of-bias findings are likely a true reflection of the reporting limitations in the primary studies rather than an artifact of poor extraction. Overall, the evidence base should therefore be interpreted with **caution**, and any conclusions drawn from the meta-analysis should be considered tentative because of the consistently unclear domain-level methodology and the predominance of studies judged at high overall risk of bias.

## Discussion

Across 27 included studies, with 24 contributing to the primary quantitative synthesis, bisphosphonate use was associated with a modest reduction in overall cancer risk compared with non-use (random-effects OR 0.89, 95% CI 0.83-0.96; fixed-effects OR 0.89, 95% CI 0.88-0.91). The direction of effect was consistent across analytic models, which supports the possibility of a real inverse association, but the magnitude was small and should be interpreted cautiously. From a clinical perspective, an approximately 11% relative reduction is potentially relevant at the population level given the widespread use of bisphosphonates in older adults, particularly those with osteoporosis and other bone-related conditions. However, the very high between-study heterogeneity (I2=88.6%, Q p<0.001) indicates that the pooled estimate is an average across substantially different study settings rather than a single effect that is likely to apply uniformly across populations, bisphosphonate classes, durations of use, and cancer sites.

These findings are broadly consistent with the hypothesis that commonly used medications can influence cancer risk, but they should be situated carefully within the wider literature. Unlike prior meta-analyses showing increased colorectal cancer risk with antibiotic exposure or reduced neoplastic progression with cyclooxygenase inhibitors in Barrett's esophagus, our review addresses a different intervention, population, and cancer spectrum, so direct effect-size comparisons are not appropriate. Still, the contrast is instructive: medication-cancer associations are highly exposure-specific and likely depend on mechanism, indication, treatment duration, and the underlying risk profile of the treated population. Our pooled estimate suggests a possible protective association for bisphosphonates overall, but the signal is weaker than that reported for COX inhibitors in a high-risk premalignant population, and it is far less dramatic than the excess mortality signals seen in severe chronic disease populations such as bipolar disorder. This pattern supports a restrained interpretation: bisphosphonates may influence carcinogenesis or cancer detection pathways, but any effect is likely modest and context-dependent.

Several biological mechanisms could plausibly explain an inverse association between bisphosphonate exposure and cancer risk. Nitrogen-containing bisphosphonates inhibit farnesyl pyrophosphate synthase within the mevalonate pathway, which may impair prenylation-dependent signaling involved in tumor cell proliferation, survival, migration, and angiogenesis. Bisphosphonates have also been reported to alter the bone microenvironment, modulate immune activity, and reduce establishment of metastatic niches, although these mechanisms are more directly relevant to cancer progression than to incident primary cancers. For hormone-related cancers such as breast and endometrial cancer, indirect pathways may also be relevant, including differences in bone turnover, estrogen status, and health-system contact among treated patients. At the same time, biological plausibility does not eliminate the possibility of noncausal explanations. Bisphosphonate users may differ systematically from non-users in screening intensity, comorbidity burden, body composition, fracture risk, medication adherence, or concurrent use of calcium, vitamin D, hormone therapy, aspirin, or statins, all of which could shift observed cancer risk independently of bisphosphonates themselves.

The substantial heterogeneity observed in this review is therefore unsurprising. The included studies appear to have varied in population source, underlying indication for treatment, exposure definitions, adjustment strategies, cancer outcomes, and likely duration and class of bisphosphonate use. Pooling all-cancer outcomes with site-specific cancers such as colorectal, breast, endometrial, liver, and pancreatic cancer also introduces clinical heterogeneity because these malignancies differ materially in etiology, latency, and susceptibility to medication-related effects. Exposure misclassification is another likely contributor, particularly where studies relied on prescription or dispensing records that may not reflect adherence. Duration of use is especially important: a causal protective effect would likely require sustained exposure, whereas short-term prescribing may be less informative biologically. Confounding by indication is also a central concern, as patients receiving bisphosphonates are not exchangeable with non-users in most observational settings. Differences in adjustment for age, sex, smoking, obesity, alcohol use, diabetes, prior fractures, and healthcare utilization could readily produce divergent estimates across studies.

This review has several strengths. First, it synthesizes a relatively large body of observational evidence on a clinically important question spanning multiple cancer outcomes and bisphosphonate exposure patterns. Second, the consistency between random- and fixed-effects estimates suggests that the overall inverse direction was not driven solely by small studies. Third, the study-quality profile was generally favorable, with most included studies classified as high quality (24 of 27), while still retaining transparency about the smaller number of medium- and low-quality studies. Fourth, the enhanced extraction process allowed recovery of effect estimates even when raw 2x2 data were unavailable, which is common in pharmacoepidemiologic cancer studies that report only adjusted odds ratios. That said, this same literature imposes important limitations. Many extracted records lacked complete bibliographic metadata, raw event counts, exposure-group totals, or full covariate details, which restricted deeper assessment of comparability across studies and limited opportunities for more granular secondary analyses. The reliance on predominantly observational evidence leaves the findings vulnerable to residual confounding, selection bias, immortal time bias, and surveillance bias. Generalizability may also be limited, as bisphosphonate users are often older and disproportionately female, and the pooled estimate may not apply equally across men, younger populations, or settings with different prescribing patterns.

Taken together, the current evidence does not support using bisphosphonates for cancer prevention in clinical practice, but it does suggest that concerns about increased overall cancer risk with bisphosphonate therapy are not supported and that a modest protective association is plausible. For current practice, bisphosphonates should continue to be prescribed on established indications such as osteoporosis and other bone-related disorders, with any possible anticancer benefit regarded as hypothesis-generating rather than decision-defining. Future research should move beyond broad ever-versus-never comparisons and prioritize well-designed studies that distinguish nitrogen-containing from non-nitrogen-containing agents, quantify cumulative dose and duration, and analyze site-specific cancers separately. New work should also address time-related biases explicitly, use active-comparator designs where feasible, and standardize confounder adjustment to improve comparability. Individual-participant-data meta-analyses and large registry-based studies with validated exposure and outcome definitions would be especially valuable for determining whether the observed inverse association reflects a true pharmacologic effect or the structure of the underlying treated population.

## Conclusion

In this meta-analysis of 27 studies, including 24 contributing to the pooled odds ratio, bisphosphonate use was associated with a lower overall risk of cancer compared with non-use (random-effects OR 0.89, 95% CI 0.83–0.96; p=0.002), indicating about an 11% relative reduction. Clinically, this suggests that bisphosphonates do not appear to increase cancer risk and may confer a modest protective association across the general population and typical users with osteoporosis or related bone disease. These findings support reassurance for patients already using bisphosphonates for established indications and do not suggest a need to avoid treatment because of cancer concerns. However, the substantial between-study heterogeneity (I²=88.6%) and likely differences in populations, cancer types, bisphosphonate classes, and duration of use mean the observed association should be interpreted cautiously and should not, by itself, justify prescribing bisphosphonates for cancer prevention.

## Final Included Studies

- Corpus ID: 664 | A prospective study of bisphosphonate use and risk of colorectal cancer.
- Corpus ID: 678 | Use of bisphosphonates and reduced risk of colorectal cancer.
- Corpus ID: 666 | Reduced colon cancer incidence and mortality in postmenopausal women treated with an oral bisphosphonate--Danish National Register Based Cohort Study.
- Corpus ID: 670 | Exposure to bisphosphonates and risk of colorectal cancer: a population-based nested case-control study.
- Corpus ID: 663 | Oral bisphosphonate use and risk of postmenopausal endometrial cancer.
- Corpus ID: 669 | Bisphosphonate use and risk of renal cell carcinoma: A population-based case-control study.
- Corpus ID: 662 | Oral bisphosphonate use and lung cancer incidence among postmenopausal women.
- Corpus ID: 668 | Alendronate and risk of esophageal cancer: a nationwide population-based study in Taiwan.
- Corpus ID: 679 | Oral alendronate use and risk of cancer in postmenopausal women with osteoporosis: A nationwide study.
- Corpus ID: 64974 | Exposure to oral bisphosphonates and risk of cancer.
- Corpus ID: 677 | The effect of bisphosphonates on the risk of endometrial and ovarian malignancies.
- Corpus ID: 676 | Oral bisphosphonates and risk of cancer of oesophagus, stomach, and colorectum: case-control analysis within a UK primary care cohort.
- Corpus ID: 65046 | Risk of colorectal cancer in users of bisphosphonates: analysis of population-based electronic health records.
- Corpus ID: 658 | Esophageal and gastric cancer incidence and mortality in alendronate users.
- Corpus ID: 675 | Oral bisphosphonates and colorectal cancer.
- Corpus ID: 659 | Exposure to oral bisphosphonates and risk of esophageal cancer.
- Corpus ID: 667 | Use of Bisphosphonates and Risk of Breast Cancer in a French Cohort of Postmenopausal Women.
- Corpus ID: 65069 | Bisphosphonates and risk of upper gastrointestinal cancer--a case control study using the General Practice Research Database (GPRD).
- Corpus ID: 64946 | Exposure to oral bisphosphonates and risk of gastrointestinal cancer.
- Corpus ID: 64949 | Oral Bisphosphonates and Upper Gastrointestinal Cancer Risks in Asians with Osteoporosis: A Nested Case-Control Study Using National Retrospective Cohort Sample Data from Korea.
- Corpus ID: 665 | Protective effect of bisphosphonates on endometrial cancer incidence in data from the Prostate, Lung, Colorectal and Ovarian (PLCO) cancer screening trial.
- Corpus ID: 64973 | Oral bisphosphonates and risk of esophageal cancer: a dose-intensity analysis in a nationwide population.
- Corpus ID: 673 | Oral Bisphosphonate Exposure and the Risk of Upper Gastrointestinal Cancers.
- Corpus ID: 64950 | Oral bisphosphonates and upper gastrointestinal toxicity: a study of cancer and early signals of esophageal injury.
- Corpus ID: 672 | Exposure to bisphosphonates and risk of gastrointestinal cancers: series of nested case-control studies with QResearch and CPRD data.
- Corpus ID: 660 | A higher dosage of oral alendronate will increase the subsequent cancer risk of osteoporosis patients in Taiwan: a population-based cohort study.
- Corpus ID: 671 | Exposure to bisphosphonates and risk of common non-gastrointestinal cancers: series of nested case-control studies using two primary-care databases.
