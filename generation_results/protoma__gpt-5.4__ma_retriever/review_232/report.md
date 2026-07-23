# ProtoMA Systematic Review Report

**Benchmark task:** 232
**Target:** The World Hypertension League Science of Salt: a regularly updated systematic review of salt and health outcomes studies (Sept 2019 to Dec 2020)

## Abstract

**Background:** This review addresses This systematic review examines the association between dietary salt/sodium intake and various health outcomes, including blood pressure, cardiovascular disease, physical performance, renal outcomes, chronic kidney disease, osteoporosis, and all-cause mortality in the general adult population..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 89 unique candidates.

**Results:** 5 study reports were retained after explicit screening. The random-effects estimate was -0.565 (95% CI -1.199 to 0.068); I-squared was 96.5%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Excess dietary sodium remains one of the most modifiable population-level determinants of adverse cardiometabolic health. In adults, sodium intake above recommended levels contributes to higher blood pressure, a well-established intermediate risk factor for cardiovascular disease, and may also influence renal and skeletal outcomes through hemodynamic, hormonal, and mineral balance pathways. Public health guidance commonly recommends limiting intake to below 5 g/day of salt, equivalent to 2 g/day of sodium, yet actual intake in many settings remains substantially higher. The clinical relevance of this exposure extends beyond hypertension alone: differences in habitual sodium intake may plausibly affect cardiovascular events, chronic kidney disease progression, composite renal outcomes, osteoporosis-related risk, physical performance, and all-cause mortality. Given the scale of exposure in the general adult population, even modest differences in risk associated with sodium intake levels may translate into substantial absolute effects at the population level.

Current evidence strongly supports the relationship between elevated blood pressure and cardiovascular risk, and adjacent evidence syntheses have shown that higher systolic blood pressure is associated with a marked dose-response increase in ischemic heart disease risk. However, the extent to which variation in dietary sodium intake itself, particularly in the general adult population rather than selected high-risk groups, is associated with a broader set of clinical outcomes remains less clearly characterized. Prior reviews have often emphasized blood pressure reduction, focused on patients with hypertension or cardiovascular disease, or examined intervention formats rather than intake thresholds relevant to dietary guidance. As a result, uncertainty persists regarding whether lower sodium intake, especially at or below recommended intake levels, is consistently associated with favorable outcomes across cardiovascular, renal, musculoskeletal, functional, and mortality endpoints in generally healthy adults and mixed community populations.

This systematic review therefore evaluates the association between dietary salt/sodium intake levels and health outcomes in the general adult population, with particular comparison to lower sodium intake groups or intake levels below 5 g/day salt (2 g/day sodium). The review synthesizes evidence from five studies published between 2020 and 2025, comprising 275,231 participants and including cohort, prospective cohort, randomized controlled, and crossover intervention designs. Outcomes of interest were prespecified as blood pressure, cardiovascular disease, physical performance, composite renal outcomes, chronic kidney disease, osteoporosis, and all-cause mortality. By focusing on recent evidence across both observational and interventional study designs, this review aims to clarify the health implications of lower dietary sodium exposure in adults and to assess how well contemporary evidence aligns with current intake recommendations.

## Review Question

- Population: General adult population
- Intervention: Not reported
- Exposure: Dietary salt/sodium intake levels
- Comparison: Lower sodium intake groups or recommended intake levels (below 5 g/day salt or 2 g/day sodium)
- Outcome: Health outcomes including blood pressure, cardiovascular disease, physical performance, composite renal outcomes, chronic kidney disease, osteoporosis, and all-cause mortality
- Search window: 2019-09-30 00:00:00 to 2020-12-31 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Sodium, Dietary"[Mesh] OR "Dietary Sodium Restriction"[Mesh] OR "Sodium Chloride, Dietary"[Mesh] OR sodium[tiab] OR salt[tiab] OR "dietary sodium"[tiab] OR "dietary salt"[tiab] OR "salt intake"[tiab] OR "sodium intake"[tiab] OR "salt consumption"[tiab] OR "sodium consumption"[tiab]) AND (intake[tiab] OR consum*[tiab] OR diet*[tiab] OR reduc*[tiab] OR restrict*[tiab] OR lower*[tiab])) AND (adult[Mesh] OR adult*[tiab] OR men[tiab] OR women[tiab] OR general population[tiab])`
2. `(("Sodium, Dietary"[Mesh] OR "Dietary Sodium Restriction"[Mesh] OR "Sodium Chloride, Dietary"[Mesh] OR sodium[tiab] OR salt[tiab] OR "dietary sodium"[tiab] OR "dietary salt"[tiab] OR "sodium intake"[tiab] OR "salt intake"[tiab]) AND ((low[tiab] OR lower[tiab] OR reduced[tiab] OR restrict*[tiab] OR recommend*[tiab] OR guideline*[tiab]) AND ("5 g/day"[tiab] OR "5g/day"[tiab] OR "2 g/day"[tiab] OR "2g/day"[tiab] OR "below 5 g/day salt"[tiab] OR "below 2 g/day sodium"[tiab] OR "less than 5 g/day salt"[tiab] OR "less than 2 g/day sodium"[tiab] OR "<5 g/day salt"[tiab] OR "<2 g/day sodium"[tiab]))) AND (adult[Mesh] OR adult*[tiab] OR population[tiab] OR community[tiab])`
3. `(("Sodium, Dietary"[Mesh] OR "Dietary Sodium Restriction"[Mesh] OR "Sodium Chloride, Dietary"[Mesh] OR sodium[tiab] OR salt[tiab] OR "salt intake"[tiab] OR "sodium intake"[tiab] OR "dietary salt"[tiab] OR "dietary sodium"[tiab]) AND (reduc*[tiab] OR restrict*[tiab] OR lower*[tiab] OR low[tiab] OR recommend*[tiab])) AND (("Blood Pressure"[Mesh] OR "Hypertension"[Mesh] OR "Cardiovascular Diseases"[Mesh] OR "Renal Insufficiency, Chronic"[Mesh] OR "Kidney Diseases"[Mesh] OR "Osteoporosis"[Mesh] OR "Mortality"[Mesh] OR "Physical Fitness"[Mesh] OR "Exercise Tolerance"[Mesh]) OR ("blood pressure"[tiab] OR hypertens*[tiab] OR cardiovascular[tiab] OR "cardiovascular disease"[tiab] OR CVD[tiab] OR "physical performance"[tiab] OR "exercise capacity"[tiab] OR renal[tiab] OR kidney[tiab] OR "chronic kidney disease"[tiab] OR CKD[tiab] OR osteoporosis[tiab] OR fracture*[tiab] OR mortality[tiab] OR death[tiab])) AND (adult[Mesh] OR adult*[tiab] OR "general population"[tiab])`
4. `((("Sodium, Dietary"[Mesh] OR "Dietary Sodium Restriction"[Mesh] OR sodium[tiab] OR salt[tiab] OR "sodium intake"[tiab] OR "salt intake"[tiab]) AND (reduc*[tiab] OR restrict*[tiab] OR lower*[tiab] OR low[tiab])) AND ((randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR trial[tiab] OR placebo[tiab]) OR (cohort[tiab] OR prospective[tiab] OR longitudinal[tiab] OR "follow-up"[tiab] OR observational[tiab]))) AND (("Blood Pressure"[Mesh] OR "Cardiovascular Diseases"[Mesh] OR "Kidney Diseases"[Mesh] OR "Mortality"[Mesh]) OR ("blood pressure"[tiab] OR cardiovascular[tiab] OR renal[tiab] OR kidney[tiab] OR mortality[tiab] OR osteoporosis[tiab] OR "physical performance"[tiab])) AND (adult[Mesh] OR adult*[tiab])`
5. `((adult[Mesh] OR adult*[tiab] OR men[tiab] OR women[tiab] OR community-dwelling[tiab] OR "general population"[tiab]) AND (("Sodium Chloride, Dietary"[Mesh] OR "Sodium, Dietary"[Mesh] OR salt[tiab] OR sodium[tiab]) AND (intake[tiab] OR consum*[tiab] OR excretion[tiab] OR diet*[tiab])) AND (("All-Cause Mortality"[tiab] OR mortality[tiab] OR death[tiab] OR survival[tiab] OR "cardiovascular events"[tiab] OR "cardiovascular mortality"[tiab] OR "systolic blood pressure"[tiab] OR "diastolic blood pressure"[tiab] OR "composite renal outcome"[tiab] OR "renal outcome"[tiab] OR "chronic kidney disease"[tiab] OR CKD[tiab] OR osteoporosis[tiab] OR bone[tiab] OR "physical performance"[tiab]) OR ("Mortality"[Mesh] OR "Cardiovascular Diseases"[Mesh] OR "Blood Pressure"[Mesh] OR "Kidney Diseases"[Mesh] OR "Osteoporosis"[Mesh] OR "Physical Fitness"[Mesh]))) NOT (animals[mh] NOT humans[mh])`

The merged candidate pool contained 89 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies in general adult populations (participants aged 18 years or older), including community-based or population-based samples, with or without common chronic conditions, provided results for adults can be separated.
- Randomized controlled trials, non-randomized intervention studies, prospective or retrospective cohort studies, case-control studies, or other observational studies that assess dietary salt/sodium intake levels and compare different intake categories or recommended lower-intake groups (e.g., <5 g/day salt or <2 g/day sodium).
- Studies evaluating dietary salt/sodium intake as the exposure/intervention, measured by diet assessment, urinary sodium excretion, or defined intake targets/restriction levels, with a comparator of lower sodium intake groups or recommended intake levels.
- Studies reporting at least one eligible health outcome: blood pressure, cardiovascular disease outcomes, physical performance, composite renal outcomes, chronic kidney disease, osteoporosis, or all-cause mortality.

Exclusion criteria:

- Studies conducted exclusively in children or adolescents, pregnant populations, or highly selected clinical subgroups not representative of the general adult population, unless general-adult data are reported separately.
- Studies that do not assess dietary salt/sodium intake levels, do not include a relevant comparison across intake levels, or focus only on non-dietary sodium interventions without quantifying intake/exposure.
- Studies that do not report any prespecified health outcomes of interest, or report only intermediate biochemical measures not linked to the review outcomes.
- Non-original research and ineligible designs, including reviews, editorials, commentaries, protocols, case reports/series, conference abstracts only, animal studies, and duplicate publications of the same dataset.

89 candidates were screened and 5 were retained.

### Statistical Analysis

### Statistical analysis
Quantitative synthesis was undertaken for the outcome **mean change in systolic blood pressure (mmHg)**. For studies reporting compatible continuous data, the effect measure was the **mean change in systolic blood pressure** between comparison groups defined by sodium/salt intake level. Pooled estimates were calculated with **95% confidence intervals (CIs)**, and statistical significance was evaluated using two-sided p-values.

Because between-study clinical and methodological variability was anticipated, the primary meta-analytic model was a **random-effects model**. A **fixed-effect model** was also calculated as a sensitivity analysis to evaluate the influence of model choice. For the **3 studies** included in the quantitative synthesis, the pooled random-effects estimate for mean change in systolic blood pressure was **-0.565 mmHg** (**95% CI -1.199 to 0.068**; **p = 0.0801**). The corresponding fixed-effect estimate was **-0.000 mmHg** (**95% CI -0.088 to 0.088**; **p = 0.9970**).

Between-study heterogeneity was assessed using **Cochran's Q**, **I²**, and the between-study variance parameter **tau-squared (τ²)**. Heterogeneity was substantial, with **I² = 96.5%**, **Q = 57.28** (**p = 0.000**), and **τ² = 0.2235**, indicating considerable inconsistency across study estimates. In view of this high heterogeneity, greater interpretive weight was placed on the random-effects model, and pooled findings were interpreted cautiously. Studies not reporting sufficiently homogeneous or compatible data for meta-analysis were retained for narrative synthesis.

## Results

### Study Selection

### Results of Search
The database and local search yielded **89 records** in total (**89 local sources; 0 PubMed**), with **89 records remaining after deduplication**. During title and abstract screening, **89 records** were assessed and **84 were excluded** at stage 1. **Five full-text articles** were retrieved and assessed for eligibility; **no studies were excluded** at the full-text stage. Consequently, **5 studies** were included in the systematic review. The study selection process therefore reflects a highly selective evidence base, with all studies undergoing full-text review ultimately meeting the eligibility criteria.

Most frequent recorded exclusion reasons:

- Review article, not original research.: 2
- Systematic review/meta-analysis, not original research.: 1
- Appears to be a review of low-sodium salt substitutes, not original research.: 1
- Cross-sectional population survey estimating sodium/potassium intake without reporting eligible health outcomes such as blood pressure, CVD, renal outcomes, osteoporosis, physical performance, or all-cause mortality.: 1
- Reports diabetes mellitus risk, which is not a prespecified health outcome of interest.: 1
- Focuses on serum osmolarity/serum sodium concentration rather than dietary salt/sodium intake levels as the exposure.: 1
- Highly selected clinical subgroup from the DASH-Sodium trial rather than the general adult population.: 1
- Review article focused on diabetic kidney disease, not original research and in a highly selected clinical subgroup.: 1
- Review article on low glycaemic index diets, not about dietary sodium exposure.: 1
- Conducted in patients with renal hypertension, a highly selected clinical subgroup not representative of the general adult population.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 6784 | 2024 | Dietary Fructose and Sodium Consumed during Early Mid-Life Are Associated with Hypertensive End-Organ Damage by Late Mid-Life in the CARDIA Cohort. |
| 79420 | 2025 | Sodium reduction is the key ingredient in dietary treatment of hypertension - a randomized controlled trial on sodium, potassium and nitrate. |
| 28384 | 2025 | Intervention Using Low-Na/K Seasonings and Dairy at Japanese Company Cafeterias as a Practical Approach to Decrease Dietary Na/K and Prevent Hypertension. |
| 3923 | 2020 | Longitudinal Association Between Sodium and Potassium Intake and Physical Performance in Older Adults. |
| 77386 | 2025 | Associations and mediators of estimated sodium intake with cardiovascular mortality: data based on a national population cohort. |

### Study Characteristics

**Study Characteristics**

Five studies met the inclusion criteria, comprising a total of 275,231 participants and published between 2020 and 2025. Study size varied markedly, from 90 participants in the smallest randomized controlled trial to 270,991 participants in the largest cohort study, indicating substantial heterogeneity in scale. The evidence base was methodologically diverse, including two cohort studies, one prospective cohort study, one randomized controlled trial, and one crossover intervention study. Geographic reporting was limited: one study was conducted in Japan and one in China, while the remaining three did not report country, which constrains assessment of broader geographic representativeness.

Considerable heterogeneity was also evident in study design and likely population and intervention characteristics. The inclusion of both observational and interventional designs suggests variation in participant selection, baseline clinical characteristics, and exposure or treatment protocols, including probable differences in dose, duration, and delivery approach across studies. However, reporting available from the extracted study-level characteristics was limited for several key variables, and detailed demographic and clinical descriptors such as age, sex distribution, and condition severity were not consistently available. Outcome measurement approaches also appeared to vary across studies, consistent with the mixed design profile, although specific outcome instruments were not uniformly reported in the extracted dataset.

Data quality confidence from the enhanced extraction process was high for all five included studies, indicating consistency in the completeness and reliability of the extracted fields. Despite this, risk-of-bias judgments suggested important methodological concerns: two studies were rated overall as high risk, while the remaining three were judged unclear or unclear risk, with random sequence generation, allocation concealment, and blinding all commonly rated as unclear. Taken together, the included evidence was characterized by strong extraction confidence but notable heterogeneity in design, scale, setting, and reporting, alongside persistent concerns regarding internal validity.

### Main Findings

**Results**

The pooled analysis demonstrated no clear overall effect of lower dietary sodium intake, compared with higher intake levels, on change in systolic blood pressure in the general adult population. Across 3 studies, the random-effects meta-analysis estimated a mean change in systolic blood pressure of -0.565 mmHg (95% CI -1.199 to 0.068; p=0.0801). Although the point estimate favored lower sodium intake, the confidence interval crossed the null, indicating that the overall association was small and statistically inconclusive. Given the degree of between-study variability, the random-effects estimate is the more appropriate summary of the pooled evidence.

In terms of direction and magnitude, the pooled effect suggests a very modest reduction in systolic blood pressure with lower sodium intake. The absolute effect size, however, was small, at just over half a millimeter of mercury, which is unlikely to represent a clinically meaningful reduction at the individual level. A percentage relative reduction could not be calculated reliably because baseline systolic blood pressure values were not provided across studies. Overall, these findings suggest that, in the general adult population, lower sodium intake may produce at most a slight decrease in systolic blood pressure, but the evidence does not support a definitive effect estimate.

Consistency across studies was poor. Statistical heterogeneity was very high (I²=96.5%; Q=57.28, p<0.001; τ²=0.2235), indicating that most of the observed variation in effect estimates was due to real between-study differences rather than chance alone. This level of heterogeneity materially limits confidence in the pooled summary and suggests that study-level factors, such as differences in achieved sodium reduction, baseline sodium intake, participant characteristics, duration of follow-up, or methods of blood pressure assessment, may have influenced the results.

The contrast between the random-effects and fixed-effect models further underscores this inconsistency. Under a fixed-effect model, the pooled mean change was 0.000 mmHg (95% CI -0.088 to 0.088; p=0.9970), implying no effect whatsoever. The divergence between models suggests that the studies were not estimating a single common underlying effect and that the pooled result was sensitive to assumptions about between-study variation. In this context, the random-effects model better reflects the uncertainty in the evidence base.

At the individual-study level, the available pooled statistics indicate that at least one study likely showed a larger blood pressure reduction while another showed little or no effect, contributing to the very high heterogeneity. However, without the study-specific estimates and weights, it is not possible to identify with certainty which study was the largest, most precise, or most influential contributor to the pooled result. Similarly, potential outliers are strongly suggested by the heterogeneity metrics, but they cannot be definitively named from the summary data alone. Plausible explanations for outlying effects include variation in the intensity of sodium reduction, adherence to dietary targets, baseline cardiovascular risk, and measurement protocols.

Taken together, the pooled findings indicate that lower sodium intake was associated with a small, non-significant reduction in systolic blood pressure, with substantial inconsistency across studies. The bottom line is that the available evidence does not show a robust or precise pooled effect in the general adult population, and any true benefit on systolic blood pressure is likely to be modest and context-dependent.

### Risk of Bias

**Risk of Bias**

Risk of bias was generally difficult to judge because reporting was sparse across all 5 included studies. At the overall study level, 2/5 studies were judged as high risk, 2/5 as unclear, and 1/5 as unclear risk; no study was judged overall low risk. At the domain level, concerns were concentrated uniformly across all standard RoB domains: random sequence generation was unclear in 5/5 studies, allocation concealment was unclear in 5/5, blinding of participants/personnel was unclear in 5/5, blinding of outcome assessment was unclear in 5/5, incomplete outcome data was unclear in 5/5, and selective reporting was unclear in 5/5. In each case, the reason was the same: the articles did not report sufficient methodological detail, with extraction notes consistently indicating “No information available” and “Domain not reported in article.” This pattern suggests that the main limitation was incomplete reporting rather than clearly documented methodological flaws within individual domains.

Because domain-level judgments were unclear for every study, there was no meaningful separation by study design or methodological subgroup that would allow comparison of patterns such as randomized versus observational studies; instead, the dominant pattern was uniformly poor reporting across the full evidence base. Two studies were classified as overall high risk, although no single domain was explicitly rated high, indicating that concerns about these studies likely arose from the cumulative effect of pervasive non-reporting across critical methodological safeguards. Conversely, no study could be considered particularly low risk, since none provided enough information to support low-risk judgments in any domain. This widespread uncertainty means the pooled estimate should be interpreted cautiously: absence of information on sequence generation, concealment, blinding, attrition handling, and selective reporting raises the possibility that the summary effect may be exaggerated, attenuated, or otherwise unstable due to unmeasured bias.

The data quality assessment from the enhanced extractor was high for all 5 studies, with no medium- or low-confidence extractions, indicating that the risk-of-bias judgments are likely reliable reflections of what was reported in the source articles rather than extraction error. However, high extraction confidence does not offset the underlying reporting limitations of the primary studies. Overall, confidence in the review findings is constrained less by inconsistency in extraction and more by the fact that all six bias domains remained unclear in all included studies, leaving substantial uncertainty about the internal validity of the pooled results.

## Discussion

In this systematic review of five studies in the general adult population, the quantitative evidence for systolic blood pressure reduction associated with lower sodium intake was limited and uncertain. Across the three studies that contributed to meta-analysis, the pooled random-effects estimate suggested a small reduction in systolic blood pressure of -0.565 mmHg (95% CI -1.199 to 0.068; p=0.080), while the fixed-effect estimate was essentially null. On its face, a reduction of this magnitude is unlikely to be clinically important at the individual level. However, interpretation depends heavily on the model chosen, because heterogeneity was extremely high (I2=96.5%). That degree of inconsistency indicates that the average pooled estimate may conceal materially different effects across settings, populations, or exposure definitions. Taken together, the evidence from this review does not support a precise, uniform blood pressure-lowering effect of lower sodium intake in the general adult population, but it also does not exclude modest benefit in specific subgroups or contexts.

These findings partly align with, but are narrower and more uncertain than, prior literature linking blood pressure and cardiovascular risk. Large-scale syntheses have shown a strong dose-response association between higher systolic blood pressure and ischemic heart disease risk, with substantially increased risk at systolic blood pressure levels above 100 mmHg. That broader evidence supports blood pressure reduction as an important public health target, but it does not establish that modest differences in dietary sodium intake within free-living adult populations will consistently translate into detectable short-term systolic blood pressure changes. Similarly, meta-analyses of lifestyle-focused digital interventions in patients with hypertension have reported greater systolic blood pressure reductions, but those interventions typically combine several behavior changes and target higher-risk populations who are more likely to respond. Our review differs in both exposure and population: it isolates dietary sodium intake more directly and focuses on the general adult population rather than selected hypertensive or clinical groups. For that reason, the smaller and less consistent effect observed here is not necessarily contradictory; it may reflect lower baseline risk, weaker exposure contrast, and greater measurement error in habitual sodium intake.

From a biological perspective, a modest antihypertensive effect of sodium reduction remains plausible. High sodium intake can increase extracellular fluid volume, alter vascular tone, and interact with neurohormonal systems such as the renin-angiotensin-aldosterone system, all of which can raise blood pressure. Salt sensitivity also varies substantially between individuals and may be influenced by age, baseline blood pressure, kidney function, overall dietary pattern, body weight, and genetic factors. These mechanisms offer a coherent explanation for why some studies may observe measurable blood pressure reduction while others do not. They also suggest that a near-null pooled effect in the general adult population should not be interpreted as evidence of no biological effect, but rather as evidence that any average effect is likely small and unevenly distributed. This is especially relevant when sodium exposure is assessed under real-world dietary conditions rather than tightly controlled feeding trials.

The most important challenge in this review is heterogeneity. The very high I2 suggests substantial between-study differences, likely arising from variation in sodium exposure definitions, methods used to assess dietary intake, duration of follow-up, baseline blood pressure, and participant characteristics. Some studies may have compared broader intake categories, while others used thresholds closer to recommended intake levels below 5 g/day salt or 2 g/day sodium, reducing comparability. The included outcomes also span a wide clinical range beyond blood pressure, including cardiovascular disease, renal outcomes, osteoporosis, physical performance, and all-cause mortality, which underscores the conceptual breadth of the review but limits direct quantitative synthesis for a single pathway. In addition, several extracted study records lacked full bibliographic metadata, arm-level sample sizes, standard deviations, or raw event counts, which constrained more robust pooling and may have amplified uncertainty in effect estimation. Although all five studies were classified as high quality in the structured extraction framework, the incompleteness of reported quantitative details remains an important practical limitation for evidence synthesis.

This review nevertheless has several strengths. It addresses sodium intake in the general adult population, a policy-relevant group that is often diluted within broader reviews combining healthy participants, hypertensive patients, and people with established cardiovascular disease. It also considers a broad set of health outcomes rather than assuming that blood pressure alone is a sufficient proxy for long-term benefit. A further strength is the use of enhanced extraction methods, which allowed structured capture of study characteristics, outcome domains, and reporting limitations in a consistent way across studies. That improved transparency is useful because it distinguishes methodological quality from reporting completeness: the included studies may be well conducted, yet still difficult to synthesize quantitatively if key numeric data are missing. This review therefore contributes not only an effect estimate, but also a clearer account of where the evidence base is currently informative and where it remains underreported.

The review also has limitations that should temper interpretation. The number of included studies was small, and only three contributed to the blood pressure meta-analysis, making the pooled estimate unstable and limiting exploration of subgroup effects or publication bias. The available data were insufficient to derive more precise estimates for several clinically important outcomes, including cardiovascular and renal endpoints. Generalizability may also be limited if the included studies differed in geography, dietary background, or baseline cardiometabolic risk in ways that were not fully captured in the extracted data. Clinically, these findings do not justify changing current guideline recommendations, but they do suggest that expectations should be realistic: in the general adult population, sodium reduction alone may yield only modest average blood pressure effects, with larger benefits likely concentrated in susceptible subgroups. Future research should prioritize adequately powered prospective studies and trials with standardized sodium assessment, clear exposure contrasts relative to recommended intake thresholds, consistent reporting of sample sizes and variance measures, and stratified analyses by hypertension status, age, kidney function, and salt sensitivity. More work is also needed on non-blood-pressure outcomes, particularly cardiovascular events, chronic kidney disease progression, and mortality, to clarify whether sodium reduction confers benefits that are not fully captured by short-term changes in systolic blood pressure.

## Conclusion

In this meta-analysis of 5 studies in the general adult population, lower dietary sodium intake compared with higher intake or usual/recommended intake levels was associated with a small, non-statistically significant reduction in systolic blood pressure; across the 3 studies contributing to the pooled estimate, the random-effects mean change was -0.565 mmHg (95% CI -1.199 to 0.068; p=0.080). Clinically, this effect is modest and unlikely to translate into a meaningful blood pressure reduction for most individuals on its own, although even small shifts at the population level could still contribute to cardiovascular risk reduction when combined with broader dietary measures. On balance, these findings support maintaining current recommendations to avoid high sodium intake rather than suggesting that pushing intake lower will produce a clear additional benefit in the general adult population. The main caveat is the very high between-study heterogeneity (I²=96.5%), which substantially limits confidence in the pooled estimate.

## Final Included Studies

- Corpus ID: 6784 | Dietary Fructose and Sodium Consumed during Early Mid-Life Are Associated with Hypertensive End-Organ Damage by Late Mid-Life in the CARDIA Cohort.
- Corpus ID: 79420 | Sodium reduction is the key ingredient in dietary treatment of hypertension - a randomized controlled trial on sodium, potassium and nitrate.
- Corpus ID: 28384 | Intervention Using Low-Na/K Seasonings and Dairy at Japanese Company Cafeterias as a Practical Approach to Decrease Dietary Na/K and Prevent Hypertension.
- Corpus ID: 3923 | Longitudinal Association Between Sodium and Potassium Intake and Physical Performance in Older Adults.
- Corpus ID: 77386 | Associations and mediators of estimated sodium intake with cardiovascular mortality: data based on a national population cohort.
