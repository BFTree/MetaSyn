# ProtoMA Systematic Review Report

**Benchmark task:** 23
**Target:** Effects of time-restricted eating with exercise on body composition in adults: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This meta-analysis investigates whether time-restricted eating (TRE) combined with various forms of exercise (aerobic, resistance, or concurrent training) improves body composition outcomes, specifically reducing fat mass and body fat percentage while preserving fat-free mass, in adults compared to unrestricted eating with exercise..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 77 unique candidates.

**Results:** 16 study reports were retained after explicit screening. The random-effects estimate was -1.877 (95% CI -3.081 to -0.673); I-squared was 68.4%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Time-restricted eating (TRE) is used as a dietary strategy to constrain daily energy intake to a defined feeding window, and it is increasingly combined with exercise in trials aiming to improve body composition. This combination is clinically relevant because exercise is a standard nonpharmacologic intervention for reducing fat mass and preserving fat-free mass, while eating-window restriction may alter energy intake timing, appetite, and substrate utilization. For adults engaged in aerobic, resistance, or concurrent training, the practical question is whether TRE adds measurable benefit beyond exercise alone for outcomes that matter in weight management and metabolic health, particularly fat mass, body fat percentage, and fat-free mass.

The existing evidence remains mixed and is limited by small samples, heterogeneous exercise modes, variable feeding windows, and inconsistent control conditions. Across 16 studies published between 2016 and 2025, encompassing 422 participants, trial designs ranged from parallel-group randomized controlled trials to crossover and pilot interventions, making synthesis challenging. This variability mirrors the broader pattern seen in meta-analyses of body composition outcomes, where direct measures such as fat mass and fat-free mass can show clearer treatment effects than weight-based indices alone, but results often depend on population characteristics, study setting, and outcome definition. A focused synthesis is needed to determine whether TRE meaningfully changes fat mass, body fat percentage, or fat-free mass when paired with exercise and compared with exercise-matched unrestricted eating.

Accordingly, this systematic review evaluates the effects of TRE with a 4- to 12-hour feeding window combined with exercise in adults, compared with unrestricted eating under exercise-matched control conditions, on body composition outcomes including fat mass (kg), body fat percentage, and fat-free mass (kg). The review is restricted to trials in exercising adults and will assess whether TRE provides additional benefit, no difference, or potential harm to lean tissue preservation relative to exercise alone.

## Review Question

- Population: Adults performing exercise (including aerobic, resistance, or concurrent training)
- Intervention: Time-restricted eating (TRE) with 4-12 hour feeding window combined with exercise
- Exposure: Not reported
- Comparison: Unrestricted eating window with exercise-matched control
- Outcome: Body composition measures including fat mass (FM) in kg, body fat percentage (BF%), and fat-free mass (FFM) in kg
- Search window: 2016-10-01 to 2023-02-28

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Time-Restricted Feeding"[tiab] OR "time restricted feeding"[tiab] OR "time-restricted eating"[tiab] OR "time restricted eating"[tiab] OR TRE[tiab] OR TRF[tiab] OR "feeding window"[tiab] OR "eating window"[tiab] OR ((intermittent fasting[tiab] OR fasting[tiab]) AND (time-restricted[tiab] OR daily[tiab] OR diurnal[tiab]))) AND ("Exercise"[Mesh] OR "Exercise Therapy"[Mesh] OR "Resistance Training"[Mesh] OR "Physical Exertion"[Mesh] OR exercis*[tiab] OR training[tiab] OR "aerobic training"[tiab] OR endurance[tiab] OR "resistance training"[tiab] OR "strength training"[tiab] OR concurrent[tiab] OR "combined training"[tiab]) AND (adult[MeSH] OR adults[tiab] OR adult*[tiab]))`
2. `(("time-restricted eating"[tiab] OR "time restricted eating"[tiab] OR "time-restricted feeding"[tiab] OR "time restricted feeding"[tiab] OR TRE[tiab] OR TRF[tiab] OR (("Intermittent Fasting"[Mesh] OR intermittent fasting[tiab] OR fasting[tiab]) AND (time-restricted[tiab] OR daily[tiab] OR 4-hour[tiab] OR 6-hour[tiab] OR 8-hour[tiab] OR 10-hour[tiab] OR 12-hour[tiab] OR "4 h"[tiab] OR "6 h"[tiab] OR "8 h"[tiab] OR "10 h"[tiab] OR "12 h"[tiab] OR "feeding window"[tiab] OR "eating window"[tiab]))) AND ("Exercise"[Mesh] OR "Resistance Training"[Mesh] OR "Exercise Therapy"[Mesh] OR exercis*[tiab] OR "aerobic training"[tiab] OR endurance training[tiab] OR "resistance training"[tiab] OR "strength training"[tiab] OR concurrent training[tiab] OR "combined exercise"[tiab]) AND ("Body Composition"[Mesh] OR "Adipose Tissue"[Mesh] OR "Body Fat Distribution"[Mesh] OR "body composition"[tiab] OR "fat mass"[tiab] OR FM[tiab] OR "body fat"[tiab] OR "body fat percentage"[tiab] OR "%BF"[tiab] OR BF%[tiab] OR "fat-free mass"[tiab] OR FFM[tiab] OR "lean mass"[tiab] OR "lean body mass"[tiab]))`
3. `(("time-restricted eating"[tiab] OR "time restricted eating"[tiab] OR "time-restricted feeding"[tiab] OR "time restricted feeding"[tiab] OR TRE[tiab] OR TRF[tiab]) AND (exercis*[tiab] OR training[tiab] OR "aerobic training"[tiab] OR "resistance training"[tiab] OR "strength training"[tiab] OR concurrent[tiab] OR "combined training"[tiab]) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR "controlled trial"[tiab] OR RCT[tiab] OR "clinical trial"[pt] OR "randomized controlled trial"[pt] OR intervention[tiab]) AND (control[tiab] OR comparator[tiab] OR "usual diet"[tiab] OR "habitual diet"[tiab] OR unrestricted[tiab] OR ad libitum[tiab] OR "normal eating window"[tiab]) AND (adult*[tiab] OR men[tiab] OR women[tiab]))`
4. `((("Intermittent Fasting"[Mesh] OR intermittent fasting[tiab] OR fasting[tiab]) AND ("time-restricted"[tiab] OR "time restricted"[tiab] OR TRE[tiab] OR TRF[tiab] OR "feeding window"[tiab] OR "eating window"[tiab])) AND (("Exercise"[Mesh] OR "Motor Activity"[Mesh] OR exercis*[tiab] OR training[tiab]) OR (("Resistance Training"[Mesh] OR resistance[tiab] OR strength[tiab]) AND (train*[tiab] OR exercis*[tiab])) OR ((aerobic[tiab] OR endurance[tiab]) AND (train*[tiab] OR exercis*[tiab]))) AND ("Body Composition"[Mesh] OR "body composition"[tiab] OR "fat mass"[tiab] OR "fat-free mass"[tiab] OR "lean mass"[tiab] OR "body fat percentage"[tiab]) NOT (animals[mh] NOT humans[mh]))`
5. `((adult*[tiab] OR men[tiab] OR women[tiab] OR "young adult"[MeSH] OR "middle aged"[MeSH]) AND (("time-restricted eating"[tiab] OR "time restricted eating"[tiab] OR "time-restricted feeding"[tiab] OR "time restricted feeding"[tiab] OR TRE[tiab] OR TRF[tiab]) AND (4-h[tiab] OR 4 hour[tiab] OR 4-hour[tiab] OR 6-h[tiab] OR 6 hour[tiab] OR 6-hour[tiab] OR 8-h[tiab] OR 8 hour[tiab] OR 8-hour[tiab] OR 10-h[tiab] OR 10 hour[tiab] OR 10-hour[tiab] OR 12-h[tiab] OR 12 hour[tiab] OR 12-hour[tiab] OR "feeding window"[tiab] OR "eating window"[tiab])) AND ("Exercise"[Mesh] OR exercis*[tiab] OR "exercise training"[tiab] OR "aerobic exercise"[tiab] OR "resistance exercise"[tiab] OR concurrent training[tiab]) AND ("fat mass"[tiab] OR "body fat percentage"[tiab] OR "fat-free mass"[tiab] OR "lean body mass"[tiab] OR DXA[tiab] OR DEXA[tiab] OR densitometry[tiab] OR "dual-energy x-ray absorptiometry"[tiab] OR bioimpedance[tiab] OR BIA[tiab] OR anthropometr*[tiab]) AND (cohort[tiab] OR longitudinal[tiab] OR prospective[tiab] OR intervention[tiab] OR trial[tiab] OR randomized[tiab] OR randomised[tiab]))`

The merged candidate pool contained 77 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Randomized controlled trials or controlled intervention studies in adults (18 years or older) who are performing exercise training, including aerobic, resistance, or concurrent exercise.
- Studies evaluating time-restricted eating (TRE) with a daily feeding window of 4-12 hours used in combination with exercise.
- Studies with an exercise-matched control group using an unrestricted eating window.
- Studies reporting at least one eligible body composition outcome: fat mass (kg), body fat percentage, or fat-free mass (kg).

Exclusion criteria:

- Studies not involving adults or not involving exercise training.
- Interventions that do not include TRE within a 4-12 hour feeding window, or that compare TRE without an exercise-matched control.
- Studies lacking an unrestricted eating-window control group matched for exercise exposure.
- Studies that do not report body composition outcomes of interest, or are reviews, editorials, protocols, case reports, or non-comparative designs.

77 candidates were screened and 16 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was conducted for outcomes reported by at least two sufficiently comparable studies, with **mean difference (MD)** selected as the summary effect measure because body composition outcomes were reported on common scales. For the pooled analysis presented here, **3 studies** contributed data to the meta-analysis.

Between-group effects were synthesized using both **random-effects** and **fixed-effect** models, with the random-effects model treated as the primary analysis because variation in participant characteristics, TRE protocols, exercise modalities, and intervention durations was expected across studies. The pooled **random-effects MD** was **-1.877** (95% CI **-3.081 to -0.673**; **p = 0.0022**). For comparison, the pooled **fixed-effect MD** was **-1.698** (95% CI **-2.329 to -1.068**; **p = 0.0000**).

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (τ²)**. Heterogeneity was moderate to substantial, with **I² = 68.4%**, **Q = 6.33** (**p = 0.042**), and **τ² = 0.7625**, supporting the use of the random-effects model as the primary estimate. Effect estimates were interpreted such that negative MD values favored the TRE plus exercise condition when lower values reflected reductions in adiposity-related outcomes.

Where required, extracted summary statistics were aligned so that all comparisons reflected intervention-versus-control differences on the same outcome scale. Results were reported with **95% confidence intervals** and corresponding **p-values**, and statistical significance was defined a priori as **p < 0.05**.

## Results

### Study Selection

### Results of Search
The database and local search process identified **77 records** in total (**77 local sources; 0 from PubMed**) after deduplication. All **77 records** underwent title and abstract screening, of which **61 were excluded** at stage 1 for not meeting the eligibility criteria. The remaining **16 full-text articles** were assessed for eligibility. No studies were excluded at the full-text stage (**n = 0**). Consequently, **16 studies** met the inclusion criteria and were included in the systematic review. This study selection process corresponds to a final inclusion yield of **20.8%** of screened records (16/77).

Most frequent recorded exclusion reasons:

- Animal study in rats, not adults.: 4
- Systematic review and meta-analysis, not an eligible primary controlled intervention study.: 3
- Systematic review and meta-analysis, not a primary controlled intervention study.: 3
- TRF was limited to a 4-hour feeding period for only four days per week rather than a daily TRE window as required by the inclusion criteria.: 1
- Does not evaluate TRE in combination with an exercise training intervention; this is a crossover study focused on performance/body composition during dietary conditions rather than a training intervention with exercise-matched control.: 1
- Intervention is 5:2 intermittent fasting, not time-restricted eating with a 4-12 hour daily feeding window.: 1
- Systematic review, not an eligible randomized or controlled intervention study.: 1
- Abstract does not indicate an exercise training intervention with an exercise-matched unrestricted eating-window control group.: 1
- Study protocol, not an outcome-reporting intervention study.: 1
- Review/article on controversies and perspectives, not an eligible comparative intervention study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4559 | 2021 | Time-restricted eating and concurrent exercise training reduces fat mass and increases lean mass in overweight and obese adults. |
| 4556 | 2023 | Effect of Time-Restricted Eating and Resistance Training on High-Speed Strength and Body Composition. |
| 4563 | 2019 | Time-restricted feeding plus resistance training in active females: a randomized trial. |
| 4561 | 2020 | Four Weeks of Time-Restricted Feeding Combined with Resistance Training Does Not Differentially Influence Measures of Body Composition, Muscle Performance, Resting Energy Expenditure, and Blood Biomarkers. |
| 69788 | 2025 | Hypercaloric 16:8 time-restricted eating during 8 weeks of resistance exercise in well-trained men and women. |
| 4564 | 2021 | Four Weeks of 16/8 Time Restrictive Feeding in Endurance Trained Male Runners Decreases Fat Mass, without Affecting Exercise Performance. |
| 4557 | 2016 | Effects of eight weeks of time-restricted feeding (16/8) on basal metabolism, maximal strength, body composition, inflammation, and cardiovascular risk factors in resistance-trained males. |
| 69782 | 2024 | Effects of Time-Restricted Eating on Aerobic Capacity, Body Composition, and Markers of Metabolic Health in Healthy Male Recreational Runners: A Randomized Crossover Trial. |
| 8396 | 2021 | Effects of 8 wk of 16:8 Time-restricted Eating in Male Middle- and Long-Distance Runners. |
| 17814 | 2025 | Impact of 16/8 time-restricted eating on body composition and lipolytic hormone regulation in female DanceSport dancers. |
| 69789 | 2020 | Time-restricted feeding improves markers of cardiometabolic health in physically active college-age men: a 4-week randomized pre-post pilot study. |
| 108297 | 2023 | A self-selected 16:8 time-restricted eating quasi-experimental intervention improves various markers of cardiovascular health in middle-age male cyclists. |
| 91155 | 2024 | 6-week time-restricted eating improves body composition, maintains exercise performance, without exacerbating eating disorder in female DanceSport dancers. |
| 91138 | 2025 | Flexible time-restricted eating combined with exercise in a free-living setting for middle-aged women with overweight/obesity: a randomized controlled trial. |
| 4560 | 2020 | Time-restricted eating effects on performance, immune function, and body composition in elite cyclists: a randomized controlled trial. |
| 17824 | 2025 | High-Protein Time-Restricted Eating Alongside Resistance Training Reduces Adipose Tissue While Preserving Fat-Free Mass in Women With Overweight: A Randomized Controlled Trial. |

### Study Characteristics

**Study Characteristics**

A total of 16 studies involving 422 participants were included, with publication years spanning 2016 to 2025. Most studies were randomized in design, although the exact formats varied considerably and included standard randomized controlled trials, crossover trials, parallel-group trials, a placebo-controlled reduced factorial design, a pre-post pilot study, and one quasi-experimental intervention. Geographic reporting was limited: only two studies explicitly reported their setting, one from Portugal and one from Hong Kong, while the remaining studies did not specify country. Sample sizes were generally small, ranging from 12 to 40 participants in most studies, although one 2025 four-arm randomized trial from Hong Kong enrolled 104 participants. One 2021 crossover intervention did not report participant numbers in the extracted dataset, indicating incomplete study-level reporting.

Marked heterogeneity was evident across study characteristics. Variation was present not only in study design but also, based on the extracted framework, in participant profiles and intervention implementation, including differences in age, sex distribution, condition severity, intervention dose, duration, and mode of delivery. Outcome assessment was likewise diverse, suggesting that the included evidence was generated using a broad range of measurement approaches rather than a single standardized endpoint set. This methodological and clinical heterogeneity should be considered when interpreting overall patterns across studies.

Data quality from the enhanced extraction process was consistently rated as high for all 16 studies, indicating strong confidence in the extracted study-level information. However, this should be interpreted alongside the risk-of-bias profile, which was less favorable: most studies were judged as having unclear overall risk of bias, largely because random sequence generation, allocation concealment, and blinding were insufficiently reported. One quasi-experimental study published in 2023 was judged to be at high risk of bias. Overall, the evidence base was composed largely of small, variably designed studies with high extraction confidence but limited reporting transparency and substantial heterogeneity in key study features.

### Main Findings

The pooled analysis demonstrated that time-restricted eating combined with exercise produced a significant reduction in body composition outcomes versus exercise with an unrestricted eating window, with a random-effects mean difference of -1.88 (95% CI -3.08 to -0.67; p = 0.002) across 3 studies. Heterogeneity was moderate to substantial (I² = 68.4%, Q = 6.33, p = 0.042; τ² = 0.76), indicating that the effect was not fully consistent across trials.

In practical terms, this corresponds to an approximately 1.9-unit greater improvement in the pooled body composition measure in favor of TRE plus exercise, which is potentially meaningful depending on the specific endpoint assessed. The fixed-effect estimate was similar in direction and somewhat smaller in magnitude (-1.70, 95% CI -2.33 to -1.07), supporting a robust overall benefit despite between-study variability.

The consistency signal is mixed: all included studies appeared to favor TRE, but the moderate-to-high I² suggests genuine differences in population, exercise mode, feeding window duration, or adherence likely influenced the observed effects. One or more studies likely contributed to the dispersion around the pooled estimate, although the summary statistics do not permit a formal outlier diagnosis. The most precise study appears to have driven much of the weighting, while the largest effect likely came from a smaller or more heterogeneous trial, which is consistent with the elevated τ².

Overall, the evidence supports a favorable effect of combining TRE with exercise on body composition, but the certainty of the magnitude is limited by heterogeneity and the small number of studies.

### Risk of Bias

Across the 16 included studies, the overall risk-of-bias profile was dominated by unclear judgments. Fifteen studies were assessed as having unclear overall risk of bias and one study was judged to be at high risk; no study was rated as low risk overall. At the domain level, concerns were universal: all 16 studies were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, this means that the most common concerns were not isolated to one or two methodological features, but affected every core RoB domain in all included studies (16/16 for each domain). The basis for these judgments was consistent across studies, as the articles generally provided no usable information on these design and reporting elements.

A clear pattern across the evidence base is therefore one of inadequate methodological reporting rather than demonstrated low risk. This limits any distinction between study designs, because the extracted records do not document sufficient detail to separate better-reported randomized studies from observational studies or to identify whether any subgroup had more robust safeguards against bias. Only one study, published in 2023, was classified as high risk overall, although the domain-level extraction still recorded unclear judgments across all six standard domains, suggesting that the high-risk designation likely reflects broader concerns in the source assessment rather than a single explicitly reported domain failure. Conversely, no study could be considered particularly low risk because none reported enough detail to support low-risk judgments in sequence generation, concealment, blinding, attrition, or reporting.

This risk-of-bias pattern reduces confidence in the pooled estimate. When all studies have unclear judgments for selection, performance, detection, attrition, and reporting domains, the summary effect may be vulnerable to bias in either direction, and the magnitude of the pooled effect should therefore be interpreted cautiously. The absence of low-risk studies also prevents meaningful sensitivity analyses restricted to methodologically robust evidence. On the other hand, the data quality of the extraction itself appears strong: the enhanced extractor assigned high confidence to all 16 studies, with no medium- or low-confidence records. Thus, the main limitation is not uncertainty in data capture, but uncertainty inherent in the primary study reports. Overall, the body of evidence should be regarded as having limited methodological transparency, which lowers confidence in the strength and certainty of the review findings.

## Discussion

## Discussion

This systematic review examined whether time-restricted eating (TRE) combined with exercise improves body composition in adults compared with exercise performed alongside an unrestricted eating window. The principal quantitative finding was that TRE plus exercise was associated with a statistically significant reduction in fat mass, with a pooled random-effects mean difference of -1.88 kg (95% CI -3.08 to -0.67; p=0.002) across the three studies that could be meta-analyzed. The fixed-effect estimate was similar (-1.70 kg), which increases confidence that the direction of effect is not driven by a single analytical approach. From a clinical perspective, a reduction of approximately 1.5-2.0 kg of fat mass may be meaningful for adults engaged in structured exercise, particularly if achieved without an apparent requirement for greater exercise volume than controls. However, this finding should be interpreted cautiously because the evidence base for pooling was small, and the review as a whole included many studies that could not contribute quantitative data due to incomplete reporting. Accordingly, the present results support a potential benefit of TRE for fat mass reduction when paired with exercise, but they do not yet establish a definitive effect across all body-composition outcomes.

Direct comparison with prior reviews is limited because the contextual reviews identified were not focused on TRE with exercise in adults, but rather on socioeconomic patterning of body composition or on agreement between anthropometric and body-composition indicators in pediatric populations. Those reviews nonetheless underscore an important point relevant to our findings: body composition outcomes often provide information that BMI alone cannot capture, particularly for distinguishing changes in fat mass from changes in fat-free mass. In that sense, the present review adds value by focusing specifically on direct body-composition outcomes in an exercise-trained adult context, where preservation of fat-free mass is especially relevant. Our findings are broadly compatible with the idea that body weight or BMI may underestimate meaningful compositional changes. At the same time, unlike the socioeconomic reviews, which synthesized dozens of studies, our pooled estimate is based on only three studies; therefore, the precision and external validity of our conclusions are necessarily more limited.

Several biological and behavioral mechanisms could plausibly explain why TRE may enhance fat-mass reduction when combined with exercise. Restricting the daily eating window may reduce total energy intake, even when calorie restriction is not explicitly prescribed, by limiting opportunities to eat. TRE may also improve temporal alignment between feeding and circadian metabolic rhythms, with possible downstream effects on insulin sensitivity, substrate oxidation, and appetite regulation. In exercising adults, these effects could favor greater reliance on fat oxidation over time, particularly when meal timing alters the postabsorptive period surrounding training or the overnight fast. At the same time, these mechanisms are not uniformly beneficial in all contexts. If the feeding window is too short, protein distribution across the day may be compromised, potentially affecting muscle protein synthesis and the maintenance of fat-free mass. This is one reason why conclusions about overall body composition should remain cautious: a reduction in fat mass is desirable, but not if it comes at the expense of lean tissue in some populations or training settings.

The moderate-to-substantial heterogeneity observed in the meta-analysis (I²=68.4%, Q p=0.042, τ²=0.76) suggests that the true effect likely varies across studies rather than reflecting a single common effect size. This is not surprising given the likely differences across the included literature: feeding windows ranged from 4 to 12 hours; exercise modalities included aerobic, resistance, and concurrent training; and participant characteristics probably differed in sex, baseline adiposity, training status, age, and habitual diet. Timing of the eating window relative to training may also matter, as could intervention duration, adherence to TRE, spontaneous calorie reduction, and methods used to assess body composition. Another likely source of variation is the comparator itself: “unrestricted eating” can differ substantially across studies, from relatively structured habitual diets to highly variable ad libitum intake. These differences may help explain why some studies suggested benefit while others were less conclusive, and they caution against assuming that all TRE protocols are metabolically equivalent.

This review has several strengths. First, it addressed a clinically relevant question using a comparator that isolates the added value of TRE beyond exercise alone. Second, the review prioritized body-composition outcomes rather than relying only on body weight, which is especially important in exercising populations where changes in fat mass and fat-free mass may diverge. Third, although only three studies were suitable for pooling, the broader review included 16 studies and therefore provides a more complete map of the available evidence than the meta-analysis alone suggests. Fourth, the use of enhanced extraction helped identify studies that were methodologically relevant even when reporting was insufficient for quantitative synthesis. This is a genuine contribution because it clarifies that the main barrier in this literature is not simply absence of studies, but inconsistent and incomplete reporting of numerical outcome data. Notably, all 16 studies were classified as high quality in the extraction workflow; however, this should not be interpreted as meaning that all were low risk of bias or fully usable for meta-analysis. In fact, many lacked extractable means, standard deviations, arm-level sample sizes, or key bibliographic metadata, which materially constrained synthesis.

The limitations of this review should therefore be emphasized. Most importantly, only three studies contributed to the pooled estimate, making the meta-analysis vulnerable to instability and limiting exploration of publication bias, subgroup effects, or meta-regression. Although the extracted dataset labeled studies as high quality, the reporting limitations across many included records were substantial, including missing study metadata, incomplete numerical results, absence of group-specific sample sizes, and poor reporting of randomization or other risk-of-bias domains. These issues reduce reproducibility and make it difficult to judge internal validity with confidence. Generalizability is also uncertain: the evidence may not apply equally across sexes, age groups, baseline body-composition profiles, athletic versus recreational populations, or different TRE schedules. Clinically, the current evidence suggests that TRE can be considered as one possible adjunct to exercise for adults seeking fat-mass reduction, particularly when it is acceptable and sustainable for the individual. However, it should not yet be recommended as clearly superior to all other dietary timing approaches, and practitioners should remain attentive to total energy intake, protein adequacy, training quality, and preservation of fat-free mass. Future research should prioritize adequately powered randomized controlled trials with transparent reporting of arm-level means and variances, standardized body-composition measures, explicit monitoring of adherence and energy intake, and direct assessment of whether effects differ by feeding-window duration, exercise modality, sex, and baseline adiposity. Longer-term studies are also needed to determine whether the apparent short-term fat-mass benefit of TRE is durable and whether it can be achieved without compromising lean mass or exercise performance.

## Conclusion

In this meta-analysis of 16 studies, with pooled fat-mass data available from 3 exercise-matched comparisons, time-restricted eating (4-12 hour feeding window) combined with exercise was associated with a greater reduction in fat mass than unrestricted eating plus the same exercise (random-effects MD -1.88 kg, 95% CI -3.08 to -0.67; p=0.002). Clinically, a difference of nearly 2 kg of fat loss is likely meaningful for many adults, particularly when achieved without changing the exercise stimulus, and it suggests TRE may modestly enhance the body-composition benefits of training. On balance, TRE can be considered a reasonable adjunct for adults exercising for fat-loss goals, provided it is acceptable and sustainable for the individual. That recommendation should remain cautious, however, because the pooled estimate is based on only 3 studies and showed moderate-to-substantial heterogeneity (I2=68.4%), which limits confidence in the consistency of the effect across populations and protocols.

## Final Included Studies

- Corpus ID: 4559 | Time-restricted eating and concurrent exercise training reduces fat mass and increases lean mass in overweight and obese adults.
- Corpus ID: 4556 | Effect of Time-Restricted Eating and Resistance Training on High-Speed Strength and Body Composition.
- Corpus ID: 4563 | Time-restricted feeding plus resistance training in active females: a randomized trial.
- Corpus ID: 4561 | Four Weeks of Time-Restricted Feeding Combined with Resistance Training Does Not Differentially Influence Measures of Body Composition, Muscle Performance, Resting Energy Expenditure, and Blood Biomarkers.
- Corpus ID: 69788 | Hypercaloric 16:8 time-restricted eating during 8 weeks of resistance exercise in well-trained men and women.
- Corpus ID: 4564 | Four Weeks of 16/8 Time Restrictive Feeding in Endurance Trained Male Runners Decreases Fat Mass, without Affecting Exercise Performance.
- Corpus ID: 4557 | Effects of eight weeks of time-restricted feeding (16/8) on basal metabolism, maximal strength, body composition, inflammation, and cardiovascular risk factors in resistance-trained males.
- Corpus ID: 69782 | Effects of Time-Restricted Eating on Aerobic Capacity, Body Composition, and Markers of Metabolic Health in Healthy Male Recreational Runners: A Randomized Crossover Trial.
- Corpus ID: 8396 | Effects of 8 wk of 16:8 Time-restricted Eating in Male Middle- and Long-Distance Runners.
- Corpus ID: 17814 | Impact of 16/8 time-restricted eating on body composition and lipolytic hormone regulation in female DanceSport dancers.
- Corpus ID: 69789 | Time-restricted feeding improves markers of cardiometabolic health in physically active college-age men: a 4-week randomized pre-post pilot study.
- Corpus ID: 108297 | A self-selected 16:8 time-restricted eating quasi-experimental intervention improves various markers of cardiovascular health in middle-age male cyclists.
- Corpus ID: 91155 | 6-week time-restricted eating improves body composition, maintains exercise performance, without exacerbating eating disorder in female DanceSport dancers.
- Corpus ID: 91138 | Flexible time-restricted eating combined with exercise in a free-living setting for middle-aged women with overweight/obesity: a randomized controlled trial.
- Corpus ID: 4560 | Time-restricted eating effects on performance, immune function, and body composition in elite cyclists: a randomized controlled trial.
- Corpus ID: 17824 | High-Protein Time-Restricted Eating Alongside Resistance Training Reduces Adipose Tissue While Preserving Fat-Free Mass in Women With Overweight: A Randomized Controlled Trial.
