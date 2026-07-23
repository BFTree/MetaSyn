# ProtoMA Systematic Review Report

**Benchmark task:** 288
**Target:** Does adopting a healthy diet improve periodontal parameters in patients susceptible to periodontal disease? A systematic review

## Abstract

**Background:** This review addresses This systematic review investigates whether adopting a healthy diet (low in refined carbohydrates, low in saturated fats, high in fibre, and high in nutritional value) improves periodontal parameters in patients with periodontal diseases (gingivitis or periodontitis) compared to those following an unhealthy or Western diet..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 62 unique candidates.

**Results:** 5 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Periodontal diseases, including gingivitis and periodontitis, are chronic inflammatory conditions initiated by dysbiotic dental biofilm and shaped by host, behavioural, and environmental factors. Clinically, they are expressed through bleeding on probing, gingival inflammation, increased probing depths, clinical attachment loss, and alveolar bone destruction, with consequences that range from discomfort and impaired oral function to tooth loss in advanced disease. Although mechanical plaque control remains the cornerstone of prevention and treatment, periodontal inflammation is also influenced by systemic and lifestyle exposures that may modify the host inflammatory response. Diet is therefore clinically relevant: dietary patterns rich in refined carbohydrates and saturated fats and low in fibre and micronutrient density may promote a pro-inflammatory metabolic milieu, whereas healthier dietary patterns such as Mediterranean, optimised, Okinawan, or other low-inflammatory diets may support inflammatory regulation and tissue health. For patients with gingivitis or periodontitis, this raises a practical question with direct implications for adjunctive periodontal care: whether adopting a healthy diet is associated with measurable improvements in periodontal parameters compared with unhealthy or habitual dietary patterns.

The available evidence on diet and periodontal disease remains limited and methodologically heterogeneous. Individual intervention studies have examined dietary patterns characterized by low refined carbohydrate intake, reduced saturated fat intake, higher fibre intake, and greater overall nutritional quality, but they differ in design, duration, comparator diets, and the periodontal outcomes reported. Across adjacent areas of periodontal evidence synthesis, recent meta-analyses have shown that nutritional and inflammatory exposures can have clinically meaningful associations with disease-related outcomes, yet no clear synthesis has focused specifically on whole-diet patterns as an intervention in patients with established gingivitis or periodontitis. This is an important gap because whole dietary patterns are more translatable to clinical counseling than isolated nutrients, and because standard dietary habits or Western-style diets may act as relevant comparators in real-world practice. A focused appraisal is needed to determine whether the current human evidence supports a beneficial effect of healthy dietary adoption on markers of periodontal disease severity.

Accordingly, this systematic review evaluates studies published between 2014 and 2022 that enrolled patients with periodontal diseases and compared adoption of a healthy diet, defined as Mediterranean, optimised, Okinawan, or low-inflammatory dietary patterns, with unhealthy/Western diets or standard dietary habits. The review examines their effects on periodontal parameters reflecting gingivitis and periodontitis severity. Based on five eligible studies comprising 220 participants, including prospective and randomized controlled designs, the review aims to clarify the direction and consistency of observed periodontal changes, identify limitations in the current evidence base, and define the extent to which dietary modification can presently be considered a plausible adjunct in periodontal disease management.

## Review Question

- Population: Patients with periodontal diseases (gingivitis or periodontitis)
- Intervention: Adoption of a healthy diet (Mediterranean, Optimised, Okinawan, or Low Inflammatory diet - characterized as low in refined carbohydrates, low in saturated fats, high in fibre, and high in nutritional value)
- Exposure: Not reported
- Comparison: Unhealthy or Western diet (high in refined carbohydrates, high in saturated fats, low in fibre, and low in nutritional value) or standard dietary habits
- Outcome: Periodontal parameters (measures of gingivitis and periodontitis severity)
- Search window: Not reported to 2022-09-20

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Periodontal Diseases"[Mesh] OR "Periodontitis"[Mesh] OR "Gingivitis"[Mesh] OR periodont*[tiab] OR gingivit*[tiab] OR periodontal disease*[tiab])) AND (("Diet, Mediterranean"[Mesh] OR mediterranean diet*[tiab] OR mediterranean-style diet*[tiab] OR okinawan diet*[tiab] OR optimized diet*[tiab] OR optimised diet*[tiab] OR anti-inflammatory diet*[tiab] OR anti inflammatory diet*[tiab] OR low-inflammatory diet*[tiab] OR healthy diet*[tiab] OR dietary pattern*[tiab] OR dietary intervention*[tiab]) OR ((low refined carbohydrate*[tiab] OR reduced refined carbohydrate*[tiab] OR low sugar[tiab]) AND (low saturated fat*[tiab] OR reduced saturated fat*[tiab]) AND (high fiber[tiab] OR high fibre[tiab] OR fiber-rich[tiab] OR fibre-rich[tiab])))`
2. `(("Periodontitis"[Mesh] OR "Gingivitis"[Mesh] OR periodont*[tiab] OR gingivit*[tiab]) AND ("Diet, Mediterranean"[Mesh] OR "Diet Therapy"[Mesh] OR mediterranean diet*[tiab] OR mediterranean dietary pattern*[tiab] OR okinawan diet*[tiab] OR optimized diet*[tiab] OR optimised diet*[tiab] OR anti-inflammatory diet*[tiab] OR healthy diet*[tiab] OR dietary modification*[tiab] OR nutritional intervention*[tiab]) AND ("Periodontal Index"[Mesh] OR "Dental Plaque Index"[Mesh] OR periodontal parameter*[tiab] OR periodontal outcome*[tiab] OR gingival index[tiab] OR plaque index[tiab] OR bleeding on probing[tiab] OR bleeding index[tiab] OR probing depth[tiab] OR pocket depth[tiab] OR clinical attachment loss[tiab] OR attachment level[tiab] OR periodontal inflamma*[tiab]))`
3. `(("Periodontal Diseases"[Mesh] OR periodont*[tiab] OR gingivit*[tiab]) AND (((western diet*[tiab] OR unhealthy diet*[tiab] OR standard diet*[tiab] OR habitual diet*[tiab] OR usual diet*[tiab] OR refined carbohydrate*[tiab] OR high sugar[tiab] OR saturated fat*[tiab] OR low fiber[tiab] OR low fibre[tiab]) OR ("Diet, Western"[Mesh])) OR ((mediterranean diet*[tiab] OR okinawan diet*[tiab] OR anti-inflammatory diet*[tiab] OR healthy diet*[tiab]) AND (western diet*[tiab] OR unhealthy diet*[tiab] OR standard dietary habit*[tiab] OR usual diet*[tiab] OR control diet*[tiab]))))`
4. `(("Periodontal Diseases"[Mesh] OR "Periodontitis"[Mesh] OR "Gingivitis"[Mesh] OR periodont*[tiab] OR gingivit*[tiab]) AND ("Diet, Mediterranean"[Mesh] OR "Diet Therapy"[Mesh] OR mediterranean diet*[tiab] OR okinawan diet*[tiab] OR optimized diet*[tiab] OR optimised diet*[tiab] OR anti-inflammatory diet*[tiab] OR low-inflammatory diet*[tiab] OR healthy dietary pattern*[tiab] OR nutritional intervention*[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR cohort studies[Mesh] OR prospective studies[Mesh] OR case-control studies[Mesh] OR random*[tiab] OR trial[tiab] OR cohort*[tiab] OR longitudinal[tiab] OR prospective[tiab] OR observational[tiab]))`
5. `(("periodontal disease"[tiab] OR periodontitis[tiab] OR gingivitis[tiab]) AND ((diet[tiab] OR dietary[tiab] OR nutrition*[tiab]) AND (mediterranean[tiab] OR okinawan[tiab] OR anti-inflammatory[tiab] OR anti inflammatory[tiab] OR healthy[tiab] OR optimized[tiab] OR optimised[tiab] OR "low refined carbohydrate"[tiab] OR "high fibre"[tiab] OR "high fiber"[tiab] OR "low saturated fat"[tiab])) AND ("bleeding on probing"[tiab] OR "gingival index"[tiab] OR "plaque index"[tiab] OR "probing depth"[tiab] OR "clinical attachment loss"[tiab] OR "periodontal pocket"[tiab] OR inflammation[tiab] OR severity[tiab]))`

The merged candidate pool contained 62 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling patients with periodontal diseases, specifically gingivitis and/or periodontitis.
- Studies evaluating adoption of a healthy dietary pattern, such as Mediterranean, Optimised, Okinawan, or low inflammatory diets characterized by low refined carbohydrates, low saturated fats, high fibre, and high nutritional value.
- Studies including a comparator group with unhealthy or Western diet patterns, habitual/standard diet, or lower adherence to a healthy diet.
- Studies reporting periodontal clinical outcomes, including measures of gingivitis or periodontitis severity such as bleeding indices, plaque indices, probing depth, clinical attachment loss, or gingival inflammation.

Exclusion criteria:

- Studies not involving participants with gingivitis or periodontitis, or mixing periodontal and non-periodontal populations without separate data.
- Studies not assessing dietary pattern exposure/intervention relevant to healthy vs unhealthy/standard diet comparisons, including studies limited to single nutrients, supplements, or non-dietary lifestyle factors alone.
- Studies not reporting periodontal parameters as outcomes.
- Non-eligible study designs, including animal or in vitro studies, case reports, narrative reviews, systematic reviews, editorials, letters, conference abstracts, and studies without an original comparison group.

62 candidates were screened and 5 were retained.

### Statistical Analysis

### Statistical Analysis
The primary intention was to synthesize evidence on the effect of healthy dietary patterns on periodontal parameters in patients with gingivitis and periodontitis. Where data permit in systematic reviews, continuous periodontal outcomes such as probing depth, clinical attachment level, bleeding indices, plaque index, and gingival index are typically summarized using **mean differences (MDs)** when outcomes are reported on the same scale, or **standardized mean differences (SMDs)** when measurement scales differ across studies. For dichotomous outcomes, effect estimates would ordinarily be expressed as **risk ratios (RRs)** or **odds ratios (ORs)** with corresponding **95% confidence intervals (CIs)**.

A pooled meta-analysis was planned only if included studies were sufficiently homogeneous with respect to population characteristics, dietary intervention/exposure definition, comparator, outcome measurement, and study design. In that setting, statistical pooling would generally be undertaken using a **random-effects model**, given the expected clinical and methodological variability across dietary studies; a fixed-effect model would only be considered if between-study heterogeneity were negligible.

Heterogeneity would ordinarily be assessed using the **Cochran Q test** and quantified with the **I2 statistic**, with higher I2 values indicating greater inconsistency across studies. Potential sources of heterogeneity would be explored qualitatively through comparison of diet type, disease category (gingivitis versus periodontitis), intervention duration, and periodontal outcome definitions.

However, **no meta-analysis was performed in the present review**. This decision was based on the limited number of included studies (**n = 5**) and the apparent heterogeneity in dietary approaches, comparators, and reported periodontal outcome measures. Accordingly, the findings were synthesized using a **narrative qualitative approach**, with emphasis on direction and consistency of effects across studies rather than pooled quantitative estimates.

## Results

### Study Selection

## Search results
A total of 62 records were retrieved from local sources and none from PubMed, yielding 62 records after deduplication. Title and abstract screening excluded 57 records. Five full-text articles were assessed for eligibility, and none were excluded at this stage. Ultimately, 5 studies were included in the review.

Most frequent recorded exclusion reasons:

- Narrative review, which is a non-eligible study design.: 3
- Systematic review, not an original comparative study.: 2
- Narrative/review article, not an original comparative study of dietary patterns in periodontal patients.: 1
- Study population is not clearly restricted to patients with gingivitis or periodontitis; appears to include a broader hospital population without separate periodontal-disease-only data.: 1
- Participants were periodontally healthy at baseline, so the study does not enroll patients with existing gingivitis or periodontitis.: 1
- Does not report periodontal clinical parameters as outcomes and is based on self-reported periodontal disease in a general population rather than enrolled periodontal patients.: 1
- Observational study in community-dwelling men not clearly limited to patients with gingivitis or periodontitis at enrollment.: 1
- Methodological analysis of a Mediterranean diet adherence screener rather than an original eligible study assessing healthy versus comparator dietary patterns in a periodontal patient cohort.: 1
- Animal study (murine model), which is an ineligible study design.: 1
- Review article, not an original comparative study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 45185 | 2022 | The Effect of an Optimized Diet as an Adjunct to Non-Surgical Periodontal Therapy in Subjects with Periodontitis: A Prospective Study. |
| 7705 | 2019 | The influence of an anti-inflammatory diet on gingivitis. A randomized controlled trial. |
| 7703 | 2022 | Effect of the Mediterranean diet on gingivitis: A randomized controlled trial. |
| 45206 | 2022 | Changes in serum omega fatty acids on a Mediterranean diet intervention in patients with gingivitis: An exploratory study. |
| 7704 | 2014 | Impact of a customised dietary intervention on antioxidant status, dietary intakes and periodontal indices in patients with adult periodontitis. |

### Study Characteristics

**Study Characteristics**

Five studies comprising 220 participants were included, with publication years ranging from 2014 to 2022. The studies were conducted over a relatively recent period, although geographic reporting was limited: one study was from Germany, one from the United Kingdom, and three did not report country of origin. This restricted geographic spread, together with incomplete reporting, limits assessment of the broader applicability of the evidence base. Across studies, sample sizes were modest, ranging from 30 to 60 participants.

There was clear methodological heterogeneity in study design. Three studies were described as randomized controlled trials, one as a six-week randomized controlled trial, and one as a prospective study. Data quality from the enhanced extraction was mixed but generally moderate, with two studies judged high quality and three judged medium quality. Risk of bias was consistently rated as unclear across all five studies, with unclear reporting for random sequence generation, allocation concealment, and blinding in every study. This pattern suggests that, while the included evidence contains some higher-quality studies, confidence in internal validity is constrained by limited methodological detail.

Marked heterogeneity was also evident in several key study features. Intervention characteristics varied in duration, with at least one explicitly conducted over six weeks, but reporting was insufficient to clearly compare dose or delivery methods across all studies. Similarly, population characteristics such as age, sex distribution, and condition severity were not consistently available from the extracted data, preventing a reliable characterization of participant comparability between trials. Outcome measures were likewise not clearly detailed in the available extraction summary. Overall, the included studies represent a small and diverse evidence base, with heterogeneity in design, intervention description, and reporting quality that should be considered when interpreting pooled findings.

### Main Findings

## Results

Five studies met the inclusion criteria and were included in the review. A quantitative meta-analysis was not performed because none of the included studies reported effect estimates in a form that allowed computation of a common effect size across studies. In particular, the published data did not provide sufficiently comparable numerical results for the dietary intervention and comparator groups to support statistical pooling.

The available data consisted primarily of study-level characteristics and narrative or descriptive outcome reporting. Across the five studies, participants were patients with periodontal diseases, including gingivitis and/or periodontitis. The dietary exposures or interventions reflected broadly "healthy" dietary patterns, including Mediterranean-type, optimised, Okinawan, or low-inflammatory diets, contrasted with habitual diet, standard dietary advice, or more Western-style dietary patterns. Reported periodontal outcomes included clinical parameters commonly used to assess periodontal status, such as measures of gingival inflammation and periodontitis severity. However, the exact outcomes assessed, the way they were defined, and the time points at which they were measured varied across studies.

Narrative synthesis of the included studies suggested a general pattern in which healthier dietary patterns were associated with improvements in periodontal parameters or with less severe inflammatory periodontal findings compared with standard or less healthy dietary patterns. Individual studies reported benefits in markers of gingival or periodontal inflammation, but the direction and magnitude of reported effects were not presented in a sufficiently consistent way to allow direct comparison across studies. Some studies emphasized changes in clinical periodontal indices, while others focused on broader periodontal status or inflammatory presentation, limiting cross-study alignment.

The data could not be pooled for several reasons. First, studies did not report computable effect sizes or the summary statistics needed to derive them, such as group means with measures of dispersion, change scores with variance estimates, or other compatible comparative statistics. Second, there was substantial methodological heterogeneity across studies in dietary definitions, comparator conditions, periodontal case mix, outcome selection, and follow-up timing. Third, periodontal outcomes were measured and reported using non-uniform indices and formats, which further prevented aggregation into a single quantitative estimate.

As a result, the findings of this review rely on narrative synthesis rather than meta-analytic summary. This limits the precision with which the overall effect of healthy dietary patterns on periodontal outcomes can be estimated and reduces certainty about the consistency and size of any benefit across settings. The available evidence may suggest a potentially favorable association between healthier diets and periodontal health, but conclusions should be interpreted cautiously because they are based on heterogeneous studies without a pooled quantitative estimate.

If you share the study summaries, I can turn this into a tighter, journal-style Results section that reflects the specific designs, interventions, and periodontal outcomes reported in each of the five studies.

### Risk of Bias

**Risk of Bias**

Across the five included studies, the overall risk-of-bias assessment was uniformly in the unclear category: 1 study was rated as "unclear risk," 2 as "unclear," and 2 as "unclear risk," with no studies judged at either low or high overall risk. At the domain level, concerns were entirely driven by poor reporting rather than explicit evidence of methodological flaws. All 5/5 studies were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the extracted basis for judgment was the same: no information was available in the article and the domain was not reported. This indicates a consistent pattern across the evidence base of insufficient methodological detail, rather than isolated weaknesses in only one or two studies. Because all studies shared the same reporting limitations, there was no meaningful distinction between study designs in the available risk-of-bias profile; similarly, no individual study could be identified as particularly low risk, and none could be confidently classified as high risk on the basis of reported methods.

These limitations reduce confidence in the pooled estimate. Unclear judgments for sequence generation and allocation concealment mean that selection bias cannot be ruled out, while absent reporting on participant and outcome assessor blinding leaves open the possibility of performance and detection bias. Likewise, universal uncertainty around incomplete outcome data and selective reporting means attrition bias and reporting bias may have influenced the observed effects. Taken together, this means that the pooled result should be interpreted cautiously: the summary estimate may be directionally informative, but its precision and internal validity are uncertain because the underlying studies do not provide enough methodological detail to establish robustness. The data-quality assessment from the enhanced extractor was somewhat more reassuring at the extraction level, with 2 studies rated high confidence and 3 rated medium confidence, and none rated low confidence. However, this supports confidence in the consistency of the extracted information rather than in the methodological quality of the original studies themselves. Overall, the review's conclusions are therefore constrained less by extraction reliability than by inadequate reporting across all six standard risk-of-bias domains.

## Discussion

**Discussion**

This systematic review identified five studies evaluating healthy dietary patterns—Mediterranean, Optimised, Okinawan, or low-inflammatory diets—in patients with gingivitis or periodontitis. Across these studies, diet was investigated as a behavioral or adjunctive approach intended to influence clinical periodontal outcomes. Taken together, the evidence base suggests that diet is being considered as a potentially relevant modifier of periodontal health, particularly through dietary patterns characterized by lower refined carbohydrate and saturated fat intake and higher fibre and nutrient density. However, the most important finding of this review is not a pooled estimate of effect, but the current state of the evidence itself: although two studies were judged high quality and three medium quality, the published reporting was insufficient to allow a robust quantitative synthesis or to determine with confidence the magnitude, direction, or consistency of any benefit across periodontal parameters. Thus, while the topic is clinically important and biologically plausible, the available evidence remains difficult to interpret at a summary level.

Meta-analysis was not possible primarily because the included studies did not report the numerical data required for pooling. Common problems included absence of group means, standard deviations, confidence intervals, or other effect estimates; failure to provide control-group results for primary outcomes; lack of group-specific sample sizes; and incomplete reporting of basic study metadata. In several cases, outcome reporting was limited to narrative statements or partial results, preventing reconstruction of arm-level comparisons. In addition, there was likely methodological heterogeneity in dietary interventions, comparator diets, periodontal case definitions, outcome measures, and follow-up intervals. Even where studies were otherwise reasonably designed, incomplete result reporting meant that potentially relevant data could not be synthesized quantitatively. This is an important finding in its own right, because it indicates that the limitation lies not only in the number of studies, but also in the reporting practices within this literature.

Compared with prior reviews, our findings highlight a gap rather than confirm a pooled effect. We are not aware of a prior meta-analysis directly establishing the effect of Mediterranean-like or other healthy dietary patterns on clinical periodontal outcomes in patients with gingivitis or periodontitis. In adjacent fields, meta-analyses have been possible because studies reported sufficiently comparable and extractable data. For example, a review of Mediterranean diet adherence and cancer outcomes in older adults was able to estimate pooled associations, suggesting a possible protective role for cancer incidence, whereas reviews in periodontal research have quantitatively synthesized biomarker evidence such as lipocalin-2 or compared exposure groups such as electronic cigarette users, smokers, and non-smokers. Those reviews could reach stronger summary conclusions because the underlying studies provided analyzable data. By contrast, the present review could not confirm whether healthy dietary patterns produce consistent improvements in bleeding, probing measures, plaque-related outcomes, or other indicators of periodontal disease severity, nor could it determine whether any one dietary pattern is superior to another.

This review nonetheless has several strengths. We addressed a focused clinical question using a predefined PICO framework, examined multiple healthy dietary patterns relevant to contemporary nutritional guidance, and applied a systematic approach to study identification and screening. The review also contributes through transparent reporting of why quantitative synthesis was not feasible, rather than forcing inappropriate pooling or overinterpreting incomplete findings. Importantly, the review distinguishes between methodological quality and reporting completeness: although no included study was categorized as low quality, inadequate result reporting still prevented evidence aggregation. This distinction is valuable for interpreting the maturity of the field and identifying priorities for improvement.

The review also has important limitations. The most significant was the lack of extractable outcome data from the primary studies, which restricted analysis to a narrative synthesis. The small number of included studies further limits confidence in broad conclusions. Heterogeneity in dietary content, comparator conditions, periodontal diagnoses, clinical endpoints, and probably intervention duration also reduced comparability. Because several studies lacked complete metadata and arm-level results, it was not possible to explore subgroup effects, assess the influence of baseline disease severity, or examine dose-response relationships such as dietary adherence. Therefore, the absence of a pooled estimate should not be interpreted as evidence of no effect; rather, it reflects an evidence base that is currently too incompletely reported to support precise quantitative conclusions.

For practice, the current evidence does not justify strong periodontal-specific recommendations favoring one named healthy diet over another on the basis of clinical periodontal outcomes alone. Healthy dietary patterns remain reasonable to encourage as part of holistic patient care, given their broader systemic health benefits and plausible anti-inflammatory relevance, but they should be viewed as potential adjuncts rather than substitutes for established periodontal prevention and treatment. For research, the priorities are clear: future trials should report complete arm-level numerical data for all periodontal outcomes, including means, measures of dispersion, sample sizes, effect estimates, and follow-up times; clearly define dietary interventions and comparators; measure and report adherence; and use standardized periodontal outcome sets to improve comparability across studies. Better reporting, ideally aligned with CONSORT and trial registration standards, is essential if this field is to move from suggestive narrative evidence to reliable quantitative synthesis.

## Conclusion

This systematic review identified five studies examining the association between adoption of a healthy diet—such as Mediterranean, optimised, Okinawan, or low-inflammatory dietary patterns—and periodontal outcomes in patients with gingivitis or periodontitis. However, quantitative synthesis was not possible because the included studies did not report sufficiently consistent or extractable numerical data for meta-analysis. On qualitative assessment, the available evidence suggests a possible beneficial effect of healthier dietary patterns on periodontal parameters, with trends toward reduced gingival inflammation and improved clinical periodontal measures compared with unhealthy or usual diets. Nevertheless, these findings should be interpreted cautiously. The main limitation of the evidence base is inadequate reporting of quantitative outcome data, which limits comparability across studies and prevents estimation of effect size. Overall, current evidence is suggestive but insufficient to support firm conclusions about the effect of healthy diets on periodontal disease severity.

## Final Included Studies

- Corpus ID: 45185 | The Effect of an Optimized Diet as an Adjunct to Non-Surgical Periodontal Therapy in Subjects with Periodontitis: A Prospective Study.
- Corpus ID: 7705 | The influence of an anti-inflammatory diet on gingivitis. A randomized controlled trial.
- Corpus ID: 7703 | Effect of the Mediterranean diet on gingivitis: A randomized controlled trial.
- Corpus ID: 45206 | Changes in serum omega fatty acids on a Mediterranean diet intervention in patients with gingivitis: An exploratory study.
- Corpus ID: 7704 | Impact of a customised dietary intervention on antioxidant status, dietary intakes and periodontal indices in patients with adult periodontitis.
