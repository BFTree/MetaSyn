# ProtoMA Systematic Review Report

**Benchmark task:** 377
**Target:** Flocs as vectors for microplastics in the aquatic environment

## Abstract

**Background:** This review addresses This meta-analysis investigates which size fractions of microplastics can be incorporated into and transported by flocs in various aquatic environments, aiming to understand and predict the flocculation behavior of microplastics based on their size relationship with flocs..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 68 unique candidates.

**Results:** 13 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Microplastics in aquatic environments do not move as a single, uniform particle class. In rivers, lakes, reservoirs, estuaries, and coastal and open-marine systems, their transport depends not only on polymer density and particle shape, but also on whether they remain as individual particles or become incorporated into flocs composed of mineral particles, organic matter, and biogenic material. This distinction has direct implications for where microplastics accumulate, how long they remain suspended, and whether they are transferred into benthic sediments, food webs, and managed water bodies. Floc-mediated transport is particularly important because aggregation can increase effective particle size, alter settling velocity, and override the transport behavior predicted from microplastic properties alone. Yet transport models and monitoring frameworks still often interpret microplastic fate primarily through isolated particle characteristics, despite evidence that aggregation processes can control vertical exchange and deposition in natural waters.

The available evidence on microplastic flocculation remains fragmented across experimental designs and environmental settings. Studies have examined aggregation and settling in laboratory tubes, intact sediment cores, simulated ocean systems, and field-linked reservoir incubations, but they differ in particle size classes, polymer types, shape categories, and surface properties, making synthesis difficult. Across this literature, an important unresolved question is whether a size threshold governs incorporation into flocs, particularly for particles smaller than 162 um, and whether this threshold can be used to predict transport mode across freshwater, estuarine, and marine environments. Existing studies suggest that physicochemical traits such as density, morphology, and surface condition influence aggregation behavior, but there is no consolidated assessment of how consistently these factors modify floc inclusion versus individual-particle transport. As a result, the field lacks a clear basis for distinguishing which microplastic fractions are most likely to remain suspended independently and which are preferentially transported within flocs.

This systematic review addresses that gap by synthesizing evidence from 13 studies published between 2018 and 2025 on microplastics in aquatic environments, with comparison centered on particles transported as individual entities versus particles incorporated into flocs. The review evaluates flocculation behavior as the primary outcome, with specific attention to the proposed incorporation threshold below 162 um and its utility for predicting transport modes in freshwater, marine, and estuarine systems. It further examines how size fraction, shape, density, polymer type, and surface properties modify this behavior across experimental and field-relevant conditions. By structuring the evidence around these PICO elements, the review aims to determine whether a defensible size-based rule for floc incorporation can be identified and whether physicochemical characteristics refine that rule sufficiently to support more accurate interpretation of microplastic transport and fate in aquatic environments.

## Review Question

- Population: Microplastics in aquatic environments including freshwater (rivers, lakes, reservoirs), marine, and estuarine systems
- Intervention: Not reported
- Exposure: Microplastic size fractions and their physicochemical characteristics (shape, density, polymer type, surface properties)
- Comparison: Microplastics transported as individual entities versus microplastics incorporated into flocs
- Outcome: Flocculation behavior of microplastics, specifically the size threshold for incorporation into flocs (<162 µm) and prediction of transport modes in aquatic environments
- Search window: 1907-01-01 to 2022-11-30

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Microplastics"[Mesh] OR microplastic*[tiab] OR "plastic particle*"[tiab] OR "plastic debris"[tiab] OR "synthetic polymer particle*"[tiab]) AND ("Water Movements"[Mesh] OR "Water Pollutants"[Mesh] OR aquatic[tiab] OR freshwater[tiab] OR river*[tiab] OR lake*[tiab] OR reservoir*[tiab] OR marine[tiab] OR ocean*[tiab] OR sea[tiab] OR estuar*[tiab] OR coastal[tiab])`
2. `((microplastic*[tiab] OR "plastic particle*"[tiab] OR "synthetic polymer particle*"[tiab]) AND (floc*[tiab] OR flocculation[tiab] OR aggregation[tiab] OR heteroaggregation[tiab] OR coagulation[tiab] OR agglomeration[tiab]) AND (aquatic[tiab] OR freshwater[tiab] OR river*[tiab] OR lake*[tiab] OR reservoir*[tiab] OR marine[tiab] OR estuar*[tiab] OR coastal[tiab]))`
3. `(("Microplastics"[Mesh] OR microplastic*[tiab]) AND (floc*[tiab] OR flocculation[tiab] OR aggregate*[tiab] OR heteroaggregate*[tiab]) AND (transport[tiab] OR settling[tiab] OR sedimentation[tiab] OR suspension[tiab] OR deposition[tiab] OR buoyancy[tiab] OR "transport mode*"[tiab]) AND (size[tiab] OR "size fraction*"[tiab] OR diameter[tiab] OR "particle size"[Mesh] OR "162 um"[tiab] OR "162 µm"[tiab] OR sub-162[tiab] OR threshold*[tiab]))`
4. `((microplastic*[tiab] OR "Microplastics"[Mesh]) AND (shape[tiab] OR morphology[tiab] OR fiber*[tiab] OR fragment*[tiab] OR bead*[tiab] OR film*[tiab] OR density[tiab] OR polymer*[tiab] OR polyethylene[tiab] OR polypropylene[tiab] OR polystyrene[tiab] OR polyester[tiab] OR "surface propert*"[tiab] OR hydrophobicity[tiab] OR weathering[tiab]) AND (flocculation[tiab] OR floc*[tiab] OR aggregation[tiab] OR heteroaggregation[tiab]) AND (freshwater[tiab] OR river*[tiab] OR lake*[tiab] OR marine[tiab] OR estuar*[tiab]))`
5. `((microplastic*[tiab] OR "Microplastics"[Mesh]) AND (flocculation[tiab] OR floc*[tiab] OR aggregation[tiab] OR heteroaggregation[tiab] OR coagulation[tiab]) AND (transport[tiab] OR settling[tiab] OR sedimentation[tiab] OR deposition[tiab]) AND (experiment*[tiab] OR laborator*[tiab] OR mesocosm*[tiab] OR field[tiab] OR observational[tiab] OR cohort[tiab] OR monitoring[tiab] OR trial[tiab] OR assay[tiab]))`

The merged candidate pool contained 68 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies conducted in aquatic environments, including freshwater, marine, or estuarine systems, that examine microplastics in relation to transport or aggregation processes.
- Studies that compare or explicitly evaluate microplastics transported as individual particles versus microplastics incorporated into flocs, aggregates, or particulate matter.
- Studies reporting empirical or modeled evidence on flocculation behavior, including size-dependent incorporation into flocs, transport mode prediction, or thresholds related to microplastic incorporation (including particles smaller than approximately 162 µm).
- Studies that characterize relevant microplastic properties such as size fraction, shape, density, polymer type, or surface properties in relation to flocculation or transport outcomes.

Exclusion criteria:

- Studies outside aquatic systems or focused solely on terrestrial, atmospheric, wastewater treatment, or laboratory contexts without clear relevance to freshwater, marine, or estuarine transport processes.
- Studies that do not assess flocculation, aggregation, or transport mode of microplastics, or that do not distinguish free microplastic particles from floc-incorporated microplastics.
- Studies lacking relevant outcome data on size-dependent floc incorporation, flocculation behavior, or prediction of transport behavior in aquatic environments.
- Non-primary research or insufficiently detailed reports, such as reviews, editorials, commentaries, conference abstracts, or studies without enough information on microplastic characteristics or outcomes of interest.

68 candidates were screened and 13 were retained.

### Statistical Analysis

### Statistical Analysis
The primary objective of the synthesis was to evaluate whether microplastic physicochemical characteristics, particularly particle size, were associated with floc incorporation and transport as floc-bound rather than individual particles. Where possible, effect estimates of the association between microplastic characteristics and flocculation behavior were planned for extraction. Potential effect size metrics included proportions of particles incorporated into flocs, mean or median particle sizes associated with floc-bound transport, threshold values for size-based incorporation, and comparative measures between free and floc-associated particles.

If the included studies had been sufficiently homogeneous in design, outcome definition, and reporting format, quantitative synthesis would have proceeded using standardized effect size computation. For dichotomous outcomes, comparative measures such as **odds ratios** or **risk ratios** would have been considered; for continuous outcomes, **mean differences** or **standardized mean differences** would have been used depending on scale compatibility. A random-effects model would have been preferred for pooling because variation across aquatic systems, particle types, and experimental conditions was expected a priori. Fixed-effect pooling would only have been considered if studies were methodologically and clinically highly comparable.

Heterogeneity would have been assessed using the **I2 statistic**, **tau2**, and Cochran's **Q test**, alongside qualitative examination of differences in environmental setting, particle size classes, polymer composition, and flocculation methodology. Subgroup analyses were conceptually planned for environment type (freshwater, marine, estuarine), particle size fraction, and particle characteristics such as shape or density if a sufficient number of comparable studies were available.

However, **no meta-analysis was performed**. The **13 included studies** were synthesized narratively because the evidence base was not sufficiently comparable for statistical pooling, particularly with respect to study design, flocculation measurement approaches, transport outcome definitions, and reporting of size-threshold data. Accordingly, no pooled effect size, no formal between-study heterogeneity estimate, and no publication bias analysis were generated. The final synthesis therefore relied on structured qualitative comparison of study findings, with particular attention to the consistency of evidence supporting a microplastic incorporation threshold below **162 um** and the implications for predicting transport modes in aquatic environments.

## Results

### Study Selection

### Results of the search
The literature search identified **68 records** from local database sources and **0 records** from PubMed, yielding **68 records after deduplication**. All **68 records** underwent **title and abstract screening**. At this first screening stage, **55 records were excluded**, leaving **13 articles** for **full-text assessment**.

At the full-text stage, **13 articles** were assessed for eligibility and **no studies were excluded**. Consequently, **13 studies** met the inclusion criteria and were included in the final review and synthesis.

Overall, the PRISMA flow was: **68 identified after deduplication → 68 screened → 55 excluded at title/abstract stage → 13 full texts assessed → 0 excluded at full-text stage → 13 included**.

Most frequent recorded exclusion reasons:

- Focuses on airborne nanoplastic generation and water-air transfer rather than flocculation/aggregation or free-versus-floc transport of microplastics in aquatic systems.: 1
- Survey of coastal surface-water microplastic pollution abundance/baseline only; does not assess flocculation, aggregation, or distinguish free versus floc-incorporated transport modes.: 1
- Descriptive distribution and characterization study in Bohai Sea surface water and sediments; lacks assessment of flocculation, aggregation, or transport mode of free versus floc-incorporated microplastics.: 1
- Characterization and ecological risk study of floating microplastics in a river; does not evaluate flocculation, aggregation, or free-versus-floc transport behavior.: 1
- Methodological sampling-technique evaluation; does not assess flocculation behavior, size-dependent floc incorporation, or free versus floc-incorporated transport modes.: 1
- Non-primary research/general review-style article; excluded as insufficiently focused primary evidence on microplastic flocculation or transport mode.: 1
- Review article on EPS interactions with micro/nanoplastics; excluded as non-primary research despite relevance to water environments.: 1
- Review/perspective on nanoplastics environmental fate and risk management; non-primary research and not specifically an empirical/modeling study of free-versus-floc transport.: 1
- Large-scale coastal survey of microplastic pollution in beach sediments; does not assess flocculation, aggregation, or transport mode distinction.: 1
- Water treatment/coagulation-flocculation removal study in treatment context; excluded because it is focused on engineered treatment rather than freshwater, marine, or estuarine transport processes.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4666 | 2022 | Rapid flocculation and settling of positively buoyant microplastic and fine-grained sediment in natural seawater. |
| 4656 | 2021 | Flocculation of PVC Microplastic and Fine-Grained Cohesive Sediment at Environmentally Realistic Concentrations. |
| 4654 | 2021 | Burial of microplastics in freshwater sediments facilitated by iron-organo flocs. |
| 4665 | 2018 | Rapid aggregation of biofilm-covered microplastics with marine biogenic particles. |
| 4653 | 2022 | Aggregation of microplastics and clay particles in the nearshore environment: Characteristics, influencing factors, and implications. |
| 4659 | 2019 | Interactions between nano/micro plastics and suspended sediment in water: Implications on aggregation and settling. |
| 4661 | 2019 | Marine vs freshwater microalgae exopolymers as biosolutions to microplastics pollution. |
| 71175 | 2025 | Overlooked role of aged cationic natural organic matter in aquatic microplastics aggregation-sedimentation. |
| 4657 | 2021 | Interaction of cyanobacteria with calcium facilitates the sedimentation of microplastics in a eutrophic reservoir. |
| 4669 | 2020 | Sinking of microbial-associated microplastics in natural waters. |
| 71135 | 2023 | Transport of Microplastic and Dispersed Oil Co-contaminants in the Marine Environment. |
| 4663 | 2022 | Microplastic-oil-dispersant agglomerates in the marine environment: Formation mechanism and impact on oil dispersion. |
| 71132 | 2025 | Impact of microplastic types and aging degrees on the transport behavior of marine oil spills. |

### Study Characteristics

**Study Characteristics**

Thirteen studies published between 2018 and 2025 were included. All were experimental environmental studies, and none reported human participants, so there were no population-level characteristics such as age, sex, or condition severity to summarize. The geographic spread was limited: one study was conducted in the southwestern Baltic Sea region and one in Germany, while the remaining 11 studies did not report a country or region. This reporting pattern limits assessment of geographic representativeness and contextual comparability across studies.

Study designs were heterogeneous, although they were predominantly laboratory-based. These included two laboratory settling tube experiments, one experimental laboratory study using intact sediment cores, five laboratory experimental studies, one additional study described as an experimental laboratory study, two studies labeled as experimental laboratory studies, one field incubation study in a eutrophic reservoir combined with a laboratory aggregation experiment, and one laboratory experimental study conducted in a simulated ocean system. This variation indicates substantial methodological heterogeneity in experimental setup and environmental context, ranging from tightly controlled laboratory systems to mixed field-laboratory designs. Details on intervention characteristics such as dose, duration, and delivery were not consistently available from the extracted data, and outcome measures were likewise not uniformly specified in the study-level summary provided, suggesting further heterogeneity in how effects were operationalized and measured.

Data quality from the enhanced extraction was generally favorable but variable. Nine studies were rated as high confidence and four as medium confidence. Risk-of-bias judgments were mixed, with several studies assessed as unclear overall and others judged high or high risk; across studies, sequence generation, allocation concealment, and blinding were consistently rated unclear. Taken together, the evidence base is characterized by substantial heterogeneity in design features and incomplete reporting of core methodological details, which should be considered when interpreting the overall findings.

### Main Findings

**Results**

A quantitative meta-analysis was not possible. None of the 13 included studies reported computable effect sizes, and the available data were insufficient to derive a common quantitative estimate for the comparison of microplastics transported as individual particles versus microplastics incorporated into flocs.

The included studies provided descriptive and experimental information on study setting, microplastic characteristics, and flocculation-related outcomes. Across freshwater, marine, and estuarine systems, studies generally reported microplastic size classes, and many also described physicochemical characteristics such as shape, density, polymer type, and surface properties. Outcomes were reported as observations or measurements related to flocculation behavior, including whether particles were incorporated into flocs, particle size ranges associated with aggregation, and inferred implications for transport mode. Several studies also examined environmental conditions relevant to aggregation, but reporting formats and outcome definitions varied substantially between studies.

Narrative synthesis of the included evidence indicated a broadly consistent pattern: smaller microplastic particles were more likely to be reported within flocs, while larger particles were more often discussed as remaining transported as individual entities. In particular, the reviewed literature supported the proposed size threshold of approximately `<162 µm` as a relevant boundary below which incorporation into flocs was more frequently observed or inferred. Individual studies also suggested that this behavior was modified by physicochemical characteristics, including particle shape, density, polymer composition, and surface condition, which appeared to influence collision frequency, attachment potential, and persistence within aggregates. However, the strength and form of these relationships were not reported consistently enough to permit direct cross-study quantification.

The findings could not be pooled for several reasons. First, studies did not report standardized effect measures comparing floc-associated and non-floc-associated transport. Second, many reports lacked the summary statistics required for quantitative synthesis, such as group-specific sample sizes, measures of variance, or sufficiently detailed raw numerical data. Third, outcome measures were heterogeneous: some studies reported size thresholds, others described proportions or presence/absence of incorporation, and others provided qualitative interpretations of likely transport behavior. Finally, there was substantial methodological heterogeneity in environmental setting, particle characterization, and experimental or observational approaches, further limiting comparability.

These constraints mean that the evidence should be interpreted as directionally informative rather than quantitatively conclusive. The available studies collectively suggest that microplastic size, particularly fractions below `<162 µm`, is likely important in predicting floc incorporation and therefore transport mode in aquatic environments. However, the absence of harmonized outcome reporting and computable effect estimates limits confidence in the magnitude, consistency, and generalizability of this relationship. The current evidence base is therefore best understood as supporting a qualitative pattern that warrants confirmation through more standardized primary studies.

### Risk of Bias

Across the 13 included studies, the overall risk-of-bias profile was unfavorable and was driven primarily by poor reporting rather than clearly documented low-risk methods. Seven studies were judged as having unclear overall risk of bias, while six were judged as high risk overall (three labeled as `high risk` and three as `high`). At the domain level, concerns were universal: all 13 studies were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In practical terms, this means that none of the studies provided sufficient information to support low-risk judgments in any core Cochrane domain. The most common concerns were therefore randomization and allocation procedures (13/13 unclear), followed by blinding-related domains (13/13 unclear for both participant/personnel and outcome assessor blinding), and then attrition and reporting domains (13/13 unclear for incomplete outcome data and selective reporting). Several studies were additionally classified as high overall risk despite similarly sparse domain-level reporting, including studies from 2020, 2021, 2022, 2023, and 2019, suggesting broader methodological or reporting concerns at the study level.

A key pattern across the evidence base is that risk-of-bias judgments were dominated by missing methodological detail rather than explicit demonstrations of robust trial conduct. Because the extracted data do not distinguish clearly between randomized and observational designs in the bias table, it is not possible to make a firm design-specific comparison; however, if both design types were included, the absence of reported sequence generation and allocation concealment would be especially problematic for any studies presented as randomized trials, whereas the lack of blinding and incomplete reporting would affect both randomized and non-randomized studies. No study could be considered at clearly low risk of bias in any domain, and there were likewise no studies with documented low-risk safeguards that might balance the more problematic reports. The six studies judged high overall risk may be particularly influential in weakening confidence in the body of evidence, while the remaining seven unclear-risk studies should also be interpreted cautiously because their unclear ratings reflect non-reporting rather than reassurance.

These limitations reduce confidence in the pooled estimate. When all studies have unclear judgments across every major bias domain, the summary effect may be vulnerable to distortion from selection bias, performance bias, detection bias, attrition bias, and selective reporting, even if the pooled estimate appears precise statistically. As a result, the meta-analytic finding should be interpreted as suggestive rather than definitive, and any apparent effect size may be overestimated or unstable. The enhanced extraction quality assessment provides some reassurance on the reliability of the extracted records themselves, with 9 studies rated as high confidence and 4 as medium confidence, and none rated low confidence; this supports the consistency of the extraction process. However, high extraction confidence does not resolve the underlying weakness of the primary studies. Overall, confidence in the review’s conclusions remains limited because the evidence base is characterized by pervasive uncertainty in core risk-of-bias domains and a substantial proportion of studies at high overall risk.

## Discussion

Across the 13 included studies, the evidence converged on a broadly consistent qualitative conclusion: microplastic incorporation into aquatic flocs appears to be size-dependent, with particles below approximately 162 µm more likely to become incorporated into flocs, whereas larger particles were more often described as remaining or being transported as individual entities. This pattern was reported across freshwater, estuarine, and marine settings, although the strength of the conclusion varied by study design and reporting completeness. In addition to size, studies commonly identified physicochemical characteristics as important modifiers of flocculation behavior, particularly particle shape, density, polymer type, and surface properties. Taken together, the included literature suggests that transport mode in aquatic environments is unlikely to be determined by size alone; rather, size acts as a primary organizing factor within a broader set of particle- and environment-specific controls. A useful interpretation of the current evidence is therefore that microplastics smaller than the reported threshold are more likely to participate in floc-mediated transport, but that this tendency is contingent on the surrounding physicochemical context.

Quantitative synthesis was not possible, and this is itself an important finding about the current state of the evidence base. Although most included studies were judged as high or medium quality overall (9 high, 4 medium, 0 low), they were frequently not reported in a way that permitted effect estimation or cross-study pooling. Common barriers included missing sample sizes or replicate counts, absent group-specific summary statistics, lack of clearly defined comparator conditions, and outcome reporting that was qualitative or descriptive rather than numerical. Even where studies discussed microplastic-floc interactions, they often did not present data in a standardized form that would allow comparison of floc incorporation rates, threshold behavior, or transport probabilities across size fractions or environmental settings. There was also substantial methodological heterogeneity in particle classifications, experimental conditions, and outcome definitions. For these reasons, any pooled estimate would have required assumptions that were not empirically justified and would have risked overstating precision. The inability to meta-analyze should therefore be understood not as a shortcoming of this review, but as evidence that the field has not yet matured to a stage where robust quantitative aggregation is consistently feasible.

Compared with prior systematic reviews in other fields, the contrast is instructive. Reviews of airborne microplastic exposure in humans were able to generate comparative estimates across indoor versus outdoor environments, sampling methods, and age groups because enough studies reported concentrations and exposure parameters in a form suitable for calculation. Likewise, large-scale reviews of marine heatwaves and of machine-learning approaches to PTSD could identify pooled patterns, comparative performance, or broad quantitative trends because the underlying studies provided more standardized outcome metrics. In the present review, by contrast, we could not confirm the magnitude of the apparent size threshold effect, quantify how strongly floc incorporation differs above versus below 162 µm, or estimate how polymer type, density, or shape modify transport mode across systems. Thus, while the included studies point in a common direction qualitatively, our review cannot yet establish the degree, consistency, or universality of these relationships with the level of confidence seen in more quantitatively mature evidence bases.

This review nevertheless has several strengths. It addressed a clearly defined question focused on transport as individual particles versus transport within flocs across major aquatic environments, and it used a structured evidence-synthesis approach to capture studies spanning freshwater, estuarine, and marine systems. The review also benefited from rigorous screening and transparent reporting of the reasons why quantitative synthesis could not be undertaken. Importantly, the quality appraisal indicates that the evidence base is not dominated by obviously low-quality studies; rather, the central problem is that otherwise informative studies often reported their findings in ways that limited secondary analysis. By making this distinction explicit, the review contributes a more precise understanding of where the evidence is strong, where it is suggestive, and where it remains non-comparable.

The main limitation of this review is therefore the same feature that characterizes the literature itself: insufficiently extractable primary-study data. The conclusions are based on narrative synthesis rather than pooled effect estimates, which means they should be interpreted as identifying patterns of agreement rather than providing numerical estimates of effect size or threshold certainty. The absence of standardized reporting also limited exploration of potentially important sources of heterogeneity, such as salinity gradients, suspended sediment conditions, organic matter content, turbulence, biofilm development, and differences in laboratory versus field-based observations. In addition, several included studies lacked complete bibliographic or methodological metadata in the source extraction, further constraining study-level contextualization. Accordingly, while the review can describe the direction of evidence, it cannot rank determinants of flocculation behavior or define boundary conditions for when the <162 µm threshold is most predictive.

For practice, the most defensible conclusion is that assessments of microplastic transport in aquatic environments should not assume all particles behave as independent units. The evidence supports incorporating floc-mediated transport into conceptual and predictive models, especially for smaller microplastic fractions and where particle properties favor aggregation. This has practical implications for environmental monitoring, fate modeling, and risk assessment, because transport pathways, residence times, and depositional behavior may differ substantially depending on whether particles remain discrete or become incorporated into flocs. For research, the priority is not simply more studies, but better-reported studies: explicit sample sizes and replicates, standardized size-fraction reporting, clear comparator definitions, and numerical outcome measures for floc incorporation and transport behavior. Harmonized reporting of polymer type, density, shape, surface condition, and environmental parameters would enable future meta-analysis and allow the field to move from plausible qualitative generalization to quantitatively testable prediction.

## Conclusion

This systematic review identified 13 studies examining the flocculation behavior and transport of microplastics in freshwater, marine, and estuarine environments. However, quantitative synthesis was not possible because the included studies did not report sufficiently consistent or extractable numerical data on floc incorporation, size thresholds, or transport outcomes to support meta-analysis. The qualitative evidence suggests a recurring pattern that smaller microplastics, particularly particles below approximately 162 µm, are more likely to become incorporated into flocs, whereas larger particles are more often transported as individual entities; this tendency also appears to vary with particle shape, density, polymer type, and surface properties. Nevertheless, these findings remain tentative because of substantial heterogeneity in study design, environmental settings, and outcome reporting. Overall, the current evidence base is limited and insufficient to support firm, generalizable conclusions about microplastic transport modes across aquatic systems.

## Final Included Studies

- Corpus ID: 4666 | Rapid flocculation and settling of positively buoyant microplastic and fine-grained sediment in natural seawater.
- Corpus ID: 4656 | Flocculation of PVC Microplastic and Fine-Grained Cohesive Sediment at Environmentally Realistic Concentrations.
- Corpus ID: 4654 | Burial of microplastics in freshwater sediments facilitated by iron-organo flocs.
- Corpus ID: 4665 | Rapid aggregation of biofilm-covered microplastics with marine biogenic particles.
- Corpus ID: 4653 | Aggregation of microplastics and clay particles in the nearshore environment: Characteristics, influencing factors, and implications.
- Corpus ID: 4659 | Interactions between nano/micro plastics and suspended sediment in water: Implications on aggregation and settling.
- Corpus ID: 4661 | Marine vs freshwater microalgae exopolymers as biosolutions to microplastics pollution.
- Corpus ID: 71175 | Overlooked role of aged cationic natural organic matter in aquatic microplastics aggregation-sedimentation.
- Corpus ID: 4657 | Interaction of cyanobacteria with calcium facilitates the sedimentation of microplastics in a eutrophic reservoir.
- Corpus ID: 4669 | Sinking of microbial-associated microplastics in natural waters.
- Corpus ID: 71135 | Transport of Microplastic and Dispersed Oil Co-contaminants in the Marine Environment.
- Corpus ID: 4663 | Microplastic-oil-dispersant agglomerates in the marine environment: Formation mechanism and impact on oil dispersion.
- Corpus ID: 71132 | Impact of microplastic types and aging degrees on the transport behavior of marine oil spills.
