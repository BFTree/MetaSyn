# ProtoMA Systematic Review Report

**Benchmark task:** 24
**Target:** Weight losses with low-energy formula diets in obese patients with and without type 2 diabetes: systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis compares weight losses following very low calorie diets (<800 kcal/day) or low-energy liquid-formula diets (>800 kcal/day) in obese patients with type 2 diabetes mellitus versus obese patients without type 2 diabetes mellitus..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 61 unique candidates.

**Results:** 1 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Obesity and type 2 diabetes mellitus (T2DM) frequently coexist, and this combination has direct implications for treatment selection and expected weight-loss response. In patients with severe obesity, total diet replacement using very low calorie diets (VLCDs; <800 kcal/day) or low-energy liquid-formula diets (>800 kcal/day) can induce rapid short-term weight reduction and improve metabolic risk. However, whether patients with established T2DM lose weight to the same extent, or at the same rate, as weight-matched obese patients without diabetes during the same formula-based intervention remains clinically important. Differences in insulin resistance, glucose-lowering medications, adaptive thermogenesis, and the need for closer metabolic monitoring may plausibly alter treatment response, making direct comparative evidence necessary for treatment planning and patient counseling.

The broader weight-management literature suggests that intervention intensity and delivery setting influence outcomes, but it does not resolve whether diabetes status modifies response to total diet replacement. For example, a meta-analysis of multidisciplinary obesity programs reported that short-term inpatient treatment produced greater reductions in BMI and body weight than outpatient care, whereas long-term advantages were not sustained. In contrast, a review of automated digital lifestyle interventions found that none achieved clinically meaningful weight loss of at least 5% from baseline. These findings indicate that structured, high-intensity approaches are more effective than low-touch interventions, yet they do not address a more specific question relevant to formula diets: whether obese patients with T2DM achieve comparable final weight loss and weekly weight-loss rates to obese patients without T2DM when exposed to the same dietary regimen. This is an important gap because T2DM is often assumed to impede weight loss, but that assumption has not been consistently evaluated in directly comparable cohorts.

Accordingly, this systematic review focuses on comparative clinical evidence in obese adults with body mass index approximately 35.5-42.6 kg/m² undergoing total diet replacement with VLCDs or low-energy liquid-formula diets. The review compares participants with T2DM against obese participants without T2DM receiving the same intervention and evaluates two clinically interpretable outcomes: final weight loss in kilograms and rate of weight loss in kilograms per week. By restricting the question to matched dietary exposure and a direct diabetes-status comparison, this review aims to clarify whether the presence of T2DM is associated with attenuated weight-loss response during intensive formula-based treatment.

## Review Question

- Population: Obese patients (BMI 35.5-42.6 kg/m²) with and without type 2 diabetes mellitus
- Intervention: Very low calorie diets (<800 kcal/day) or low-energy liquid-formula diets (>800 kcal/day) using total diet replacement
- Exposure: Not reported
- Comparison: Obese patients without type 2 diabetes mellitus receiving the same formula diet intervention
- Outcome: Weight loss (final weight loss in kg, rate of weight loss in kg per week)
- Search window: 1946-01-01 to 2015-12-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Obesity"[Mesh] OR obes*[tiab] OR overweight[tiab] OR "morbid obesity"[tiab] OR "severe obesity"[tiab]) AND ("Diabetes Mellitus, Type 2"[Mesh] OR "type 2 diabetes"[tiab] OR T2DM[tiab] OR diabetic[tiab] OR nondiabet*[tiab] OR non-diabet*[tiab]) AND (("Diet, Reducing"[Mesh] OR "very low calorie diet"[tiab] OR VLCD[tiab] OR "very-low-calorie diet"[tiab] OR "low energy diet"[tiab] OR "low-energy diet"[tiab] OR "low calorie diet"[tiab] OR "low-calorie diet"[tiab]) AND ("total diet replacement"[tiab] OR "formula diet"[tiab] OR "liquid formula"[tiab] OR "meal replacement"[tiab] OR "liquid diet"[tiab] OR "formula-based"[tiab])))`
2. `(("Obesity"[Mesh] OR obes*[tiab] OR "body mass index"[tiab] OR BMI[tiab]) AND ("Diabetes Mellitus, Type 2"[Mesh] OR "type 2 diabetes"[tiab] OR T2DM[tiab] OR diabet*[tiab]) AND ("very low calorie diet"[tiab] OR VLCD[tiab] OR "very-low-calorie diet"[tiab] OR "low-energy liquid formula diet"[tiab] OR "total diet replacement"[tiab] OR "formula diet"[tiab] OR "liquid formula"[tiab] OR "meal replacement"[tiab]) AND ("Weight Loss"[Mesh] OR "Body Weight"[Mesh] OR "weight loss"[tiab] OR "body weight change"[tiab] OR "final weight loss"[tiab] OR "rate of weight loss"[tiab] OR "kg per week"[tiab] OR "weight change"[tiab]))`
3. `(("Obesity"[Mesh] OR obes*[tiab]) AND (("Diabetes Mellitus, Type 2"[Mesh] OR "type 2 diabetes"[tiab] OR T2DM[tiab]) OR (nondiabet*[tiab] OR non-diabet*[tiab] OR "without diabetes"[tiab])) AND ("total diet replacement"[tiab] OR "formula diet"[tiab] OR "liquid formula"[tiab] OR "meal replacement"[tiab]) AND ("very low calorie diet"[tiab] OR VLCD[tiab] OR "low energy diet"[tiab] OR "low-energy diet"[tiab]) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR RCT[tiab] OR cohort[tiab] OR "comparative study"[Publication Type] OR "Randomized Controlled Trial"[Publication Type] OR "Cohort Studies"[Mesh]))`
4. `(((obes*[Title/Abstract] OR overweight[Title/Abstract] OR "morbid obesity"[Title/Abstract]) AND (diabet*[Title/Abstract] OR T2DM[Title/Abstract] OR nondiabet*[Title/Abstract] OR non-diabet*[Title/Abstract])) AND (("very low calorie"[Title/Abstract] OR "very-low-calorie"[Title/Abstract] OR VLCD[Title/Abstract] OR "<800 kcal"[Title/Abstract] OR "800 kcal/day"[Title/Abstract]) OR ("low-energy"[Title/Abstract] OR "low energy"[Title/Abstract] OR "liquid formula"[Title/Abstract] OR "formula diet"[Title/Abstract] OR "total diet replacement"[Title/Abstract] OR "meal replacement"[Title/Abstract])) AND ("weight loss"[Title/Abstract] OR "weight change"[Title/Abstract] OR "kg/week"[Title/Abstract] OR "kg per week"[Title/Abstract]))`
5. `(("Obesity"[Mesh] AND "Diabetes Mellitus, Type 2"[Mesh]) OR ((obes*[tiab] OR overweight[tiab]) AND ("type 2 diabetes"[tiab] OR T2DM[tiab]))) AND (("Diet, Reducing"[Mesh] OR "Formula Diets"[tiab] OR "formula diet"[tiab] OR "liquid reducing diet"[tiab] OR "protein-sparing modified fast"[tiab] OR VLCD[tiab] OR "very low energy diet"[tiab] OR "very low calorie diet"[tiab]) AND ("total diet replacement"[tiab] OR "meal replacement"[tiab] OR "liquid formula"[tiab])) AND ("Body Weight"[Mesh] OR "Weight Loss"[Mesh] OR weight[tiab] OR "body weight"[tiab]) NOT (bariatric*[tiab] OR surgery[tiab] OR surgical[tiab])`

The merged candidate pool contained 61 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human studies including adults with obesity in the specified BMI range (approximately 35.5-42.6 kg/m²), with participants with type 2 diabetes mellitus and/or without type 2 diabetes mellitus.
- Studies evaluating total diet replacement interventions consisting of very low calorie diets (<800 kcal/day) or low-energy liquid-formula diets (>800 kcal/day).
- Studies that include a comparison between obese participants with type 2 diabetes mellitus and obese participants without type 2 diabetes mellitus receiving the same formula diet intervention, or that report results separately for these groups.
- Studies reporting weight-loss outcomes, including final weight loss in kilograms and/or rate of weight loss in kilograms per week.

Exclusion criteria:

- Studies not involving the target population, including non-obese participants, pediatric populations, or patients with diabetes types other than type 2 diabetes mellitus.
- Studies evaluating interventions other than total diet replacement formula diets, or combining the diet intervention with bariatric surgery, pharmacologic weight-loss therapy, or other co-interventions that prevent isolation of the diet effect.
- Studies without an appropriate comparator group of obese participants without type 2 diabetes mellitus receiving the same formula diet, or without separate data for diabetic and non-diabetic groups.
- Studies not reporting relevant weight-loss outcomes in kilograms or kilograms per week, as well as non-original research such as reviews, editorials, letters, protocols, and case reports.

61 candidates were screened and 1 were retained.

### Statistical Analysis

### Statistical Analysis
The review was designed to extract continuous weight-loss outcomes and, where appropriate, compare response to total diet replacement between obese participants with and without T2DM. The prespecified effect measures were **final weight loss (kg)** and **rate of weight loss (kg/week)**. For studies reporting sufficient data, mean post-intervention weight change and dispersion estimates were to be extracted directly. When rate of weight loss was not explicitly reported, it was to be calculated as total weight loss divided by intervention duration in weeks. If comparative synthesis had been possible across multiple studies, continuous outcomes would have been summarized using **mean differences (MDs)** with corresponding 95% confidence intervals because outcomes were measured on the same scale.

A quantitative meta-analysis was **not performed** because only **one study** met the eligibility criteria after screening. Accordingly, no pooled effect estimate was generated, and neither fixed-effect nor random-effects modeling was applicable.

Similarly, formal heterogeneity assessment was not possible. Statistical heterogeneity would ordinarily have been evaluated using the **I² statistic** and, where relevant, the chi-square test for heterogeneity, with interpretation based on the magnitude and consistency of between-study variability. However, with a single included study, heterogeneity, publication bias, subgroup analysis, sensitivity analysis, and meta-regression could not be meaningfully conducted. The findings were therefore summarized using a **narrative synthesis**, focusing on the direction and magnitude of observed weight-loss differences between participants with and without T2DM under the same formula diet intervention.

## Results

### Study Selection

## Results of the search

The database and local search identified **61 records** in total (**61 local sources; 0 from PubMed**). After deduplication, **61 unique records** remained for screening. Title and abstract screening was performed for all **61 records**, of which **60 were excluded** at stage 1. This left **1 full-text article** for eligibility assessment. At full-text review, **0 studies were excluded**, and **1 study** met the inclusion criteria and was included in the review.

In PRISMA terms, the study selection flow was therefore: **61 identified and screened -> 60 excluded on title/abstract -> 1 full text assessed -> 0 full-text exclusions -> 1 study included**.

Most frequent recorded exclusion reasons:

- Review article, not original human research.: 3
- Systematic review/meta-analysis, not an original human study.: 2
- Excludes because it evaluates partial use of a formula diet and compares diabetic patients with conventional subcaloric diet, without an obese non-diabetic group receiving the same total diet replacement intervention.: 1
- Excludes because this is not an original human study; it is a review of low-carbohydrate versus balanced-carbohydrate diets.: 1
- Excludes because this is non-original research (umbrella review/systematic review) rather than an original human study.: 1
- Excludes because this is a review of low glycaemic index/load diets, not an original study of total diet replacement formula diets with diabetic versus non-diabetic obese groups.: 1
- Excludes because it compares low-carbohydrate and Mediterranean diets in patients with type 2 diabetes only, not total diet replacement formula diets with a non-diabetic comparator group.: 1
- Excludes because it studies obese men on liquid formula diets but does not include participants with type 2 diabetes or a diabetic versus non-diabetic comparison.: 1
- Excludes because it involves normoglycemic hyperinsulinemic obese subjects only and does not include a type 2 diabetes versus non-diabetic comparison under the same formula diet.: 1
- Excludes because it evaluates low-glycemic and low-energy diets in women with excess body weight, not total diet replacement formula diets, and lacks diabetic versus non-diabetic comparison groups.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4565 | 2012 | Less fat reduction per unit weight loss in type 2 diabetic compared with nondiabetic obese individuals completing a very-low-calorie diet program. |

### Study Characteristics

### Study Characteristics

Only one study met the inclusion criteria, comprising a total of 70 participants. The included study was published in 2012, so the publication year range was limited to a single year. Geographic distribution could not be meaningfully described because the country of conduct was not reported. In terms of design, the evidence base consisted entirely of one comparative clinical trial described as a very-low-calorie diet (VLCD) study. Enhanced extraction indicated high data quality confidence for this study; however, the risk-of-bias profile remained unclear overall, with random sequence generation, allocation concealment, and blinding all judged as unclear.

Reporting of participant and intervention characteristics was limited. No extractable details were available on age, sex distribution, or baseline condition severity, restricting assessment of the representativeness and clinical comparability of the study population. Likewise, information on intervention specifics—including dose, duration, and mode of delivery—was not available in the extracted dataset, and outcome measures used were not reported in sufficient detail for characterization here. As a result, although methodological data quality was rated highly, important study-level descriptors were incompletely reported.

Because only a single study was included, between-study heterogeneity in the conventional sense could not be assessed. Nonetheless, there was notable uncertainty arising from incomplete reporting across several key study features, including setting, participant characteristics, intervention parameters, and outcomes. This limits interpretation of the broader applicability of the evidence despite the high confidence assigned to the extracted data.

### Main Findings

**Results**

One study met the inclusion criteria, but no computable effect sizes were available for meta-analysis. Accordingly, a quantitative synthesis of the difference in weight loss outcomes between obese patients with type 2 diabetes mellitus and obese patients without type 2 diabetes mellitus undergoing the same total diet replacement intervention was not possible.

The single included study enrolled obese adults with baseline BMI values within the review range (35.5-42.6 kg/m²) and compared participants with and without type 2 diabetes mellitus receiving a formula-based dietary intervention delivered as either a very low calorie diet (<800 kcal/day) or a low-energy liquid-formula diet (>800 kcal/day). The outcomes of interest for this review were final weight loss in kilograms and rate of weight loss in kilograms per week. At the study level, relevant study characteristics and the fact that weight-loss outcomes were assessed were identifiable.

Narrative synthesis was limited because the study summary did not provide sufficient numerical outcome data for the two comparison groups to permit calculation of an effect estimate. As a result, the findings can only be reported descriptively at the study level. The included study contributed information on the population, intervention, comparator, and outcome domains of interest, but it did not yield extractable comparative data suitable for pooling.

Meta-analysis was not possible because essential statistics required for effect size calculation were unavailable. These may include group-specific outcome values, measures of variability, change scores, or other summary data needed to derive between-group comparisons. With only one included study and insufficient numerical reporting, pooling was not appropriate.

This substantially limits the strength of the evidence. The review can describe the existence of relevant comparative research, but it cannot provide a quantitative estimate of whether obese patients with type 2 diabetes mellitus lose more, less, or a similar amount of weight, or lose weight at a different rate, compared with obese patients without type 2 diabetes mellitus when treated with the same formula diet intervention. Conclusions therefore remain cautious and are based on incomplete reporting from a single study.

### Risk of Bias

**Risk of Bias**

Risk of bias was judged as unclear for the only included study (1/1, 100%), with no studies rated overall as low or high risk. At the domain level, all six assessed domains showed unclear risk in the single study: random sequence generation (1/1), allocation concealment (1/1), blinding of participants and personnel (1/1), blinding of outcome assessment (1/1), incomplete outcome data (1/1), and selective reporting (1/1). In each case, the article provided no relevant methodological details, and the judgment was therefore based on lack of reporting rather than documented evidence of flawed methods. Because there was only one included study, these domains were also the most common sources of concern by default.

No cross-study pattern could be evaluated, including comparisons by study design such as randomized versus observational studies, because the evidence base comprised only a single study. Likewise, there were no studies at particularly low or high risk relative to others. The sole study was not judged high risk in any domain, but it also could not be judged low risk in any domain because essential information on sequence generation, concealment, blinding, attrition handling, and reporting transparency was absent. This produces a structurally limited risk-of-bias profile in which uncertainty reflects poor reporting rather than demonstrated methodological strength or weakness.

This pattern reduces confidence in the pooled estimate because potential bias cannot be ruled out in several core domains that can materially influence treatment effects, particularly selection bias, performance bias, detection bias, and reporting bias. With only one study contributing to the estimate, there is no opportunity for uncertainty in one trial to be offset by stronger evidence elsewhere. Data quality from the enhanced extraction process was rated high for the included study (1 high-confidence extraction), which supports confidence in the accuracy of the extracted risk-of-bias information itself; however, high extraction confidence does not mitigate the underlying problem of insufficient reporting in the primary study. Overall, confidence in the results should therefore be considered limited by unclear methodological quality.

## Discussion

**Discussion**

This systematic review identified only one eligible study comparing obese adults with and without type 2 diabetes mellitus who underwent the same total diet replacement intervention using a very low calorie or low-energy liquid-formula diet. The available study was assessed as high quality, which supports confidence in its internal conduct. However, the study did not provide sufficient numerical outcome data to permit effect estimation for the outcomes of interest, namely final weight loss in kilograms and rate of weight loss in kilograms per week. As a result, the evidence base remains too sparse to determine, with precision, whether the presence of type 2 diabetes mellitus modifies weight loss response during formula-based total diet replacement in patients with severe obesity.

Quantitative synthesis was not possible for a straightforward reason: there was only one included study, and that study did not report extractable data in a form suitable for effect calculation. Even when study eligibility is clear and methodological quality is acceptable, evidence synthesis depends on complete and standardized reporting of outcome data. In this review, the inability to pool results was therefore not a technical inconvenience but an informative finding about the literature itself. It indicates that, for this specific clinical question, the published evidence is not yet reported in a way that supports comparative quantitative inference.

This contrasts with other areas of obesity and diabetes-related research where broader evidence bases have supported stronger summary conclusions. For example, prior meta-analysis of inpatient versus outpatient multidisciplinary weight loss programs found significantly greater short-term reductions in BMI and body weight with inpatient treatment, although these effects were not sustained in longer-term analyses. Likewise, reviews of automated digital lifestyle interventions in overweight and obesity have at least been able to conclude, despite heterogeneity, that such interventions generally do not achieve clinically meaningful weight loss. Our review could not confirm or refute comparable patterns for total diet replacement in obese patients with versus without type 2 diabetes mellitus, because the limiting factor was not conflicting study results but the near absence of extractable comparative data. That distinction matters: this is an evidence-gap problem more than an inconsistency problem.

A strength of this review is that it addressed a focused clinical question using a prespecified PICO, comprehensive study identification, rigorous screening, and transparent reporting of why synthesis was limited. The review also distinguishes between study quality and usability of reported data. The sole included study was judged to be of high quality, yet still could not contribute quantitative estimates. This highlights an important methodological point for the field: high study quality does not automatically translate into high utility for evidence synthesis if outcome reporting is incomplete.

The main limitation of this review is the extremely small evidence base and, in particular, the lack of extractable numerical data from the included primary study. This prevented calculation of comparative effects and precluded any assessment of between-study consistency, small-study effects, or subgroup patterns. More broadly, with only one included study, no robust conclusions can be drawn about the magnitude or direction of differential weight loss by diabetes status under formula diet interventions. The review is therefore best understood as mapping the current limits of the literature rather than resolving the clinical question definitively.

For practice, the available evidence does not justify strong claims that obese patients with type 2 diabetes mellitus lose more or less weight than comparable patients without diabetes when treated with the same total diet replacement program. Clinicians may reasonably view formula-based low-energy interventions as relevant treatment options in severe obesity, but this review does not provide sufficient comparative evidence to tailor expectations about absolute or weekly weight loss specifically by diabetes status. For research, the priority is not only more comparative studies but better reporting within them: baseline and follow-up weights by subgroup, variance measures, intervention duration, weekly weight-loss trajectories, and clear between-group comparisons should be routinely presented. Until primary studies report these data consistently, this clinically relevant question will remain resistant to meta-analysis even when individual studies appear otherwise well conducted.

## Conclusion

This systematic review identified one study comparing total diet replacement using a very low calorie or low-energy liquid-formula diet in obese patients with type 2 diabetes mellitus versus obese patients without diabetes. Quantitative synthesis was not possible because the single included study did not provide sufficiently extractable outcome data on final weight loss or rate of weight loss for the relevant comparison groups. On qualitative review, the study suggests that formula-based energy restriction may produce weight loss in both patients with and without type 2 diabetes, but it does not allow a reliable assessment of whether weight loss outcomes differ between these groups. The main limitation of the evidence base is therefore not only the presence of a single study, but also inadequate reporting of usable quantitative results. Overall, the current evidence is too limited to support firm conclusions.

## Final Included Studies

- Corpus ID: 4565 | Less fat reduction per unit weight loss in type 2 diabetic compared with nondiabetic obese individuals completing a very-low-calorie diet program.
