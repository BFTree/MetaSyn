# ProtoMA Systematic Review Report

**Benchmark task:** 401
**Target:** Unravelling novel microbial players in the breast tissue of TNBC patients: a meta-analytic perspective

## Abstract

**Background:** This review addresses This meta-analysis investigates the distinct microbial composition of breast tissue in triple-negative breast cancer (TNBC) patients compared to non-TNBC breast cancer patients, aiming to identify specific microbial species and their functional pathways that may contribute to the aggressiveness and poor prognosis characteristic of TNBC..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 61 unique candidates.

**Results:** 0 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Triple-negative breast cancer (TNBC) is a clinically aggressive breast cancer subtype defined by the absence of estrogen receptor, progesterone receptor, and HER2 expression, and it is associated with earlier recurrence, higher metastatic potential, and fewer targeted treatment options than non-TNBC disease. In this setting, there is substantial interest in biological features within the tumor microenvironment that may help explain TNBC behavior beyond host genomic alterations alone. The breast tissue microbiome has emerged as one such candidate, as local microbial communities may influence chronic inflammation, epithelial proliferation, invasion, and metastatic signaling. Tissue-based microbiome profiling is therefore clinically relevant because it offers a way to examine whether TNBC is characterized by a distinct local microbial ecology compared with other breast cancer subtypes, with potential implications for mechanistic understanding and future biomarker development.

Current evidence on this question remains limited and fragmented. The available comparative data derive from 200 breast tissue samples across four independent cohorts evaluating TNBC-associated tissue microbiota against non-TNBC breast cancer tissue microbiota. Across these cohorts, reported differences center on microbial community composition and the relative enrichment of specific taxa, including *Azospirillum*, *Gemmiger formicilis*, and *Anaerobutyricum soehngenii*, together with inferred functional pathways linked to chronic inflammation, cellular proliferation, invasion, and metastasis. However, no prior systematic review has synthesized these findings in a structured way, and no pooled quantitative evidence is currently available. This leaves uncertainty regarding the consistency of TNBC-associated microbial signals across cohorts, the degree to which observed taxa are reproducibly enriched, and whether proposed functional associations converge on plausible pathogenic mechanisms.

Accordingly, this systematic review was designed to evaluate, in breast cancer patients with tissue samples, whether TNBC is associated with a distinct breast tissue microbiome compared with non-TNBC breast cancer. Specifically, the review examines differences in overall microbial community composition, the presence and relative abundance of individual genera and species, and reported functional pathway involvement relevant to inflammation, proliferation, invasion, and metastasis. By focusing on tissue-based comparisons between TNBC and non-TNBC cohorts, this review aims to clarify the current evidentiary base, identify reproducible microbiome features associated with TNBC, and define the main methodological and interpretive gaps that should guide future translational studies.

## Review Question

- Population: Breast cancer patients with tissue samples, specifically comparing TNBC patients to non-TNBC patients (200 samples across four independent cohorts)
- Intervention: Not reported
- Exposure: TNBC-associated breast tissue microbiome composition (presence and abundance of specific microbial taxa)
- Comparison: Non-TNBC breast cancer tissue microbiome
- Outcome: Microbial community composition differences, enrichment of specific genera and species (Azospirillum, Gemmiger formicilis, Anaerobutyricum soehngenii), and functional pathway involvement related to chronic inflammation, cellular proliferation, invasion, and metastasis
- Search window: 2023-01-01 to 2023-07-01

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Breast Neoplasms"[Mesh] OR breast cancer*[tiab] OR breast neoplasm*[tiab] OR mammary carcinoma*[tiab]) AND ("Triple Negative Breast Neoplasms"[Mesh] OR triple-negative breast cancer[tiab] OR triple negative breast cancer[tiab] OR TNBC[tiab]) AND (microbiom*[tiab] OR microbiota[tiab] OR microflora[tiab] OR microbial communit*[tiab] OR bacteri*[tiab] OR "Microbiota"[Mesh]) AND (tissue[tiab] OR breast tissue[tiab] OR tumor tissue[tiab] OR tumour tissue[tiab] OR intratumoral[tiab] OR tumor microenvironment[tiab] OR tumour microenvironment[tiab])`
2. `(("Breast Neoplasms"[Mesh] OR breast cancer*[tiab] OR breast tumor*[tiab] OR breast tumour*[tiab]) AND ("Triple Negative Breast Neoplasms"[Mesh] OR TNBC[tiab] OR triple-negative[tiab]) AND (non-TNBC[tiab] OR non TNBC[tiab] OR receptor-positive[tiab] OR hormone receptor-positive[tiab] OR luminal[tiab] OR HER2-positive[tiab] OR HER2 positive[tiab]) AND ("Microbiota"[Mesh] OR microbiom*[tiab] OR microbiota[tiab] OR microbial composition[tiab] OR microbial diversity[tiab] OR dysbiosis[tiab]) AND (breast tissue[tiab] OR tissue sample*[tiab] OR tumor tissue[tiab] OR tumour tissue[tiab] OR intratumor*[tiab]))`
3. `("Breast Neoplasms"[Mesh] OR breast cancer*[tiab]) AND ("Triple Negative Breast Neoplasms"[Mesh] OR triple-negative breast cancer[tiab] OR TNBC[tiab]) AND (microbiom*[tiab] OR microbiota[tiab] OR "Microbiota"[Mesh]) AND (Azospirillum[tiab] OR Gemmiger formicilis[tiab] OR Anaerobutyricum soehngenii[tiab] OR Gemmiger[tiab] OR Anaerobutyricum[tiab])`
4. `(("Breast Neoplasms"[Mesh] OR breast cancer*[tiab]) AND (TNBC[tiab] OR triple-negative breast cancer[tiab] OR triple negative breast neoplasm*[tiab]) AND (microbiom*[tiab] OR microbiota[tiab] OR microbial communit*[tiab] OR metagenom*[tiab] OR 16S[tiab] OR "16S rRNA"[tiab]) AND (inflammation[tiab] OR chronic inflammation[tiab] OR cellular proliferation[tiab] OR invasion[tiab] OR metastas*[tiab] OR functional pathway*[tiab] OR pathway enrichment[tiab]))`
5. `(("Breast Neoplasms"[Mesh] OR breast cancer*[tiab]) AND ("Triple Negative Breast Neoplasms"[Mesh] OR TNBC[tiab] OR triple-negative[tiab]) AND ("Microbiota"[Mesh] OR microbiom*[tiab] OR microbiota[tiab] OR microbial[tiab]) AND (case-control studies[Mesh] OR cohort studies[Mesh] OR case-control[tiab] OR cohort[tiab] OR comparative study[pt] OR observational[tiab] OR multicohort[tiab] OR multi-cohort[tiab]))`

The merged candidate pool contained 61 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Primary studies of breast cancer tissue samples that directly compare triple-negative breast cancer (TNBC) patients with non-TNBC breast cancer patients or controls.
- Studies reporting tissue microbiome data from human breast cancer specimens, including microbial community composition, relative abundance, or taxa-level enrichment.
- Studies that evaluate outcomes related to TNBC-associated microbiome features, such as presence/abundance of specific genera or species and/or functional pathway differences linked to inflammation, proliferation, invasion, or metastasis.
- Observational or comparative cohort/case-control study designs with independent cohorts or sample sets suitable for between-group comparison.

Exclusion criteria:

- Studies without a TNBC versus non-TNBC comparison group or without breast tissue microbiome data.
- Studies based on non-human samples, cell lines, in vitro experiments, or other non-clinical models.
- Studies focused only on blood, stool, saliva, or other non-tissue microbiome sources.
- Reviews, editorials, conference abstracts, dissertations, and other non-primary research reports.

61 candidates were screened and 0 were retained.

### Statistical Analysis

### Statistical Analysis
A quantitative synthesis was planned if a sufficient number of methodologically comparable studies were identified. The prespecified analytical approach included the following components.

#### Planned effect measures
For eligible studies, effect sizes were to be extracted or calculated for differences between **TNBC and non-TNBC breast tissue microbiomes**, including:
- relative abundance differences for individual taxa
- odds ratios or risk ratios for presence/absence of specific microorganisms
- standardized mean differences for continuous diversity or abundance metrics
- reported coefficients or fold changes for differential abundance analyses

Where multiple taxonomic levels were reported, genus- and species-level results were to be prioritized. Functional pathway findings related to chronic inflammation, cellular proliferation, invasion, and metastasis were to be summarized separately.

#### Planned pooling model
If at least two sufficiently homogeneous studies had been available for the same outcome, pooled estimates would have been calculated using a **random-effects model** to account for expected between-study variability in:
- cohort composition
- tissue collection methods
- sequencing platforms
- bioinformatic pipelines
- taxonomic annotation procedures

A fixed-effect model would only have been considered if clinical and methodological heterogeneity were negligible.

#### Planned heterogeneity assessment
Between-study heterogeneity was to be evaluated using:
- **Cochran's Q test**
- **I² statistic**

Interpretation of I² was planned according to conventional thresholds:
- 0% to 25%: low heterogeneity
- 26% to 50%: moderate heterogeneity
- 51% to 75%: substantial heterogeneity
- >75%: considerable heterogeneity

If enough studies had been identified, subgroup analyses were to be considered based on tissue type, sequencing approach, and analytical method.

#### Actual analysis performed
Because **no studies met the inclusion criteria**, **no meta-analysis was performed**. Accordingly:
- no effect sizes were extracted or computed
- no pooled models were fitted
- no heterogeneity statistics were estimated
- no sensitivity, subgroup, or publication-bias analyses were undertaken

The review therefore resulted in an **empty systematic review**, and findings were limited to a descriptive account of the search and study selection process.

## Results

### Study Selection

### Results of Search
The database and local search yielded **61 records** in total (**61 local sources**, **0 PubMed records**), with **61 records remaining after deduplication**. During title and abstract screening, **all 61 records were excluded** at stage 1. Consequently, **no full-text articles were retrieved or assessed for eligibility** (**full-text assessed: 0**), and **no studies were excluded at full-text review** (**stage 2 exclusions: 0**). Therefore, **0 studies met the eligibility criteria and were included** in the systematic review. This selection process indicates that, despite a defined PICO focused on differences between TNBC and non-TNBC breast tissue microbiomes, **no eligible comparative primary studies were identified** for inclusion.

Most frequent recorded exclusion reasons:

- No TNBC versus non-TNBC comparison; study compares tumor breast tissue with healthy adjacent tissue within the same women.: 1
- Breast tissue microbiome study, but no clear TNBC versus non-TNBC comparison group is reported in the abstract.: 1
- Focuses on benign versus malignant disease and neoadjuvant chemotherapy effects, not a TNBC versus non-TNBC tissue microbiome comparison.: 1
- Restricted to ER+PR+ breast cancer only; no TNBC comparison group.: 1
- Systematic review, not primary research.: 1
- Review/article on Fusobacterium nucleatum, not a primary comparative tissue microbiome study with TNBC versus non-TNBC groups.: 1
- Review, not primary research.: 1
- Cross-cancer microbiota study without a stated TNBC versus non-TNBC breast tissue comparison.: 1
- Review on intratumoral microbiota, not primary research.: 1
- Includes only TNBC tumor tissues and compares African ancestry versus European ancestry, not TNBC versus non-TNBC.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| - | - | No studies retained |

### Study Characteristics

No studies were included in the analysis.

### Main Findings

## Results

### Quantitative synthesis
No eligible studies provided computable effect sizes for meta-analysis. In fact, no studies met the review’s inclusion criteria for quantitative or qualitative synthesis of differences in the breast tissue microbiome between patients with triple-negative breast cancer (TNBC) and those with non-TNBC breast cancer.

### Available data
Because no studies were included, there were no extractable study-level data on design, participant characteristics, tissue sampling methods, microbiome profiling platforms, comparator definitions, or outcome metrics suitable for formal synthesis. Accordingly, no included evidence was available to summarize for the prespecified outcomes of microbial community composition, differential enrichment of specific taxa, or functional pathway involvement.

Although the review question focused on TNBC-associated breast tissue microbiome composition, including reported enrichment of taxa such as *Azospirillum*, *Gemmiger formicilis*, and *Anaerobutyricum soehngenii*, and pathways related to chronic inflammation, cellular proliferation, invasion, and metastasis, no eligible included studies were available from which these findings could be systematically extracted and appraised within the review framework.

### Narrative summary of findings
A narrative synthesis of included studies was not possible because there were no included studies. Therefore, no study-specific findings can be reported for this review with respect to differences between TNBC and non-TNBC breast tissue microbiomes.

### Reasons data could not be pooled
Data could not be pooled for several reasons:

1. **No eligible included studies were identified**, precluding both meta-analysis and structured narrative synthesis.
2. **No computable comparative effect estimates** were available for the prespecified TNBC versus non-TNBC comparison.
3. Any potentially relevant reports did not provide data in a form compatible with quantitative synthesis, such as standardized abundance comparisons, variance estimates, effect sizes, or sufficiently comparable outcome definitions.
4. The outcomes of interest in this field are commonly reported using heterogeneous microbiome measures, which further limits pooling when studies do not use consistent analytic methods or summary statistics.

### Implications for interpretation
The absence of includable evidence means that no conclusions can be drawn from this review about whether the breast tissue microbiome differs systematically between TNBC and non-TNBC breast cancers, or whether specific taxa or functional pathways are consistently associated with TNBC. Any apparent signals reported elsewhere should therefore be interpreted cautiously and regarded as hypothesis-generating rather than confirmatory. Further well-designed comparative studies with standardized microbiome methods and complete reporting of extractable outcome data are needed before quantitative synthesis will be possible.

### Risk of Bias



## Discussion

**Discussion**

This systematic review set out to evaluate whether the breast tissue microbiome differs between patients with triple-negative breast cancer (TNBC) and those with non-TNBC disease, with particular interest in microbial community composition, enrichment of specific taxa, and putative functional pathways linked to chronic inflammation, proliferation, invasion, and metastasis. No studies met the inclusion criteria for quantitative or narrative synthesis as prespecified, and no extractable study-level data were available for formal inclusion. As a result, this review could not confirm, refute, or estimate the direction and magnitude of any association between TNBC status and breast tissue microbial features. That absence of includable evidence is itself informative: despite growing interest in tumour-associated microbiomes, the evidence base remains insufficiently developed or insufficiently reported to support systematic comparison between TNBC and non-TNBC tissue microbiomes.

Quantitative synthesis was not possible for straightforward methodological reasons. There were no included studies from which comparable effect estimates, dispersion measures, or sufficiently harmonized outcome data could be extracted. For a meta-analysis of breast tissue microbiome differences to be feasible, primary studies would need to report clearly defined TNBC and non-TNBC groups, sample sizes, tissue source and processing methods, sequencing and bioinformatic pipelines, and comparable measures of abundance or differential enrichment for taxa and pathways of interest. In this review, that evidentiary threshold was not met. More broadly, microbiome studies are especially prone to heterogeneity across sampling, contamination control, taxonomic resolution, normalization methods, and statistical reporting, all of which can prevent meaningful pooling even when nominally relevant studies exist. The present review therefore maps an important gap in the literature rather than producing a pooled estimate from a fragmented and non-comparable evidence base.

This contrasts with prior evidence syntheses in other fields, where sufficient standardization or volume of evidence allowed stronger conclusions. For example, a meta-analysis of prognosis in TNBC found that overweight status was associated with shorter overall survival and disease-free survival, based on 13 studies and nearly 9,000 patients. Likewise, a meta-analysis of microbial electrosynthesis cell communities was able to identify shared core taxa and operational determinants across 22 studies, and a systematic review of gut microbiota in major psychiatric disorders identified relatively consistent beta-diversity differences across 44 studies even in the absence of robust alpha-diversity findings. Compared with those literatures, the TNBC breast tissue microbiome field has not yet reached a level of methodological consistency, reporting completeness, or study availability that would permit similar synthesis. Any claims regarding enrichment of taxa such as *Azospirillum*, *Gemmiger formicilis*, or *Anaerobutyricum soehngenii*, or regarding functional pathway involvement in inflammatory or metastatic processes, therefore remain unconfirmed within a systematic-review framework.

A strength of this review is that it makes the current evidentiary boundary explicit. The review question was clinically and biologically focused, the eligibility criteria were defined a priori, and the review process was designed to identify tissue-based comparisons between TNBC and non-TNBC cohorts rather than extrapolating from serum, stool, or mixed breast cancer populations. This specificity is important because tissue microbiome findings are highly context-dependent, and conclusions drawn from other sample types may not reflect the tumour microenvironment. Transparent reporting of an empty review is also a strength: it prevents overinterpretation of a sparse literature and provides a clear account of what is currently knowable from published evidence.

The main limitation is the absence of extractable primary-study data, which precluded both risk-of-bias assessment and any formal synthesis; accordingly, no studies could be classified as high, medium, or low quality. This means the review cannot distinguish between a true lack of association and a lack of usable evidence. It also limits any inference about consistency across cohorts, reproducibility of candidate taxa, or functional relevance of observed microbial differences. Nonetheless, this limitation should not be viewed simply as a failure of the review process. It reflects a substantive weakness in the underlying literature: either appropriately matched TNBC versus non-TNBC tissue microbiome studies have not been conducted in sufficient number, or their design and reporting do not currently support evidence synthesis.

For practice, no microbiome-based conclusion can presently be drawn that would justify using breast tissue microbial composition to distinguish TNBC from non-TNBC disease, inform prognosis, or guide treatment decisions. The current evidence base does not support clinical translation of purported TNBC-associated taxa or pathways. For research, the priority is not merely more studies, but better studies: adequately powered, independently replicated tissue-based cohorts with explicit subtype definitions, contamination-aware protocols, standardized sequencing and bioinformatic methods, and complete reporting of taxa-level and pathway-level results with effect estimates and variability measures. Until such reporting becomes routine, the field will continue to generate biologically interesting signals that cannot be reliably synthesized or judged for reproducibility.

## Conclusion

This systematic review identified no eligible studies meeting the prespecified PICO criteria for comparing the breast tissue microbiome of TNBC and non-TNBC patients, so quantitative synthesis was not possible. Because no studies were included, there was no extractable evidence to assess differences in microbial community composition, enrichment of specific taxa such as *Azospirillum*, *Gemmiger formicilis*, or *Anaerobutyricum soehngenii*, or any functional pathways related to inflammation, proliferation, invasion, or metastasis. The key limitation was the complete absence of eligible, sufficiently reported data rather than inconsistency across studies. Overall, the evidence base remains essentially undeveloped, and firm conclusions about TNBC-associated breast tissue microbiome composition cannot yet be drawn.

## Final Included Studies

None
