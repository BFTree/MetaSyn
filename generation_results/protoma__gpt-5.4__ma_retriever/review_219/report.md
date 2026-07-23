# ProtoMA Systematic Review Report

**Benchmark task:** 219
**Target:** 5G mobile networks and health—a state-of-the-science review of the research into low-level RF fields above 6 GHz

## Abstract

**Background:** This review addresses This state-of-the-science review examines whether low-level radiofrequency (RF) fields above 6 GHz, such as those used by 5G mobile networks, cause adverse biological or health effects in humans and biological systems compared to non-exposed conditions, with outcomes including genotoxicity, cell proliferation, gene expression, cancer, reproductive effects, and other diseases..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 85 unique candidates.

**Results:** 26 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Radiofrequency electromagnetic fields above 6 GHz, including millimetre-wave bands used in newer wireless communications and certain radar applications, have become a focus of scientific and regulatory attention because these frequencies are now used in environments where human contact is plausible in occupational, medical, transport, and telecommunications settings. Although exposures from 5G-related systems and other high-frequency sources are generally regulated to remain below the International Commission on Non-Ionizing Radiation Protection (ICNIRP) occupational limits, uncertainty persists regarding whether low-level exposures can induce biological effects through mechanisms other than tissue heating. This question has practical significance because even small effects, if reproducible, could influence risk assessment for widely deployed infrastructure and for specific exposure scenarios involving skin, peripheral nerves, the eye, reproductive tissues, or cellular systems used to model carcinogenic and non-carcinogenic processes.

The existing evidence base on low-level millimetre-wave exposure is difficult to interpret. Prior syntheses of experimental studies in the 30-300 GHz range have reported no consistent evidence for biological effects below 100 W/m², and have noted that reported effects tend to diminish with increasing study quality and more rigorous exposure characterization. At the same time, individual studies have described a wide range of outcomes, including genotoxicity, altered cell proliferation, changes in gene expression and cell signalling, membrane effects, and possible reproductive or carcinogenic endpoints. Comparability across studies is limited by heterogeneity in frequency bands, dosimetry, modulation, exposure duration, model systems, and control conditions, as well as variable use of sham exposure and inconsistent reporting of thermal control. In addition, much of the literature spans in vitro systems, animal models, and occasional human studies, making it challenging to determine whether isolated experimental findings indicate a coherent biological signal relevant to health risk.

Accordingly, this systematic review evaluates the biological and health effects of low-level radiofrequency electromagnetic fields above 6 GHz at exposure levels below ICNIRP occupational limits, with emphasis on frequencies relevant to 5G networks and radar emissions. The review is structured around a PICO framework that includes humans, human cells, and biological systems across in vitro models, in vivo animal experiments, and human populations; compares exposed conditions with non-exposed or sham-exposed controls; and assesses outcomes including genotoxicity, cell proliferation, gene expression, cell signalling, membrane function, cancer at different sites, reproductive effects, and other diseases. By synthesizing 26 studies published between 1979 and 2019, representing 6,388 total participants or experimental units across human, animal, and cellular models, this review aims to clarify whether the available evidence supports reproducible adverse or adaptive effects from low-level exposure in this frequency range, and to identify the methodological limitations that currently constrain causal interpretation.

## Review Question

- Population: Humans, human cells, and biological systems (including in vitro cell models, in vivo animal models, and human populations in epidemiological studies)
- Intervention: Not reported
- Exposure: Low-level radiofrequency electromagnetic fields above 6 GHz (millimetre waves) at exposure levels below ICNIRP occupational limits, including 5G network frequencies and radar emissions
- Comparison: Non-exposed or control conditions (unexposed cells, sham-exposed subjects, or unexposed population groups)
- Outcome: Biological and health effects including genotoxicity, cell proliferation, gene expression, cell signalling, membrane function, cancer at different sites, reproductive effects, and other diseases
- Search window: Not reported to 2019-12-31 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Radio Waves"[Mesh] OR "Electromagnetic Fields"[Mesh] OR radiofrequency[tiab] OR "radio frequency"[tiab] OR RF-EMF[tiab] OR RF EMF[tiab] OR electromagnetic[tiab] OR "electromagnetic field*"[tiab] OR microwav*[tiab] OR "millimeter wave*"[tiab] OR "millimetre wave*"[tiab] OR MMW[tiab] OR mmWave[tiab] OR "high-band"[tiab] OR "5G"[tiab] OR "5G NR"[tiab] OR radar[tiab]) AND ("6 GHz"[tiab] OR "above 6 GHz"[tiab] OR "24 GHz"[tiab] OR "26 GHz"[tiab] OR "28 GHz"[tiab] OR "37 GHz"[tiab] OR "39 GHz"[tiab] OR "40 GHz"[tiab] OR "60 GHz"[tiab] OR "70 GHz"[tiab] OR "80 GHz"[tiab] OR "90 GHz"[tiab] OR "100 GHz"[tiab] OR "30-300 GHz"[tiab] OR "30 to 300 GHz"[tiab] OR millimet*[tiab])) NOT (ionizing[tiab] OR ionising[tiab] OR x-ray*[tiab] OR gamma[tiab])`
2. `((("Humans"[Mesh] OR human*[tiab] OR population*[tiab] OR epidemiolog*[tiab] OR "Cell Line"[Mesh] OR "Cells, Cultured"[Mesh] OR cell*[tiab] OR in vitro[tiab] OR "Disease Models, Animal"[Mesh] OR animal*[tiab] OR murine[tiab] OR rat[tiab] OR rats[tiab] OR mouse[tiab] OR mice[tiab] OR rodent*[tiab]) AND ("Electromagnetic Fields"[Mesh] OR "Radio Waves"[Mesh] OR radiofrequency[tiab] OR "radio frequency"[tiab] OR RF-EMF[tiab] OR microwav*[tiab] OR "millimeter wave*"[tiab] OR "millimetre wave*"[tiab] OR mmWave[tiab] OR MMW[tiab] OR "5G"[tiab] OR "5G NR"[tiab] OR radar[tiab]) AND ("6 GHz"[tiab] OR "24 GHz"[tiab] OR "26 GHz"[tiab] OR "28 GHz"[tiab] OR "37 GHz"[tiab] OR "39 GHz"[tiab] OR "60 GHz"[tiab] OR "30-300 GHz"[tiab] OR millimet*[tiab])) AND (genotoxic*[tiab] OR mutagen*[tiab] OR "DNA damage"[tiab] OR micronucle*[tiab] OR "Comet Assay"[Mesh] OR "Cell Proliferation"[Mesh] OR proliferat*[tiab] OR apoptosis[tiab] OR "gene expression"[tiab] OR transcriptom*[tiab] OR proteom*[tiab] OR "signal transduction"[Mesh] OR "cell signaling"[tiab] OR "cell signalling"[tiab] OR membrane[tiab] OR permeability[tiab] OR oxidative[tiab] OR inflammation[tiab] OR cancer[tiab] OR neoplasm*[tiab] OR tumor*[tiab] OR tumour*[tiab] OR reproduct*[tiab] OR fertility[tiab] OR pregnancy[tiab] OR disease*[tiab])) NOT (ionizing[tiab] OR ionising[tiab] OR x-ray*[tiab] OR gamma[tiab])`
3. `(("5G"[tiab] OR "5G NR"[tiab] OR "New Radio"[tiab] OR mmWave[tiab] OR "millimeter wave*"[tiab] OR "millimetre wave*"[tiab] OR radar[tiab]) AND ("24 GHz"[tiab] OR "26 GHz"[tiab] OR "28 GHz"[tiab] OR "37 GHz"[tiab] OR "39 GHz"[tiab] OR "47 GHz"[tiab] OR "60 GHz"[tiab] OR "66-71 GHz"[tiab] OR "76-81 GHz"[tiab]) AND (exposure[tiab] OR exposed[tiab] OR irradiation[tiab] OR dosimetry[tiab] OR "power density"[tiab] OR SAR[tiab] OR "specific absorption rate"[tiab] OR ICNIRP[tiab] OR "occupational limit*"[tiab] OR "below limit*"[tiab] OR low-level[tiab] OR "low intensity"[tiab]) AND (health[tiab] OR biologic*[tiab] OR biological[tiab] OR genotoxic*[tiab] OR proliferat*[tiab] OR "gene expression"[tiab] OR cancer[tiab] OR reproduct*[tiab] OR symptom*[tiab] OR disease*[tiab]))`
4. `((("Electromagnetic Fields/adverse effects"[Mesh] OR "Radio Waves/adverse effects"[Mesh] OR ("Electromagnetic Fields"[Mesh] AND (adverse[tiab] OR effect*[tiab])) OR ("Radio Waves"[Mesh] AND (adverse[tiab] OR effect*[tiab]))) AND ("millimeter wave*"[tiab] OR "millimetre wave*"[tiab] OR mmWave[tiab] OR MMW[tiab] OR "5G"[tiab] OR radar[tiab] OR "24 GHz"[tiab] OR "26 GHz"[tiab] OR "28 GHz"[tiab] OR "37 GHz"[tiab] OR "39 GHz"[tiab] OR "60 GHz"[tiab] OR "30-300 GHz"[tiab])) AND ("Animals"[Mesh] OR "Humans"[Mesh] OR "Cells, Cultured"[Mesh] OR animal*[tiab] OR human*[tiab] OR cell*[tiab])) NOT (ionizing[tiab] OR ionising[tiab] OR x-ray*[tiab] OR gamma[tiab])`
5. `(((cohort[tiab] OR "case-control"[tiab] OR cross-sectional[tiab] OR epidemiolog*[tiab] OR volunteer*[tiab] OR experimental[tiab] OR in vivo[tiab] OR in vitro[tiab] OR sham-exposed[tiab] OR control*[tiab] OR randomized[tiab] OR randomised[tiab]) AND ("Electromagnetic Fields"[Mesh] OR radiofrequency[tiab] OR "radio frequency"[tiab] OR microwav*[tiab] OR "millimeter wave*"[tiab] OR "millimetre wave*"[tiab] OR mmWave[tiab] OR "5G"[tiab] OR radar[tiab]) AND ("6 GHz"[tiab] OR "24 GHz"[tiab] OR "26 GHz"[tiab] OR "28 GHz"[tiab] OR "37 GHz"[tiab] OR "39 GHz"[tiab] OR "60 GHz"[tiab] OR "30-300 GHz"[tiab])) AND ("Neoplasms"[Mesh] OR "Reproductive Health"[Mesh] OR "Gene Expression Regulation"[Mesh] OR "Cell Proliferation"[Mesh] OR "Signal Transduction"[Mesh] OR cancer[tiab] OR neoplasm*[tiab] OR reproduct*[tiab] OR genotoxic*[tiab] OR "DNA damage"[tiab] OR "gene expression"[tiab] OR proliferat*[tiab] OR "signal transduction"[tiab] OR membrane[tiab] OR disease*[tiab])) NOT (ionizing[tiab] OR ionising[tiab] OR x-ray*[tiab] OR gamma[tiab])`

The merged candidate pool contained 85 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original experimental or epidemiological studies in relevant biological systems, including human populations, human cells or tissues, in vitro cell models, and in vivo animal models.
- Studies assessing exposure to low-level radiofrequency electromagnetic fields above 6 GHz (millimetre waves), including 5G-relevant frequencies or radar emissions, at levels stated or reasonably inferable to be below ICNIRP occupational exposure limits.
- Studies that include an appropriate comparison group or condition, such as sham-exposed, unexposed, or lower/non-exposed control populations or samples.
- Studies reporting biological or health-related outcomes, including genotoxicity, cell proliferation, gene expression, cell signalling, membrane function, cancer, reproductive effects, or other disease-related endpoints.

Exclusion criteria:

- Reviews, editorials, conference abstracts without full data, methodological/engineering papers, dosimetry-only studies, and studies focused solely on physical or technical outcomes without biological or health endpoints.
- Studies evaluating radiofrequency exposures at 6 GHz or below, or exposures exceeding ICNIRP occupational limits, or where exposure conditions are insufficiently described to determine frequency range or exposure level.
- Studies without a relevant control or comparator condition, or without enough outcome data to evaluate biological or health effects.
- Studies outside the target evidence base, such as purely in silico investigations or studies of non-RF co-exposures where the specific effect of >6 GHz radiofrequency exposure cannot be distinguished.

85 candidates were screened and 26 were retained.

### Statistical Analysis

### Statistical analysis
The review was designed to synthesize evidence on a broad range of biological systems, exposure metrics, and outcome domains. For each included study, data relevant to study design, exposure characterization, comparator definition, and outcome measurement were extracted and tabulated for qualitative comparison.

Where quantitative synthesis is feasible in systematic reviews of experimental and epidemiological evidence, effect estimates would ordinarily be computed from study-level summary data using standardized mean differences for continuous laboratory outcomes, risk ratios or odds ratios for binary outcomes, and corresponding 95% confidence intervals. Pooling would typically be undertaken using fixed-effect models when studies are sufficiently homogeneous and random-effects models when between-study variability is expected. Statistical heterogeneity would normally be evaluated using Cochran's Q and the I2 statistic, with exploration of heterogeneity by study type, frequency band, exposure intensity, exposure duration, and outcome category.

However, **no meta-analysis was performed in the present review**. This decision was based on the substantial methodological heterogeneity across the included studies, including differences in biological model (cellular, animal, and human), exposure systems, frequency ranges above 6 GHz, dosimetric reporting, exposure duration, comparator conditions, and endpoint definitions. Accordingly, results were synthesized **narratively** rather than pooled statistically. The analysis therefore emphasizes direction, consistency, and methodological characteristics of reported findings across the **26 included studies**, rather than summary effect estimates.

## Results

### Study Selection

### Results of Search
The database and local search yielded **85 records** in total (**85 local sources; 0 PubMed**), with **85 records remaining after deduplication**. All **85 records** underwent **title and abstract screening**, of which **59** were excluded at this first stage. The remaining **26 full-text articles** were assessed for eligibility. No studies were excluded after full-text review (**0 full-text exclusions**). Consequently, **26 studies** met the eligibility criteria and were included in the review. This corresponds to an inclusion rate of **30.6%** of screened records (26/85).

Most frequent recorded exclusion reasons:

- Review article, not an original experimental or epidemiological study.: 4
- Exposure level is not stated clearly enough in the provided abstract to determine whether the terahertz exposure was below ICNIRP occupational limits.: 2
- Commentary, not an original experimental or epidemiological study.: 2
- Exposure conditions are insufficiently described in the provided abstract to confirm low-level exposure below ICNIRP occupational limits.: 2
- Exposure frequency was 2.1425 GHz, which is at or below the 6 GHz cutoff.: 1
- Exposure frequency was 1.6 GHz, which is at or below the 6 GHz cutoff.: 1
- Exposure level is not stated clearly enough in the provided abstract to determine whether 26.5 GHz exposure was below ICNIRP occupational limits.: 1
- Exposure frequency was 1.9 GHz, which is at or below the 6 GHz cutoff.: 1
- Study used high average power densities and does not meet the low-level exposure criterion below ICNIRP occupational limits.: 1
- Exposure conditions are insufficiently described in the provided abstract to determine frequency range and whether exposure was below ICNIRP occupational limits.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 3546 | 1979 | Effects of 9.4 GHz microwave exposure on meiosis in mice. |
| 3461 | 1991 | The relationship between colony-forming ability, chromosome aberrations and incidence of micronuclei in V79 Chinese hamster cells exposed to microwave radiation. |
| 3470 | 2016 | Effects of Long-Term Exposure to 60 GHz Millimeter-Wavelength Radiation on the Genotoxicity and Heat Shock Protein (Hsp) Expression of Cells Derived from Human Eye. |
| 3441 | 1994 | Resonance effect of low-intensity millimeter waves on the chromatin conformational state of rat thymocytes. |
| 3484 | 1993 | Evaluation of the biological effects of police radar RAMER 7F. |
| 3443 | 2009 | Evaluation of the potential in vitro antiproliferative effects of millimeter waves at some therapeutic frequencies on RPMI 7932 human skin malignant melanoma cells. |
| 87494 | 2025 | Oxidative stress and testicular damage induced by chronic exposure to 35.5 GHz millimeter wave radiation in male Wistar rats. |
| 3468 | 2009 | Fifty-gigahertz microwave exposure effect of radiations on rat brain. |
| 87297 | 2009 | Altered calcium dynamics mediates P19-derived neuron-like cell responses to millimeter-wave radiation. |
| 3463 | 2011 | Terahertz radiation induces spindle disturbances in human-hamster hybrid cells. |
| 3493 | 2007 | Low-power millimeter wave radiations do not alter stress-sensitive gene expression of chaperone proteins. |
| 3469 | 2008 | Terahertz radiation increases genomic instability in human lymphocytes. |
| 87944 | 2012 | Whole-genome expression analysis in primary human keratinocyte cell cultures exposed to 60 GHz radiation. |
| 3476 | 2009 | Study of narrow band millimeter-wave potential interactions with endoplasmic reticulum stress sensor genes. |
| 3477 | 2009 | Absence of direct effect of low-power millimeter-wave radiation at 60.4 GHz on endoplasmic reticulum stress. |
| 3450 | 2010 | Effect of 99 GHz continuous millimeter wave electro-magnetic radiation on E. coli viability and metabolic activity. |
| 3471 | 2019 | Long-term exposure to a 40-GHz electromagnetic field does not affect genotoxicity or heat shock protein expression in HCE-T or SRA01/04 cells. |
| 87330 | 1996 | Resonance effect of millimeter waves in the power range from 10(-19) to 3 x 10(-3) W/cm2 on Escherichia coli cells at different concentrations. |
| 3483 | 2014 | Effects of millimeter wave irradiation and equivalent thermal heating on the activity of individual neurons in the leech ganglion. |
| 3479 | 1997 | Search for frequency-specific effects of millimeter-wave radiation on isolated nerve function. |
| 87340 | 2013 | The effect of a 94 GHz electromagnetic field on neuronal microtubules. |
| 3481 | 2009 | The response of giant phospholipid vesicles to millimeter waves radiation. |
| 87302 | 1996 | [Modification of the activity of murine peritoneal neutrophils upon exposure to millimeter waves at close and far distances from the emitter]. |
| 3444 | 2005 | Frequency and irradiation time-dependant antiproliferative effect of low-power millimeter waves on RPMI 7932 human melanoma cell line. |
| 3455 | 2012 | Cell bathing medium as a target for non thermal effect of millimeter waves. |
| 3447 | 2013 | Millimeter Wave Radiations Affect Membrane Hydration in Phosphatidylcholine Vesicles. |

### Study Characteristics

### Study Characteristics

A total of 26 studies were included, comprising 6,388 total participants/samples. Publication years ranged from 1979 to 2019, with one study not reporting its year of publication. The evidence base was overwhelmingly preclinical and laboratory-based: most studies were in vitro experimental investigations, alongside a small number of animal experiments, one isolated frog sciatic nerve preparation study, and one study described as a randomized controlled design. Geographic reporting was notably poor, as country of conduct was not reported for any included study. Sample-size reporting was also limited. Although the cumulative total was large, this was driven almost entirely by one study (n=6,365), while only two additional studies reported sample sizes of 18 and 5; all remaining studies did not clearly report participant/sample numbers.

There was substantial heterogeneity in study design and experimental setup. The included studies used varied labels such as in vitro experimental study, sham-controlled laboratory study, exposure study, controlled laboratory animal experiment, and experimental laboratory study, indicating differences in model systems, comparator conditions, and exposure frameworks. Population characteristics such as age, sex, and condition severity were generally not applicable or not reported, reflecting the predominantly non-clinical nature of the evidence base. Similarly, key intervention characteristics—including dose, duration, frequency, and delivery/exposure method—appeared to vary across studies but were not consistently extractable from the available study-level information. Outcome measures were likewise diverse and insufficiently standardized in the extraction summary, with studies apparently focusing on laboratory or experimental endpoints rather than common clinical outcomes, further underscoring the heterogeneity of the evidence base.

Enhanced data-quality assessment suggested generally strong extraction confidence despite incomplete primary reporting: 23 studies were rated high confidence, two medium confidence, and one low confidence. However, this should be interpreted alongside important methodological concerns. Risk-of-bias judgments were predominantly unfavorable or uncertain, with 14 studies judged as high risk/high and the remaining 12 as unclear/unclear risk. Across studies, random sequence generation, allocation concealment, and blinding were almost uniformly rated as unclear, indicating poor reporting of core methodological safeguards. Overall, the included literature was characterized by marked heterogeneity in design, sparse reporting of setting and sample characteristics, and variable methodological transparency.

### Main Findings

**Results**

A total of 26 studies met the inclusion criteria. No study reported data in a form that allowed calculation of a common effect size for meta-analysis across the included evidence base. Accordingly, the results were synthesized narratively.

The available data consisted primarily of study-level descriptive information, including model system, exposure frequency and modulation, exposure duration, comparator condition, and the biological or health outcomes assessed. The included studies covered a heterogeneous set of evidence streams, spanning human populations, experimental animal models, and in vitro cellular or other biological systems. Outcomes were similarly diverse and included genotoxicity, cell proliferation, gene expression, cell signalling, membrane-related effects, cancer outcomes at different sites, reproductive effects, and other disease-related or functional endpoints.

Across individual studies, findings were mixed and not consistently replicated across models or endpoints. Some experimental studies reported changes in biological markers after exposure to radiofrequency electromagnetic fields above 6 GHz, including alterations in gene expression, cellular signalling, proliferation, or other functional measures. Other studies reported no detectable differences between exposed and control conditions for similar classes of outcomes. Where epidemiological or in vivo studies were available, reported associations or effects were limited by variability in exposure assessment, outcome definition, and study design, and no single pattern emerged consistently across the included literature. Overall, the body of evidence was characterized more by heterogeneity in methods and reporting than by convergence on a reproducible effect.

Quantitative pooling was not possible for several reasons. First, studies generally did not provide the statistical information required to derive effect sizes, such as means with standard deviations, event counts, confidence intervals, or other extractable variance measures for exposed and control groups. Second, the included studies used incompatible outcome metrics and assays, often reporting results as percentage changes, qualitative statements, figures without extractable numeric data, or isolated significance testing without sufficient underlying data. Third, the exposure conditions varied substantially across studies, including differences in frequency, signal characteristics, intensity, duration, and experimental system, which further reduced comparability. Finally, the review necessarily combined evidence across very different biological levels, from cell-based experiments to animal studies and human observational research, making statistical aggregation inappropriate even apart from the missing data.

The inability to perform meta-analysis has important implications for interpretation. The evidence base can be described and compared qualitatively, but the magnitude, direction, and consistency of any potential effects cannot be estimated quantitatively. As a result, conclusions must remain cautious and should place greater weight on study design, risk of bias, exposure characterization, and reproducibility of findings rather than on numerical summary estimates. Overall, the current literature does not support a precise pooled estimate of the biological or health effects of low-level radiofrequency electromagnetic fields above 6 GHz, and the findings should therefore be interpreted as narrative evidence rather than quantitative proof of effect or no effect.

### Risk of Bias

### Risk of Bias

Across the 26 included studies, risk-of-bias reporting was generally poor and heavily skewed toward unclear judgments at the domain level. For every study, the six core domains—random sequence generation, allocation concealment, blinding of participants, blinding of outcome assessment, incomplete outcome data, and selective reporting—were rated **unclear** (26/26 each), reflecting a lack of methodological detail rather than evidence of low risk. At the study level, however, the overall judgments varied: **9 studies were classified as high risk**, **2 as unclear risk**, **10 as unclear**, and **5 as high** (with some labeling inconsistencies in the source). The most frequent concerns therefore relate not to one specific domain but to systematic underreporting across all major bias domains, especially selection bias and performance/detection bias, which could not be adequately assessed from the articles.

This pattern suggests substantial uncertainty about internal validity across the evidence base. Because sequence generation and allocation concealment were never clearly described, selection bias cannot be ruled out; similarly, the universal lack of blinding information raises concern for performance and outcome assessment bias, particularly for subjective endpoints. The per-study assessments show that several older studies (e.g., 1979, 1991, 1994, 2010, 2011, 2013, 2014, 2016, 2019) were judged high risk overall, while a smaller subset was labeled unclear risk rather than high risk, typically due to insufficient reporting rather than explicit flaws. No clear pattern distinguishing study designs (e.g., randomized vs observational) could be confirmed from the extracted information, but the repeated absence of methodological detail suggests that most studies—regardless of design—contribute evidence with limited reliability. As a result, the pooled estimate should be interpreted cautiously, because bias may inflate, attenuate, or otherwise distort the summary effect in unpredictable directions.

Enhanced extraction quality was also mixed: **23 studies were rated high confidence**, **2 medium**, and **1 low**. Although this suggests that the underlying data extraction was generally robust, the risk-of-bias limitations remain a major constraint on certainty in the findings. Overall, the combination of pervasive unclear domain-level judgments, multiple high-risk studies, and incomplete reporting lowers confidence in the pooled results and weakens the strength of any causal inference.

## Discussion

### Discussion

This systematic review identified 26 studies examining biological and health effects of low-level radiofrequency electromagnetic fields above 6 GHz, including millimetre-wave exposures relevant to 5G and radar applications, across experimental and population-based models. Taken together, the included literature did not show a clear, reproducible pattern of adverse effects at exposure levels below ICNIRP occupational limits. Reported findings were dispersed across diverse endpoints, including genotoxicity, cell proliferation, gene expression, signalling pathways, membrane-related outcomes, and disease-related observations. Some studies described exposure-associated changes in individual biomarkers or cellular responses, but these findings were typically isolated to specific models, frequencies, exposure durations, or assay conditions, and were not replicated in a sufficiently comparable way across studies. The overall picture is therefore one of fragmented and heterogeneous evidence rather than a coherent signal of effect.

A quantitative synthesis was not possible, and this is itself an important finding about the current state of the evidence base. The barrier was not simply clinical or biological heterogeneity, although that was substantial; it was also the pervasive lack of extractable numerical data needed for meta-analysis. Across the 26 included studies, most did not report group-specific sample sizes, means and measures of variance, effect estimates, confidence intervals, exact p-values, or outcome data in a form that could be transformed for synthesis. In addition, studies differed markedly in exposure characteristics (frequency, modulation, power density, duration), biological systems (cell lines, animal models, human studies), comparators, and outcome definitions. Even where studies addressed similar endpoints, inconsistent reporting and non-standardized metrics prevented meaningful pooling. Accordingly, the absence of meta-analysis should not be interpreted as a weakness of the review methods, but as a transparent reflection of limitations in the primary literature.

Our findings are broadly in line with the direction of the previous meta-analysis of experimental millimetre-wave studies, which reported no consistent evidence of biological effects below 100 W/m² in the 30–300 GHz range and found smaller effects in studies with higher methodological quality. We likewise did not identify a robust, recurring pattern of effects that would support a consistent biological hazard at low exposure levels. However, unlike that earlier review, we were not able to quantitatively test effect magnitude, heterogeneity, or quality-related gradients because the underlying reports in our corpus rarely provided sufficient numerical information. More generally, our review illustrates a common problem seen across complex exposure literatures: whereas some fields can support formal synthesis through standardized reporting and comparable endpoints, evidence on low-level >6 GHz exposures remains too heterogeneous and incompletely reported for the same approach to be reliably applied.

This review nevertheless has several strengths. We applied a broad PICO framework spanning human, animal, and in vitro evidence, which is appropriate for an emerging exposure domain in which mechanistic, toxicological, and epidemiological data all contribute to hazard identification. Study selection and extraction were conducted systematically, and the review reports explicitly where evidence was and was not available. The included set was also not dominated by studies judged low quality on our overall appraisal; most were classified as high quality, with only a small number rated medium or low. At the same time, our review highlights an important distinction between general study appraisal and usability for evidence synthesis: a study may address a relevant question and meet basic design criteria, yet still be unusable for meta-analysis if essential numerical results are not reported.

The main limitation of this review is therefore inseparable from its main contribution: the published evidence is insufficiently reported for quantitative integration. Because many studies presented only qualitative statements, representative examples, fold changes without denominators, or narrative claims of significance, we could not estimate pooled effects or formally explore publication bias, dose-response patterns, or subgroup differences by model, frequency band, or endpoint. This necessarily limits the certainty and precision of any conclusion. For practice and policy, the most defensible interpretation is cautious: based on the currently available and reportable evidence, there is no consistent, reproducible indication of biological or health effects from low-level >6 GHz exposures below ICNIRP occupational limits, but the evidence base is not yet strong enough to support precise quantitative risk estimates.

Future research should prioritize reporting quality as much as experimental innovation. Primary studies in this field should provide complete metadata, explicit exposure characterization, sham/control details, sample sizes, prespecified outcomes, and group-level numerical results with variance estimates or effect sizes sufficient for secondary analysis. Greater harmonization of endpoints, dosimetry, and analytic methods would also improve comparability across studies and enable future meta-analysis. For epidemiological and experimental investigators alike, adherence to reporting guidelines and routine sharing of underlying data would substantially strengthen the field. In that sense, the inability to pool the current literature is not a null result of the review; it is a substantive finding that maps the evidence landscape and identifies what must improve before stronger inference is possible.

## Conclusion

This systematic review identified 26 studies evaluating biological and health effects of low-level radiofrequency electromagnetic fields above 6 GHz, including millimetre-wave exposures relevant to 5G and radar, in human, animal, and cellular models. However, quantitative synthesis was not possible because the included studies reported outcomes too heterogeneously and, critically, often did not provide extractable numerical data needed for meta-analysis. The qualitative evidence does not show a consistent pattern of adverse effects across endpoints such as genotoxicity, cell proliferation, gene expression, signalling, membrane function, cancer, reproduction, and other diseases; reported findings were mixed and frequently difficult to interpret across study types and exposure conditions. The main limitation of this review is therefore the poor completeness and comparability of reported data. Overall, the current evidence base remains limited and insufficient to support firm conclusions about health risks from low-level exposures above 6 GHz.

## Final Included Studies

- Corpus ID: 3546 | Effects of 9.4 GHz microwave exposure on meiosis in mice.
- Corpus ID: 3461 | The relationship between colony-forming ability, chromosome aberrations and incidence of micronuclei in V79 Chinese hamster cells exposed to microwave radiation.
- Corpus ID: 3470 | Effects of Long-Term Exposure to 60 GHz Millimeter-Wavelength Radiation on the Genotoxicity and Heat Shock Protein (Hsp) Expression of Cells Derived from Human Eye.
- Corpus ID: 3441 | Resonance effect of low-intensity millimeter waves on the chromatin conformational state of rat thymocytes.
- Corpus ID: 3484 | Evaluation of the biological effects of police radar RAMER 7F.
- Corpus ID: 3443 | Evaluation of the potential in vitro antiproliferative effects of millimeter waves at some therapeutic frequencies on RPMI 7932 human skin malignant melanoma cells.
- Corpus ID: 87494 | Oxidative stress and testicular damage induced by chronic exposure to 35.5 GHz millimeter wave radiation in male Wistar rats.
- Corpus ID: 3468 | Fifty-gigahertz microwave exposure effect of radiations on rat brain.
- Corpus ID: 87297 | Altered calcium dynamics mediates P19-derived neuron-like cell responses to millimeter-wave radiation.
- Corpus ID: 3463 | Terahertz radiation induces spindle disturbances in human-hamster hybrid cells.
- Corpus ID: 3493 | Low-power millimeter wave radiations do not alter stress-sensitive gene expression of chaperone proteins.
- Corpus ID: 3469 | Terahertz radiation increases genomic instability in human lymphocytes.
- Corpus ID: 87944 | Whole-genome expression analysis in primary human keratinocyte cell cultures exposed to 60 GHz radiation.
- Corpus ID: 3476 | Study of narrow band millimeter-wave potential interactions with endoplasmic reticulum stress sensor genes.
- Corpus ID: 3477 | Absence of direct effect of low-power millimeter-wave radiation at 60.4 GHz on endoplasmic reticulum stress.
- Corpus ID: 3450 | Effect of 99 GHz continuous millimeter wave electro-magnetic radiation on E. coli viability and metabolic activity.
- Corpus ID: 3471 | Long-term exposure to a 40-GHz electromagnetic field does not affect genotoxicity or heat shock protein expression in HCE-T or SRA01/04 cells.
- Corpus ID: 87330 | Resonance effect of millimeter waves in the power range from 10(-19) to 3 x 10(-3) W/cm2 on Escherichia coli cells at different concentrations.
- Corpus ID: 3483 | Effects of millimeter wave irradiation and equivalent thermal heating on the activity of individual neurons in the leech ganglion.
- Corpus ID: 3479 | Search for frequency-specific effects of millimeter-wave radiation on isolated nerve function.
- Corpus ID: 87340 | The effect of a 94 GHz electromagnetic field on neuronal microtubules.
- Corpus ID: 3481 | The response of giant phospholipid vesicles to millimeter waves radiation.
- Corpus ID: 87302 | [Modification of the activity of murine peritoneal neutrophils upon exposure to millimeter waves at close and far distances from the emitter].
- Corpus ID: 3444 | Frequency and irradiation time-dependant antiproliferative effect of low-power millimeter waves on RPMI 7932 human melanoma cell line.
- Corpus ID: 3455 | Cell bathing medium as a target for non thermal effect of millimeter waves.
- Corpus ID: 3447 | Millimeter Wave Radiations Affect Membrane Hydration in Phosphatidylcholine Vesicles.
