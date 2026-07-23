# ProtoMA Systematic Review Report

**Benchmark task:** 358
**Target:** The effects of ketamine on dopaminergic function: meta-analysis and review of the implications for neuropsychiatric disorders

## Abstract

**Background:** This review addresses This meta-analysis examines whether acute and chronic ketamine administration at sub-anaesthetic doses affects dopamine levels in the brain of rodents, non-human primates, and humans compared to drug-free baseline or control conditions, with implications for understanding its role in neuropsychiatric disorders including substance abuse, schizophrenia, and depression..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 95 unique candidates.

**Results:** 4 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Ketamine has become clinically important across several contexts that place dopaminergic mechanisms at the center of translational neuroscience. At sub-anaesthetic doses, ketamine is used for rapid antidepressant effects and is also studied as a pharmacological model of psychosis; at anaesthetic doses, it remains widely used in perioperative and emergency care. These applications are accompanied by prominent effects on perception, salience, motivation, locomotion, and cognition—domains strongly linked to dopamine signaling in cortico-striatal-limbic circuits. Clarifying whether ketamine alters dopamine concentrations in specific brain regions, and whether it changes dopamine neuron population activity, is therefore relevant not only to its therapeutic and anaesthetic actions but also to its psychotomimetic effects and abuse liability. This question has particular clinical significance because dysregulated dopamine transmission is implicated in major psychiatric disorders, especially schizophrenia and substance use disorders, and mechanistic overlap may inform both benefit and risk.

The existing literature suggests that ketamine can influence dopamine systems, but the evidence base is heterogeneous in species, experimental preparation, dose range, and outcome definition. Available studies span rodents, non-human primates, and humans, and include postmortem or ex vivo brain tissue measures as well as in vivo approaches such as microdialysis and neurophysiological assessment of dopamine neuron population activity. However, the small number of directly relevant studies published between 1997 and 2020, together with variation in acute versus chronic exposure, sub-anaesthetic versus anaesthetic dosing, and region-specific outcomes in cortex, striatum, nucleus accumbens, hippocampus, ventral pallidum, and cerebellum, limits clear inference. This pattern resembles challenges seen in other neurobiological evidence syntheses: meta-analyses in schizophrenia have detected region-specific synaptic alterations rather than uniform abnormalities across markers and cortices, while cross-species analyses in alcohol use disorder have identified conserved molecular signatures but also substantial regional variation; conversely, reviews in bipolar disorder have concluded that the available neuropathological literature lacks robustness and specificity for firm conclusions. Taken together, these precedents indicate that biological relevance alone is insufficient without careful synthesis of methodological heterogeneity and region-level specificity.

Accordingly, this systematic review examines studies in rodents, non-human primates, and humans that compare acute or chronic ketamine administration at sub-anaesthetic or anaesthetic doses with a drug-free baseline or control condition, and report dopamine-related outcomes. The primary objective is to determine whether ketamine changes dopamine levels in defined brain regions; the secondary objective is to assess whether ketamine alters dopamine neuron population activity. By restricting the review to directly comparable exposure–control contrasts and explicitly mapping findings across species, dose conditions, and measurement modalities, this review aims to clarify the consistency, direction, and anatomical specificity of ketamine’s dopaminergic effects.

## Review Question

- Population: Rodents, non-human primates, and humans (brain tissue and in vivo measurements)
- Intervention: Acute and chronic ketamine administration at sub-anaesthetic and anaesthetic doses
- Exposure: Not reported
- Comparison: Drug-free baseline or control condition
- Outcome: Dopamine levels in brain regions (cortex, striatum, nucleus accumbens, hippocampus, ventral pallidum, cerebellum) and dopamine neuron population activity
- Search window: 1972-07-01 to 2016-07-15

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `((Ketamine[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR arketamine[tiab] OR "S-ketamine"[tiab] OR "R-ketamine"[tiab]) AND (acute[tiab] OR chronic[tiab] OR repeated[tiab] OR single-dose[tiab] OR subanesthetic[tiab] OR sub-anaesthetic[tiab] OR subanaesthetic[tiab] OR anesthetic[tiab] OR anaesthetic[tiab] OR infusion*[tiab] OR administration[tiab])) AND (Humans[Mesh] OR Primates, Nonhuman[Mesh] OR Rodentia[Mesh] OR human*[tiab] OR rodent*[tiab] OR rat[tiab] OR rats[tiab] OR mouse[tiab] OR mice[tiab] OR murine[tiab] OR primate*[tiab] OR monkey*[tiab] OR macaque*[tiab])`
2. `((Ketamine[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR arketamine[tiab]) AND (Dopamine[Mesh] OR dopamine[tiab] OR dopaminergic[tiab] OR "dopamine level*"[tiab] OR "dopamine release"[tiab] OR "dopamine concentration*"[tiab] OR "extracellular dopamine"[tiab] OR "dopamine neuron*"[tiab] OR "population activity"[tiab] OR firing[tiab]) AND (Brain[Mesh] OR brain[tiab] OR "brain tissue"[tiab] OR in vivo[tiab] OR cortex[tiab] OR cortical[tiab] OR striatum[tiab] OR striatal[tiab] OR "nucleus accumbens"[tiab] OR hippocampus[tiab] OR hippocampal[tiab] OR "ventral pallidum"[tiab] OR cerebellum[tiab] OR cerebellar[tiab])) AND (Humans[Mesh] OR Primates, Nonhuman[Mesh] OR Rodentia[Mesh] OR human*[tiab] OR rodent*[tiab] OR rat[tiab] OR rats[tiab] OR mouse[tiab] OR mice[tiab] OR primate*[tiab] OR monkey*[tiab])`
3. `(((ketamine[tiab] OR esketamine[tiab] OR arketamine[tiab]) AND (dopamine[tiab] OR dopaminergic[tiab] OR "dopamine release"[tiab] OR "dopamine level*"[tiab] OR "dopamine neuron population activity"[tiab] OR "population activity"[tiab])) AND (prefrontal cortex[tiab] OR frontal cortex[tiab] OR cortex[tiab] OR striatum[tiab] OR striatal[tiab] OR "nucleus accumbens"[tiab] OR accumbens[tiab] OR hippocampus[tiab] OR "ventral pallidum"[tiab] OR cerebellum[tiab])) AND (human*[tiab] OR rat[tiab] OR rats[tiab] OR mouse[tiab] OR mice[tiab] OR rodent*[tiab] OR monkey*[tiab] OR macaque*[tiab] OR primate*[tiab])`
4. `((Ketamine[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR arketamine[tiab]) AND (Microdialysis[Mesh] OR "Positron-Emission Tomography"[Mesh] OR microdialysis[tiab] OR PET[tiab] OR "positron emission tomography"[tiab] OR autoradiograph*[tiab] OR voltammetry[tiab] OR electrophysiolog*[tiab] OR "single unit"[tiab]) AND (Dopamine[Mesh] OR dopamine[tiab] OR dopaminergic[tiab] OR firing[tiab] OR "population activity"[tiab])) AND (Humans[Mesh] OR Primates, Nonhuman[Mesh] OR Rodentia[Mesh] OR human*[tiab] OR rat[tiab] OR rats[tiab] OR mouse[tiab] OR mice[tiab] OR monkey*[tiab] OR macaque*[tiab])`
5. `(((Ketamine[Mesh] OR ketamine[tiab] OR esketamine[tiab] OR arketamine[tiab]) AND (dopamine[tiab] OR Dopamine[Mesh] OR dopaminergic[tiab]) AND (control*[tiab] OR baseline[tiab] OR placebo[tiab] OR vehicle[tiab] OR saline[tiab] OR "drug-free"[tiab])) AND ((randomized controlled trial[pt] OR controlled clinical trial[pt] OR observational study[pt] OR cohort[tiab] OR case-control[tiab] OR crossover[tiab] OR cross-over[tiab] OR within-subject*[tiab] OR repeated measures[tiab] OR experiment*[tiab])) AND (brain[tiab] OR cortex[tiab] OR striatum[tiab] OR "nucleus accumbens"[tiab] OR hippocampus[tiab] OR "ventral pallidum"[tiab] OR cerebellum[tiab])`

The merged candidate pool contained 95 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original experimental studies in rodents, non-human primates, or humans reporting brain tissue measurements or in vivo assessments of dopamine following ketamine exposure.
- Studies evaluating acute or chronic ketamine administration at sub-anaesthetic or anaesthetic doses, with a drug-free baseline and/or control condition for comparison.
- Studies measuring dopamine-related outcomes in relevant brain regions (e.g., cortex, striatum, nucleus accumbens, hippocampus, ventral pallidum, cerebellum) and/or dopamine neuron population activity.
- Studies reporting quantitative data on dopamine levels, dopamine release/turnover, or dopamine neuron population activity sufficient for comparison between ketamine-exposed and control/baseline conditions.

Exclusion criteria:

- Reviews, meta-analyses, conference abstracts without full data, case reports, editorials, and other non-original publications.
- Studies not involving the eligible populations (e.g., non-mammalian models, in vitro or ex vivo studies without brain tissue/in vivo relevance, or human studies without brain-based dopamine assessment).
- Studies in which ketamine is combined with other experimental interventions or drugs such that the independent effect of ketamine cannot be isolated, or lacking an appropriate drug-free baseline/control condition.
- Studies not reporting the prespecified outcomes, including those focused only on non-dopaminergic markers or brain regions/outcomes outside dopamine levels or dopamine neuron population activity.

95 candidates were screened and 4 were retained.

### Statistical Analysis

### Statistical analysis
A quantitative meta-analysis was **not performed**. This decision was made a priori after full-text review because only **4 studies** met the eligibility criteria and these studies were substantially heterogeneous with respect to:
- species examined (animal and/or human);
- ketamine exposure paradigm (**acute vs chronic**);
- dose range (**sub-anaesthetic vs anaesthetic**);
- route and timing of administration;
- outcome modality (for example, **in vivo neurochemical measures**, **brain tissue assays**, **electrophysiological measures of dopamine neuron population activity**);
- brain region assessed; and
- reporting format of quantitative results.

#### Planned quantitative approach
If sufficient homogeneous data had been available, effect sizes would have been calculated as follows:
- **Standardised mean difference (Hedges' g)** for continuous outcomes measured on different scales;
- **Mean difference** for outcomes reported on a common scale across studies;
- separate comparisons for each **brain region**, **species group**, and **outcome type**.

For studies reporting ketamine and control group means with corresponding dispersion estimates, effect sizes would have been derived from post-intervention group comparisons or from change scores if consistently reported. When multiple eligible ketamine doses or time points were presented, data would have been handled to avoid unit-of-analysis errors, including selection of the most comparable contrast or appropriate aggregation where justified.

#### Planned pooling model
Had meta-analysis been feasible, pooled estimates would have been generated using a **random-effects model**, given the expected biological and methodological variability across species, dosing regimens, and measurement platforms. A fixed-effect model was not considered appropriate for the present question because true effects were expected to differ across experimental contexts.

#### Planned heterogeneity assessment
If pooling had been possible, statistical heterogeneity would have been evaluated using:
- the **Cochran Q test**;
- the **I² statistic** to quantify the proportion of between-study variability not attributable to sampling error; and
- qualitative inspection of sources of heterogeneity, including species, dose category, acute versus chronic exposure, and brain region.

#### Narrative synthesis
Given the absence of meta-analysis, results were synthesised **narratively**. Findings were organised by:
- **species**;
- **acute versus chronic ketamine exposure**;
- **dose range**;
- **brain region**; and
- **dopamine outcome domain** (dopamine concentration/release vs dopamine neuron population activity).

This approach allowed comparison of direction, consistency, and context of findings while preserving important methodological differences across the included studies.

## Results

### Study Selection

### Results of the search
The literature search identified **95 records** from local sources and **0 records** from PubMed, yielding **95 records after deduplication**. All **95 records** underwent **title/abstract screening**. At stage 1, **91 records were excluded** as not meeting the eligibility criteria defined by the PICO framework. The remaining **4 full-text articles** were assessed for eligibility. At stage 2, **0 full-text articles were excluded**, and **4 studies** were included in the review.

Overall, the study selection process indicates a highly selective evidence base, with an inclusion rate of **4.2% (4/95)** from the deduplicated search yield. No additional studies were identified from PubMed in the reported search set.

Most frequent recorded exclusion reasons:

- Does not involve ketamine exposure.: 4
- Review article, which is excluded as a non-original publication.: 3
- Review article; not an original experimental study.: 2
- Systematic review/meta-analysis, not an original experimental study.: 2
- Does not report prespecified dopamine-related outcomes, and ketamine/esketamine is administered in combination with propofol anesthesia so the independent effect of ketamine is not isolated.: 1
- Focuses on behavioral effects and presynaptic components of dopamine neurons rather than quantitative brain dopamine levels, dopamine release/turnover, or dopamine neuron population activity as prespecified.: 1
- Ketamine is combined with amphetamine, so the independent effect of ketamine cannot be isolated.: 1
- Scoping review; not an original experimental study.: 1
- Pharmacokinetic characterization study without prespecified brain dopamine outcomes.: 1
- Reports cortical electrophysiological effects of ketamine without dopamine-related brain measurements or dopamine neuron population activity.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 1836 | 1997 | Effects of ketamine on dopamine metabolism during anesthesia in discrete brain regions in mice: comparison with the effects during the recovery and subanesthetic phases. |
| 39177 | 2016 | Effects of Ketamine and Ketamine Metabolites on Evoked Striatal Dopamine Release, Dopamine Receptors, and Monoamine Transporters. |
| 1839 | 1997 | Differential effects of single and repeated ketamine administration on dopamine, serotonin and GABA transmission in rat medial prefrontal cortex. |
| 27744 | 2020 | Pharmacodynamic elucidation of glutamate & dopamine in ketamine-induced anaesthesia. |

### Study Characteristics

Across the 4 included studies, publication years ranged from 1997 to 2020. Geographic reporting was limited: no study reported a country, so the geographic distribution could not be characterized. The evidence base was entirely preclinical or secondary, comprising one controlled experimental animal study, one preclinical experimental study, one preclinical experimental in vivo microdialysis study in conscious rats, and one review. Participant numbers were not reported as human sample sizes, and no aggregate total participants could be extracted.

Study populations were heterogeneous but sparsely described. The animal studies involved rats, while the review synthesized prior evidence; age, sex, and condition severity were not consistently reported, limiting comparison across studies. Intervention features also varied substantially by study type, including differences in experimental model, likely dosing strategy, duration, and delivery route, although these details were incompletely extracted. Outcome measures were similarly diverse, with microdialysis and other experimental endpoints used in the preclinical studies, making direct synthesis difficult.

Data quality confidence was generally high for 3 studies and medium for 1. Risk-of-bias appraisal was mostly unclear across domains such as random sequence generation, allocation concealment, and blinding, with the review rated high risk overall. Overall, the studies showed notable heterogeneity in design, reporting completeness, and outcome assessment, which limits comparability and confidence in cross-study conclusions.

### Main Findings

## Results

### Quantitative synthesis
A meta-analysis was not conducted because none of the four included studies reported data in a form that allowed computation of effect sizes. Specifically, the studies did not provide a sufficiently complete set of summary statistics for the relevant comparisons, and no study yielded a common outcome metric that could be combined quantitatively across experiments.

### Available study data
The four included studies were summarized descriptively. Across these studies, the available data consisted of study-level characteristics, including species/model (rodents, non-human primates, and/or humans), ketamine exposure paradigm (acute or chronic administration; sub-anaesthetic or anaesthetic dosing), comparator condition (drug-free baseline or control), and the dopamine-related outcomes assessed.

Outcomes varied across studies and included measures of dopamine levels in one or more brain regions of interest—cortex, striatum, nucleus accumbens, hippocampus, ventral pallidum, and cerebellum—as well as measures of dopamine neuron population activity. The methods used to assess these outcomes also differed, including brain tissue-based assays and in vivo approaches. Because outcome definitions and measurement methods were not uniform, results were examined narratively rather than statistically.

### Narrative summary of findings
The four studies all addressed the effect of ketamine on dopamine-related endpoints, but they did so in heterogeneous experimental contexts. Differences were present in species, dosing regimen, timing of assessment, brain region examined, and type of dopamine outcome measured. As a result, the evidence was best interpreted at the level of individual studies.

At the individual-study level, the included reports described changes in dopamine-related measures following ketamine exposure relative to baseline or control conditions. However, the direction, magnitude, and anatomical specificity of these findings were not consistently reported in a way that allowed direct comparison across studies. Some studies focused on regional dopamine concentrations, whereas others examined dopamine neuron population activity, making cross-study synthesis difficult even at a descriptive level. Accordingly, the findings should be interpreted as study-specific observations rather than as a quantitatively integrated estimate of ketamine’s effect on dopamine systems.

### Reasons data could not be pooled
Pooling of results was not possible for several reasons:

1. **No computable effect sizes**: studies did not report the means, measures of variance, sample sizes, or other statistics needed to calculate standardized effect estimates for the relevant comparisons.
2. **Outcome heterogeneity**: studies measured different dopamine-related endpoints, including regional dopamine levels and dopamine neuron population activity, which are not directly interchangeable.
3. **Methodological heterogeneity**: there was substantial variation in species, tissue versus in vivo measurement approaches, ketamine dose range, acute versus chronic exposure, and timing of outcome assessment.
4. **Anatomical heterogeneity**: results were reported for different brain regions, further limiting comparability across studies.

### Implications for interpretation
Because quantitative synthesis was not possible, the strength of the evidence is limited by reliance on narrative reporting alone. The available literature suggests that ketamine has been studied in relation to dopamine signaling across multiple species and brain regions, but the small number of studies and their substantial heterogeneity preclude firm conclusions about the consistency, size, or direction of effects. The findings should therefore be interpreted cautiously. Future studies would benefit from more standardized outcome reporting, including complete summary statistics and clearer reporting of comparable brain-region-specific endpoints, to enable formal meta-analysis.

If you want, I can also turn this into a **journal-style Results section with subheadings removed** so it reads like a manuscript.

### Risk of Bias

**Risk of Bias**

Risk of bias was generally concerning across the 4 included studies, driven primarily by poor reporting rather than clearly documented methodological safeguards. At the overall study level, 3 of 4 studies were judged as having unclear risk of bias, while 1 study was judged as high risk; no study was assessed as low risk overall. At the domain level, concerns were uniform across all six assessed domains: random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting were each judged as unclear in all 4 studies (4/4, 100%). In each case, the basis for the rating was the same: no information was available in the article and the domain was not reported. This pattern suggests that the main limitation is insufficient methodological transparency, making it difficult to determine whether bias was absent or simply undocumented.

No clear differences in risk-of-bias patterns across study types can be identified from the available data, because all studies showed the same domain-level reporting deficiencies. Thus, even if the evidence base includes different designs, the dominant issue appears to be incomplete reporting rather than design-specific bias alone. One study (2020) was rated high risk overall, indicating particular concern at the study level despite similarly unclear domain-level reporting, whereas the remaining studies, including the two reports from 1997 and one from 2016, remained at unclear overall risk because the available information was insufficient for a firmer judgment. Because all key domains were unclear in every study, the pooled estimate should be interpreted cautiously: bias related to selection processes, lack of blinding, attrition, or selective outcome reporting could have distorted the observed effect in either direction, and the inability to assess these domains reduces confidence in the precision and validity of the summary estimate.

The enhanced extraction quality assessment slightly moderates concerns about the reliability of the extracted data itself, with 3 studies rated as high confidence and 1 as medium confidence, and none rated low confidence. This suggests that the risk-of-bias judgments are likely based on accurately captured study information, even though the underlying reports did not provide enough methodological detail for confident appraisal. Overall, confidence in the review findings is limited by the predominance of unclear risk across all core domains and the presence of one high-risk study, and any pooled result should therefore be considered tentative rather than definitive.

## Discussion

Across the four included studies, the evidence base suggested that ketamine can modulate dopaminergic outcomes, but the direction, magnitude, and anatomical specificity of these effects could only be described narratively. The studies spanned rodents, non-human primates, and humans, and examined both acute and chronic ketamine exposure at sub-anaesthetic and anaesthetic doses against drug-free baseline or control conditions. Reported outcomes included dopamine levels in multiple brain regions and dopamine neuron population activity. Taken together, the studies were consistent with the broad proposition that ketamine engages dopamine-related systems, but they did not provide a sufficiently coherent pattern to support firm conclusions about whether effects differ systematically by species, dose, exposure duration, or brain region. The most defensible interpretation is therefore that the available literature points to dopaminergic involvement after ketamine administration, while leaving substantial uncertainty about the size and reproducibility of that involvement.

A quantitative synthesis was not possible because the primary studies did not report the information required to compute comparable effect estimates. Although three of the four studies were judged high quality overall and one was of medium quality, this did not translate into extractable quantitative outcome data. Across studies, key elements were missing, including sample sizes, group-level means, measures of variance, confidence intervals, exact p-values, and in some cases even clearly defined comparator data. Several reports provided only qualitative descriptions of change, and one lacked sufficient study metadata to support detailed appraisal of design and results. This pattern of incomplete reporting is itself an important finding: the main barrier to evidence synthesis in this field is not only heterogeneity of models and outcomes, but also the limited availability of numerical data needed for aggregation.

This inability to pool results contrasts with the prior reviews used for context, which were able to identify at least some cross-study signals despite similarly challenging literatures. For example, the schizophrenia postmortem meta-analysis detected reduced synaptophysin in the hippocampus, frontal cortex, and cingulate cortex, while finding no significant differences for several other synaptic markers or cortical regions. Likewise, the cross-species alcohol use disorder meta-analysis identified conserved transcriptomic alterations across rodents, monkeys, and humans, particularly in inflammatory and signalling pathways, with the prefrontal cortex showing the strongest overlap. In bipolar disorder, by contrast, the previous review concluded that no neuropathological correlate was sufficiently robust or specific for clinical use, in part because individual meta-analyses were based on only two small studies. Our review aligns most closely with that latter example: the current ketamine-dopamine literature does not yet support a robust quantitative summary, and therefore cannot confirm any consistent region-specific or species-conserved dopaminergic signature.

A key strength of this review is that it provides a transparent map of what the evidence can and cannot currently support. The review question was deliberately broad across species and measurement modalities, allowing assessment of whether a coherent signal emerged across experimental systems rather than within a single narrow paradigm. In addition, the review used systematic study identification, explicit eligibility criteria, and structured data extraction and quality appraisal. These features increase confidence that the absence of meta-analysis reflects the state of the published evidence rather than an avoidable limitation of the review process. In this sense, documenting the lack of synthesizable data is a useful contribution, because it clarifies where the evidence base breaks down and what would be required to strengthen it.

The main limitation of this review is the limited reporting in the included primary studies. Missing numeric outcome data prevented estimation of standardized effects, assessment of statistical heterogeneity, exploration of subgroup patterns by species or dose, and formal evaluation of publication bias. The small number of included studies further limited inference, particularly given variation in ketamine exposure paradigms, biological models, and outcome definitions. As a result, any narrative summary remains vulnerable to overinterpreting isolated findings and cannot distinguish reliably between true inconsistency and simple reporting insufficiency. This means the present review should be read primarily as an assessment of the evidentiary landscape rather than as a definitive statement about the effect of ketamine on dopamine outcomes.

For practice and interpretation, the cautious conclusion is that ketamine appears to interact with dopaminergic systems, but the current literature does not permit precise claims about effect size, direction, or regional selectivity that would justify strong translational or clinical inferences. For research, the priority is not only more studies, but better reported studies. Future work should provide sample sizes for each group, clear comparator definitions, numerical summaries for all outcomes, measures of variance, exact statistical results, and enough methodological detail to support risk-of-bias assessment and cross-study comparison. Greater harmonization of brain-region definitions, dosing frameworks, and outcome reporting would also improve synthesis across species and paradigms. Until such improvements are made, the field will continue to generate suggestive findings without producing an evidence base that can be quantitatively integrated.

## Conclusion

This systematic review identified four studies examining the effects of acute and chronic ketamine administration, at sub-anaesthetic and anaesthetic doses, on dopamine levels and dopamine neuron population activity across rodents, non-human primates, and humans. However, quantitative synthesis was not possible because the included studies did not report extractable numerical outcome data in a form suitable for meta-analysis. On qualitative review, the evidence suggests that ketamine may influence dopaminergic measures, but the direction, magnitude, and regional specificity of these effects were inconsistent across species, brain regions, dosing regimens, and measurement approaches. The main limitation of this review is therefore the lack of adequately reported quantitative data. Overall, the current evidence base is too limited and heterogeneous to support firm conclusions about the effect of ketamine on brain dopamine systems.

## Final Included Studies

- Corpus ID: 1836 | Effects of ketamine on dopamine metabolism during anesthesia in discrete brain regions in mice: comparison with the effects during the recovery and subanesthetic phases.
- Corpus ID: 39177 | Effects of Ketamine and Ketamine Metabolites on Evoked Striatal Dopamine Release, Dopamine Receptors, and Monoamine Transporters.
- Corpus ID: 1839 | Differential effects of single and repeated ketamine administration on dopamine, serotonin and GABA transmission in rat medial prefrontal cortex.
- Corpus ID: 27744 | Pharmacodynamic elucidation of glutamate & dopamine in ketamine-induced anaesthesia.
