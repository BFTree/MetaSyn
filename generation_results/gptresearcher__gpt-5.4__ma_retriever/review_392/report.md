# Systematic Review Report: Salt Intake, Blood Pressure, and Cardiovascular Outcomes Across Study Designs in the Local MetaSyn Corpus

## Abstract

This report systematically reviews evidence from the local MetaSyn PubMed corpus on salt intake and related sodium/potassium exposures in relation to blood pressure and cardiovascular outcomes, with attention to randomized controlled trials (RCTs), observational cohorts, and Mendelian randomization (MR) evidence. The user’s query framed this as an evidence-triangulation case study, but the corpus material retrieved for the prespecified period and topic was dominated by RCTs, systematic reviews, and observational cohorts rather than MR studies specific to sodium intake. After screening the retrieved records against the stated eligibility criteria, no direct MR study on sodium intake and major cardiovascular outcomes in hypertensive populations was identified. The most policy-relevant causal evidence came from higher-quality randomized and systematic-review evidence showing that sodium reduction and low-sodium salt substitutes lower blood pressure, while observational evidence suggested that potassium intake is protective for stroke mortality and that sodium exposure may follow a non-linear association with cardiovascular outcomes. Safety evidence for potassium-enriched salt substitutes remained incomplete in chronic kidney disease (CKD) and among people taking renin-angiotensin-aldosterone system (RAAS)-modifying medications because high-risk individuals were usually excluded from trials. Overall, the local corpus supports a firm conclusion that sodium reduction causally lowers blood pressure, but it does **not** support a similarly firm conclusion that currently available MR evidence, within this corpus and search frame, materially strengthens causal inference for major cardiovascular outcomes in hypertensive populations. The triangulation is therefore incomplete, and any automated synthesis claiming convergence across RCT, observational, and MR branches would be overstated based on the retrieved corpus alone.

## Introduction

High salt intake is a longstanding candidate cause of elevated blood pressure and downstream cardiovascular disease. The research question supplied here asks whether evidence can be triangulated across multiple designs—observational studies, MR studies, and randomized trials—to support automated causal synthesis. For this assignment, retrieval was restricted to the **local MetaSyn corpus only**, and the review had to preserve exact Corpus IDs from search results.

A critical methodological constraint shaped this report: the supplied search evidence and candidate list overwhelmingly favored salt-reduction RCTs, systematic reviews, and observational cohort studies, while the corpus did **not** surface strong MR evidence directly testing sodium or salt intake against major cardiovascular outcomes in hypertensive populations. That gap is itself an important finding for triangulation, because evidence convergence cannot be asserted when one branch is missing or only indirectly represented.

## Methods

### Retrieval Source

Only the local MetaSyn PubMed corpus was used, as required.

### Search Strategy

The provided corpus output documented the following local corpus query:

`((randomized controlled trial OR clinical trial OR intervention) AND (salt substitute OR potassium-enriched salt OR low-sodium salt OR sodium reduction) AND (cardiovascular mortality OR major adverse cardiovascular events OR stroke OR all-cause mortality OR safety OR hyperkalemia) AND (hypertension OR hypertensive OR chronic kidney disease OR diabetes OR RAAS inhibitor OR ACE inhibitor OR ARB))`

This query returned 20 candidate records from the local corpus search tool, including Corpus IDs `22682`, `79420`, `69247`, `91520`, `29105`, `69240`, `91514`, `77386`, `6783`, `14902`, and `86637` as the most relevant records cited in the supplied research notes ([MetaSyn corpus search result](mcp://search_metasyn_corpus/0)).

### Eligibility Criteria

#### Inclusion
- Studies from the local MetaSyn corpus relevant to salt/sodium intake, salt substitutes, potassium-enriched salt, or sodium-to-potassium balance.
- Outcomes involving blood pressure, cardiovascular disease, cardiovascular mortality, stroke, heart failure, atrial fibrillation, myocardial infarction, renal safety, or related clinical safety endpoints.
- Study designs of interest: RCTs, observational cohorts, and MR studies.
- For MR studies specifically, titles and abstracts had to contain the phrase “Mendelian randomization.”

#### Exclusion
- Relations where statistical significance was “not found.”
- Studies not providing empirical results relevant to the research question.
- Non-primary evidence from the final included-study list where a more directly relevant primary study was available, though systematic reviews were still used to contextualize the field because the query explicitly concerned synthesis across evidence branches.
- Records outside the practical topical scope of salt intake and cardiovascular/blood-pressure inference.

### Screening Logic

Because the research question specifically emphasized triangulation across study designs, the screening prioritized:
1. Direct salt/sodium exposure studies.
2. Hypertensive, diabetic, or CKD-relevant populations.
3. Primary studies when available.
4. MR evidence meeting the exact phrase requirement.

## Retrieval and Screening Results

### Candidate Screening Summary

The supplied search output and notes indicated that the retrieved literature was **not balanced across design types**. Most high-ranking records were:
- Systematic reviews of salt substitutes or sodium reduction,
- RCTs of sodium reduction,
- Observational cohorts on sodium or potassium exposure,
- CKD cohort analyses of urinary sodium-to-potassium ratio.

The search notes explicitly stated that **the results did not show a Mendelian randomization study directly addressing sodium or salt intake and major cardiovascular outcomes in people with hypertension**, and that most high-ranking matches were randomized trials, systematic reviews, or observational cohorts instead ([Replacing salt with low-sodium salt substitutes](metasyn://corpus/22682)).

One candidate MR-related result linked genetically predicted “adding salt to food” with myocardial infarction, but it was not specific to hypertensive populations and did not isolate total sodium intake as the primary exposure; thus, it did not satisfy the focused causal question well enough for inclusion as core triangulation evidence ([MR-related candidate on salt-adding behavior](metasyn://corpus/86637)).

### Included Evidence Types

| Evidence branch | Included? | Rationale |
|---|---:|---|
| Randomized trials | Yes | Strong direct evidence on sodium reduction and blood pressure |
| Observational cohorts | Yes | Relevant to long-term cardiovascular and stroke outcomes |
| Mendelian randomization | No direct eligible study | No directly relevant hypertensive-population MR study surfaced in retrieval |

## Included Studies and Findings

## 1. Randomized and Systematic-Review Evidence

### Low-sodium salt substitutes

The strongest broad intervention evidence came from the 2022 Cochrane review on low-sodium salt substitutes (Corpus ID `22682`). It included 26 RCTs and 34,961 adults and found that replacing regular salt with low-sodium salt substitutes lowered blood pressure and **may** reduce cardiovascular events and cardiovascular mortality in adults ([Cochrane review on low-sodium salt substitutes](metasyn://corpus/22682)).

This review is especially important because it addresses both efficacy and scalability. It supports the view that low-sodium salt substitutes are a practical population strategy, particularly where discretionary salt accounts for a large share of intake. However, its safety interpretation must be narrowed: all 26 trials excluded participants in whom increased potassium intake was known to be potentially harmful, and although seven studies included some adults possibly at risk of hyperkalemia, the overall safety evidence remains incomplete for CKD, ACE inhibitor users, ARB users, and related high-risk groups ([Cochrane review on low-sodium salt substitutes](metasyn://corpus/22682)).

My judgment is that this is the most policy-actionable source in the corpus, but it should **not** be generalized without caution to people with impaired potassium excretion.

### Sodium reduction in people with diabetes

The 2023 Cochrane review on altered dietary salt intake in diabetes (Corpus ID `69247`) found that reduced sodium intake lowered blood pressure in randomized trials. In longer-term studies lasting 4 to 12 weeks, systolic blood pressure fell by about **6.15 mm Hg** and diastolic blood pressure by about **3.41 mm Hg**. Effects were similar in hypertensive and normotensive participants, though certainty was low ([Altered dietary salt intake for preventing diabetic kidney disease and its progression](metasyn://corpus/69247)).

This matters for triangulation because it shows the sodium-blood-pressure relationship holds even in metabolically complex populations. Despite low certainty and small sample sizes, directionality was consistent. The evidence supports a causal interpretation for blood-pressure lowering, but not yet for hard cardiovascular endpoints within diabetic subgroups.

### Short-term hypertension RCT isolating sodium as the main driver

A 2025 double-blind RCT in hypertension (Corpus ID `79420`) showed that low-sodium groups had a **7 mm Hg reduction in systolic blood pressure** over one week, while added potassium chloride or nitrate supplementation did not provide additional blood-pressure benefit in that trial ([Sodium reduction is the key ingredient in dietary treatment of hypertension](metasyn://corpus/79420)).

This is a particularly clarifying result. It suggests that, at least in the short term, sodium reduction itself is the dominant causal driver of blood-pressure lowering, rather than potassium supplementation acting independently in the same timeframe. That finding helps separate mechanistic hypotheses and improves the internal coherence of the intervention evidence branch.

## 2. Observational Evidence

### Potassium intake and stroke mortality

A 12-year prospective cohort study (Corpus ID `69240`) found that each **10 mmol/day increase in dietary potassium intake** was associated with about a **40% lower risk of stroke-associated mortality**, independent of blood pressure and other cardiovascular risk factors ([Dietary potassium and stroke-associated mortality](metasyn://corpus/69240)).

Although this is older evidence and observational, it remains notable because the effect estimate is large and biologically plausible. However, because it concerns potassium intake rather than sodium reduction per se, it is better interpreted as complementary rather than dispositive. It supports the broader sodium-potassium balance framework, not a standalone conclusion that increasing potassium is always safe or equivalent to lowering sodium.

### Sodium intake and cardiovascular mortality: possible U-shape

A large national Chinese cohort (Corpus ID `77386`) reported a **U-shaped association** between estimated sodium intake and cardiovascular mortality: both low intake (<163.5 mmol/day) and high intake (>278.8 mmol/day) were linked to higher mortality compared with a middle range of 200.8–235.1 mmol/day ([National Chinese cohort on sodium and cardiovascular mortality](metasyn://corpus/77386)).

This is one of the most important counterweights to a simplistic “lower is always better” narrative. The same source suggested that higher mortality at low sodium may be mediated more by heart rate and blood glucose, whereas higher mortality at high sodium was partly mediated by systolic blood pressure and body mass index ([National Chinese cohort on sodium and cardiovascular mortality](metasyn://corpus/77386)).

My interpretation is that this U-shaped finding is hypothesis-generating rather than practice-changing. Observational sodium studies are especially vulnerable to reverse causation, measurement error, illness-related dietary changes, and residual confounding. Therefore, I do **not** consider this cohort strong enough to overturn randomized evidence that sodium reduction lowers blood pressure. It does, however, warn against overgeneralizing extreme sodium restriction without context.

### Sodium-related physiology and incident hypertension

A large 5-year Japanese cohort (Corpus ID `6783`) found that hyperosmolarity and higher serum sodium were independent predictors of incident hypertension in normotensive adults ([Japanese cohort on serum sodium and incident hypertension](metasyn://corpus/6783)). This supports the idea that sodium-related physiology matters beyond self-reported diet alone, though it is indirect evidence rather than a direct salt-intake exposure study.

### CKD and urinary sodium-to-potassium ratio

A 2025 CKD cohort study (Corpus ID `91514`) found that a higher 24-hour urinary sodium-to-potassium ratio was associated with elevated risk of overall heart failure (HR 1.44), heart failure with reduced ejection fraction (HR 1.90), and atrial fibrillation (HR 1.48), but not myocardial infarction ([Urinary sodium and potassium excretion and the risk of cardiovascular events in CKD](metasyn://corpus/91514)).

This is clinically important because it suggests that in CKD, the sodium-to-potassium ratio may be more informative than sodium alone. Still, it remains observational and should not be read as proof that potassium enrichment is safe in CKD.

## 3. Kidney Safety and Mechanistic Considerations

The DASH-Sodium trial analysis (Corpus ID `91520`) found that lower sodium intake reduced eGFR over 4 weeks, and the reduction was larger when low sodium was combined with the DASH diet ([Effects of Reduced Dietary Sodium and the DASH Diet on GFR](metasyn://corpus/91520)). This short-term eGFR decline may reflect renal hemodynamic change rather than kidney injury, but it complicates naive interpretations of “renal benefit” from sodium restriction.

In my view, this trial does **not** negate sodium reduction; rather, it underscores the need to distinguish short-term functional eGFR changes from long-term renal outcomes.

## Evidence Triangulation Assessment

### Convergence across branches

The evidence branches converge strongly on one point: **lower sodium intake reduces blood pressure**. This is supported by:
- Salt-substitute RCT evidence,
- Diabetes-focused sodium-reduction RCT evidence,
- A short-term mechanistic hypertension RCT,
- Observational evidence linking sodium exposure to blood pressure and hypertension risk.

### Where triangulation fails

The triangulation is incomplete for major cardiovascular outcomes because the MR branch is effectively absent in the retrieved local corpus for the targeted question. The one MR-adjacent candidate based on “adding salt to food” and myocardial infarction is too indirect to serve as a robust anchor for this review’s causal question ([MR-related candidate on salt-adding behavior](metasyn://corpus/86637)).

Therefore, any claim that automated evidence triangulation successfully integrates RCTs, observational studies, and MR studies for this salt-intake case study would be overstated **on the basis of the retrieved corpus alone**.

## Limitations

- The review was restricted to the **local MetaSyn corpus** and could not supplement retrieval externally.
- Several relevant records were **abstract-only**, including Corpus IDs `79420`, `29105`, and `69240`; this limits detailed risk-of-bias assessment.
- The retrieved evidence was skewed toward intervention and observational designs, with **no directly eligible MR study** identified for the targeted hypertensive-population question.
- Some key supporting evidence came from systematic reviews rather than only primary studies, though this was useful for mapping the evidence landscape.
- Sodium exposure measurement in observational studies is often imprecise and vulnerable to confounding.
- The search output included studies published after the seed end date of 2022; these were useful for context, but conclusions about strict replication of a historical search frame should be interpreted cautiously.

## Conclusion

The local MetaSyn corpus provides strong and consistent evidence that reducing sodium intake lowers blood pressure, including in hypertensive and diabetic populations, and that low-sodium salt substitutes are a plausible scalable intervention with potential cardiovascular benefit. However, the safety evidence for potassium-enriched substitutes is incomplete in CKD and among people taking medications that reduce potassium excretion. Observational evidence suggests that higher potassium intake is associated with lower stroke mortality and that sodium-related cardiovascular risk may be non-linear, but these findings are not strong enough to overturn randomized evidence on blood-pressure reduction.

My concrete conclusion is this: **for the salt-intake case study, the corpus supports a causal claim for sodium reduction lowering blood pressure, but it does not support a complete triangulated causal claim for major cardiovascular outcomes across RCT, observational, and Mendelian randomization designs.** The missing MR branch is not a minor gap; it materially limits convergence assessment. An LLM system may perform well at extracting direction and significance where evidence exists, but for this case it should be judged just as much on recognizing **absence of evidence in one design branch** as on synthesizing positive findings in the others.

## Included-Study List

### Included primary studies
- `Sodium reduction is the key ingredient in dietary treatment of hypertension - a randomized controlled trial on sodium, potassium and nitrate.` Corpus ID `79420`
- `Dietary potassium and stroke-associated mortality. A 12-year prospective population study.` Corpus ID `69240`
- `Urinary Sodium and Potassium Excretion and the Risk of Cardiovascular Events in CKD.` Corpus ID `91514`
- `Effects of Reduced Dietary Sodium and the DASH Diet on GFR: The DASH-Sodium Trial.` Corpus ID `91520`

### Included synthesis/context studies
- `Replacing salt with low-sodium salt substitutes (LSSS) for cardiovascular health in adults, children and pregnant women.` Corpus ID `22682`
- `Altered dietary salt intake for preventing diabetic kidney disease and its progression.` Corpus ID `69247`

### Screened but not included as core evidence
- `Effect of low-sodium, potassium-rich salt based on the Chinese modified DASH diet on home blood pressure monitoring in patients with hypertension and type 2 diabetes: a clinical trial.` Corpus ID `29105` — abstract-only, preliminary, less informative than included intervention evidence
- MR-related salt-adding behavior and myocardial infarction candidate. Corpus ID `86637` — not specific to hypertensive populations and did not isolate total sodium intake as primary exposure

## References

- Cochrane review on low-sodium salt substitutes. [metasyn://corpus/22682](metasyn://corpus/22682)
- Sodium reduction RCT in hypertension. [metasyn://corpus/79420](metasyn://corpus/79420)
- Cochrane review in diabetes. [metasyn://corpus/69247](metasyn://corpus/69247)
- DASH-Sodium kidney analysis. [metasyn://corpus/91520](metasyn://corpus/91520)
- Chinese modified DASH low-sodium salt trial. [metasyn://corpus/29105](metasyn://corpus/29105)
- Potassium and stroke mortality cohort. [metasyn://corpus/69240](metasyn://corpus/69240)
- CKD sodium-to-potassium cardiovascular cohort. [metasyn://corpus/91514](metasyn://corpus/91514)
- Chinese sodium and cardiovascular mortality cohort. [metasyn://corpus/77386](metasyn://corpus/77386)
- Japanese serum sodium and incident hypertension cohort. [metasyn://corpus/6783](metasyn://corpus/6783)
- Global sodium-to-potassium intake systematic review. [metasyn://corpus/14902](metasyn://corpus/14902)
- MR-related candidate on salt-adding behavior and myocardial infarction. [metasyn://corpus/86637](metasyn://corpus/86637)
- MetaSyn local corpus search result. [mcp://search_metasyn_corpus/0](mcp://search_metasyn_corpus/0)