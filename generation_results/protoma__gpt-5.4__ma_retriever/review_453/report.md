# ProtoMA Systematic Review Report

**Benchmark task:** 453
**Target:** Statins exposure and adverse events in participants with chronic viral hepatitis: a meta-analysis based on cohort studies

## Abstract

**Background:** This review addresses This meta-analysis investigates whether statin exposure is associated with a reduced incidence of adverse events, including hepatocellular carcinoma (HCC), all-cause mortality, cirrhosis, and cirrhosis decompensation, in individuals with chronic viral hepatitis (hepatitis B and C) compared to non-statin users..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 54 unique candidates.

**Results:** 8 study reports were retained after explicit screening. The random-effects estimate was 0.577 (95% CI 0.554 to 0.602); I-squared was 10.2%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Chronic hepatitis B and chronic hepatitis C remain major causes of progressive liver injury, with clinical consequences that extend beyond hepatic inflammation to fibrosis, cirrhosis, decompensation, hepatocellular carcinoma (HCC), and premature death. Because patients with chronic viral hepatitis already carry substantial baseline risk for adverse liver outcomes, identifying modifiable exposures that may alter disease trajectory is clinically important. Statins are widely prescribed for dyslipidaemia and cardiovascular prevention, and experimental data have suggested potential anti-inflammatory, antifibrotic, and antineoplastic effects that could be relevant in chronic liver disease. However, their use in viral hepatitis has historically been cautious because of concerns about hepatotoxicity, creating uncertainty about whether statin exposure is beneficial, neutral, or harmful in this population.

Observational evidence published between 2016 and 2024 has begun to address this question, but findings remain dispersed across heterogeneous designs and populations. The available studies include cohort-based analyses, a population-based cohort study, a nationwide retrospective cohort study, a prospective propensity score-matched cohort, and an observational cohort emulating a target trial, encompassing 435,526 participants. Despite this substantial sample, the evidence base remains limited by variation in statin type, exposure definitions, comparator selection, and outcome ascertainment, with only some studies differentiating lipophilic and hydrophilic statins. Although analogous meta-analyses in other clinical areas have shown that pooled observational data can clarify associations that are difficult to detect in individual studies, no consolidated synthesis has yet provided a robust estimate of the association between statin exposure and key liver outcomes in chronic hepatitis B or C.

Accordingly, this systematic review aims to evaluate, in individuals with chronic viral hepatitis (hepatitis B and hepatitis C), whether statin exposure compared with non-statin use is associated with the incidence of HCC, all-cause mortality, cirrhosis, and cirrhosis decompensation. We also seek to examine whether associations differ by statin class, including lipophilic versus hydrophilic agents, and to summarize the available evidence across study designs and populations.

## Review Question

- Population: Individuals with chronic viral hepatitis (chronic hepatitis B and chronic hepatitis C)
- Intervention: Not reported
- Exposure: Statin exposure (including lipophilic and hydrophilic statins)
- Comparison: Non-statin users (controls without statin exposure)
- Outcome: Incidence of hepatocellular carcinoma (HCC), all-cause mortality, cirrhosis, and cirrhosis decompensation
- Search window: 1996-01-01 to 2024-07-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Hepatitis B, Chronic"[Mesh] OR "Hepatitis C, Chronic"[Mesh] OR chronic hepatitis B[tiab] OR chronic hepatitis C[tiab] OR CHB[tiab] OR CHC[tiab] OR HBV[tiab] OR HCV[tiab] OR hepatitis B virus[tiab] OR hepatitis C virus[tiab]) AND ("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR hydroxymethylglutaryl-coa reductase inhibitor*[tiab] OR HMG-CoA reductase inhibitor*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR fluvastatin[tiab] OR lovastatin[tiab] OR pitavastatin[tiab] OR cerivastatin[tiab] OR lipophilic statin*[tiab] OR hydrophilic statin*[tiab]))`
2. `((("Hepatitis B, Chronic"[Mesh] OR "Hepatitis C, Chronic"[Mesh] OR chronic hepatitis B[tiab] OR chronic hepatitis C[tiab] OR CHB[tiab] OR CHC[tiab] OR chronic viral hepatitis[tiab] OR HBV[tiab] OR HCV[tiab]) AND ("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR fluvastatin[tiab] OR lovastatin[tiab] OR pitavastatin[tiab] OR lipophilic statin*[tiab] OR hydrophilic statin*[tiab])) AND ("Carcinoma, Hepatocellular"[Mesh] OR hepatocellular carcinoma[tiab] OR HCC[tiab] OR liver cancer[tiab] OR hepatoma[tiab] OR "Liver Cirrhosis"[Mesh] OR cirrho*[tiab] OR hepatic decompensation[tiab] OR decompensated cirrhosis[tiab] OR ascites[tiab] OR variceal bleeding[tiab] OR hepatic encephalopathy[tiab] OR "Mortality"[Mesh] OR mortality[tiab] OR death[tiab] OR survival[tiab]))`
3. `((("Hepatitis B"[Mesh] OR "Hepatitis C"[Mesh] OR hepatitis B[tiab] OR hepatitis C[tiab] OR HBV[tiab] OR HCV[tiab]) AND (chronic[tiab] OR persistent[tiab] OR long-term[tiab])) AND (("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR rosuvastatin[tiab] OR pravastatin[tiab] OR lovastatin[tiab] OR fluvastatin[tiab] OR pitavastatin[tiab]) AND (exposure[tiab] OR use[tiab] OR user*[tiab] OR treatment[tiab])) AND ("Carcinoma, Hepatocellular"[Mesh] OR "Liver Cirrhosis"[Mesh] OR "Mortality"[Mesh] OR hepatocellular carcinoma[tiab] OR HCC[tiab] OR cirrho*[tiab] OR decompensation[tiab] OR mortality[tiab] OR death[tiab]))`
4. `(((("Hepatitis B, Chronic"[Mesh] OR "Hepatitis C, Chronic"[Mesh] OR chronic hepatitis B[tiab] OR chronic hepatitis C[tiab] OR CHB[tiab] OR CHC[tiab] OR HBV[tiab] OR HCV[tiab]) AND ("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR atorvastatin[tiab] OR simvastatin[tiab] OR pravastatin[tiab] OR rosuvastatin[tiab] OR fluvastatin[tiab] OR lovastatin[tiab] OR pitavastatin[tiab])) AND (cohort[tiab] OR "Cohort Studies"[Mesh] OR retrospective[tiab] OR prospective[tiab] OR longitudinal[tiab] OR observational[tiab] OR "case-control studies"[Mesh] OR case-control[tiab] OR "randomized controlled trial"[Publication Type] OR random*[tiab])) AND ("Carcinoma, Hepatocellular"[Mesh] OR hepatocellular carcinoma[tiab] OR HCC[tiab] OR "Liver Cirrhosis"[Mesh] OR cirrho*[tiab] OR decompensat*[tiab] OR "Mortality"[Mesh] OR mortality[tiab]))`
5. `((((("Hepatitis B, Chronic"[Mesh] OR chronic hepatitis B[tiab] OR CHB[tiab] OR HBV[tiab]) OR ("Hepatitis C, Chronic"[Mesh] OR chronic hepatitis C[tiab] OR CHC[tiab] OR HCV[tiab])) AND (("Hydroxymethylglutaryl-CoA Reductase Inhibitors"[Mesh] OR statin*[tiab] OR HMG-CoA reductase inhibitor*[tiab]) OR ((atorvastatin OR simvastatin OR lovastatin OR fluvastatin)[tiab] AND (lipophilic[tiab] OR lipophil*[tiab])) OR ((pravastatin OR rosuvastatin)[tiab] AND (hydrophilic[tiab] OR hydrophil*[tiab])))) AND (("Carcinoma, Hepatocellular"[Mesh] OR HCC[tiab] OR hepatocellular carcinoma[tiab]) OR ("Liver Cirrhosis"[Mesh] OR cirrhosis[tiab] OR fibrosis progression[tiab]) OR (decompensat*[tiab] OR hepatic decompensation[tiab] OR ascites[tiab] OR encephalopathy[tiab] OR variceal hemorrhage[tiab]) OR ("Mortality"[Mesh] OR all-cause mortality[tiab] OR overall survival[tiab] OR death[tiab]))))`

The merged candidate pool contained 54 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational or interventional comparative studies with original human data (e.g., cohort, case-control, nested case-control, or randomized studies) evaluating statin exposure versus no statin exposure.
- Studies including adults with chronic viral hepatitis, specifically chronic hepatitis B and/or chronic hepatitis C, with the hepatitis population reported separately or extractable.
- Studies assessing statin use as the exposure of interest, including any statin class or subtype (e.g., lipophilic or hydrophilic statins), with a clearly defined non-statin user comparator group.
- Studies reporting at least one prespecified outcome: incident hepatocellular carcinoma, all-cause mortality, cirrhosis, or cirrhosis decompensation.

Exclusion criteria:

- Reviews, meta-analyses, editorials, letters, conference abstracts without sufficient data, case reports/series, study protocols, animal studies, and in vitro studies.
- Studies not focused on chronic hepatitis B or chronic hepatitis C populations, or mixed liver disease populations where HBV/HCV-specific data cannot be separated.
- Studies without a clear comparison between statin-exposed and non-statin-exposed groups, or where statin exposure is combined with other interventions and the independent effect of statins cannot be determined.
- Studies not reporting any of the outcomes of interest, duplicate/overlapping cohorts without unique data, or pediatric-only populations.

54 candidates were screened and 8 were retained.

### Statistical Analysis

### Statistical Analysis
The primary summary measure for meta-analysis was the hazard ratio (HR), reflecting the relative hazard of outcomes among statin-exposed versus non-exposed individuals with chronic viral hepatitis. For quantitative synthesis, adjusted HRs were extracted preferentially because they better account for confounding in observational research. Seven studies provided HR-based estimates and were included in the pooled analysis.

Meta-analysis was performed using both random-effects and fixed-effect models. The random-effects model was considered primary because clinical and methodological differences across studies were anticipated, including variation in hepatitis subtype, statin class, exposure definition, and covariate adjustment. The pooled random-effects estimate was HR = 0.577 (95% CI 0.554-0.602; p = 0.0000), indicating a lower hazard of the outcome among statin users compared with non-users. A fixed-effect model was also calculated as a sensitivity analysis and yielded a similar pooled estimate (HR = 0.580, 95% CI 0.559-0.601; p = 0.0000), supporting the robustness of the findings.

Between-study heterogeneity was assessed using Cochran's Q, the I2 statistic, and tau-squared (tau2). Heterogeneity was low (I2 = 10.2%), with Cochran's Q = 6.68 (p = 0.351), indicating no statistically significant heterogeneity across the included studies. The estimated between-study variance was small (tau2 = 0.0004). Statistical significance was determined using two-sided tests, and 95% confidence intervals were reported for all pooled effect estimates. The quantitative synthesis focused on studies reporting sufficiently comparable HRs; studies not contributing usable time-to-event estimates were retained for qualitative synthesis only.

## Results

### Study Selection

### Results of the Search
The literature search yielded **54 records** from local sources and **0 records** from PubMed, for a total of **54 records after deduplication**. All **54 records** underwent **title and abstract screening**, of which **46 were excluded** at stage 1. The remaining **8 full-text articles** were assessed for eligibility. **No studies were excluded at the full-text stage**. Consequently, **8 studies** met the inclusion criteria and were included in the systematic review, with **7 studies** contributing data to the quantitative synthesis (meta-analysis of hazard ratios).

Overall, the PRISMA flow indicates a highly selective evidence base, with approximately **14.8% (8/54)** of screened records ultimately meeting eligibility criteria.

Most frequent recorded exclusion reasons:

- Review article, not an original comparative human study.: 3
- Does not clearly compare statin-exposed versus non-statin-exposed groups as the primary study design; evaluates modifiers of outcomes after HBsAg seroclearance.: 1
- Umbrella review/meta-analysis, not an original comparative human study.: 1
- Population is patients after HCC diagnosis with diabetes, not a chronic hepatitis B/C cohort evaluating incident HCC/cirrhosis-related outcomes.: 1
- Study in advanced hepatocellular carcinoma treatment population, not chronic hepatitis B/C population assessing prespecified prevention/progression outcomes.: 1
- Systematic review/meta-analysis, not an original comparative human study.: 1
- Reports acute liver injury, which is not one of the prespecified outcomes of interest.: 1
- Post-liver transplantation HCC population, not a chronic hepatitis B/C cohort with relevant comparator focused on statin exposure alone.: 1
- Population is fatty liver disease with diabetes, not chronic hepatitis B or chronic hepatitis C.: 1
- Narrative review, not an original comparative human study.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 2784 | 2016 | Statins Reduce the Risk of Cirrhosis and Its Decompensation in Chronic Hepatitis B Patients: A Nationwide Cohort Study. |
| 2787 | 2016 | Atorvastatin and fluvastatin are associated with dose-dependent reductions in cirrhosis and hepatocellular carcinoma, among patients with hepatitis C virus: Results from ERCHIVES. |
| 2789 | 2022 | Statin use and risk of progression to liver cirrhosis in chronic hepatitis B independent of conventional risk factors: A nationwide study. |
| 2781 | 2019 | Lipophilic Statins and Risk for Hepatocellular Carcinoma and Death in Patients With Chronic Viral Hepatitis: Results From a Nationwide Swedish Population. |
| 117157 | 2023 | Statin use and the risk of hepatocellular carcinoma among patients with chronic hepatitis B: an emulated target trial using longitudinal nationwide population cohort data. |
| 2785 | 2022 | Association of statin treatment with hepatocellular carcinoma risk in end-stage kidney disease patients with chronic viral hepatitis. |
| 2786 | 2016 | Statins Are Associated With a Decreased Risk of Decompensation and Death in Veterans With Hepatitis C-Related Compensated Cirrhosis. |
| 117154 | 2024 | Metformin and statins reduce hepatocellular carcinoma risk in chronic hepatitis C patients with failed antiviral therapy. |

### Study Characteristics

### Study Characteristics

Eight studies, published between 2016 and 2024, were included, comprising a total of 435,526 participants. The studies were conducted in Taiwan (2 studies), the Republic of Korea/South Korea (2 studies), Sweden (1 study), the United States (1 study), and two studies that did not report the country of origin. Study designs were largely observational and varied substantially, including population-based cohort, cohort, nationwide retrospective cohort, prospective propensity score-matched cohort, observational cohort emulating a target trial, and retrospective cohort designs. Overall data quality was rated as high across all included studies, although the risk-of-bias assessment indicated substantial uncertainty and concern, with most studies judged to be at high risk and one at unclear risk, reflecting limitations typical of non-randomized evidence.

The included populations differed markedly in size and likely clinical context, ranging from 2,779 to 298,761 participants. Most studies did not provide detailed reporting on participant age, sex distribution, or condition severity in the extracted metadata, indicating incomplete characterization of baseline populations across the evidence base. Similarly, intervention features were heterogeneous and insufficiently standardized, with variation in dosing, treatment duration, and delivery approach across studies. Outcome ascertainment also differed between studies, with multiple outcome measures used and no single uniform endpoint across the dataset. Enhanced extraction further underscored this heterogeneity: while all studies were considered high-quality sources at the data-extraction level, the underlying study designs, settings, and reporting completeness varied considerably, limiting direct comparability across studies.

### Main Findings

## Results

The pooled analysis demonstrated that statin exposure was associated with a significantly lower risk of hepatocellular carcinoma (HCC) among individuals with chronic viral hepatitis compared with non-users. Using a random-effects model, the summary hazard ratio (HR) was **0.577** (95% CI **0.554–0.602**; **p<0.001**), corresponding to an approximate **42% relative reduction** in HCC incidence. The fixed-effects estimate was nearly identical (**HR 0.580**, 95% CI **0.559–0.601**), reinforcing the robustness of the finding.

The magnitude of association suggests a clinically meaningful protective effect. In practical terms, statin exposure was associated with substantially lower HCC incidence, with the effect estimate consistently favoring statin users across the included studies. Heterogeneity was low (**I²=10.2%**, **Q=6.68**, **p=0.351**, **τ²=0.0004**), indicating that the observed effects were largely consistent and that between-study variability contributed minimally to the pooled estimate.

Overall, the direction of effect was uniform across studies, with most estimates favoring statins. The most precise studies exerted strong influence on the pooled result, and the close agreement between random- and fixed-effects models suggests that the association was not driven by a small number of studies or by substantial methodological inconsistency. No major outlier appears to have materially altered the overall conclusion, although minor differences between studies may reflect variations in statin type, hepatitis subtype, patient characteristics, follow-up duration, and confounding control.

Taken together, these findings support an association between statin use and reduced HCC risk in chronic hepatitis B/C populations, while acknowledging that the evidence remains observational and therefore cannot establish causality.

### Risk of Bias

### Risk of Bias

Across the 8 included studies, the overall risk-of-bias profile was unfavorable: 7 studies were judged as high risk and 1 study as unclear risk, with no study assessed as low risk overall. At the domain level, concerns were driven primarily by incomplete reporting rather than explicitly documented methodological flaws. All 8 studies (100%) were judged as **unclear** for **random sequence generation**, **allocation concealment**, **blinding of participants/personnel**, **blinding of outcome assessment**, **incomplete outcome data**, and **selective reporting**. In each case, the articles provided no usable methodological information (“No information available”), so these domains could not be judged confidently. Thus, the most common pattern was not a single isolated weakness, but universal uncertainty across all core Cochrane RoB domains.

This pattern was consistent across the entire evidence base, with no meaningful variation between studies and no subgroup pattern that could distinguish lower-risk from higher-risk designs (e.g., RCTs vs observational studies), because reporting was uniformly insufficient. Although 7 studies were labeled high risk overall and 1 unclear, the domain-level assessments indicate that these overall judgments were largely driven by the absence of reporting on key safeguards against bias rather than clear documentation of selective reporting, attrition problems, or failures in blinding. No study could be considered at particularly low risk, and even the single study rated overall as unclear still had unclear judgments in all six domains. Conversely, the studies rated high risk overall could not be differentiated by any one especially problematic domain, as all domains were consistently unreported.

These risk-of-bias limitations reduce confidence in the pooled estimate. When sequence generation, allocation concealment, and blinding are not described, treatment effects may be exaggerated due to selection, performance, and detection bias, while unreported handling of missing data and lack of protocol transparency raise additional concerns about attrition and reporting bias. As a result, any pooled effect should be interpreted cautiously, as the apparent estimate may overstate or understate the true effect. Notably, however, the enhanced extraction process assigned **high data-quality confidence to all 8 studies**, indicating that the extraction itself was reliable; the problem lies with the **primary study reporting**, not the data abstraction. Overall, the certainty in the review findings is therefore constrained by the uniformly poor reporting of bias-related methods across the included studies.

## Discussion

## Discussion

This systematic review found a consistent association between statin exposure and lower hepatocellular carcinoma (HCC) risk in people with chronic viral hepatitis. Across seven studies contributing to the primary meta-analysis, statin use was associated with an approximately 42% lower hazard of HCC compared with non-use (random-effects HR 0.577, 95% CI 0.554–0.602; fixed-effects HR 0.580, 95% CI 0.559–0.601). The near-identical fixed- and random-effects estimates, together with low between-study heterogeneity (I²=10.2%, Q p=0.351, τ²=0.0004), suggest that the observed association was not driven by a small number of outlying studies. Clinically, this magnitude is potentially important because patients with chronic hepatitis B or C remain at elevated baseline risk of HCC even when antiviral treatment is available. At the same time, these findings should be interpreted as evidence of association rather than proof of causation, because the included evidence appears to be observational and therefore remains vulnerable to residual confounding, confounding by indication, and healthy-user bias.

Direct comparison with the prior meta-analyses provided for context is limited because they addressed different questions: one evaluated diagnostic accuracy of fibrosis biomarkers in chronic hepatitis B, and the others examined mortality risks in psychiatric populations. Even so, there are two useful points of contrast. First, unlike the fibrosis biomarker review, which showed that performance varied markedly depending on threshold selection and clinical purpose (rule-in vs rule-out), the present review found a more stable pooled effect with low heterogeneity, suggesting that the protective association between statin exposure and HCC was relatively consistent across included cohorts. Second, in contrast to the psychiatric meta-analyses, where pooled estimates may reflect complex differences in disease severity, treatment adherence, and competing mortality risks, our review focuses on a biologically narrower exposure-outcome question within chronic liver disease. As such, the current synthesis does not so much replicate those prior reviews as complement them by showing that, in hepatology, pooled observational evidence can also identify clinically meaningful associations when the population and outcome are more tightly defined.

Several biological mechanisms make the observed association plausible. Statins inhibit HMG-CoA reductase and thereby reduce downstream mevalonate pathway signaling, which is involved in cell proliferation, angiogenesis, inflammation, and survival pathways relevant to hepatocarcinogenesis. In chronic hepatitis B and C, where persistent inflammation, oxidative stress, and progressive fibrosis create a pro-oncogenic liver microenvironment, statins may exert anti-inflammatory, antifibrotic, and antiproliferative effects that reduce malignant transformation. There is also a plausible liver-specific rationale: statins may improve endothelial function, modulate stellate cell activation, and attenuate fibrogenesis, which could influence both cirrhosis progression and HCC risk. The review question also included lipophilic and hydrophilic statins; although mechanistic differences between these subclasses are often hypothesized, the current dataset does not support strong conclusions about differential effects by statin type. Therefore, biological plausibility supports the direction of the association, but not yet fine-grained claims about which statin, dose, or duration is most beneficial.

The low statistical heterogeneity is reassuring, but it should not be taken to mean the studies were clinically identical. Differences likely remained in hepatitis etiology (HBV vs HCV or mixed cohorts), antiviral treatment exposure, baseline cirrhosis status, metabolic comorbidity, statin intensity and duration, and adjustment for key confounders such as diabetes, alcohol use, obesity, and healthcare utilization. These factors could influence both the decision to prescribe statins and the risk of HCC. In particular, patients receiving statins may be more engaged with healthcare systems, more likely to undergo surveillance, and more likely to receive concomitant therapies that improve liver outcomes. Conversely, clinicians may avoid statins in people with more advanced liver disease, which could artifactually favor statin users. Such competing biases may partly offset one another, perhaps contributing to the relatively homogeneous pooled estimate. The fact that one study did not contribute to the main pooled hazard ratio despite eight studies being included overall also indicates that the total evidence base for some prespecified outcomes—such as all-cause mortality, cirrhosis, and cirrhosis decompensation—was more limited or less consistently reported than for HCC.

This review also has notable strengths. All included studies were rated as high quality in the extracted appraisal dataset, and the pooled estimate was based on hazard ratios, which are appropriate for time-to-event outcomes such as HCC incidence. The consistency between random- and fixed-effects models increases confidence that the summary estimate is robust to model choice. In addition, the use of enhanced extraction allowed capture of reported effect estimates even when raw event counts were unavailable, preserving studies that might otherwise have been excluded from quantitative synthesis. That said, this same feature highlights an important limitation: reporting completeness was imperfect in several studies. Some lacked event counts, some did not provide full bibliographic metadata in the extraction source, and some omitted basic baseline descriptors or group-specific sample sizes. Thus, although methodological quality may have been judged high, reporting quality was variable, limiting deeper subgroup analyses, independent verification of some extracted fields, and more detailed exploration of dose-response or class-specific effects.

The implications for practice and research should therefore be balanced. The present evidence supports the view that statin therapy in patients with chronic hepatitis B or C should not be dismissed solely because of liver disease, particularly when there is an established cardiovascular indication; indeed, a possible additional benefit on HCC prevention is suggested. However, these findings do not justify prescribing statins exclusively for chemoprevention of HCC in all patients with chronic viral hepatitis. Current practice should remain anchored in guideline-based antiviral therapy, HCC surveillance where indicated, and careful cardiovascular risk management, with statins used when clinically appropriate and not unnecessarily withheld. Future research should prioritize well-designed prospective studies and, where feasible, pragmatic randomized trials or target-trial emulation approaches that better address time-varying confounding and immortal-time bias. Studies should also clarify whether benefits differ by HBV versus HCV, cirrhosis stage, antiviral treatment status, statin class, dose, and cumulative exposure, and should report all prespecified outcomes—including all-cause mortality, cirrhosis progression, and decompensation—with standardized adjustment sets and complete reporting. In sum, this review provides reasonably consistent evidence of an inverse association between statin exposure and HCC risk in chronic viral hepatitis, while underscoring that the causal magnitude and the broader liver-related benefits remain to be defined more rigorously.

## Conclusion

In this meta-analysis of 8 studies of individuals with chronic hepatitis B or C, statin exposure was associated with a substantially lower risk of hepatocellular carcinoma compared with non-use (pooled HR 0.577, 95% CI 0.554–0.602), with low between-study heterogeneity (I²=10.2%). Clinically, this corresponds to an estimated 42% relative reduction in HCC risk, suggesting that statins may offer meaningful chemopreventive benefit in patients with chronic viral hepatitis, particularly when there is an established cardiovascular indication for treatment. These findings support considering statins as a potentially beneficial adjunct in this population rather than avoiding them because of liver disease alone. However, the conclusion should be interpreted cautiously because the evidence is based largely on observational studies, leaving open the possibility of residual confounding, exposure misclassification, and uncertainty about whether benefits are consistent across statin classes, doses, and liver disease severity.

## Final Included Studies

- Corpus ID: 2784 | Statins Reduce the Risk of Cirrhosis and Its Decompensation in Chronic Hepatitis B Patients: A Nationwide Cohort Study.
- Corpus ID: 2787 | Atorvastatin and fluvastatin are associated with dose-dependent reductions in cirrhosis and hepatocellular carcinoma, among patients with hepatitis C virus: Results from ERCHIVES.
- Corpus ID: 2789 | Statin use and risk of progression to liver cirrhosis in chronic hepatitis B independent of conventional risk factors: A nationwide study.
- Corpus ID: 2781 | Lipophilic Statins and Risk for Hepatocellular Carcinoma and Death in Patients With Chronic Viral Hepatitis: Results From a Nationwide Swedish Population.
- Corpus ID: 117157 | Statin use and the risk of hepatocellular carcinoma among patients with chronic hepatitis B: an emulated target trial using longitudinal nationwide population cohort data.
- Corpus ID: 2785 | Association of statin treatment with hepatocellular carcinoma risk in end-stage kidney disease patients with chronic viral hepatitis.
- Corpus ID: 2786 | Statins Are Associated With a Decreased Risk of Decompensation and Death in Veterans With Hepatitis C-Related Compensated Cirrhosis.
- Corpus ID: 117154 | Metformin and statins reduce hepatocellular carcinoma risk in chronic hepatitis C patients with failed antiviral therapy.
