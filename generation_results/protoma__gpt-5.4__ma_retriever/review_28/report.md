# ProtoMA Systematic Review Report

**Benchmark task:** 28
**Target:** A systematic review of influences on engagement with remote health interventions targeting weight management for individuals living with excess weight

## Abstract

**Background:** This review addresses This systematic review examines the barriers and facilitators influencing engagement of adults living with excess weight (BMI ≥27.5 kg/m²) in synchronous, remote health interventions for weight management, with findings mapped to the COM-B model of behaviour change and Theoretical Domains Framework..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 76 unique candidates.

**Results:** 5 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

I’m drafting the Background around your PICO and the evidence pattern you gave, with the aim of making the gap and the review objective explicit rather than generic. I’ll keep it to 2-3 compact academic paragraphs.Adults living with excess weight or obesity often require sustained behavioural support to achieve clinically meaningful weight management, yet access to in-person care is constrained by time, travel, work, caregiving, and service availability. Synchronous remote health interventions delivered in real time may reduce these access barriers by allowing direct clinician contact without requiring attendance at a physical site, while still preserving interaction, feedback, and accountability. Their practical value depends not only on efficacy, but on whether participants are able and willing to engage consistently enough for the intervention to be delivered as intended.

The current evidence base on engagement with synchronous remote weight management interventions remains small and heterogeneous. Across five studies published between 2014 and 2025, including one pragmatic single-arm nonrandomized study, one comparative study, one pilot randomized controlled trial, one qualitative focus group evaluation of trial completers, and one randomized controlled trial with mixed-methods acceptability evaluation, 1,859 participants were represented in total. Existing work suggests that engagement is shaped by interacting capability, opportunity, and motivation factors, but the available studies are not yet sufficient to establish which barriers or facilitators are most influential, how these factors cluster across trial and real-world settings, or which are modifiable at the intervention level. This leaves an important implementation gap: interventions may be feasible in principle yet still fail to reach the people who need them if engagement barriers are not identified and addressed.

Accordingly, this systematic review will synthesize evidence on factors associated with engagement in synchronous, real-time remote health interventions for weight management among adults aged 18 years or older with BMI >=27.5 kg/m². The review will compare barriers versus facilitators to engagement and map these factors to the capability, opportunity, and motivation domains. By doing so, it aims to clarify what supports or hinders engagement with remote weight management care and to inform the design and delivery of interventions that are more usable, acceptable, and sustainable in practice.

## Review Question

- Population: Adults aged 18 years or older with BMI ≥27.5 kg/m² (living with excess weight or obesity)
- Intervention: Synchronous (real-time), remote health interventions for weight management
- Exposure: Not reported
- Comparison: Factors facilitating engagement versus factors hindering engagement (barriers versus facilitators)
- Outcome: Engagement with remote weight management interventions (barriers and facilitators to engagement mapped to capability, opportunity, and motivation domains)
- Search window: Not reported to 2023-10-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Overweight"[Mesh] OR "Obesity"[Mesh] OR overweight[tiab] OR obes*[tiab] OR "excess weight"[tiab] OR "body mass index"[tiab] OR BMI[tiab]) AND (adult*[tiab] OR "Adult"[Mesh]) AND ("Telemedicine"[Mesh] OR "Remote Consultation"[Mesh] OR telemedicine[tiab] OR telehealth[tiab] OR eHealth[tiab] OR mHealth[tiab] OR "digital health"[tiab] OR remot*[tiab] OR virtual[tiab] OR online[tiab] OR videoconferenc*[tiab] OR telephone[tiab] OR phone[tiab] OR "synchronous"[tiab] OR "real-time"[tiab] OR live[tiab]) AND ("Weight Loss"[Mesh] OR "Body Weight"[Mesh] OR "weight management"[tiab] OR "weight loss"[tiab] OR "weight reduction"[tiab] OR "lifestyle intervention"[tiab])`
2. `("Obesity"[Mesh] OR "Overweight"[Mesh] OR obes*[tiab] OR overweight[tiab] OR "excess weight"[tiab]) AND (adult*[tiab] OR "Adult"[Mesh]) AND (("Telemedicine"[Mesh] OR "Remote Consultation"[Mesh]) OR ((telehealth[tiab] OR telemedicine[tiab] OR remot*[tiab] OR virtual[tiab] OR online[tiab] OR video[tiab] OR videoconferenc*[tiab] OR telephone[tiab] OR phone[tiab]) AND (synchronous[tiab] OR "real-time"[tiab] OR live[tiab] OR interactive[tiab]))) AND (engag*[tiab] OR participat*[tiab] OR adheren*[tiab] OR uptake[tiab] OR acceptab*[tiab] OR retention[tiab] OR attendance[tiab]) AND (barrier*[tiab] OR facilitator*[tiab] OR challenge*[tiab] OR enabler*[tiab] OR obstacle*[tiab] OR motivator*[tiab])`
3. `(("Overweight"[Mesh] OR "Obesity"[Mesh] OR overweight[tiab] OR obes*[tiab]) AND (adult*[tiab] OR "Adult"[Mesh])) AND (("Telemedicine"[Mesh] OR telehealth[tiab] OR telemedicine[tiab] OR eHealth[tiab] OR mHealth[tiab] OR virtual[tiab] OR online[tiab] OR videoconferenc*[tiab] OR telephone[tiab]) AND ("weight management"[tiab] OR "weight loss"[tiab] OR "obesity treatment"[tiab] OR "lifestyle intervention"[tiab])) AND ((engag*[tiab] OR adheren*[tiab] OR participat*[tiab] OR uptake[tiab] OR retention[tiab]) AND (barrier*[tiab] OR facilitator*[tiab] OR enabler*[tiab] OR obstacle*[tiab])) AND (capability[tiab] OR opportunity[tiab] OR motivation[tiab] OR COM-B[tiab] OR behaviour[tiab] OR behavior[tiab])`
4. `("Obesity"[Mesh] OR "Overweight"[Mesh] OR obes*[tiab] OR overweight[tiab] OR "excess weight"[tiab]) AND (adult*[tiab] OR "Adult"[Mesh]) AND ("Telemedicine"[Mesh] OR "Remote Consultation"[Mesh] OR telehealth[tiab] OR telemedicine[tiab] OR "remote intervention"[tiab] OR "distance intervention"[tiab] OR "virtual care"[tiab] OR online[tiab] OR videoconferenc*[tiab] OR telephone[tiab]) AND ("Weight Loss"[Mesh] OR "weight management"[tiab] OR "weight loss"[tiab] OR "body weight"[tiab]) AND (engag*[tiab] OR participat*[tiab] OR adheren*[tiab] OR retention[tiab] OR attendance[tiab]) AND (barrier*[tiab] OR facilitator*[tiab] OR enabler*[tiab] OR obstacle*[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR observational study[pt] OR cohort[tiab] OR longitudinal[tiab] OR qualitative[tiab] OR interview*[tiab] OR "focus group*"[tiab] OR mixed-method*[tiab])`
5. `((adult*[tiab] OR "Adult"[Mesh]) AND (BMI[tiab] OR "body mass index"[tiab] OR overweight[tiab] OR obes*[tiab] OR "Overweight"[Mesh] OR "Obesity"[Mesh])) AND ((synchronous[tiab] OR "real-time"[tiab] OR live[tiab] OR interactive[tiab]) AND (remote[tiab] OR telehealth[tiab] OR telemedicine[tiab] OR virtual[tiab] OR online[tiab] OR videoconferenc*[tiab] OR telephone[tiab] OR phone[tiab])) AND ("weight management"[tiab] OR "weight loss"[tiab] OR "obesity management"[tiab]) AND ((barrier*[tiab] OR facilitator*[tiab] OR enabler*[tiab] OR obstacle*[tiab] OR challenge*[tiab]) AND (engag*[tiab] OR adheren*[tiab] OR participat*[tiab] OR uptake[tiab] OR retention[tiab] OR attendance[tiab] OR acceptab*[tiab])) NOT (child*[tiab] OR adolescen*[tiab] OR pediatric*[tiab])`

The merged candidate pool contained 76 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies involving adults aged 18 years or older with BMI ≥27.5 kg/m², or populations explicitly described as living with excess weight, overweight, or obesity and broadly consistent with this threshold.
- Studies evaluating synchronous, real-time remote health interventions for weight management, such as telephone, video, or live online coaching/counselling delivered at a distance.
- Primary qualitative, quantitative, or mixed-methods studies that report barriers, facilitators, or other determinants of engagement with the remote intervention.
- Studies reporting engagement-related outcomes or data that can be mapped to capability, opportunity, and/or motivation domains (e.g., uptake, attendance, adherence, participation, retention, acceptability-related engagement factors).

Exclusion criteria:

- Studies including children/adolescents, pregnant populations, or participants not primarily living with excess weight/obesity, or where adult/BMI-eligible data cannot be separated.
- Studies of asynchronous-only or non-remote interventions, or interventions not focused on weight management (e.g., app-only self-guided programs without real-time contact, in-person-only programs, surgical interventions).
- Studies that do not examine engagement barriers/facilitators or do not provide engagement-related outcomes/data relevant to remote weight management intervention use.
- Non-primary research and insufficient-report publications, such as reviews, protocols, editorials, letters, conference abstracts without full data, or studies with unclear eligibility that cannot be determined from the report.

76 candidates were screened and 5 were retained.

### Statistical Analysis

### Statistical analysis
A quantitative meta-analysis was **not performed**. This decision was made because the **5 included studies** were limited in number and were methodologically heterogeneous with respect to study design, intervention format, definitions of engagement, and the way barriers and facilitators were identified and reported. Accordingly, the review used a **structured narrative synthesis**.

Where quantitative data on engagement-related factors were available, these were extracted descriptively, including frequencies, proportions, or author-reported associations. If sufficiently comparable outcome data had been available, effect estimates would have been extracted or calculated using standard methods appropriate to the data type: **odds ratios or risk ratios** for dichotomous outcomes and **mean differences or standardized mean differences** for continuous outcomes, each with corresponding **95% confidence intervals**. For adjusted analyses, adjusted estimates would have been prioritised over crude estimates where comparable.

Because statistical pooling was not appropriate, **no pooled effect size**, **no fixed-effect or random-effects model**, and **no formal heterogeneity statistics** (such as **I²**, **τ²**, or Cochran's Q) were calculated. Likewise, no subgroup analysis, sensitivity analysis, meta-regression, or publication bias assessment was undertaken.

Instead, findings were synthesised by:
- grouping reported factors as **barriers** or **facilitators** to engagement;
- mapping each factor to the **COM-B domains** of **Capability**, **Opportunity**, or **Motivation**;
- comparing patterns across studies in relation to participant characteristics and intervention features; and
- summarising the consistency and prominence of reported determinants of engagement.

This approach was considered the most methodologically appropriate for the available evidence base and aligned with the review objective of identifying and classifying determinants of engagement rather than estimating a single pooled intervention effect.

## Results

### Study Selection

### Results of the Search
The database and local search yielded **76 records** in total (**76 local sources; 0 PubMed**), with **76 records remaining after deduplication**. All **76 records** underwent title and abstract screening. At this first screening stage, **71 records were excluded** as not meeting the eligibility criteria. The full texts of the remaining **5 articles** were assessed for eligibility. No studies were excluded at full-text review (**n = 0**). Consequently, **5 studies** met the inclusion criteria and were included in the review. This corresponds to an inclusion rate of **6.6%** of records screened (5/76) and **100%** of studies assessed at full text (5/5).

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis; non-primary research and therefore excluded.: 4
- Scoping review; non-primary research and therefore excluded.: 1
- Guideline/recommendations article rather than a primary empirical study; excluded as non-primary research.: 1
- Intervention is described as self-directed and remotely delivered, indicating asynchronous/self-guided rather than synchronous real-time remote contact; also no engagement barriers/facilitators focus is evident.: 1
- Primary telehealth weight-management study in adults with obesity, but the abstract reports effectiveness outcomes (%TBWL, HbA1c, resource use) and does not examine engagement barriers/facilitators or engagement-related determinants.: 1
- Intervention relies on telemonitoring plus weekly counseling letters by post/email, which is asynchronous rather than synchronous real-time remote intervention.: 1
- Review article; non-primary research and therefore excluded.: 1
- Internet-based weight maintenance trial, but engagement barriers/facilitators are not reported in the abstract, and the intervention is not clearly synchronous real-time remote care.: 1
- Primary study of videoconferenced weight-management classes in adults, but the abstract focuses on effectiveness and does not report engagement barriers/facilitators or engagement-related determinants.: 1
- Primary remotely delivered obesity treatment study, but the abstract focuses on optimizing treatment components/weight loss and does not report engagement barriers/facilitators or engagement-related outcomes relevant to intervention use.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 6921 | 2019 | Feasibility and acceptability of a rural, pragmatic, telemedicine-delivered healthy lifestyle programme. |
| 69878 | 2014 | Using synchronous distance-education technology to deliver a weight management intervention. |
| 6942 | 2019 | Enhancing group-based internet obesity treatment: A pilot RCT comparing video and text-based chat. |
| 6938 | 2021 | Participant perspectives of a telehealth trial investigating the use of telephone and text message support in obesity management: a qualitative evaluation. |
| 115646 | 2025 | Exploring the Acceptability of Post-bariatric Nutritional-Behavioral and Supervised Exercise Intervention (BARI-LIFESTYLE): A Mixed Methods Evaluation. |

### Study Characteristics

**Study Characteristics**

Five studies met the inclusion criteria, comprising 1,859 participants in total, although one 2021 study was a qualitative follow-up using focus groups and did not contribute a participant count to the pooled total. The studies were published between 2014 and 2025, indicating that the evidence base spans more than a decade but remains limited in size. Geographic distribution could not be meaningfully described because no study reported country information in the extracted dataset. There was substantial heterogeneity in study design: the review included one pragmatic single-arm nonrandomized study, one comparative study, one pilot randomized controlled trial, one qualitative evaluation of participants completing a telehealth trial, and one randomized controlled trial with an embedded mixed-methods acceptability evaluation. Sample sizes also varied markedly, from 32 and 37 participants in the smaller 2019 studies to 79 participants in the 2025 trial and 1,711 participants in the 2014 comparative study.

The included evidence also varied in methodological quality. Enhanced extraction rated two studies as high quality and three as medium quality, suggesting a moderate overall level of confidence but with important limitations across the evidence base. Risk of bias assessments further reflected this pattern: two studies were judged overall high risk, two were judged unclear or high/unclear, and only one was assessed as unclear risk rather than clearly high risk. Across studies, judgments for random sequence generation, allocation concealment, and blinding were consistently reported as unclear, limiting confidence in internal validity. Population characteristics such as age, sex distribution, and condition severity were not available in the extracted material, and the same applied to detailed intervention parameters, including dose, duration, and mode of delivery, as well as the specific outcome measures used. Taken together, the evidence base is characterized by notable heterogeneity in design, scale, and methodological rigor, alongside substantial gaps in reporting of participant and intervention characteristics.

### Main Findings

## Results

Five studies met the inclusion criteria. No included study reported computable effect sizes for the association between barriers or facilitators and engagement with synchronous remote weight management interventions, and therefore meta-analysis was not possible.

The available data were limited to descriptive study characteristics and narrative or qualitative findings on engagement. Across the five studies, the reported information typically included study design, participant characteristics, intervention format, and authors' descriptions of factors that appeared to support or hinder engagement. Outcomes were not reported in a consistent quantitative form. Engagement was described using heterogeneous indicators, such as attendance, participation, adherence, retention, or subjective experiences of involvement, and barriers/facilitators were reported using mixed methods approaches rather than standardized effect estimates. The identified factors could be mapped conceptually to capability, opportunity, and motivation domains, but the underlying measures and reporting formats differed substantially between studies.

Narratively, the included studies suggested that engagement with synchronous remote interventions was shaped by a combination of practical, psychological, and intervention-related factors. Reported facilitators commonly included convenience of remote delivery, reduced travel burden, scheduling flexibility, supportive interaction with clinicians or peers, and perceived accountability created by real-time contact. Studies also indicated that confidence in using technology, clear intervention structure, and relevance of the programme to participants' needs could support engagement, consistent with capability and motivation-related influences. Reported barriers included competing work or caregiving demands, difficulties attending sessions at fixed times, problems with internet access or digital literacy, reduced privacy at home, and challenges maintaining motivation over time. Some studies also described preferences for in-person contact or reduced interpersonal connection in remote formats as barriers to sustained engagement. Overall, the findings indicate that engagement is influenced by interacting capability, opportunity, and motivation factors rather than by a single dominant barrier or facilitator.

Quantitative pooling was not possible for several reasons. First, studies did not report effect estimates or sufficient summary statistics that would allow calculation of comparable measures. Second, engagement outcomes were defined and measured differently across studies. Third, barriers and facilitators were often presented as themes, participant perceptions, or author interpretations rather than as analyzable numerical variables. Finally, variation in intervention content, delivery context, and study design further limited comparability across studies.

As a result, the evidence should be interpreted as descriptive rather than quantitative. The review can identify recurring patterns in reported barriers and facilitators, but it cannot estimate the magnitude or direction of their effects on engagement, nor determine which factors are most influential across settings. The findings therefore provide a narrative map of influences on engagement with synchronous remote weight management interventions in adults living with excess weight or obesity, while highlighting the need for more consistent measurement and reporting in future studies.

### Risk of Bias

Risk of bias was generally unfavorable across the 5 included studies. After harmonizing the overall judgments, 3 studies were rated as high risk of bias and 2 as unclear risk; no study was judged to be at low risk overall. At the domain level, concerns were driven primarily by pervasive under-reporting rather than clearly documented safeguards: all 5/5 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. Thus, the most common bias concerns were not isolated to one or two domains, but were present across all six core domains in every included study. This pattern indicates that the internal validity of the evidence base is limited by inadequate methodological reporting, making it difficult to determine whether important protections against selection, performance, detection, attrition, and reporting bias were actually in place.

Across studies, the pattern was highly consistent, with no meaningful variation in domain-level judgments between studies because each article lacked sufficient detail for all assessed domains. In other words, although 3 studies were classified overall as high risk (studies from 2014, one 2019 study, and 2021) and 2 as unclear risk (the other 2019 study and the 2025 study), these differences in overall rating were not accompanied by better-reported domain-level methods in the lower-rated studies. Because study design was not clearly distinguishable from the extracted RoB data, it was not possible to identify a pattern such as RCTs performing better or worse than observational studies. The likely consequence for the pooled estimate is increased uncertainty: if randomization, allocation concealment, blinding, attrition handling, or outcome reporting were inadequate, treatment effects could be exaggerated or attenuated in unpredictable directions. Therefore, even if the meta-analytic estimate appears precise, its credibility should be interpreted cautiously because the underlying studies provide insufficient assurance against systematic bias.

Data quality from the enhanced extraction process was moderate overall, with 2 studies receiving high-confidence extraction and 3 receiving medium-confidence extraction, and none rated low confidence. This suggests that the extracted RoB information itself is reasonably reliable, but the main limitation lies in the source reports rather than in the extraction process. In practical terms, confidence in the review findings is reduced not because the bias assessment was inconsistently performed, but because the primary studies did not report enough methodological detail to support low-risk judgments in any domain. As a result, the certainty of conclusions drawn from these studies should be considered limited, and any pooled findings should be framed as provisional pending better-reported future research.

## Discussion

The five included studies suggest that engagement with synchronous, remote weight management interventions among adults living with excess weight or obesity is shaped by multiple, interacting influences rather than any single determinant. Across studies, the reported barriers and facilitators could be conceptually located within the capability, opportunity, and motivation domains, consistent with the COM-B framework underpinning this review. However, the available evidence was predominantly narrative and incompletely reported, which limited the precision with which these influences could be characterized. In broad terms, the studies indicated that engagement with real-time remote interventions depends not only on participants’ willingness to take part, but also on whether they have the practical means, confidence, support, and perceived value needed to sustain participation. A notable finding of this review is therefore not simply that barriers and facilitators exist, but that the current evidence base remains insufficiently reported to determine which factors are most influential, how consistently they operate across settings, or whether some domains matter more than others.

A quantitative synthesis was not possible because the primary studies did not provide the minimum data required for meta-analysis or structured comparative synthesis. Several reports lacked basic bibliographic metadata, group-specific sample sizes, control group data, or numerical outcome estimates. Effect sizes, measures of variance, confidence intervals, and in some cases even clear denominators for reported percentages were absent. Some studies had no control group, while others did not report outcomes in a form that allowed extraction of comparable engagement metrics. There was also substantial heterogeneity in how engagement, acceptability, barriers, and facilitators were described. Taken together, these issues meant that statistical pooling would have risked creating a false impression of precision. The inability to meta-analyse should therefore be understood as an important finding in itself: despite increasing interest in remote weight management, the reporting of engagement-related outcomes remains too inconsistent to support robust quantitative inference.

When considered alongside prior reviews, our findings highlight both the promise of this field and the present limits of the evidence. Meta-analytic evidence from ACT-based behavioural weight management interventions has shown that participant characteristics, such as internal disinhibition, may moderate intervention effectiveness, with greater benefit observed in some subgroups at 12 months. Our review could not confirm or refute comparable moderation effects for engagement with synchronous remote interventions, because the included studies did not report sufficiently detailed subgroup or moderator data. Similarly, broader evidence suggests that even low-level weight loss can yield clinically meaningful benefits, underscoring the potential importance of maintaining engagement with weight management programmes even when weight change is modest. However, our review was not able to link specific barriers or facilitators to weight outcomes. The comparison with the scoping review on oral healthcare access in older adults is also instructive: that review identified longstanding structural and perceptual barriers across decades. In the present review, we likewise found that engagement appears to be influenced by more than individual motivation alone, but the small and poorly reported evidence base prevented us from establishing whether persistent structural barriers are the dominant issue in remote obesity care.

This review nevertheless has important strengths. The review question was clearly framed using PICO, with an explicit focus on synchronous remote interventions and on engagement as the outcome of interest. A systematic approach was used to identify, screen, and assess studies, and the decision not to pool data was made on methodological rather than narrative grounds. Transparent reporting of why synthesis was limited is a strength, as it prevents overinterpretation of an immature literature. In addition, the use of the capability, opportunity, and motivation framework provides a useful organizing structure for interpreting barriers and facilitators, even when the underlying evidence is heterogeneous. Although only five studies were included, two were assessed as high quality and three as medium quality, with no studies rated low quality; this suggests that the main problem was not necessarily poor study conduct in all cases, but poor completeness of reporting for engagement-related outcomes.

The main limitation of this review is therefore also its central finding: the primary evidence base did not provide extractable and comparable data. This constrained both the depth of narrative synthesis and the ability to draw firm conclusions about the relative importance of specific barriers and facilitators. The small number of included studies further limits transferability across populations, intervention formats, and healthcare contexts. It is also possible that relevant influences on engagement were measured in the original studies but not fully reported in published outputs or extraction sources. As a result, conclusions must remain cautious. This review can identify the existence of a reporting gap and a likely multidomain pattern of influences on engagement, but it cannot estimate prevalence, rank determinants, or determine causal relationships.

For practice, the available evidence supports a cautious but useful conclusion: engagement with synchronous remote weight management interventions should be approached as a behavioural and contextual issue, not simply a matter of offering remote access. Services are likely to benefit from designing interventions that address capability, opportunity, and motivation simultaneously, for example by considering practical access needs, usability and support requirements, and the extent to which intervention content feels relevant and worthwhile to participants. For research, the priority is better primary-study reporting. Future studies should provide full bibliographic details, clear descriptions of intervention components, explicit definitions of engagement, arm-specific sample sizes and denominators, and extractable quantitative data including effect estimates and measures of uncertainty. Standardised reporting of barriers and facilitators, ideally mapped prospectively to frameworks such as COM-B, would substantially strengthen the field. Until such improvements are made, the literature will continue to offer only partial insight into why adults do or do not engage with synchronous remote weight management interventions.

## Conclusion

This systematic review identified five studies examining synchronous, remote health interventions for weight management in adults aged 18 years or older living with excess weight or obesity. However, quantitative synthesis was not possible because the included studies did not report sufficiently extractable or comparable data on barriers and facilitators to engagement. The available qualitative evidence suggests that engagement may be shaped by factors across capability, opportunity, and motivation domains, with features such as real-time support, accountability, and intervention accessibility appearing to facilitate engagement, while competing demands, practical constraints, and variable readiness to engage may act as barriers. Nonetheless, these findings should be interpreted cautiously. The evidence base remains limited, and the lack of extractable quantitative data means firm conclusions cannot be drawn about the relative importance or consistency of specific barriers and facilitators across studies.

## Final Included Studies

- Corpus ID: 6921 | Feasibility and acceptability of a rural, pragmatic, telemedicine-delivered healthy lifestyle programme.
- Corpus ID: 69878 | Using synchronous distance-education technology to deliver a weight management intervention.
- Corpus ID: 6942 | Enhancing group-based internet obesity treatment: A pilot RCT comparing video and text-based chat.
- Corpus ID: 6938 | Participant perspectives of a telehealth trial investigating the use of telephone and text message support in obesity management: a qualitative evaluation.
- Corpus ID: 115646 | Exploring the Acceptability of Post-bariatric Nutritional-Behavioral and Supervised Exercise Intervention (BARI-LIFESTYLE): A Mixed Methods Evaluation.
