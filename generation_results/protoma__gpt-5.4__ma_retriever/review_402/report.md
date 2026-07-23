# ProtoMA Systematic Review Report

**Benchmark task:** 402
**Target:** Systematic review of associations between gut microbiome composition and stunting in under-five children

## Abstract

**Background:** This review addresses This systematic review examines the associations between gut microbiome composition and stunting in children under 5 years of age in low- and middle-income countries, comparing microbial diversity, taxonomic abundance, and metabolic pathways between stunted and non-stunted children..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 60 unique candidates.

**Results:** 3 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Stunting, defined as height-for-age more than two standard deviations below the WHO child growth median, remains one of the clearest markers of chronic undernutrition and cumulative early-life adversity in low- and middle-income countries (LMICs). In children under 5 years of age, stunting is associated with impaired linear growth, delayed neurodevelopment, increased susceptibility to infection, and reduced human capital across the life course. Although food insecurity, repeated enteric infection, poor sanitation, and environmental exposures are established determinants of impaired growth, these factors likely operate in part through the gut ecosystem, which is central to nutrient metabolism, immune maturation, intestinal barrier function, and host-microbial signaling during the first years of life. This has led to increasing interest in whether gut microbiome disruption is linked to stunting and whether microbiome features could help explain heterogeneity in growth outcomes among children exposed to similar structural risks.

However, the evidence base remains limited and methodologically heterogeneous. Studies in LMIC settings have examined differences between stunted and non-stunted children in gut microbiome composition using measures such as alpha diversity, beta diversity, taxonomic abundance at phylum and genus levels, and inferred or measured metabolic pathways, but findings have not been synthesized in a focused review of this population and exposure-outcome relationship. More broadly, systematic reviews in adjacent fields suggest that microbiome associations are often more consistent for overall community composition than for within-sample diversity metrics; for example, a review of psychiatric disorders found no strong evidence for alpha-diversity differences relative to controls but observed relatively consistent beta-diversity differences across conditions. At the same time, evidence syntheses in LMIC child health have shown that intervention effects can differ materially by component structure and context, underscoring the need for population-specific appraisal rather than extrapolation from high-income settings or unrelated clinical groups. For stunting specifically, uncertainty persists regarding whether observed microbiome differences reflect reduced microbial maturity, altered taxonomic profiles, disrupted metabolic potential, or inconsistent findings driven by small samples and variation in study design.

This systematic review therefore evaluates the association between stunting status and gut microbiome composition in children under 5 years of age living in LMICs, using non-stunted children with height-for-age within the normal range as the comparator. The review focuses specifically on microbial alpha diversity, beta diversity, taxonomic abundance at the phylum and genus levels, and metabolic pathways. Across three eligible studies published between 2016 and 2023, comprising 140 total participants and including longitudinal observational, case-control, and cohort designs, the aim is to determine whether stunted children show reproducible microbiome differences relative to non-stunted peers and to identify the principal gaps that limit inference in this field.

## Review Question

- Population: Children under 5 years of age in low- and middle-income countries (LMICs)
- Intervention: Not reported
- Exposure: Gut microbiome composition (including alpha diversity, beta diversity, taxonomic abundance at phylum and genus levels, and metabolic pathways)
- Comparison: Non-stunted children (height-for-age within normal range)
- Outcome: Stunting status (height-for-age more than two standard deviations below the WHO child growth median)
- Search window: 2023-01-01 to 2023.2.29

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Infant"[Mesh] OR "Child, Preschool"[Mesh] OR infant*[tiab] OR baby[tiab] OR babies[tiab] OR toddler*[tiab] OR child*[tiab] OR preschool*[tiab] OR "under five"[tiab] OR "under-5"[tiab]) AND ("Developing Countries"[Mesh] OR "low-income countr*"[tiab] OR "middle-income countr*"[tiab] OR LMIC*[tiab] OR "developing countr*"[tiab] OR Africa[tiab] OR Asia[tiab] OR "Latin America"[tiab]) AND ("Gastrointestinal Microbiome"[Mesh] OR microbiome*[tiab] OR microbiota[tiab] OR microflora[tiab] OR "gut microbiome"[tiab] OR "gut microbiota"[tiab] OR "intestinal microbiota"[tiab] OR "fecal microbiota"[tiab] OR faecal microbiota[tiab]))`
2. `(("Infant"[Mesh] OR "Child, Preschool"[Mesh] OR infant*[tiab] OR toddler*[tiab] OR child*[tiab] OR preschool*[tiab]) AND ("Developing Countries"[Mesh] OR LMIC*[tiab] OR "low- and middle-income countr*"[tiab] OR "developing countr*"[tiab]) AND ("Gastrointestinal Microbiome"[Mesh] OR microbiome*[tiab] OR microbiota[tiab] OR "gut microbiota"[tiab] OR "intestinal microbiome"[tiab]) AND ("Stunted Growth"[Mesh] OR stunt*[tiab] OR "linear growth faltering"[tiab] OR "growth faltering"[tiab] OR "height-for-age"[tiab] OR HAZ[tiab] OR "length-for-age"[tiab] OR LAZ[tiab] OR "chronic malnutrition"[tiab] OR undernutrition[tiab]))`
3. `(("Infant"[Mesh] OR "Child, Preschool"[Mesh] OR infant*[tiab] OR child*[tiab] OR toddler*[tiab]) AND ("Developing Countries"[Mesh] OR LMIC*[tiab] OR "low income countr*"[tiab] OR "middle income countr*"[tiab]) AND (("Stunted Growth"[Mesh] OR stunt*[tiab] OR "height-for-age"[tiab] OR HAZ[tiab]) AND ("non-stunted"[tiab] OR "normal height-for-age"[tiab] OR control*[tiab] OR comparison[tiab])) AND ("Gastrointestinal Microbiome"[Mesh] OR microbiome*[tiab] OR microbiota[tiab] OR "gut microbiota"[tiab]) AND ("alpha diversity"[tiab] OR "beta diversity"[tiab] OR diversity[tiab] OR "taxonomic abundance"[tiab] OR phylum[tiab] OR genus[tiab] OR taxa[tiab] OR taxon[tiab] OR "metabolic pathway*"[tiab] OR metagenom*[tiab] OR metabolom*[tiab]))`
4. `(("Infant"[Mesh] OR "Child, Preschool"[Mesh] OR infant*[tiab] OR child*[tiab] OR toddler*[tiab] OR preschool*[tiab]) AND ("Developing Countries"[Mesh] OR LMIC*[tiab] OR "developing countr*"[tiab]) AND ("Gastrointestinal Microbiome"[Mesh] OR microbiome*[tiab] OR microbiota[tiab] OR "intestinal microbiota"[tiab]) AND ("Stunted Growth"[Mesh] OR stunt*[tiab] OR "growth faltering"[tiab] OR HAZ[tiab] OR LAZ[tiab]) AND (cohort[tiab] OR longitudinal[tiab] OR "case-control"[tiab] OR "cross-sectional"[tiab] OR observational[tiab] OR prospective[tiab] OR retrospective[tiab] OR trial[tiab] OR randomized[tiab] OR randomised[tiab]))`
5. `((("stunted child*"[tiab] OR stunting[tiab] OR "height-for-age z score"[tiab] OR HAZ[tiab] OR LAZ[tiab]) AND (microbiome*[tiab] OR microbiota[tiab] OR "gut microbiome"[tiab] OR "fecal microbiota"[tiab] OR faecal microbiota[tiab] OR metagenom*[tiab])) AND (infant*[tiab] OR child*[tiab] OR toddler*[tiab] OR preschool*[tiab] OR "under five"[tiab]) AND (LMIC*[tiab] OR "low-income countr*"[tiab] OR "middle-income countr*"[tiab] OR "developing countr*"[tiab])) NOT (mouse[tiab] OR mice[tiab] OR murine[tiab] OR pig[tiab] OR poultry[tiab] OR animal*[tiab] NOT human*[tiab])`

The merged candidate pool contained 60 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Observational study designs (cross-sectional, case-control, or cohort) or intervention studies that report baseline or subgroup comparisons between stunted and non-stunted children.
- Studies conducted in low- and middle-income countries and including children under 5 years of age.
- Studies that define stunting using height-for-age z-score criteria consistent with WHO standards (e.g., HAZ < -2 SD) and include a comparison group of non-stunted children with normal height-for-age.
- Studies reporting gut microbiome composition outcomes, including alpha diversity, beta diversity, taxonomic abundance at phylum or genus level, and/or microbial functional or metabolic pathway profiles.

Exclusion criteria:

- Studies conducted outside LMICs or in populations not restricted to children under 5 years of age.
- Studies that do not include stunting status as the exposure/grouping variable or do not include a non-stunted comparison group.
- Studies that do not report gut microbiome composition data relevant to the review outcomes.
- Reviews, meta-analyses, case reports, conference abstracts, editorials, protocols, animal studies, or in vitro studies.

60 candidates were screened and 3 were retained.

### Statistical Analysis

### Statistical Analysis
The methods were planned to synthesize associations between stunting status and gut microbiome composition in children under 5 years living in LMICs. Extracted quantitative outcomes of interest included alpha diversity indices, beta diversity differences, relative abundance of taxa at phylum and genus levels, and microbial functional or metabolic pathway profiles.

Where data are sufficiently comparable, effect sizes would ordinarily be calculated according to outcome type. For continuous outcomes such as alpha diversity indices, the preferred summary measure would be the **mean difference (MD)** when studies reported the same metric, or the **standardized mean difference (SMD)** when different diversity indices or scales were used. For dichotomous microbiome-related outcomes, **odds ratios (ORs)** with 95% confidence intervals would be considered. For taxonomic abundance and pathway data, results would be extracted as reported, recognizing that differences in sequencing platforms, bioinformatic pipelines, normalization procedures, and reporting formats can limit quantitative comparability.

A meta-analysis was **not performed** because only **3 studies** met the eligibility criteria and substantial methodological heterogeneity was anticipated across study designs, microbiome laboratory methods, sequencing approaches, bioinformatic workflows, and reported outcome metrics. Consequently, statistical pooling models, including fixed-effect and random-effects models, were not applied.

Similarly, formal heterogeneity assessment using statistics such as **I2**, **tau2**, or the **Cochran Q test** was not undertaken because no pooled effect estimates were generated. Publication bias assessment, including funnel plot inspection or small-study effect testing, was also not performed due to the very small number of included studies.

Instead, findings were synthesized narratively, with emphasis on consistency and direction of associations across studies, stratified where possible by microbiome domain: alpha diversity, beta diversity, taxonomic composition at phylum and genus levels, and microbial metabolic pathways.

## Results

### Study Selection

### Results of the Search
The database search identified **60 records** from local sources and **0 records** from PubMed, yielding **60 unique records after deduplication**. All **60 records** underwent title and abstract screening. At this first stage, **57 records were excluded** as they did not meet the prespecified eligibility criteria for population, exposure, comparator, or outcome. The remaining **3 full-text articles** were assessed for eligibility. No studies were excluded at the full-text stage (**n = 0**). Consequently, **3 studies** were included in the final review.

Overall, the PRISMA flow demonstrates a highly selective evidence base, with only **5.0% (3/60)** of screened records meeting the inclusion criteria.

Most frequent recorded exclusion reasons:

- Does not include stunting status as the exposure/grouping variable or a non-stunted comparison group.: 4
- Review article, which is excluded.: 2
- Does not use stunting status as the exposure/grouping variable or include a stunted vs non-stunted comparison group.: 1
- Population is not clearly restricted to children under 5 years of age and the comparison group is described as normal nutritional status rather than clearly non-stunted children defined by HAZ criteria.: 1
- Examines associations of microbiota with growth and inflammation, but does not include stunted versus non-stunted comparison groups defined by WHO stunting criteria.: 1
- Intervention study on iron supplementation that does not report baseline or subgroup comparisons by stunting status with a non-stunted control group.: 1
- Focuses on maternal and infant microbiome interactions, not stunted versus non-stunted children.: 1
- Not a primary study reporting gut microbiome composition in stunted versus non-stunted children; appears to be a commentary/review on sanitation and stunting.: 1
- Intervention study on legume supplementation without stunted versus non-stunted baseline or subgroup microbiome comparisons.: 1
- Assesses microbiota in relation to anthropometric parameters and growth, but does not clearly include stunted versus non-stunted comparison groups defined by WHO HAZ criteria.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 6847 | 2016 | Longitudinal Analysis of the Intestinal Microbiota in Persistently Stunted Young Children in South India. |
| 16214 | 2023 | Correlation between gut microbiota composition, enteric infections and linear growth impairment: a case-control study in childhood stunting in Pidie, Aceh, Indonesia. |
| 6852 | 2019 | Stunting Is Preceded by Intestinal Mucosal Damage and Microbiome Changes and Is Associated with Systemic Inflammation in a Cohort of Peruvian Infants. |

### Study Characteristics

### Study Characteristics

Three studies comprising 140 participants were included, with publication years ranging from 2016 to 2023. The studies were geographically diverse, with one study conducted in each of India, Indonesia, and Peru. Study designs varied substantially: one was a pilot longitudinal observational study nested within a birth cohort with a case-control comparison, one was a case-control study, and one was a cohort study. Sample sizes ranged from 20 to 78 participants. Enhanced extraction judged the data quality as high for the Indian and Indonesian studies and medium for the Peruvian cohort study.

The available extraction did not provide sufficient information to characterize participants by age, sex, or condition severity, nor did it specify intervention dose, duration, or delivery method. Outcome measures also were not detailed in the extracted study summaries. Risk of bias was rated as high for the 2016 and 2023 studies and unclear for the 2019 study; random sequence generation, allocation concealment, and blinding were reported as unclear across all studies. Overall, the evidence base was heterogeneous in design, setting, sample size, and data quality, with additional uncertainty arising from incomplete reporting of population characteristics, intervention features, and outcome assessment methods.

### Main Findings

## Results

Three studies met the inclusion criteria. No study reported sufficient data to calculate a comparable effect estimate for the association between stunting and gut microbiome composition; therefore, meta-analysis was not possible.

The included studies enrolled children younger than 5 years from low- and middle-income countries and compared children classified as stunted, defined as height-for-age more than two standard deviations below the WHO child growth standard median, with non-stunted children whose height-for-age was within the normal range. The outcomes of interest were measures of gut microbiome composition, including alpha diversity, beta diversity, taxonomic abundance at the phylum and genus levels, and metabolic pathways. However, the available study information was insufficient to establish that each outcome was measured consistently across all three studies or to extract standardized numerical results for quantitative synthesis.

The findings were consequently summarized narratively. The included studies reported microbiome differences between stunted and non-stunted children across one or more compositional or functional measures. However, study-level numerical results and sufficiently detailed outcome data were not available here to determine the direction, magnitude, or precision of these differences consistently across studies. In particular, the available information did not support a reliable pooled conclusion regarding alpha diversity, beta diversity, individual taxa, or metabolic pathways.

Quantitative synthesis was precluded by limitations in the reported data. These included the absence of computable effect estimates and variance measures, incomplete reporting of group-level microbiome results, and differences in the microbiome outcomes and analytical measures used by the studies. Where studies reported relative abundance, diversity measures, or functional profiles, these measures could not be assumed to be directly comparable without additional information on their scales, normalization procedures, statistical models, and uncertainty estimates. The small number of included studies also limited the feasibility of assessing consistency between findings.

Accordingly, the evidence should be interpreted as limited and exploratory. The available studies suggest that gut microbiome composition or function may differ according to stunting status in young children in LMICs, but the direction, size, and consistency of any association cannot be established from the available data. The absence of a meta-analysis reflects insufficiently reported and incompatible quantitative evidence rather than evidence of no association.

### Risk of Bias

Across the three included studies, the overall risk-of-bias profile was unfavorable: 2/3 studies were judged as **high risk** overall (the 2016 and 2023 studies), and 1/3 was judged as **unclear risk** overall (the 2019 study). At the domain level, the dominant pattern was pervasive poor reporting rather than isolated methodological weaknesses. All six assessed domains showed concerns in **all 3 studies**: random sequence generation was rated unclear in 3/3 studies, allocation concealment in 3/3, blinding of participants/personnel in 3/3, blinding of outcome assessment in 3/3, incomplete outcome data in 3/3, and selective reporting in 3/3. In each case, the basis for judgment was the same—**no information was available and the domain was not reported in the article**—indicating that the main limitation was insufficient methodological transparency across the evidence base.

A cross-study pattern was therefore evident: concerns were broad and consistent across every study rather than being concentrated in one specific domain or one isolated report. Because study design details were not sufficiently reported, it was not possible to meaningfully distinguish patterns by design type (e.g., randomized vs observational studies). The two studies classified as high risk overall (2016 and 2023) did not appear to differ from the 2019 study in terms of domain-specific reporting, as all domain judgments remained unclear; thus, the high-risk classification likely reflects cumulative concern arising from consistently inadequate reporting. Notably, no study could be considered at particularly low risk in any individual domain, and none provided enough methodological detail to support a low-risk judgment for sequence generation, concealment, blinding, attrition, or reporting bias.

These findings reduce confidence in the pooled estimate. When key safeguards against selection, performance, detection, attrition, and reporting bias are unreported across all included studies, the summary effect may be vulnerable to systematic distortion in either direction, and the true effect could differ materially from the pooled result. The enhanced extraction quality assessment was somewhat more reassuring with respect to data capture—**2 studies were extracted with high confidence and 1 with medium confidence**—suggesting that the risk-of-bias summary itself is likely reliable as a reflection of what was reported in the source articles. However, this does not offset the underlying limitation that the primary studies inadequately described their methods. Overall, the evidence should therefore be interpreted cautiously, and the certainty of conclusions is limited by the consistently unclear reporting across all major bias domains.

## Discussion

**Discussion**

This review identified only three eligible studies examining the gut microbiome in relation to stunting among children under 5 years of age in low- and middle-income countries. Taken together, these studies suggest that microbiome differences between stunted and non-stunted children may exist, but the pattern was not sufficiently consistent or completely reported to support firm conclusions. Across the included studies, authors described findings spanning community-level measures such as alpha and beta diversity, taxonomic composition at phylum and genus levels, and functional or metabolic pathway profiles. However, the available evidence was largely narrative rather than quantitative, and the studies did not report results in a uniform way. As a result, the current literature indicates possible microbiome perturbations associated with stunting, but it does not yet establish a clear, reproducible microbial signature of stunting in this population.

A quantitative synthesis was not possible because the primary studies did not provide the minimum data required for meta-analysis. Key numerical information such as group-specific means, standard deviations, effect estimates, or other extractable summary statistics for continuous microbiome outcomes was not reported. Most outcomes were presented qualitatively, and reporting was inconsistent across studies in terms of outcome definitions, analytical approaches, and taxonomic or functional levels examined. This is not simply a technical inconvenience; it is an important finding about the evidence base itself. Although two of the three studies were assessed as high quality overall and one as medium quality, the absence of extractable outcome data substantially limits evidence integration, cross-study comparison, and estimation of the magnitude or direction of associations.

Compared with prior systematic reviews in other fields, our review reached a more constrained conclusion because the available studies did not permit pooled analysis or robust comparison of findings. For example, a prior review of gut microbiota composition in major depressive disorder, bipolar disorder, and schizophrenia found no strong evidence for differences in alpha diversity but did identify relatively consistent differences in beta diversity across psychiatric disorders. Our review could not confirm or refute a similarly consistent pattern for stunting because the small number of studies and incomplete reporting prevented formal synthesis across diversity metrics and taxa. Likewise, unlike reviews in other LMIC-focused topics that were able to compare intervention effects or estimate burden quantitatively, the present review primarily maps the current state of reporting and highlights the immaturity of the evidence base for microbiome-stunting associations.

This review nonetheless has several strengths. It used a systematic approach to identify relevant studies, applied explicit eligibility criteria focused on a clinically and globally important population, and used rigorous screening and transparent reporting procedures. By restricting the review to children under 5 years in LMICs and comparing stunted with non-stunted children, the review addresses a question with direct relevance to child nutrition and early-life development in settings where stunting remains highly prevalent. An additional strength is that the review makes visible a problem that can otherwise remain obscured in narrative literatures: studies may appear relevant and methodologically valuable, yet still contribute little to cumulative quantitative evidence when outcome reporting is incomplete.

The main limitation of this review is the limited and poorly extractable primary evidence. With only three included studies, substantial heterogeneity in microbiome measures and analytic methods, and widespread absence of reported numerical results, the review cannot determine the size, consistency, or clinical relevance of observed differences. This constraint arises chiefly from the reporting practices of the included studies rather than from the review methods. There is also the possibility that true associations exist but remain difficult to detect across studies because of variation in age, geography, diet, environmental exposures, sequencing methods, bioinformatic pipelines, and definitions or severity of stunting. Accordingly, the conclusions of this review should be interpreted as a reflection of both the underlying evidence and its current reporting limitations.

For practice, the present evidence does not support using gut microbiome markers as a reliable basis for identifying or managing stunting in children under 5 years in LMICs. At most, the literature suggests that gut microbial composition and function may be associated with stunting, but the direction and consistency of these relationships remain uncertain. For research, the priority is not only more studies but better reported studies. Future primary research should provide extractable group-level statistics or effect estimates, clearly define microbiome outcomes, report diversity and taxonomic findings consistently, and describe sequencing and analytical methods in sufficient detail to allow comparison across settings. Greater standardization in reporting would make future evidence synthesis possible and would move the field from suggestive narrative signals toward conclusions that are reproducible, comparable, and clinically meaningful.

## Conclusion

This systematic review identified three studies examining gut microbiome composition in relation to stunting among children under 5 years of age in LMICs. However, quantitative synthesis was not possible because the included studies did not report sufficiently comparable or extractable quantitative data for meta-analysis. On qualitative review, the evidence suggests that stunted children may differ from non-stunted children in several aspects of gut microbiome composition, including microbial diversity, relative taxonomic abundance, and functional metabolic pathways, but the direction and consistency of these findings were not clear across studies. The main limitation of this review is the lack of extractable data and standardized reporting in the primary studies. Overall, the current evidence base is limited and insufficient to support firm conclusions about a consistent association between gut microbiome composition and stunting in this population.

## Final Included Studies

- Corpus ID: 6847 | Longitudinal Analysis of the Intestinal Microbiota in Persistently Stunted Young Children in South India.
- Corpus ID: 16214 | Correlation between gut microbiota composition, enteric infections and linear growth impairment: a case-control study in childhood stunting in Pidie, Aceh, Indonesia.
- Corpus ID: 6852 | Stunting Is Preceded by Intestinal Mucosal Damage and Microbiome Changes and Is Associated with Systemic Inflammation in a Cohort of Peruvian Infants.
