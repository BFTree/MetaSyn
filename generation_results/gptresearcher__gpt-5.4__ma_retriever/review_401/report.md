# Systematic Review Report: Breast Tissue Microbiome in Triple-Negative Versus Non-TNBC Breast Cancer in the Local MetaSyn Corpus

## Abstract

This report evaluates whether the local MetaSyn PubMed corpus contains eligible primary studies for a systematic review and meta-analysis of breast tissue microbiome differences between triple-negative breast cancer (TNBC) and non-TNBC breast cancer, with emphasis on *Azospirillum*, *Gemmiger formicilis*, *Anaerobutyricum soehngenii*, and pathways linked to inflammation, proliferation, invasion, and metastasis. I used only the local corpus search output provided in the prompt and screened candidate records against the prespecified eligibility criteria. The result is straightforward: no study in the retrieved local corpus meets the full inclusion criteria within the search window of January 1, 2023 to July 1, 2023. The nearest subtype-specific breast tissue study is a 2025 TNBC metatranscriptomic analysis showing ancestry-associated intratumoral microbial differences, but it falls outside the date window and does not use 16S rRNA Illumina V4 or V3-V4 tissue sequencing comparing TNBC to non-TNBC. Broader breast tissue studies do support tumor-associated microbiome differences and subgroup-specific patterns, but they do not establish the query’s named taxa as TNBC-enriched tissue microbes. My assessment is that the claimed TNBC-specific microbial signature centered on *Azospirillum*, *Gemmiger formicilis*, and *Anaerobutyricum soehngenii* is not substantiated by the retrieved local corpus. The evidence base, as retrieved, supports biological plausibility for intratumoral microbiome effects in breast cancer, but not the specific meta-analytic claim posed here.

## Introduction

The tumor microbiome has moved from a controversial finding to a recognized component of the tumor microenvironment across multiple solid tumors. Intratumoral microbes are now discussed as potential modifiers of tumor growth, metastasis, immune contexture, and treatment response rather than as passive contaminants alone ([Frontiers in Microbiology, 2025](metasyn://corpus/66322)). At the same time, low microbial biomass in tumor tissue makes this field unusually vulnerable to contamination, inconsistent pipelines, and irreproducibility, which sharply limits confidence in isolated taxa-level claims ([Frontiers in Cellular and Infection Microbiology, 2025](metasyn://corpus/83368)).

The present review was framed by a highly specific question: whether breast tissue microbiome studies comparing TNBC and non-TNBC identify enrichment of *Azospirillum*, *Gemmiger formicilis*, and *Anaerobutyricum soehngenii*, and whether these taxa map to functional programs plausibly linked to TNBC aggressiveness. The eligibility criteria were narrow and methodologically restrictive: tissue microbiome studies, case-control or cohort design, breast cancer subtype inclusion, Illumina 16S rRNA sequencing covering V4 or V3-V4, homogeneous available data, and no recent antibiotic exposure. Because the corpus search results are the only allowed retrieval source, this report is limited to what those records contain.

## Methods

### Retrieval source

Only the local MetaSyn corpus search results supplied in the prompt were used. No external databases, websites, or inferred references were added.

### Search queries used

The following local corpus search queries were used, exactly as provided in the retrieval context:

1. `triple-negative breast cancer tumor tissue shotgun metagenomics metatranscriptomics contamination-controlled Azospirillum Gemmiger formicilis Anaerobutyricum soehngenii intratumoral microbiome`
2. `TNBC intratumoral microbiome Azospirillum Gemmiger formicilis Anaerobutyricum soehngenii NF-kappaB EMT Wnt beta-catenin macrophage polarization cytokine chemokine co-culture organoid`

### Screening approach

Records were screened in two stages:

1. **Title/abstract-level screening** using the candidate list and abstracts in the search results.
2. **Eligibility assessment** against the protocol:
   - Date window: 2023-01-01 to 2023-07-01
   - Primary case-control or cohort study
   - Tissue microbiome samples
   - 16S rRNA with Illumina platform covering V4 or V3-V4
   - Included breast cancer subtypes
   - Data available and reasonably homogeneous
   - No recent antibiotic administration within three months before sampling
   - Publicly accessible data or metadata

### Important constraint

Several relevant records are from 2025 and therefore outside the search window. They are discussed as contextual evidence but were excluded from inclusion.

## Retrieval Results

The provided searches returned 20 candidate records per query. The most relevant breast-cancer-related records from the returned candidate lists were:

| Corpus ID | Year | Study type / scope | Immediate relevance |
|---|---:|---|---|
| 16181 | 2025 | TNBC tumor metatranscriptomics | Most directly TNBC-specific, but outside date window and wrong assay |
| 16197 | 2025 | Breast cancer vs adjacent normal tissue, 16S tissue study with subtype stratification | Relevant to subtype analysis, but outside date window and variable-region details do not match V4/V3-V4 requirement |
| 6845 | 2022 | Case-control breast normal adipose tissue 16S study | Relevant tissue microbiome context, but outside date window and not TNBC-vs-non-TNBC |
| 6846 | 2022 | Paired tumor vs adjacent healthy breast tissue NGS study | Relevant tissue context, but outside date window and not subtype-comparative |
| 16198 | 2025 | Systematic review | Not a primary study |
| 66322 | 2025 | Review on intratumoral microbiota | Not a primary study |
| 83368 | 2025 | Methods/review on intratumoral microbiota | Not a primary study |
| 100111 | 2023 | Review on *Fusobacterium nucleatum* in breast cancer | Within approximate year but not a primary subtype-comparison study |

## Screening and Eligibility Assessment

### Excluded at full screening

#### 1. Race-related host and microbe transcriptomic signatures in triple-negative breast cancer (Corpus ID: 16181)

This is the closest TNBC-specific hit in the local corpus. It profiled TNBC tumor tissues from women of African and European ancestry and found *Hafnia* and *Cedecea* more abundant in African-ancestry tumors and *Erwinia* higher in European-ancestry tumors, with immune cell differences and an association between *Hafnia*, SPDYE2B expression, and poorer disease-free survival ([NPJ Breast Cancer, 2025](metasyn://corpus/16181)). It was excluded because:
- It is outside the date window.
- It compares ancestry groups within TNBC, not TNBC versus non-TNBC.
- It uses meta-transcriptomics rather than 16S Illumina V4/V3-V4.

#### 2. Microbial community profiles in breast cancer and normal adjacent tissues: associations with clinicopathological characteristics (Corpus ID: 16197)

This 2025 study analyzed 31 breast cancer tumor and adjacent normal tissues by 16S rRNA across five variable regions using the SMURF framework. It found no overall alpha/beta diversity difference between cancer and adjacent tissue, but *Flavobacteriales*, *Comamonas*, and *Delftia* were enriched in tumors; *Brevundimonas* dominated the high-Ki-67 subgroup with predicted enrichment of glycolysis/gluconeogenesis, bacterial toxins, and isoflavonoid biosynthesis pathways ([Translational Cancer Research, 2025](metasyn://corpus/16197)). It was excluded because:
- It is outside the date window.
- It is not a TNBC-vs-non-TNBC comparison in the abstracted results.
- It used five variable regions, not specifically V4 or V3-V4 as required.

#### 3. Breast microbiome associations with breast tumor characteristics and neoadjuvant chemotherapy: A case-control study (Corpus ID: 6845)

This 2022 case-control study used 16S sequencing of breast normal adipose tissues from malignant and benign cases. It found lower Proteobacteria and higher Firmicutes in malignant cases, plus a positive correlation between tumor grade and *Streptococcus* abundance ([Frontiers in Oncology, 2022](metasyn://corpus/6845)). It was excluded because:
- It is outside the date window.
- It compares malignant versus benign/control tissue, not TNBC versus non-TNBC.
- The abstract does not establish the required subtype-comparative design.

#### 4. Microbiome composition indicate dysbiosis and lower richness in tumor breast tissues compared to healthy adjacent paired tissue, within the same women (Corpus ID: 6846)

This 2022 paired-tissue study found lower ASV richness in tumor tissues than adjacent healthy tissues, with healthy tissue having higher Actinobacteria and Proteobacteria relative to tumor tissue ([BMC Cancer, 2022](metasyn://corpus/6846)). It was excluded because:
- It is outside the date window.
- It is tumor-vs-adjacent, not TNBC-vs-non-TNBC.
- Sequencing and variable-region details required by the protocol are not demonstrated in the prompt.

#### 5. Fusobacterium nucleatum: a novel immune modulator in breast cancer? (Corpus ID: 100111)

This 2023 record is a review, not a primary study. It summarizes evidence that *F. nucleatum* is enriched in breast tumor tissue and may promote growth, metastasis, immune escape, and inflammatory signaling ([Expert Reviews in Molecular Medicine, 2023](metasyn://corpus/100111)). It was excluded because it is not a primary cohort or case-control study.

### Reviews and pan-cancer records excluded

Records 66322, 83368, 16198, 44011, 16192, and others were useful for contextual interpretation but are not eligible primary studies for the target question.

## Results of the Review

## No Included Studies

After applying the stated criteria, **no study from the retrieved local MetaSyn corpus was eligible for inclusion**.

That means:
- No included breast tissue study comparing **TNBC vs non-TNBC** was found in the specified search window.
- No included study supported the named taxa **Azospirillum**, **Gemmiger formicilis**, or **Anaerobutyricum soehngenii** as TNBC-associated tissue microbes.
- No quantitative meta-analysis could be performed from the retrieved corpus because the set of included studies is empty.

This is not a near miss. It is a direct contradiction between the narrow review question and the evidence retrievable under the local corpus constraints.

## Evidence Synthesis From Excluded but Informative Records

Although no eligible study was included, the broader retrieved literature still helps characterize the evidence landscape.

### 1. TNBC-specific tissue microbiome evidence exists, but not in the required form

The strongest TNBC-specific record in the corpus is the 2025 metatranscriptomic study (Corpus ID: 16181). It indicates that intratumoral microbial transcripts differ across ancestry groups in TNBC, with *Hafnia* and *Cedecea* elevated in African-ancestry tumors and *Erwinia* elevated in European-ancestry tumors. It also links microbial differences to immune contexture: African-ancestry TNBC had higher Th1 abundance, while European-ancestry TNBC showed higher M2 macrophage abundance. Importantly, high SPDYE2B expression associated with *Hafnia* abundance and worse disease-free survival ([NPJ Breast Cancer, 2025](metasyn://corpus/16181)).

This matters because it demonstrates that TNBC intratumoral microbiology may be clinically meaningful. But it does **not** validate the specific taxa in the query, and it does **not** provide the required TNBC-versus-non-TNBC 16S tissue comparison.

### 2. Breast tissue microbiome studies support dysbiosis, but with inconsistent direction and taxa

Breast tissue studies in the corpus suggest real but inconsistent tumor-associated microbial differences. One paired tissue study found lower richness in tumor tissue and shifts in Proteobacteria and Actinobacteria ([BMC Cancer, 2022](metasyn://corpus/6846)). Another study of breast normal adipose tissue found lower Proteobacteria and higher Firmicutes in malignant versus benign cases, plus grade-associated *Streptococcus* enrichment ([Frontiers in Oncology, 2022](metasyn://corpus/6845)). A later 2025 tissue study found no overall alpha/beta diversity difference but detected taxon-level enrichment of *Flavobacteriales*, *Comamonas*, and *Delftia* in tumors ([Translational Cancer Research, 2025](metasyn://corpus/16197)).

Taken together, the pattern is that broad diversity metrics are often unhelpful, while subgroup analysis and specific taxa/pathway comparisons are more informative. However, there is no reproducible genus-level consensus across studies, which is reinforced by the 2025 systematic review noting that no genus was consistently linked to the same outcome across breast cancer studies ([BMC Women's Health, 2025](metasyn://corpus/16198)).

### 3. Functional plausibility is stronger than taxonomic certainty

The mechanistic branch of the retrieved evidence is more coherent than the taxonomic branch. Reviews across intratumoral microbiota research indicate that tumor-resident microbes can shape cancer progression through inflammatory signaling, immune polarization, oncogenic pathway activation, altered autophagy, and effects on metastasis ([Frontiers in Microbiology, 2025](metasyn://corpus/66322); [World Journal of Gastrointestinal Oncology, 2025](metasyn://corpus/44011)). Specific mechanisms highlighted include NF-kappaB activation, M2 macrophage polarization, and autophagy-related drug resistance ([World Journal of Gastrointestinal Oncology, 2025](metasyn://corpus/44011)).

That mechanistic plausibility supports testing whether TNBC-associated microbes could influence aggressiveness. But plausibility is not evidence. In this corpus, the functional claim outruns the taxonomic data for TNBC.

### 4. The named taxa in the review question are unsupported in the retrieved corpus

The prompt’s hierarchical evidence summary already makes this point, and the candidate records confirm it: direct evidence for *Azospirillum*, *Gemmiger formicilis*, and *Anaerobutyricum soehngenii* in TNBC tumor tissue was not identified in the retrieved local corpus. My conclusion is that, within this evidence frame, these taxa should be treated as **unverified candidate claims** rather than established TNBC tissue biomarkers.

## Limitations

This review has several important limitations.

First, it is constrained to the **local MetaSyn corpus search output provided** and cannot use external retrieval. Second, several records are **abstract-only in practical terms** because the prompt provides candidate summaries but not extracted full sections, even when sections are available in the corpus listing. Third, low-biomass intratumoral microbiome work is especially vulnerable to contamination and analytic heterogeneity, which weakens confidence in isolated taxa-level findings ([Frontiers in Cellular and Infection Microbiology, 2025](metasyn://corpus/83368)). Fourth, the date window is narrow and excludes the most relevant TNBC-specific study in the retrieved corpus. Fifth, the protocol’s sequencing constraints are very specific; many otherwise relevant studies do not demonstrate V4 or V3-V4 Illumina coverage in the provided abstracted material.

## Conclusion

The local MetaSyn corpus, searched only through the provided retrieval results, does **not** support inclusion of any primary study for a meta-analysis comparing TNBC versus non-TNBC breast tissue microbiomes under the stated eligibility criteria. No eligible study was retrieved from the January 1, 2023 to July 1, 2023 window. The specific taxa named in the research question, *Azospirillum*, *Gemmiger formicilis*, and *Anaerobutyricum soehngenii*, are not substantiated in the returned TNBC tissue literature. The strongest TNBC-specific evidence in the corpus instead points to ancestry-associated intratumoral microbial transcripts involving *Hafnia*, *Cedecea*, and *Erwinia*, along with immune-contexture and disease-free-survival associations ([NPJ Breast Cancer, 2025](metasyn://corpus/16181)).

My concrete judgment is that the proposed meta-analytic claim is currently not evidentially supportable from the retrieved local corpus. The field does support a broader proposition: breast tumor tissues harbor microbiome differences, and intratumoral microbes may plausibly contribute to aggressive biology through immune and inflammatory pathways. But the narrower proposition that TNBC tissue is specifically characterized by *Azospirillum*, *Gemmiger formicilis*, and *Anaerobutyricum soehngenii* relative to non-TNBC is not demonstrated here.

## Included Study List

**No study was included.**

## References

Frontiers in Oncology. (2022). *Breast microbiome associations with breast tumor characteristics and neoadjuvant chemotherapy: A case-control study.* [metasyn://corpus/6845](metasyn://corpus/6845)

BMC Cancer. (2022). *Microbiome composition indicate dysbiosis and lower richness in tumor breast tissues compared to healthy adjacent paired tissue, within the same women.* [metasyn://corpus/6846](metasyn://corpus/6846)

Expert Reviews in Molecular Medicine. (2023). *Fusobacterium nucleatum: a novel immune modulator in breast cancer?* [metasyn://corpus/100111](metasyn://corpus/100111)

NPJ Breast Cancer. (2025). *Race-related host and microbe transcriptomic signatures in triple-negative breast cancer.* [metasyn://corpus/16181](metasyn://corpus/16181)

Translational Cancer Research. (2025). *Microbial community profiles in breast cancer and normal adjacent tissues: associations with clinicopathological characteristics.* [metasyn://corpus/16197](metasyn://corpus/16197)

BMC Women's Health. (2025). *Breast cancer and microbiome: a systematic review highlighting challenges for clinical translation.* [metasyn://corpus/16198](metasyn://corpus/16198)

Frontiers in Microbiology. (2025). *Intratumoral microbiota: implications for cancer progression and treatment.* [metasyn://corpus/66322](metasyn://corpus/66322)

Frontiers in Cellular and Infection Microbiology. (2025). *Emerging technologies and current challenges in intratumoral microbiota research.* [metasyn://corpus/83368](metasyn://corpus/83368)

World Journal of Gastrointestinal Oncology. (2025). *Tumor-resident microorganisms as clinical biomarkers in primary liver cancer: A systematic review of current evidence.* [metasyn://corpus/44011](metasyn://corpus/44011)