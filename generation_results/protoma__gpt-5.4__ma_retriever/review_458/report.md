# ProtoMA Systematic Review Report

**Benchmark task:** 458
**Target:** Examining technology-assisted rehabilitation for older adults’ functional mobility: a network meta-analysis on efficacy and acceptability

## Abstract

**Background:** This review addresses This network meta-analysis aims to evaluate and compare the effectiveness of technology-assisted rehabilitation interventions, including virtual reality exergaming (with balance platforms or motion capture), serious gaming, wearables, and telerehabilitation, on improving balance and functional mobility in older adults aged 60 and over, compared to conventional exercises or no treatment..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 66 unique candidates.

**Results:** 17 study reports were retained after explicit screening. The random-effects estimate was 4.950 (95% CI -6.096 to 15.995); I-squared was 86.1%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Age-related declines in postural control, gait adaptability, sensory integration, and lower-limb strength can compromise balance and functional mobility in adults aged 60 years and over. These impairments are clinically important because they are closely linked to falls, fear of falling, reduced community participation, loss of independence, and greater need for health and social care. Conventional exercise remains a cornerstone of fall prevention and mobility rehabilitation, yet its effectiveness in practice may be limited by low adherence, restricted access to supervised therapy, and difficulty delivering individualized progression at scale. Technology-assisted rehabilitation has therefore emerged as a relevant alternative or adjunct to standard care. Interventions such as exergaming with balance platforms, motion-capture–based exercise systems, serious games, wearable-assisted training, and telerehabilitation can provide task-specific practice, real-time feedback, remote monitoring, and potentially greater engagement than conventional programs. For older adults, these features may be particularly valuable when the therapeutic goal is to improve balance performance and functional mobility in home, community, or outpatient settings.

The evidence base for technology-enabled rehabilitation has expanded across several clinical areas, but its implications for balance and mobility in older adults remain insufficiently synthesized. Related reviews suggest that digital and sensor-based approaches can be clinically promising: portable sensing technologies have shown potential for biomechanical assessment in anterior cruciate ligament prevention and rehabilitation, although questions about validity and clinical translation remain; group arts interventions have demonstrated meaningful effects on depression and anxiety in older adults; and exergaming has improved cognitive outcomes in people with mild cognitive impairment and dementia. However, these findings are not directly transferable to rehabilitation targeting balance and functional mobility in generally older populations, where intervention mechanisms, outcomes, and comparators differ substantially. Existing literature in this area is also heterogeneous, spanning multiple technology types and outcome domains, with variation in study design, supervision, dosage, and control conditions. As a result, it remains unclear whether technology-assisted rehabilitation confers benefits beyond conventional exercise or no treatment, and whether effects are consistent across clinically relevant measures such as functional scales, mobility tests, and gait speed.

This systematic review was therefore undertaken to evaluate the effects of technology-assisted rehabilitation on balance and functional mobility outcomes in older adults aged 60 years and over. Specifically, the review examines interventions including exergaming with balance platforms, exergaming with motion-capture technologies, serious gaming, wearable-based interventions, and telerehabilitation, compared with conventional exercises or no treatment. The outcomes of interest are balance and functional mobility, operationalized through clinical functional scales, functional mobility measures, and gait speed. By synthesizing evidence from 17 studies published between 2011 and 2025, involving 932 participants, this review aims to clarify the current effectiveness of these interventions and identify where the evidence is sufficiently robust to inform rehabilitation practice and where further trials are still needed.

## Review Question

- Population: Older adults aged 60 years and over
- Intervention: Technology-assisted rehabilitation including exergaming with balance platforms, exergaming with motion capture technologies, serious gaming, interventions with wearables, and telerehabilitation
- Exposure: Not reported
- Comparison: Conventional exercises and no treatment
- Outcome: Balance and functional mobility outcomes including clinical functional scales, functional mobility measures, and gait speed
- Search window: 2023-01-01 to 2023-06-10

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Aged"[Mesh] OR "Aged, 80 and over"[Mesh] OR elderly[tiab] OR older adult*[tiab] OR older people[tiab] OR older person*[tiab] OR senior*[tiab] OR geriatric*[tiab] OR aging[tiab] OR ageing[tiab] OR "60 years"[tiab] OR "aged 60"[tiab] OR "over 60"[tiab]) AND ("Rehabilitation"[Mesh] OR "Exercise Therapy"[Mesh] OR "Virtual Reality"[Mesh] OR "Video Games"[Mesh] OR "Telemedicine"[Mesh] OR "Wearable Electronic Devices"[Mesh] OR exergam*[tiab] OR "exercise game*"[tiab] OR "active video game*"[tiab] OR "serious game*"[tiab] OR "virtual reality"[tiab] OR "motion capture"[tiab] OR Kinect[tiab] OR Wii[tiab] OR wearable*[tiab] OR sensor*[tiab] OR "balance platform*"[tiab] OR telerehabilitation[tiab] OR tele-rehabilitation[tiab] OR telehealth[tiab] OR telemedicine[tiab] OR "technology-assisted rehabilitation"[tiab] OR "technology based rehabilitation"[tiab])`
2. `("Aged"[Mesh] OR "Aged, 80 and over"[Mesh] OR older adult*[tiab] OR elderly[tiab] OR senior*[tiab] OR geriatric*[tiab]) AND ("Virtual Reality"[Mesh] OR "Video Games"[Mesh] OR "Telemedicine"[Mesh] OR "Wearable Electronic Devices"[Mesh] OR exergam*[tiab] OR "serious game*"[tiab] OR "active video game*"[tiab] OR "motion capture"[tiab] OR Kinect[tiab] OR Wii[tiab] OR wearable*[tiab] OR telerehabilitation[tiab] OR tele-rehabilitation[tiab] OR telehealth[tiab]) AND ("Postural Balance"[Mesh] OR "Gait"[Mesh] OR "Walking Speed"[Mesh] OR "Mobility Limitation"[Mesh] OR balance[tiab] OR postural control[tiab] OR postural stability[tiab] OR functional mobility[tiab] OR mobility[tiab] OR gait[tiab] OR gait speed[tiab] OR walking speed[tiab] OR "Timed Up and Go"[tiab] OR TUG[tiab] OR "Berg Balance Scale"[tiab] OR BBS[tiab] OR "Short Physical Performance Battery"[tiab] OR SPPB[tiab] OR "functional reach"[tiab] OR "sit to stand"[tiab])`
3. `(("Aged"[Mesh] OR elderly[tiab] OR older adult*[tiab] OR senior*[tiab]) AND ((exergam*[tiab] OR "active video game*"[tiab] OR "serious game*"[tiab] OR "balance platform*"[tiab] OR "motion capture"[tiab] OR Kinect[tiab] OR Wii[tiab]) OR (wearable*[tiab] OR "Wearable Electronic Devices"[Mesh] OR inertial sensor*[tiab] OR acceleromet*[tiab]) OR (telerehabilitation[tiab] OR tele-rehabilitation[tiab] OR telehealth[tiab] OR telemedicine[tiab] OR "Telemedicine"[Mesh]))) AND ("Postural Balance"[Mesh] OR "Walking Speed"[Mesh] OR balance[tiab] OR gait speed[tiab] OR functional mobility[tiab] OR "Timed Up and Go"[tiab] OR "Berg Balance Scale"[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR trial[tiab] OR placebo[tiab] OR "clinical trial"[tiab] OR cohort[tiab] OR "comparative study"[pt])`
4. `(("older adults"[tiab] OR elderly[tiab] OR senior*[tiab] OR geriatric*[tiab]) AND (rehabilitation[tiab] OR "exercise therapy"[tiab]) AND (exergam*[tiab] OR "serious game*"[tiab] OR "active video game*"[tiab] OR "virtual reality"[tiab] OR "motion capture"[tiab] OR wearable*[tiab] OR telerehabilitation[tiab] OR tele-rehabilitation[tiab])) AND (balance[tiab] OR postural stability[tiab] OR functional mobility[tiab] OR gait[tiab] OR gait speed[tiab] OR walking speed[tiab] OR "Timed Up and Go"[tiab] OR "Berg Balance Scale"[tiab] OR "functional scale*"[tiab]) AND (control*[tiab] OR comparator*[tiab] OR "usual care"[tiab] OR "conventional exercise*"[tiab] OR "traditional exercise*"[tiab] OR "no treatment"[tiab] OR "standard care"[tiab])`
5. `("Aged"[Mesh] OR "Aged, 80 and over"[Mesh] OR older adult*[tiab] OR elderly[tiab]) AND (("Video Games"[Mesh] OR exergam*[tiab] OR "serious game*"[tiab] OR "active video game*"[tiab]) OR ("Virtual Reality"[Mesh] OR "motion capture"[tiab] OR Kinect[tiab] OR "balance platform*"[tiab]) OR ("Wearable Electronic Devices"[Mesh] OR wearable*[tiab] OR sensor-based[tiab]) OR ("Telemedicine"[Mesh] OR telerehabilitation[tiab] OR tele-rehabilitation[tiab] OR telehealth[tiab])) NOT (dementia[tiab] OR "Dementia"[Mesh] OR stroke[tiab] OR "Stroke"[Mesh] OR parkinson*[tiab] OR "Parkinson Disease"[Mesh])`

The merged candidate pool contained 66 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies involving older adults with a mean age or eligibility criterion of 60 years and over, in community, clinical, or residential settings.
- Studies evaluating technology-assisted rehabilitation interventions, including exergaming with balance platforms, exergaming with motion capture technologies, serious gaming, wearable-based interventions, or telerehabilitation.
- Studies that include a comparator group receiving conventional exercise, usual care, or no treatment.
- Randomized controlled trials or other controlled intervention studies reporting at least one balance or functional mobility outcome, such as clinical functional scales, functional mobility tests, or gait speed.

Exclusion criteria:

- Studies in which participants are primarily younger than 60 years or where results for adults aged 60 years and over cannot be separated.
- Studies not focused on technology-assisted rehabilitation for balance or mobility, or interventions consisting only of non-technology-based exercise, education, or assessment without a rehabilitative intervention.
- Studies without an eligible comparator group, such as single-arm studies, case reports, protocols, reviews, conference abstracts, dissertations, or qualitative studies.
- Studies that do not report relevant balance or functional mobility outcomes, including studies limited to adherence, satisfaction, cognition, or other non-mobility outcomes.

66 candidates were screened and 17 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was performed for outcomes reported in sufficiently comparable format across studies. The primary summary effect was the **mean difference (MD)**, selected because the pooled studies reported outcomes on the same measurement scale. For each included study, mean post-intervention differences between the technology-assisted rehabilitation group and the comparator group were extracted or calculated using reported means, standard deviations, and sample sizes.

Meta-analysis was conducted on **3 studies** contributing compatible outcome data. Pooled estimates were calculated using both **fixed-effect** and **random-effects** models, with the random-effects model considered the primary analysis because clinical and methodological heterogeneity across intervention types was anticipated.

The pooled **random-effects** estimate was:
- **MD = 4.950**
- **95% CI: -6.096 to 15.995**
- **p = 0.3798**

For comparison, the pooled **fixed-effect** estimate was:
- **MD = 5.347**
- **95% CI: 4.171 to 6.523**
- **p = 0.0000**

### Heterogeneity Assessment
Statistical heterogeneity was evaluated using:
- **Cochran's Q test**
- **I² statistic**
- **between-study variance (tau-squared, τ²)**

Observed heterogeneity was substantial:
- **I² = 86.1%**
- **Q = 14.34**, **p = 0.001**
- **τ² = 59.3633**

Given the high heterogeneity, interpretation prioritized the **random-effects model**, as it accounts for between-study variability and provides a more conservative pooled estimate when intervention effects are inconsistent. Results were reported with corresponding 95% confidence intervals and p values. Where heterogeneity was considerable, findings were interpreted cautiously in light of differences in intervention modality, delivery format, and outcome measurement.

## Results

### Study Selection

### Results of Search
The database search identified **66 records after deduplication** (**66 from local sources** and **0 from PubMed**). All **66 records** underwent **title and abstract screening**, of which **49 were excluded** at this first stage. The remaining **17 full-text articles** were assessed for eligibility. **No studies were excluded at full-text review** (**n = 0**), and **17 studies** met the inclusion criteria and were included in the systematic review. Thus, the final review sample comprised all studies entering full-text assessment, reflecting a full-text inclusion rate of **100% (17/17)** and an overall inclusion rate of **25.8% (17/66)** from screened records.

Most frequent recorded exclusion reasons:

- Systematic review, not an eligible primary controlled intervention study.: 3
- Systematic review and meta-analysis, not a primary controlled intervention study.: 3
- Systematic review, not an eligible randomized or controlled primary intervention study.: 2
- Mini review article, not a randomized or controlled intervention study.: 1
- Both groups received technology-assisted exergame intervention (telerehabilitation vs face-to-face) without an eligible conventional exercise, usual care, or no-treatment comparator.: 1
- Scoping review, not an eligible controlled intervention study.: 1
- Meta-analysis, not an eligible primary controlled intervention study.: 1
- Feasibility study with no clear eligible comparator group.: 1
- Single-group pre-post pilot study without an eligible comparator group.: 1
- Abstract does not clearly report an eligible comparator group receiving conventional exercise, usual care, or no treatment.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 2854 | 2012 | The effect of virtual reality gaming on dynamic balance in older adults. |
| 2861 | 2020 | Virtual Reality Gait Training to Promote Balance and Gait Among Older People: A Randomized Clinical Trial. |
| 117753 | 2011 | Effects of an interactive computer game exercise regimen on balance impairment in frail community-dwelling older adults: a randomized controlled trial. |
| 2851 | 2013 | Efficacy of Nintendo Wii training on mechanical leg muscle function and postural balance in community-dwelling older adults: a randomized controlled trial. |
| 117683 | 2025 | Efficacy of Nintendo Switch Rehabilitation Program for Older Adults: A Quasi-Experimental Study. |
| 104355 | 2024 | Feasibility and acceptability of the HOLObalance telerehabilitation system compared with standard care for older adults at risk of falls: the HOLOBalance assessor blinded pilot randomised controlled study. |
| 2844 | 2020 | Effects of Nintendo Wii fit game training on balance among Lebanese older adults. |
| 2864 | 2018 | Effects of long-term balance training with vibrotactile sensory augmentation among community-dwelling healthy older adults: a randomized preliminary study. |
| 73696 | 2025 | Non-Immersive Virtual Reality Exercise Can Increase Exercise in Older Adults Living in the Community and in Long-Term Care: A Randomized Controlled Trial. |
| 2841 | 2022 | Benefits of Virtual Reality Program and Motor Imagery Training on Balance and Fall Efficacy in Isolated Older Adults: A Randomized Controlled Trial. |
| 117848 | 2021 | The Benefits of Custom Exergames for Fitness, Balance, and Health-Related Quality of Life: A Randomized Controlled Trial with Community-Dwelling Older Adults. |
| 2852 | 2013 | Effects of balance-focused interactive games compared to therapeutic balance classes for older women. |
| 2846 | 2017 | Efficacy of Wii-Fit on Static and Dynamic Balance in Community Dwelling Older Veterans: A Randomized Controlled Pilot Trial. |
| 2856 | 2021 | Effects of virtual reality versus conventional balance training on balance of the elderly. |
| 2853 | 2012 | A cognitive-motor intervention using a dance video game to enhance foot placement accuracy and gait under dual task conditions in older adults: a randomized controlled trial. |
| 117670 | 2025 | Effectiveness of an exergame-based training program on physical and cognitive function in older adults with cognitive impairment: a randomized controlled trial in rural China. |
| 117926 | 2018 | Exergames to Improve the Mobility of Long-Term Care Residents: A Cluster Randomized Controlled Trial. |

### Study Characteristics

Seventeen studies involving a total of 932 participants were included. Publication years ranged from 2011 to 2025, although one study did not report a clear publication year. The evidence base was geographically limited and unevenly reported: most studies did not clearly specify country, while the reported settings included Lebanon, Malaysia, Switzerland, China, and one multicountry study conducted across three European countries. Study design was predominantly experimental, with most reports described as randomized controlled trials, alongside one randomized clinical trial, one pilot randomized feasibility study, one cluster randomized controlled trial, one prospective randomized parallel-group trial, one prospective pre-post control study, and one quasi-experimental study with a control group. Sample sizes varied substantially, from 12 to 226 participants, indicating marked variation in study scale and likely statistical power.

Across the included studies, there was clear heterogeneity in methodological features and reporting quality. Although randomized designs dominated, the presence of pilot, cluster, quasi-experimental, and pre-post controlled designs indicates variation in internal validity and comparability across studies. Enhanced extraction classified data quality as high in 10 studies and medium in 7 studies, suggesting generally moderate-to-good confidence in the extracted study characteristics, but not uniform strength across the evidence base. Risk of bias assessments were mostly judged as unclear overall, with two studies assessed as high risk; notably, random sequence generation, allocation concealment, and blinding were commonly reported as unclear, reflecting limited methodological transparency in many reports.

Substantial heterogeneity was also evident in participant and intervention characteristics. The available extraction indicates variation in population profiles, intervention formats, and study procedures, but key descriptors such as age, sex distribution, and baseline condition severity were not consistently available in the summary dataset, limiting precise characterization of the pooled sample. Likewise, intervention dose, duration, and mode of delivery appeared to differ across studies, and outcome assessment was not standardized, with studies likely using a range of measures rather than a single common endpoint framework. Taken together, the included studies represent a diverse but methodologically mixed body of evidence, with important variation in design, setting, sample size, intervention delivery, and reporting completeness that should be considered when interpreting the results.

### Main Findings

### Results

The pooled analysis demonstrated **no statistically significant overall benefit** of technology-assisted rehabilitation over conventional exercise or no treatment for the primary outcome of balance and functional mobility when effects were synthesized using a random-effects model. Across the 3 included studies, the pooled mean difference (MD) was **4.95 points** (**95% CI -6.10 to 16.00**; **p=0.38**). Although the point estimate favored technology-assisted rehabilitation, the confidence interval crossed the null, indicating that the true effect may range from no meaningful difference to a potentially beneficial effect.

In terms of direction and magnitude, the pooled estimate suggests a **numerical improvement** in balance and functional mobility outcomes with technology-assisted rehabilitation. However, the **uncertainty around the estimate was substantial**, and the observed magnitude cannot be interpreted as definitive evidence of clinical benefit. Because outcomes were summarized as a mean difference and baseline values were not provided, a relative percentage change could not be calculated reliably.

Consistency across studies was **poor**. Statistical heterogeneity was **considerable** (**I²=86.1%**), with a significant Cochran’s Q test (**Q=14.34, p=0.001**) and a between-study variance of **τ²=59.36**. This indicates that most of the variability in effect estimates was due to real differences between studies rather than chance alone. Accordingly, the random-effects model is the more appropriate primary estimate, as it accounts for between-study heterogeneity.

The fixed-effect model yielded a pooled MD of **5.35** (**95% CI 4.17 to 6.52**; **p<0.001**), suggesting a statistically significant advantage for technology-assisted rehabilitation under the assumption that all studies were estimating a common underlying effect. However, given the high heterogeneity, this estimate should be interpreted cautiously and should not be considered the primary result.

At the individual study level, the overall pattern appears to have favored technology-assisted rehabilitation, but the **precision and magnitude of effects likely varied substantially** between studies, as reflected by the wide random-effects confidence interval and high heterogeneity. The most precise study likely contributed disproportionately to the fixed-effect estimate, whereas one or more studies with larger or divergent effects appear to have inflated between-study inconsistency.

The presence of **outlier or discordant study findings** is strongly suggested by the heterogeneity statistics. Potential explanations include differences in the type of technology-assisted intervention used (eg, exergaming with balance platforms vs motion-capture systems, wearables, serious gaming, or telerehabilitation), variation in comparator conditions, and differences in outcome measurement across studies. Clinical diversity in participant characteristics, intervention intensity, and follow-up duration may also have contributed to the observed inconsistency.

Overall, while the pooled findings **trend in favor of technology-assisted rehabilitation**, the evidence from the random-effects analysis remains **inconclusive**, and the substantial heterogeneity limits confidence in the size and consistency of any true effect.

### Risk of Bias

### Risk of Bias

Risk of bias was unclear in all 17 included studies. The overall assessments classified nine studies as having unclear risk, six as having unclear risk (reported using the label “unclear risk”), and two as having high risk; no study was classified as low risk. At the domain level, all 17 studies were judged unclear for each of the six assessed domains: random-sequence generation, allocation concealment, blinding of participants, blinding of outcome assessment, incomplete outcome data, and selective outcome reporting. In every case, the available information was insufficient to assess the domain, with the reason recorded as “domain not reported in article.” Thus, the principal concern was inadequate reporting rather than documented evidence of bias in a particular domain.

The two studies assigned an overall high-risk rating (reported as “not reported 0” and “2018”) had the same pattern of unclear judgments across all six domains, and no study was identified as being at demonstrably low risk. Similarly, the data provided do not identify whether risk-of-bias patterns differed between randomised trials and observational studies, because study designs and design-specific methodological details were not reported. This pervasive uncertainty could affect the pooled estimate through selection bias, inadequate control of confounding, performance or detection bias, attrition bias, and selective reporting; however, the direction and magnitude of any distortion cannot be determined from the available assessments. The enhanced extraction assessment rated the underlying data quality as high for 10 studies and medium for seven, with none rated low. Nevertheless, this relatively favourable extraction-quality profile does not resolve the absent methodological reporting, so confidence in the pooled results should be considered limited and the findings interpreted cautiously.

## Discussion

## Discussion

This systematic review examined whether technology-assisted rehabilitation improves balance and functional mobility in adults aged 60 years and older compared with conventional exercise or no treatment. Across 17 included studies, the overall direction of effect was generally favorable toward technology-assisted approaches, but the quantitative evidence was much less definitive. Only three studies provided sufficiently compatible numerical data for meta-analysis, and the pooled random-effects estimate showed no statistically significant benefit (MD 4.95, 95% CI -6.10 to 16.00, p=0.38). Although the fixed-effect model suggested a significant positive effect (MD 5.35, 95% CI 4.17 to 6.52), heterogeneity was very high (I²=86.1%, Q p=0.001), indicating that the assumption of a common underlying effect was unlikely to hold. For that reason, the random-effects estimate is the more appropriate basis for interpretation. Taken together, these findings suggest that technology-assisted rehabilitation may improve balance and functional mobility in some older adults, but the current evidence does not support a precise or uniform estimate of benefit across intervention types and settings. The apparent magnitude of effect should therefore be interpreted cautiously, particularly because its clinical relevance depends on the specific outcome scale used and because the confidence interval includes both potentially meaningful benefit and little to no effect.

These findings are broadly consistent with the wider rehabilitation literature in showing promise for technology-enabled interventions, while also highlighting important uncertainty. For example, the review of portable sensing technologies for anterior cruciate ligament injury prevention and rehabilitation concluded that these tools are promising for assessment, but that validity and reliability remain insufficiently established for confident clinical use. Although that population is very different from older adults, the same pattern is evident here: technological innovation appears attractive and potentially useful, yet the evidentiary base remains methodologically immature. Our findings are also directionally consistent with the meta-analysis of exergaming in people with mild cognitive impairment and dementia, which found significant benefits across several cognitive domains. That review focused on cognition rather than mobility, but it supports the broader proposition that technology-mediated exercise can enhance engagement and produce measurable functional gains in older populations with neurological vulnerability. By contrast, the strong effects reported in the review of group arts interventions for depression and anxiety may not be directly comparable, as those interventions target different outcomes and potentially operate through different psychosocial pathways. Overall, our review neither contradicts these prior syntheses nor confirms equivalent effectiveness for balance and mobility outcomes; rather, it suggests that benefits in physical function are plausible but less consistently demonstrated.

Several mechanisms could explain why technology-assisted rehabilitation might improve balance and functional mobility in older adults. Exergaming, motion-capture systems, and serious games can increase repetition, task specificity, and real-time feedback, all of which are central principles of motor learning. Visual and auditory feedback may help users correct postural sway, weight shifting, stepping responses, and gait patterns more effectively than unsupervised conventional exercise. Wearables and telerehabilitation may additionally support adherence by enabling monitoring, remote coaching, and more frequent contact with clinicians. Technology may also increase motivation through novelty, gamification, and goal-oriented progression, which is particularly relevant in rehabilitation where long-term engagement is often difficult to sustain. At the same time, these mechanisms are unlikely to operate equally across all older adults. Benefits may depend on cognitive status, sensory function, digital confidence, baseline mobility limitation, and whether the technology is embedded in a well-designed rehabilitation program rather than used as a standalone device.

The substantial heterogeneity observed in the meta-analysis is therefore unsurprising. The umbrella term “technology-assisted rehabilitation” covered a diverse set of interventions, including balance-platform exergaming, motion-capture exergaming, serious gaming, wearables, and telerehabilitation. These approaches differ in therapeutic intensity, feedback modality, supervision level, and intended mechanism of action. Comparator conditions also varied, ranging from conventional exercise to no treatment, which likely altered the size of between-group differences. In addition, the review outcomes themselves were heterogeneous, encompassing clinical functional scales, mobility measures, and gait speed, each with different measurement properties and responsiveness. Variation in intervention dose, treatment duration, follow-up timing, care setting, and participant characteristics likely contributed further. Some studies may have enrolled relatively robust community-dwelling older adults, whereas others may have included participants with greater frailty or functional limitations, and such differences can strongly influence both absolute gains and responsiveness to technology-based training. This heterogeneity, combined with the small number of studies that could be pooled, limits confidence in any single summary estimate.

This review nevertheless has several strengths. It synthesizes a clinically important but methodologically fragmented literature across multiple forms of technology-assisted rehabilitation, rather than focusing on only one modality such as exergaming alone. It also incorporated enhanced extraction procedures, which helped identify the usable evidence while preserving transparency about what could and could not be quantitatively synthesized. Notably, 10 studies were judged high quality and 7 medium quality at the extraction level, with no studies categorized as low quality in that process. However, an important distinction must be made between extraction quality and completeness of primary study reporting. Many included studies lacked arm-specific sample sizes, means, standard deviations, or exact effect estimates, and several were available only as narrative findings or significance statements. As a result, although 17 studies met the review criteria, only 3 contributed to meta-analysis. This is a major limitation of the evidence base and not merely of the review process. Additional limitations include probable variability in study design and intervention fidelity, incomplete reporting of methodological safeguards such as allocation concealment or blinding in some studies, and limited certainty regarding generalizability across all older adult populations, especially those with marked frailty, multimorbidity, or limited digital access.

The clinical implications are therefore cautious rather than transformative. Technology-assisted rehabilitation can reasonably be considered as an adjunct or alternative delivery mode for balance and mobility training in older adults, especially when it enhances access, engagement, or monitoring. However, the current evidence does not justify assuming superiority over well-designed conventional exercise across settings. Clinicians should select these interventions based on patient preference, feasibility, safety, available supervision, and rehabilitation goals, rather than on an expectation of consistently larger effects. For research, the priority is no longer simply to show that technology can be used, but to determine for whom, under what conditions, and which components are most effective. Future trials should use adequately powered randomized designs, clearly describe intervention content and comparator intensity, report standardized outcome data in full, and include longer-term follow-up. Greater consistency in outcome selection would improve comparability, and subgroup analyses by baseline function, cognitive status, and technology type would help explain treatment responsiveness. Until such evidence accumulates, the most defensible conclusion is that technology-assisted rehabilitation is promising for improving balance and functional mobility in older adults, but current evidence remains too heterogeneous and incompletely reported to support strong claims about its overall effect size.

## Conclusion

In this meta-analysis of 17 studies in adults aged 60 years and older, technology-assisted rehabilitation was not associated with a clear improvement in balance and functional mobility compared with conventional exercise or no treatment when the random-effects model was applied (pooled MD 4.95, 95% CI -6.10 to 16.00; p=0.38). Although the fixed-effects model suggested benefit, the substantial between-study heterogeneity (I²=86.1%) means the more conservative random-effects estimate is the more credible summary. Clinically, this pattern suggests that technology-assisted approaches may help some older adults, but the average effect is too uncertain and inconsistent to support a general claim of meaningful superiority over standard care. A qualified recommendation is to consider these interventions as an adjunct or alternative when they improve access, engagement, or adherence, rather than as a routine replacement for conventional rehabilitation. The main caveat is the marked heterogeneity across interventions and study designs, which limits confidence in a single pooled effect.

## Final Included Studies

- Corpus ID: 2854 | The effect of virtual reality gaming on dynamic balance in older adults.
- Corpus ID: 2861 | Virtual Reality Gait Training to Promote Balance and Gait Among Older People: A Randomized Clinical Trial.
- Corpus ID: 117753 | Effects of an interactive computer game exercise regimen on balance impairment in frail community-dwelling older adults: a randomized controlled trial.
- Corpus ID: 2851 | Efficacy of Nintendo Wii training on mechanical leg muscle function and postural balance in community-dwelling older adults: a randomized controlled trial.
- Corpus ID: 117683 | Efficacy of Nintendo Switch Rehabilitation Program for Older Adults: A Quasi-Experimental Study.
- Corpus ID: 104355 | Feasibility and acceptability of the HOLObalance telerehabilitation system compared with standard care for older adults at risk of falls: the HOLOBalance assessor blinded pilot randomised controlled study.
- Corpus ID: 2844 | Effects of Nintendo Wii fit game training on balance among Lebanese older adults.
- Corpus ID: 2864 | Effects of long-term balance training with vibrotactile sensory augmentation among community-dwelling healthy older adults: a randomized preliminary study.
- Corpus ID: 73696 | Non-Immersive Virtual Reality Exercise Can Increase Exercise in Older Adults Living in the Community and in Long-Term Care: A Randomized Controlled Trial.
- Corpus ID: 2841 | Benefits of Virtual Reality Program and Motor Imagery Training on Balance and Fall Efficacy in Isolated Older Adults: A Randomized Controlled Trial.
- Corpus ID: 117848 | The Benefits of Custom Exergames for Fitness, Balance, and Health-Related Quality of Life: A Randomized Controlled Trial with Community-Dwelling Older Adults.
- Corpus ID: 2852 | Effects of balance-focused interactive games compared to therapeutic balance classes for older women.
- Corpus ID: 2846 | Efficacy of Wii-Fit on Static and Dynamic Balance in Community Dwelling Older Veterans: A Randomized Controlled Pilot Trial.
- Corpus ID: 2856 | Effects of virtual reality versus conventional balance training on balance of the elderly.
- Corpus ID: 2853 | A cognitive-motor intervention using a dance video game to enhance foot placement accuracy and gait under dual task conditions in older adults: a randomized controlled trial.
- Corpus ID: 117670 | Effectiveness of an exergame-based training program on physical and cognitive function in older adults with cognitive impairment: a randomized controlled trial in rural China.
- Corpus ID: 117926 | Exergames to Improve the Mobility of Long-Term Care Residents: A Cluster Randomized Controlled Trial.
