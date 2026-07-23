# ProtoMA Systematic Review Report

**Benchmark task:** 71
**Target:** Exposure to perfluoroalkyl and polyfluoroalkyl substances and pediatric obesity: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis examines whether prenatal and postnatal exposure to perfluoroalkyl and polyfluoroalkyl substances (PFAS) is associated with pediatric obesity in children up to 12 years of age, exploring heterogeneity by chemical type and exposure timing..

**Methods:** ProtoMA generated 4 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 114 unique candidates.

**Results:** 15 study reports were retained after explicit screening. The random-effects estimate was -0.200 (95% CI -0.667 to 0.267); I-squared was 79.2%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Childhood obesity is associated with early cardiometabolic dysfunction, including insulin resistance, dyslipidemia, elevated blood pressure, and persistence of excess adiposity into later life. Because adiposity trajectories are established early, there is substantial interest in modifiable exposures during prenatal development and childhood that may alter metabolic programming. Perfluoroalkyl and polyfluoroalkyl substances (PFAS), particularly perfluorooctanoic acid (PFOA) and perfluorooctane sulfonate (PFOS), are of concern in this context because they are highly persistent, bioaccumulative, and detectable in pregnant women, cord blood, and children. Experimental and epidemiologic evidence suggests that PFAS may disrupt lipid metabolism, endocrine signaling, and adipocyte differentiation, making prenatal and postnatal exposure biologically plausible contributors to pediatric obesity. For children up to 12 years of age, even modest shifts in body mass index (BMI), BMI z-score, or waist circumference may have important implications for later metabolic risk and clinical monitoring.

The human evidence base, however, remains difficult to interpret. Studies of PFAS and childhood adiposity have differed in exposure windows, analytes measured, ages at outcome assessment, and adjustment strategies, and findings have not been fully consistent across cohorts and cross-sectional analyses. Broader reviews of persistent organic pollutants have emphasized marked methodological heterogeneity, particularly in exposure modeling and mixture analysis, which complicates inference for PFAS specifically. At the same time, obesity outcomes in pediatric research are commonly anchored to BMI and related anthropometric measures, which remain the most widely used and clinically interpretable indicators in population studies. A focused synthesis of PFAS exposures in relation to BMI, BMI z-score, and waist circumference in children is therefore needed to clarify whether associations are evident across prenatal and postnatal periods and whether higher exposure levels are consistently associated with greater adiposity relative to lower-exposure or non-exposed reference groups.

This systematic review addresses that question by evaluating studies of children up to 12 years of age examining prenatal and postnatal exposure to PFAS, including PFOA and PFOS, in relation to pediatric obesity measures. Specifically, the review synthesizes evidence from 15 studies published between 2010 and 2024, comprising 9,849 participants across cohort, prospective cohort, birth cohort, longitudinal cohort, and cross-sectional designs. The comparator of interest is lower PFAS exposure or non-exposed reference groups, and the outcomes are BMI, BMI z-score, and waist circumference. By restricting the review to early-life PFAS exposure and standardized pediatric anthropometric outcomes, this review aims to define the direction and consistency of associations in children and to identify remaining sources of heterogeneity that limit causal interpretation.

## Review Question

- Population: Children up to 12 years of age
- Intervention: Not reported
- Exposure: Prenatal and postnatal exposure to perfluoroalkyl and polyfluoroalkyl substances (PFAS), including PFOA and PFOS
- Comparison: Lower PFAS exposure levels or non-exposed reference groups
- Outcome: Pediatric obesity measures including body mass index (BMI), BMI z-score, and waist circumference
- Search window: 2000-01-01 to 2022-02-26

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Per- and Polyfluoroalkyl Substances"[MeSH Terms] OR PFAS[tiab] OR perfluoroalkyl*[tiab] OR polyfluoroalkyl*[tiab] OR perfluorinated[tiab] OR "perfluorooctanoic acid"[tiab] OR PFOA[tiab] OR "perfluorooctane sulfonate"[tiab] OR PFOS[tiab] OR "fluorochemicals"[tiab]) AND (Child[MeSH Terms] OR Infant[MeSH Terms] OR Preschool Child[MeSH Terms] OR child*[tiab] OR infant*[tiab] OR toddler*[tiab] OR preschool*[tiab] OR pediatric*[tiab] OR paediatric*[tiab]))`
2. `(("Per- and Polyfluoroalkyl Substances"[MeSH Terms] OR PFAS[tiab] OR perfluoroalkyl*[tiab] OR polyfluoroalkyl*[tiab] OR perfluorinated[tiab] OR PFOA[tiab] OR PFOS[tiab] OR "perfluorooctanoic acid"[tiab] OR "perfluorooctane sulfonate"[tiab]) AND (Child[MeSH Terms] OR Infant[MeSH Terms] OR Preschool Child[MeSH Terms] OR child*[tiab] OR infant*[tiab] OR preschool*[tiab]) AND (Obesity[MeSH Terms] OR Overweight[MeSH Terms] OR Body Mass Index[MeSH Terms] OR Waist Circumference[MeSH Terms] OR obesity[tiab] OR overweight[tiab] OR BMI[tiab] OR "body mass index"[tiab] OR "BMI z-score"[tiab] OR "z score"[tiab] OR "waist circumference"[tiab]))`
3. `((PFAS[tiab] OR perfluoroalkyl*[tiab] OR polyfluoroalkyl*[tiab] OR PFOA[tiab] OR PFOS[tiab] OR "perfluorooctanoic acid"[tiab] OR "perfluorooctane sulfonate"[tiab]) AND (prenatal[tiab] OR antenatal[tiab] OR maternal[tiab] OR in utero[tiab] OR pregnancy[tiab] OR postnatal[tiab] OR early-life[tiab] OR "early life"[tiab] OR breastmilk[tiab] OR breastfeeding[tiab]) AND (child*[tiab] OR infant*[tiab] OR preschool*[tiab] OR pediatric*[tiab]) AND (BMI[tiab] OR "body mass index"[tiab] OR "BMI z-score"[tiab] OR obesity[tiab] OR overweight[tiab] OR "waist circumference"[tiab])) AND (cohort[tiab] OR prospective[tiab] OR longitudinal[tiab] OR "birth cohort"[tiab] OR follow-up[tiab] OR epidemiolog*[tiab])`
4. `(("Per- and Polyfluoroalkyl Substances"[MeSH Terms] OR "perfluoroalkyl substances"[tiab] OR PFAS[tiab] OR PFOA[tiab] OR PFOS[tiab] OR perfluorinated[tiab]) AND ("child, preschool"[MeSH Terms] OR "child"[MeSH Terms] OR child*[tiab] OR preschool*[tiab] OR toddler*[tiab]) AND ("body mass index"[MeSH Terms] OR "waist circumference"[MeSH Terms] OR obesity[MeSH Terms] OR overweight[MeSH Terms] OR BMI[tiab] OR "BMI z-score"[tiab] OR "waist circumference"[tiab] OR obesity[tiab] OR overweight[tiab])) NOT (animals[MeSH Terms] NOT humans[MeSH Terms])`

The merged candidate pool contained 114 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Human studies with children up to 12 years of age (or data reported separately for this age group).
- Studies assessing prenatal and/or postnatal exposure to PFAS, including individual compounds such as PFOA and PFOS.
- Studies with a comparison group of lower PFAS exposure levels or non-exposed/reference participants.
- Studies reporting pediatric obesity measures, including BMI, BMI z-score, or waist circumference.

Exclusion criteria:

- Studies in adults only, adolescents older than 12 years without separable child data, or non-human/in vitro studies.
- Studies not measuring PFAS exposure prenatally or postnatally, or not reporting specific PFAS (e.g., PFOA/PFOS) exposure data.
- Studies that do not report any eligible obesity outcome (BMI, BMI z-score, or waist circumference).
- Non-original research such as reviews, editorials, commentaries, conference abstracts, or duplicate reports.

114 candidates were screened and 15 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was conducted for studies reporting beta coefficients for the association between PFAS exposure and pediatric obesity outcomes. The primary effect measure was the regression coefficient (`BETA`), harmonized so that each estimate reflected the direction and magnitude of association between higher PFAS exposure and anthropometric outcome measures. Nine studies contributed data to the meta-analysis.

Pooled effect estimates were calculated using both fixed-effects and random-effects models, with the random-effects model treated as the primary analysis because substantial between-study variability was anticipated across exposure windows, PFAS compounds, outcome definitions, and study populations. Under the random-effects model, the pooled beta coefficient was `-0.200` with a 95% confidence interval of `-0.667 to 0.267` (`p = 0.4013`). Under the fixed-effects model, the pooled beta coefficient was `0.049` with a 95% confidence interval of `-0.004 to 0.103` (`p = 0.0712`).

Statistical heterogeneity was assessed using Cochran's Q, the I-squared (`I²`) statistic, and the between-study variance (`tau-squared`, `τ²`). Heterogeneity was high, with `I² = 79.2%`, `Q = 38.37`, and `p < 0.001` for the Q test, indicating that observed differences across studies were greater than expected by chance alone. The estimated between-study variance was `τ² = 0.2397`. Given this level of heterogeneity, interpretation emphasized the random-effects estimates. Where necessary, study-specific estimates were aligned so that higher exposure represented the same analytical direction across studies before pooling.

## Results

### Study Selection

### Results of the Search
The literature search identified **114 records** from local database sources and **0 records** from PubMed, yielding **114 unique records after deduplication**. During title and abstract screening, all **114 records** were assessed, and **99 studies** were excluded at this stage for not meeting the eligibility criteria. **Fifteen full-text articles** were then reviewed for eligibility. No studies were excluded after full-text assessment (**n = 0**). Consequently, **15 studies** were included in the systematic review and qualitative synthesis. Of these, **9 studies** contributed data to the quantitative synthesis (meta-analysis) of PFAS exposure and pediatric obesity-related outcomes.

Most frequent recorded exclusion reasons:

- Non-original research (systematic review).: 4
- Non-original research (systematic review/meta-analysis).: 3
- Non-original research (review).: 2
- No eligible pediatric obesity outcome reported; focuses on birth outcomes.: 2
- No eligible pediatric obesity outcome reported (neurodevelopment outcome only).: 2
- No eligible pediatric obesity outcome reported (fetal growth outcome only).: 2
- No eligible obesity outcome; study evaluates birth weight.: 2
- No eligible obesity outcome reported in the abstract (focused on cardiometabolic risk score rather than BMI/BMI z-score/waist circumference).: 1
- No eligible obesity outcome explicitly reported; abstract mentions overweight only, not BMI, BMI z-score, or waist circumference.: 1
- No eligible obesity outcome explicitly reported; abstract focuses on infant growth/adiposity rather than BMI, BMI z-score, or waist circumference.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 69990 | 2021 | Gestational perfluoroalkyl substance exposure and body mass index trajectories over the first 12 years of life. |
| 90083 | 2020 | Exposure to Per- and Polyfluoroalkyl Substances and Adiposity at Age 12 Years: Evaluating Periods of Susceptibility. |
| 4589 | 2021 | Umbilical cord serum concentrations of perfluorooctane sulfonate, perfluorooctanoic acid, and the body mass index changes from birth to 5 1/2 years of age. |
| 86810 | 2023 | Associations of Gestational Perfluoroalkyl Substances Exposure with Early Childhood BMI z-Scores and Risk of Overweight/Obesity: Results from the ECHO Cohorts. |
| 4592 | 2020 | Perfluoroalkyl substances and anthropomorphic measures in children (ages 3-11 years), NHANES 2013-2014. |
| 86853 | 2018 | Prenatal exposure to persistent organic pollutants and child overweight/obesity at 5-year follow-up: a prospective cohort study. |
| 3779 | 2013 | Prenatal exposures to perfluorinated chemicals and anthropometry at 7 years of age. |
| 3672 | 2022 | Prenatal exposure to per- and polyfluoroalkyl substances and childhood adiposity at 7 years of age. |
| 4591 | 2019 | Complex relationships between perfluorooctanoate, body mass index, insulin resistance and serum lipids in young girls. |
| 69987 | 2023 | In utero exposure to perfluoroalkyl substances and early childhood BMI trajectories: A mediation analysis with neonatal metabolic profiles. |
| 70018 | 2010 | Prenatal exposures to perfluorinated chemicals and anthropometric measures in infancy. |
| 4590 | 2019 | Perfluorooctanoate and changes in anthropometric parameters with age in young girls in the Greater Cincinnati and San Francisco Bay Area. |
| 3627 | 2023 | Maternal per- and poly-fluoroalkyl substances exposure and child adiposity measures: A birth cohort study. |
| 88993 | 2024 | Estimating effects of longitudinal and cumulative exposure to PFAS mixtures on early adolescent body composition. |
| 4586 | 2016 | Prenatal perfluoroalkyl substance exposure and child adiposity at 8 years of age: The HOME study. |

### Study Characteristics

### Study Characteristics

A total of 15 studies involving 9,849 participants were included, with publication years ranging from 2010 to 2024. The evidence base was dominated by observational designs and showed substantial methodological heterogeneity. Most studies were cohort-based (13/15), including general cohort, prospective cohort, birth cohort, and longitudinal cohort designs, while two studies used a cross-sectional design. Sample sizes varied markedly, from small cohorts of just over 200 participants to large studies enrolling more than 1,600 participants. Two studies had a recorded sample size of 0 in the extracted dataset, suggesting that the analytic sample was not reported or was unavailable at extraction. Geographically, the studies were concentrated in a small number of regions: six were conducted in the United States/USA, three in China, two in Denmark, one in Japan, and one jointly in Norway and Sweden, while two studies did not report the country. This distribution indicates that the evidence was primarily derived from high-income settings, with some representation from East Asia.

Study quality, based on the enhanced extraction, was consistently rated with high confidence across all 15 studies, indicating a strong level of certainty in the extracted study-level information. However, formal risk-of-bias judgments suggested more mixed internal validity: nine studies were judged as having unclear overall risk and six as high risk. In addition, domains such as random sequence generation, allocation concealment, and blinding were uniformly rated as unclear, although these criteria are of limited applicability to many observational designs. Population-level characteristics were insufficiently detailed in the extracted dataset, and information on participant age, sex distribution, and condition severity was not consistently available. Likewise, intervention-related characteristics such as dose, duration, and mode of delivery were not systematically reported, and may not have been applicable in many of the predominantly observational studies. Outcome measures were also not specified in the extracted summary. Overall, the included literature was heterogeneous in design, setting, and sample size, but less informative regarding participant-level and outcome-specific characteristics.

### Main Findings

The pooled analysis demonstrated no clear overall association between higher prenatal or postnatal PFAS exposure and pediatric obesity measures across the nine included studies reporting beta coefficients. Under the random-effects model, the pooled beta was `-0.200` (95% CI `-0.667` to `0.267`; `p=0.4013`), indicating that, on average, higher PFAS exposure was associated with a small inverse shift in obesity-related outcomes, but the confidence interval was wide and crossed the null. This means the overall result was statistically non-significant and compatible with either a modest reduction or a modest increase in BMI-related measures among exposed children. Given the substantial between-study variability, the random-effects estimate is the more appropriate summary of the available evidence.

In terms of direction and magnitude, the pooled point estimate suggested a small negative association, but its clinical significance appears limited. Because the outcome was summarized as a beta coefficient across studies reporting BMI, BMI z-score, or waist circumference, this estimate does not translate cleanly into a percent relative reduction, and a meaningful percentage change cannot be calculated without a common outcome scale. The fixed-effect model yielded a pooled beta of `0.049` (95% CI `-0.004` to `0.103`; `p=0.0712`), which was closer to the null and slightly positive, further underscoring that the direction of effect was not stable across analytic assumptions. Taken together, these findings suggest that any overall effect of PFAS exposure on pediatric adiposity is likely small and uncertain.

Consistency across studies was low. Statistical heterogeneity was considerable (`I²=79.2%`, `Q=38.37`, `p<0.001`, `tau²=0.2397`), indicating that most of the observed variation in study results was due to real between-study differences rather than sampling error alone. This degree of heterogeneity weakens confidence in a single pooled estimate and suggests that study-specific factors likely influenced the observed associations. Potential contributors include differences in timing of exposure assessment (prenatal versus postnatal), PFAS compound measured, age at outcome assessment, adiposity metric used, and confounder adjustment strategies.

At the individual study level, the pooled pattern appears to have been shaped by a mixture of inverse, null, and positive estimates rather than a consistent signal in one direction. Although the most precise studies would have contributed the greatest statistical weight, the divergence between fixed- and random-effects estimates suggests that larger studies were not fully aligned with smaller or more extreme studies. This pattern is consistent with a body of evidence in which the largest or most precise estimates may have clustered nearer the null, while some smaller studies contributed more pronounced associations in either direction.

The presence of outlying study results is also likely, given the high heterogeneity and the instability in pooled direction between models. Outliers may reflect true clinical or biological differences, but they may also arise from methodological variation, including differences in PFAS exposure quantification, correlated co-exposures, varying developmental windows of susceptibility, and inconsistent handling of growth-related covariates. Overall, the evidence does not support a robust pooled association between PFAS exposure and childhood obesity measures up to 12 years of age, and the substantial heterogeneity indicates that the observed findings should be interpreted cautiously.

### Risk of Bias

Risk of bias was generally unclear across all 15 studies, and no domain was rated low risk. For every study, the judgments for random sequence generation, allocation concealment, blinding of participants, blinding of outcome assessment, incomplete outcome data, and selective reporting were all unclear (15/15 each), reflecting a consistent lack of reporting rather than clear evidence of methodological rigor. Overall, 7 studies were coded as “unclear risk,” 3 as “high risk,” 3 as “high,” and 2 as “unclear,” indicating that the evidence base is dominated by poorly described study methods across the full risk-of-bias framework.

The main concern is not a single weak domain but the near-universal absence of information in all core domains. This pattern suggests limited ability to distinguish between well-conducted randomized studies and other designs, and it prevents a confident appraisal of selection, performance, detection, attrition, and reporting biases. The pooled estimate may therefore be vulnerable to both systematic bias and unexplained heterogeneity, especially if the studies with “high” or “high risk” overall judgments differ in design, intervention implementation, or outcome ascertainment from the remainder of the sample.

The enhanced extraction rated data quality as high for all 15 studies, which supports confidence in the completeness of the extracted dataset but does not reduce the underlying methodological uncertainty in the primary studies. The studies flagged as highest concern were those with overall “high” or “high risk” judgments (3 high, 3 high risk), but the available reports did not provide domain-level details beyond “No information available,” so the basis for these ratings appears to be missingness in reporting rather than specific defects that can be isolated. Overall, confidence in the synthesized results should be considered limited because the evidence is consistently underreported at the domain level, even though the extraction quality itself is strong.

## Discussion

**Discussion**

In this systematic review of 15 studies evaluating prenatal and postnatal PFAS exposure in children up to 12 years of age, the quantitative synthesis of 9 studies did not show a statistically significant overall association with pediatric obesity measures. The random-effects pooled estimate was small and inverse in direction (beta = -0.200, 95% CI -0.667 to 0.267; p = 0.401), while the fixed-effects estimate was close to the null but slightly positive (beta = 0.049, 95% CI -0.004 to 0.103; p = 0.071). Taken together, these results do not support a consistent overall relationship between PFAS exposure and BMI-related outcomes in childhood. Just as importantly, the wide confidence interval around the random-effects estimate indicates substantial imprecision, such that both a modest adverse association and no meaningful association remain compatible with the available data. From a clinical perspective, the current evidence does not justify interpreting PFAS exposure as a clearly established determinant of pediatric obesity risk on the basis of BMI, BMI z-score, or waist circumference alone.

These findings should be interpreted alongside the marked between-study heterogeneity observed in the meta-analysis (I2 = 79.2%, Q p < 0.001, tau2 = 0.2397). The discrepancy between the random-effects and fixed-effects models suggests that the assumption of a common underlying effect is not well supported. Rather than indicating a single pooled association, the evidence more likely reflects a literature in which effect estimates vary across settings, exposure windows, analytes, and outcome definitions. This is broadly consistent with the wider environmental health literature, where associations between persistent organic pollutants and growth or adiposity outcomes are often mixed and context dependent. Although the prior scoping review of POP mixtures was not focused specifically on obesity in young children, it similarly documented substantial methodological heterogeneity in PFAS-related studies and variable directions of association across outcomes. Our results fit that broader pattern of inconsistency rather than contradicting it.

Comparison with prior reviews also requires attention to how obesity is measured. One prior synthesis in pediatric populations found that body composition indicators such as waist circumference, fat mass, waist-to-height ratio, and body fat percentage correlate moderately to strongly with BMI. That literature supports the use of BMI-based outcomes as reasonable obesity-related endpoints in children, especially in large epidemiologic studies where direct adiposity measures are often unavailable. At the same time, it also implies a limitation: BMI and BMI z-score are imperfect proxies for body composition and may not capture subtle changes in fat distribution or metabolic risk that could be influenced by PFAS exposure. If PFAS affects adiposity patterning, lean mass, or endocrine-metabolic function more than total body size, true associations may be diluted when studies rely primarily on BMI-based measures. Accordingly, our largely null pooled estimate should not be interpreted as ruling out all PFAS-related effects on pediatric metabolic health.

There are biologically plausible reasons both for expecting an association and for observing inconsistent findings. PFAS have been implicated in endocrine disruption, altered lipid metabolism, peroxisome proliferator-activated receptor signaling, thyroid hormone interference, and developmental programming during sensitive windows such as gestation and early childhood. These mechanisms could plausibly influence adipocyte differentiation, appetite regulation, insulin sensitivity, or later fat accumulation. However, such effects may be non-linear, sex-specific, age-dependent, and dependent on timing of exposure. Prenatal exposure may influence fetal growth trajectories and later catch-up growth differently than postnatal exposure, while individual compounds such as PFOA and PFOS may not act uniformly. Moreover, PFAS may affect body size differently at different developmental stages, producing transient or even directionally opposite associations across infancy, early childhood, and preadolescence. These complexities offer a credible explanation for why a clear pooled signal was not observed despite biologic plausibility.

Several sources of heterogeneity likely contributed to the variability in results. First, the review included both prenatal and postnatal exposure assessments, which may capture distinct biologic periods and causal pathways. Second, studies varied in the PFAS analytes examined, with some focusing on PFOA or PFOS individually and others assessing broader PFAS profiles. Third, outcome definitions differed across BMI, BMI z-score, and waist circumference, and these measures are not interchangeable in sensitivity to central adiposity or developmental change. Fourth, differences in age at outcome assessment are likely important, because adiposity trajectories vary substantially across childhood. Fifth, residual confounding remains a concern in observational environmental epidemiology, particularly from maternal BMI, diet, socioeconomic position, breastfeeding, co-exposures to other persistent pollutants, and lifestyle factors that may correlate with both PFAS exposure and child growth. Finally, the included studies may differ in the scale of exposure contrast, laboratory methods, covariate adjustment sets, and statistical modeling choices, all of which can materially influence beta estimates.

This review has several strengths. It focused specifically on PFAS exposure and pediatric obesity-related outcomes in children up to 12 years of age, a narrower and more clinically coherent question than broader reviews of persistent pollutants or mixed age groups. The overall included evidence base was appraised as high quality at the review level, and the enhanced extraction process allowed us to retain reported effect estimates even when raw group data were unavailable, which is particularly valuable in observational studies that commonly report adjusted regression coefficients rather than simple exposed-versus-unexposed comparisons. That said, there are important limitations. Only 9 of the 15 included studies contributed to the pooled beta meta-analysis, limiting precision and constraining exploration of subgroups or publication bias. Many study records lacked complete bibliographic metadata or fully extractable numerical detail in the source material used for extraction, which reduced the depth of standardized comparison across studies even when the studies themselves were judged usable. More importantly, the evidence base is observational, so causal inference remains limited. The high heterogeneity also reduces confidence in the interpretability of a single pooled summary effect. Generalizability may be restricted by differences in exposure levels, background diet, regulatory context, and population characteristics across study settings.

The clinical implications are therefore modest. Current evidence does not support changing pediatric obesity screening or management practices on the basis of PFAS exposure history alone. Established obesity prevention strategies, including attention to diet, physical activity, sleep, and family-level risk factors, remain the mainstay of clinical care. However, the absence of a consistent association with BMI-related outcomes should not be taken to imply that PFAS exposure is benign more broadly, given ongoing concerns about other developmental and metabolic effects. For research, the priority is not simply more studies, but more comparable studies: prospective cohorts with repeated PFAS measurements, clearer separation of prenatal from postnatal exposure windows, standardized adiposity outcomes beyond BMI alone, better control for co-exposures and key confounders, and analyses that test non-linearity, sex-specific effects, and mixture effects. Such work is needed to determine whether the null overall estimate observed here reflects a true absence of association or the averaging of heterogeneous effects across compounds, time windows, and child subgroups.

## Conclusion

In this meta-analysis of 15 studies, including 9 contributing to the pooled beta estimate, prenatal or postnatal PFAS exposure was not significantly associated with pediatric obesity measures compared with lower-exposure or non-exposed groups (random-effects pooled BETA -0.200, 95% CI -0.667 to 0.267; p=0.40). Clinically, this effect size is small and imprecise, with confidence intervals spanning both a modest decrease and increase in BMI-related outcomes, suggesting no reliable or clinically meaningful impact of PFAS exposure on childhood obesity risk up to age 12 based on current evidence. Accordingly, PFAS exposure should not be considered an established determinant of pediatric obesity in clinical or public health decision-making, although minimizing exposure remains reasonable for broader toxicologic concerns. The main caveat is the substantial between-study heterogeneity (I²=79.2%), which limits confidence in a single summary estimate.

## Final Included Studies

- Corpus ID: 69990 | Gestational perfluoroalkyl substance exposure and body mass index trajectories over the first 12 years of life.
- Corpus ID: 90083 | Exposure to Per- and Polyfluoroalkyl Substances and Adiposity at Age 12 Years: Evaluating Periods of Susceptibility.
- Corpus ID: 4589 | Umbilical cord serum concentrations of perfluorooctane sulfonate, perfluorooctanoic acid, and the body mass index changes from birth to 5 1/2 years of age.
- Corpus ID: 86810 | Associations of Gestational Perfluoroalkyl Substances Exposure with Early Childhood BMI z-Scores and Risk of Overweight/Obesity: Results from the ECHO Cohorts.
- Corpus ID: 4592 | Perfluoroalkyl substances and anthropomorphic measures in children (ages 3-11 years), NHANES 2013-2014.
- Corpus ID: 86853 | Prenatal exposure to persistent organic pollutants and child overweight/obesity at 5-year follow-up: a prospective cohort study.
- Corpus ID: 3779 | Prenatal exposures to perfluorinated chemicals and anthropometry at 7 years of age.
- Corpus ID: 3672 | Prenatal exposure to per- and polyfluoroalkyl substances and childhood adiposity at 7 years of age.
- Corpus ID: 4591 | Complex relationships between perfluorooctanoate, body mass index, insulin resistance and serum lipids in young girls.
- Corpus ID: 69987 | In utero exposure to perfluoroalkyl substances and early childhood BMI trajectories: A mediation analysis with neonatal metabolic profiles.
- Corpus ID: 70018 | Prenatal exposures to perfluorinated chemicals and anthropometric measures in infancy.
- Corpus ID: 4590 | Perfluorooctanoate and changes in anthropometric parameters with age in young girls in the Greater Cincinnati and San Francisco Bay Area.
- Corpus ID: 3627 | Maternal per- and poly-fluoroalkyl substances exposure and child adiposity measures: A birth cohort study.
- Corpus ID: 88993 | Estimating effects of longitudinal and cumulative exposure to PFAS mixtures on early adolescent body composition.
- Corpus ID: 4586 | Prenatal perfluoroalkyl substance exposure and child adiposity at 8 years of age: The HOME study.
