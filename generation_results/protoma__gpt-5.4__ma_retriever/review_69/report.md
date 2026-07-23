# ProtoMA Systematic Review Report

**Benchmark task:** 69
**Target:** The effectiveness and usability of online, group-based interventions for people with severe obesity: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis examines the effectiveness of online, group-based behavior change interventions for adults with severe obesity (BMI ≥ 35 kg/m²) in achieving weight loss and positive health behavior changes compared to waitlist or standard care conditions, while also exploring user perceptions of acceptability and usability..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 89 unique candidates.

**Results:** 0 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Severe obesity in adults, commonly defined as a body mass index (BMI) of at least 35 kg/m², is associated with substantially elevated risks of type 2 diabetes, cardiovascular disease, obstructive sleep apnea, osteoarthritis, and premature mortality, while also imposing major functional, psychosocial, and healthcare-system consequences. For this population, clinically meaningful weight reduction is often difficult to achieve and sustain, particularly when treatment relies on repeated in-person contact that may be limited by travel demands, work schedules, stigma, mobility constraints, and service availability. Online, group-based behavior change interventions are a plausible response to these barriers because they can deliver structured weight-management support at scale while preserving peer interaction, accountability, and facilitator guidance, all of which are central features of behavioral treatment. However, the extent to which this format is effective and acceptable specifically for adults with severe obesity remains unclear.

The broader digital weight-management literature suggests potential benefit, but it does not resolve this question. An umbrella review of 46 systematic and scoping reviews found that digital interventions targeting diet, physical activity, sedentary behavior, and weight management were generally effective across adult populations, although engagement findings were mixed and the overall review quality was low. More targeted evidence from behavioral intervention research also indicates that outcomes may vary according to participant characteristics; for example, a meta-analysis of 15 trials (N=2,535) reported greater 12-month weight benefit from Acceptance and Commitment Therapy-based behavioral weight management interventions among participants with medium versus high internal disinhibition. Yet these syntheses largely combine adults across broad BMI ranges, intervention modalities, and delivery formats, limiting their applicability to adults with BMI ≥35 kg/m² and to interventions delivered specifically online in a group-based format. In addition, user-centered outcomes such as acceptability, usability, and overall experience are often treated as secondary considerations despite their importance for uptake, retention, and real-world implementation.

Accordingly, this systematic review was designed to evaluate evidence on online, group-based behavior change interventions for weight management in adults with severe obesity (BMI ≥35 kg/m²), compared with waitlist or standard care conditions. The review aimed to assess effects on weight loss and weight-related behavior changes, and to synthesize evidence on participant perceptions of acceptability, usability, and overall intervention experience. No eligible studies were identified. This absence of evidence is itself an important finding, indicating that a clinically high-risk population and a scalable intervention model have not yet been adequately connected within the comparative literature.

## Review Question

- Population: Adults with severe obesity (BMI ≥ 35 kg/m²)
- Intervention: Online, group-based behavior change interventions for weight management
- Exposure: Not reported
- Comparison: Waitlist or standard care conditions
- Outcome: Weight loss, weight-related behavior changes, and user perceptions of acceptability, usability, and overall experience
- Search window: Not reported to 2024-05-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Obesity, Morbid"[Mesh] OR "Obesity"[Mesh] OR obes*[tiab] OR "severe obes*"[tiab] OR "morbid obes*"[tiab] OR "class II obes*"[tiab] OR "class III obes*"[tiab] OR "BMI 35"[tiab] OR "body mass index 35"[tiab]) AND ("Internet-Based Intervention"[tiab] OR "online"[tiab] OR "web-based"[tiab] OR "internet-based"[tiab] OR "digital"[tiab] OR "eHealth"[tiab] OR "mHealth"[tiab] OR telehealth[tiab] OR telemedicine[Mesh] OR "social media"[tiab] OR videoconference*[tiab]) AND (group*[tiab] OR peer*[tiab] OR collectiv*[tiab] OR "group-based"[tiab] OR "group intervention"[tiab] OR "group program*"[tiab] OR cohort*[tiab]) AND ("Behavior Therapy"[Mesh] OR "behavior change"[tiab] OR behavioural[tiab] OR behavioral[tiab] OR "lifestyle intervention"[tiab] OR counsel*[tiab] OR coaching[tiab] OR self-monitor*[tiab] OR "weight management"[tiab] OR "weight loss program*"[tiab])`
2. `(("Obesity, Morbid"[Mesh] OR "obesity, severe"[tiab] OR "morbid obesity"[tiab] OR "severe obesity"[tiab] OR "class III obesity"[tiab] OR "BMI >=35"[tiab] OR "BMI ≥35"[tiab] OR "body mass index"[tiab]) AND ("Weight Loss"[Mesh] OR "Body Weight"[Mesh] OR "weight loss"[tiab] OR "weight reduction"[tiab] OR "weight change"[tiab] OR adiposity[tiab]) AND ("Internet"[Mesh] OR online[tiab] OR "web based"[tiab] OR "web-based"[tiab] OR "digital intervention"[tiab] OR "remote intervention"[tiab] OR telehealth[tiab]) AND (group*[tiab] OR "group visit*"[tiab] OR "group session*"[tiab] OR "peer support"[tiab]) AND ("Behavior Therapy"[Mesh] OR "Health Behavior"[Mesh] OR "behavior change"[tiab] OR "behaviour change"[tiab] OR diet*[tiab] OR "physical activity"[tiab] OR exercise[tiab])) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR RCT[tiab] OR "Randomized Controlled Trial"[Publication Type])`
3. `("Adults"[Mesh] OR adult*[tiab]) AND ("Obesity, Morbid"[Mesh] OR obes*[tiab] OR "severe obesity"[tiab] OR "morbid obesity"[tiab]) AND (online[tiab] OR "internet-based"[tiab] OR "web-based"[tiab] OR digital[tiab] OR eHealth[tiab] OR telehealth[tiab]) AND (group*[tiab] OR "group-based"[tiab] OR peer*[tiab]) AND ("weight management"[tiab] OR "weight loss"[tiab] OR diet*[tiab] OR exercise[tiab] OR "physical activity"[tiab]) AND (waitlist[tiab] OR "wait-list"[tiab] OR "usual care"[tiab] OR "standard care"[tiab] OR control[tiab] OR comparator[tiab]) AND (acceptab*[tiab] OR usab*[tiab] OR satisfaction[tiab] OR feasibility[tiab] OR experience*[tiab] OR perception*[tiab] OR engagement[tiab] OR adherence[tiab])`
4. `(("Obesity, Morbid"[Mesh] OR "morbid obes*"[tiab] OR "severe obes*"[tiab] OR "class II obes*"[tiab] OR "class III obes*"[tiab]) AND ("Weight Reduction Programs"[Mesh] OR "weight management"[tiab] OR "weight loss intervention"[tiab] OR "lifestyle program*"[tiab]) AND ("Telemedicine"[Mesh] OR "Internet"[Mesh] OR online[tiab] OR "internet-delivered"[tiab] OR "web-delivered"[tiab] OR videoconference*[tiab] OR virtual[tiab]) AND (group*[tiab] OR "group coaching"[tiab] OR "group counseling"[tiab] OR "peer-led"[tiab]) AND (cohort[tiab] OR longitudinal[tiab] OR pragmatic[tiab] OR trial[tiab] OR randomized[tiab] OR randomised[tiab] OR controlled[tiab])) NOT (adolescent*[tiab] OR child*[tiab] OR pediatr*[tiab] OR pregnancy[tiab] OR pregnant[tiab])`
5. `("Obesity, Morbid"[Mesh] OR obes*[tiab] OR "BMI 35"[tiab] OR "BMI >= 35"[tiab] OR "BMI ≥ 35"[tiab]) AND (("online group"[tiab] OR "web-based group"[tiab] OR "internet group"[tiab] OR "virtual group"[tiab] OR "group-mediated"[tiab] OR "group-based"[tiab]) AND (behavior*[tiab] OR behaviour*[tiab] OR lifestyle[tiab] OR counsel*[tiab] OR coaching[tiab] OR self-management[tiab])) AND ("Weight Loss"[Mesh] OR "Feeding Behavior"[Mesh] OR "Motor Activity"[Mesh] OR "weight loss"[tiab] OR "eating behavior"[tiab] OR "dietary behavior"[tiab] OR "physical activity"[tiab] OR sedentary[tiab] OR acceptab*[tiab] OR usab*[tiab] OR "user experience"[tiab] OR satisfaction[tiab])`

The merged candidate pool contained 89 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies including adults aged 18 years or older with severe obesity, defined as BMI >= 35 kg/m2 or an equivalent clinical classification reported for the sample.
- Studies evaluating an online or digitally delivered, group-based behavior change intervention aimed at weight management, weight loss, or related lifestyle change.
- Studies using a waitlist, usual care, standard care, or similar minimal-intervention comparator condition.
- Studies reporting at least one relevant outcome: weight loss or body weight change, weight-related behavior change (for example diet or physical activity), or participant perceptions such as acceptability, usability, satisfaction, or overall experience.

Exclusion criteria:

- Studies focused on children or adolescents, mixed populations where adults with severe obesity cannot be distinguished, or samples not meeting the severe obesity threshold.
- Studies assessing interventions that are not online and group-based behavioral weight-management programs, including primarily in-person, individual-only, surgical, pharmacological, or non-weight-management interventions.
- Studies without a relevant comparator, or studies not reporting any eligible outcome related to weight, weight-related behaviors, or user perceptions of the intervention.
- Study designs not suitable for evaluating intervention effects or experiences, such as protocols, reviews, editorials, commentaries, conference abstracts without full data, or case reports.

89 candidates were screened and 0 were retained.

### Statistical Analysis

### Statistical Analysis
A quantitative synthesis was planned if a sufficient number of clinically and methodologically comparable studies were identified. For continuous outcomes such as body weight change, BMI change, or behavioral scale scores, the intended effect measure was the **mean difference (MD)** when studies used the same metric, or the **standardized mean difference (SMD)** when conceptually similar outcomes were measured using different instruments. For dichotomous outcomes, such as attainment of a prespecified weight-loss threshold or binary indicators of acceptability, the planned effect measure was the **risk ratio (RR)** with 95% confidence intervals.

Where data permitted, post-intervention and follow-up effect estimates would have been calculated from reported group means, standard deviations, change scores, and sample sizes. When necessary, standard errors, confidence intervals, p-values, or other summary statistics would have been converted into common effect-size metrics using standard meta-analytic methods. Outcome data would have been grouped by construct, including: **weight loss**, **weight-related behavior change**, and **user perceptions of acceptability/usability/overall experience**.

If pooling had been possible, between-study synthesis would have used a **random-effects model** as the default approach, given the anticipated heterogeneity in intervention format, behavioral content, duration, and outcome measurement. Statistical heterogeneity would have been assessed using the **I^2 statistic**, **tau^2**, and the **chi-square test for heterogeneity**. Prespecified qualitative consideration of heterogeneity would also have included variation in participant characteristics, intervention intensity, comparator type, and follow-up duration.

Subgroup or sensitivity analyses were planned only if enough studies were available, for example by intervention platform, program duration, or type of user-experience outcome. Publication bias assessment, such as funnel-plot inspection, would only have been considered if an adequate number of studies were available for a given pooled outcome.

### Review Outcome
**No meta-analysis was performed**, because **no studies met the inclusion criteria**. Accordingly, no effect sizes were computed, no pooled models were fitted, and no statistical heterogeneity or reporting-bias analyses were undertaken.

## Results

### Study Selection

### Results of the search
The database and local search yielded **89 records** in total (**89 local sources; 0 from PubMed**). After deduplication, **89 unique records** remained for title and abstract screening. At stage 1, **all 89 records were excluded** as not meeting the eligibility criteria. Consequently, **0 full-text articles** were assessed for eligibility, **0 full-text reports** were excluded at stage 2, and **0 studies** were included in the systematic review.

In PRISMA terms, the review process identified no studies eligible for inclusion on adults with severe obesity (BMI ≥ 35 kg/m²) evaluating **online, group-based behavior change interventions for weight management** against **waitlist or standard care** comparators.

Most frequent recorded exclusion reasons:

- Systematic review/meta-analysis; excluded study design, not a primary intervention study.: 4
- Review article, not a primary intervention study.: 2
- Study design is a systematic review, which is excluded.: 2
- Comparator is active intervention arms (in-person support vs Internet), not waitlist/usual care/standard care; also severe obesity threshold is not established from the abstract.: 1
- Comparator is another active online group intervention (video vs text chat), not waitlist/usual care/standard care; severe obesity threshold is not established from the abstract.: 1
- Study protocol; excluded study design and no results reported.: 1
- Comparator is another active intervention (online social network vs group phone conference), not waitlist/usual care/standard care; severe obesity threshold is not established from the abstract.: 1
- Guideline/recommendation article, not a primary intervention study with eligible comparator and outcomes.: 1
- Comparator is active treatment (group online program with vs without motivational interviewing), not waitlist/usual care/standard care; sample is overweight/obesity without severe obesity threshold established.: 1
- Review/guideline-oriented article, not a primary intervention study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| - | - | No studies retained |

### Study Characteristics

No studies were included in the analysis.

### Main Findings

**Results**

No included studies were identified that met the eligibility criteria for this review; therefore, no studies contributed computable effect sizes for meta-analysis. As a result, a quantitative synthesis of the effects of online, group-based behavior change interventions for weight management in adults with severe obesity (BMI >= 35 kg/m2) was not possible.

Because no eligible studies were included, there were no study-level data to extract on intervention characteristics, comparator conditions, sample size, participant demographics, outcome timing, or risk of bias. Likewise, no data were available on the prespecified outcomes of weight loss, weight-related behavior change, or user perceptions such as acceptability, usability, and overall experience.

A narrative synthesis of individual study findings was also not possible, as no eligible studies were available for review. Accordingly, there were no intervention effects, behavioral findings, or qualitative user-experience results to summarize.

Data could not be pooled because there were no eligible studies and therefore no outcome data, summary statistics, or effect estimates available. This goes beyond the usual barriers to meta-analysis, such as missing variance data, inconsistent reporting, or incompatible outcome measures: in this case, the evidence base meeting the review criteria was absent.

These findings indicate that there is currently no direct evidence from eligible studies to support or refute the effectiveness or acceptability of online, group-based behavior change interventions for weight management in adults with severe obesity compared with waitlist or standard care. The absence of eligible studies should be interpreted as an evidence gap rather than evidence of no effect. This limits the conclusions that can be drawn and highlights the need for primary research using clearly defined interventions, appropriate comparator groups, and standardized reporting of clinical, behavioral, and user-experience outcomes.

### Risk of Bias



## Discussion

**Discussion**

This systematic review set out to identify and synthesize evidence on online, group-based behavior change interventions for weight management in adults with severe obesity (BMI >= 35 kg/m2), compared with waitlist or standard care, across outcomes including weight loss, weight-related behavior change, and user perceptions of acceptability, usability, and overall experience. No studies met the inclusion criteria. As a result, there were no primary data to narratively synthesize on intervention effects, participant experience, or implementation outcomes, and no study-level conclusions or quality ratings could be generated. This empty review is itself informative: it indicates that, within the published and screened literature captured by this review, there is no directly identifiable evidence base addressing this specific intervention format and population under the stated comparator conditions.

Quantitative synthesis was not possible for the most fundamental reason: there were no eligible studies to pool. The absence of included studies means there were no extractable outcome data, no common effect measures, and no basis on which to assess between-study heterogeneity, publication bias, or certainty of evidence. This is not simply a technical barrier to meta-analysis, but a substantive finding about the current state of the literature. It suggests either that such interventions have not been evaluated in controlled studies meeting these criteria, or that evaluations have not been reported in a way that makes them retrievable and usable for evidence synthesis. In either case, the result highlights a clear gap between a clinically relevant question and the available published evidence.

This gap stands in contrast to broader evidence from adjacent fields. Prior meta-analytic work on Acceptance and Commitment Therapy-based weight management interventions in adults with overweight or obesity found some evidence of benefit in specific subgroups, with greater weight reduction among participants with medium versus high internal disinhibition at 12 months. Likewise, an umbrella review of digital interventions for weight-related behaviors in adults suggested that such interventions are generally effective across age groups, although patterns of engagement and subgroup benefit were mixed and the review quality was low. However, these broader findings cannot be assumed to apply to adults with severe obesity participating specifically in online, group-based programs, particularly when compared against waitlist or standard care. The present review therefore cannot confirm whether effects observed in wider obesity populations, or in digital interventions more generally, extend to this more narrowly defined and potentially higher-need group.

A key strength of this review is that it applied a focused clinical question, explicit eligibility criteria, and a systematic, transparent approach to study identification and selection. The review also prespecified outcomes spanning both effectiveness and user experience, which is appropriate for digitally delivered behavioral interventions where acceptability and usability may influence engagement and outcomes. Transparent reporting of an empty review is important because it prevents false confidence based on indirect evidence and clarifies where evidence is currently absent rather than merely inconclusive. In this sense, the review contributes to the evidence landscape by documenting a precise gap in evaluated interventions for adults with severe obesity.

The main limitation is the absence of eligible primary studies and, consequently, the absence of extractable data. This precludes any assessment of intervention effectiveness, acceptability, or risk of bias, and limits inference to the statement that direct evidence is lacking under the specified PICO. It is also possible that relevant interventions exist but were described using inconsistent terminology, embedded within mixed-population samples without separate reporting for severe obesity, or evaluated in uncontrolled or otherwise ineligible designs. Even so, from an evidence-synthesis perspective, lack of extractable and applicable reporting remains a meaningful limitation of the primary literature rather than of the review question itself.

For practice, the findings indicate that there is currently no direct controlled evidence to support or refute the use of online, group-based behavior change interventions for weight management specifically in adults with severe obesity relative to waitlist or standard care. Clinicians and service planners may still draw cautiously on broader evidence for digital and behavioral weight management interventions, but should recognize that this requires extrapolation beyond the population and delivery format of interest. For research, the priority is clear: primary studies are needed that explicitly enroll or report adults with BMI >= 35 kg/m2, clearly describe the online group-based intervention components, use appropriate comparator conditions, and report outcomes on weight, behavior change, and user experience in sufficient detail for synthesis. Better reporting and more targeted evaluations are necessary before robust conclusions can be made about the effectiveness and acceptability of these interventions in this population.

## Conclusion

This systematic review identified no included studies evaluating online, group-based behavior change interventions for weight management in adults with severe obesity (BMI >= 35 kg/m2) against waitlist or standard care. As a result, quantitative synthesis was not possible, and no pooled estimates could be generated for weight loss, weight-related behavior change, or user-reported acceptability, usability, and overall experience. Because no eligible studies were available, there was also no qualitative evidence to meaningfully summarize regarding intervention effects or participant perceptions. The main limitation of this review is therefore the absence of extractable outcome data, which prevents assessment of effectiveness, engagement, or patient experience in this population. Overall, the current evidence base is insufficient to support any firm conclusions about whether these interventions are beneficial, acceptable, or feasible for adults with severe obesity.

## Final Included Studies

None
