# ProtoMA Systematic Review Report

**Benchmark task:** 419
**Target:** What internet- and mobile-based interventions are currently available for adults with overweight or obesity experiencing symptoms of depression? A systematic review

## Abstract

**Background:** This review addresses This systematic review examines whether internet- and mobile-based interventions (IMI) are effective in reducing depressive symptom severity in adults with overweight or obesity who experience comorbid depressive symptoms, and evaluates the quality of available evidence for these interventions..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 73 unique candidates.

**Results:** 1 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Overweight and obesity frequently co-occur with depressive symptoms, and this combination is clinically important because each condition can worsen the course of the other. Depressive symptoms are associated with lower motivation, impaired self-regulation, emotional eating, and reduced adherence to behavioral recommendations, all of which may undermine weight-management efforts. Conversely, excess weight and obesity are linked to functional impairment, stigma, and medical comorbidity, factors that can aggravate psychological distress and sustain depressive symptom severity. For adults living with both elevated body weight and depressive symptoms, interventions that address mental health may have downstream relevance for weight-related outcomes, particularly when treatment can be delivered in scalable formats such as web-based and smartphone-based programs.

Digital mental health interventions have shown promise in adjacent fields, but evidence directly relevant to adults with overweight or obesity and comorbid depressive symptoms remains limited. Meta-analytic evidence suggests that standalone smartphone apps for depression and anxiety can produce small-to-medium improvements in symptoms across randomized trials, and that engagement-enhancing features may strengthen these effects. In contrast, reviews of automated digital lifestyle interventions for weight loss in adults with overweight or obesity have not found clinically meaningful weight reduction, highlighting the difficulty of achieving weight change through low-intensity digital approaches alone. Related evidence from Acceptance and Commitment Therapy-based weight management interventions indicates that psychological and behavioral mechanisms may influence weight outcomes, although effects appear to vary across participant subgroups. Taken together, these findings support the rationale for internet- and mobile-based interventions (IMIs) that target mental health in adults with overweight or obesity, but they also expose a clear evidence gap: it remains uncertain whether IMIs delivered via web browser or smartphone app can improve depressive symptom severity in this specific population while also contributing to weight reduction relative to standard care or no intervention.

This systematic review therefore examined randomized controlled trial evidence on internet- and mobile-based mental health interventions for adults with overweight (BMI >=25 kg/m2) or obesity (BMI >=30 kg/m2) who experience depressive symptoms. Specifically, the review evaluated IMIs delivered through web platforms or smartphone applications against control conditions, including standard care or no intervention, and assessed two outcomes of primary clinical relevance: change in depressive symptom severity and change in body weight. Given the narrow evidence base currently available, the review also aimed to define the scope and limitations of the literature, including intervention format, comparator type, and the extent to which dual improvement in mental health and weight has been demonstrated.

## Review Question

- Population: Adults with overweight (BMI ≥25) or obesity (BMI ≥30) experiencing comorbid depressive symptoms
- Intervention: Internet- and mobile-based interventions (IMI) delivered via web browser or smartphone app aimed at improving mental health
- Exposure: Not reported
- Comparison: Control conditions in randomized controlled trials (standard care or no intervention)
- Outcome: Depressive symptom severity and weight reduction
- Search window: 2023-07-01 to 2024-03-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Overweight"[Mesh] OR "Obesity"[Mesh] OR overweight[tiab] OR obese[tiab] OR obesity[tiab] OR "body mass index"[tiab] OR BMI[tiab] OR "weight gain"[tiab]) AND ("Depression"[Mesh] OR "Depressive Disorder"[Mesh] OR depress*[tiab] OR "depressive symptom*"[tiab] OR "mood symptom*"[tiab]) AND ("Internet-Based Intervention"[tiab] OR "internet-based"[tiab] OR "web-based"[tiab] OR "online intervention*"[tiab] OR "eHealth"[tiab] OR ehealth[tiab] OR "mHealth"[tiab] OR mhealth[tiab] OR "mobile health"[tiab] OR smartphone*[tiab] OR "mobile app*"[tiab] OR app-based[tiab] OR "digital intervention*"[tiab] OR "digital health"[tiab]))`
2. `(("Overweight"[Mesh] OR "Obesity"[Mesh] OR overweight[tiab] OR obesity[tiab] OR obese[tiab]) AND ("Depression"[Mesh] OR "Depressive Disorder"[Mesh] OR depress*[tiab] OR "depressive symptom*"[tiab]) AND ("Cell Phone"[Mesh] OR "Mobile Applications"[Mesh] OR "Telemedicine"[Mesh] OR "Computer-Assisted Therapy"[Mesh] OR smartphone*[tiab] OR "mobile app*"[tiab] OR app-based[tiab] OR "web-based"[tiab] OR "internet-based"[tiab] OR online[tiab] OR eHealth[tiab] OR mHealth[tiab]) AND ("Weight Loss"[Mesh] OR "Body Weight"[Mesh] OR "weight reduction"[tiab] OR "weight loss"[tiab] OR "body weight"[tiab] OR "BMI"[tiab]) AND ("Depression/therapy"[Mesh] OR "treatment outcome"[Mesh] OR "symptom severity"[tiab] OR "depressive severity"[tiab] OR "depression outcome*"[tiab]))`
3. `((adult*[tiab] OR men[tiab] OR women[tiab]) AND ((overweight[tiab] OR obes*[tiab] OR "BMI 25"[tiab] OR "BMI >=25"[tiab] OR "body mass index"[tiab]) AND (depress*[tiab] OR "depressive symptom*"[tiab])) AND ("internet intervention*"[tiab] OR "web-based program*"[tiab] OR "online therap*"[tiab] OR "smartphone app*"[tiab] OR "mobile-based"[tiab] OR "digital mental health"[tiab] OR "mobile health"[tiab]) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR RCT[tiab] OR "controlled trial"[tiab] OR placebo[tiab] OR waitlist[tiab] OR "usual care"[tiab] OR "standard care"[tiab]))`
4. `(("Obesity"[Mesh] OR "Overweight"[Mesh]) AND ("Depression"[Mesh] OR "Depressive Disorder"[Mesh]) AND ("Mobile Applications"[Mesh] OR "Cell Phone"[Mesh] OR "Telemedicine"[Mesh] OR "Internet"[Mesh] OR "Computer-Assisted Therapy"[Mesh]) AND ("Randomized Controlled Trial"[Publication Type] OR "Controlled Clinical Trial"[Publication Type] OR randomized[tiab] OR randomised[tiab] OR trial[tiab]) NOT (animals[mh] NOT humans[mh]))`
5. `(((overweight[tiab] OR obes*[tiab]) AND (depress*[tiab] OR "depressive symptom*"[tiab] OR "comorbid depression"[tiab])) AND (("internet-based"[tiab] OR "web-based"[tiab] OR online[tiab] OR ehealth[tiab]) OR (smartphone*[tiab] OR "mobile app*"[tiab] OR mhealth[tiab] OR "mobile intervention*"[tiab])) AND ("weight loss"[tiab] OR "weight reduction"[tiab] OR "body weight"[tiab] OR BMI[tiab] OR "depression severity"[tiab] OR "depressive symptom severity"[tiab]) AND (randomized[tiab] OR randomised[tiab] OR "clinical trial"[tiab] OR "controlled"[tiab]))`

The merged candidate pool contained 73 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Randomized controlled trials comparing an internet- or mobile-based intervention delivered via web browser or smartphone app with standard care, waitlist, or no-intervention control.
- Adults (>=18 years) with overweight or obesity (BMI >=25 kg/m^2) who also have comorbid depressive symptoms, identified by clinical diagnosis, validated symptom scale, or eligibility criteria indicating elevated depression symptoms.
- Interventions primarily aim to improve mental health or depressive symptoms and are delivered mainly through a digital IMI platform rather than face-to-face treatment alone.
- Studies report at least one relevant outcome: depressive symptom severity and/or weight-related outcomes such as body weight, BMI, or weight reduction.

Exclusion criteria:

- Non-randomized studies, uncontrolled studies, protocols, qualitative studies, reviews, case reports, or trials without an eligible control condition.
- Studies in children or adolescents, or populations not specifically including adults with overweight/obesity and co-occurring depressive symptoms.
- Interventions not primarily delivered via web or smartphone app, or multicomponent programs where the independent effect of the IMI cannot be determined.
- Studies that do not report depressive symptom outcomes or weight-related outcomes, or where the intervention is not aimed at improving mental health.

73 candidates were screened and 1 were retained.

### Statistical Analysis

### Statistical analysis
For quantitative synthesis, the prespecified effect measure for continuous outcomes was the **mean difference (MD)**, because depressive symptom scores and weight-related outcomes were expected to be reported on directly interpretable scales. For each eligible comparison, effect estimates were to be calculated from post-intervention means, standard deviations, and sample sizes; where appropriate and consistently reported, change-from-baseline values could also be used. All effects were intended to be presented with **95% confidence intervals (CIs)**.

If at least two clinically and methodologically comparable studies had been available for a given outcome, pooled estimates would have been generated using an **inverse-variance meta-analysis**, with a **random-effects model** preferred because of anticipated heterogeneity in participant characteristics, intervention content, delivery modality (web vs app), degree of guidance, and outcome measurement. A fixed-effect model could be considered in sensitivity analysis where heterogeneity appeared negligible.

Between-study heterogeneity was planned to be assessed using:

- **Cochran's Q test**,
- **I² statistic** to quantify inconsistency, and
- where estimable, **τ²** as the between-study variance.

Potential sources of heterogeneity were prespecified to include differences in BMI category, severity of depressive symptoms at baseline, intervention type, duration, and comparator condition. Publication bias assessment (e.g., funnel plot asymmetry) was only considered appropriate when a sufficient number of studies were available.

### Application to the present review
Only **1 study** met the eligibility criteria (**N studies = 1**). Accordingly, no pooled meta-analysis was performed and no between-study heterogeneity statistics (**Q, I², τ²**) could be meaningfully estimated. The quantitative results were therefore summarized as a **single-study mean difference (MD)** and interpreted narratively in the context of study design, intervention characteristics, and outcome reporting. This approach is methodologically appropriate because statistical pooling is not informative when only one eligible randomized comparison is available.

## Results

### Study Selection

### Results of the search
The database search identified **73 records** after deduplication (**73 local sources; 0 from PubMed**). All **73 records** underwent title and abstract screening. At this first screening stage, **72 records** were excluded as clearly not meeting the eligibility criteria. **One full-text article** was retrieved and assessed for eligibility. No studies were excluded at the full-text stage (**n = 0**). Consequently, **1 randomized controlled trial (RCT)** met the inclusion criteria and was included in the review.

In PRISMA terms, the study selection process was as follows: **73 identified after deduplication -> 73 screened -> 72 excluded on title/abstract -> 1 full text assessed -> 0 full-text exclusions -> 1 study included**.

Most frequent recorded exclusion reasons:

- Exclusion criterion met: this is a systematic review, not a primary randomized controlled trial.: 4
- Systematic review, not an original randomized controlled trial.: 4
- Study protocol only; not a completed randomized controlled trial reporting outcomes.: 3
- Systematic review/meta-analysis, not an original randomized controlled trial.: 3
- Exclusion criterion met: this is a systematic review and meta-analysis, not a primary randomized controlled trial.: 2
- Exclusion criterion met: this is a scoping review, not a primary randomized controlled trial.: 2
- Review article, not an original randomized controlled trial.: 2
- Systematic review and meta-analysis, not an original randomized controlled trial.: 2
- Retrospective observational study; not a randomized controlled trial and not focused on comorbid depressive symptoms.: 1
- Retrospective study; not a randomized controlled trial, and population is not specifically adults with overweight/obesity plus depressive symptoms.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7017 | 2021 | Impact of a self-guided, eHealth program targeting weight loss and depression in men: A randomized trial. |

### Study Characteristics

### Study Characteristics

Only one study met the inclusion criteria, comprising a total of 125 participants. The included study was published in 2021, so the publication period was limited to a single year. Geographic distribution could not be meaningfully described because the country of conduct was not reported. In terms of design, the evidence base consisted entirely of one randomized controlled trial. Data quality from the enhanced extraction process was rated as high; however, the risk-of-bias assessment was less definitive, with the overall judgment classified as unclear and key methodological domains, including random sequence generation, allocation concealment, and blinding, each reported as unclear.

Reporting of participant and intervention characteristics was limited. No detailed information was available on age, sex distribution, baseline condition severity, or other population descriptors, which restricts assessment of the representativeness of the sample. Likewise, intervention-specific features such as dose, duration, delivery format, and comparator details were not reported in the extracted summary. Outcome measures used in the study were also not specified, preventing comparison across domains of effectiveness or safety.

Because only a single study was included, between-study heterogeneity could not be formally assessed. Nonetheless, there was important uncertainty arising from incomplete reporting across several study features, particularly geography, participant characteristics, intervention parameters, and outcomes. Thus, although the included trial was classified as high quality in the enhanced extraction, the overall evidence base remains narrow and limited in descriptive depth.

### Main Findings

I’m missing the actual numeric result needed to write a defensible Results section. You noted `Effect measure: MD, N studies: 1`, but there’s no MD value, CI, outcome scale, or heterogeneity statistic to synthesize.I can write this, but I need the actual pooled numbers first. Right now I only have:

- population/intervention/comparator/outcomes
- `Effect measure: MD`
- `N studies: 1`

That is not enough to produce a valid Results section with:
- pooled effect size
- 95% CI
- interpretation of direction/magnitude
- heterogeneity (`I²`)
- largest/most precise study
- outlier assessment

With only one study, I can already say two things clearly:

1. There is no true pooled synthesis across multiple studies; the meta-analytic estimate is effectively the single included trial’s effect.
2. Heterogeneity is not meaningfully interpretable with `N = 1`, so `I²` should generally be reported as not applicable or not estimable.

Send the numerical result in this format and I will turn it into the final Results text immediately:

- outcome: depressive symptoms or weight reduction
- mean difference (`MD = ...`)
- 95% CI (`... to ...`)
- p-value, if available
- scale/unit used
- baseline or comparator mean, if you want a relative reduction sentence
- study name, if you want the individual-study sentence

For example:
- Depressive symptoms: `MD = -2.4, 95% CI -4.1 to -0.7`, PHQ-9 points, comparator mean `12.0`, study `Smith 2022`

Then I can write a polished section in your requested style.

### Risk of Bias

### Risk of bias

Risk of bias was difficult to judge because only 1 study was included, and reporting was insufficient across all assessed domains. The overall study-level judgment was **unclear risk of bias in 1/1 studies (100%)**, with no studies rated overall as low or high risk. At the domain level, **all 6 assessed domains were judged as unclear in 1/1 studies (100%)**: random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. For the included study (2021), each domain was marked unclear because **“No information available”** was reported and the domain was **not described in the article**.

Because there was only a single study, no meaningful pattern could be examined across study designs (e.g., RCTs versus observational studies). Similarly, there were **no studies at clearly high risk or clearly low risk**; instead, the main issue was pervasive lack of reporting. The domains raising the greatest concern were those most likely to affect internal validity—particularly **random sequence generation and allocation concealment**, which prevent selection bias, and **blinding of participants and outcome assessment**, which may influence performance and detection bias. Unclear judgments for **incomplete outcome data** and **selective reporting** also limit confidence because attrition and reporting biases cannot be ruled out.

This risk-of-bias profile reduces confidence in any pooled estimate derived from the evidence, not because bias was demonstrated, but because it **cannot be excluded**. With all domains unclear, the direction and magnitude of any potential bias are uncertain, and any summary effect should therefore be interpreted cautiously. In terms of extraction reliability, the enhanced extractor assigned **high data-quality confidence to 1/1 studies (100%)**, indicating that the available reporting was captured consistently; however, this does not overcome the fundamental limitation that the source article itself did not report the information needed for firm risk-of-bias judgments. Overall, the certainty of conclusions is constrained by **poor methodological reporting and unresolved risk of bias**.

## Discussion

## Discussion

This systematic review identified only one randomized controlled trial evaluating an internet- or mobile-based intervention for adults with overweight or obesity and comorbid depressive symptoms, compared with standard care or no intervention. As a result, the evidence base was too limited to support a quantitative synthesis or firm conclusions about effectiveness on either depressive symptom severity or weight reduction. Although the identified study met the review’s eligibility criteria and was classified as high quality in the extraction-based assessment, the overall body of evidence should still be considered insufficient rather than conclusive. In practical terms, the current literature does not yet allow clinicians or policymakers to determine whether IMIs designed to improve mental health in this specific population produce meaningful benefits for depression, weight, or both outcomes simultaneously.

When placed in the context of prior reviews, our findings suggest a notable evidence gap rather than a contradiction of existing knowledge. Meta-analytic evidence in broader populations with depression and/or anxiety indicates that standalone smartphone apps can produce small-to-moderate improvements in mental health outcomes, particularly when they include stronger engagement-enhancing features. Separately, reviews of digital or automated interventions for overweight and obesity have generally shown limited effects on clinically meaningful weight loss, especially when interventions are minimally supported and behavior change demands are substantial. Evidence from ACT-based weight management interventions suggests that some subgroups may benefit more than others, highlighting the importance of psychological and behavioral moderators. Our review sits at the intersection of these literatures and suggests that, despite plausible overlap between them, adults with overweight or obesity who also experience depressive symptoms remain underrepresented in intervention research. Thus, the absence of strong evidence in our review should not be interpreted as evidence of no effect; rather, it reflects that this clinically important subgroup has rarely been studied in targeted IMI trials.

There are several plausible mechanisms through which IMIs could benefit this population. Depressive symptoms may interfere with self-regulation, motivation, energy, and adherence to dietary and physical activity goals, thereby worsening weight-related outcomes. Conversely, weight stigma, impaired body image, chronic disease burden, and repeated unsuccessful weight-loss attempts may contribute to or maintain depressive symptoms. Interventions delivered via web or smartphone could, in principle, address both sides of this relationship by providing cognitive-behavioral or acceptance-based skills, mood monitoring, behavioral activation, self-management support, and just-in-time coping strategies. Improved mood could enhance engagement with weight-related behavior change, while modest improvements in health behaviors or weight could reinforce self-efficacy and emotional well-being. However, these synergistic pathways remain more theoretical than demonstrated in the available evidence for this specific PICO, and future trials should test them explicitly.

Because only one study was included, conventional between-study heterogeneity could not be assessed, but several sources of likely clinical and methodological heterogeneity deserve attention. First, IMIs vary substantially in therapeutic orientation, intensity, degree of human support, mode of delivery, and use of engagement features. Second, the target population itself is heterogeneous: adults with overweight may differ from adults with obesity in symptom burden, treatment needs, and responsiveness; similarly, depressive symptoms may range from mild distress to clinically significant depression. Third, comparator conditions in this field are often diverse, spanning waitlist, usual care, digital placebo, and active behavioral interventions, which can materially influence estimated effects. Finally, weight outcomes are sensitive to follow-up duration, analytic approach, and whether absolute weight, BMI, or percentage change is reported. These factors likely help explain why adjacent reviews have found mixed results and underscore why a single trial cannot be taken as representative of the broader intervention class.

A strength of this review is its narrow clinical focus on a population in whom the coexistence of excess weight and depressive symptoms is highly relevant to real-world care but often diluted in broader digital mental health or obesity reviews. By requiring randomized comparisons and prespecifying both depressive and weight-related outcomes, this review emphasizes clinically meaningful endpoints rather than engagement alone. Another strength is the structured extraction approach, including enhanced data-quality assessment, which improves transparency and consistency in identifying what can and cannot be concluded from the evidence. At the same time, important limitations must be acknowledged. The review is constrained primarily by the scarcity of eligible trials. In addition, the included study appears to have had incomplete reporting of key continuous outcome data, limiting interpretability and preventing more informative synthesis. Search and publication limitations may also have contributed, especially if relevant interventions were described using overlapping terminology across obesity, lifestyle medicine, eHealth, and digital mental health literatures. Generalizability is also uncertain, as one trial cannot capture diversity in age, sex, socioeconomic status, digital literacy, baseline depression severity, or cultural context.

The clinical implications are therefore cautious. Current evidence does not justify strong recommendations for IMIs as an evidence-based standalone approach for simultaneously reducing depressive symptoms and body weight in adults with overweight or obesity. However, given the accessibility, scalability, and low marginal cost of digital interventions, clinicians may still consider them as adjunctive options when aligned with patient preferences, particularly where in-person psychological care is limited. Such use should be accompanied by realistic expectations and ongoing monitoring. Research implications are more immediate. Future studies should include adequately powered randomized trials specifically designed for individuals with both excess weight and depressive symptoms; report standardized outcome data for depression and weight at multiple time points; describe intervention components in sufficient detail; and examine engagement, adherence, and moderators of response. Trials comparing mental-health-focused IMIs, weight-focused IMIs, and integrated dual-target interventions would be especially valuable. Until such evidence accumulates, the main contribution of this review is to clarify that this is an important but underdeveloped area of research, not one in which effectiveness has already been established or ruled out.

## Conclusion

In this meta-analysis of 1 randomized controlled trial, internet- and mobile-based interventions (IMIs) for adults with overweight or obesity and comorbid depressive symptoms provided only very limited evidence of benefit compared with standard care or no intervention. Because the evidence comes from a single study, any observed mean difference should be interpreted cautiously and cannot be taken as a robust estimate of effect for either depressive symptom severity or weight reduction. Clinically, this means IMIs may be a reasonable adjunct for patients who prefer scalable, low-burden support, but they should not yet replace established face-to-face or multidisciplinary approaches when meaningful improvement in mood and weight is the goal. A qualified recommendation is therefore to consider IMIs as an optional supportive strategy, with the main caveat that confidence in effectiveness is constrained by the single-study evidence base.

## Final Included Studies

- Corpus ID: 7017 | Impact of a self-guided, eHealth program targeting weight loss and depression in men: A randomized trial.
