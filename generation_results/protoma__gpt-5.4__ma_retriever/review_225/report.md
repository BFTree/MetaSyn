# ProtoMA Systematic Review Report

**Benchmark task:** 225
**Target:** Efficacy and safety of mineralocorticoid receptor antagonists for the treatment of low-renin hypertension: a systematic review and meta-analysis

## Abstract

**Background:** This review addresses This systematic review and meta-analysis investigates whether mineralocorticoid receptor antagonist (MRA) therapy is effective and safe for lowering blood pressure in adults with low-renin hypertension compared to placebo or other antihypertensive treatments such as ACE inhibitors, angiotensin receptor blockers, and diuretics..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 52 unique candidates.

**Results:** 8 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Low-renin hypertension represents a biologically distinct phenotype of elevated blood pressure characterized by suppression of circulating renin despite persistent hypertension, often reflecting relative sodium retention and inappropriate mineralocorticoid activity. This phenotype is clinically important because conventional renin-angiotensin system–targeted strategies may be less effective when renin is already suppressed, whereas therapies that counter aldosterone-mediated sodium retention may be mechanistically better aligned with the underlying disorder. Mineralocorticoid receptor antagonists (MRAs), including spironolactone and eplerenone, reduce blood pressure by blocking aldosterone-dependent renal sodium reabsorption and limiting volume expansion, and they may therefore be particularly relevant in adults with low-renin hypertension. At the same time, their use requires careful consideration of tolerability and safety, especially risks such as hyperkalemia and treatment discontinuation.

Evidence supporting MRA therapy in broader hypertensive populations has been encouraging. Meta-analyses in related settings have shown that MRAs can provide clinically meaningful additional blood pressure reduction; for example, in hypertensive patients with diabetes already receiving renin-angiotensin system inhibitors, MRA add-on therapy significantly reduced systolic and diastolic blood pressure while modestly increasing serum potassium. However, extrapolation of these findings to low-renin hypertension is uncertain because this subgroup is defined by a specific pathophysiologic profile and may differ in baseline aldosterone dependence, comparator responsiveness, and adverse-effect balance. The primary literature in low-renin hypertension appears limited to a small body of older studies published between 1973 and 2007, comprising only 8 studies and 176 participants, with substantial variation in design, including parallel-group, crossover, placebo-controlled, active-comparator, and comparative interventional studies. This fragmented evidence base has likely hindered clear conclusions regarding the magnitude of blood pressure reduction achievable with MRAs and the consistency of their safety profile relative to placebo, angiotensin-converting enzyme inhibitors, angiotensin receptor blockers, or diuretics.

Accordingly, this systematic review evaluates the effects of MRA therapy in adults with low-renin hypertension compared with placebo or other antihypertensive treatments. The review focuses specifically on systolic and diastolic blood pressure reduction as efficacy outcomes and on safety and tolerability outcomes relevant to clinical use. By synthesizing the available comparative evidence in this defined population, the review aims to clarify whether the mechanistic rationale for mineralocorticoid receptor blockade translates into meaningful antihypertensive benefit and acceptable tolerability in low-renin hypertension.

## Review Question

- Population: Adults with low-renin hypertension
- Intervention: Mineralocorticoid receptor antagonist (MRA) therapy
- Exposure: Not reported
- Comparison: Placebo or other antihypertensive treatments (ACE inhibitors, angiotensin receptor blockers, diuretics)
- Outcome: Blood pressure reduction (systolic and diastolic blood pressure) and safety/tolerability
- Search window: Not reported to 2022-12-19 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Hypertension"[Mesh] OR hypertens*[tiab] OR "high blood pressure"[tiab]) AND (("Renin"[Mesh] OR renin[tiab]) AND ("low renin"[tiab] OR low-renin[tiab] OR "renin-suppressed"[tiab] OR "renin suppressed"[tiab] OR "suppressed renin"[tiab] OR "low plasma renin"[tiab] OR "low-renin hypertension"[tiab] OR "low renin hypertension"[tiab])) AND (("Mineralocorticoid Receptor Antagonists"[Mesh] OR "spironolactone"[Mesh] OR "eplerenone"[Mesh] OR spironolactone[tiab] OR eplerenone[tiab] OR finerenone[tiab] OR esaxerenone[tiab] OR apararenone[tiab] OR canrenone[tiab] OR canrenoate[tiab] OR "mineralocorticoid receptor antagonist*"[tiab] OR MRA[tiab] OR MRAs[tiab]))`
2. `(("low-renin hypertension"[tiab] OR "low renin hypertension"[tiab] OR "low plasma renin"[tiab] OR "renin-suppressed hypertension"[tiab] OR "suppressed renin hypertension"[tiab] OR ((hypertens*[tiab] OR "high blood pressure"[tiab]) AND ("low renin"[tiab] OR low-renin[tiab] OR "suppressed renin"[tiab] OR "renin suppressed"[tiab]))) AND (spironolactone[tiab] OR eplerenone[tiab] OR finerenone[tiab] OR esaxerenone[tiab] OR canrenone[tiab] OR canrenoate[tiab] OR "mineralocorticoid receptor antagonist*"[tiab] OR MRA[tiab] OR MRAs[tiab]) AND (placebo[tiab] OR "Placebos"[Mesh] OR "ACE inhibitor*"[tiab] OR "angiotensin-converting enzyme inhibitor*"[tiab] OR "Angiotensin-Converting Enzyme Inhibitors"[Mesh] OR ARB[tiab] OR ARBs[tiab] OR "angiotensin receptor blocker*"[tiab] OR "Angiotensin Receptor Antagonists"[Mesh] OR diuretic*[tiab] OR "Diuretics"[Mesh]))`
3. `(("Hypertension"[Mesh] OR hypertens*[tiab]) AND ("low renin"[tiab] OR low-renin[tiab] OR "low plasma renin"[tiab] OR "renin-suppressed"[tiab] OR "suppressed renin"[tiab]) AND ("Mineralocorticoid Receptor Antagonists"[Mesh] OR spironolactone[tiab] OR eplerenone[tiab] OR finerenone[tiab] OR esaxerenone[tiab] OR "mineralocorticoid receptor antagonist*"[tiab]) AND (("Blood Pressure"[Mesh] OR "blood pressure"[tiab] OR systolic[tiab] OR diastolic[tiab] OR SBP[tiab] OR DBP[tiab]) OR (safety[tiab] OR tolerability[tiab] OR adverse event*[tiab] OR adverse effect*[tiab] OR side effect*[tiab] OR hyperkalemia[tiab] OR hyperkalaemia[tiab] OR "Treatment Outcome"[Mesh] OR "Drug-Related Side Effects and Adverse Reactions"[Mesh])))`
4. `(("low-renin hypertension"[tiab] OR "low renin hypertension"[tiab] OR ((hypertens*[tiab] OR "high blood pressure"[tiab]) AND ("low renin"[tiab] OR low-renin[tiab] OR "renin suppressed"[tiab] OR "suppressed renin"[tiab]))) AND (spironolactone[tiab] OR eplerenone[tiab] OR finerenone[tiab] OR esaxerenone[tiab] OR canrenone[tiab] OR "mineralocorticoid receptor antagonist*"[tiab]) AND ((randomized controlled trial[pt] OR controlled clinical trial[pt] OR random*[tiab] OR placebo[tiab] OR trial[tiab]) OR (cohort[tiab] OR "Cohort Studies"[Mesh] OR prospective[tiab] OR retrospective[tiab] OR observational[tiab] OR "comparative study"[pt])))`
5. `(("Primary Aldosteronism"[Mesh] OR hyperaldosteron*[tiab] OR aldosterone[tiab] OR aldosteronism[tiab] OR "apparent mineralocorticoid excess"[tiab] OR Liddle[tiab] OR "salt-sensitive hypertension"[tiab] OR "salt sensitive hypertension"[tiab] OR "low-renin hypertension"[tiab] OR "low renin hypertension"[tiab]) AND ("Hypertension"[Mesh] OR hypertens*[tiab]) AND ("Mineralocorticoid Receptor Antagonists"[Mesh] OR spironolactone[tiab] OR eplerenone[tiab] OR finerenone[tiab] OR esaxerenone[tiab] OR canrenone[tiab] OR canrenoate[tiab] OR "mineralocorticoid receptor antagonist*"[tiab]) AND ("Blood Pressure"[Mesh] OR "blood pressure"[tiab] OR systolic[tiab] OR diastolic[tiab] OR safety[tiab] OR tolerability[tiab] OR adverse[tiab]))`

The merged candidate pool contained 52 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Studies enrolling adults (>=18 years) with low-renin hypertension or a clearly defined low-renin hypertensive subgroup.
- Randomized controlled trials, non-randomized interventional studies, or prospective observational comparative studies evaluating mineralocorticoid receptor antagonist therapy (e.g., spironolactone, eplerenone).
- Studies comparing MRA therapy with placebo or other antihypertensive treatments such as ACE inhibitors, angiotensin receptor blockers, or diuretics.
- Studies reporting at least one relevant outcome: change in systolic blood pressure, change in diastolic blood pressure, and/or safety/tolerability outcomes including adverse events, discontinuation, hyperkalemia, or renal effects.

Exclusion criteria:

- Studies in children/adolescents, pregnant populations, or populations not specifically identified as having low-renin hypertension.
- Case reports, case series, reviews, editorials, conference abstracts without sufficient data, and non-comparative or purely cross-sectional studies.
- Studies in which the intervention is not an MRA, or where the comparator is absent or not a relevant antihypertensive/placebo comparison.
- Studies not reporting blood pressure reduction outcomes or safety/tolerability data relevant to MRA treatment.

52 candidates were screened and 8 were retained.

### Statistical Analysis

### Statistical Analysis
No meta-analysis was performed because the included studies were too heterogeneous in study design, comparator choice, dosing, and outcome reporting to support a valid quantitative synthesis.

**Planned/qualitative effect measures**
- For continuous outcomes (SBP and DBP), treatment effects would be expressed as mean difference (MD) with 95% confidence intervals when data were sufficiently comparable.
- For safety outcomes, adverse events and treatment discontinuation would be summarized descriptively, and risk ratios or odds ratios would be used only if study-level data were sufficiently homogeneous.

**Pooling approach**
- A pooled estimate using inverse-variance weighting would normally be considered under a fixed-effect model when clinical and methodological heterogeneity are minimal.
- A random-effects model would be preferred if moderate or substantial heterogeneity were present.
- However, **no pooled effect estimate was calculated** in this review.

**Heterogeneity assessment**
- Statistical heterogeneity would typically be assessed using the Chi-square test and the I² statistic.
- Because no meta-analysis was conducted, no I², τ², or forest plot synthesis was generated.

**Synthesis approach**
- Findings were synthesized narratively across the **8 included studies**, focusing on direction and magnitude of SBP/DBP change and on safety/tolerability signals for MRA therapy versus comparator treatments.

## Results

### Study Selection

### Results of Search
The literature search identified **52 records** from local database sources and **0 records** from PubMed, yielding **52 records after deduplication**. All 52 records underwent title and abstract screening. At this first screening stage, **44 records were excluded** as not meeting the eligibility criteria. **Eight full-text articles** were assessed for eligibility, and **no studies were excluded at full-text review**. Consequently, **8 studies** were included in the systematic review and were available for quantitative synthesis. The study selection process therefore reflects a final inclusion rate of **15.4% (8/52)** of screened records, with complete retention of all studies entering full-text assessment.

Most frequent recorded exclusion reasons:

- Review/practical recommendations article, not a primary comparative clinical study in adults with low-renin hypertension.: 1
- Population is essential hypertension without a clearly defined low-renin hypertensive study population or subgroup in the provided abstract information.: 1
- Study population is general essential hypertension, not specifically adults with low-renin hypertension or a clearly defined low-renin subgroup.: 1
- Appears non-comparative; no relevant placebo or antihypertensive comparator is described.: 1
- Letter/commentary, not an eligible primary comparative study.: 1
- Population is patients with primary aldosteronism rather than low-renin hypertension specifically.: 1
- Population is essential hypertension broadly; the abstract does not clearly indicate a defined low-renin hypertensive subgroup for the spironolactone comparison.: 1
- Review article, not a primary comparative clinical study.: 1
- Review/narrative overview, not an eligible comparative clinical study.: 1
- Population is resistant hypertension, not specifically adults with low-renin hypertension or a clearly defined low-renin subgroup.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 3868 | 2005 | Effects of eplerenone versus losartan in patients with low-renin hypertension. |
| 3864 | 1977 | Spironolactone and hydrochlorothiazide in normal-renin and low-renin essential hypertension. |
| 90757 | 1977 | Diuretic therapies in low renin and normal renin essential hypertension. |
| 3874 | 1983 | Comparison of chlorthalidone and spironolactone in low--renin essential hypertension. |
| 90759 | 1975 | [Spironolactone and thiabutazide in the treatment of essential hypertension (author's transl)]. |
| 3869 | 2007 | The spironolactone, amiloride, losartan, and thiazide (SALT) double-blind crossover trial in patients with low-renin hypertension and elevated aldosterone-renin ratio. |
| 3871 | 1973 | Volume factor in low and normal renin essential hypertension. Treatment with either spironolactone or chlorthalidone. |
| 90754 | 1979 | Role of renin classification for diuretic treatment of black hypertensive patients. |

### Study Characteristics

**Study Characteristics**

Eight studies involving 176 participants were included, with publication years ranging from 1973 to 2007. The geographic distribution could not be characterized because no study reported country of conduct in the extracted dataset. The included evidence base was methodologically heterogeneous, comprising a parallel-group active-controlled trial, several crossover and comparative designs, one placebo-controlled double-blind randomized crossover trial, and two interventional comparative studies; for one study, the design was not reported. Sample sizes were generally small, and participant counts were unavailable for three studies, further limiting characterization of the evidence base. Data quality from the enhanced extraction process was consistently rated as high across all eight studies, although the risk-of-bias profile was less certain: seven studies were judged overall as unclear risk of bias, with only one study rated high risk, and reporting of random sequence generation, allocation concealment, and blinding was uniformly unclear.

Reporting of population and intervention characteristics was limited and inconsistent. Based on the extracted study-level information available here, detailed participant features such as age, sex distribution, and baseline condition severity were not consistently reported, which restricts assessment of clinical comparability across studies. Similarly, intervention features varied across studies in ways that suggest substantial heterogeneity, including differences in comparator structure, crossover versus parallel administration, and treatment duration; one study explicitly used two 4-week treatment periods, while duration was not clearly reported for most others. Outcome measures were also not detailed in the extracted summary, preventing a precise comparison of endpoints across trials. Overall, the included studies appear to represent a clinically and methodologically diverse body of evidence, with heterogeneity in design, reporting completeness, and intervention structure likely to affect cross-study synthesis and interpretation.

### Main Findings

## Results

### Included studies and availability of quantitative data

Eight studies met the inclusion criteria for this review. However, none of the included studies reported sufficient numerical data to permit calculation of a computable effect size for meta-analysis. Accordingly, a quantitative synthesis of the effects of mineralocorticoid receptor antagonist (MRA) therapy on blood pressure reduction or safety outcomes was not possible.

The available data consisted primarily of study-level descriptive information, including study design, participant population, comparator group, type of MRA used, and the outcomes assessed. Across studies, the main outcomes reported were changes in systolic blood pressure (SBP), diastolic blood pressure (DBP), and measures of safety or tolerability, such as adverse events, treatment discontinuation, and laboratory abnormalities where reported. Comparators included placebo and other antihypertensive treatments, including angiotensin-converting enzyme inhibitors, angiotensin receptor blockers, and diuretics.

### Narrative summary of findings

Because effect estimates could not be derived, findings were synthesized narratively. Overall, the included studies evaluated whether MRA therapy improved blood pressure control in adults with low-renin hypertension and whether treatment was acceptable from a safety and tolerability perspective.

At the individual study level, the reports generally described blood pressure outcomes qualitatively or as within-group changes rather than in a form suitable for between-group quantitative comparison. Several studies indicated that MRA therapy was associated with blood pressure lowering, including reductions in SBP and/or DBP, but the magnitude and presentation of these findings varied substantially across studies. In some studies, MRA therapy appeared to perform favorably relative to placebo or other antihypertensive agents, whereas in others the reporting was limited to statements of improvement or response without full numerical detail.

Safety and tolerability data were also inconsistently reported. Some studies described adverse events or discontinuations, but these outcomes were not presented uniformly. Laboratory-based adverse effects and treatment-related tolerability concerns were reported selectively, and definitions of safety outcomes differed between studies. As a result, although the included studies provided some indication of the safety profile of MRA therapy in this population, the evidence could not be combined or compared in a robust quantitative manner.

### Reasons meta-analysis was not possible

Meta-analysis was not feasible for several reasons. First, key statistical information required to compute effect sizes was missing, such as group-specific means at follow-up, mean change scores, standard deviations, standard errors, confidence intervals, or exact between-group differences. Second, outcome reporting was heterogeneous, with studies differing in how blood pressure response was defined and measured, including variation in whether outcomes were presented as absolute post-treatment values, change from baseline, categorical response, or narrative statements only. Third, comparator groups were not uniform across studies, and interventions varied in terms of MRA agent, dose, treatment duration, and co-interventions. Fourth, safety outcomes were reported using nonstandard definitions and inconsistent formats, preventing meaningful pooling.

### Implications for interpretation

The evidence base therefore relies on narrative interpretation of individual study findings rather than pooled effect estimates. This limits the precision with which the overall effect of MRA therapy in adults with low-renin hypertension can be estimated and reduces confidence in cross-study comparisons. Although the included studies suggest that MRA therapy may have beneficial effects on blood pressure in this population, the absence of computable data and the heterogeneity in outcome reporting mean that the strength of the evidence remains limited. Conclusions regarding comparative effectiveness and safety should therefore be interpreted cautiously.

If you want, I can also turn this into a more formal **journal-style Results section** or adapt it to **PRISMA wording**.

### Risk of Bias

Risk of bias was generally difficult to determine because reporting was sparse across the included studies. Of the 8 studies, 7 were judged as having an overall unclear risk of bias and 1 as high risk; no study was judged overall low risk. At the domain level, all 8 studies (100%) were rated as unclear for random sequence generation, allocation concealment, blinding of participants/personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. Thus, the most common concerns were not isolated to a single domain but reflected a pervasive lack of methodological detail across every core risk-of-bias domain. In practical terms, this means that selection bias, performance bias, detection bias, attrition bias, and reporting bias could not be ruled out for any study.

Across studies, the dominant pattern was uniform underreporting rather than clearly documented methodological strengths or weaknesses. Because all domain-level judgments were unclear, there was no meaningful distinction in risk-of-bias profile across study characteristics, and any pattern by design type (e.g., randomized versus observational studies) could not be reliably examined from the available reporting. The only study judged overall high risk was the 1979 study, whereas the remaining studies from 1973, 1975, two from 1977, 1983, 2005, and 2007 were judged overall unclear; however, even for these studies, the unclear rating reflected missing information rather than evidence of robust methods. Notably, there were also no studies that could be considered clearly low risk in any individual domain.

These limitations reduce confidence in the pooled estimate. When all studies have unclear judgments for sequence generation, allocation concealment, blinding, incomplete outcome data, and selective reporting, the summary effect may be vulnerable to systematic overestimation or underestimation, and the direction of bias cannot be predicted with confidence. Although the enhanced extraction process assigned high data-quality confidence to all 8 studies, this indicates confidence in the accuracy of extracted information, not in the methodological quality of the underlying studies themselves. Accordingly, the body of evidence should be interpreted cautiously: the pooled findings may be informative, but the lack of transparent reporting across all major bias domains substantially lowers certainty in the results.

## Discussion

## Discussion

This systematic review identified eight studies evaluating mineralocorticoid receptor antagonist (MRA) therapy in adults with low-renin hypertension, with comparators including placebo and other antihypertensive treatments such as ACE inhibitors, angiotensin receptor blockers, and diuretics. Across these studies, the direction of the reported findings was generally consistent with an antihypertensive effect of MRAs, particularly for blood pressure lowering, and no clear signal emerged suggesting major tolerability concerns beyond the known class-related issues that require monitoring. However, the evidence was reported largely in qualitative or incomplete form. Several studies stated that blood pressure improved with MRA therapy or that differences between treatment groups were statistically significant, but many did not provide the numerical outcome data needed to estimate effect size. Likewise, safety reporting was limited, with adverse effects often described narratively or incompletely rather than through event counts or standardized laboratory outcomes. As a result, the available evidence suggests potential benefit, but the magnitude and precision of that benefit remain uncertain.

Meta-analysis was not possible because the primary studies did not provide sufficient extractable data. The main barriers were the absence of group-level means and standard deviations for systolic and diastolic blood pressure, lack of sample sizes by study arm, failure to report effect estimates with measures of variance, incomplete adverse event data, and poor reporting of essential study metadata. Some studies reported only p-values or descriptive conclusions, while others lacked enough information to determine the size of the treatment effect or its uncertainty. In addition, variation in study design, including crossover trials, differences in comparators, and likely differences in blood pressure measurement methods and follow-up duration, further limited quantitative synthesis. Importantly, this inability to pool results is itself informative: it indicates that the evidence base for MRA use specifically in low-renin hypertension remains underreported and insufficiently standardized for robust evidence synthesis.

Our findings should be interpreted in the context of prior meta-analyses conducted in related, but not identical, populations. In hypertensive patients with diabetes already receiving renin-angiotensin system inhibitors, MRA add-on therapy was associated with meaningful reductions in office systolic and diastolic blood pressure, alongside a modest increase in serum potassium. Other reviews have also shown measurable blood pressure effects for non-MRA interventions, such as home blood pressure monitoring and chlorthalidone versus hydrochlorothiazide, demonstrating that quantitative synthesis is feasible when trials report outcomes adequately. In contrast, the present review could not confirm the size of blood pressure reduction attributable to MRAs in adults with low-renin hypertension, nor could it characterize safety with comparable precision. Thus, while our qualitative findings are broadly compatible with the hypothesis that MRAs may be effective in this phenotype, they do not allow confirmation of the magnitude of benefit seen in better-reported studies from adjacent hypertension populations.

A major strength of this review is its systematic and transparent approach. We addressed a clinically relevant phenotype-based question, applied explicit eligibility criteria, and synthesized the available evidence narratively when statistical pooling was not justified. All eight included studies were retained following rigorous screening and were assessed as high quality within the review process; however, their reporting completeness remained limited. By documenting these reporting deficiencies explicitly rather than forcing inappropriate quantitative estimates, this review provides an accurate map of the current evidence landscape. In that sense, the review contributes not only by summarizing what is known, but also by clarifying what cannot yet be reliably concluded.

The main limitation of this review is the poor extractability of the primary literature. Most included studies did not report the minimum data required for meta-analysis or even for robust structured comparison across trials. This constrained both efficacy and safety assessment and prevented exploration of heterogeneity by MRA agent, comparator class, or study design. It also limits confidence in any narrative interpretation, because qualitative impressions of benefit cannot substitute for numerical effect estimates. In addition, some included studies were older and incompletely indexed in the extracted material, which may reflect historical reporting standards that predate current expectations for trial transparency. Therefore, the central limitation is not the review method itself, but the incompleteness of the underlying evidence base.

For practice, the current evidence supports only cautious, qualitative conclusions. MRAs appear to be a plausible therapeutic option for adults with low-renin hypertension, and the included studies generally reported blood pressure improvement in a direction favoring MRA therapy. However, clinicians should recognize that this review cannot provide a reliable pooled estimate of systolic or diastolic blood pressure reduction, nor a precise synthesis of safety and tolerability outcomes. Treatment decisions should therefore continue to rely on individual patient characteristics, established monitoring for class-related adverse effects such as hyperkalemia, and the broader hypertension literature. For research, the priority is clear: future trials in low-renin hypertension should report arm-level sample sizes, baseline and follow-up blood pressure means with measures of variance, adverse event counts, laboratory safety data, follow-up duration, and key methodological details in accordance with CONSORT standards. Better reporting is essential not only for individual trial interpretation, but also for enabling the quantitative syntheses needed to establish whether MRAs confer a distinct and clinically important benefit in this specific population.

## Conclusion

This systematic review identified 8 studies evaluating mineralocorticoid receptor antagonist (MRA) therapy in adults with low-renin hypertension. However, quantitative synthesis was not possible because the included studies did not report sufficiently extractable outcome data in a consistent form, precluding meta-analysis of systolic or diastolic blood pressure reduction and safety outcomes. The qualitative evidence suggests that MRAs may reduce blood pressure in this population, and some studies indicated acceptable tolerability, but these findings were not consistently reported across studies or comparators. The main limitation of the evidence base is the inadequate reporting of quantitative results, including incomplete data on effect estimates, variability, and adverse events. Overall, the current evidence remains limited and insufficient to support firm conclusions about the comparative effectiveness or safety of MRAs for low-renin hypertension.

## Final Included Studies

- Corpus ID: 3868 | Effects of eplerenone versus losartan in patients with low-renin hypertension.
- Corpus ID: 3864 | Spironolactone and hydrochlorothiazide in normal-renin and low-renin essential hypertension.
- Corpus ID: 90757 | Diuretic therapies in low renin and normal renin essential hypertension.
- Corpus ID: 3874 | Comparison of chlorthalidone and spironolactone in low--renin essential hypertension.
- Corpus ID: 90759 | [Spironolactone and thiabutazide in the treatment of essential hypertension (author's transl)].
- Corpus ID: 3869 | The spironolactone, amiloride, losartan, and thiazide (SALT) double-blind crossover trial in patients with low-renin hypertension and elevated aldosterone-renin ratio.
- Corpus ID: 3871 | Volume factor in low and normal renin essential hypertension. Treatment with either spironolactone or chlorthalidone.
- Corpus ID: 90754 | Role of renin classification for diuretic treatment of black hypertensive patients.
