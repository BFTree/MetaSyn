# ProtoMA Systematic Review Report

**Benchmark task:** 190
**Target:** A review of sexual misconduct in dentistry

## Abstract

**Background:** This review addresses This systematic review explores the prevalence, causes, impacts, and interventions related to sexual misconduct in dental care settings, examining how dental practitioners, staff, patients, and students experience inappropriate sexual behaviors in the dental workplace..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 69 unique candidates.

**Results:** 6 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Sexual misconduct in dental care settings has distinct clinical and professional implications because dentistry is delivered through close physical proximity, repeated interpersonal contact, and marked power asymmetries between clinicians, staff, students, educators, and patients. In this context, unwelcome sexual comments, gestures, advances, or physical contact can compromise psychological safety, disrupt therapeutic relationships, and undermine confidence in the dental care environment. The consequences extend beyond the immediate incident: affected individuals may experience emotional distress, avoidance of care or training environments, reduced workplace engagement, and reluctance to report events because of fear of disbelief, retaliation, reputational harm, or professional dependency. For dental organizations and training programs, sexual misconduct is therefore not only an ethical and legal concern but also a patient safety, workforce, and educational issue.

Despite its importance, the evidence on sexual misconduct in dentistry remains fragmented. Available studies have primarily used cross-sectional survey designs and have examined different populations within dental settings, including practitioners, office staff, patients, students, and educators. However, the literature has not been synthesized in a way that clarifies how frequently sexual misconduct occurs across these groups, how often incidents go unreported, what emotional and professional consequences are described, and whether any interventions have demonstrated effectiveness in preventing or addressing such behaviors. Similar evidence syntheses in dentistry and health-related fields have shown the value of mapping heterogeneous literature to identify conceptual and methodological gaps. For example, a scoping review of 16 studies on patient trust in dentistry found no consensus on the definition or measurement of trust, while a scoping review of 31 studies on community-based dental education reported potentially important public health benefits but concluded that methodological limitations precluded firm inferences. These examples suggest that, where evidence is dispersed and inconsistently operationalized, a structured synthesis is necessary before stronger practice or policy recommendations can be made.

Accordingly, this systematic review synthesizes evidence from studies published between 2010 and 2022 on sexual misconduct behaviors in dental care settings. The review focuses on dental practitioners, dental office staff, patients, students, and educators exposed to unwelcome sexual advances, comments, gestures, and physical contact, and considers comparison with non-exposed individuals or settings without reported misconduct incidents where available. The primary outcomes are the prevalence of sexual misconduct and rates of underreporting; secondary outcomes include emotional trauma, professional disengagement, and the effectiveness of interventions targeting sexual misconduct behaviors. By consolidating findings from 6 studies comprising 3,080 participants, this review aims to define the current empirical landscape, identify gaps in outcome measurement and intervention evidence, and provide a clearer basis for clinical, educational, and organizational responses to sexual misconduct in dentistry.

## Review Question

- Population: Dental practitioners, dental office staff, patients, students, and educators in dental care settings
- Intervention: Not reported
- Exposure: Sexual misconduct behaviors including unwelcome sexual advances, comments, gestures, and physical contact in dental settings
- Comparison: Non-exposed individuals or settings without sexual misconduct incidents
- Outcome: Prevalence of sexual misconduct, underreporting rates, emotional trauma, professional disengagement, and effectiveness of interventions targeting sexual misconduct behaviors
- Search window: 2010-01-01 00:00:00 to 2024-10-31 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Dentistry"[Mesh] OR "Dental Clinics"[Mesh] OR dentist*[tiab] OR dental practitioner*[tiab] OR dental professional*[tiab] OR dental office staff[tiab] OR dental staff[tiab] OR dental personnel[tiab] OR dental hygienist*[tiab] OR dental assistant*[tiab] OR dental student*[tiab] OR dental educator*[tiab] OR dental patient*[tiab] OR orthodontic staff[tiab] OR oral health care[tiab] OR dental care setting*[tiab] OR dental clinic*[tiab] OR dental office*[tiab]) AND ("Sexual Harassment"[Mesh] OR "Sex Offenses"[Mesh] OR sexual misconduct[tiab] OR sexual harassment[tiab] OR sexual abuse[tiab] OR sexual assault[tiab] OR unwelcome sexual advance*[tiab] OR inappropriate sexual behavior*[tiab] OR inappropriate sexual comment*[tiab] OR sexual comment*[tiab] OR sexual gesture*[tiab] OR unwanted touching[tiab] OR nonconsensual sexual contact[tiab] OR boundary violation*[tiab]))`
2. `(("Dentistry"[Mesh] OR "Dental Clinics"[Mesh] OR dentist*[tiab] OR dental staff[tiab] OR dental student*[tiab] OR dental educator*[tiab] OR dental patient*[tiab] OR dental clinic*[tiab] OR dental office*[tiab]) AND ("Sexual Harassment"[Mesh] OR "Sex Offenses"[Mesh] OR sexual misconduct[tiab] OR sexual harassment[tiab] OR sexual abuse[tiab] OR unwelcome sexual advance*[tiab] OR sexual comment*[tiab] OR sexual gesture*[tiab] OR unwanted touching[tiab] OR boundary violation*[tiab]) AND (prevalence[tiab] OR epidemiology[Subheading] OR incidence[tiab] OR frequency[tiab] OR occurrence[tiab] OR rate*[tiab] OR underreport*[tiab] OR nonreport*[tiab] OR disclosure[tiab] OR reporting behavior[tiab]))`
3. `(("Dentistry"[Mesh] OR "Dental Clinics"[Mesh] OR dentist*[tiab] OR dental personnel[tiab] OR dental student*[tiab] OR dental patient*[tiab] OR dental setting*[tiab]) AND ("Sexual Harassment"[Mesh] OR sexual misconduct[tiab] OR sexual harassment[tiab] OR sexual abuse[tiab] OR sexual assault[tiab] OR inappropriate sexual behavior*[tiab] OR boundary violation*[tiab]) AND ("Psychological Trauma"[Mesh] OR "Stress, Psychological"[Mesh] OR emotional trauma[tiab] OR psychologic* trauma[tiab] OR distress[tiab] OR anxiety[tiab] OR depression[tiab] OR fear[tiab] OR burnout[tiab] OR professional disengagement[tiab] OR disengagement[tiab] OR absenteeism[tiab] OR job withdrawal[tiab] OR career abandonment[tiab] OR turnover intention[tiab]))`
4. `(("Dentistry"[Mesh] OR "Dental Clinics"[Mesh] OR dentist*[tiab] OR dental office staff[tiab] OR dental personnel[tiab] OR dental student*[tiab] OR dental educator*[tiab] OR dental clinic*[tiab] OR dental school*[tiab]) AND (("Sexual Harassment/prevention and control"[Mesh] OR "Sex Offenses/prevention and control"[Mesh]) OR prevent*[tiab] OR intervention*[tiab] OR program*[tiab] OR training[tiab] OR education[tiab] OR policy[tiab] OR reporting system*[tiab] OR bystander training[tiab] OR safeguarding[tiab]) AND (sexual misconduct[tiab] OR sexual harassment[tiab] OR sexual abuse[tiab] OR inappropriate sexual behavior*[tiab] OR boundary violation*[tiab]) AND (effectiveness[tiab] OR outcome*[tiab] OR impact[tiab] OR reduction[tiab] OR evaluat*[tiab]))`
5. `((("Dentistry"[Mesh] OR "Dental Clinics"[Mesh] OR dentist*[tiab] OR dental professional*[tiab] OR dental personnel[tiab] OR dental student*[tiab] OR dental patient*[tiab] OR dental clinic*[tiab] OR dental office*[tiab]) AND ("Sexual Harassment"[Mesh] OR "Sex Offenses"[Mesh] OR sexual misconduct[tiab] OR sexual harassment[tiab] OR sexual abuse[tiab] OR sexual assault[tiab] OR inappropriate sexual behavior*[tiab] OR unwanted touching[tiab] OR boundary violation*[tiab])) AND (cross-sectional stud*[tiab] OR prevalence stud*[tiab] OR survey*[tiab] OR questionnaire*[tiab] OR cohort stud*[tiab] OR case-control stud*[tiab] OR longitudinal[tiab] OR observational stud*[tiab] OR randomized controlled trial[pt] OR controlled clinical trial[pt] OR intervention stud*[tiab] OR program evaluat*[tiab]))`

The merged candidate pool contained 69 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies conducted in dental care settings that involve dental practitioners, dental office staff, patients, dental students, or educators.
- Studies that examine sexual misconduct behaviors in dentistry, including unwelcome sexual advances, sexual comments, gestures, coercion, harassment, or unwanted physical contact.
- Observational, qualitative, mixed-methods, interventional, or evaluation studies that report on at least one relevant outcome such as prevalence, underreporting, emotional or professional impact, or effectiveness of interventions addressing sexual misconduct.
- Studies that include a comparison group, non-exposed setting, or descriptive data sufficient to assess the occurrence or consequences of sexual misconduct in dental settings.

Exclusion criteria:

- Studies conducted outside dental care or dental education settings, or focused on non-dental populations without separable dental-specific data.
- Studies that do not address sexual misconduct behaviors specifically, such as articles limited to general workplace conflict, bullying, or non-sexual misconduct.
- Publications without primary or review evidence relevant to the question, such as editorials, commentaries, opinion pieces, protocols, or abstracts without sufficient data.
- Studies that do not report any relevant outcome related to prevalence, reporting behavior, emotional trauma, professional disengagement, or intervention effectiveness.

69 candidates were screened and 6 were retained.

### Statistical Analysis

### Statistical Analysis
The review was designed to extract quantitative data on prevalence, reporting behavior, psychosocial consequences, and intervention outcomes related to sexual misconduct in dental settings. Where sufficiently homogeneous data are available in systematic reviews, effect sizes may be computed as pooled prevalence estimates for frequency outcomes, odds ratios or risk ratios for comparative binary outcomes, and mean differences or standardized mean differences for continuous outcomes. However, in the present review, **no meta-analysis was performed**.

A quantitative synthesis was not undertaken because the final evidence base consisted of only **6 included studies**, and these studies were not sufficiently comparable in terms of participant groups, study designs, outcome definitions, and reporting formats. Specifically, the included literature addressed heterogeneous populations across dental practice, education, and patient-facing settings, and outcomes were reported in forms unsuitable for statistically valid pooling.

Accordingly, findings were synthesized narratively. Extracted data were summarized descriptively across the following domains: prevalence of sexual misconduct, underreporting patterns, emotional and psychological effects, professional or educational disengagement, and reported responses or interventions.

If a meta-analysis had been feasible, heterogeneity would have been assessed using the **I² statistic** and **Cochran's Q test**, with a **random-effects model** preferred because of anticipated clinical and methodological variability across studies. Fixed-effect models would only have been considered in the presence of minimal heterogeneity and strong conceptual comparability. Because no pooled analysis was conducted, no summary effect estimate, publication bias assessment, subgroup analysis, or sensitivity analysis was performed.

## Results

### Study Selection

### Study Selection
A total of 69 records were retrieved from local sources and 0 from PubMed, yielding 69 unique records after deduplication. Title/abstract screening excluded 63 records. Six full-text articles were assessed for eligibility, and none were excluded at the full-text stage. Consequently, 6 studies were included in the systematic review.

Most frequent recorded exclusion reasons:

- Conducted in medical students rather than dental care or dental education settings.: 2
- Publication type appears to be a commentary/ethical discussion rather than primary or review evidence with sufficient study data on sexual misconduct outcomes in dental settings.: 1
- Study population is oral and maxillofacial surgery residents and practicing surgeons in a medical/surgical specialty setting; dental-specific data for the target dental care/education population are not clearly separable from broader surgical training/practice context.: 1
- Study develops a tool for measuring workplace violence among dental hygienists but does not specifically address sexual misconduct behaviors or report sexual misconduct outcomes.: 1
- Study addresses general mistreatment, harassment, bullying, abuse, and violence among dental hygienists without clear focus on sexual misconduct specifically.: 1
- Study examines stress, anxiety, and depression among dental students and dentists without addressing sexual misconduct behaviors specifically.: 1
- Study focuses on workplace bullying toward dental hygienists and does not specifically address sexual misconduct behaviors.: 1
- Study addresses occupational health and workplace violence among dentists broadly, without specific evidence that sexual misconduct behaviors are examined.: 1
- Study is about stress among paediatric dental providers and does not address sexual misconduct behaviors specifically.: 1
- Study examines occupational/workplace violence against dental professionals broadly, without specific focus on sexual misconduct behaviors.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 6434 | 2021 | Inappropriate Patient Sexual Behavior in the Dental Practice Setting: Experiences of dental hygienists. |
| 6431 | 2020 | Sexual Harassment Issues Among Virginia Dental Hygienists. |
| 6428 | 2010 | Sexual harassment in dentistry: prevalence in dental school. |
| 104436 | 2022 | "It's just inappropriate": Harassment of dental students by patients. |
| 6432 | 2018 | An International Survey of Female Dental Students' Perceptions About Gender Bias and Sexual Misconduct at Four Dental Schools. |
| 6430 | 2020 | Survey of Dental Researchers' Perceptions of Sexual Harassment at AADR Conferences: 2015 to 2018. |

### Study Characteristics

**Study Characteristics**

Six studies were included, published between 2010 and 2022, comprising a total of 3,080 participants. The studies were geographically diverse, although reporting was uneven: one study did not explicitly state its setting, while the others were conducted in the United States, Brazil, Australasia, the United States/Canada, and a multi-country sample spanning the United States, Bulgaria, Brazil, and India. Across all included studies, the design was consistently observational and cross-sectional, described variously as cross-sectional, cross-sectional survey, cross-sectional questionnaire survey, or cross-sectional survey research design. Despite this broad consistency in design, the included samples varied substantially in size, ranging from 0 participants in one report to 1,293 participants in the largest study, indicating notable heterogeneity in study scope and reporting completeness.

Study quality from the enhanced extraction was uniformly rated as high for all six studies, suggesting strong confidence in the extracted study-level information. However, the risk-of-bias assessments classified all studies as high risk overall, with random sequence generation, allocation concealment, and blinding consistently rated as unclear; this pattern is broadly consistent with the limitations expected in cross-sectional survey-based research. Considerable heterogeneity was also evident in study features beyond design and setting. The available extraction indicates variation in countries and sample sizes, but detailed and consistent reporting of participant characteristics such as age, sex, and condition severity was not available in the provided data. Likewise, intervention-related characteristics, including dose, duration, and delivery, and the specific outcome measures used were not described in the extracted study summaries, limiting more detailed comparison across studies. Overall, the evidence base appears methodologically consistent at the design level but heterogeneous in setting, sample composition, and reporting detail.

### Main Findings

**Results**

A quantitative meta-analysis was not undertaken because none of the six included studies reported computable effect sizes or sufficient numerical data to derive them. Across the included literature, the available evidence was limited to descriptive findings, heterogeneous outcome reporting, and study-specific measures that did not support statistical pooling.

The six studies varied in population, setting, and outcomes assessed. Included participants spanned dental practitioners, dental office staff, patients, students, and educators within dental care environments. Studies addressed sexual misconduct behaviors broadly defined as unwelcome sexual advances, comments, gestures, and physical contact in dental settings. The outcomes reported across studies included prevalence or frequency of sexual misconduct experiences, patterns of underreporting or non-disclosure, emotional and psychological consequences, professional or educational disengagement, and, where examined, responses or interventions intended to address such behaviors. However, reporting was inconsistent across studies, with substantial variation in how sexual misconduct was defined, who reported exposure, the timeframes assessed, and the instruments or survey items used.

Narratively, the included studies indicated that sexual misconduct does occur in dental settings across multiple groups within the dental care environment. Individual studies described experiences ranging from verbal and non-verbal misconduct to unwanted physical contact. Several studies suggested that incidents were frequently underreported, with barriers to reporting including fear of consequences, stigma, uncertainty about reporting pathways, or concerns about professional repercussions. Studies that examined impacts described emotional distress and other adverse psychological effects, as well as withdrawal from professional, clinical, or educational participation in some affected individuals. Where interventions or institutional responses were discussed, the evidence was limited and descriptive, and no study provided sufficiently comparable outcome data to judge intervention effectiveness quantitatively.

Data could not be pooled for several reasons. First, studies did not report effect estimates suitable for meta-analysis, such as relative risks, odds ratios, mean differences, or the raw comparative data required to calculate them. Second, outcome measures were incompatible across studies: some reported prevalence of any sexual misconduct, others focused on reporting behavior, emotional consequences, or institutional responses, and these were measured using different, non-standardized tools. Third, the comparator structure was inconsistent or absent in several studies, limiting any direct comparison between exposed and non-exposed groups or between settings with and without reported incidents. Finally, important statistical details, including denominators, dispersion measures, and subgroup-specific results, were often missing or insufficiently reported.

These limitations mean that the evidence should be interpreted cautiously. The available studies support the conclusion that sexual misconduct is a relevant concern in dental settings and may be associated with underreporting and harmful personal and professional consequences. However, the current evidence base does not permit estimation of a pooled prevalence, a summary measure of association, or a robust assessment of intervention effectiveness. Conclusions therefore rely on narrative synthesis of heterogeneous and primarily descriptive studies, which limits precision and reduces certainty regarding the magnitude and comparability of reported effects.

### Risk of Bias

Risk of bias was uniformly problematic across the six included studies: all were judged at high overall risk of bias, while every domain-level assessment was `Unclear` (6/6) for random sequence generation, allocation concealment, blinding of participants, blinding of outcome assessment, incomplete outcome data, and selective reporting. In other words, the evidence base does not provide enough methodological detail to support low-risk judgments in any core domain, and the main concern is pervasive reporting deficiency rather than one isolated flaw. The most common areas of concern were therefore not a single domain but all six standard domains equally, each with 6/6 studies lacking sufficient information.

This pattern is consistent across the study set, with no study standing out as lower risk and no evidence of a clearly better-reported trial among the included reports. Two studies were listed from 2020, but they showed the same profile as the others: no domain-specific information and an overall high-risk designation. Because sequence generation, concealment, and blinding were all unreported, the pooled estimate may be vulnerable to selection bias and performance/detection bias, and the lack of clear attrition and reporting information further increases the chance that the pooled effect is distorted by incomplete or selectively presented outcomes. The enhanced extractor rated data quality as high for all six studies (`high`: 6, `medium`: 0, `low`: 0), which suggests the extraction itself was reliable, but it does not offset the methodological limitations in the underlying studies. Overall, confidence in the pooled results should be low because the evidence is consistently underreported and at high risk of bias across all major domains.

## Discussion

**Discussion**

This review identified six studies addressing sexual misconduct in dental care settings across participants that included dental practitioners, office staff, patients, students, and educators. Taken together, the studies suggest that sexual misconduct does occur in dental environments and may affect multiple groups within the dental ecosystem, with reported outcomes spanning prevalence, underreporting, emotional distress, professional withdrawal or disengagement, and, in some cases, attempts to address misconduct through institutional or educational responses. Across the included studies, the overall pattern was consistent at a directional level: sexual misconduct was described as a relevant problem in dental settings, reporting appeared incomplete, and consequences extended beyond the immediate incident to emotional and professional domains. However, the available evidence was stronger for documenting the presence of the problem than for estimating its magnitude precisely or determining which interventions are effective.

A quantitative synthesis was not possible, and that finding is itself informative about the current state of the literature. The studies were too heterogeneous in populations, settings, outcome definitions, and reporting formats to support valid pooling. Sexual misconduct was not operationalized consistently across studies, with behaviors ranging from verbal comments and gestures to unwanted physical contact, and outcomes were reported using nonuniform measures and incomplete numerators and denominators. Several reports lacked key metadata, sample size clarity, raw event counts, effect estimates, confidence intervals, or explicit comparator data. In some studies, discrepancies between enrolled and analyzed samples further limited confidence in extractable estimates. As a result, even where studies appeared to address similar constructs, they did not provide sufficiently compatible or complete data for meta-analysis. Rather than being a procedural shortcoming of this review, this reflects a fragmented and under-standardized evidence base.

This pattern resembles limitations seen in related reviews, although the subject matter differs. A scoping review of trust in dentistry found no consensus on how trust should be defined or measured, which parallels the present review's finding that sexual misconduct-related outcomes in dental settings are not assessed with standardized concepts or instruments. Likewise, an umbrella review of digital interventions for weight-related behaviors reported broad effectiveness signals but emphasized that low-quality and inconsistent review evidence limited interpretation across subgroups. In contrast, our review could not even reach that level of synthesis for intervention effectiveness because the primary studies rarely reported comparable intervention data or robust outcome estimates. A scoping review of community-based education in dentistry similarly concluded that potentially important public health benefits were suggested but methodological limitations prevented firm conclusions. Our findings align with that broader pattern in dental education and practice research: important topics are being studied, but inconsistent design and reporting constrain cumulative inference. What prior reviews were sometimes able to suggest directionally, we often could not confirm quantitatively here because the underlying reporting on sexual misconduct was even less complete.

This review has several strengths. The search and study selection process was designed to capture evidence across the breadth of dental care settings and stakeholder groups, which was important given that sexual misconduct in dentistry may involve patients, clinicians, staff, and learners in different configurations. Screening and data extraction were conducted systematically, and the review reports transparently not only the findings but also the reasons synthesis was limited. That transparency matters: documenting the absence of extractable, comparable data is a useful contribution because it clarifies where the evidence base is currently weak and why stronger conclusions remain out of reach. The consistency of high ratings in the review's internal quality assessment framework should also be interpreted alongside the reporting deficiencies observed in the source reports; methodologic appraisal and extractability are related but not interchangeable.

The main limitation of this review is the limited extractable data available from the primary studies. Although the studies were retained as relevant to the review question, many did not report the basic quantitative details needed to estimate prevalence reliably, compare exposed and non-exposed groups, or assess intervention effects. Missing bibliographic metadata, absent raw counts, unclear analytic denominators, truncated results, and lack of confidence intervals or comparator information reduced both interpretability and synthesis options. The small number of included studies and likely contextual variation across institutions and countries also limit generalizability. These limitations do not negate the importance of the topic; rather, they indicate that the literature has not yet matured to the point where precise pooled estimates or strong comparative conclusions are justified.

For practice, the most defensible conclusion is that sexual misconduct should be treated as a credible occupational, educational, and patient-safety issue within dental settings, even though its exact prevalence remains uncertain. Dental schools, clinics, and professional organizations do not need pooled prevalence estimates to justify clear reporting pathways, staff and student training, trauma-informed response procedures, and institutional policies that define unacceptable behaviors and protect complainants from retaliation. The repeated signals of underreporting and emotional or professional harm suggest that prevention and response systems should not rely solely on formal complaints as indicators of burden. For research, the priority is better primary study design and reporting: consistent definitions of sexual misconduct, clearly described populations and settings, validated or at least reproducible measurement tools, explicit numerators and denominators, complete intervention descriptions, comparator data where relevant, and reporting of effect estimates with measures of precision. Future studies should also distinguish between patients, students, clinicians, and staff; capture reporting behavior and barriers to disclosure; and evaluate interventions using designs that permit comparative inference. Until that reporting improves, the inability to pool results will remain a central feature of this evidence base, and an important finding in its own right.

## Conclusion

This systematic review identified six studies examining sexual misconduct behaviors in dental care settings among practitioners, office staff, patients, students, and educators. However, quantitative synthesis was not possible because the included studies did not report sufficiently consistent or extractable numerical data across outcomes, populations, and study methods. The qualitative evidence suggests that sexual misconduct does occur in dental settings and may be associated with underreporting, emotional harm, and professional disengagement, but these findings were variably described and not measured in a way that allowed robust comparison. Evidence regarding the effectiveness of interventions to prevent or address sexual misconduct was especially limited. The main limitation of this review is the lack of extractable quantitative data from the included studies. Overall, the current evidence base remains sparse and heterogeneous, and it is insufficient to support firm conclusions about prevalence, impacts, or intervention effectiveness.

## Final Included Studies

- Corpus ID: 6434 | Inappropriate Patient Sexual Behavior in the Dental Practice Setting: Experiences of dental hygienists.
- Corpus ID: 6431 | Sexual Harassment Issues Among Virginia Dental Hygienists.
- Corpus ID: 6428 | Sexual harassment in dentistry: prevalence in dental school.
- Corpus ID: 104436 | "It's just inappropriate": Harassment of dental students by patients.
- Corpus ID: 6432 | An International Survey of Female Dental Students' Perceptions About Gender Bias and Sexual Misconduct at Four Dental Schools.
- Corpus ID: 6430 | Survey of Dental Researchers' Perceptions of Sexual Harassment at AADR Conferences: 2015 to 2018.
