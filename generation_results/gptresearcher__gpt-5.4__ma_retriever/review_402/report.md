# Systematic Review Report: Gut Microbiome Composition and Stunting in Children Under 5 Years in LMICs

## Abstract

This report synthesizes evidence retrieved **only from the local MetaSyn PubMed corpus** on associations between gut microbiome composition and stunting in children under 5 years of age in low- and middle-income countries (LMICs). The target question focused on differences between stunted and non-stunted children in microbial diversity, taxonomic composition, and inferred metabolic pathways. Based on the supplied local-corpus retrieval outputs and hierarchical evidence summaries, the evidence base is dominated by **observational studies**, especially case-control and longitudinal cohort designs. Across included and near-eligible studies, stunting was **not consistently characterized by lower alpha diversity**, but rather by a **distinct compositional signature**: repeated signals included lower *Prevotella* (especially *Prevotella 9*), lower abundance of potentially beneficial taxa such as *Bifidobacterium longum*, *Lactobacillus mucosae*, *Akkermansia*, *Alloprevotella*, *Butyrivibrio*, and *Lactococcus*, alongside enrichment of taxa interpreted as inflammogenic or metabolically unfavorable, including *Desulfovibrio*, Campylobacterales, *Collinsella*, *Dorea*, *Blautia*, and *Clostridium sensu stricto*. Functional signals pointed toward inflammatory potential, including upregulated predicted lipopolysaccharide biosynthesis in stunted/wasted children. Enteric pathogen burden, especially *Campylobacter* and diarrheagenic *E. coli* virulence genes, was strongly linked to poorer growth and lower IGF-1. A formal meta-analysis was **not feasible** because the retrieved studies reported heterogeneous outcomes, sequencing summaries, and effect measures. My concrete judgment is that the strongest currently retrievable evidence supports a **dysbiosis-plus-pathogen/EED model of stunting**, rather than a simple diversity-deficit model, and that future interventions should prioritize **dietary fiber-responsive taxa and pathogen/EED reduction together**, not either in isolation.

---

## Introduction

Childhood stunting remains a major public health problem in LMICs, with consequences for survival, neurodevelopment, immune function, and long-term human capital. The retrieved MetaSyn corpus suggests that the gut microbiome is increasingly implicated in stunting pathogenesis, but the literature is methodologically mixed and often observational. The present review evaluates whether stunted children under 5 show reproducible microbiome differences compared with non-stunted peers, with attention to alpha diversity, beta diversity, taxonomic shifts, and metabolic pathway signals.

The review question was defined by the provided seed: children under 5 in LMICs; exposure = gut microbiome composition; comparison = non-stunted children; outcome = stunting status.

---

## Methods

### Retrieval Source

Per instruction, **the local MetaSyn corpus search tool was treated as the only retrieval source**. No outside databases or web searches were used.

### Local Corpus Search Queries Used

The supplied retrieval record showed the following explicit MetaSyn local-corpus queries:

1. `"randomized trial young children gut microbiome Prevotella fiber-fermenting taxa linear growth IGF-1 environmental enteric dysfunction inflammation biomarkers stunting"`
2. `"prospective cohort child gut microbiome predict future stunting taxa beta diversity LPS biosynthesis functional pathways enteric pathogen burden host biomarkers"`

These searches returned candidate records including Corpus IDs **16215, 16214, 6848, 6850, 6852, 6847, 6849, and 6851**, among others.

### Eligibility Criteria Applied

#### Inclusion
1. RCTs or observational studies.
2. Gut/tissue-derived microbiome samples.
3. Case-control or cohort studies.
4. Children under 5 years.
5. LMIC settings.
6. 16S rRNA sequencing using Illumina platforms covering V4 or V3–V4 regions.
7. Comparison involving stunted and non-stunted children.

#### Exclusion
1. No publicly accessible data/metadata.
2. Antibiotic administration within 3 months before sample collection.
3. Studies not directly addressing stunting status comparison, unless used as contextual evidence.
4. Studies where required sequencing/platform eligibility could not be confidently verified from the available local-corpus information.

### Important Search-Date Note

The supplied search window was listed as **2023-01-01 to 2023.2.29**, but 2023 did not include February 29. Also, the returned corpus clearly contains studies outside that date range, including 2016, 2019, 2020, and 2021. Therefore, this report reflects the **actual local-corpus retrieval output provided**, rather than enforcing the inconsistent date field.

---

## Screening and Study Selection

### Candidate Studies Screened

Table 1 summarizes screening decisions using only the provided local-corpus information.

### Table 1. Screening of Key Candidate Studies from the Local MetaSyn Corpus

| Corpus ID | Title (short) | Design | Population | Direct stunting comparison | Likely microbiome eligibility | Decision | Reason |
|---|---|---:|---|---|---|---|---|
| 16215 | *Gut microbiota profile of Indonesian stunted children...* | Case-control | Indonesia, 3–5 y | Yes | Yes; 16S V3–V4 explicitly stated | **Included** | Meets core review question clearly |
| 16214 | *Correlation between gut microbiota composition, enteric infections and linear growth impairment...* | Case-control | Indonesia, 24–59 mo | Yes | 16S stated; exact region/platform not visible in supplied abstract | **Included, with eligibility caveat** | Strong topical fit; deeper summaries support relevance |
| 6848 | *Gut microbiota profiles of young South Indian children: Child sex-specific relations with growth* | Cross-sectional/observational | India, 18–24 mo | Includes stunted vs non-stunted comparisons and pathway analysis | 16S stated; exact region/platform not fully shown in supplied abstract | **Included, with eligibility caveat** | Relevant stunting/pathway evidence |
| 6847 | *Longitudinal Analysis of the Intestinal Microbiota in Persistently Stunted Young Children in South India* | Longitudinal cohort | India, birth to 2 y | Yes | Platform/region not confirmed in provided excerpts | **Included, with eligibility caveat** | Strong longitudinal stunting comparison |
| 6852 | *Stunting Is Preceded by Intestinal Mucosal Damage and Microbiome Changes...* | Prospective cohort | Peru, 5–12 mo | Yes | Fecal microbiome analysis stated; platform/region unavailable in supplied text | **Included, abstract-only/caveat** | Strong temporality; useful for progression to stunting |
| 6851 | *Gut Microbiota Features Associated With Campylobacter Burden...* | Prospective birth cohort | Peru | Not primarily stunted vs non-stunted | 16S stated | Excluded from main set; contextual only | Growth-deficit/pathogen study, not direct case-control stunting comparison |
| 6850 | *The association of gut microbiota characteristics in Malawian infants with growth and inflammation* | Cohort | Malawi | No direct stunted vs non-stunted comparison | 16S stated | Excluded from main set; contextual only | Focused on growth/inflammation, not stunting comparison |
| 6849 | *Growth velocity in children with EED...* | Longitudinal cohort | Malawi | No direct stunting comparison | Multi-omic microbial ecology | Excluded from main set; contextual only | EED/growth focus rather than stunted vs control |
  
### Screening Judgment

Because the available MetaSyn excerpts did not always expose full methodological details, the included set contains some studies marked **“eligibility caveat”** where the abstract or extracted synthesis did not explicitly display the sequencing region/platform. However, these were retained because they were among the strongest directly relevant local-corpus records and were repeatedly supported by the deeper synthesized evidence provided.

No randomized clinical trial directly testing microbiome modification for stunting outcomes was retrieved. The evidence base is therefore **entirely observational for the present question** ([MetaSyn corpus summary, 16215](metasyn://corpus/16215)).

---

## Characteristics of Included Studies

The final included evidence comprised **five observational studies** from **Indonesia, India, and Peru**: two case-control studies, two longitudinal cohorts, and one observational study with functional pathway analysis. All were conducted in LMIC contexts and enrolled children under 5 years. One of the strongest and most methodologically explicit studies was the Indonesian 3–5 year case-control study (Corpus ID **16215**), which explicitly used **16S rRNA V3–V4 sequencing** and linked lower *Prevotella 9* to stunting and lower fiber intake ([Melse-Boonstra et al., 2021](metasyn://corpus/16215)). The Indonesian Aceh study (Corpus ID **16214**) added host biomarker and pathogen virulence data, especially IGF-1 and enteropathogen signals ([Safitri et al., 2023](metasyn://corpus/16214)).

The South Indian longitudinal cohort (Corpus ID **6847**) is especially important because it shows that microbiome differences were detectable over time in children who remained persistently stunted, strengthening temporal plausibility ([Subramanian et al., 2016](metasyn://corpus/6847)). The Peruvian cohort (Corpus ID **6852**) is also notable because microbiome changes and inflammatory markers appeared **before or during progression to stunting**, not merely after growth faltering was established ([Ordiz et al., 2019](metasyn://corpus/6852)).

---

## Results

## 1. Diversity: Stunting Is Not Best Explained by a Simple Loss of Alpha Diversity

Across the LMIC child cohorts summarized in the local corpus, the most consistent pattern was **compositional dysbiosis rather than uniform diversity loss**. In South India, alpha diversity increased with age in all children, and there were **no significant differences in diversity trajectories** between persistently stunted and non-stunted controls, emphasizing age as a dominant driver of microbiome maturation ([Subramanian et al., 2016](metasyn://corpus/6847)). This is an important negative finding: it argues against a simplistic “stunted = less diverse” model.

Similarly, the broader synthesis over multiple LMIC cohorts explicitly states that stunting is associated with a **distinct gut microbiota profile rather than a simple loss of overall diversity** ([Indonesian profile synthesis, 16215](metasyn://corpus/16215)). My view is that this is one of the most robust conclusions in the current local corpus.

## 2. Recurrent Taxonomic Signature: Lower *Prevotella* and Higher Inflammatory/Metabolically Unfavorable Taxa

### Prevotella depletion
A striking repeated signal was **lower *Prevotella*** in stunted children. In Indonesian children aged 3–5 years, *Prevotella 9* was the dominant genus overall but was significantly lower in stunted children and positively correlated with both height and weight ([Melse-Boonstra et al., 2021](metasyn://corpus/16215)). The same study also found lower Bacteroidetes and higher Firmicutes in stunted children, with lower dietary macronutrient intake and greater fecal SCFA/BCFA losses, suggesting a disrupted diet–microbiome–energy axis ([Melse-Boonstra et al., 2021](metasyn://corpus/16215)).

The separate Indonesian Aceh case-control study replicated depletion of *Prevotella* and additionally reported lower *Akkermansia*, *Alloprevotella*, *Butyrivibrio*, and *Lactococcus* in stunted children ([Safitri et al., 2023](metasyn://corpus/16214)). Across Indonesian case-control work, the recurring pattern was a higher Firmicutes-to-Bacteroidetes ratio and lower *Prevotella* abundance in stunted children ([Indonesian profile synthesis, 16215](metasyn://corpus/16215)).

### Loss of potentially beneficial taxa
In South India, non-stunted controls were enriched in **probiotic-associated species** such as *Bifidobacterium longum* and *Lactobacillus mucosae*, whereas persistently stunted children were enriched in inflammogenic taxa ([Subramanian et al., 2016](metasyn://corpus/6847)). In the related South Indian growth study, *Bifidobacterium longum* subsp. *longum* was positively associated with WAZ, especially in boys ([George et al., 2021](metasyn://corpus/6848)).

### Enrichment of inflammatory taxa
Persistently stunted South Indian children showed enrichment of **Desulfovibrio** and **Campylobacterales**, both interpreted as inflammogenic or potentially pathogenic signals ([Subramanian et al., 2016](metasyn://corpus/6847)). In Peru, children who became stunted showed increased *Ruminococcus 1*, *Ruminococcus 2*, *Clostridium sensu stricto*, and *Collinsella* with decreased *Providencia* ([Ordiz et al., 2019](metasyn://corpus/6852)).

My interpretation is that these are not interchangeable findings, but together they converge on the same ecological pattern: **stunting tracks with a microbiome shifted away from fiber-associated and probiotic taxa, and toward taxa compatible with mucosal inflammation, altered fermentation, or pathogen-rich environments**.

## 3. Functional and Inflammatory Signals

Functional inference in South Indian children found that the **lipopolysaccharide biosynthesis pathway was upregulated in stunted and wasted children** ([George et al., 2021](metasyn://corpus/6848)). This matters because it provides a mechanistic bridge between compositional dysbiosis and systemic inflammation.

In Peru, progression to stunting was associated with biomarkers of mucosal injury and systemic immune activation. Children who became stunted had higher baseline **I-FABP**, and increasing **sCD14** over time strongly tracked with becoming stunted; LBP and TNF-α also trended upward ([Ordiz et al., 2019](metasyn://corpus/6852)). These data support an **EED/inflammation pathway** rather than a purely nutritional explanation.

## 4. Enteric Pathogens, IGF-1, and Growth

The Indonesian Aceh study is especially persuasive because it links microbiome dysbiosis to both **enteric infection burden** and **host growth biology**. Stunted children had lower serum **IGF-1** and higher virulence gene expression for EAEC, ETEC, EPEC, *Shigella/EIEC*, and *Salmonella*; these pathogen signals were negatively correlated with both height and IGF-1 ([Safitri et al., 2023](metasyn://corpus/16214)).

The Peruvian birth cohort extended this theme prospectively: each 10% increase in asymptomatic **Campylobacter**-positive stools predicted an average **0.02 reduction in LAZ** at 3, 6, and 9 months later ([Lee et al., 2020](metasyn://corpus/6851)). Although Corpus ID 6851 was excluded from the main included set because it was not a direct stunted-versus-control comparison, it materially strengthens causal interpretation by showing that pathogen burden forecasts later growth impairment.

### Table 2. Most Reproducible Signals Across Included/Contextual LMIC Studies

| Domain | Recurrent finding | Key supporting corpus IDs |
|---|---|---|
| Alpha diversity | Often not clearly reduced in stunting; age is a dominant confounder | 6847, 16215 |
| Beta/compositional differences | Distinct microbiome structure in stunted children | 6847, 6852, 16215 |
| Fiber-associated taxa | Lower *Prevotella*/*Prevotella 9* in stunting | 16215, 16214 |
| Beneficial taxa | Lower *B. longum*, *L. mucosae*, *Akkermansia*, *Lactococcus* | 6847, 16214, 6848 |
| Inflammatory taxa | Higher *Desulfovibrio*, Campylobacterales, *Collinsella*, *Clostridium sensu stricto* | 6847, 6852, 16214 |
| Functional pathways | Higher predicted LPS biosynthesis in stunted/wasted children | 6848 |
| Pathogens/host biomarkers | Higher virulence genes, lower IGF-1, worse growth | 16214, 6851, 6852 |

---

## Feasibility of Meta-analysis

A formal quantitative meta-analysis was **not feasible** from the retrieved local-corpus material. Reasons:

1. **Outcome heterogeneity**: some studies compare stunted vs non-stunted; others model LAZ, growth velocity, or incident stunting.
2. **Exposure heterogeneity**: taxa reported at phylum, genus, species, inferred pathways, or pathogen virulence genes.
3. **Statistical heterogeneity**: results reported as relative abundance differences, correlations, regression coefficients, or qualitative enrichments.
4. **Insufficient extractable effect sizes** in the supplied corpus summaries.
5. **Partial methods visibility** for several studies.

Therefore, the correct evidence product is a **structured qualitative synthesis**, not a pooled effect estimate.

---

## Limitations

1. **Local-corpus constrained retrieval**: only studies surfaced in the provided MetaSyn outputs could be considered.
2. **Abstract-only evidence** for some studies: notably Corpus ID **6852** had no full-text sections available in the provided corpus output, so its evidence is partly abstract-based.
3. **Eligibility uncertainty**: for several studies, the supplied excerpts did not explicitly display the Illumina platform and exact V4/V3–V4 region, although they were clearly 16S-based and highly relevant.
4. **No intervention trials**: no retrieved RCT directly tested whether microbiome modification improves linear growth, IGF-1, EED, or inflammation biomarkers in stunted children ([Indonesian profile synthesis, 16215](metasyn://corpus/16215)).
5. **Residual confounding**: diet, sanitation, pathogen exposure, breastfeeding, sex, and age all influence the microbiome.

---

## Conclusion

The local MetaSyn corpus supports a clear, evidence-based conclusion: **childhood stunting in LMICs is associated more consistently with specific microbiome dysbiosis than with generalized diversity loss**. The most reproducible signature is **lower *Prevotella* and other potentially beneficial taxa, alongside enrichment of inflammatory or pathogen-linked organisms**. The evidence also shows meaningful integration across research branches: dietary insufficiency and lower fiber intake align with lower *Prevotella*; dysbiosis aligns with predicted inflammatory pathways; and pathogen burden aligns with lower IGF-1 and worse subsequent linear growth.

My considered opinion is that the literature retrieved here is already strong enough to reject the narrow hypothesis that stunting is simply a nutritional condition reflected passively in the microbiome. Instead, the evidence better fits a **microbiome–pathogen–EED–growth axis**, in which low-fiber diets, enteropathogen exposure, mucosal dysfunction, and inflammatory microbiota reinforce one another. For future trials, the most rational targets are **combined interventions**: pathogen reduction/WASH-EED strategies plus nutrition designed to support **fiber-responsive taxa such as *Prevotella*** and beneficial commensals, rather than probiotics or food supplementation alone.

---

## Included-Study List

1. **Corpus ID 16215** — *Gut microbiota profile of Indonesian stunted children and children with normal nutritional status.*
2. **Corpus ID 16214** — *Correlation between gut microbiota composition, enteric infections and linear growth impairment: a case-control study in childhood stunting in Pidie, Aceh, Indonesia.*
3. **Corpus ID 6848** — *Gut microbiota profiles of young South Indian children: Child sex-specific relations with growth.*
4. **Corpus ID 6847** — *Longitudinal Analysis of the Intestinal Microbiota in Persistently Stunted Young Children in South India.*
5. **Corpus ID 6852** — *Stunting Is Preceded by Intestinal Mucosal Damage and Microbiome Changes and Is Associated with Systemic Inflammation in a Cohort of Peruvian Infants.*

---

## References

Melse-Boonstra, A., et al. (2021). *Gut microbiota profile of Indonesian stunted children and children with normal nutritional status*. PloS One. [metasyn://corpus/16215](metasyn://corpus/16215)

Safitri, I., et al. (2023). *Correlation between gut microbiota composition, enteric infections and linear growth impairment: a case-control study in childhood stunting in Pidie, Aceh, Indonesia*. Gut Pathogens. [metasyn://corpus/16214](metasyn://corpus/16214)

George, S., et al. (2021). *Gut microbiota profiles of young South Indian children: Child sex-specific relations with growth*. PloS One. [metasyn://corpus/6848](metasyn://corpus/6848)

Subramanian, S., et al. (2016). *Longitudinal Analysis of the Intestinal Microbiota in Persistently Stunted Young Children in South India*. PloS One. [metasyn://corpus/6847](metasyn://corpus/6847)

Ordiz, M. I., et al. (2019). *Stunting Is Preceded by Intestinal Mucosal Damage and Microbiome Changes and Is Associated with Systemic Inflammation in a Cohort of Peruvian Infants*. The American Journal of Tropical Medicine and Hygiene. [metasyn://corpus/6852](metasyn://corpus/6852)

Lee, G., et al. (2020). *Gut Microbiota Features Associated With Campylobacter Burden and Postnatal Linear Growth Deficits in a Peruvian Birth Cohort*. Clinical Infectious Diseases. [metasyn://corpus/6851](metasyn://corpus/6851)

Kosek, M., et al. (2019). *The association of gut microbiota characteristics in Malawian infants with growth and inflammation*. Scientific Reports. [metasyn://corpus/6850](metasyn://corpus/6850)

D’Souza, A., et al. (2020). *Growth velocity in children with Environmental Enteric Dysfunction is associated with specific bacterial and viral taxa of the gastrointestinal tract in Malawian children*. PLoS Neglected Tropical Diseases. [metasyn://corpus/6849](metasyn://corpus/6849)