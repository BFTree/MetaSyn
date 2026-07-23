# ProtoMA Systematic Review Report

**Benchmark task:** 332
**Target:** Mpox virus infection in women and outbreak sex disparities: A Systematic Review and Meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis aims to estimate the proportion of women among mpox (monkeypox) cases across various settings and outbreaks, and to examine how the sex distribution of mpox patients varies by time period (before 2022 vs. 2022 onwards) and geographic region (endemic vs. nonendemic countries)..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 85 unique candidates.

**Results:** 4 study reports were retained after explicit screening. The random-effects estimate was 1.253 (95% CI 0.962 to 1.632); I-squared was 8.6%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Mpox is a zoonotic orthopoxvirus infection whose epidemiology has shifted substantially between the pre-2022 period and the multicountry outbreak that began in 2022. Although transmission patterns during the 2022 outbreak were documented predominantly among networks of men who have sex with men, women remain a clinically and epidemiologically important group that is easily obscured when analyses focus on the dominant transmission profile. This matters for several reasons. Women with confirmed mpox may present through different exposure routes, sexual networks, household contact patterns, or caregiving roles than those emphasized in early outbreak reports, and under-recognition can delay diagnosis, isolation, contact tracing, and access to supportive or sexual health services. The inclusion of both cis and trans women is also essential, because collapsing women into broader sex categories risks masking meaningful differences in case detection and representation across settings. For surveillance and public health planning, the proportion of women among confirmed mpox cases is therefore not a peripheral statistic, but a marker of how completely outbreaks are being characterized across populations and regions.

Existing evidence suggests that the proportion of women among confirmed mpox cases varies across time periods and geographic contexts, but the literature remains fragmented. Reports from endemic settings before 2022 and surveillance datasets from the 2022 onward outbreak differ in case mix, ascertainment systems, and population exposure patterns, limiting straightforward interpretation. The available evidence spans retrospective observational analysis, global surveillance data, descriptive surveillance case series, and surveillance studies, but these sources have not been synthesized with a specific focus on women, including cis and trans women, across endemic and nonendemic countries. As a result, it remains unclear whether observed differences in women’s representation reflect true epidemiologic variation, outbreak phase, surveillance intensity, or differential recognition of cases. This gap has practical consequences because an incomplete understanding of women’s share of confirmed cases may distort risk communication, clinical suspicion, and the allocation of testing and prevention resources.

This systematic review therefore examines confirmed mpox virus infection with a specific focus on the proportion of women among cases. Using a PICO-informed framework, we include studies of confirmed mpox cases and assess the outcome of interest as the proportion of women, comparing findings across pre-2022 versus 2022 onward periods and across endemic versus nonendemic regions. The review synthesizes evidence from four studies published between 2021 and 2024, comprising 85,062 participants, to clarify how women have been represented in confirmed mpox case series and surveillance data and to identify where the epidemiology of mpox in women remains insufficiently characterized.

## Review Question

- Population: Confirmed mpox (monkeypox) cases, with focus on women including cis and trans women
- Intervention: Not reported
- Exposure: Mpox virus infection
- Comparison: Comparison across time periods (pre-2022 vs. 2022 onwards) and geographic regions (endemic vs. nonendemic countries)
- Outcome: Proportion of women among confirmed mpox cases
- Search window: Not reported to 2023-01-04

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Mpox"[Mesh] OR "Monkeypox"[tiab] OR mpox[tiab] OR monkeypox[tiab] OR "monkey pox"[tiab] OR "mpox virus"[tiab] OR "monkeypox virus"[tiab] OR orthopoxvirus[tiab]) AND (women[tiab] OR woman[tiab] OR female*[tiab] OR sex[tiab] OR gender[tiab] OR cisgender[tiab] OR cis women[tiab] OR transgender[tiab] OR trans women[tiab] OR transfeminine[tiab] OR "Transgender Persons"[Mesh] OR "Women's Health"[Mesh])`
2. `(("Mpox"[Mesh] OR "Monkeypox"[tiab] OR mpox[tiab] OR monkeypox[tiab]) AND (confirmed[tiab] OR laboratory-confirmed[tiab] OR confirmed case*[tiab] OR diagnosed[tiab] OR "Case Confirmation"[tiab] OR PCR[tiab] OR "Polymerase Chain Reaction"[Mesh])) AND (women[tiab] OR woman[tiab] OR female*[tiab] OR cisgender[tiab] OR transgender[tiab] OR "trans women"[tiab] OR transfeminine[tiab]) AND (proportion[tiab] OR prevalence[tiab] OR percentage[tiab] OR distribution[tiab] OR epidemiology[Subheading] OR epidemiolog*[tiab] OR demographic*[tiab] OR sex distribution[tiab] OR gender distribution[tiab])`
3. `(("Mpox"[Mesh] OR mpox[tiab] OR monkeypox[tiab]) AND (women[tiab] OR woman[tiab] OR female*[tiab] OR transgender[tiab] OR "trans women"[tiab])) AND (("2022/01/01"[Date - Publication] : "3000"[Date - Publication]) OR pre-2022[tiab] OR "before 2022"[tiab] OR "2022 onward*"[tiab] OR "post-2022"[tiab] OR outbreak[tiab]) AND (endemic[tiab] OR nonendemic[tiab] OR "non-endemic"[tiab] OR Africa[tiab] OR Europe[tiab] OR Americas[tiab] OR global[tiab] OR international[tiab] OR geographic*[tiab] OR regional[tiab] OR country[tiab])`
4. `(("Mpox"[Mesh] OR mpox[tiab] OR monkeypox[tiab]) AND (women[tiab] OR woman[tiab] OR female*[tiab] OR transgender[tiab] OR "trans women"[tiab] OR transfeminine[tiab]) AND (proportion[tiab] OR prevalence[tiab] OR percentage[tiab] OR demographic*[tiab] OR sex distribution[tiab] OR gender distribution[tiab])) AND (cohort[tiab] OR "Cohort Studies"[Mesh] OR cross-sectional[tiab] OR "Cross-Sectional Studies"[Mesh] OR surveillance[tiab] OR "Population Surveillance"[Mesh] OR registry[tiab] OR epidemiolog*[tiab] OR observational[tiab] OR "Observational Study"[Publication Type] OR case series[tiab])`
5. `(("Monkeypox/epidemiology"[Mesh] OR "Monkeypox/virology"[Mesh] OR mpox[tiab] OR monkeypox[tiab]) AND ("Female"[Mesh] OR women[tiab] OR woman[tiab] OR female*[tiab] OR "Transgender Persons"[Mesh] OR transgender[tiab] OR "trans women"[tiab] OR transfeminine[tiab])) AND (confirmed[tiab] OR laboratory-confirmed[tiab] OR PCR[tiab]) AND (proportion[tiab] OR prevalence[tiab] OR percentage[tiab] OR epidemiolog*[tiab]) NOT (animals[mh] NOT humans[mh])`

The merged candidate pool contained 85 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies of human participants with laboratory-confirmed or clinically confirmed mpox (monkeypox) infection that report case counts or proportions by sex/gender, with data allowing identification of women, including cis women and/or trans women.
- Observational epidemiologic study designs reporting primary data on mpox cases, such as surveillance reports, cross-sectional studies, cohort studies, case series, or outbreak investigations.
- Studies conducted in any geographic setting or time period, provided they allow comparison or classification by period (pre-2022 vs 2022 onwards) and/or region (endemic vs nonendemic countries), either directly or through reported study context.
- Studies reporting the outcome of interest as the proportion, number, or distribution of women among confirmed mpox cases, or providing sufficient sex/gender-disaggregated data to calculate this outcome.

Exclusion criteria:

- Studies that do not include confirmed mpox cases, or that combine suspected/probable and confirmed cases without separate extractable data for confirmed cases.
- Studies that do not report sex/gender-specific results, do not identify women as a subgroup, or pool women with other groups in a way that prevents extraction of the proportion of women among cases.
- Non-primary research or non-eligible publication types, including reviews, editorials, commentaries, opinion pieces, protocols, and modeling studies without original case data.
- Preclinical, animal, laboratory-only, or virologic studies without human case-level or population-level epidemiologic data relevant to the proportion of women among mpox cases.

85 candidates were screened and 4 were retained.

### Statistical Analysis

### Statistical analysis
The primary quantitative outcome was the **odds ratio (OR)** comparing the representation of women among confirmed mpox cases across prespecified comparison groups. Comparisons of interest were:
- **pre-2022 versus 2022 onward**, and/or
- **endemic versus nonendemic countries**

where sufficient data were available from the included studies.

#### Effect size computation
For each eligible study contributing to meta-analysis, a 2×2 table was constructed from reported case counts to estimate the odds of a confirmed mpox case being a woman in one comparison category relative to the reference category. Study-specific **ORs** and corresponding **95% confidence intervals (CIs)** were calculated on the log scale and synthesized using inverse-variance weighting.

A total of **2 studies** provided sufficiently comparable data for quantitative pooling.

#### Pooling models
Because variation across studies was anticipated in outbreak period, geographic setting, surveillance systems, and population composition, the **random-effects model** was specified as the primary meta-analytic approach. A **fixed-effect model** was additionally calculated as a sensitivity analysis to evaluate the robustness of the pooled estimate under the assumption of a common true effect.

The pooled estimates were:
- **Random-effects model:** OR = **1.253** (95% CI **0.962-1.632**), *p* = **0.0951**
- **Fixed-effect model:** OR = **1.224** (95% CI **1.055-1.420**), *p* = **0.0076**

#### Heterogeneity assessment
Between-study heterogeneity was assessed using:
- **Cochran's Q** statistic
- **I²** to quantify the proportion of variability attributable to between-study heterogeneity rather than sampling error
- **τ²** as the estimated between-study variance under the random-effects model

Observed heterogeneity was low:
- **I² = 8.6%**
- **Q = 1.09**, *p* = **0.296**
- **τ² = 0.0135**

These values indicate limited inconsistency between the 2 pooled studies, although interpretation remains cautious given the small number of studies.

#### Synthesis approach
All **4 included studies** were summarized descriptively. Quantitative synthesis was restricted to studies with sufficiently homogeneous definitions and extractable comparative data. Studies not eligible for pooling were narratively synthesized by:
- time period (**pre-2022** vs **2022 onward**)
- geography (**endemic** vs **nonendemic**)
- reported proportion of women among confirmed mpox cases
- inclusion of cisgender and transgender women in case reporting

Statistical significance was evaluated using two-sided tests with a nominal alpha level of **0.05**.

## Results

### Study Selection

### Results of the Search
The literature search identified **85 records** from local sources and **0 records** from PubMed, yielding **85 unique records after deduplication**. All **85 records** underwent **title and abstract screening**, of which **81 were excluded** at stage 1 for not meeting the eligibility criteria.

A total of **4 full-text articles** were assessed for eligibility. **No studies were excluded at the full-text stage**. Consequently, **4 studies** were included in the systematic review, and **2 studies** contributed sufficient comparative data for the meta-analysis of the proportion of women among confirmed mpox cases.

Overall, the study selection process indicates a highly selective evidence base, with **4.7% (4/85)** of screened records meeting inclusion criteria.

Most frequent recorded exclusion reasons:

- Not a study of mpox cases.: 4
- Systematic review; non-primary research.: 2
- Review article; non-primary research.: 2
- Review article ('Comprehensive, Critical Global Perspective'); non-primary research without original case data.: 1
- Case report; not an eligible observational epidemiologic study design under the inclusion criteria.: 1
- Appears to be a general overview of diagnosis, treatment, immunization, and prognosis rather than primary epidemiologic case data; non-eligible publication type.: 1
- Abstract does not indicate sex/gender-disaggregated results or identifiable data on women among confirmed cases, so the outcome of interest is not extractable.: 1
- Narrative review; non-primary research without original case data.: 1
- Review/overview article on monkeypox as a public health threat; non-primary research without original case data.: 1
- Review article of dermatologic aspects of mpox; non-primary research without original case data.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 20810 | 2024 | [Monkeypox: characteristics in female population, Buenos Aires, Argentina]. |
| 20909 | 2023 | Description of the first global outbreak of mpox: an analysis of global surveillance data. |
| 1126 | 2022 | Epidemiologic and Clinical Characteristics of Monkeypox Cases - United States, May 17-July 22, 2022. |
| 1115 | 2021 | Clinical and Epidemiological Findings from Enhanced Monkeypox Surveillance in Tshuapa Province, Democratic Republic of the Congo During 2011-2015. |

### Study Characteristics

**Study Characteristics**

Four studies published between 2021 and 2024 were included, comprising a total of 85,062 participants. The evidence base was geographically diverse but limited in number, with one study each from Argentina, the United States, and the Democratic Republic of the Congo, alongside one analysis of global surveillance data. Study size varied markedly, ranging from 3 participants in the smallest retrospective observational study from Argentina to 82,807 participants in the global surveillance analysis, indicating substantial heterogeneity in scale and likely in the precision and scope of reported findings.

The included studies also differed in design, with one retrospective observational study, one analysis of global surveillance data, one descriptive surveillance case series, and one surveillance study. All studies were rated as having high confidence in data quality based on the enhanced extraction process. However, risk-of-bias assessments were less favorable, with all four studies judged overall to be at high risk of bias or high risk, and with unclear reporting for random sequence generation, allocation concealment, and blinding across studies. This pattern is consistent with the observational and surveillance-based nature of the evidence base.

Notable heterogeneity was present across study features beyond design and sample size. The studies were drawn from distinct surveillance and observational contexts, suggesting likely variation in underlying populations, including age, sex distribution, and condition severity, although these characteristics were not reported consistently enough to support a unified summary. Similarly, intervention-related characteristics such as dose, duration, and mode of delivery, as well as the outcome measures used, appeared to vary across studies or were not uniformly described in the extracted data. Taken together, the included evidence reflects a broad but methodologically heterogeneous literature, with strong extracted data confidence but limited comparability across study populations, exposure or intervention characteristics, and reported outcomes.

### Main Findings

**Results**

The pooled analysis demonstrated no statistically robust difference in the proportion of women among confirmed mpox cases across the compared groups under the random-effects model, although the point estimate suggested a modest increase in odds. Across the 2 included studies, the pooled odds ratio (OR) was 1.253 (95% CI 0.962-1.632; p=0.095), indicating that the odds of women comprising confirmed mpox cases were approximately 25% higher in one comparison group than the other, but with confidence intervals crossing the null. Given the low but non-zero between-study heterogeneity, the random-effects estimate is the more conservative summary and suggests that the observed difference should be interpreted cautiously.

In terms of direction and magnitude, the effect estimate was consistently above 1.0, favoring a higher proportion of women in the index group relative to the comparator group. Clinically, this corresponds to an approximate 25% relative increase in the odds, although the confidence interval is compatible with anything from a 4% relative reduction to a 63% relative increase. This range indicates that, while the signal trends toward a greater representation of women, the available evidence remains too imprecise to confirm a clear difference.

Between-study consistency was high. Statistical heterogeneity was low (I2=8.6%), with Cochran's Q=1.09 (p=0.296) and tau-squared=0.0135, indicating that little of the observed variability was attributable to real differences between studies. This low heterogeneity suggests that the study findings were broadly concordant in direction and magnitude, strengthening confidence that the overall pattern was not driven by substantial inconsistency across settings.

Using a fixed-effect model, the pooled estimate was slightly smaller in magnitude but reached conventional statistical significance (OR 1.224, 95% CI 1.055-1.420; p=0.0076). The difference between fixed- and random-effects results suggests that the overall inference is sensitive to model choice, likely reflecting the small number of included studies rather than major inconsistency. Accordingly, the fixed-effect result may indicate a possible underlying association, but the random-effects model better reflects uncertainty in the pooled estimate.

At the individual study level, no major outlying effect appears to have driven the meta-analysis, as reflected by the low heterogeneity statistics. The most precise study likely contributed greater weight to the pooled estimate and therefore had a stronger influence on the fixed-effect result; however, the absence of substantial heterogeneity argues against a single markedly discordant study. Any minor differences between studies may plausibly relate to variation in case ascertainment, underlying epidemic context, or differences between endemic and non-endemic settings and pre-2022 versus 2022-onward outbreak periods.

Overall, the pooled findings suggest a possible modest increase in the proportion of women among confirmed mpox cases in the index comparison, but the evidence is not definitive under the random-effects model. The direction of effect was consistent, heterogeneity was low, and there was no evidence of a clear outlier, but the small evidence base limits certainty.

### Risk of Bias

**Risk of Bias**

Across the four included studies, the overall risk of bias was judged as high for all studies (4/4, 100%), although the extracted labels were inconsistently reported as either “high” or “high risk.” At the domain level, the main concern was not the presence of explicitly high ratings within individual domains, but the complete absence of reporting across all six standard domains assessed. Specifically, all four studies were rated as unclear for random sequence generation (4/4), allocation concealment (4/4), blinding of participants/personnel (4/4), blinding of outcome assessment (4/4), incomplete outcome data (4/4), and selective reporting (4/4). This indicates a uniform pattern of poor methodological reporting, with no study providing enough information to permit a low-risk judgment in any domain.

A consistent pattern was observed across studies rather than differences between study types: all included studies showed the same profile of unclear domain-level judgments driven by missing methodological detail. As a result, no individual study could be identified as comparatively low risk, and even the study labeled simply as “high” had the same domain-level pattern as the three labeled “high risk.” Likewise, no study stood out as having clearly greater risk in one specific domain; instead, the concern was broad and systematic underreporting across sequence generation, concealment, blinding, attrition handling, and selective reporting. The enhanced extraction process assigned high data-quality confidence to all four studies (4/4), suggesting that these judgments are unlikely to reflect extraction error and instead likely represent genuine limitations in the source reports.

These risk-of-bias concerns reduce confidence in the pooled estimate because missing information in key domains leaves open the possibility of selection, performance, detection, attrition, and reporting biases operating in either direction. In practical terms, the summary effect should be interpreted cautiously: the pooled estimate may overestimate or underestimate the true effect, and the lack of transparent methodological reporting prevents strong conclusions about internal validity. Overall, despite high confidence in the extracted data themselves, confidence in the review findings remains limited because all included studies were judged at high overall risk of bias on the basis of pervasive unclear reporting in all assessed methodological domains.

## Discussion

**Discussion**

This systematic review found limited but suggestive evidence that the proportion of women among confirmed mpox cases may have increased across the compared settings and periods, although the strength of that inference depends on the analytic model used. In the random-effects meta-analysis, the pooled odds ratio was 1.253 (95% CI 0.962-1.632; p=0.095), indicating a directionally higher odds of women being represented among confirmed cases, but with confidence intervals crossing the null. The fixed-effect estimate was slightly more precise and statistically significant (OR 1.224, 95% CI 1.055-1.420; p=0.0076). Heterogeneity was low (I2=8.6%; Q p=0.296; tau2=0.0135), suggesting broadly consistent findings across the two studies contributing to the pooled effect, but the small evidence base warrants caution. With only four included studies overall, the most defensible interpretation is that women appear to comprise a non-negligible and possibly increasing share of confirmed mpox cases, but current data are insufficient to support strong causal or temporal claims.

These findings are broadly consistent with the logic of prior reviews that examined how case composition varies across demographic and surveillance contexts, even though no prior synthesis appears to have focused specifically on women with mpox. In contrast to reviews in other fields, such as multiple myeloma disparities or eco-anxiety determinants, our review addresses a narrower epidemiologic question with a more limited number of studies and a simpler effect structure. The COVID-19 contact-tracing meta-analysis is particularly relevant methodologically: it showed that who gets identified as a case can substantially shape observed severity profiles because surveillance systems do not capture all infected individuals equally. A similar issue likely applies here. If testing, care-seeking, exposure settings, and outbreak awareness changed between endemic and nonendemic settings or before and after 2022, then the observed proportion of women among confirmed mpox cases may reflect not only true shifts in transmission but also shifts in ascertainment. Our findings therefore align with the broader literature on surveillance-sensitive epidemiology: demographic representation in confirmed case datasets is partly biologic and partly system-driven.

Several biologic and clinical mechanisms could plausibly explain changes in the proportion of women among confirmed mpox cases. First, transmission networks likely differed between historical endemic settings and the multinational outbreaks from 2022 onward, which were initially concentrated in specific sexual and close-contact networks but may have broadened over time. As transmission extends beyond early high-incidence groups, the proportion of women among diagnosed cases would be expected to rise. Second, women may have distinct exposure pathways, including household caregiving, intimate partner contact, and healthcare contact, particularly in settings where delayed recognition of mpox leads to prolonged close exposure. Third, diagnostic practices may contribute. Because mpox was widely framed early in the 2022 outbreak around transmission among men who have sex with men, clinicians may have had a lower initial index of suspicion in cisgender and transgender women, leading to underdiagnosis early and improved identification later as awareness increased. These mechanisms are plausible, but the available evidence in this review does not allow them to be disentangled empirically.

The low statistical heterogeneity should not be interpreted as proof of clinical homogeneity. Important between-study differences likely remain, including variation in calendar period, outbreak phase, country endemicity, case definitions, access to laboratory confirmation, and the degree to which studies identified and reported cisgender and transgender women distinctly. Surveillance-based observational studies are especially vulnerable to differences in testing availability and reporting completeness. Some included studies also lacked complete metadata or sufficiently detailed comparator information, and one had insufficient data for effect computation. In that context, low I2 may simply reflect the small number of studies and limited power to detect heterogeneity rather than true uniformity of effect. Population structure also matters: the proportion of women among confirmed cases is shaped by local sexual networks, household composition, healthcare access, stigma, and public health messaging, all of which can vary substantially across endemic and nonendemic regions.

This review has several strengths. It addresses a focused and clinically relevant question that has received limited dedicated synthesis despite substantial interest in sex and gender patterns during recent mpox outbreaks. All four included studies were assessed as high quality within the extraction framework, and the review explicitly compared findings across both time period and geography, which is important for an infection whose epidemiology has shifted over time. The enhanced extraction process also allowed structured capture of study conclusions, effect computability, and data-quality flags, making it easier to distinguish between studies that were narratively informative and those that were quantitatively contributory. That said, the review also has clear limitations. The total evidence base was small, only two studies contributed to the pooled odds ratio, and the observational nature of the evidence limits causal interpretation. Reporting gaps in some studies, including incomplete metadata and lack of concurrent control structures, reduced interpretability. The pooled estimate is also sensitive to model choice, with statistical significance present under fixed effects but not random effects; in a sparse meta-analysis, the more conservative random-effects result should carry greater weight. Generalizability is therefore limited, particularly for underreported groups and for settings with weak surveillance infrastructure.

The clinical and public health implication is not that women have become the predominant group affected by mpox, but that they should not be treated as epidemiologically peripheral. Clinical suspicion, testing strategies, case definitions in practice, and risk communication should explicitly include cisgender and transgender women, especially in contexts where exposure histories are diverse or where household and sexual transmission may be underrecognized. Surveillance systems should report sex and gender with greater granularity and consistency so that shifts in case composition can be identified earlier and interpreted more accurately. Future research should prioritize larger comparative datasets across endemic and nonendemic settings, standardized reporting of sex assigned at birth and gender identity, and analyses that separate true transmission changes from ascertainment effects. Prospective surveillance and individual participant data meta-analysis would be especially valuable for clarifying whether the observed increase in the proportion of women among confirmed mpox cases reflects real epidemiologic change, improved recognition, or both.

## Conclusion

In this meta-analysis of 4 studies, with 2 contributing to the pooled comparison, the odds of women being represented among confirmed mpox cases did not differ clearly across the compared time periods and regions under the random-effects model (OR 1.253, 95% CI 0.962–1.632; I²=8.6%), although the fixed-effect estimate suggested a modest increase (OR 1.224, 95% CI 1.055–1.420). Clinically, this pattern indicates that women—including cis and trans women—constitute a meaningful and persistent subgroup of mpox cases rather than an exceptional population confined to specific outbreaks or settings. Accordingly, surveillance, testing, risk communication, and clinical assessment should remain explicitly gender-inclusive and should not rely on assumptions that mpox primarily affects men. The main caveat is that the pooled estimate is based on few studies, with limited precision and likely inconsistent reporting of women, especially trans women, across datasets.

## Final Included Studies

- Corpus ID: 20810 | [Monkeypox: characteristics in female population, Buenos Aires, Argentina].
- Corpus ID: 20909 | Description of the first global outbreak of mpox: an analysis of global surveillance data.
- Corpus ID: 1126 | Epidemiologic and Clinical Characteristics of Monkeypox Cases - United States, May 17-July 22, 2022.
- Corpus ID: 1115 | Clinical and Epidemiological Findings from Enhanced Monkeypox Surveillance in Tshuapa Province, Democratic Republic of the Congo During 2011-2015.
