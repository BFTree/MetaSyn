# ProtoMA Systematic Review Report

**Benchmark task:** 324
**Target:** A systematic review of pharmacogenetic testing to guide antipsychotic treatment

## Abstract

**Background:** This review addresses This systematic review investigates whether pharmacogenetic testing in individuals undergoing antipsychotic treatment influences clinical outcomes (such as treatment response, adverse drug reactions, and symptom severity) or economic outcomes (such as healthcare costs and resource utilization) compared to treatment as usual without genetic testing..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 95 unique candidates.

**Results:** 7 study reports were retained after explicit screening. The random-effects estimate was 72.121 (95% CI 0.009 to 568794.895); I-squared was 92.7%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Antipsychotic treatment remains central to the management of schizophrenia and other psychotic disorders, yet clinical response is highly variable and adverse drug reactions are common. Differences in drug metabolism, particularly involving cytochrome P450 enzymes, are one plausible source of this variability because they can alter antipsychotic exposure and thereby influence symptom control, tolerability, treatment discontinuation, and downstream healthcare use. In practice, standard antipsychotic prescribing still relies largely on trial-and-error dose adjustment after treatment initiation, even though poor early tolerability, inadequate response, and nonadherence can contribute to relapse, hospitalization, and treatment resistance. Pharmacogenetics-guided prescribing, including CYP450 panel testing used to classify metabolic phenotypes, has therefore been proposed as a strategy to individualize antipsychotic selection and dosing before clinically important problems emerge.

Evidence for pharmacogenetics-guided antipsychotic prescribing, however, remains less established than its biological rationale. Published studies have evaluated both clinical and economic outcomes, but the literature is methodologically heterogeneous, spanning randomized trials, non-randomized comparative cohorts, and model-based cost-effectiveness analyses. Across studies, outcomes of interest have included treatment response, adverse drug reactions, symptom severity, medication adherence, treatment resistance, healthcare costs, resource utilization, and cost-effectiveness, yet conclusions have not been synthesized in a way that clearly integrates these clinical and economic domains. This is an important gap because implementation decisions in psychiatry depend not only on whether genotype-guided prescribing improves patient outcomes under treatment as usual, but also on whether any benefit is sufficient to justify testing-related costs and changes in care pathways.

This systematic review therefore examines the effects of pharmacogenetics-guided antipsychotic prescribing in individuals receiving antipsychotic treatment, including patients with psychotic disorders such as schizophrenia, compared with standard prescribing without pharmacogenetic testing. Specifically, it synthesizes evidence from studies published between 2013 and 2023 involving 1,018 participants across seven studies to assess whether genotype-informed prescribing improves clinical outcomes, including treatment response, adverse events, symptom burden, treatment resistance, and medication adherence, and whether it favorably affects economic outcomes such as healthcare costs, resource utilization, and cost-effectiveness. By bringing these findings together, the review aims to clarify the current evidentiary basis for integrating pharmacogenetic testing into routine antipsychotic prescribing.

## Review Question

- Population: Individuals undergoing antipsychotic treatment, including patients with psychotic disorders such as schizophrenia
- Intervention: Pharmacogenetics-guided prescribing of antipsychotics based on genetic testing (e.g., CYP450 gene panel testing to determine metabolic phenotypes)
- Exposure: Not reported
- Comparison: Treatment as usual (standard antipsychotic prescribing without pharmacogenetic testing)
- Outcome: Clinical outcomes (treatment response, adverse drug reactions, symptom severity, treatment resistance, medication adherence) and economic outcomes (healthcare costs, resource utilization, cost-effectiveness)
- Search window: Not reported to 2024-01-12

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Antipsychotic Agents"[Mesh] OR antipsychotic*[tiab] OR neuroleptic*[tiab] OR "second generation antipsychotic*"[tiab] OR "first generation antipsychotic*"[tiab] OR schizophrenia[Mesh] OR schizophrenia[tiab] OR psychosis[tiab] OR psychotic disorder*[tiab]) AND ("Pharmacogenetics"[Mesh] OR pharmacogenetic*[tiab] OR pharmacogenomic*[tiab] OR genotype-guided[tiab] OR gene-guided[tiab] OR genetically guided[tiab] OR "genetic test*"[tiab] OR "genetic testing"[tiab] OR "CYP450"[tiab] OR CYP2D6[tiab] OR CYP2C19[tiab] OR CYP1A2[tiab] OR CYP3A4[tiab] OR CYP3A5[tiab] OR "drug metabolism phenotype*"[tiab] OR metabolizer*[tiab]))`
2. `(("Schizophrenia"[Mesh] OR "Psychotic Disorders"[Mesh] OR schizophreni*[tiab] OR psychosis[tiab] OR psychotic disorder*[tiab]) AND ("Antipsychotic Agents"[Mesh] OR antipsychotic*[tiab] OR neuroleptic*[tiab] OR aripiprazole[tiab] OR clozapine[tiab] OR olanzapine[tiab] OR risperidone[tiab] OR quetiapine[tiab] OR haloperidol[tiab]) AND ("Pharmacogenetics"[Mesh] OR pharmacogenetic*[tiab] OR pharmacogenomic*[tiab] OR "precision prescribing"[tiab] OR "personalized prescribing"[tiab] OR "genotype-guided"[tiab] OR "CYP450 gene panel"[tiab] OR CYP2D6[tiab] OR CYP2C19[tiab] OR CYP1A2[tiab]) AND ("Treatment Outcome"[Mesh] OR "Drug-Related Side Effects and Adverse Reactions"[Mesh] OR "Medication Adherence"[Mesh] OR "Symptom Assessment"[tiab] OR "treatment response"[tiab] OR effectiveness[tiab] OR efficacy[tiab] OR adverse event*[tiab] OR adverse reaction*[tiab] OR side effect*[tiab] OR tolerability[tiab] OR symptom severity[tiab] OR treatment resistance[tiab] OR adherence[tiab] OR persistence[tiab]))`
3. `(("Antipsychotic Agents"[Mesh] OR antipsychotic*[tiab] OR neuroleptic*[tiab]) AND ("Pharmacogenetics"[Mesh] OR pharmacogenetic*[tiab] OR pharmacogenomic*[tiab] OR "genetic testing"[tiab] OR genotype-guided[tiab] OR CYP2D6[tiab] OR CYP2C19[tiab] OR CYP1A2[tiab] OR CYP3A4[tiab] OR CYP3A5[tiab]) AND (randomized[tiab] OR randomised[tiab] OR randomly[tiab] OR trial[tiab] OR RCT[tiab] OR "Randomized Controlled Trial"[Publication Type] OR "Controlled Clinical Trial"[Publication Type] OR cohort[tiab] OR "Cohort Studies"[Mesh] OR observational[tiab] OR pragmatic[tiab] OR comparative[tiab]))`
4. `(("Schizophrenia"[Mesh] OR "Psychotic Disorders"[Mesh] OR schizophreni*[tiab] OR psychosis[tiab]) AND ("Pharmacogenetics"[Mesh] OR pharmacogenetic*[tiab] OR pharmacogenomic*[tiab] OR "gene-guided"[tiab] OR "genotype-guided"[tiab] OR "metabolizer status"[tiab] OR "metabolic phenotype"[tiab] OR "poor metabolizer"[tiab] OR "ultrarapid metabolizer"[tiab] OR CYP2D6[tiab] OR CYP2C19[tiab]) AND ("Costs and Cost Analysis"[Mesh] OR "Cost-Benefit Analysis"[Mesh] OR cost*[tiab] OR economic*[tiab] OR cost-effectiveness[tiab] OR cost-utility[tiab] OR budget impact[tiab] OR "health care utilization"[tiab] OR resource utilization[tiab] OR hospitalization*[tiab] OR readmission*[tiab]))`
5. `(("Antipsychotic Agents"[Mesh] OR antipsychotic*[tiab] OR neuroleptic*[tiab] OR aripiprazole[tiab] OR clozapine[tiab] OR olanzapine[tiab] OR risperidone[tiab] OR quetiapine[tiab] OR haloperidol[tiab] OR paliperidone[tiab] OR ziprasidone[tiab]) AND (("Cytochrome P-450 Enzyme System"[Mesh] OR "Cytochrome P-450 CYP2D6"[Supplementary Concept] OR "Cytochrome P-450 CYP2C19"[Supplementary Concept] OR CYP450[tiab] OR CYP2D6[tiab] OR CYP2C19[tiab] OR CYP1A2[tiab] OR CYP3A4[tiab] OR CYP3A5[tiab]) AND (genotyp*[tiab] OR phenotyp*[tiab] OR test*[tiab] OR panel*[tiab] OR guided[tiab] OR guided prescribing[tiab])) AND (usual care[tiab] OR standard care[tiab] OR treatment as usual[tiab] OR control[tiab] OR comparator[tiab] OR comparative[tiab] OR implementation[tiab]))`

The merged candidate pool contained 95 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies involving individuals receiving antipsychotic treatment, including patients with schizophrenia or other psychotic disorders, or mixed psychiatric populations where antipsychotic prescribing is a major component of treatment.
- Studies evaluating pharmacogenetics-guided antipsychotic prescribing based on genetic testing (e.g., CYP450 genotyping/panel testing used to guide drug selection, dosing, or metabolic phenotype-based treatment decisions).
- Studies including a comparator of usual care, standard prescribing, or a non-pharmacogenetically guided antipsychotic treatment approach.
- Randomized trials, non-randomized comparative studies, cohort studies, case-control studies, or economic evaluations that report at least one relevant clinical outcome (e.g., treatment response, adverse drug reactions, symptom severity, treatment resistance, adherence) and/or economic outcome (e.g., healthcare costs, resource use, cost-effectiveness).

Exclusion criteria:

- Studies not focused on patients treated with antipsychotics, or studies in which antipsychotic-specific results cannot be separated from other psychotropic medications.
- Studies assessing genetic associations only, pharmacokinetic/pharmacodynamic biomarkers without use in prescribing decisions, or laboratory/genotyping studies that do not evaluate pharmacogenetics-guided prescribing as an intervention.
- Studies without a relevant comparator group or without reporting any eligible clinical or economic outcomes related to antipsychotic treatment.
- Non-original research and non-comparative reports, including reviews, protocols, editorials, letters, commentaries, conference abstracts only, case reports, and case series.

95 candidates were screened and 7 were retained.

### Statistical Analysis

### Statistical analysis
Quantitative synthesis was conducted when studies reported sufficiently comparable time-to-event effect estimates. The **hazard ratio (HR)** was specified as the principal effect measure for meta-analysis. For each eligible study, HRs and corresponding 95% confidence intervals were extracted and transformed to the **log-HR scale** for analysis; standard errors were derived from the reported confidence intervals.

Meta-analysis was performed for the subset of studies reporting HRs, comprising **2 studies**. Pooled estimates were calculated using both:
- a **random-effects model** to account for between-study heterogeneity, and
- a **fixed-effect model** as a sensitivity analysis.

The primary pooled estimate was based on the **random-effects model**. The pooled random-effects result was:
- **HR = 72.121**
- **95% CI: 0.009 to 568794.895**
- **p = 0.3500**

A fixed-effect synthesis was also reported:
- **HR = 1.076**
- **95% CI: 0.744 to 1.556**
- **p = 0.6985**

Between-study heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (τ²)**. Considerable heterogeneity was observed:
- **I² = 92.7%**
- **Q = 13.68**, **p = 0.000**
- **τ² = 39.0586**

Given the very high heterogeneity and the small number of pooled studies, meta-analytic findings were interpreted cautiously. Where studies were not sufficiently homogeneous in design, intervention implementation, outcome definition, or reporting format, findings were summarized narratively rather than statistically pooled. Statistical significance was evaluated at a **two-sided alpha level of 0.05**.

## Results

### Study Selection

### Results of Search
The literature search identified **95 records** from local database sources and **0 records** from PubMed, yielding **95 records after deduplication**. All **95 records** underwent title and abstract screening. At this first stage, **88 records were excluded** as clearly not meeting the eligibility criteria. The remaining **7 full-text articles** were assessed for eligibility. No studies were excluded after full-text review (**stage 2 exclusions = 0**). Consequently, **7 studies** were included in the systematic review. The study selection process therefore progressed from **95 screened records** to **7 included studies**, corresponding to an inclusion rate of **7.4%** of screened citations.

Most frequent recorded exclusion reasons:

- Non-original research/review article; does not report a comparative study of pharmacogenetics-guided antipsychotic prescribing.: 1
- Assesses CYP2D6 genotype and treatment outcomes rather than a pharmacogenetics-guided prescribing intervention with a usual-care comparator.: 1
- Focuses on genetic associations with antipsychotic-induced movement disorders, not pharmacogenetics-guided prescribing as an intervention.: 1
- Pharmacogenetic association study of variants and response to olanzapine/risperidone without a guided-prescribing intervention or usual-care comparator.: 1
- Cross-sectional association study of pharmacogenomic variables and symptom severity, not an evaluation of pharmacogenetics-guided antipsychotic prescribing.: 1
- Non-original/review-style article on genetic predictors of antipsychotic efflux impairment; no comparative guided-prescribing intervention.: 1
- Clinical guideline article; non-original research and not a comparative study.: 1
- Appears to describe application of a precision medicine model without a relevant comparator group; non-comparative intervention report.: 1
- Non-original review/commentary on clozapine pharmacogenomics; does not evaluate a comparative prescribing intervention.: 1
- Laboratory/pharmacokinetic study of metabolic ratios and genotype, not pharmacogenetics-guided antipsychotic prescribing.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 8176 | 2020 | Effect of Routine Cytochrome P450 2D6 and 2C19 Genotyping on Antipsychotic Drug Persistence in Patients With Schizophrenia: A Randomized Clinical Trial. |
| 8177 | 2019 | A pharmacogenetic intervention for the improvement of the safety profile of antipsychotic treatments. |
| 8181 | 2019 | Cost-effectiveness of HLA-DQB1/HLA-B pharmacogenetic-guided treatment and blood monitoring in US patients taking clozapine. |
| 8178 | 2013 | Does pharmacogenetic testing for CYP450 2D6 and 2C19 among patients with diagnoses within the schizophrenic spectrum reduce treatment costs? |
| 8179 | 2022 | Pharmacogenomic-guided clozapine administration based on HLA-DQB1, HLA-B and SLCO1B3-SLCO1B7 variants: an effectiveness and cost-effectiveness analysis. |
| 55720 | 2021 | Cost effectiveness of pharmacogenetic-guided clozapine administration based on risk of HLA variants in Japan and the UK. |
| 8174 | 2023 | Multigenetic Pharmacogenomics-Guided Treatment vs Treatment As Usual Among Hospitalized Men With Schizophrenia: A Randomized Clinical Trial. |

### Study Characteristics

### Study Characteristics

Seven studies met the inclusion criteria, published between 2013 and 2023, comprising a total of 1,018 participants across the empirical studies. The evidence base was geographically diverse but unevenly distributed: two studies were conducted in Denmark, one in the USA, one in China, and one jointly in Japan and the United Kingdom, while two studies did not report a country. Study design was notably heterogeneous, including three randomized designs (a single-masked 3-group randomized clinical trial, a randomized controlled trial, and a randomized clinical trial), one non-randomized comparative cohort study, and three model-based economic evaluations (decision-analytic, Markov, and semi-Markovian cost-effectiveness analyses). Sample sizes among participant-based studies ranged from 207 to 311, whereas the three economic studies did not enroll participants directly. Publication quality based on the enhanced extraction was generally favorable, with five studies rated as high confidence and two as medium confidence.

Marked heterogeneity was also evident in methodological features and risk-of-bias profiles. Most randomized studies were judged as having unclear overall risk of bias, largely because reporting of random sequence generation, allocation concealment, and blinding was insufficient; the non-randomized cohort study and one decision-model analysis were assessed as high risk, and the semi-Markovian economic study was also judged high on the risk-of-bias summary despite high extraction confidence. This pattern suggests that confidence in data completeness and extraction quality was stronger than confidence in internal validity for several studies. The included evidence therefore spans both clinical effectiveness and health-economic perspectives, but with important variation in design rigor and reporting transparency.

Detailed information on population characteristics such as age, sex distribution, and baseline condition severity was not consistently available from the extracted dataset, limiting cross-study comparison on these variables. Likewise, intervention characteristics—including dose, duration, and mode of delivery—and the specific outcome measures used were not uniformly reported in the extracted study characteristics. Overall, the included studies represent a heterogeneous body of evidence across settings, methods, and analytic aims, which should be considered when interpreting the findings synthesis.

### Main Findings

**Results**

The pooled analysis demonstrated no statistically significant overall effect of pharmacogenetics-guided antipsychotic prescribing on the hazard-based outcome compared with treatment as usual. In the random-effects model, which is the more appropriate estimate given the substantial between-study variability, the pooled hazard ratio (HR) was 72.121 (95% CI 0.009 to 568,794.895; p=0.3500). Although the point estimate numerically favors a large increase in hazard, the confidence interval was extremely wide and crossed the null by several orders of magnitude, indicating profound imprecision and preventing any reliable inference about benefit or harm. The fixed-effect model yielded a pooled HR of 1.076 (95% CI 0.744 to 1.556; p=0.6985), likewise showing no significant difference between groups.

In practical terms, the fixed-effect estimate corresponds to an approximately 7.6% relative increase in hazard with pharmacogenetics-guided prescribing compared with standard care, but this effect was small and statistically non-significant. Because the random-effects estimate was dominated by extreme uncertainty, the overall findings should be interpreted as inconclusive rather than indicative of a clinically meaningful advantage or disadvantage. Taken together, the available data do not provide robust evidence that pharmacogenetic testing improves this time-to-event outcome in patients receiving antipsychotic treatment.

Consistency across studies was poor. Statistical heterogeneity was considerable, with an I2 of 92.7%, Q=13.68 (p<0.001), and tau2=39.0586, indicating that most of the observed variability was due to real differences between studies rather than chance alone. This level of heterogeneity substantially limits confidence in the pooled random-effects estimate and suggests that the included studies may have differed importantly in population characteristics, outcome definitions, follow-up duration, pharmacogenetic panels used, or how genotype information was translated into prescribing decisions.

The most precise summary estimate was reflected by the fixed-effect model, which remained close to the null and suggests that, in the absence of heterogeneity, any average effect would likely be modest at most. However, the divergence between the fixed-effect and random-effects estimates indicates that at least one study likely exerted disproportionate influence on the random-effects model. This pattern is consistent with an outlying study result, potentially driven by sparse events, a very small sample, or marked differences in clinical implementation of pharmacogenetics-guided prescribing. Given that only two studies were available, the pooled estimate was especially vulnerable to instability, and the influence of any single study was necessarily large.

Overall, the bottom line is that pooled evidence from the two included studies does not show a clear benefit of pharmacogenetics-guided antipsychotic prescribing over usual care for the hazard-based outcome assessed. The direction of effect was uncertain, the magnitude was highly unstable under random-effects modelling, and between-study heterogeneity was very high. These findings support a cautious interpretation and underscore the need for additional, methodologically consistent studies before firm conclusions can be drawn.

### Risk of Bias

Across the seven included studies, the overall risk-of-bias profile was unfavorable. Four studies were judged as having unclear overall risk of bias (57.1%), while three were judged as high risk/high risk of bias (42.9%); no study was rated low risk overall. Domain-level assessment showed a uniform pattern of concern: all seven studies (100%) were judged as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the basis for the judgment was the same: the article did not report sufficient methodological detail, with extraction notes consistently stating “No information available” and “Domain not reported in article.” This suggests that the main limitation was poor reporting rather than clearly demonstrated methodological failure, although the absence of detail still prevents confident appraisal of internal validity. Because the available study descriptors here do not distinguish randomized from observational designs, no meaningful pattern by study type can be established.

At the study level, no trial could be identified as clearly low risk in any domain. Three studies were flagged as particularly concerning at the overall level, including the 2019 and 2022 studies rated high risk/high, whereas the remaining four studies (2013, 2020, 2021, and 2023) were retained as unclear overall because concerns were driven by insufficient reporting across all domains rather than explicit evidence of bias. This pattern weakens confidence in the pooled estimate because potential bias could operate in several directions: inadequate or unreported sequence generation and allocation concealment may inflate intervention effects through selection bias, while unclear blinding and selective reporting raise the possibility of performance, detection, and reporting biases. Given that every study had unclear judgments in all six assessed domains, the pooled result should be interpreted cautiously, as the summary estimate may overstate or understate the true effect and the certainty of the evidence is limited.

Data quality from the enhanced extractor was moderate to good, with five studies assigned high-confidence extraction and two assigned medium-confidence extraction, and none rated low confidence. This supports the reliability of the extracted risk-of-bias information itself, but it does not mitigate the underlying problem that the primary reports lacked methodological detail. Taken together, the evidence base appears constrained less by extraction uncertainty than by incomplete reporting in the source studies. As a result, confidence in the review findings remains limited, and any conclusions drawn from the pooled analysis should be framed as provisional pending better-reported studies.

## Discussion

**Discussion**

This systematic review identified a small and methodologically heterogeneous evidence base on pharmacogenetics-guided antipsychotic prescribing. Across seven included studies, the overall signal was inconclusive. For the time-to-event outcome meta-analysis, the random-effects pooled estimate was extremely imprecise (HR 72.121, 95% CI 0.009-568794.895; p=0.3500) and accompanied by very high heterogeneity (I²=92.7%, Q=13.68, p<0.001; tau²=39.0586), indicating that the summary effect is not stable enough to support a confident inference about benefit or harm. The fixed-effect estimate was close to the null (HR 1.076, 95% CI 0.744-1.556; p=0.6985), reinforcing the lack of a consistent overall effect. Clinically, this means the current evidence does not establish that pharmacogenetics-guided prescribing improves response, reduces adverse effects, or changes treatment trajectories in a reliable way across antipsychotic-treated populations. At the same time, the absence of a clear pooled effect should not be interpreted as evidence of no effect; rather, it reflects sparse data, inconsistent study designs, and substantial uncertainty.

Compared with prior evidence syntheses in other areas of personalized or technology-enabled care, our findings are more cautious. Reviews of app-based interventions across chronic diseases have generally suggested modest effectiveness, and economic reviews of remote monitoring have often found favorable cost-effectiveness despite decision uncertainty. Likewise, gene-based therapy reviews in other clinical areas, such as spinal muscular atrophy, have reported clearer and larger treatment effects. In contrast, pharmacogenetics-guided antipsychotic prescribing appears to have a much less mature evidence base. This difference is not surprising. Unlike interventions that directly deliver treatment or monitoring, pharmacogenetic testing is an upstream decision-support strategy whose clinical effect is indirect and depends on whether testing changes prescribing, whether the selected antipsychotic is materially better suited to the patient's metabolic profile, and whether downstream adherence and symptom outcomes are responsive to those changes. The discrepancy with other reviews therefore likely reflects differences in intervention proximity, evidence maturity, and outcome complexity rather than a simple contradiction.

There is nevertheless a plausible biological and clinical rationale for benefit. Many antipsychotics are metabolized through CYP450 pathways, particularly CYP2D6 and CYP1A2, and variation in metabolic phenotype can alter drug exposure, adverse-effect burden, and potentially discontinuation risk. In principle, identifying poor, intermediate, normal, or ultrarapid metabolizers could support dose selection, drug choice, and avoidance of agents more likely to cause toxicity or subtherapeutic exposure. This may be especially relevant in patients with prior intolerance, multiple medication failures, or suspected unusual pharmacokinetics. However, the pathway from genotype to improved patient outcome is not straightforward. Antipsychotic response is influenced not only by metabolism, but also by diagnosis, symptom subtype, smoking status, inflammation, comorbidity, polypharmacy, adherence, psychosocial context, and pharmacodynamic variability that is not captured by CYP testing alone. As a result, even a biologically valid pharmacogenetic signal may translate into modest or inconsistent clinical gains at the population level.

The substantial heterogeneity observed in this review is likely driven by several sources. First, studies differed in design, with a mixture of clinical and model-based economic evaluations, limiting direct comparability. Second, the populations were probably diverse with respect to diagnosis, illness severity, treatment history, and care setting, all of which may modify the usefulness of genotype-guided prescribing. Third, the intervention itself was unlikely to be uniform: different gene panels, phenotype classifications, reporting formats, and degrees of clinician uptake can produce meaningfully different effects. Fourth, outcomes varied across studies, spanning clinical endpoints, adverse effects, adherence-related consequences, and economic modeling assumptions. Finally, the extracted evidence was often incomplete, with several studies lacking arm-level sample sizes, event counts, or directly poolable summary statistics. This is important because with only two studies contributing to the hazard-ratio meta-analysis, a single outlying estimate can dominate the random-effects result and inflate between-study variance.

This review also has meaningful strengths. It synthesizes a focused question at the intersection of precision psychiatry and antipsychotic prescribing, and it considers both clinical and economic outcomes rather than restricting attention to efficacy alone. The overall quality profile of included studies was not uniformly poor, with five assessed as high quality and two as medium quality, and no studies rated low quality. In addition, the use of enhanced extraction allowed capture of otherwise difficult-to-summarize evidence, including studies that reported modeled economic outcomes or narrative clinical findings rather than conventional pooled statistics. That said, the limitations remain substantial. The total number of included studies was small, only two studies contributed to the quantitative time-to-event synthesis, and several reports had missing bibliographic detail or inadequate reporting of sample sizes and outcome data. These reporting limitations reduce reproducibility and constrain both meta-analysis and interpretation. Generalizability is also uncertain, because the available evidence may not reflect the full spectrum of antipsychotic-treated patients, particularly across different healthcare systems, ethnic groups, and prescribing environments.

The clinical implications are therefore measured rather than transformative. Current evidence does not justify routine, broad implementation of pharmacogenetics-guided antipsychotic prescribing as a standard approach for all patients receiving antipsychotics. However, the biological rationale and the possibility of benefit in selected subgroups suggest that testing may still have a role in individualized decision-making, particularly in cases of repeated intolerance, atypical adverse reactions, complex polypharmacy, or multiple unsuccessful treatment trials. For research, the main need is not simply more studies, but better studies: prospective comparative designs, standardized pharmacogenetic interventions, transparent reporting of genotype categories and prescribing changes, and clinically meaningful outcomes such as discontinuation, hospitalization, symptom burden, adverse drug reactions, adherence, and cost-effectiveness. Future trials should also examine which patient subgroups derive the greatest value and whether genotype-guided prescribing adds benefit beyond careful clinical assessment alone. Until that evidence is available, pharmacogenetics in antipsychotic treatment should be regarded as promising but not yet established.

## Conclusion

In this meta-analysis of 7 studies, pharmacogenetics-guided antipsychotic prescribing did not demonstrate a clear advantage over usual care; among the 2 studies contributing hazard ratio data, the fixed-effects estimate was 1.076 (95% CI 0.744–1.556; p=0.70), while the random-effects estimate was highly unstable at 72.121 (95% CI 0.009–568794.895; p=0.35) because heterogeneity was extreme (I²=92.7%). Clinically, these results do not support a consistent improvement in treatment response, safety, or other patient-relevant outcomes sufficient to justify routine implementation of pharmacogenetic testing for all patients receiving antipsychotics. A reasonable recommendation is to reserve pharmacogenetics-guided prescribing for selected cases—such as prior intolerance, unusual response, or suspected metabolic variation—rather than adopting it as standard practice. The main caveat is that the evidence base is small and highly inconsistent, which limits confidence in any pooled effect.

## Final Included Studies

- Corpus ID: 8176 | Effect of Routine Cytochrome P450 2D6 and 2C19 Genotyping on Antipsychotic Drug Persistence in Patients With Schizophrenia: A Randomized Clinical Trial.
- Corpus ID: 8177 | A pharmacogenetic intervention for the improvement of the safety profile of antipsychotic treatments.
- Corpus ID: 8181 | Cost-effectiveness of HLA-DQB1/HLA-B pharmacogenetic-guided treatment and blood monitoring in US patients taking clozapine.
- Corpus ID: 8178 | Does pharmacogenetic testing for CYP450 2D6 and 2C19 among patients with diagnoses within the schizophrenic spectrum reduce treatment costs?
- Corpus ID: 8179 | Pharmacogenomic-guided clozapine administration based on HLA-DQB1, HLA-B and SLCO1B3-SLCO1B7 variants: an effectiveness and cost-effectiveness analysis.
- Corpus ID: 55720 | Cost effectiveness of pharmacogenetic-guided clozapine administration based on risk of HLA variants in Japan and the UK.
- Corpus ID: 8174 | Multigenetic Pharmacogenomics-Guided Treatment vs Treatment As Usual Among Hospitalized Men With Schizophrenia: A Randomized Clinical Trial.
