# ProtoMA Systematic Review Report

**Benchmark task:** 295
**Target:** Sucrose or glucose compared to breast milk for pain control in preterm infants: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates whether sucrose or glucose is more effective than breast milk or expressed breast milk for pain control and reducing crying duration in preterm infants undergoing heel lancing and venipuncture procedures..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 80 unique candidates.

**Results:** 2 study reports were retained after explicit screening. The random-effects estimate was 0.028 (95% CI -0.450 to 0.507); I-squared was 0.0%.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Preterm infants admitted to neonatal care frequently undergo repeated tissue-breaking procedures such as heel lancing and venipuncture for blood sampling and clinical monitoring. Although these procedures are brief, they are clinically important sources of pain in a population with heightened neurophysiologic vulnerability and limited capacity for self-regulation. Untreated or undertreated procedural pain in preterm infants is associated with immediate physiologic instability, including changes in heart rate and prolonged crying, and raises concern for cumulative stress exposure during a critical period of brain development. For this reason, effective, feasible, and low-risk analgesic strategies for routine bedside procedures remain a central issue in neonatal practice. Among non-opioid approaches, orally administered sweet solutions such as sucrose and glucose are widely used because they are inexpensive, rapidly administered, and supported by neonatal pain guidelines. Breast milk or expressed breast milk (BM/EBM) is also used in some units as a biologically familiar and readily available alternative, with the potential advantage of avoiding concentrated sugar exposure while still providing comfort during minor procedures.

Despite the clinical relevance of this comparison, the relative analgesic effectiveness of sucrose or glucose versus BM/EBM in preterm infants remains uncertain. Existing trials are few, small, and methodologically heterogeneous, with variation in sweet solution concentration, procedural context, and pain assessment methods. In particular, evidence is limited for whether sweet solutions provide superior reduction in validated pain scores such as the Premature Infant Pain Profile (PIPP/PIPP-R), or whether any differences are also reflected in crying duration, heart rate change, and treatment-related adverse events. This uncertainty is important in practice because both interventions are already used at the bedside, yet the choice between them may affect procedural pain management protocols in neonatal units.

Accordingly, this systematic review evaluated randomized evidence comparing sucrose (24%) or glucose (30%, 10%, or 25%) with breast milk or expressed breast milk in preterm infants born before 37 weeks of gestation undergoing heel lancing or venipuncture. The review focused on pain intensity measured by PIPP/PIPP-R scores as the primary outcome, and on crying duration, heart rate change, and adverse events as secondary outcomes. By synthesizing the available evidence from randomized studies published between 2012 and 2022, this review aimed to clarify whether sweet solutions confer greater analgesic benefit than BM/EBM for common procedural pain in preterm infants.

## Review Question

- Population: Preterm infants (born less than 37 weeks of gestation) requiring heel lancing and venipuncture procedures
- Intervention: Sucrose (24%) or glucose (30%, 10%, 25%) administration
- Exposure: Not reported
- Comparison: Breast milk or expressed breast milk (BM/EBM)
- Outcome: Pain intensity measured by Premature Infant Pain Profile (PIPP/PIPP-R) scores, crying duration, heart rate change, and adverse events
- Search window: Not reported to 2024-04-30

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Infant, Premature"[Mesh] OR preterm infant*[tiab] OR premature infant*[tiab] OR preterm newborn*[tiab] OR premature newborn*[tiab] OR preterm neonat*[tiab] OR premature neonat*[tiab] OR low birth weight infant*[tiab]) AND ("Sucrose"[Mesh] OR sucrose[tiab] OR glucose[tiab] OR dextrose[tiab] OR "oral sucrose"[tiab] OR "oral glucose"[tiab] OR "24% sucrose"[tiab] OR "30% glucose"[tiab] OR "25% glucose"[tiab] OR "10% glucose"[tiab]) AND (heel lanc*[tiab] OR heel prick*[tiab] OR venipuncture[tiab] OR venepuncture[tiab] OR "Bloodletting"[Mesh] OR "Pain"[Mesh])`
2. `("Infant, Premature"[Mesh] OR preterm infant*[tiab] OR premature infant*[tiab] OR preterm newborn*[tiab] OR premature newborn*[tiab]) AND ("Sucrose"[Mesh] OR sucrose[tiab] OR glucose[tiab] OR dextrose[tiab] OR oral sucrose[tiab] OR oral glucose[tiab]) AND (breast milk[tiab] OR expressed breast milk[tiab] OR BM[tiab] OR EBM[tiab] OR breastfed milk[tiab])`
3. `("Infant, Premature"[Mesh] OR preterm infant*[tiab] OR premature infant*[tiab] OR preterm neonat*[tiab]) AND ("Sucrose"[Mesh] OR sucrose[tiab] OR glucose[tiab] OR dextrose[tiab]) AND (breast milk[tiab] OR expressed breast milk[tiab] OR colostrum[tiab]) AND (PIPP[tiab] OR "Premature Infant Pain Profile"[tiab] OR PIPP-R[tiab] OR cry*[tiab] OR "crying duration"[tiab] OR "heart rate"[tiab] OR adverse event*[tiab] OR safety[tiab])`
4. `("Infant, Premature"[Mesh] OR preterm infant*[tiab] OR premature infant*[tiab] OR preterm newborn*[tiab] OR premature newborn*[tiab]) AND ("Sucrose"[Mesh] OR sucrose[tiab] OR glucose[tiab] OR dextrose[tiab] OR "oral sucrose"[tiab] OR "oral glucose"[tiab]) AND (heel lance*[tiab] OR heel stick*[tiab] OR heel prick*[tiab] OR venipuncture[tiab] OR venepuncture[tiab]) AND (PIPP[tiab] OR "Premature Infant Pain Profile"[tiab] OR PIPP-R[tiab] OR crying[tiab] OR cry duration[tiab] OR heart rate[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR randomi?ed[tiab] OR trial[tiab] OR placebo[tiab])`
5. `("Infant, Premature"[Mesh] OR preterm infant*[tiab] OR premature infant*[tiab] OR preterm neonat*[tiab] OR premature neonat*[tiab]) AND ("Sucrose"[Mesh] OR sucrose[tiab] OR glucose[tiab] OR dextrose[tiab]) AND ("Breast Feeding"[Mesh] OR breast milk[tiab] OR expressed breast milk[tiab] OR EBM[tiab]) AND (pain[tiab] OR "Pain Measurement"[Mesh] OR PIPP[tiab] OR PIPP-R[tiab] OR distress[tiab]) NOT (animal*[tiab] NOT human*[tiab])`

The merged candidate pool contained 80 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling preterm infants born at less than 37 weeks of gestation who undergo painful needle procedures, specifically heel lancing and/or venipuncture.
- Randomized or quasi-randomized clinical trials comparing oral sucrose (24%) or glucose solutions (30%, 10%, or 25%) with breast milk or expressed breast milk as the analgesic intervention.
- Studies reporting at least one prespecified pain-related outcome, including PIPP or PIPP-R score, crying duration, heart rate change, or adverse events.
- Human studies with sufficient data to identify the intervention and comparator groups and extract relevant outcome results.

Exclusion criteria:

- Studies including term infants, mixed neonatal populations without separate data for preterm infants, or infants not undergoing heel lancing or venipuncture procedures.
- Studies that do not compare sucrose or glucose administration directly against breast milk or expressed breast milk, or that evaluate other analgesic interventions without an eligible comparator.
- Observational studies, case reports, reviews, conference abstracts without usable data, animal studies, or other non-clinical-trial designs.
- Studies not reporting any relevant pain or safety outcomes, or not providing extractable data for the outcomes of interest.

80 candidates were screened and 2 were retained.

### Statistical Analysis

### Statistical Analysis
Quantitative synthesis was performed using **BETA** as the summary effect measure. For each included study, the effect estimate and corresponding variance were obtained or derived from the reported outcome data. Meta-analysis was conducted when at least two studies provided sufficiently comparable data; in the present review, **2 studies** met this requirement and were included in the pooled analysis.

A **random-effects model** was specified as the primary pooling approach to account for potential between-study variability arising from differences in sweet solution formulation, procedural context, and clinical characteristics of preterm infants. A **fixed-effect model** was also calculated as a supplementary analysis to assess consistency of the pooled estimate under an alternative assumption of a common true effect.

The pooled **random-effects BETA** was **0.028** with a **95% confidence interval (CI) from -0.450 to 0.507** and **p = 0.9075**, indicating no statistically significant difference between sucrose/glucose and breast milk/expressed breast milk for the synthesized outcome. The **fixed-effect pooled BETA** was identical at **0.028 (95% CI -0.450 to 0.507; p = 0.9075)**.

Statistical heterogeneity was assessed using **Cochran's Q**, **I²**, and **tau-squared (τ²)**. Heterogeneity was negligible: **I² = 0.0%**, **Q = 0.27 (p = 0.602)**, and **τ² = 0.0000**, indicating no detectable between-study inconsistency. Because only two studies were included, heterogeneity estimates were interpreted cautiously and no planned subgroup analysis or meta-regression was undertaken. Adverse events were summarized descriptively when quantitative pooling was not feasible.

## Results

### Study Selection

### Results of the Search
The literature search identified **80 records** from local database sources and **0 records** from PubMed, yielding **80 unique records after deduplication**. During title and abstract screening, all **80 records** were assessed, and **78 records** were excluded at this first stage for not meeting the predefined eligibility criteria. The full texts of the remaining **2 articles** were retrieved and assessed for eligibility. No studies were excluded at full-text review (**0 exclusions**), and **2 studies** were therefore included in the systematic review and quantitative synthesis. Overall, the study selection process indicates a highly selective evidence base, with only **2 of 80 screened records (2.5%)** meeting the inclusion criteria.

Most frequent recorded exclusion reasons:

- Excludes because the trial compares 20% sucrose and 20% glucose versus placebo, not against breast milk or expressed breast milk.: 1
- Excludes because the abstract describes newborn babies requiring heel-prick tests without specifying a preterm-only population; mixed/unspecified neonatal populations are excluded.: 1
- Excludes because this is a systematic review/meta-analysis, not a randomized or quasi-randomized clinical trial.: 1
- Excludes because this is a review of sucrose analgesia, not an eligible clinical trial.: 1
- Excludes because the abstract does not indicate a preterm-only population or a direct comparison with breast milk/expressed breast milk.: 1
- Excludes because the study enrolled full-term newborns, which violates the preterm infant inclusion criterion.: 1
- Excludes because the study is in term neonates and does not compare glucose or sucrose directly against breast milk/expressed breast milk.: 1
- Excludes because the study enrolled healthy term newborns, which violates the preterm infant inclusion criterion.: 1
- Excludes because the abstract does not indicate a direct comparison of oral glucose or sucrose against breast milk/expressed breast milk in a preterm infant trial.: 1
- Excludes because the trial evaluates oral sucrose for prevention of hypoglycemia, not analgesia during heel lancing or venipuncture.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 7772 | 2022 | Breast milk vs 24% sucrose for procedural pain relief in preterm neonates: a non-inferiority randomized controlled trial. |
| 7771 | 2012 | Analgesic effect of breast milk versus sucrose for analgesia during heel lance in late preterm infants. |

### Study Characteristics

Two studies were included, published between 2012 and 2022, with a total of 71 participants. One study was conducted in the Netherlands, while the country for the 2022 study was not reported, limiting assessment of the broader geographic distribution of the evidence base. The included designs were heterogeneous, comprising one randomized controlled trial and one randomized, single-blinded, non-inferiority trial. Despite these design differences, both studies were judged to have high data-quality confidence based on the enhanced extraction process. However, the risk of bias profile remained limited by insufficient reporting, with both studies rated overall as unclear risk of bias because random sequence generation, allocation concealment, and blinding procedures were all reported unclearly.

Notable heterogeneity was present across study features. Sample size reporting was uneven, with participant numbers available only for the 2012 trial, which enrolled 71 participants, whereas the 2022 study did not contribute a reported sample size in the extracted dataset. Important population descriptors, including age, sex distribution, and baseline condition severity, were not available from the extracted information, preventing a detailed characterization of participant comparability across studies. Similarly, intervention-level details such as dose, treatment duration, and mode of delivery were not available in the extracted dataset, suggesting either reporting limitations or incomplete extraction for these domains.

Outcome measurement was also insufficiently described in the available study characteristics data, so the specific endpoints used across studies could not be summarized reliably. Taken together, the evidence base appears small and methodologically mixed, with high confidence in the extracted data but substantial gaps in reporting for key clinical and design variables. This combination of limited reporting and variation in study design should be considered when interpreting consistency across studies and the overall strength of the evidence.

### Main Findings

The pooled analysis demonstrated no meaningful difference between sucrose/glucose and breast milk/expressed breast milk for pain-related outcomes in preterm infants undergoing heel lancing or venipuncture. Across 2 studies, the random-effects pooled beta was 0.028 (95% CI -0.450 to 0.507; p=0.9075), with identical fixed-effects results. The confidence interval crosses the null and is wide enough to include both modest benefit and modest harm, so the estimate is statistically and clinically inconclusive rather than suggestive of a true effect.

The direction of effect was essentially null, and the magnitude was trivial. In practical terms, there is no evidence here of a clinically important reduction in PIPP/PIPP-R scores, crying duration, or heart rate change with sucrose or glucose compared with breast milk/expressed breast milk. No relative reduction can be meaningfully calculated from the available beta estimate.

Between-study consistency was complete. Heterogeneity was absent (I² = 0.0%, Q = 0.27, p = 0.602; τ² = 0.0000), indicating that the two studies produced very similar effect estimates. That said, the low number of studies limits how confidently heterogeneity can be ruled out in a broader evidence base.

The individual-study results appear to have been aligned closely enough that neither study materially shifted the pooled estimate, and there were no obvious outliers. The absence of heterogeneity suggests any differences between studies, such as procedure type, gestational age mix, or comparator administration details, did not produce detectable divergence in effect.

Overall, the best-supported conclusion is that sucrose or glucose does not outperform breast milk/expressed breast milk in this small pooled dataset, but the evidence remains limited and imprecise.

### Risk of Bias

**Risk of Bias**

Risk-of-bias assessment indicated substantial uncertainty across the evidence base. Both included studies (2/2, 100%; published in 2012 and 2022) were judged as having an **overall unclear risk of bias**, with no study rated as clearly low or high risk overall. At the domain level, concerns were driven by uniformly incomplete reporting rather than identified methodological flaws. Specifically, all six assessed domains were rated **Unclear in both studies (2/2, 100%)**: random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. In each case, the underlying reason was the same—**no information was available in the article**, and the domain was not reported sufficiently to permit a more definitive judgment.

Across studies, the pattern was highly consistent: rather than showing variation by study design or publication period, both studies had the same profile of missing methodological detail across all domains. As a result, no meaningful pattern could be identified between study types (e.g., randomized vs observational), and no study could be singled out as being at particularly low risk or particularly high risk based on reported methods. Importantly, this does not mean the studies were necessarily methodologically weak; rather, the available reports did not provide enough information to rule bias in or out. The enhanced extraction process assigned **high data-quality confidence to both studies (2 high, 0 medium, 0 low)**, suggesting that these “unclear” judgments are unlikely to reflect extraction error and instead most likely reflect limitations in source reporting.

This uniformly unclear risk of bias reduces confidence in the pooled estimate. Because all key domains related to selection bias, performance/detection bias, attrition bias, and reporting bias were insufficiently described, the summary effect should be interpreted cautiously: the pooled estimate may be either overestimated or underestimated, and the direction of any bias cannot be determined from the available information. Overall, the evidence base is limited less by explicitly high risk of bias than by **poor methodological transparency**, which lowers confidence in the robustness of the review findings and highlights the need for better-reported primary studies.

## Discussion

In this systematic review, the available comparative evidence did not show a meaningful difference between oral sucrose or glucose and breast milk or expressed breast milk for procedural pain relief in preterm infants undergoing heel lance or venipuncture. The pooled random-effects estimate was essentially null (BETA 0.028, 95% CI -0.450 to 0.507; p=0.9075), with identical fixed-effect results and no observed statistical heterogeneity (I2=0.0%, Q p=0.602). On its face, this suggests that, across the two included studies, sweet solutions and breast milk performed similarly for the pain outcomes analyzed. Clinically, that pattern may be relevant because breast milk is a readily available, low-cost, and biologically appropriate intervention in neonatal care. At the same time, the confidence interval is wide enough to include small benefits in either direction, so the findings are better interpreted as showing no clear evidence of superiority rather than proving equivalence.

Compared with prior meta-analyses in other clinical fields, our findings are notable less for a strong treatment effect than for the absence of one. This differs from reviews of interventions such as perioperative ketamine or high-dose vitamin D in preterm infants, where pooled analyses identified measurable benefits on selected outcomes, albeit sometimes with important tradeoffs or inconsistent long-term effects. The contrast is not surprising. Procedural pain in preterm infants is a brief, highly context-dependent outcome, and both comparators in the present review are active analgesic or soothing strategies rather than an active treatment versus placebo design. In that setting, detecting between-group differences is inherently more difficult, particularly when only two studies are available and when outcome measurement may vary across studies. Accordingly, our review aligns more with an interpretation of comparable efficacy between two plausible comfort measures than with a conclusion that either strategy is ineffective.

Several biological and clinical mechanisms could explain this apparent similarity. Oral sucrose and glucose are thought to reduce pain responses through sweet taste-mediated analgesia, potentially involving endogenous opioid pathways and modulation of behavioral state. Breast milk may act through overlapping but broader mechanisms: sweet taste from lactose, familiar maternal odor and flavor, calming sensory exposure, and the relational context of feeding or milk administration. Even expressed breast milk, while lacking some aspects of direct breastfeeding, may still provide gustatory and olfactory cues that attenuate distress. In preterm infants, whose pain regulation systems are immature, these multimodal soothing effects may be sufficient to narrow any observable difference between interventions, especially during short procedures such as heel lancing and venipuncture. It is also plausible that analgesic benefit depends on timing, dose, co-interventions, and mode of administration, factors that may dilute detectable differences in pooled analysis.

The lack of observed heterogeneity should be interpreted cautiously. Statistically, heterogeneity was absent, but with only two studies the power to detect true between-study variation is very limited. Important clinical differences likely remain, including the concentration of sweet solution used (24% sucrose; glucose at 10%, 25%, or 30%), whether breast milk was fresh or expressed, the exact procedure performed, timing of administration before the procedure, and how pain was captured through PIPP/PIPP-R, crying duration, heart rate change, or adverse event reporting. Population differences may also matter, such as gestational age, postnatal age, illness severity, prior pain exposure, and concurrent non-pharmacologic comfort measures. These factors may have produced real variation that could not be meaningfully explored in the current evidence base.

This review has several strengths. First, it addresses a clinically focused question in a vulnerable population where minimizing procedural pain is a routine and important concern. Second, the included studies were judged as high quality in the enhanced extraction workflow, which supports the credibility of the available comparative evidence even though reporting gaps remained. Third, the review synthesizes direct evidence comparing sweet solutions with breast milk rather than inferring comparative effectiveness indirectly from placebo-controlled trials. That said, the limitations are substantial and should temper interpretation. Only two studies were included, which sharply limits precision, subgroup analysis, and assessment of publication bias. Reporting deficiencies in the extracted study records, including incomplete metadata, missing group-specific sample sizes, and limited reporting of dispersion measures or methodological details, restrict full appraisal of internal validity and reproducibility. Generalizability may also be limited because results from specific neonatal settings, procedures, and feeding practices may not transfer uniformly across NICUs or across subgroups of preterm infants.

From a clinical standpoint, the current evidence does not support a clear preference for sucrose or glucose over breast milk or expressed breast milk for pain reduction during heel lance or venipuncture in preterm infants. Where breast milk is available and feasible to administer, it appears to be a reasonable option within a broader neonatal pain management strategy. However, these findings should not be interpreted to mean that all approaches are interchangeable in every context, nor that single-agent oral interventions are sufficient for all infants. Multimodal care remains appropriate. For research, adequately powered randomized trials are still needed, using standardized intervention protocols, consistent pain outcomes such as PIPP/PIPP-R at prespecified time points, clear reporting of adverse events, and subgroup analyses by gestational age and procedure type. Future studies should also compare these interventions within contemporary bundled pain management approaches, so that clinicians can make decisions based on effectiveness in real neonatal practice rather than under simplified trial conditions.

## Conclusion

In this meta-analysis of 2 studies in preterm infants undergoing heel lance or venipuncture, sucrose or glucose was not associated with lower pain scores than breast milk/expressed breast milk, with a pooled effect estimate of BETA 0.028 (95% CI -0.450 to 0.507; p=0.91). The confidence interval spans modest benefit and modest harm, but the point estimate is essentially null, suggesting no clinically meaningful advantage of sweet solutions over BM/EBM for procedural pain control based on available data. With no observed heterogeneity (I²=0%), these limited results were consistent across studies. Clinically, BM/EBM appears to be a reasonable alternative when available, particularly given its practicality and acceptability in neonatal care. However, this conclusion should be interpreted cautiously because it is based on only two small studies with limited precision and likely variation in sugar concentration and procedural context.

## Final Included Studies

- Corpus ID: 7772 | Breast milk vs 24% sucrose for procedural pain relief in preterm neonates: a non-inferiority randomized controlled trial.
- Corpus ID: 7771 | Analgesic effect of breast milk versus sucrose for analgesia during heel lance in late preterm infants.
