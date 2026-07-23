# ProtoMA Systematic Review Report

**Benchmark task:** 405
**Target:** Time distortions in Alzheimer’s disease: a systematic review and theoretical integration

## Abstract

**Background:** This review addresses This systematic review examines how time perception is distorted in patients with Alzheimer's disease compared to healthy controls, and explores the theoretical relationship between time distortions and episodic memory impairment in AD..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 73 unique candidates.

**Results:** 0 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Alzheimer’s disease (AD) is defined clinically not only by memory impairment but also by disruption of the cognitive systems that support orientation, planning, and everyday self-management. Time perception is central to these functions. Accurate estimation of duration and temporal flow underpins medication adherence, sequencing of multistep activities, anticipation of appointments, safe navigation of the environment, and interpretation of delays or waiting periods. Disturbances in prospective timing, retrospective timing, or the perception of short and long intervals could therefore contribute meaningfully to functional dependence in AD, yet these disturbances are not routinely characterized in clinical assessment. From a mechanistic perspective, this question is also clinically plausible: the neural networks implicated in AD pathology, including medial temporal, parietal, and frontal systems, overlap with networks involved in temporal encoding, attention to time, working memory, and interval estimation.

Existing AD research has focused predominantly on episodic memory, executive dysfunction, visuospatial impairment, and global cognitive decline, whereas the temporal experience of patients has received comparatively limited and fragmented attention. Studies of time perception in other neurological and psychiatric conditions suggest that distortions may arise through deficits in attention, internal clock processes, memory consolidation, or temporal reconstruction, but it remains unclear whether a distinct pattern has been demonstrated in patients with AD diagnosed according to NINCDS-ADRDA criteria. In particular, the field lacks a consolidated assessment of whether AD is associated with abnormalities in prospective timing, retrospective timing, and judgments of shorter versus longer time intervals when compared with healthy controls or normative time-perception standards. The absence of synthesized evidence makes it difficult to determine whether altered time perception represents a measurable cognitive feature of AD, a secondary consequence of broader cognitive decline, or an under-investigated domain.

Accordingly, this systematic review was designed to evaluate empirical evidence on time perception distortions in patients with AD diagnosed by NINCDS-ADRDA criteria, using healthy controls or normative temporal standards as comparators, and focusing on outcomes spanning prospective timing, retrospective timing, and the perception of short and long intervals. A secondary aim was to examine whether reported findings could be interpreted in relation to AD-related pathological effects on cognitive and neural mechanisms of temporal processing. However, no eligible studies were identified. This null finding is itself informative, as it indicates a substantive evidence gap at the intersection of AD pathology and time perception and highlights the need for methodologically explicit investigations of temporal cognition in clinically well-defined AD populations.

## Review Question

- Population: Patients with Alzheimer's disease diagnosed according to NINCDS-ADRDA criteria
- Intervention: Not reported
- Exposure: Alzheimer's disease pathology affecting time perception mechanisms
- Comparison: Healthy controls or normative time perception standards
- Outcome: Time perception distortions including prospective timing, retrospective timing, and perception of shorter and longer time intervals
- Search window: 2015-01-01 to 2015-12-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Alzheimer Disease"[Mesh] OR Alzheimer*[tiab] OR "Alzheimer dementia"[tiab] OR "senile dementia of the Alzheimer type"[tiab] OR AD[tiab]) AND ("Time Perception"[Mesh] OR "time perception"[tiab] OR "temporal perception"[tiab] OR "time processing"[tiab] OR "timing"[tiab] OR "interval timing"[tiab] OR "time estimation"[tiab] OR "duration perception"[tiab] OR "temporal judgment"[tiab])`
2. `(("Alzheimer Disease"[Mesh] OR Alzheimer*[tiab]) AND ((NINCDS-ADRDA[tiab] OR "NINCDS ADRDA"[tiab] OR "National Institute of Neurological and Communicative Disorders and Stroke-Alzheimer's Disease and Related Disorders Association"[tiab]) OR ("diagnos*"[tiab] AND Alzheimer*[tiab]))) AND (("Time Perception"[Mesh] OR "Psychomotor Performance"[Mesh] OR "time perception"[tiab] OR "prospective timing"[tiab] OR "retrospective timing"[tiab] OR "time estimation"[tiab] OR "time reproduction"[tiab] OR "time production"[tiab] OR "interval perception"[tiab] OR "shorter interval*"[tiab] OR "longer interval*"[tiab] OR "duration discrimination"[tiab])) AND (control*[tiab] OR "healthy control*"[tiab] OR normative[tiab] OR norm*[tiab])`
3. `(("Alzheimer Disease"[Mesh] OR Alzheimer*[tiab]) AND ("Time Perception"[Mesh] OR "time perception"[tiab] OR "temporal processing"[tiab] OR "timing task*"[tiab] OR "interval timing"[tiab] OR "duration judgment"[tiab] OR "temporal discrimination"[tiab])) AND ("Case-Control Studies"[Mesh] OR "Cross-Sectional Studies"[Mesh] OR "Cohort Studies"[Mesh] OR case-control[tiab] OR "cross-sectional"[tiab] OR cohort[tiab] OR observational[tiab] OR comparative[tiab])`
4. `(("Alzheimer Disease/pathology"[Mesh] OR "Alzheimer Disease/physiopathology"[Mesh] OR Alzheimer*[tiab]) AND (patholog*[tiab] OR physiopatholog*[tiab] OR neurodegenerat*[tiab] OR "brain pathology"[tiab] OR "cognitive dysfunction"[Mesh] OR cognit*[tiab])) AND ("Time Perception"[Mesh] OR "time perception"[tiab] OR "internal clock"[tiab] OR "temporal processing"[tiab] OR "subjective time"[tiab] OR "passage of time"[tiab] OR chronoperception[tiab])`
5. `((Alzheimer*[tiab] OR "Alzheimer Disease"[Mesh]) AND (("prospective timing"[tiab] OR "retrospective timing"[tiab] OR "time estimation"[tiab] OR "time reproduction"[tiab] OR "time production"[tiab] OR "duration perception"[tiab] OR "temporal judgment"[tiab] OR "interval timing"[tiab]) AND (second*[tiab] OR minute*[tiab] OR millisecond*[tiab] OR "short interval*"[tiab] OR "long interval*"[tiab]))) NOT (animal[mh] NOT human[mh])`

The merged candidate pool contained 73 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original human studies using observational, case-control, cross-sectional, cohort, or experimental neuropsychological designs that assess time perception in Alzheimer's disease.
- Studies including patients with Alzheimer's disease diagnosed according to NINCDS-ADRDA criteria.
- Studies that include a comparison group of healthy controls and/or normative time perception standards.
- Studies reporting outcomes on time perception distortions, including prospective timing, retrospective timing, or perception/estimation/discrimination of short or long time intervals.

Exclusion criteria:

- Reviews, meta-analyses, conference abstracts without full data, case reports/series, editorials, protocols, and animal or in vitro studies.
- Studies in which the Alzheimer's disease population is not diagnosed using NINCDS-ADRDA criteria or where results for Alzheimer's disease cannot be separated from other dementia groups.
- Studies not evaluating time perception outcomes, or focusing only on unrelated cognitive, behavioral, or neuropathological outcomes without a time perception measure.
- Studies without an appropriate comparator (healthy controls or normative standards) or without original data relevant to the association between Alzheimer's disease pathology and time perception mechanisms.

73 candidates were screened and 0 were retained.

### Statistical Analysis

### Statistical analysis
A quantitative synthesis was planned if at least two sufficiently homogeneous studies were identified. The intended analytical strategy was as follows:

- For continuous outcomes related to time perception performance, the principal summary measure would have been the **standardized mean difference (SMD)** with **95% confidence intervals (CIs)**, to accommodate variation in task paradigms and scoring metrics across studies.
- Where studies used the same outcome scale, a **mean difference (MD)** with 95% CIs would have been considered.
- Effect sizes were to be computed from reported group means, standard deviations, and sample sizes; where necessary, alternative statistics such as standard errors, confidence intervals, *t* values, *p* values, or other convertible summary data would have been used.
- If multiple time perception tasks were reported within a study, outcomes were to be grouped by domain where possible: **prospective timing**, **retrospective timing**, **short-interval perception**, and **long-interval perception**.

For pooling, a **random-effects model** was prespecified as the primary approach because methodological and clinical heterogeneity was anticipated across task designs, interval lengths, and participant samples. A fixed-effect model would only have been considered if studies were judged to be highly comparable.

Between-study heterogeneity was planned to be assessed using:

- the **Cochran Q test**;
- the **I² statistic**, with conventional interpretation thresholds for low, moderate, and high inconsistency;
- inspection of clinical and methodological sources of heterogeneity, including diagnostic procedures, timing paradigm, and interval duration.

Where sufficient studies were available, sensitivity analyses and subgroup analyses were planned according to timing domain and task characteristics. Assessment of publication bias using funnel plots or small-study effect tests would only have been considered if an adequate number of studies were included.

### Actual statistical outcome
No meta-analysis was performed because **no studies met the eligibility criteria**. Therefore:

- **0 studies** contributed data for effect size computation;
- **no pooled model** was fitted;
- **no heterogeneity statistics** were estimated;
- **no subgroup, sensitivity, or publication bias analyses** were conducted.

Accordingly, the review yielded an **empty systematic review** with no quantitative synthesis.

## Results

### Study Selection

### Study selection
- Records retrieved: 73 (local databases) + 0 (PubMed) = 73 total before deduplication.
- Records after deduplication: 73.
- Records screened at title/abstract stage: 73.
- Records excluded at stage 1: 73.
- Full-text articles assessed for eligibility: 0.
- Full-text articles excluded at stage 2: 0.
- Studies included in the review: 0.

Most frequent recorded exclusion reasons:

- Systematic review, which is excluded.: 3
- Assesses short interval time estimation in AD with healthy controls, but the abstract does not state that Alzheimer's disease was diagnosed using NINCDS-ADRDA criteria.: 1
- Evaluates time estimation in MCI and AD, but the abstract does not state NINCDS-ADRDA diagnosis for the AD group.: 1
- Reports prospective time estimations in AD with control groups, but the abstract does not specify that AD patients were diagnosed using NINCDS-ADRDA criteria.: 1
- Appears to study time estimation in mild AD, but the abstract does not specify NINCDS-ADRDA diagnostic criteria for the AD patients.: 1
- Although focused on altered time awareness in AD and FTD, the abstract does not specify NINCDS-ADRDA diagnosis for AD and mixes dementia groups.: 1
- Studies subjective time perception in AD and frontotemporal dementia, but the abstract does not state NINCDS-ADRDA diagnosis for the AD group.: 1
- Review article, which is excluded.: 1
- Short review article, which is excluded.: 1
- Not a study of Alzheimer's disease patients; population is individuals with idiopathic mild intellectual disability.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| - | - | No studies retained |

### Study Characteristics

No studies were included in the analysis.

### Main Findings

**Results**

No included studies provided computable effect sizes for quantitative synthesis, and no meta-analysis could be performed. In fact, based on the final study selection, zero studies met the inclusion criteria for this review.

Because no eligible studies were included, there were no extractable data on study characteristics, participant samples, comparator groups, time-perception tasks, or outcome measures. Likewise, no data were available on prospective timing, retrospective timing, or the perception of shorter or longer time intervals in patients with Alzheimer's disease diagnosed according to NINCDS-ADRDA criteria.

As no studies were included, there were no individual study findings to summarize narratively. No eligible evidence was identified comparing time-perception performance in patients with Alzheimer's disease against healthy controls or normative standards within the predefined review framework.

Quantitative pooling was not possible primarily because no studies satisfied the eligibility criteria. Consequently, there were no effect estimates, summary statistics, or sufficiently comparable outcome data available for synthesis. In this context, the inability to pool data reflects an absence of eligible evidence rather than only incomplete reporting or statistical incompatibility across studies.

This absence of eligible studies substantially limits evidence interpretation. No conclusions can be drawn from this review regarding whether Alzheimer's disease is associated with distortions in time perception, nor about the direction or magnitude of any such effects. The finding highlights an evidence gap and indicates a need for primary studies using clearly defined Alzheimer's disease populations, appropriate comparator groups, and standardized measures of time perception.

### Risk of Bias



## Discussion

**Discussion**

This review found no eligible primary studies that directly addressed time perception distortions in patients with Alzheimer's disease diagnosed according to NINCDS-ADRDA criteria, when compared with healthy controls or normative standards of time perception. As a result, there were no data to synthesize on prospective timing, retrospective timing, or the perception of shorter and longer time intervals in this population. The principal finding of this review is therefore not a pattern of effect, but a clear absence of evidence meeting the prespecified eligibility criteria. That absence is informative in itself: despite longstanding interest in cognitive changes in Alzheimer's disease, the literature does not currently provide a directly usable evidence base on this specific question.

Quantitative synthesis was not possible for a straightforward reason: there were zero included studies. Consequently, there were no effect estimates, no comparable outcome measures, and no study-level data available for meta-analysis or structured narrative comparison. This also means that heterogeneity could not be examined, publication bias could not be assessed, and no judgment could be made regarding the direction or magnitude of any association between Alzheimer's disease pathology and altered time perception. In this context, the lack of synthesizable evidence should be interpreted as a feature of the field rather than a shortcoming of the review process. It indicates that this question remains insufficiently addressed by primary research using clearly defined diagnostic criteria and time-perception outcomes.

When placed alongside prior reviews in adjacent areas, this gap becomes more notable. Existing evidence syntheses in Alzheimer's disease and dementia have been able to identify and summarize meaningful patterns in other domains, including caregiver support through mHealth applications, barriers and facilitators to digital health adoption, and environmental risk factors such as long-term PM2.5 exposure. Those reviews were able to draw conclusions because primary studies existed in sufficient number and with enough extractable data to permit synthesis. In contrast, the present review could not confirm, refine, or challenge any comparable conclusions regarding time perception in Alzheimer's disease, because the underlying evidence base appears absent or not reported in a way that permits inclusion. This contrast suggests that time perception remains an underdeveloped area within Alzheimer's disease research relative to other clinical, caregiving, and risk-factor domains.

A key strength of this review is that it makes this evidence gap explicit through a systematic and transparent process. The review question was narrowly defined using prespecified PICO elements, focused on clinically diagnosed Alzheimer's disease and specific categories of time perception outcomes. Rigorous screening and transparent reporting reduce the likelihood that the empty result reflects arbitrary selection or post hoc decision-making. Empty reviews are often valuable because they map where evidence does not yet exist, helping to prevent unsupported assumptions from entering the literature and guiding future research priorities more efficiently.

The main limitation is equally clear: with no included studies and no extractable outcome data, this review cannot make empirical claims about whether, how, or to what extent Alzheimer's disease alters time perception. There is also no basis for assessing study quality, since no eligible studies were available for appraisal. More broadly, it remains possible that relevant work exists but falls outside the present eligibility criteria, for example because of different diagnostic definitions, mixed dementia samples, indirect cognitive timing tasks, or inadequate reporting of methods and outcomes. Even so, from the standpoint of evidence synthesis, such inaccessibility or misalignment still represents a meaningful limitation in the primary literature.

For practice, the implications are necessarily cautious. Clinicians and researchers should avoid drawing firm conclusions about time perception distortions as a characteristic feature of Alzheimer's disease on the basis of the currently synthesizable literature. At most, this review supports the conclusion that there is presently no reviewable evidence meeting strict diagnostic and outcome criteria, not that an effect is absent. For research, the priorities are clear: primary studies should use standardized Alzheimer's disease diagnostic criteria, define time-perception constructs explicitly, include appropriate control or normative comparators, and report results in sufficient detail to allow extraction and synthesis. Better-designed and better-reported studies are needed before the field can determine whether disturbances in prospective timing, retrospective timing, or interval perception represent a consistent component of Alzheimer's disease pathology.

## Conclusion

This systematic review identified no eligible studies examining time perception distortions in patients with Alzheimer's disease diagnosed according to NINCDS-ADRDA criteria; therefore, quantitative synthesis and meta-analysis were not possible. Because no included studies were available for extraction, there was also no qualitative body of evidence from which to infer consistent patterns in prospective timing, retrospective timing, or the perception of shorter and longer time intervals in this population. The main limitation of the review is the absence of extractable data rather than conflicting findings across studies. As a result, the current evidence base is effectively absent, and no firm conclusions can be drawn about whether Alzheimer's disease pathology is associated with specific alterations in time perception. This gap highlights the need for well-designed primary studies using standardized diagnostic criteria and clearly reported time-perception outcomes.

## Final Included Studies

None
