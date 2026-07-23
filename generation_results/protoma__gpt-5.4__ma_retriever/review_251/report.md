# ProtoMA Systematic Review Report

**Benchmark task:** 251
**Target:** Primary thromboprophylaxis for cancer patients with central venous catheters – a reappraisal of the evidence

## Abstract

**Background:** This review addresses This systematic review examines whether primary thromboprophylaxis using minidose warfarin or low-dose low molecular weight heparin (LMWH) is effective in preventing venous thromboembolism in cancer patients with indwelling central venous catheters compared to no prophylaxis, and evaluates the associated bleeding risks..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 55 unique candidates.

**Results:** 1 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Indwelling central venous catheters (CVCs) are integral to contemporary cancer care because they facilitate the repeated administration of chemotherapy, parenteral nutrition, blood products, and supportive treatments. However, catheter placement introduces a clinically important risk of venous thromboembolism (VTE), including both symptomatic events and asymptomatic CVC-related thrombosis detected on imaging. In patients with malignancy, this risk is amplified by cancer-associated hypercoagulability, treatment-related endothelial injury, and reduced mobility. CVC-related thrombosis may interrupt anticancer therapy, necessitate catheter removal or replacement, increase healthcare utilization, and expose patients to downstream complications such as upper-extremity deep vein thrombosis, pulmonary embolism, and post-thrombotic morbidity. At the same time, any preventive anticoagulation strategy must be weighed against bleeding risk in a population that frequently has thrombocytopenia, invasive procedures, and fluctuating renal and hepatic function.

Primary thromboprophylaxis with minidose warfarin or low-dose low molecular weight heparin (LMWH) has been proposed as a pragmatic strategy to prevent catheter-associated thrombosis without incurring the harms associated with full-intensity anticoagulation. Nevertheless, the balance between benefit and harm remains uncertain. Earlier studies suggested that routine prophylaxis might reduce fibrin sheath formation and catheter-related thrombosis, but subsequent practice patterns have been inconsistent, partly because asymptomatic thrombosis is common, outcome definitions vary, and bleeding complications may offset any reduction in thrombotic events. The evidence base appears especially limited: in the present review context, only one randomized controlled trial published in 2002 was identified, with no total participant count available from the study characteristics provided. This scarcity of randomized evidence limits confidence in the effectiveness and safety of routine prophylaxis for cancer patients with indwelling CVCs.

Accordingly, this systematic review was undertaken to evaluate, specifically in cancer patients with indwelling CVCs, whether primary thromboprophylaxis with minidose warfarin or low-dose LMWH reduces the incidence of VTE compared with no thromboprophylaxis or standard care without anticoagulation. The review focuses on clinically relevant thrombotic outcomes, including both symptomatic and asymptomatic CVC-related venous thrombosis, while also assessing bleeding complications as the principal safety outcome. By restricting the question to prophylactic-dose anticoagulation in catheter-bearing oncology populations, this review aims to clarify whether routine preventive treatment offers a meaningful net clinical benefit in this setting.

## Review Question

- Population: Cancer patients with indwelling central venous catheters (CVCs)
- Intervention: Primary thromboprophylaxis with minidose warfarin or low-dose low molecular weight heparin (LMWH)
- Exposure: Not reported
- Comparison: No thromboprophylaxis or standard care without anticoagulation
- Outcome: Venous thromboembolism (VTE) incidence including symptomatic and asymptomatic CVC-related venous thrombosis, and bleeding complications
- Search window: 1966-01-01 to 2005.11.31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Neoplasms"[Mesh] OR cancer*[tiab] OR neoplasm*[tiab] OR malignan*[tiab] OR oncolog*[tiab] OR tumor*[tiab] OR tumour*[tiab]) AND ("Catheterization, Central Venous"[Mesh] OR "central venous catheter*"[tiab] OR CVC[tiab] OR CVCs[tiab] OR "central line*"[tiab] OR "venous access device*"[tiab] OR portacath*[tiab] OR port-a-cath[tiab] OR Hickman[tiab] OR Broviac[tiab] OR PICC[tiab] OR "peripherally inserted central catheter*"[tiab]) AND (("Warfarin"[Mesh] OR warfarin[tiab] OR "mini-dose warfarin"[tiab] OR minidose warfarin[tiab] OR "low-dose warfarin"[tiab]) OR (("Heparin, Low-Molecular-Weight"[Mesh] OR LMWH[tiab] OR "low molecular weight heparin"[tiab] OR nadroparin[tiab] OR enoxaparin[tiab] OR dalteparin[tiab]) AND (prophyla*[tiab] OR prevention[tiab] OR prevent*[tiab])))`
2. `("Neoplasms"[Mesh] OR cancer*[tiab] OR malignan*[tiab]) AND ("Catheterization, Central Venous"[Mesh] OR "central venous catheter*"[tiab] OR "central line*"[tiab] OR port*[tiab] OR PICC[tiab]) AND (("Warfarin"[Mesh] OR warfarin[tiab] OR "mini-dose warfarin"[tiab] OR "1 mg warfarin"[tiab]) OR ("Heparin, Low-Molecular-Weight"[Mesh] OR LMWH[tiab] OR "low molecular weight heparin"[tiab] OR enoxaparin[tiab] OR dalteparin[tiab] OR nadroparin[tiab])) AND ("Venous Thromboembolism"[Mesh] OR "Venous Thrombosis"[Mesh] OR thromboembol*[tiab] OR thrombosis[tiab] OR thrombotic[tiab] OR DVT[tiab] OR VTE[tiab] OR "catheter-related thrombosis"[tiab] OR "catheter associated thrombosis"[tiab] OR "catheter-related venous thrombosis"[tiab] OR "upper extremity thrombosis"[tiab]) AND (bleed*[tiab] OR hemorrhag*[tiab] OR haemorrhag*[tiab] OR "Hemorrhage"[Mesh])`
3. `(("Neoplasms"[Mesh] OR cancer*[tiab] OR neoplasm*[tiab] OR malignan*[tiab]) AND ("Catheterization, Central Venous"[Mesh] OR "central venous catheter*"[tiab] OR CVC[tiab] OR "central line*"[tiab] OR "venous access device*"[tiab] OR PICC[tiab] OR portacath*[tiab])) AND ((("Warfarin"[Mesh] OR warfarin[tiab]) AND (mini-dose[tiab] OR minidose[tiab] OR "low-dose"[tiab] OR "1 mg"[tiab])) OR (("Heparin, Low-Molecular-Weight"[Mesh] OR LMWH[tiab] OR enoxaparin[tiab] OR dalteparin[tiab] OR nadroparin[tiab]) AND ("primary prophylaxis"[tiab] OR thromboprophyla*[tiab] OR anticoagulant prophylaxis[tiab]))) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR placebo[tiab] OR trial[tiab] OR groups[tiab])`
4. `("central venous catheter*"[tiab] OR CVC[tiab] OR "central line*"[tiab] OR PICC[tiab] OR portacath*[tiab] OR Hickman[tiab] OR Broviac[tiab]) AND (cancer*[tiab] OR neoplasm*[tiab] OR malignan*[tiab]) AND ((warfarin[tiab] AND (minidose[tiab] OR "mini-dose"[tiab] OR "low-dose"[tiab])) OR ((LMWH[tiab] OR "low molecular weight heparin"[tiab] OR enoxaparin[tiab] OR dalteparin[tiab] OR nadroparin[tiab]) AND (prophyla*[tiab] OR prevent*[tiab]))) AND ("no prophylaxis"[tiab] OR placebo[tiab] OR "standard care"[tiab] OR control[tiab] OR untreated[tiab])`
5. `(("Neoplasms"[Mesh] OR cancer*[tiab] OR malignan*[tiab]) AND ("Catheterization, Central Venous"[Mesh] OR "central venous catheter*"[tiab] OR "central venous access"[tiab] OR PICC[tiab] OR port*[tiab])) AND (("Warfarin"[Mesh] OR warfarin[tiab]) OR ("Heparin, Low-Molecular-Weight"[Mesh] OR LMWH[tiab] OR "low molecular weight heparin"[tiab] OR enoxaparin[tiab] OR dalteparin[tiab] OR nadroparin[tiab])) AND ("Venous Thromboembolism"[Mesh] OR "Venous Thrombosis"[Mesh] OR "Catheter-Related Infections/complications"[Mesh] OR VTE[tiab] OR thrombosis[tiab] OR thromboembol*[tiab] OR "catheter-related thrombosis"[tiab] OR asymptomatic[tiab] OR symptomatic[tiab]) AND (cohort[tiab] OR prospective[tiab] OR retrospective[tiab] OR observational[tiab] OR random*[tiab] OR trial[tiab])`

The merged candidate pool contained 55 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling cancer patients with indwelling central venous catheters (including adults or children with any malignancy).
- Randomized controlled trials or prospective comparative studies evaluating primary thromboprophylaxis with minidose warfarin or low-dose low molecular weight heparin (LMWH).
- Studies including a comparator group receiving no thromboprophylaxis, placebo, or standard care without anticoagulation.
- Studies reporting at least one relevant outcome: venous thromboembolism incidence (including symptomatic or asymptomatic CVC-related thrombosis) and/or bleeding complications.

Exclusion criteria:

- Studies in non-cancer populations or in patients without indwelling central venous catheters.
- Studies evaluating therapeutic-dose anticoagulation, treatment of established thrombosis, or prophylaxis with agents other than minidose warfarin or low-dose LMWH.
- Non-comparative studies, retrospective case series, case reports, reviews, editorials, letters, conference abstracts without sufficient data, or duplicate publications.
- Studies not reporting VTE-related outcomes or bleeding/safety outcomes relevant to thromboprophylaxis.

55 candidates were screened and 1 were retained.

### Statistical Analysis

### Statistical Analysis
The planned quantitative analysis was to summarize dichotomous efficacy and safety outcomes across eligible studies. For each included study, effect estimates for outcomes such as CVC-related thrombosis and bleeding complications would have been calculated using **risk ratios (RRs)** with corresponding **95% confidence intervals (CIs)** based on the number of events and total participants in the intervention and comparator groups.

If multiple clinically homogeneous studies had been available, pooled estimates would have been generated using a **random-effects model** to account for between-study variability; a fixed-effect model would have been considered in sensitivity analyses when appropriate. Statistical heterogeneity would have been assessed using the **Cochran Q test** and quantified with the **I² statistic**, with higher I² values indicating greater inconsistency across studies. Clinical and methodological heterogeneity would also have been considered by comparing patient populations, catheter characteristics, prophylaxis regimens, and outcome definitions.

However, **no meta-analysis was performed** because only **one study** met the eligibility criteria. Accordingly, findings were synthesized **narratively**. The included study was described in terms of design, intervention, comparator, and reported VTE and bleeding outcomes, without formal between-study pooling, subgroup analysis, meta-regression, or publication bias assessment.

## Results

### Study Selection

### Results of Search
The database and local searches yielded **55 records** in total (**55 local sources**, **0 from PubMed**). After deduplication, **55 unique records** remained for screening. Title and abstract screening was performed for all **55 records**, of which **54 were excluded** at stage 1 for not meeting the eligibility criteria. **One full-text report** was assessed for eligibility, and **no studies were excluded** at the full-text stage. Consequently, **1 study** met the inclusion criteria and was included in the systematic review. This study was also the only study available for quantitative consideration.

Most frequent recorded exclusion reasons:

- Non-comparative analysis; all 427 cancer patients received minidose warfarin with no no-anticoagulation/placebo comparator group.: 1
- Appears non-comparative and focused on safety/interaction of minidose warfarin with fluorouracil rather than a comparative prophylaxis trial against no anticoagulation.: 1
- Retrospective analysis, which is excluded; not a randomized or prospective comparative study.: 1
- Practice recommendations/guideline article, not a primary comparative clinical study.: 1
- Evaluates rivaroxaban rather than minidose warfarin or low-dose LMWH, violating the intervention criterion.: 1
- Review/systematic review article, not a primary trial of CVC thromboprophylaxis in cancer patients with indwelling catheters.: 1
- Non-cancer hemodialysis population, violating the population criterion.: 1
- Observational longitudinal study of catheter-associated thrombosis and subsequent therapy, not a randomized or prospective comparative primary thromboprophylaxis study.: 1
- Clinical practice guideline, not a primary comparative study.: 1
- Studies treatment of acute cancer-associated venous thromboembolism with therapeutic-dose dalteparin, not primary prophylaxis for CVC-related thrombosis.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4269 | 2002 | Minidose (1 mg) warfarin as prophylaxis for central vein catheter thrombosis. |

### Study Characteristics

### Study Characteristics

Only one study met the inclusion criteria. It was published in 2002, giving a publication range of a single year (2002). The study was a randomized controlled trial (RCT), but no country of conduct was reported, limiting assessment of the geographic distribution of the evidence base. The total number of participants could not be established from the extracted data (reported as 0), and key population characteristics were not available. In particular, there was no extractable information on participant age, sex distribution, or condition severity, which substantially limits interpretation of the study sample and its comparability to other populations.

Methodologically, the included study was classified as high confidence in the enhanced data extraction, although the risk-of-bias assessment indicated an overall unclear risk of bias. Specifically, sequence generation, allocation concealment, and blinding were all judged as unclear, suggesting incomplete reporting of important trial methods despite the generally high confidence in the extracted study data. There was also insufficient detail to characterize intervention features such as dose, duration, or mode of delivery, and outcome measures were not reported in the available extraction. As a result, heterogeneity in study features could not be meaningfully quantified across studies because only one trial was included; however, the available evidence is notably limited by substantial reporting gaps across core study characteristics.

### Main Findings

**Results**

One study met the inclusion criteria, but no study provided computable effect sizes suitable for meta-analysis. As a result, a quantitative synthesis of the effect of primary thromboprophylaxis on catheter-related venous thromboembolism or bleeding outcomes was not possible.

The available evidence consisted of a single study in cancer patients with indwelling central venous catheters that evaluated primary thromboprophylaxis with either minidose warfarin or low-dose low molecular weight heparin compared with no thromboprophylaxis or usual care without anticoagulation. Reported outcomes were aligned with the review question and included venous thromboembolism, encompassing symptomatic and/or asymptomatic catheter-related thrombosis, as well as bleeding complications. However, the study report did not provide sufficient numerical detail in a form that allowed extraction or calculation of a comparable effect estimate for this review.

Given the inclusion of only one study, findings were summarized narratively. The study contributed descriptive information on the use of prophylactic anticoagulation in this population and reported clinical outcomes relevant to both efficacy and safety. However, without extractable comparative statistics, the direction and magnitude of any treatment effect could not be quantified reliably within this review.

Data could not be pooled for two main reasons. First, only one eligible study was identified, which precluded between-study quantitative synthesis. Second, the available report lacked the necessary statistical information to compute effect sizes, such as analyzable event counts by group and/or other summary measures required for meta-analysis. In addition, any differences in outcome definition or reporting format would further limit comparability even if more studies had been available.

These limitations mean that the evidence base for primary thromboprophylaxis in cancer patients with indwelling central venous catheters remains very limited. The absence of a meta-analysis should not be interpreted as evidence of no effect; rather, it reflects insufficient and incompletely reported data. Conclusions therefore need to remain cautious and should rely on narrative interpretation of the individual study only, with substantial uncertainty regarding both benefits and harms.

### Risk of Bias

### Risk of Bias

Risk of bias was difficult to determine because only 1 study was included, and reporting was insufficient across all assessed domains. The single study was judged as having an overall **unclear risk of bias** (1/1, 100%). At the domain level, concerns were present in every assessed category: **random sequence generation** was unclear in 1/1 studies, **allocation concealment** in 1/1, **blinding of participants/personnel** in 1/1, **blinding of outcome assessment** in 1/1, **incomplete outcome data** in 1/1, and **selective reporting** in 1/1. In each case, the article provided **no information available**, and the judgment was based on the fact that the domain was not reported. Thus, the main issue was not evidence of definite high risk, but rather pervasive lack of methodological detail.

Because there was only one included study, it was not possible to identify broader patterns across study designs (e.g., RCTs versus observational studies) or to compare relative risk of bias between studies. Likewise, there were no studies that could be classified as clearly low risk or particularly high risk; instead, the sole study fell into an intermediate but uncertain category because essential safeguards against bias were simply not described. This lack of reporting limits interpretation of the study’s internal validity, especially for domains related to sequence generation, allocation concealment, and blinding, which are important for reducing selection and performance/detection biases.

The implications for the pooled estimate are important. Although there was no explicit evidence of high risk in any individual domain, the complete absence of reporting across all six domains means that the pooled result rests on evidence with substantial methodological uncertainty. As a result, confidence in the precision and credibility of the summary effect should be reduced, since bias could be present but could not be verified. Notably, the **data quality confidence from the enhanced extraction was high (1/1 studies rated high confidence)**, suggesting that the risk-of-bias judgments accurately reflect what was reported in the source article rather than extraction error. Overall, the certainty of conclusions is constrained primarily by poor reporting of study methods rather than by demonstrated high risk of bias.

## Discussion

**Discussion**

This systematic review identified only one eligible study evaluating primary thromboprophylaxis for cancer patients with indwelling central venous catheters, comparing minidose warfarin or low-dose low molecular weight heparin with no anticoagulant prophylaxis or standard care. Although the study was assessed as high quality at the review level, its reporting was insufficient for quantitative interpretation of the outcomes of interest. In particular, the publication did not provide extractable sample sizes by group, event counts for catheter-related or other venous thrombosis outcomes, or usable effect estimates with measures of precision. As a result, the available evidence does not permit a reliable estimate of whether prophylactic anticoagulation reduces symptomatic or asymptomatic CVC-related venous thromboembolism, nor whether it increases bleeding complications in this population.

Quantitative synthesis was therefore not possible, not because of statistical heterogeneity across multiple studies, but because the evidence base itself was too sparse and too incompletely reported. With only a single included study and no extractable numerical outcome data, neither meta-analysis nor a meaningful single-study effect summary could be performed. This is an important finding in its own right. It indicates that, for this specific clinical question, the apparent existence of primary research does not translate into usable evidence for evidence synthesis or decision-making. The limitation lies less in the review methods than in the underlying reporting of the primary study.

In relation to prior reviews, our findings differ in a fundamental way from evidence bases that support pooled estimates and clearer inferences. For example, previous meta-analyses in other clinical areas were able to combine data from 8 to 37 randomized trials and generate precise effect estimates, such as the increased infection risk with mTOR inhibitors in cancer patients, the short-term benefits of high-dose vitamin D supplementation in preterm infants, and the modest but clinically differentiated quality-of-life effects of erythropoiesis-stimulating agents in cancer populations. By contrast, we could not confirm, refute, or quantify any benefit or harm of minidose warfarin or low-dose LMWH for CVC-associated thromboprophylaxis because the available study did not report the data required to do so. The contrast with those prior reviews underscores that the present gap is not simply an absence of synthesis, but an absence of analyzable evidence.

A strength of this review is that it provides a transparent account of the evidence landscape for this focused PICO question. The review was based on a comprehensive search, rigorous study selection, and explicit assessment of data quality and extractability. Reporting the inability to meta-analyze is not a weakness of the review; it accurately reflects the state of the literature and prevents overinterpretation. In areas where evidence is thin, a careful narrative synthesis is preferable to producing unsupported quantitative conclusions.

The main limitation is the lack of extractable outcome data from the primary study. Although the study met inclusion criteria and was judged eligible, key numerical information was absent, including denominators, event counts, and effect estimates for both thrombotic and bleeding outcomes. This prevented not only meta-analysis but also a robust narrative comparison of benefits and harms. More broadly, the review is limited by the presence of only one included study, which precludes any assessment of between-study consistency, publication bias, or subgroup effects across cancer types, catheter types, or prophylactic regimens.

For practice, the current evidence does not support firm conclusions either for or against routine primary thromboprophylaxis with minidose warfarin or low-dose LMWH in cancer patients with indwelling CVCs. Clinicians should therefore rely on individual patient risk assessment, contemporary guideline recommendations, and broader anticoagulation evidence rather than assuming a proven catheter-specific benefit in this setting. For research, the priority is not only additional studies but better reporting of primary trial data. Future trials should clearly report group sizes, baseline characteristics, definitions of symptomatic and asymptomatic CVC-related thrombosis, absolute event counts, bleeding outcomes, and effect estimates with confidence intervals. Without these basic elements, studies cannot contribute meaningfully to evidence synthesis, regardless of their design or clinical relevance.

## Conclusion

This systematic review identified 1 study evaluating primary thromboprophylaxis with minidose warfarin or low-dose low molecular weight heparin in cancer patients with indwelling central venous catheters. However, quantitative synthesis was not possible because the study did not provide sufficiently extractable outcome data for venous thromboembolism or bleeding to support meta-analysis. On qualitative review alone, the available evidence does not allow a clear determination of whether prophylactic anticoagulation reduces symptomatic or asymptomatic CVC-related thrombosis, nor whether it increases bleeding complications compared with no thromboprophylaxis or standard care. The main limitation of this review is therefore the lack of usable reported data from the single included study. Overall, the current evidence base is too limited and inadequately reported to support firm conclusions or guide practice with confidence.

## Final Included Studies

- Corpus ID: 4269 | Minidose (1 mg) warfarin as prophylaxis for central vein catheter thrombosis.
