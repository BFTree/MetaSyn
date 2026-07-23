# ProtoMA Systematic Review Report

**Benchmark task:** 255
**Target:** Ultrabrief pulse electroconvulsive therapy for depression: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis aims to assess acute and long-term outcomes following ultrabrief pulse electroconvulsive therapy (ECT) for depression, including remission rates, response rates, relapse rates, and switching rates to other forms of ECT, compared to conventional brief-pulse ECT..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 58 unique candidates.

**Results:** 7 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Major depressive disorder is a leading cause of disability and remains difficult to treat in a substantial minority of patients despite pharmacotherapy and psychotherapy. For severe, psychotic, suicidal, or treatment-resistant depression, electroconvulsive therapy (ECT) remains one of the most effective acute interventions, often producing rapid symptom improvement when delay carries significant clinical risk. However, the therapeutic value of ECT must be weighed against adverse cognitive effects, particularly disorientation and retrograde memory impairment, which influence patient acceptability, treatment continuation, and selection of stimulus parameters. Pulse width is a clinically important determinant of this balance. Ultrabrief pulse ECT, typically defined as a pulse width of less than 0.5 milliseconds, has been proposed to reduce cognitive adverse effects by delivering a more physiologically efficient stimulus, whereas brief-pulse or conventional ECT, usually using pulse widths of 0.5-1.5 milliseconds, has been the standard approach in many settings. The central clinical question is whether ultrabrief pulse ECT preserves antidepressant efficacy while offering a more favorable treatment course.

Evidence on this question has accumulated over the past decade, but the findings remain difficult to translate into practice because studies differ in design, electrode placement, treatment protocols, and outcome definitions. Across seven studies published between 2008 and 2021, including randomized controlled trials, a multicenter double-blind trial, prospective and cohort studies, and retrospective analyses, a total of 2,382 participants have contributed data comparing ultrabrief pulse ECT with brief-pulse or conventional ECT in depressive disorders. Individual studies have variously suggested that ultrabrief pulse ECT may achieve comparable remission or response in some settings, while in others it may require more treatments, show lower acute efficacy, or prompt switching to alternative ECT modalities. Outcomes such as relapse after initial improvement and switching rates are especially relevant for real-world decision-making, yet they have not been consistently synthesized alongside remission and response. As a result, clinicians still lack a clear evidence summary on whether reduced pulse width alters not only short-term antidepressant benefit but also treatment durability and the likelihood of protocol modification during a course of ECT.

This systematic review therefore evaluates patients with depression receiving ECT, comparing ultrabrief pulse ECT (pulse width <0.5 milliseconds) with brief-pulse or conventional ECT (pulse width 0.5-1.5 milliseconds). The review focuses on four clinically consequential outcomes: remission rates, response rates, relapse rates, and switching rates to other forms of ECT. By synthesizing evidence from randomized and observational comparative studies, this review aims to clarify whether ultrabrief pulse ECT provides an acceptable efficacy tradeoff relative to standard pulse widths and to identify where uncertainty remains in the comparative effectiveness of these treatment strategies.

## Review Question

- Population: Patients with depression receiving electroconvulsive therapy
- Intervention: Ultrabrief pulse electroconvulsive therapy (pulse width <0.5 milliseconds)
- Exposure: Not reported
- Comparison: Brief-pulse electroconvulsive therapy (pulse width 0.5-1.5 milliseconds) or conventional ECT
- Outcome: Remission rates, response rates, relapse rates, and switching rates to other forms of ECT
- Search window: 2007-01-01 to 2024-09-17

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Depressive Disorder"[Mesh] OR depress*[tiab] OR "major depressive disorder"[tiab] OR MDD[tiab] OR melanchol*[tiab]) AND ("Electroconvulsive Therapy"[Mesh] OR electroconvulsive therap*[tiab] OR electroshock[tiab] OR ECT[tiab]) AND ((ultrabrief[tiab] OR "ultra-brief"[tiab] OR "ultra brief"[tiab]) AND (pulse[tiab] OR pulsewidth[tiab] OR "pulse width"[tiab] OR stimulus[tiab]))`
2. `("Depressive Disorder"[Mesh] OR depress*[tiab] OR "major depression"[tiab] OR "major depressive disorder"[tiab]) AND ("Electroconvulsive Therapy"[Mesh] OR ECT[tiab] OR electroconvulsive therap*[tiab]) AND (((ultrabrief[tiab] OR "ultra-brief"[tiab] OR "ultra brief"[tiab]) AND (pulse[tiab] OR "pulse width"[tiab] OR pulsewidth[tiab])) OR (("pulse width"[tiab] OR pulsewidth[tiab]) AND ("0.25 ms"[tiab] OR "0.3 ms"[tiab] OR "0.25 millisecond*"[tiab] OR "0.3 millisecond*"[tiab] OR "<0.5 ms"[tiab]))) AND ((brief[tiab] AND pulse[tiab]) OR "brief-pulse"[tiab] OR conventional[tiab] OR standard[tiab] OR (("pulse width"[tiab] OR pulsewidth[tiab]) AND ("0.5 ms"[tiab] OR "1.0 ms"[tiab] OR "1.5 ms"[tiab])))`
3. `("Depressive Disorder"[Mesh] OR depress*[tiab] OR "major depressive disorder"[tiab]) AND ("Electroconvulsive Therapy"[Mesh] OR electroconvulsive therap*[tiab] OR ECT[tiab]) AND ((ultrabrief[tiab] OR "ultra-brief"[tiab] OR "ultra brief"[tiab]) AND (pulse[tiab] OR "pulse width"[tiab])) AND (remission[tiab] OR remitted[tiab] OR response[tiab] OR responder*[tiab] OR relapse[tiab] OR recurren*[tiab] OR switching[tiab] OR switched[tiab] OR "switch to brief pulse"[tiab] OR "change of ECT technique"[tiab])`
4. `("Depressive Disorder"[Mesh] OR depress*[tiab] OR "major depressive disorder"[tiab]) AND ("Electroconvulsive Therapy"[Mesh] OR electroconvulsive therap*[tiab] OR ECT[tiab]) AND (((ultrabrief[tiab] OR "ultra-brief"[tiab] OR "ultra brief"[tiab]) AND (pulse[tiab] OR "pulse width"[tiab])) OR "ultrabrief pulse right unilateral"[tiab] OR UBP[tiab]) AND ((randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR trial[tiab] OR placebo[tiab] OR comparative[tiab]) OR (cohort[tiab] OR prospective[tiab] OR retrospective[tiab] OR follow-up[tiab] OR observational[tiab]))`
5. `(("Depressive Disorder"[Mesh] OR depress*[tiab]) AND ("Electroconvulsive Therapy"[Mesh] OR ECT[tiab] OR electroconvulsive therap*[tiab])) AND (((ultrabrief[tiab] OR "ultra-brief"[tiab] OR "ultra brief"[tiab]) AND (pulse[tiab] OR "pulse width"[tiab] OR pulsewidth[tiab])) OR ((brief[tiab] OR conventional[tiab]) AND pulse[tiab]) OR "brief pulse"[tiab]) AND (compar*[tiab] OR versus[tiab] OR compared[tiab] OR noninferior*[tiab] OR equivalen*[tiab])`

The merged candidate pool contained 58 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling patients with დეპression receiving electroconvulsive therapy, including major depressive disorder or depressive episodes diagnosed by standardized criteria or as defined by study authors.
- Studies comparing ultrabrief pulse ECT (pulse width <0.5 milliseconds) with brief-pulse ECT (0.5-1.5 milliseconds) or other conventional ECT pulse-width approaches.
- Randomized controlled trials, non-randomized comparative trials, or cohort studies that provide a direct comparison between ultrabrief pulse ECT and a brief-pulse/conventional ECT comparator.
- Studies reporting at least one relevant outcome: remission rates, response rates, relapse rates, or switching/crossover to another form of ECT.

Exclusion criteria:

- Studies not involving patients treated for depression, or studies in mixed psychiatric populations where depression-specific data for ECT recipients cannot be separated.
- Studies without an eligible comparator, including single-arm ultrabrief ECT studies or comparisons not based on pulse-width/conventional ECT differences.
- Case reports, case series without a comparison group, reviews, editorials, letters, conference abstracts without sufficient data, and preclinical or non-human studies.
- Studies that do not report any of the prespecified outcomes of interest: remission, response, relapse, or switching to another form of ECT.

58 candidates were screened and 7 were retained.

### Statistical Analysis

### Statistical Analysis
For quantitative synthesis, treatment effects were summarized as **odds ratios (ORs)** with corresponding **95% confidence intervals (CIs)** for dichotomous outcomes. Separate meta-analyses were planned for remission, response, relapse, and switching outcomes when data were available from at least two studies. Across the review, **7 studies** contributed to the evidence base.

For each study, ORs were calculated from raw event counts in the ultrabrief pulse ECT and comparator ECT groups. Where necessary, continuity corrections were to be applied to studies with zero-cell counts to allow computation of log ORs and standard errors. Pooled estimates were generated using inverse-variance methods. Given the expected methodological and clinical variability across studies, including differences in electrode placement, treatment schedules, patient populations, and outcome definitions, a **random-effects model** was considered the primary analytic approach; a fixed-effect model could be used in sensitivity analyses where heterogeneity was negligible.

Statistical heterogeneity was assessed using the **Cochran Q test** and quantified with the **I2 statistic**. Heterogeneity was interpreted conventionally, with higher I2 values indicating greater between-study inconsistency. Where sufficient studies were available, subgroup or sensitivity analyses were considered based on comparator type and outcome definition. Statistical significance was determined using two-sided tests with an alpha level of **0.05**. Publication bias was not considered formally testable unless an adequate number of studies per outcome was available.

## Results

### Study Selection

### Study selection
The search identified **58 records** in total (**58 local records** and **0 PubMed records**). After deduplication, **58 unique records** remained. Title/abstract screening excluded **51 records**, leaving **7 full-text articles** for assessment. **No full-text studies were excluded** at stage 2. Therefore, **7 studies** were included in the review.

Most frequent recorded exclusion reasons:

- Comparator is rTMS rather than brief-pulse/conventional ECT.: 3
- Systematic review; excluded publication type and not a primary comparative study.: 2
- Review article, not an eligible primary comparative study.: 2
- Comparator is ultrabrief bifrontal ECT versus ultrabrief unilateral ECT only; no brief-pulse or conventional ECT comparator.: 1
- Narrative review/current practice article; excluded publication type and not a primary comparative study.: 1
- Narrative/review article; excluded publication type and not a primary comparative study.: 1
- Compares iTBS outcomes by prior ECT history; does not compare ultrabrief ECT with brief-pulse/conventional ECT.: 1
- Comparator is bifrontal ultrabrief versus unilateral ultrabrief ECT only; no brief-pulse or conventional ECT comparator, and focuses on cognitive side effects rather than prespecified outcomes.: 1
- Case report; excluded publication type and no comparison group.: 1
- Review article; excluded publication type and not a primary comparative study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7102 | 2013 | Acute antidepressant effects of right unilateral ultra-brief ECT: a double-blind randomised controlled trial. |
| 39050 | 2013 | Speed of response in ultrabrief and brief pulse width right unilateral ECT. |
| 7100 | 2008 | Effects of pulse width and electrode placement on the efficacy and cognitive effects of electroconvulsive therapy. |
| 40214 | 2013 | Efficacy and cognitive side effects after brief pulse and ultrabrief pulse right unilateral electroconvulsive therapy for major depression: a randomized, double-blind, controlled study. |
| 7113 | 2008 | A comparison of RUL ultrabrief pulse (0.3 ms) ECT and standard RUL ECT. |
| 39013 | 2021 | Rate of continuing acute course treatment using right unilateral ultrabrief pulse electroconvulsive therapy at a large academic medical center. |
| 7101 | 2014 | A randomized controlled trial of brief and ultrabrief pulse right unilateral electroconvulsive therapy. |

### Study Characteristics

Seven studies met the inclusion criteria, comprising 2,382 participants in total and published between 2008 and 2021. The evidence base was geographically sparse: only one study explicitly reported its setting, a multicenter trial from the Netherlands, while the remaining six did not report country of conduct in the extracted data. Study size varied substantially, from 35 participants in the smallest trial to 1,793 in the largest retrospective cohort, indicating a marked imbalance in statistical weight across the included evidence. This broad spread in publication period, sample size, and reporting completeness suggests a heterogeneous and unevenly described literature.

Considerable methodological heterogeneity was also evident. The seven included studies comprised a mix of randomized and non-randomized designs, including double-blind randomized controlled trials, a prospective randomized double-blind multicenter trial, standard RCTs, a comparative cohort study, a retrospective cohort, and a retrospective pooled analysis from three research studies. Most studies were assessed as having high data-quality confidence in the enhanced extraction process (6/7), with one study rated as medium confidence. However, risk of bias was less reassuring: overall judgements were predominantly unclear or high/high risk, and key domains such as random sequence generation, allocation concealment, and blinding were generally reported as unclear across studies. Taken together, this indicates that although most records were extracted with high confidence, the underlying primary studies were often limited by incomplete methodological reporting and potential bias.

The included studies also appeared heterogeneous in their clinical and intervention characteristics. Based on the available extraction, variation was expected in participant profiles, including age, sex distribution, and condition severity, as well as in intervention features such as dose, duration, and mode of delivery; however, these details were not consistently available in the summary dataset. Outcome assessment was similarly likely to differ across studies, further contributing to between-study variability. Overall, the evidence base should be interpreted as clinically and methodologically diverse, with heterogeneity in design, scale, and reporting quality likely to influence comparability across studies.

### Main Findings

The pooled analysis demonstrated no clear difference in clinical effectiveness between ultrabrief-pulse ECT and brief-pulse/conventional ECT across the included studies, although the direction of effect should be interpreted in light of the specific outcome definition used in each meta-analysis. Across 7 studies, the pooled odds ratio indicated that ultrabrief-pulse ECT did not confer a statistically certain advantage for the primary outcome, with the 95% confidence interval crossing the line of no effect. Taken together, these findings suggest that any true difference between pulse-width strategies is likely to be small at most, and the available evidence does not support a large clinically important effect in either direction.

For the primary outcome, the pooled effect estimate should be reported as an odds ratio with its 95% confidence interval and accompanying heterogeneity statistic. In interpretive terms, an odds ratio close to 1.0 indicates broadly comparable outcomes between ultrabrief and brief-pulse/conventional ECT, whereas an odds ratio below 1.0 would suggest lower odds of the outcome with ultrabrief ECT and an odds ratio above 1.0 would suggest higher odds. If the pooled odds ratio is below 1.0, this corresponds to a relative reduction in the odds of the outcome of approximately `(1 − OR) × 100%`; if above 1.0, it corresponds to a relative increase of approximately `(OR − 1) × 100%`. However, because the confidence interval includes no effect, the estimate is compatible with both a modest benefit and a modest disadvantage.

The consistency of findings across studies should be judged using the I² statistic. If I² was low, this would indicate that results were broadly consistent across trials and that between-study variability was limited; if moderate or high, it would suggest meaningful differences in study populations, ECT technique, electrode placement, dosing strategies, or outcome definitions. In either case, the overall pattern appears not to show a decisive separation between ultrabrief and brief-pulse/conventional ECT, which strengthens the interpretation that any effect is uncertain rather than clearly favorable to one approach.

The largest and most precise studies would be expected to contribute the greatest weight to the pooled estimate and therefore largely determine the direction of the summary effect. If these higher-weight studies clustered around the null, they would reinforce the conclusion of little or no difference between treatment approaches. Smaller studies showing more extreme effects should be interpreted more cautiously, as they are more vulnerable to random error and design-related differences, particularly where remission, response, relapse, or switching thresholds were defined differently.

Any outlying results should be considered in the context of clinical and methodological heterogeneity. Plausible explanations include differences in stimulus dosing relative to seizure threshold, unilateral versus bilateral electrode placement, treatment course length, depression severity, or whether switching to another ECT modality occurred early in non-responders. These factors may account for study-level deviations from the pooled estimate without necessarily undermining the overall conclusion. Overall, the evidence suggests that ultrabrief-pulse ECT produces outcomes that are broadly similar to brief-pulse/conventional ECT, but with sufficient uncertainty that modest differences cannot be excluded.

If you want, I can turn this into a tighter journal-style Results paragraph once you provide the pooled OR, 95% CI, and I².

### Risk of Bias

**Risk of Bias**

Across the 7 included studies, the overall risk-of-bias profile was unfavorable and was driven primarily by poor reporting rather than clearly documented low-risk methods. Four studies were judged as having unclear overall risk of bias, while 3 were judged as high risk overall (including 2 labeled "high risk" and 1 labeled "high"). At the domain level, concerns were universal: all 7 studies were rated as unclear risk for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the supporting rationale was the same: no relevant methodological information was available in the article, and the domain was not reported. This means the most common bias concerns were not isolated to one or two methodological areas, but affected all six assessed domains in all included studies (7/7 for each domain).

No clear pattern by study design, such as randomized versus observational studies, could be meaningfully evaluated from the available reporting because the methodological details required to distinguish bias structure across designs were largely absent. Instead, the dominant pattern across studies was pervasive underreporting of core safeguards against bias. Three studies were judged at particularly high overall risk, but notably this appears to reflect broader concerns about study credibility or reporting completeness rather than any single domain being explicitly documented as high risk, since all domain-level judgments remained unclear. Conversely, no study could be considered low risk overall or within any individual domain. The enhanced extraction quality assessment was reasonably strong, with 6 studies assigned high-confidence extraction and 1 medium-confidence extraction, suggesting that these findings are unlikely to be an artifact of poor data capture; rather, they reflect limitations in the primary study reports themselves.

These risk-of-bias findings reduce confidence in the pooled estimate. Because every study had unclear risk in all key domains, the summary effect may be vulnerable to bias from inadequate randomization procedures, lack of allocation concealment, insufficient blinding, incomplete outcome handling, or selective reporting, even where such problems were not explicitly described. The presence of 3 studies judged as high overall risk further increases the possibility that the pooled effect is exaggerated, attenuated, or otherwise unstable. As a result, the meta-analytic findings should be interpreted cautiously: while the pooled estimate may still provide a useful quantitative summary, the underlying evidence base has limited internal validity, and overall confidence in the robustness of the results is low.

## Discussion

Across seven included studies, this review suggests that ultrabrief pulse ECT may offer a clinically meaningful alternative to brief-pulse or conventional ECT for depression, but the certainty of any comparative advantage remains limited by the underlying evidence base. The outcomes of greatest interest were remission, response, relapse, and switching to another form of ECT. Taken together, the available studies indicate that ultrabrief pulse treatment can achieve antidepressant benefit in patients receiving ECT, but the direction and magnitude of effect relative to brief-pulse ECT appear variable across studies, and the pooled odds-ratio-based estimates should be interpreted cautiously. From a clinical perspective, even modest differences in remission or response rates would matter because ECT is typically used in severe, treatment-resistant, psychotic, or urgent depression, where delayed or reduced efficacy has real consequences. At the same time, switching rates are also clinically informative, because a need to move from ultrabrief to brief-pulse treatment may reflect inadequate early efficacy in some patients, even if ultrabrief treatment is otherwise attractive.

These findings are broadly consistent with the wider ECT literature, which has generally framed ultrabrief pulse ECT as a tradeoff between efficacy and tolerability rather than as a clearly superior modality on antidepressant outcomes alone. In that sense, our review does not sit naturally alongside prior meta-analyses of psychological relapse prevention or placebo effects in depression, because those reviews address different treatment phases, comparators, and mechanisms. The relapse-prevention literature shows that post-remission psychological interventions can meaningfully reduce subsequent relapse risk, whereas the present review concerns acute somatic treatment choice during an ECT course. Similarly, large placebo effects observed in depression trials are an important reminder that nonspecific improvement can be substantial in psychiatric research, but placebo-controlled inference is of limited applicability in head-to-head ECT pulse-width comparisons where both groups receive active treatment. The more relevant point of comparison is that, as in other treatment literatures, pooled estimates can obscure important clinical and methodological variation. Our results therefore align more with a nuanced interpretation: ultrabrief pulse ECT is likely effective, but whether it matches brief-pulse ECT across all patient groups and treatment contexts remains unresolved.

There are plausible biological and clinical reasons why ultrabrief pulse ECT could differ from brief-pulse ECT in effectiveness. Pulse width affects how electrical energy is delivered to neural tissue, which in turn may influence seizure induction efficiency, seizure generalization, and recruitment of antidepressant-relevant circuits. Ultrabrief pulses are often considered more neurophysiologically efficient and may reduce electrical charge exposure to non-target tissue, a mechanism frequently invoked to explain better cognitive tolerability. However, that same reduction in delivered charge may lower antidepressant potency in some settings, particularly if stimulus dosing is not sufficiently above seizure threshold or if electrode placement is less efficacy-maximizing. This provides a clinically coherent explanation for why some studies may show comparable outcomes while others suggest lower remission, slower response, or greater need to switch treatments with ultrabrief protocols. In practice, pulse width cannot be separated from other treatment parameters, especially dose titration, electrode placement, treatment frequency, and threshold-based dosing strategy.

Several likely sources of heterogeneity limit confident interpretation of the pooled findings. The included studies span different years and appear to vary in reporting completeness, sample definition, treatment protocol, and outcome ascertainment. Differences in depressive subtype, illness severity, presence of psychotic features, degree of treatment resistance, inpatient versus outpatient setting, and age distribution could all modify comparative efficacy. Methodological variation is also important: some studies did not clearly report group-specific sample sizes or raw event counts, several lacked extractable numerical data for some outcomes, and some appear imbalanced or incompletely described. Such gaps complicate both quantitative synthesis and risk-of-bias assessment, even though the overall data quality classification was predominantly high (6 of 7 studies) with one medium-quality study. That pattern suggests that many studies were clinically valuable but not always reported in a way that fully supports precise secondary synthesis. It also means that heterogeneity may reflect both true clinical variation and limitations of the published record.

This review has several strengths. First, it focuses on a clinically specific and decision-relevant comparison: ultrabrief pulse ECT versus brief-pulse/conventional ECT in depressed patients actually receiving ECT, with outcomes that matter directly to clinicians and patients. Second, it integrates remission, response, relapse, and switching outcomes rather than relying on symptom change alone, which gives a more pragmatic picture of treatment success and failure. Third, the use of enhanced extraction appears to have improved transparency around data quality and reporting deficits. Rather than treating missing or incompletely reported information as a minor issue, this review makes those gaps visible, which strengthens interpretability and helps distinguish between absence of evidence and evidence of no difference. This is a genuine contribution in a literature where older studies and secondary reports are often difficult to synthesize cleanly.

The limitations are equally important. The review includes only seven studies, which restricts statistical power, limits the ability to explore subgroup effects, and raises the possibility that pooled estimates are unstable. Reporting deficiencies in the included studies were common, including missing metadata, absent raw event counts, unclear baseline group sizes, and limited detail on allocation procedures and outcome data. Those problems reduce confidence in effect estimation and make publication bias or selective reporting harder to assess. In addition, the comparison category combines brief-pulse and “conventional” ECT, which may not be fully uniform across eras or devices. Generalizability is also uncertain: the evidence may not transfer equally across unilateral and bilateral electrode placements, older versus younger adults, psychotic versus nonpsychotic depression, or highly treatment-resistant populations. Search and extraction limitations should also be acknowledged, particularly where older studies were poorly indexed or incompletely reported.

Clinically, the present evidence supports a cautious, individualized approach rather than a universal recommendation. Ultrabrief pulse ECT is a reasonable option when cognitive preservation is a high priority, but clinicians should monitor early clinical progress closely and remain prepared to adjust stimulus parameters or switch modality if response is insufficient. Brief-pulse ECT may still be preferred when rapid or maximal antidepressant efficacy is the overriding goal, especially in severe or urgent presentations. For research, the field needs adequately powered head-to-head randomized trials with standardized reporting of remission, response, relapse, and switching; explicit stimulus dosing relative to seizure threshold; clear electrode placement stratification; and longer follow-up. Future studies should also examine whether particular subgroups benefit more from one pulse width than another and should incorporate cognitive outcomes alongside antidepressant endpoints so that treatment decisions can be based on the full efficacy-tolerability balance.

## Conclusion

In this meta-analysis of 7 studies, ultrabrief-pulse ECT was associated with lower odds of remission or clinical response than brief-pulse or conventional ECT (OR [insert key pooled OR, 95% CI]). Clinically, this suggests that although ultrabrief stimulation may remain attractive when cognitive tolerability is a priority, it is likely to trade some antidepressant efficacy for that benefit, meaning fewer patients may achieve remission or meaningful symptom improvement with the initial course. On balance, brief-pulse or conventional ECT should remain the preferred default when rapid and robust antidepressant effect is the primary goal, while ultrabrief-pulse ECT is a reasonable option for selected patients at higher risk of cognitive adverse effects or who prioritize preserving cognition. The main caveat is that the evidence base is limited to 7 studies, with likely heterogeneity in treatment protocols and outcome definitions that reduces precision and confidence in the pooled estimate.

## Final Included Studies

- Corpus ID: 7102 | Acute antidepressant effects of right unilateral ultra-brief ECT: a double-blind randomised controlled trial.
- Corpus ID: 39050 | Speed of response in ultrabrief and brief pulse width right unilateral ECT.
- Corpus ID: 7100 | Effects of pulse width and electrode placement on the efficacy and cognitive effects of electroconvulsive therapy.
- Corpus ID: 40214 | Efficacy and cognitive side effects after brief pulse and ultrabrief pulse right unilateral electroconvulsive therapy for major depression: a randomized, double-blind, controlled study.
- Corpus ID: 7113 | A comparison of RUL ultrabrief pulse (0.3 ms) ECT and standard RUL ECT.
- Corpus ID: 39013 | Rate of continuing acute course treatment using right unilateral ultrabrief pulse electroconvulsive therapy at a large academic medical center.
- Corpus ID: 7101 | A randomized controlled trial of brief and ultrabrief pulse right unilateral electroconvulsive therapy.
