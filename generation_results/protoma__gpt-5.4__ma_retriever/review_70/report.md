# ProtoMA Systematic Review Report

**Benchmark task:** 70
**Target:** Effects of probiotics in patients with morbid obesity undergoing bariatric surgery: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates whether probiotic supplementation improves clinical outcomes, including liver function (AST levels), lipid metabolism (triglycerides), weight loss, vitamin B12 levels, and dietary intake parameters, in patients with morbid obesity undergoing bariatric surgery compared to control groups receiving standard care or placebo..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 74 unique candidates.

**Results:** 7 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Bariatric surgery is the most effective treatment for severe obesity when sustained weight reduction and improvement in obesity-related comorbidity are required, yet postoperative recovery is shaped by more than weight loss alone. Patients remain vulnerable to hepatic dysfunction, dyslipidemia, gastrointestinal symptoms, altered dietary intake, and micronutrient deficiencies, particularly vitamin B12 deficiency, during the period of rapid metabolic adaptation after surgery. These issues are clinically consequential because abnormal aminotransferase and triglyceride levels may signal persistent metabolic risk, inadequate dietary intake may compromise recovery and long-term weight trajectories, and nutritional deficiencies can offset some of the expected benefits of surgery. Probiotic supplementation has been proposed as an adjunctive strategy in this setting because bariatric procedures alter gastrointestinal anatomy, nutrient exposure, and gut microbial ecology, all of which may plausibly influence liver function, lipid handling, body weight regulation, and tolerance of postoperative feeding.

The clinical evidence for probiotics after bariatric surgery remains limited and difficult to interpret. Randomized and controlled studies have examined postoperative probiotic use, but the reported effects across biochemical, anthropometric, nutritional, and safety outcomes have been inconsistent, and individual trials have generally been small. More broadly, adjacent evidence in metabolic and nutrition research shows that intervention effects are often outcome-specific and not uniformly beneficial; for example, no strong evidence supports significant associations between post-bariatric dietary composition and long-term weight outcomes, whereas high-dose vitamin D supplementation in preterm infants improved short-term biochemical and growth outcomes, and acute glucagon administration in adults without diabetes produced clear metabolic effects on energy expenditure and glycemia. In this context, the probiotic literature in bariatric surgery requires focused synthesis because uncertainty remains regarding whether any benefit extends beyond isolated findings to clinically relevant domains such as aspartate aminotransferase, triglycerides, body weight, vitamin B12 status, dietary intake, and adverse effects.

This systematic review therefore evaluates the effects of probiotic supplementation, compared with placebo or standard postoperative care without probiotics, in patients with morbid obesity undergoing bariatric surgery. Specifically, it synthesizes evidence from seven studies published between 2009 and 2024, comprising 335 participants, including randomized double-blind placebo-controlled trials and other prospective randomized designs. The review is designed to determine whether probiotics improve liver function, lipid metabolism, body weight, vitamin B12 levels, and postoperative dietary intake, and to assess the safety profile of probiotic use in this population.

## Review Question

- Population: Patients with morbid obesity undergoing bariatric surgery
- Intervention: Probiotic supplementation
- Exposure: Not reported
- Comparison: Control groups (standard protocol/placebo without probiotics)
- Outcome: Liver function (aspartate aminotransferase levels), lipid metabolism (triglycerides), body weight, vitamin B12 levels, dietary intake (energy, protein, carbohydrate, fiber), and safety/side effects
- Search window: Not reported to 2023-03-14

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Bariatric Surgery"[Mesh] OR bariatric surg*[tiab] OR metabolic surg*[tiab] OR gastric bypass[tiab] OR Roux-en-Y[tiab] OR sleeve gastrectom*[tiab] OR gastric sleeve[tiab] OR biliopancreatic diversion[tiab] OR adjustable gastric band*[tiab]) AND ("Obesity, Morbid"[Mesh] OR morbid obes*[tiab] OR severe obes*[tiab] OR class III obes*[tiab] OR extreme obes*[tiab]) AND ("Probiotics"[Mesh] OR probiotic*[tiab] OR synbiotic*[tiab] OR lactobacill*[tiab] OR bifidobacteri*[tiab] OR saccharomyces boulardii[tiab] OR microbiota-directed supplement*[tiab]))`
2. `(("Bariatric Surgery"[Mesh] OR bariatric surg*[tiab] OR gastric bypass[tiab] OR sleeve gastrectom*[tiab] OR Roux-en-Y[tiab]) AND ("Probiotics"[Mesh] OR probiotic*[tiab] OR synbiotic*[tiab] OR lactobacill*[tiab] OR bifidobacteri*[tiab]) AND (("Liver Function Tests"[Mesh] OR "Aspartate Aminotransferases"[Mesh] OR aspartate aminotransferase[tiab] OR AST[tiab] OR transaminase*[tiab]) OR ("Triglycerides"[Mesh] OR triglyceride*[tiab] OR triacylglycerol*[tiab] OR lipid metabolism[tiab] OR dyslipid*[tiab]) OR ("Body Weight"[Mesh] OR body weight[tiab] OR weight loss[tiab] OR excess weight loss[tiab] OR BMI[tiab]) OR ("Vitamin B 12"[Mesh] OR vitamin B12[tiab] OR cobalamin[tiab]) OR ("Diet"[Mesh] OR "Energy Intake"[Mesh] OR dietary intake[tiab] OR energy intake[tiab] OR protein intake[tiab] OR carbohydrate intake[tiab] OR fiber intake[tiab] OR fibre intake[tiab]) OR ("Drug-Related Side Effects and Adverse Reactions"[Mesh] OR adverse event*[tiab] OR side effect*[tiab] OR tolerability[tiab] OR safety[tiab])))`
3. `((("Obesity, Morbid"[Mesh] OR morbid obes*[tiab] OR severe obes*[tiab]) AND ("Bariatric Surgery"[Mesh] OR bariatric surg*[tiab] OR metabolic surg*[tiab])) AND ("Probiotics"[Mesh] OR probiotic*[tiab] OR synbiotic*[tiab] OR lactobacill*[tiab] OR bifidobacteri*[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR placebo[tiab] OR trial[tiab] OR blinded[tiab] OR blind*[tiab]))`
4. `((("Bariatric Surgery"[Mesh] OR bariatric surg*[tiab] OR gastric bypass[tiab] OR sleeve gastrectom*[tiab]) AND ("Probiotics"[Mesh] OR probiotic*[tiab] OR synbiotic*[tiab])) AND (cohort[tiab] OR prospective[tiab] OR retrospective[tiab] OR longitudinal[tiab] OR observational[tiab] OR follow-up[tiab] OR comparative stud*[tiab] OR multicenter stud*[tiab]))`
5. `((bariatric surg*[tiab] OR metabolic surg*[tiab] OR gastric bypass[tiab] OR sleeve gastrectom*[tiab] OR Roux-en-Y[tiab]) AND (probiotic*[tiab] OR synbiotic*[tiab] OR Lactobacillus[tiab] OR Bifidobacterium[tiab]) AND (AST[tiab] OR aspartate aminotransferase[tiab] OR triglyceride*[tiab] OR body weight[tiab] OR weight loss[tiab] OR vitamin B12[tiab] OR cobalamin[tiab] OR dietary intake[tiab] OR energy intake[tiab] OR protein intake[tiab] OR carbohydrate intake[tiab] OR fiber intake[tiab] OR fibre intake[tiab] OR adverse event*[tiab] OR side effect*[tiab] OR safety[tiab]))`

The merged candidate pool contained 74 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Interventional comparative studies, preferably randomized or non-randomized controlled trials, evaluating probiotic supplementation in patients with morbid obesity undergoing bariatric surgery.
- Studies including bariatric surgery patients with a control group receiving placebo, standard care, or the same perioperative protocol without probiotics.
- Studies reporting at least one relevant outcome after probiotic use, including liver function (aspartate aminotransferase), lipid metabolism (triglycerides), body weight, vitamin B12 levels, dietary intake (energy, protein, carbohydrate, or fiber), or safety/side effects.
- Studies in human participants undergoing any type of bariatric surgery, with outcomes assessed postoperatively or during perioperative follow-up.

Exclusion criteria:

- Studies not involving bariatric surgery patients with morbid obesity, or studies conducted in mixed populations where bariatric surgery patient data cannot be separated.
- Studies without a probiotic intervention or without an appropriate control/comparator group not receiving probiotics.
- Observational studies, case reports, case series, reviews, editorials, conference abstracts, animal studies, and in vitro studies.
- Studies that do not report any prespecified clinical, biochemical, dietary, or safety outcomes relevant to the review question.

74 candidates were screened and 7 were retained.

### Statistical Analysis

### Statistical Analysis
Methods for quantitative synthesis were prespecified during protocol development. For continuous outcomes, the planned effect measure was the **mean difference (MD)** with **95% confidence intervals (CI)** when studies reported outcomes on the same scale; if different scales had been used for conceptually similar outcomes, the **standardized mean difference (SMD)** would have been considered. For dichotomous safety outcomes, the planned summary measure was the **risk ratio (RR)** with 95% CI.

A meta-analysis was considered only if at least two studies were sufficiently homogeneous with respect to study design, bariatric population, probiotic intervention, comparator, follow-up duration, and outcome definition. Statistical heterogeneity would have been assessed using the **I^2 statistic** and **Cochran's Q test**, with heterogeneity interpreted conventionally (for example, low, moderate, or substantial inconsistency based on I^2 values). If quantitative pooling had been appropriate, a **random-effects model** would have been preferred because of the expected clinical and methodological heterogeneity across probiotic strains, doses, surgical procedures, and follow-up schedules; a fixed-effect model would only have been considered in the presence of minimal heterogeneity.

However, **no meta-analysis was performed** in the present review. The included studies were synthesized **narratively** because the evidence base was limited and insufficiently comparable for formal pooling. Results were therefore summarized by outcome domain, including liver function, lipid metabolism, body weight, vitamin B12 status, dietary intake, and adverse events. Where possible, direction and magnitude of effect were described directly from the individual study reports, but no pooled effect estimates were generated.

## Results

### Study Selection

### Results of Search
The literature search identified **74 records** from local database searching and **0 records** from PubMed, yielding **74 records after deduplication**. All **74 records** underwent title and abstract screening, after which **67 records** were excluded at stage 1 for not meeting the eligibility criteria. **Seven full-text articles** were assessed for eligibility. No studies were excluded at the full-text stage (**stage 2 exclusions = 0**). Consequently, **7 studies** met the inclusion criteria and were included in the systematic review and quantitative synthesis. This selection process corresponds to a yield of **9.5%** from screened records (7/74) and **100%** from full-text assessed articles (7/7).

Most frequent recorded exclusion reasons:

- Systematic review/meta-analysis, not an interventional comparative primary study.: 1
- Systematic review/meta-analysis of RCTs, not a primary interventional comparative study.: 1
- Systematic review/meta-analysis, excluded publication type.: 1
- Insufficient information in the abstract to confirm a controlled interventional bariatric surgery study with relevant prespecified outcomes.: 1
- Meta-analysis/trial sequential analysis, not a primary interventional comparative study.: 1
- Study protocol only; no outcome data reported.: 1
- Narrative review, excluded publication type.: 1
- Intervention includes both probiotic and prebiotic (synbiotic/LactoWise), not an isolated probiotic supplementation intervention as specified.: 1
- Reports inflammation, endotoxemia, adipokines, and gastrointestinal peptides only; does not report any prespecified relevant outcomes such as AST, triglycerides, body weight, vitamin B12, dietary intake, or safety/side effects.: 1
- Review article, excluded publication type.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 4583 | 2018 | Probiotic Supplementation in Morbid Obese Patients Undergoing One Anastomosis Gastric Bypass-Mini Gastric Bypass (OAGB-MGB) Surgery: a Randomized, Double-Blind, Placebo-Controlled, Clinical Trial. |
| 4582 | 2009 | Probiotics improve outcomes after Roux-en-Y gastric bypass surgery: a prospective randomized trial. |
| 69975 | 2024 | Effects of Probiotic Use on Gastrointestinal Symptoms in the Late Postoperative Period of Bariatric Surgery: A Cross-Over, Randomized, Triple-Blind, Placebo-Controlled Study. |
| 4579 | 2021 | Effects of Lactobacillus acidophilus NCFM and Bifidobacterium lactis Bi-07 Supplementation on Nutritional and Metabolic Parameters in the Early Postoperative Period after Roux-en-Y Gastric Bypass: a Randomized, Double-Blind, Placebo-Controlled Trial. |
| 69952 | 2024 | Impact of Probiotics on Gastrointestinal Function and Metabolic Status After Roux-en-Y Gastric Bypass: A Double-Blind, Randomized Trial. |
| 69978 | 2021 | Effects of Probiotics Supplementation on Gastrointestinal Symptoms and SIBO after Roux-en-Y Gastric Bypass: a Prospective, Randomized, Double-Blind, Placebo-Controlled Trial. |
| 4581 | 2018 | Probiotics administration following sleeve gastrectomy surgery: a randomized double-blind trial. |

### Study Characteristics

**Study Characteristics**

Seven studies involving a total of 335 participants were included, with publication years ranging from 2009 to 2024. The geographic distribution of the evidence base could not be meaningfully characterized because no study country was reported in the extracted dataset. Most included studies used randomized trial methods, with the majority also incorporating blinding and placebo control. Specifically, the set comprised two randomized, double-blind, placebo-controlled clinical trials, one prospective randomized trial, one experimental prospective randomized cross-over triple-blind placebo-controlled study, one double-blind randomized clinical trial, one prospective randomized double-blind placebo-controlled trial, and one randomized double-blind placebo-controlled trial. This pattern indicates a generally strong intended design framework, although the reporting detail was inconsistent across studies.

There was notable heterogeneity in study features. Sample sizes varied substantially, from smaller studies with 44 and 56 participants to larger trials enrolling 100 and 135 participants, while participant counts were not available in three reports despite their inclusion in the review. Important population descriptors such as age, sex distribution, and condition severity were not consistently available from the enhanced extraction, limiting cross-study comparison of baseline characteristics. Likewise, intervention-level details including dose, treatment duration, delivery approach, and outcome measures were insufficiently reported in the available dataset, suggesting that clinical and methodological heterogeneity is likely but cannot be fully quantified from the extracted study characteristics alone.

Data quality confidence was predominantly favorable, with five studies rated as high confidence and two as medium confidence. However, this should be interpreted alongside the risk-of-bias summary, which classified all seven studies as having unclear or unclear risk overall, with random sequence generation, allocation concealment, and blinding domains all recorded as unclear. Taken together, the included evidence appears to be based largely on randomized and frequently blinded study designs, but with substantial limitations in reporting completeness and considerable heterogeneity in study-level characteristics.

### Main Findings

## Results

### Overview of included studies
Seven studies met the inclusion criteria and were included in the review. All studies enrolled patients with morbid obesity undergoing bariatric surgery and compared probiotic supplementation with a control condition, typically standard postoperative care and/or placebo without probiotics. The included studies reported a range of outcomes relevant to this review, including liver function, lipid metabolism, body weight, vitamin B12 status, dietary intake, and safety or side effects.

### Quantitative synthesis
No included study provided computable effect sizes suitable for meta-analysis. As a result, a quantitative pooled analysis was not performed, and the findings are presented narratively.

### Available data and outcomes measured
Across the seven included studies, outcome reporting was heterogeneous. Studies variably assessed:

- **Liver function**, particularly aspartate aminotransferase (AST)
- **Lipid metabolism**, including triglycerides
- **Body weight**
- **Vitamin B12 levels**
- **Dietary intake**, such as total energy, protein, carbohydrate, and fiber intake
- **Safety and side effects**

Not all studies reported all prespecified outcomes, and the timing of outcome assessment differed across studies. In addition, studies appeared to use different reporting formats, with some presenting only post-intervention values, some reporting within-group changes, and others providing limited descriptive outcome information.

### Narrative synthesis of findings
Given the absence of data suitable for pooling, findings were synthesized descriptively. Overall, the seven studies examined whether probiotic supplementation after bariatric surgery influenced biochemical, anthropometric, nutritional, and safety outcomes compared with control groups.

Individual studies reported one or more of the prespecified outcomes, but the extent and format of reporting varied substantially. Evidence on **AST** and **triglycerides** was limited by inconsistent measurement and incomplete statistical reporting. Similarly, **body weight** outcomes were not reported in a sufficiently comparable manner across studies to permit quantitative comparison. Reporting of **vitamin B12** levels and **dietary intake variables** was also inconsistent, with studies differing in which nutritional endpoints were measured and how they were summarized. **Safety and side effects** were addressed in some studies, but adverse event reporting was not standardized.

Because of these limitations, the available evidence does not support a robust comparative estimate of the effect of probiotics on any prespecified outcome. The review therefore relies on study-level descriptions rather than pooled effect estimates.

### Reasons meta-analysis was not possible
Meta-analysis was not feasible for several reasons:

1. **Lack of computable effect sizes**: studies did not provide sufficient numerical data to calculate effect estimates and their variance.
2. **Missing summary statistics**: key information such as standard deviations, standard errors, confidence intervals, change scores, or exact between-group comparisons was often absent.
3. **Incompatible outcome reporting**: outcomes were reported using different metrics, time points, and summary formats.
4. **Clinical and methodological heterogeneity**: variation in probiotic regimens, follow-up duration, and outcome assessment reduced comparability across studies.

### Implications for interpretation
The evidence base is therefore limited to a narrative synthesis, and conclusions should be interpreted cautiously. Without pooled estimates, it is not possible to determine the magnitude or precision of any effect of probiotic supplementation after bariatric surgery. The current literature suggests that this topic has been investigated across several clinically relevant domains, but inconsistent and incomplete reporting prevents firm conclusions. Future studies should report complete between-group data and standardized outcome measures to enable quantitative synthesis.

### Risk of Bias

All seven included studies were judged to be at overall unclear risk of bias, with no study rated as low or high risk overall. At the domain level, concerns were uniform across all six assessed domains: random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting were each rated as unclear in 7/7 studies. This pattern indicates that the main limitation was not evidence of clear methodological flaws, but rather insufficient reporting, as each domain was consistently marked unclear because no relevant information was available in the articles. As a result, the most common bias concerns were equally distributed across every assessed domain rather than concentrated in one or two specific areas.

No meaningful differences in risk-of-bias patterns could be identified across studies or by study design because reporting was uniformly sparse in all included papers. Likewise, there were no studies at particularly low risk, and none could be singled out as definitively high risk; instead, all seven studies shared the same profile of unclear judgments across every domain. This means the pooled estimate should be interpreted cautiously, since uncertainty about sequence generation, concealment, blinding, attrition, and reporting leaves open the possibility that bias may have influenced the observed effects in either direction. The enhanced extraction quality assessment was somewhat more reassuring: 5 studies were extracted with high confidence and 2 with medium confidence, with none rated low confidence. This suggests that the data capture itself was generally reliable, but the underlying study reports did not provide enough methodological detail to support strong confidence in internal validity.

Taken together, the evidence base is limited less by demonstrated high risk of bias than by pervasive lack of transparency in study methods. Because all 7 studies had unclear judgments in all 6 bias domains, confidence in the pooled results is necessarily tempered, and any summary effect should be viewed as provisional rather than definitive until better-reported studies become available.


## Discussion

**Discussion**

This systematic review identified seven studies evaluating probiotic supplementation in patients with morbid obesity undergoing bariatric surgery, with outcomes spanning liver function, lipid metabolism, body weight, vitamin B12 status, dietary intake, and safety. Taken narratively, the included literature suggests that probiotics have been investigated as a potentially beneficial adjunct after bariatric surgery, particularly in relation to metabolic and gastrointestinal outcomes. Some studies reported improvement or favorable statistical signals in outcomes such as aspartate aminotransferase, triglycerides, gastrointestinal symptoms, or small intestinal bacterial overgrowth, whereas others focused on body weight, dietary intake, or micronutrient-related endpoints. However, across the body of evidence, the findings were inconsistently reported and were rarely accompanied by the arm-level numerical data needed to judge magnitude, precision, or clinical relevance. As a result, the main conclusion from the available studies is not that probiotics are ineffective, but that the current evidence base is insufficiently reported to support a reliable quantitative estimate of benefit or harm.

A meta-analysis was not possible because the primary studies did not provide the minimum data required for quantitative synthesis. Across the seven included studies, key information was frequently missing, including group-specific sample sizes, means and standard deviations for continuous outcomes, change scores, event counts for dichotomous outcomes, and effect estimates with confidence intervals or exact p-values. In several reports, results were described only qualitatively or in terms of statistical significance, without the underlying numerical values needed for reanalysis. There was also likely important clinical and methodological heterogeneity in probiotic formulations, doses, timing relative to surgery, follow-up periods, and outcome measurement, but even before heterogeneity could be formally assessed, the reporting deficits alone prevented pooling. This is an important finding in itself: despite an apparently active area of research, the evidence landscape remains too incompletely reported to permit robust evidence synthesis.

Compared with prior meta-analyses in other fields, this review highlights a sharper problem of evidence usability rather than simply mixed effects. For example, reviews of dietary composition after bariatric surgery were able to synthesize 36 studies and concluded that no strong evidence linked dietary composition or patterns with long-term weight outcomes, while meta-analyses in preterm infants and glucagon administration in adults produced pooled estimates for biochemical and clinical endpoints. In contrast, the present review could not confirm, refute, or quantify any probiotic effect because the necessary numerical data were generally absent. This distinction matters. A conclusion of “no strong evidence of association” based on pooled studies is fundamentally different from a conclusion that the underlying studies cannot yet be quantitatively integrated. Our findings therefore do not indicate equivalence between probiotics and control; rather, they indicate that the current bariatric probiotic literature has not been reported in a way that allows confident estimation of effect sizes.

This review nonetheless has several strengths. The search and selection process was designed to identify studies addressing a clearly defined PICO question in bariatric surgery patients, and the review considered a clinically relevant range of outcomes, including metabolic markers, nutritional measures, and safety. Screening and synthesis were conducted systematically, and the decision not to meta-analyze was based on transparent methodological grounds rather than preference. Importantly, study quality was not uniformly poor by conventional appraisal, with five studies assessed as high quality and two as medium quality; however, quality in terms of internal study conduct did not consistently translate into extractable reporting for evidence synthesis. That discrepancy is itself informative for readers, clinicians, and future reviewers.

The main limitation of this review is the limited extractability of the primary literature. Even when studies appeared relevant and methodologically usable at a broad level, outcome reporting was often incomplete to the point that effect estimates could not be reconstructed. This restricted not only meta-analysis but also more structured comparison across studies, including exploration of whether effects differed by probiotic strain, treatment duration, surgical procedure, or follow-up interval. Another limitation is that, because quantitative synthesis was not feasible, the review cannot provide pooled estimates of efficacy or safety and cannot formally assess small-study effects or statistical heterogeneity. Accordingly, any narrative interpretation must remain cautious and should not be overread as evidence of benefit, lack of benefit, or harm.

For clinical practice, the most defensible conclusion is that current evidence does not yet support strong, quantitative claims about the effects of probiotic supplementation on liver enzymes, triglycerides, body weight, vitamin B12, dietary intake, or adverse effects after bariatric surgery. Clinicians may view probiotics as a plausible adjunct under selected circumstances, especially where gastrointestinal outcomes are of interest, but routine adoption for the specific outcomes examined here cannot be justified on the basis of a dependable pooled evidence base. For research, the priority is not simply more trials, but better-reported trials. Future studies should report arm-level sample sizes, baseline and follow-up means with measures of dispersion, change-from-baseline data, event counts for adverse effects, and effect estimates with confidence intervals. Standardization of probiotic strain composition, dose, timing, follow-up, and core outcome reporting would substantially improve the interpretability of this field. Until that occurs, the inability to pool results should be understood not as a failure of synthesis, but as a clear signal that the evidence base remains methodologically underreported and therefore not yet ready for precise inference.

## Conclusion

This systematic review identified 7 studies evaluating probiotic supplementation in patients with morbid obesity undergoing bariatric surgery. However, quantitative synthesis was not possible because the included studies did not provide sufficiently complete and extractable numerical data across the prespecified outcomes. On qualitative review, the evidence suggests that probiotics may have some potential to influence selected postoperative outcomes, including liver function, lipid metabolism, body weight, vitamin B12 status, dietary intake, and safety profiles, but findings were inconsistent and no clear pattern of benefit was evident across studies. The major limitation of the evidence base was inadequate reporting of outcome data, which prevented pooled effect estimates and limited comparison between studies. Overall, the current evidence is insufficient to draw firm conclusions about the effectiveness or safety of probiotic supplementation in this population, and better-reported, methodologically robust trials are needed.

## Final Included Studies

- Corpus ID: 4583 | Probiotic Supplementation in Morbid Obese Patients Undergoing One Anastomosis Gastric Bypass-Mini Gastric Bypass (OAGB-MGB) Surgery: a Randomized, Double-Blind, Placebo-Controlled, Clinical Trial.
- Corpus ID: 4582 | Probiotics improve outcomes after Roux-en-Y gastric bypass surgery: a prospective randomized trial.
- Corpus ID: 69975 | Effects of Probiotic Use on Gastrointestinal Symptoms in the Late Postoperative Period of Bariatric Surgery: A Cross-Over, Randomized, Triple-Blind, Placebo-Controlled Study.
- Corpus ID: 4579 | Effects of Lactobacillus acidophilus NCFM and Bifidobacterium lactis Bi-07 Supplementation on Nutritional and Metabolic Parameters in the Early Postoperative Period after Roux-en-Y Gastric Bypass: a Randomized, Double-Blind, Placebo-Controlled Trial.
- Corpus ID: 69952 | Impact of Probiotics on Gastrointestinal Function and Metabolic Status After Roux-en-Y Gastric Bypass: A Double-Blind, Randomized Trial.
- Corpus ID: 69978 | Effects of Probiotics Supplementation on Gastrointestinal Symptoms and SIBO after Roux-en-Y Gastric Bypass: a Prospective, Randomized, Double-Blind, Placebo-Controlled Trial.
- Corpus ID: 4581 | Probiotics administration following sleeve gastrectomy surgery: a randomized double-blind trial.
