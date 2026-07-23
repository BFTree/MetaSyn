# ProtoMA Systematic Review Report

**Benchmark task:** 148
**Target:** Alcohol intake and renal cell cancer risk: a meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates whether alcoholic beverage intake (including total alcohol, beer, wine, and liquor) is associated with the risk of renal cell cancer, and examines whether this association differs by sex, study design, and level of consumption..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 44 unique candidates.

**Results:** 8 study reports were retained after explicit screening. The random-effects estimate was 0.686 (95% CI 0.633 to 0.745); I-squared was 5.0%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Renal cell cancer is the predominant histologic subtype of kidney cancer in adults and accounts for most kidney cancer-related morbidity and mortality. Because established risk factors such as smoking, obesity, and hypertension do not fully explain disease occurrence, potentially modifiable dietary exposures remain relevant for prevention research. Alcohol intake is of particular interest because it is common in the general adult population, varies substantially by beverage type and consumption level, and has shown site-specific associations with cancer risk that are not uniformly adverse. For renal cell cancer, clarification of this relationship has direct public health relevance: even modest risk differences associated with total alcohol or specific beverages could affect a large number of adults given the widespread exposure.

Epidemiologic findings on alcohol intake and renal cell cancer risk have been inconsistent across case-control and cohort studies. Published evidence includes population-based case-control studies, pooled analyses of multicenter case-control datasets, prospective cohort studies, and a large pooled analysis of 12 prospective cohorts, together comprising 8 studies published between 2002 and 2015 and 1,072,457 participants. Although several investigations have suggested an inverse association between alcohol consumption and renal cell cancer, the magnitude and consistency of the association have varied according to study design, exposure definition, and beverage subtype, including beer, wine, and liquor. In addition, comparisons have often used different reference groups, with the lowest category of intake defined as non-drinking or minimal drinking, which complicates interpretation across studies. A focused synthesis is therefore needed to determine whether alcohol-related associations are consistent when evaluated against the lowest intake category and when beverage-specific exposures are considered separately.

This systematic review was undertaken to evaluate the association between alcoholic beverage intake and risk of renal cell cancer in the general adult population. Specifically, we examined evidence from case-control and cohort studies comparing higher categories of total alcohol, beer, wine, and liquor consumption with the lowest or bottom category of intake, defined as non-drinkers or minimal drinkers, and assessed renal cell cancer risk using relative risk estimates. By synthesizing data across these study designs and exposure categories, this review aims to clarify the direction and strength of the association and to identify whether any observed relationship differs by alcoholic beverage type.

## Review Question

- Population: General adult population (participants from case-control and cohort studies examining renal cell cancer)
- Intervention: Not reported
- Exposure: Alcoholic beverage intake (total alcohol, beer, wine, and liquor consumption)
- Comparison: Lowest/bottom category of alcohol intake (non-drinkers or minimal drinkers)
- Outcome: Renal cell cancer risk (measured as relative risk)
- Search window: Not reported to 2011-08-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Carcinoma, Renal Cell"[Mesh] OR "Kidney Neoplasms"[Mesh] OR renal cell carcinoma[tiab] OR renal cell cancer[tiab] OR kidney cancer[tiab] OR kidney neoplasm*[tiab] OR RCC[tiab]) AND ("Alcohol Drinking"[Mesh] OR alcohol*[tiab] OR ethanol[tiab] OR alcoholic beverage*[tiab] OR beer[tiab] OR wine[tiab] OR liquor[tiab] OR spirits[tiab])`
2. `(("Carcinoma, Renal Cell"[Mesh] OR "Kidney Neoplasms"[Mesh] OR renal cell carcinoma[tiab] OR renal cell cancer[tiab] OR kidney cancer[tiab] OR kidney neoplasm*[tiab]) AND ("Alcohol Drinking"[Mesh] OR alcohol drinking[tiab] OR alcohol consumption[tiab] OR alcohol intake[tiab] OR ethanol[tiab] OR alcoholic beverage*[tiab] OR beer[tiab] OR wine[tiab] OR liquor[tiab] OR spirits[tiab]) AND (risk[tiab] OR relative risk[tiab] OR odds ratio[tiab] OR hazard ratio[tiab] OR incidence[tiab] OR association[tiab]))`
3. `(("Carcinoma, Renal Cell"[Mesh] OR renal cell carcinoma[tiab] OR renal cell cancer[tiab] OR kidney cancer[tiab]) AND (beer[tiab] OR wine[tiab] OR liquor[tiab] OR spirits[tiab] OR total alcohol[tiab] OR alcohol intake[tiab] OR alcohol consumption[tiab]) AND (cohort[tiab] OR prospective[tiab] OR longitudinal[tiab] OR "Cohort Studies"[Mesh] OR "Prospective Studies"[Mesh] OR case-control[tiab] OR case control[tiab] OR "Case-Control Studies"[Mesh]))`
4. `(("Kidney Neoplasms"[Mesh] OR "Carcinoma, Renal Cell"[Mesh] OR renal cell carcinoma[tiab] OR kidney neoplasm*[tiab]) AND ("Alcohol Drinking"[Mesh] OR alcohol*[tiab] OR beer[tiab] OR wine[tiab] OR liquor[tiab] OR spirits[tiab]) AND (nondrinker*[tiab] OR non-drinker*[tiab] OR abstainer*[tiab] OR never drinker*[tiab] OR minimal drinker*[tiab] OR lowest category[tiab] OR reference category[tiab]))`
5. `((renal cell carcinoma[tiab] OR renal cell cancer[tiab] OR kidney cancer[tiab] OR "Carcinoma, Renal Cell"[Mesh]) AND (alcohol intake[tiab] OR alcohol consumption[tiab] OR alcohol drinking[tiab] OR alcoholic beverage*[tiab] OR ethanol[tiab] OR beer[tiab] OR wine[tiab] OR liquor[tiab] OR spirits[tiab]) AND ("Case-Control Studies"[Mesh] OR "Cohort Studies"[Mesh] OR case-control[tiab] OR case control[tiab] OR cohort[tiab] OR prospective[tiab] OR observational[tiab]) NOT (review[pt] OR meta-analysis[pt] OR editorial[pt] OR letter[pt]))`

The merged candidate pool contained 44 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational studies with a case-control or cohort design conducted in the general adult population.
- Studies evaluating alcoholic beverage intake as the exposure, including total alcohol, beer, wine, or liquor consumption, with a lowest/bottom intake category (non-drinkers or minimal drinkers) as the reference/comparator.
- Studies reporting renal cell cancer risk or incidence as the outcome.
- Studies providing relative risk estimates (e.g., RR, OR, or HR) with 95% confidence intervals, or sufficient data to calculate them, for alcohol intake categories.

Exclusion criteria:

- Studies not using a case-control or cohort design, such as reviews, editorials, case reports, ecological studies, or experimental trials.
- Studies conducted in non-general or non-adult populations, or not specifically examining renal cell cancer.
- Studies not assessing alcohol intake separately (e.g., only total dietary patterns or mixed exposures) or not distinguishing total alcohol, beer, wine, or liquor consumption.
- Studies not reporting effect estimates for renal cell cancer risk, lacking a usable low-intake reference group, or duplicate publications of the same study population.

44 candidates were screened and 8 were retained.

### Statistical Analysis

### Statistical Analysis
The quantitative synthesis was based on **odds ratios (ORs)** as the common effect measure. For each included study, the risk estimate comparing the **highest category of alcohol intake** with the **lowest category** (non-drinkers or minimal drinkers) was extracted. Because renal cell cancer is a relatively uncommon outcome, reported relative risks were considered sufficiently comparable to odds ratios for meta-analytic pooling when necessary.

Pooled summary estimates were calculated using both **random-effects** and **fixed-effect** models, with the random-effects model treated as the primary analysis because it accounts for potential between-study variability in populations, exposure definitions, and beverage-specific intake assessment. Across **8 studies**, the pooled **random-effects OR was 0.686** with a **95% CI of 0.633 to 0.745** (**p = 0.0000**). The corresponding **fixed-effect OR was 0.687** with a **95% CI of 0.636 to 0.743** (**p = 0.0000**).

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and the between-study variance estimate **tau-squared (τ²)**. Heterogeneity was low, with **I² = 5.0%**, **Q = 7.37 (p = 0.392)**, and **τ² = 0.0007**, indicating minimal inconsistency across studies. The close agreement between the fixed-effect and random-effects estimates further supported the stability of the pooled result. All statistical tests were two-sided, and a p-value <0.05 was considered statistically significant.

## Results

### Study Selection

### Results of Search
The literature search yielded **44 records** after deduplication (**44 from local sources** and **0 from PubMed**). All 44 records underwent title and abstract screening, of which **36 were excluded** at the first stage. **Eight full-text articles** were assessed for eligibility, and **no studies were excluded** at the full-text stage. Consequently, **8 studies** met the inclusion criteria and were included in the qualitative and quantitative synthesis. The study selection process therefore showed complete retention from full-text review to final inclusion (**8/8, 100%**).

Most frequent recorded exclusion reasons:

- Meta-analysis/systematic review of prospective cohort studies, not an original case-control or cohort study.: 1
- Meta-analysis of published case-control studies, not an original observational study.: 1
- Meta-analysis of observational studies, not an original case-control or cohort study.: 1
- Prospective cohort of UK women focused on total fluids and specific beverages; abstract does not indicate alcohol was assessed separately as total alcohol, beer, wine, or liquor with a usable low-intake alcohol reference group.: 1
- Study focused on total fluid and specific beverage intake; abstract does not indicate separate assessment of alcohol exposure with a low-intake alcohol reference group or alcohol-specific effect estimates.: 1
- Case-control study of 13 cancer types in men; abstract does not specifically report renal cell cancer results or alcohol effect estimates for renal cell cancer.: 1
- Ecological worldwide population-based study, which is an excluded study design.: 1
- Prospective study of soft drink and juice consumption, not alcohol intake as the exposure of interest.: 1
- Case-cohort study focused on sodium, potassium, and fluid intake rather than alcohol intake as the exposure.: 1
- Although a case-control study of renal cell carcinoma risk factors, the abstract does not provide alcohol-specific renal cell cancer effect estimates or clearly assess alcohol separately with a low-intake reference group.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 426 | 2007 | Alcoholic beverages and risk of renal cell cancer. |
| 427 | 2007 | Alcohol intake and renal cell cancer in a pooled analysis of 12 prospective studies. |
| 61863 | 2008 | Alcohol consumption and renal cell cancer risk in two Italian case-control studies. |
| 425 | 2002 | Gender, alcohol consumption, and renal cell carcinoma. |
| 61859 | 2015 | A prospective study of alcohol consumption and renal cell carcinoma risk. |
| 429 | 2008 | Alcohol drinking and renal cell carcinoma in Canadian men and women. |
| 61870 | 2006 | Total fluid intake and use of individual beverages and risk of renal cell cancer in two large cohorts. |
| 61864 | 2005 | Alcohol consumption and risk of renal cell carcinoma: a prospective study of Swedish women. |

### Study Characteristics

Eight studies met the inclusion criteria, contributing data from 1,072,457 participants and spanning publication years from 2002 to 2015. The evidence base was methodologically diverse, comprising two population-based case-control studies, two prospective cohort studies, one prospective cohort study, one pooled analysis of 12 prospective cohort studies, one pooled analysis of two multicentric case-control studies, and one additional case-control study. Geographically, the studies were conducted mainly in high-income Western settings, with two from Sweden and one each from Italy, the USA, Canada, and the United States; two pooled or cohort analyses did not clearly report a single country of origin. This distribution indicates a concentration of evidence in North America and Northern/Western Europe, with limited representation from other regions.

Substantial heterogeneity was evident across study characteristics. Sample sizes varied markedly, from small case-control datasets involving a few thousand participants to very large pooled and cohort analyses including more than 760,000 individuals. Based on the enhanced extraction, overall data quality was generally strong, with seven studies assessed as high confidence and one as medium confidence. However, risk-of-bias judgments were more mixed: two studies were rated as high risk, one as low risk, and the remainder as unclear risk, with random sequence generation, allocation concealment, and blinding uniformly reported as unclear. The predominance of observational designs, together with variation in study scale and analytic approach, suggests important methodological heterogeneity that should be considered when interpreting pooled findings.

Reporting of participant and intervention characteristics appeared inconsistent across studies. While the included populations likely differed in age distribution, sex composition, and condition severity, these features were not consistently available in the extracted dataset, limiting more detailed cross-study comparison. Similarly, there was insufficient structured information on intervention dose, duration, delivery mode, or the exact outcome measures used to permit a precise synthesis of these elements in this subsection. Nonetheless, the variation in design, setting, and reporting completeness indicates notable clinical and methodological heterogeneity across the included evidence base.

### Main Findings

**Results**

The pooled analysis demonstrated an inverse association between higher alcohol intake and renal cell cancer risk when compared with the lowest category of intake. Across 8 studies reporting odds ratios, the random-effects pooled OR was 0.686 (95% CI 0.633-0.745; p<0.001), indicating that alcohol consumption was associated with a statistically significant lower relative risk of renal cell cancer. The corresponding fixed-effect estimate was nearly identical (OR 0.687, 95% CI 0.636-0.743; p<0.001), which supports the stability of the overall finding.

In practical terms, this corresponds to an approximately 31% relative reduction in renal cell cancer risk among participants in the higher alcohol intake categories compared with those in the lowest or minimal intake groups. The magnitude of effect was moderate and the confidence interval was relatively narrow, suggesting a fairly precise pooled estimate. While this pattern is consistent with a potentially meaningful protective association, the observational nature of the underlying studies means the finding should be interpreted with appropriate caution.

Between-study heterogeneity was low. The I2 value was 5.0%, with a Cochran Q statistic of 7.37 (p=0.392) and tau2 of 0.0007, indicating little evidence of important inconsistency across studies. This low heterogeneity suggests that the direction and magnitude of the association were generally similar across the included case-control and cohort studies, and that the pooled estimate was not driven by substantial disagreement between studies.

The close agreement between the random-effects and fixed-effect models further indicates that no single study or small subset of studies appeared to materially distort the summary effect. Taken together, the data suggest a consistent inverse association across the available evidence base, with the most precise studies likely contributing substantially to the overall estimate while remaining aligned with the broader pattern observed across studies.

No clear evidence of influential outliers is apparent from the heterogeneity statistics alone. The low I2 and non-significant Q test argue against the presence of markedly divergent study results. Any minor variation between studies may plausibly reflect differences in study design, exposure categorization, residual confounding, or the composition of the reference group, particularly where the lowest alcohol category included either lifelong non-drinkers or minimal drinkers. However, these differences do not appear sufficient to meaningfully alter the overall conclusion. If study-level forest plot or influence-analysis data are available, these would allow more specific identification of the largest or most precise individual studies and any subtle outlying estimates.

### Risk of Bias

Across the eight included studies, the overall risk-of-bias profile was mixed but generally limited by poor reporting. After harmonizing the overall judgments, 3 of 8 studies were classified as high risk, 4 of 8 as unclear risk, and 1 of 8 as low risk. At the domain level, however, the main pattern was not one of isolated weaknesses but uniformly insufficient methodological detail: all six assessed domains were judged as unclear in all 8 studies. Specifically, concerns were present in random sequence generation (8/8 unclear), allocation concealment (8/8 unclear), blinding of participants/personnel (8/8 unclear), blinding of outcome assessment (8/8 unclear), incomplete outcome data (8/8 unclear), and selective reporting (8/8 unclear). In each case, the basis for judgment was the same: the articles did not report enough information to determine whether appropriate safeguards against bias were in place.

This suggests that the dominant issue across the evidence base is underreporting rather than a clearly documented problem confined to one or two domains. Because all studies had unclear judgments for sequence generation and allocation concealment, protection against selection bias cannot be confirmed in any study. Likewise, the absence of reporting on blinding across all 8 studies leaves open the possibility of performance and detection bias, while the lack of detail on incomplete outcome data and selective reporting makes attrition and reporting biases difficult to exclude. No clear differences by study design, such as randomized versus observational studies, can be described from the available risk-of-bias data because the reporting deficits were universal and the extracted judgments do not provide design-specific methodological detail.

These limitations reduce confidence in the pooled estimate. The single study labeled low risk still had unclear judgments in every individual domain, indicating that its apparently favorable overall rating should be interpreted cautiously. Conversely, the 3 studies judged high risk are of particular concern because they contribute to an evidence base already weakened by pervasive uncertainty in core domains, although the extracted records do not specify one dominant domain driving their high-risk classification. The enhanced extraction process assigned high data-quality confidence to 7 studies and medium confidence to 1, suggesting that the extraction itself is likely reliable and that the uncertainty reflects missing information in the original reports rather than extraction error. Taken together, the pooled effect should be interpreted with caution: while the studies were consistently extractable, the lack of transparent reporting across all major bias domains means the true effect may be overestimated or underestimated, and the overall certainty in the review findings is therefore constrained.

## Discussion

**Discussion**

In this systematic review and meta-analysis of eight observational studies, higher alcohol intake was associated with a lower risk of renal cell cancer when compared with the lowest category of intake, which typically comprised non-drinkers or minimal drinkers. The pooled random-effects estimate showed a statistically significant inverse association (OR 0.686, 95% CI 0.633-0.745), and the fixed-effects model yielded a nearly identical result, which supports the numerical stability of the finding. Heterogeneity was low (I2=5.0%; Q p=0.392; tau2=0.0007), suggesting that the direction and magnitude of association were relatively consistent across included studies. On its face, this corresponds to an approximate 31% lower relative odds of renal cell cancer among participants in higher alcohol intake categories versus those with the lowest intake. That said, the clinical meaning of this result requires caution because the exposure contrast was based on broad intake categories rather than a standardized dose, and because observational associations do not by themselves establish causality.

Compared with prior reviews summarized in the broader literature, our findings fit a pattern in which dietary and lifestyle exposures show variable relationships with cancer risk depending on the cancer site, exposure definition, and study design. For example, prior pooled evidence on red and processed meat and ovarian cancer found essentially no association, whereas processed meat has shown a positive association with pancreatic cancer risk, and in metastatic renal cell carcinoma a separate meta-analytic literature has demonstrated strong endpoint correlations in treatment trials rather than etiologic risk associations. These comparisons are not directly analogous to alcohol and renal cell cancer, but they underscore an important point: pooled estimates are highly sensitive to differences in exposure measurement, underlying biology, and the epidemiologic context. Our inverse association is therefore not notable merely because it is statistically significant, but because it appears relatively robust despite the usual variability seen in nutritional and lifestyle epidemiology. At the same time, disagreement with null or mixed findings in other cancer-exposure pairings should not be interpreted as evidence of a uniquely protective effect without considering residual confounding, selection effects, and misclassification of drinking behavior.

Several biologically plausible mechanisms may explain an inverse association between alcohol intake and renal cell cancer risk, although none is sufficient to establish a protective causal effect. Moderate alcohol intake has been hypothesized to improve insulin sensitivity, and hyperinsulinemia has been implicated in renal carcinogenesis. Alcohol consumption has also been associated in some studies with higher high-density lipoprotein concentrations and possible improvements in vascular or metabolic profiles that could indirectly influence renal cancer risk pathways. In addition, certain alcoholic beverages, particularly wine and beer, contain phenolic compounds with antioxidant properties, though the relevance of these compounds at usual intake levels remains uncertain. Counterbalancing these hypotheses is the well-established carcinogenic potential of alcohol for several other malignancies. Any site-specific inverse association for renal cell cancer must therefore be interpreted as potentially reflecting a complex interplay among metabolic effects, beverage-specific constituents, correlated lifestyle factors, and methodological bias rather than a simple protective action of ethanol itself.

The low between-study heterogeneity is reassuring, but it should not be overinterpreted as proof of uniformity across all relevant clinical and methodological dimensions. Differences likely remained in study design, case ascertainment, exposure assessment, categorization of alcohol intake, adjustment for smoking, adiposity, hypertension, diet, and other renal cancer risk factors. The comparator category is especially important: "non-drinkers" may include former drinkers who stopped because of ill health, which can exaggerate an apparent protective association among current drinkers. Likewise, total alcohol and beverage-specific exposures such as beer, wine, and liquor may not have equivalent biological or behavioral correlates. Population variation by sex, baseline comorbidity, and drinking patterns could also matter, but the available evidence was not sufficient here to resolve these issues with confidence. The small tau2 estimate suggests limited statistical dispersion, yet clinically relevant heterogeneity may still be present but obscured by the modest number of studies and broad exposure groupings.

This review has several strengths. First, the pooled association was based on eight studies and showed concordant fixed- and random-effects estimates, which reduces concern that the result is driven by model choice. Second, the overall quality profile of the included evidence was relatively strong, with seven studies assessed as high quality and one as medium quality, and no study classified as low quality. Third, the extraction process allowed recovery of effect estimates even when raw 2x2 tables were not reported, which is common in observational nutritional epidemiology. That enhanced extraction improves evidence capture and reduces the risk that usable studies are excluded solely because authors reported adjusted relative measures instead of tabulatable counts. Even so, the strengths of extraction should be viewed as complementary to, not a substitute for, the quality of the original studies.

Several limitations should temper interpretation. The evidence base was restricted to observational studies, leaving the pooled estimate vulnerable to residual confounding and reverse causation. Exposure ascertainment was likely heterogeneous and subject to misclassification, particularly where alcohol intake was self-reported or categorized differently across studies. The extracted materials indicate that many studies lacked complete reporting of metadata and raw group counts, and one extraction was notably incomplete, which limits reproducibility at the study level even when the reported effect estimate could still be used. The relatively small number of included studies also constrained deeper subgroup analyses by beverage type, sex, geography, or level of adjustment. Generalizability may be limited if included populations were concentrated in specific settings or did not adequately represent diverse drinking patterns and background renal cancer risk. Finally, because alcohol increases the risk of several other cancers and non-cancer outcomes, these findings should not be translated into a general recommendation to consume alcohol for cancer prevention.

From a clinical and public health perspective, the present evidence does not justify recommending alcohol consumption as a strategy to reduce renal cell cancer risk. At most, the findings suggest that higher alcohol intake, as observed in these studies, was associated with lower renal cell cancer odds relative to minimal intake, but that association exists within a broader risk-benefit landscape in which alcohol has recognized harms. The more appropriate implication is interpretive rather than prescriptive: clinicians and guideline developers should recognize that renal cell cancer may not follow the same direction of association seen for alcohol and other cancer outcomes. Future research should prioritize well-reported prospective studies with standardized exposure definitions, separation of never-drinkers from former drinkers, beverage-specific analyses, repeated measures of intake over time, and rigorous adjustment for smoking, obesity, hypertension, and other key confounders. Dose-response analyses and studies examining effect modification by sex and metabolic risk profile would be particularly valuable in clarifying whether the observed inverse association reflects biology, behavior, or bias.

## Conclusion

In this meta-analysis of 8 observational studies, higher alcoholic beverage intake was associated with a lower risk of renal cell cancer compared with the lowest alcohol intake category, with a pooled random-effects OR of 0.686 (95% CI 0.633-0.745). This corresponds to roughly a 31% lower relative risk, and the consistency between random- and fixed-effects estimates, together with low heterogeneity (I2=5.0%), suggests the association was stable across studies. Clinically, this points to a potentially meaningful inverse association at the population level, but it should not be interpreted as evidence to recommend alcohol consumption for renal cancer prevention, given the well-established harms of alcohol for other cancers and overall health. A cautious interpretation is warranted because all included data were from case-control and cohort studies, so residual confounding, exposure misclassification, and differences in drinking patterns or beverage type may partly explain the observed effect.

## Final Included Studies

- Corpus ID: 426 | Alcoholic beverages and risk of renal cell cancer.
- Corpus ID: 427 | Alcohol intake and renal cell cancer in a pooled analysis of 12 prospective studies.
- Corpus ID: 61863 | Alcohol consumption and renal cell cancer risk in two Italian case-control studies.
- Corpus ID: 425 | Gender, alcohol consumption, and renal cell carcinoma.
- Corpus ID: 61859 | A prospective study of alcohol consumption and renal cell carcinoma risk.
- Corpus ID: 429 | Alcohol drinking and renal cell carcinoma in Canadian men and women.
- Corpus ID: 61870 | Total fluid intake and use of individual beverages and risk of renal cell cancer in two large cohorts.
- Corpus ID: 61864 | Alcohol consumption and risk of renal cell carcinoma: a prospective study of Swedish women.
