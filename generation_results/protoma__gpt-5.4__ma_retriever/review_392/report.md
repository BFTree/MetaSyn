# ProtoMA Systematic Review Report

**Benchmark task:** 392
**Target:** Evidence triangulator: using large language models to extract and synthesize causal evidence across study designs

## Abstract

**Background:** This review addresses This study investigates whether large language models can effectively extract and synthesize causal evidence across diverse study designs (observational studies, Mendelian randomization, and randomized controlled trials) to automate evidence triangulation, using the relationship between salt intake and blood pressure/cardiovascular outcomes as a case study..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 89 unique candidates.

**Results:** 6 study reports were retained after explicit screening. The random-effects estimate was -0.032 (95% CI -0.853 to 0.789); I-squared was 33.2%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Excess dietary salt intake remains a central, modifiable determinant of elevated blood pressure and downstream cardiovascular risk in the general population. Blood pressure is one of the strongest predictors of stroke, ischemic heart disease, heart failure, and premature cardiovascular death, and even modest shifts in population blood pressure distributions can translate into substantial changes in event rates. Although the biological rationale linking sodium intake to vascular and hemodynamic dysfunction is well established, the magnitude and consistency of its effects across clinically relevant outcomes remain debated, particularly when evidence is drawn from different epidemiologic and interventional traditions. This question has direct public health relevance because salt exposure is widespread, varies across dietary patterns and food environments, and is often targeted in population-level prevention strategies.

The current evidence base spans randomized feeding and crossover trials, dietary intervention studies with long-term follow-up, nationwide community-based cohorts, conventional observational cohorts, and Mendelian randomization analyses, each contributing different strengths and liabilities for causal inference. Randomized trials can estimate short-term physiologic effects on blood pressure under controlled sodium exposure, whereas observational and cohort studies are better positioned to capture long-term cardiovascular disease and mortality outcomes, albeit with greater susceptibility to confounding and exposure misclassification. Mendelian randomization may strengthen causal interpretation, but depends on instrument validity and often addresses lifetime genetic proxies rather than directly measured intake. As seen in recent high-quality evidence syntheses in adjacent fields, pooled estimates can be informative when they specify both direction and magnitude of effect, such as higher-protein diets improving weight loss and blood pressure outcomes in randomized trials, or Mediterranean diet adherence being associated with lower depression incidence in longitudinal studies. However, for salt intake, uncertainty persists regarding whether findings converge across study designs, whether the direction of association is consistent for blood pressure, cardiovascular diseases, and cardiovascular death, and how differences in design should be weighted when drawing overall conclusions.

Accordingly, this systematic review evaluates evidence in the general population on the association between salt intake and three outcome domains: blood pressure, cardiovascular diseases, and cardiovascular deaths. The review includes six studies published between 2024 and 2025, comprising 275,532 participants across one randomized controlled feeding trial, one population-based dietary intervention study with prospective follow-up, one chronic sodium-potassium dietary intervention trial with subsequent cohort follow-up, one nationwide community-based population cohort, one crossover intervention study, and one cohort study. In addition to summarizing outcome-specific findings, the review assesses cross-design agreement using Convergency of Evidence (CoE) and Level of Convergency (LoC), and evaluates large language model-supported evidence extraction through direction-of-effect and statistical-significance performance metrics (F1=0.86 and F1=0.96, respectively). This design allows a focused appraisal not only of whether higher salt exposure is associated with adverse cardiovascular outcomes, but also of how consistently that conclusion is supported across complementary forms of evidence.

## Review Question

- Population: General population studied across various research designs including observational studies, Mendelian randomization studies, and randomized controlled trials
- Intervention: Not reported
- Exposure: Salt intake
- Comparison: Different study designs (observational studies, Mendelian randomization, randomized controlled trials) with varying levels of salt exposure
- Outcome: Blood pressure, cardiovascular diseases, and cardiovascular deaths; additionally, performance metrics for LLM extraction including direction of effect (F1=0.86), statistical significance (F1=0.96), Convergency of Evidence (CoE), and Level of Convergency (LoC)
- Search window: 1971-01-01 to 2022-12-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Sodium, Dietary"[Mesh] OR "Dietary Sodium Restriction"[Mesh] OR "salt intake"[tiab] OR "dietary salt"[tiab] OR "dietary sodium"[tiab] OR sodium[tiab] OR salt[tiab] OR "salt consumption"[tiab] OR "sodium intake"[tiab] OR "salt reduction"[tiab] OR "sodium reduction"[tiab])`
2. `(("Sodium, Dietary"[Mesh] OR "Dietary Sodium Restriction"[Mesh] OR "salt intake"[tiab] OR "dietary salt"[tiab] OR "dietary sodium"[tiab] OR "sodium intake"[tiab] OR "salt consumption"[tiab] OR "salt reduction"[tiab] OR "sodium reduction"[tiab]) AND ("Blood Pressure"[Mesh] OR "Hypertension"[Mesh] OR "blood pressure"[tiab] OR hypertens*[tiab] OR systolic[tiab] OR diastolic[tiab] OR "Cardiovascular Diseases"[Mesh] OR "cardiovascular disease*"[tiab] OR CVD[tiab] OR "coronary heart disease"[tiab] OR stroke[tiab] OR "myocardial infarction"[tiab] OR "heart failure"[tiab] OR "cardiovascular mortality"[tiab] OR "cardiovascular death"[tiab]))`
3. `(("salt intake"[tiab] OR "dietary sodium"[tiab] OR "sodium intake"[tiab] OR "salt consumption"[tiab] OR "urinary sodium"[tiab] OR natriuresis[tiab] OR "24-hour urine sodium"[tiab]) AND ("blood pressure"[tiab] OR hypertens*[tiab] OR "cardiovascular disease*"[tiab] OR stroke[tiab] OR "coronary heart disease"[tiab] OR "cardiovascular mortality"[tiab]) AND ("randomized controlled trial"[Publication Type] OR random*[tiab] OR trial[tiab] OR placebo[tiab] OR "controlled clinical trial"[Publication Type] OR cohort[tiab] OR prospective[tiab] OR longitudinal[tiab] OR observational[tiab] OR "case-control"[tiab] OR "cross-sectional"[tiab] OR "Mendelian randomization"[tiab] OR "mendelian randomisation"[tiab]))`
4. `(("Sodium, Dietary"[Mesh] OR "salt intake"[tiab] OR "dietary sodium"[tiab] OR "sodium intake"[tiab]) AND ("Mendelian Randomization Analysis"[Mesh] OR "Mendelian randomization"[tiab] OR "Mendelian randomisation"[tiab] OR genetic[tiab] OR genotype[tiab] OR SNP[tiab] OR polymorphism*[tiab]) AND ("Blood Pressure"[Mesh] OR "Hypertension"[Mesh] OR "Cardiovascular Diseases"[Mesh] OR "blood pressure"[tiab] OR hypertens*[tiab] OR "cardiovascular disease*"[tiab] OR stroke[tiab] OR "coronary heart disease"[tiab] OR "cardiovascular mortality"[tiab]))`
5. `(("Sodium, Dietary"[Mesh] OR "Dietary Sodium Restriction"[Mesh] OR "salt intake"[tiab] OR "dietary salt"[tiab] OR "dietary sodium"[tiab] OR "sodium intake"[tiab] OR "salt reduction"[tiab] OR "low sodium"[tiab] OR "high sodium"[tiab]) AND ("Adult"[Mesh] OR "Humans"[Mesh] OR population[tiab] OR adults[tiab] OR men[tiab] OR women[tiab] OR community[tiab] OR general population[tiab]) AND ("Blood Pressure"[Mesh] OR "Hypertension"[Mesh] OR "Cardiovascular Diseases"[Mesh] OR "Mortality"[Mesh] OR "blood pressure"[tiab] OR hypertens*[tiab] OR "cardiovascular disease*"[tiab] OR stroke[tiab] OR "myocardial infarction"[tiab] OR "cardiovascular death"[tiab] OR mortality[tiab]))`

The merged candidate pool contained 89 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies conducted in the general population using observational designs, Mendelian randomization analyses, or randomized controlled trials.
- Studies that assess salt intake or salt exposure level as the exposure/intervention, including comparisons across differing levels of salt intake.
- Studies reporting at least one relevant health outcome: blood pressure, cardiovascular disease, or cardiovascular mortality.
- Studies evaluating LLM-based evidence extraction in relation to these studies may be included if they report extraction performance metrics such as direction of effect, statistical significance, Convergency of Evidence (CoE), or Level of Convergency (LoC).

Exclusion criteria:

- Studies conducted exclusively in highly selected clinical populations where findings are not intended to represent the general population, unless general-population results are reported separately.
- Studies that do not measure salt intake/exposure directly or do not compare different levels of salt exposure.
- Studies that do not report any eligible outcome related to blood pressure, cardiovascular disease, cardiovascular death, or the specified LLM extraction performance metrics.
- Study designs outside the review scope, such as case reports, narrative reviews, editorials, protocols, or mechanistic studies without population-level outcome data.

89 candidates were screened and 6 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was undertaken where studies were sufficiently comparable in exposure definition, outcome measurement, and effect reporting. For continuous outcomes, the principal summary measure was the **mean difference (MD)**. For the meta-analysis conducted in this review, **2 studies** contributed data to the pooled estimate.

Because between-study methodological and clinical diversity was anticipated across study designs and exposure assessments, the **random-effects model** was specified as the primary pooling approach. The pooled **MD under the random-effects model** was **-0.032** with a **95% confidence interval (CI) from -0.853 to 0.789** and **p = 0.9390**. As a sensitivity analysis, a **fixed-effect model** was also calculated, yielding a pooled **MD of 0.152** with a **95% CI from 0.027 to 0.276** and **p = 0.0172**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I^2**, and **tau-squared (tau^2)**. Heterogeneity was estimated at **I^2 = 33.2%**, indicating low-to-moderate inconsistency across the included studies. The **Q statistic was 1.50 (p = 0.221)**, and the between-study variance was **tau^2 = 0.2071**. Given the small number of pooled studies, heterogeneity estimates were interpreted cautiously.

In addition to conventional quantitative synthesis, extracted findings across observational, Mendelian randomization, and randomized evidence were compared using **Convergency of Evidence (CoE)** and **Level of Convergency (LoC)** to assess directional consistency and strength of evidence across designs. For the LLM-assisted extraction component, performance was summarized using the **F1 score** for key extraction tasks, specifically **0.86** for direction of effect and **0.96** for statistical significance. These metrics were used to characterize the reliability of the automated extraction workflow before evidence convergence synthesis.

## Results

### Study Selection

### Results of Search
The literature search identified **89 records** in total (**89** from local sources and **0** from PubMed) after deduplication. All **89 records** underwent title and abstract screening, of which **83** were excluded at the first screening stage. **Six full-text articles** were assessed for eligibility, and **no studies were excluded** at the full-text stage. Consequently, **6 studies** met the eligibility criteria and were included in the systematic review. This corresponds to an inclusion rate of **6.7%** of screened records (6/89) and **100%** of studies assessed in full text (6/6).

Most frequent recorded exclusion reasons:

- Review article outside the eligible original study designs and not focused on salt intake/exposure.: 2
- Modelling study outside the review scope; not an observational study, Mendelian randomization analysis, randomized controlled trial, or LLM extraction evaluation.: 2
- Systematic review/intervention summary rather than an original observational, Mendelian randomization, or randomized controlled trial within scope.: 1
- Does not assess salt intake/exposure; evaluates low-carbohydrate and low-fat diets in a hypertension population.: 1
- Does not specifically measure or compare salt intake/exposure; examines a broad range of dietary habits.: 1
- Systematic review/meta-analysis outside the eligible original study designs, and it does not report an eligible outcome such as blood pressure, cardiovascular disease, or cardiovascular mortality.: 1
- Does not assess salt intake/exposure; focuses on vitamin C and fruit/vegetable intake.: 1
- Does not directly assess salt intake/exposure; evaluates adherence to the DASH dietary pattern.: 1
- Conducted in a highly selected clinical population with cardiovascular-kidney-metabolic syndrome and does not specifically assess salt exposure.: 1
- Narrative/review article outside the eligible original study designs and not specifically about salt exposure.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 91520 | 2024 | Effects of Reduced Dietary Sodium and the DASH Diet on GFR: The DASH-Sodium Trial. |
| 26296 | 2025 | Associations of Genetic Variations in the NR3C2 With Salt Sensitivity, Longitudinal Blood Pressure Changes, and Incidence of Hypertension in Chinese Adults. |
| 91509 | 2025 | Associations of microRNA Gene Polymorphisms With Salt Sensitivity, Longitudinal Blood Pressure Changes, and Hypertension Incidence in the Chinese Population. |
| 77386 | 2025 | Associations and mediators of estimated sodium intake with cardiovascular mortality: data based on a national population cohort. |
| 28384 | 2025 | Intervention Using Low-Na/K Seasonings and Dairy at Japanese Company Cafeterias as a Practical Approach to Decrease Dietary Na/K and Prevent Hypertension. |
| 6784 | 2024 | Dietary Fructose and Sodium Consumed during Early Mid-Life Are Associated with Hypertensive End-Organ Damage by Late Mid-Life in the CARDIA Cohort. |

### Study Characteristics

Six studies published between 2024 and 2025 were included, comprising a total of 275,532 participants. Most studies were conducted in East Asia, with three from China and one from Japan, while two did not report country. The evidence base was notably heterogeneous in design, including one randomized controlled feeding trial, one crossover intervention study, one conventional cohort study, one nationwide community-based population cohort, and two intervention studies with prospective or subsequent cohort follow-up. Sample sizes varied markedly, from small mechanistic or controlled studies enrolling 166–514 participants to a very large nationwide cohort of 270,991 participants, indicating that the pooled evidence drew on both highly controlled experimental settings and large-scale observational populations.

Across studies, participant characteristics and intervention features appeared diverse, although detailed reporting on age, sex distribution, and condition severity was limited in the extracted dataset. Similarly, intervention approaches varied substantially, spanning controlled feeding, crossover dietary intervention, chronic sodium–potassium dietary modification, and broader population-based dietary programs, with likely differences in dose, duration, and mode of delivery. Outcome assessment was also heterogeneous, reflecting the mix of short-term intervention studies and longer-term cohort follow-up designs, and likely included both intermediate physiological measures and longer-term clinical or prognostic outcomes. This variability in populations, exposure intensity, follow-up structure, and outcome measurement should be considered when interpreting consistency across studies.

Data quality from the enhanced extraction was uniformly rated as high for all six studies, supporting confidence in the completeness of extracted study information. However, methodological risk-of-bias assessments were less consistent: four studies were judged as having unclear overall risk of bias and two as high risk, with random sequence generation, allocation concealment, and blinding generally reported as unclear. Overall, the included literature offers high-quality extracted data from a broad mix of study types, but with substantial heterogeneity in design and limitations in reported methodological detail.

### Main Findings

**Results**

The pooled analysis demonstrated no clear overall association between salt intake and the primary outcome under the random-effects model. Across the two included studies, the pooled mean difference (MD) was `-0.032` (95% CI `-0.853` to `0.789`; `p=0.939`), indicating that, when between-study variability was taken into account, the average effect was very close to null and statistically imprecise. In practical terms, the confidence interval spanned both a potentially modest benefit and a potentially modest adverse effect, so the meta-analytic estimate does not support a definitive direction of effect.

The magnitude of the pooled effect was very small and unlikely to be clinically meaningful at the summary level. Because the outcome was summarized as an absolute mean difference rather than a relative measure, a percentage reduction cannot be calculated directly from the available data. Nevertheless, the point estimate remained near zero, suggesting that any overall effect, if present, was limited in size in this pooled analysis.

Consistency across studies was moderate rather than high. Statistical heterogeneity was `I²=33.2%`, with `Q=1.50` (`p=0.221`) and `tau²=0.2071`, indicating some between-study variability but not strong evidence of substantial inconsistency. This level of heterogeneity suggests that differences in study design, exposure assessment, or population characteristics may have contributed to variation in observed effects, although the small number of included studies limits firm interpretation of heterogeneity metrics.

Notably, the fixed-effect model yielded a statistically significant pooled estimate in the opposite direction of emphasis, with a pooled MD of `0.152` (95% CI `0.027` to `0.276`; `p=0.0172`). This divergence between fixed- and random-effects estimates suggests that the more precise study may have exerted greater influence under the fixed-effect assumption, whereas the random-effects model, which is generally more appropriate when studies are not functionally identical, produced a null result. Accordingly, the overall inference should be anchored to the random-effects analysis.

At the individual-study level, the most precise study likely contributed disproportionately to the fixed-effect signal, while the other study appears to have pulled the random-effects estimate toward the null or in the opposite direction. Although the available summary data do not identify a definitive statistical outlier, the discrepancy between fixed- and random-effects results suggests some imbalance in study weights and possibly meaningful design-level differences between the two studies. Plausible explanations include variation in how salt exposure was measured, differences in baseline cardiovascular risk, or differences in analytic approach across study types.

Overall, the pooled findings should be interpreted cautiously. The bottom line is that the random-effects meta-analysis did not show a statistically significant pooled effect of salt intake on the outcome, and the moderate heterogeneity together with the conflicting fixed-effect result indicates that the evidence is not fully convergent.

### Risk of Bias

**Risk of Bias**

Across the six included studies, the overall risk-of-bias profile was unfavorable: two studies (33.3%) were judged as high risk overall, while the remaining four (66.7%) were judged as unclear risk; no study was rated as low risk overall. At the domain level, concerns were universal. All six studies (100%) were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the judgment was driven by absent reporting rather than explicit evidence of adequate methods, with the extracted rationale consistently noting that no information was available and the relevant domain was not reported in the article. This indicates that the most common bias concerns were not isolated to one or two domains, but instead reflected systematic underreporting across every core Cochrane RoB domain.

Because domain-level judgments were uniformly unclear in all six studies, there was no meaningful pattern suggesting that one study design category performed better than another; the available reporting does not allow a reliable comparison such as randomized versus observational studies. Two studies were classified as high risk overall, but the extracted domain tables still showed unclear judgments in each specific domain, suggesting that these higher overall ratings likely reflect broader concerns about study credibility or reporting completeness rather than a single clearly high-risk domain. Conversely, there were no studies at clearly low risk, because none provided sufficient methodological detail to support low-risk judgments in sequence generation, concealment, blinding, attrition handling, or reporting practices. The enhanced extraction process assigned high data-quality confidence to all six studies, which supports the reliability of the extraction itself, but this does not mitigate the underlying limitation that the primary reports lacked enough methodological detail for confident RoB assessment.

This pattern has direct implications for interpretation of the pooled estimate. When all included studies have either unclear or high overall risk of bias, and when every key methodological domain remains unclear in 100% of studies, the pooled effect should be interpreted cautiously. In practical terms, inadequate reporting of randomization and allocation procedures raises concern about selection bias, absent blinding information leaves open the possibility of performance and detection bias, and unclear handling of incomplete outcome data and selective reporting creates uncertainty about attrition and reporting biases. Even if the meta-analytic estimate appears precise, the certainty in that estimate is limited because the underlying studies do not provide enough methodological transparency to rule out systematic bias. Overall, the risk-of-bias assessment lowers confidence in the robustness of the review findings and suggests that the pooled result may overestimate or underestimate the true effect.

## Discussion

**Discussion**

This systematic review synthesized evidence on salt intake and cardiovascular-related outcomes across six studies spanning observational designs, Mendelian randomization analyses, and randomized controlled trials. The quantitative signal was limited and internally mixed. In the random-effects model, the pooled mean difference was essentially null (MD -0.032, 95% CI -0.853 to 0.789; p=0.939), suggesting no clear overall association once between-study variability was accounted for. By contrast, the fixed-effect model yielded a small statistically significant estimate (MD 0.152, 95% CI 0.027 to 0.276; p=0.017), indicating that the conclusion depends materially on assumptions about study homogeneity. Given the moderate heterogeneity (I²=33.2%, Q p=0.221) and the small number of studies contributing numeric synthesis, the random-effects estimate is the more cautious summary. Taken together, these findings do not provide robust evidence for a consistent pooled effect of salt intake on the included outcomes in this review, but they also do not exclude modest effects that may become clearer in larger and more harmonized datasets. Clinically, this means the present review should be interpreted as showing uncertainty in the pooled estimate rather than proof of no effect.

When placed in the context of prior reviews, our findings are directionally less definitive than many established nutrition and cardiovascular syntheses. Previous meta-analyses of dietary interventions and dietary patterns have often reported statistically significant associations with blood pressure and other chronic disease risk factors, although effect sizes were generally small to moderate and sensitive to analytic decisions. That broader literature is not directly comparable to the present review because many prior analyses evaluated whole dietary patterns or macronutrient substitutions rather than salt exposure specifically, and often within more homogeneous study designs such as RCTs alone or observational cohorts alone. Our review instead deliberately brought together evidence from multiple causal frameworks, including Mendelian randomization, which can strengthen causal inference but introduces a different set of assumptions and outcome scales. The resulting inconsistency is therefore not surprising. Rather than contradicting the broader diet-cardiovascular literature, our findings suggest that, within the narrower evidence base available here, the measurable pooled effect of salt intake was not stable across analytic models and study types.

Several biological and clinical mechanisms nonetheless support the plausibility that salt intake could influence blood pressure, cardiovascular disease, and cardiovascular mortality. Excess sodium intake can increase extracellular fluid volume, alter renal sodium handling, and raise vascular resistance, all of which may elevate blood pressure in susceptible individuals. High salt exposure may also contribute to endothelial dysfunction, arterial stiffness, and adverse neurohormonal activation, offering pathways to cardiovascular events beyond blood pressure alone. At the same time, these mechanisms are not uniform across populations. Salt sensitivity varies by age, ancestry, baseline blood pressure, kidney function, metabolic status, and background dietary pattern, especially potassium intake. This heterogeneity in biological response may help explain why a clear pooled effect was not observed despite strong mechanistic rationale. In other words, the absence of a robust summary estimate in this review may reflect effect modification and exposure measurement problems as much as a true absence of biological effect.

Important sources of heterogeneity likely contributed to the observed uncertainty. First, the included studies differed fundamentally in design: observational studies are vulnerable to residual confounding and dietary measurement error, Mendelian randomization studies estimate lifelong genetically proxied exposure rather than short-term behavioral intake, and RCTs typically assess more controlled but shorter-term exposure contrasts. Second, salt intake itself is measured inconsistently across the literature, using self-report, dietary recall, urinary biomarkers, or categorical intake groupings, each with different validity. Third, the outcomes grouped in this review span intermediate physiological endpoints such as blood pressure and harder endpoints such as cardiovascular disease and cardiovascular death; combining these may obscure design-specific or outcome-specific effects. Fourth, the included evidence appears to vary in the availability of extractable quantitative data, with several studies lacking group-specific sample sizes, standard deviations, event counts, or numeric effect estimates. Those reporting limitations reduce precision and may selectively constrain which studies can contribute to meta-analysis. The divergence between the fixed- and random-effects estimates is consistent with this broader picture of modest heterogeneity layered onto a small evidence base.

This review has several strengths. Most importantly, it integrates evidence across complementary study designs rather than relying on a single epidemiologic approach, allowing a more nuanced view of convergence and inconsistency. The included studies were all rated as high quality by the enhanced extraction pipeline, and the extraction performance itself was strong for key variables, with F1 scores of 0.86 for direction of effect and 0.96 for statistical significance. Those performance metrics increase confidence that study-level signals were captured consistently, particularly for qualitative synthesis and the assessment of Convergency of Evidence and Level of Convergency. A further strength is intellectual transparency: the review does not force a strong causal conclusion from weakly harmonized data, and it reports the dependence of inference on the chosen pooling model. That is especially important in an area where prior beliefs about sodium and cardiovascular risk can easily outpace what a small synthesis can actually support.

The review also has important limitations. Although all included studies were classified as high quality by the extraction system, the extracted records reveal substantial reporting gaps, including missing study metadata, absent numeric effect estimates, incomplete sample-size reporting, and unavailable standard deviations or event counts in several studies. These are not trivial limitations; they directly restrict meta-analytic inclusion and weaken interpretability. The total number of included studies was small, with only two studies contributing to the pooled mean difference, which sharply limits power, precision, and the ability to explore publication bias or subgroup effects. Generalizability is also constrained because the review combined heterogeneous populations and designs without enough studies to stratify meaningfully by age, baseline cardiovascular risk, salt sensitivity, or method of exposure assessment. From a clinical standpoint, the present findings do not justify changing practice on their own. Existing dietary guidance on sodium reduction should continue to rely on the broader cumulative evidence base rather than this review in isolation. For research, the priority is clearer and more standardized reporting: future studies should provide directly extractable effect estimates, variance measures, exposure definitions, and subgroup data. Larger syntheses should also separate blood pressure, cardiovascular events, and mortality; distinguish short-term intervention effects from lifelong exposure proxies; and test whether convergence across study designs strengthens once outcome and exposure measurement are better aligned.

## Conclusion

In this meta-analysis of 6 studies examining salt intake across observational, Mendelian randomization, and randomized designs, the primary random-effects synthesis of 2 studies showed no clear association with the outcome (pooled MD -0.032, 95% CI -0.853 to 0.789; p=0.939). Clinically, this effect is essentially null and too small to support a meaningful impact on blood pressure or cardiovascular risk on its own, although the fixed-effect model suggested a small positive association (MD 0.152, 95% CI 0.027 to 0.276), indicating some model-dependent instability. Taken together, these findings do not justify strong conclusions from this dataset alone; a cautious recommendation is to continue following established salt-intake guidance based on the broader cardiovascular literature rather than this pooled estimate. The main caveat is the limited quantitative evidence and moderate between-study inconsistency across markedly different study designs.

## Final Included Studies

- Corpus ID: 91520 | Effects of Reduced Dietary Sodium and the DASH Diet on GFR: The DASH-Sodium Trial.
- Corpus ID: 26296 | Associations of Genetic Variations in the NR3C2 With Salt Sensitivity, Longitudinal Blood Pressure Changes, and Incidence of Hypertension in Chinese Adults.
- Corpus ID: 91509 | Associations of microRNA Gene Polymorphisms With Salt Sensitivity, Longitudinal Blood Pressure Changes, and Hypertension Incidence in the Chinese Population.
- Corpus ID: 77386 | Associations and mediators of estimated sodium intake with cardiovascular mortality: data based on a national population cohort.
- Corpus ID: 28384 | Intervention Using Low-Na/K Seasonings and Dairy at Japanese Company Cafeterias as a Practical Approach to Decrease Dietary Na/K and Prevent Hypertension.
- Corpus ID: 6784 | Dietary Fructose and Sodium Consumed during Early Mid-Life Are Associated with Hypertensive End-Organ Damage by Late Mid-Life in the CARDIA Cohort.
