# Systematic Review Report: Salt Intake, Blood Pressure, Cardiovascular Outcomes, and the Feasibility of Evidence Triangulation from the Local MetaSyn PubMed Corpus

## Review Question

This review examined whether the local MetaSyn PubMed corpus contains primary-study evidence that could support an automated evidence-triangulation workflow across three study designs:

- observational studies
- Mendelian randomization studies
- randomized controlled trials

The case study was the relationship between salt intake and:

- blood pressure
- incident hypertension
- cardiovascular disease
- cardiovascular death

A secondary aim was to assess whether the locally retrievable primary-study literature could support triangulation-relevant extraction of:

- direction of effect
- statistical significance
- convergency-style patterns across study designs

The review was restricted to the local MetaSyn PubMed corpus as the only retrieval source, with fixed search dates from **1971-01-01 to 2022-12-31**.

## Review Scope and Eligibility Criteria

### Population

- General population across observational, intervention, and genetic-instrumented study designs
- Additional focused attention to **hypertensive populations** for salt-reduction intervention evidence

### Exposure or Intervention

- Salt intake
- Dietary sodium
- Salt reduction
- Sodium-related intervention or exposure contrasts

### Comparators

- Higher versus lower salt exposure
- Salt reduction versus comparator conditions
- Cross-design comparison among observational, Mendelian randomization, and randomized trial evidence

### Outcomes

- Blood pressure
- Hypertension incidence
- Cardiovascular disease
- Cardiovascular mortality/death

Where available in locally retrievable records, the review also considered evidence-triangulation-relevant result characteristics such as:

- direction of association/effect
- presence of statistical significance
- whether findings could be compared across study designs

### Inclusion Criteria

Studies were eligible if they were primary studies and met at least one of the following design conditions:

1. **Observational studies** relevant to salt/sodium and blood pressure or cardiovascular outcomes.
2. **Randomized or intervention studies** where salt reduction or sodium modification was meaningfully linked to blood pressure or cardiovascular outcomes.
3. **Mendelian randomization studies**, but only if the **exact phrase “Mendelian randomization”** appeared in the title and/or abstract.

### Exclusion Criteria

The following were excluded or critically flagged:

- reviews, guidelines, and non-primary summaries
- records outside the date window
- records not primarily focused on salt/sodium exposure or intervention
- records not reporting blood pressure, hypertension, or cardiovascular outcomes
- Mendelian randomization candidates lacking the exact phrase **“Mendelian randomization”**
- extracted relations where significance was marked **“not found”**
- evidence whose causal interpretation appeared materially weakened by inadequate control of confounding
- records with insufficient retrievable result detail for triangulation-ready extraction

If only abstract text was locally available, the evidence was labeled **abstract-only**.

## Local Corpus Search Strategy

## Exact Queries Used

The following exact local MetaSyn corpus search queries were used:

1. `("salt intake" OR "dietary sodium" OR "salt reduction" OR sodium OR salt) AND ("blood pressure" OR hypertension) AND (1971/01/01:2022/12/31[dp])`

2. `("salt reduction" OR "dietary sodium" OR sodium OR salt) AND (hypertension OR hypertensive) AND (randomized OR randomised OR trial OR intervention) AND (1971/01/01:2022/12/31[dp])`

3. `("salt intake" OR "dietary sodium" OR "salt reduction" OR sodium OR salt) AND ("cardiovascular disease" OR stroke OR "coronary heart disease" OR mortality OR death) AND (1971/01/01:2022/12/31[dp])`

4. `"Mendelian randomization" AND (salt OR sodium) AND ("blood pressure" OR hypertension OR cardiovascular OR stroke) AND (1971/01/01:2022/12/31[dp])`

5. `(hypertensive OR hypertension) AND ("salt reduction" OR sodium) AND (subgroup OR patients) AND (trial OR intervention) AND (1971/01/01:2022/12/31[dp])`

6. `((sodium OR salt OR "urinary sodium") AND (cohort OR prospective OR longitudinal OR follow-up)) AND (("blood pressure" OR hypertension) OR (cardiovascular OR stroke OR mortality OR death)) AND (1971/01/01:2022/12/31[dp])`

## Retrieval Yield

- **6 searches** were run.
- Each local search returned **20 candidates**.
- Total records returned before deduplication: **120**.
- The practical screening set was substantially smaller after deduplication because many records recurred across multiple searches.

An exact post-deduplication count was not preserved in the available research log, so the final report can only state the pre-deduplication yield with certainty.

## Screening and Study Selection Procedure

### Stage 1: Title/Abstract Screening

Records were first screened for obvious ineligibility. Exclusions at this stage included:

- review articles
- guideline papers
- non-primary summaries
- records unrelated to salt/sodium exposure
- records unrelated to blood pressure, hypertension, or cardiovascular outcomes
- records outside the date window

### Stage 2: Design-Specific Screening

#### Observational Studies
Included if they were primary studies on salt/sodium exposure and blood pressure or cardiovascular outcomes.

#### Randomized/Intervention Studies
Included if they tested a salt-reduction or sodium-modification intervention and reported blood pressure or cardiovascular outcomes.

#### Mendelian Randomization Studies
Included only if title and/or abstract contained the exact phrase:

- **“Mendelian randomization”**

This was a strict rule and excluded genetically oriented studies that did not use that exact wording.

### Stage 3: Result-Level Review

Where sectioned record content was available in the local corpus, methods/results/discussion were examined. The research log shows record-level fetches for:

- **Corpus ID 6783**: methods, results, discussion
- **Corpus ID 69367**: all sections
- **Corpus ID 8334**: all sections

### Stage 4: Causal-Interpretation Appraisal

Observational evidence was critically flagged when causal interpretation depended on confounding control that was absent, limited, or potentially compromised by exposure measurement limitations.

## Included Studies and Design Coverage

## High-Level Inclusion Summary

The screening log identified:

- **2 included primary studies**
  - **1 observational**
  - **1 randomized/intervention**
  - **0 Mendelian randomization**

However, only **one included study** was preserved in the available findings with complete title-level detail and exact Corpus ID. The second included intervention study was mentioned in the screening summary but its full bibliographic identity was not preserved in the supplied findings excerpt. Because the brief requires a transparent and reproducible final included-study list, the report distinguishes between:

- **screening-log inclusion count**
- **reproducibly documented included studies**

### Reproducibly documented included studies
- **1**

### Additional included study indicated in screening log but not bibliographically recoverable from the supplied findings
- **1**

## Mendelian Randomization Findings

No eligible Mendelian randomization study was identified in the returned local corpus set under the required rule that the title and/or abstract contain the exact phrase **“Mendelian randomization.”**

This is an important negative finding. It means that, within the local corpus retrieval actually conducted and under the pre-specified rule, the triangulation exercise could not be completed across all three target designs. The design coverage achieved was therefore only partial:

- observational: yes
- randomized/intervention: yes, but incompletely documented in the supplied log
- Mendelian randomization: no eligible included study found

## Results of the Reproducibly Documented Observational Study

## Included Study 1

**Title:** *Hyperosmolarity and Increased Serum Sodium Concentration Are Risks for Developing Hypertension Regardless of Salt Intake: A Five-Year Cohort Study in Japan*  
**Corpus ID:** **6783** [1]

### Study Design

- Observational cohort study
- Five-year longitudinal follow-up
- Not abstract-only; locally retrievable methods, results, and discussion were available [1]

### Population

- **10,157 normotensive adults without diabetes**
- Age range: **30–85 years**
- Setting: annual health check-ups in Tokyo, Japan [1]

### Exposure

- Salt intake estimated from a self-answered questionnaire based on a single 24-hour dietary recall [1]
- High salt intake defined as **>12 g/day** [1]
- Serum sodium and serum osmolarity were also examined [1]

### Outcome

- Incident hypertension over 5 years [1]

### Main Findings

This study found that individuals who later developed hypertension had:

- higher salt intake
- higher serum sodium
- higher serum osmolarity
- worse cardiometabolic risk profiles overall [1]

Key reported result statements included:

- cumulative 5-year incidence of hypertension: **10.2%** overall [1]
- high salt intake group versus normal salt intake group:
  - **10.9% vs 9.7%**
  - **p = 0.046** [1]
- hyperosmolarity group versus normal osmolarity group:
  - **13.0% vs 7.5%**
  - **p < 0.001** [1]
- in adjusted models, higher serum osmolarity remained an independent risk factor:
  - **OR 1.025**
  - **95% CI 1.006–1.044**
  - **p = 0.010** [1]
- higher serum sodium also remained independently associated with hypertension:
  - **OR 1.045**
  - **95% CI 1.005–1.087**
  - **p = 0.028** [1]

### Direction of Effect

- **Higher salt-related exposure markers were associated with higher hypertension risk** [1]

### Statistical Significance

- Yes, statistical significance was explicitly reported for key comparisons and adjusted estimates [1]
- This means the study contributes triangulation-ready information under the rule excluding “significance not found” relations

### Causal Interpretation and Confounding Concerns

This study is useful but should be interpreted cautiously for causal synthesis:

- Salt intake measurement relied on a **single self-reported 24-hour recall**, which is a weak measure of habitual intake.
- The association for high salt intake versus normal intake was **statistically significant but modest**.
- The study adjusted for several confounders, including:
  - age
  - sex
  - body mass index
  - smoking
  - alcohol use
  - dyslipidemia
  - hyperuricemia
  - chronic kidney disease
  - serum osmolarity [1]

Even with multivariable adjustment, residual confounding and measurement error remain important limitations. The record therefore supports an adverse salt–blood pressure direction of effect, but not strong causal certainty on its own.

## Randomized/Intervention Evidence

The screening log reports **one included randomized/intervention study**, indicating that locally retrievable evidence for salt-reduction intervention in a relevant population was found. However, the supplied findings did **not preserve the title and exact inclusion details** of that intervention study in a form sufficient for reproducible final reporting.

The available log indicates that full-record retrieval was attempted for:

- **Corpus ID 8334**
- **Corpus ID 69367**

But the supplied research findings do not specify which of these, if either, was the included randomized study, nor do they provide title-level confirmation. Because the brief requires exact Corpus ID preservation and a final included-study list with titles, that study cannot be reliably listed as a confirmed final included record from the available evidence package.

### Implication

The broader screening process appears to have identified intervention evidence consistent with the review question, but the currently preserved local-record audit trail is insufficient to reproduce that inclusion at publication level. This limits the confidence of any design-comparative synthesis.

## Evidence Triangulation Across Study Designs

## What the Local Corpus Evidence Supports

### Observational Evidence
The reproducibly documented cohort study supports the expected direction:

- higher salt-related exposure is associated with higher hypertension risk [1]

### Randomized/Intervention Evidence
The screening log indicates relevant intervention evidence exists in the retrieved local corpus, likely in the direction expected from the salt-reduction literature, but the preserved record detail is insufficient to reproduce the exact effect statement in this report.

### Mendelian Randomization Evidence
No eligible local-corpus record meeting the exact-phrase criterion for **“Mendelian randomization”** was included.

## Overall Triangulation Feasibility

A full triangulation exercise requires at least one included study from each of the target design families. That condition was **not met**.

As a result:

- **full evidence triangulation across observational, Mendelian randomization, and randomized controlled trial designs was not feasible from the retrieved and documented local corpus set**
- only **partial triangulation** was possible
- any attempt to derive Convergency of Evidence (CoE) or Level of Convergency (LoC) would be incomplete and methodologically fragile

## Why Meta-Analysis Was Not Feasible

A formal quantitative meta-analysis was not feasible for several reasons:

1. **Too few reproducibly documented included studies**
   - Only one included study is fully documented in the available findings.

2. **Design heterogeneity**
   - Observational and intervention studies are not directly combinable without predefined harmonization rules.
   - No Mendelian randomization study was included.

3. **Outcome heterogeneity**
   - The observational study focused on incident hypertension rather than a pooled continuous blood pressure estimate or shared cardiovascular endpoint.

4. **Exposure heterogeneity**
   - Salt intake was measured differently across designs and was not harmonized in the local findings.

5. **Incomplete result preservation**
   - The intervention study was not bibliographically recoverable from the supplied evidence log.
   - No reproducible set of effect sizes across multiple studies was available.

Accordingly, the appropriate synthesis is narrative rather than meta-analytic.

## Findings Relevant to the Overall Research Question

## Can large language models automate extraction and synthesis for this case study?

Based on the local corpus evidence actually retrieved and screened, the answer is **only partially**.

### What appears feasible
An automated or semi-automated system could likely extract from included primary studies:

- direction of effect
- presence of statistical significance
- basic study design
- key population and exposure descriptors

The observational study documented here is a good example: the result direction, significance, and adjusted estimates are clearly retrievable [1].

### What remains difficult from the local corpus alone
The local corpus, at least as documented in this research log, does not by itself support a complete triangulation workflow because:

- no eligible Mendelian randomization study was included under the exact-phrase rule
- the intervention evidence was not fully preserved in reproducible title-level form
- some records may be abstract-only
- confounding and exposure-measurement quality are not always easy to adjudicate from local record text alone
- full CoE and LoC metrics could not be reproduced

In practical terms, LLM-based extraction may work reasonably well for **within-study result capture**, but **cross-design causal triangulation** depends heavily on the completeness and structure of the underlying local corpus records.

## Limitations

## Retrieval and Corpus Limitations

- Only the **local MetaSyn PubMed corpus** was used.
- No external databases, web search, or full-text repositories were used.
- The search output was capped at **20 candidates per query**, which may have limited recall.
- Exact post-deduplication counts were not preserved in the available log.

## Study Documentation Limitations

- The screening summary reported **2 included studies**, but only **1** was fully documented with title and exact Corpus ID in the supplied findings.
- This creates a reproducibility gap between the screening count and the final reportable included-study list.

## Design-Coverage Limitations

- No eligible Mendelian randomization study was found under the exact-phrase criterion.
- Therefore, the intended three-way triangulation across observational, MR, and RCT evidence could not be completed.

## Reporting Limitations

- Not all locally retrieved records had full section-level detail preserved in the findings.
- Some evidence may have been abstract-only, although the documented included cohort study was **not** abstract-only [1].
- The intervention study’s abstract-only/full-text status could not be definitively reported from the supplied findings.

## Causal Interpretation Limitations

- Observational evidence remains vulnerable to:
  - residual confounding
  - exposure misclassification
  - selection bias
- The included cohort study used a self-reported single 24-hour dietary recall for salt intake, which weakens causal precision [1].

## Inability to Reproduce Full Triangulation Metrics

The requested LLM-oriented triangulation metrics—such as Convergency of Evidence and Level of Convergency—could not be fully reproduced from the local corpus evidence package because:

- design coverage was incomplete
- too few included studies were reproducibly documented
- result extraction fields were not consistently available in a structured form
- no complete triangulation-ready dataset was recoverable from the local corpus records alone

## Conclusion

The local MetaSyn PubMed corpus search and screening process identified **limited but relevant primary-study evidence** on the relationship between salt exposure and blood pressure-related outcomes. The clearest reproducibly documented included study was a five-year observational cohort from Japan showing that higher salt-related exposure markers, especially serum sodium and osmolarity, were associated with a higher risk of developing hypertension, with statistically significant findings after multivariable adjustment [1].

However, the overall evidence package was **not sufficient to support a full systematic triangulation across observational studies, Mendelian randomization studies, and randomized controlled trials**. The main reasons were:

- no eligible Mendelian randomization study found under the required exact-phrase rule
- only one included study fully reproducible from the supplied research log
- intervention evidence indicated in screening but not preserved in sufficient bibliographic detail
- substantial heterogeneity and incomplete local reporting

The local corpus therefore supports a **partial conclusion**:

- the retrievable evidence is **consistent with an adverse salt–blood pressure relationship**
- but the corpus evidence documented here is **insufficient for robust cross-design causal triangulation or quantitative meta-analysis**

## Final Included-Study List

### Reproducibly included primary studies

1. **Hyperosmolarity and Increased Serum Sodium Concentration Are Risks for Developing Hypertension Regardless of Salt Intake: A Five-Year Cohort Study in Japan** — **Corpus ID: 6783** [1]

### Studies indicated as included in the screening summary but not reproducibly recoverable from the supplied findings

- One additional randomized/intervention primary study was reported as included in the screening log, but its **title and exact inclusion identity were not preserved in the supplied findings excerpt**. To avoid introducing unsupported bibliographic information, it is **not listed as a confirmed final included study**.

### Mendelian randomization included studies

- **None**

### Sources

[1] Hyperosmolarity and Increased Serum Sodium Concentration Are Risks for Developing Hypertension Regardless of Salt Intake: A Five-Year Cohort Study in Japan: metasyn://corpus/6783