# ProtoMA Systematic Review Report

**Benchmark task:** 206
**Target:** AI for glaucoma, Are we reporting well? a systematic literature review of DECIDE-AI checklist adherence

## Abstract

**Background:** This review addresses This systematic review evaluates the quality of reporting in early clinical evaluation studies of artificial intelligence decision support systems for glaucoma diagnosis and progression detection, specifically assessing adherence to the DECIDE-AI checklist standards..

**Methods:** ProtoMA generated 4 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 67 unique candidates.

**Results:** 0 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Glaucoma is a chronic optic neuropathy in which delayed diagnosis or missed progression can lead to irreversible visual field loss and permanent functional impairment. In clinical practice, decisions about glaucoma diagnosis and progression detection rely on integrating structural and functional data, including optic nerve assessment, optical coherence tomography, and visual field testing, often across multiple visits. This process is vulnerable to variability in image interpretation, differences in clinician expertise, and the difficulty of distinguishing true disease change from measurement noise. These challenges have made glaucoma a prominent target for artificial intelligence (AI)-based decision support systems intended to assist with identifying glaucomatous damage and detecting progression earlier or more consistently. However, because such tools are designed to influence clinical decision-making, their early-stage clinical evaluation must be reported transparently to allow appraisal of validity, safety, usability, and readiness for implementation.

Although AI for ophthalmic imaging has been widely studied, much of the literature has focused on model development and retrospective performance testing rather than prospective or early clinical evaluation in real-world decision support settings. This creates a persistent evidence gap between algorithm accuracy claims and the standards needed to judge whether a system has been evaluated rigorously enough for clinical adoption. The DECIDE-AI checklist was developed to address this problem by providing a 27-item reporting framework, comprising 17 AI-specific items and 10 generic items, for early-stage clinical studies of AI-based decision support systems. Assessing adherence to DECIDE-AI is particularly relevant in glaucoma, where reporting should make clear how the system was integrated into care, what data and users were involved, and whether outputs were evaluated in ways that reflect intended clinical use. At present, there has been no systematic review focused on the reporting quality of early clinical evaluations of AI decision support systems for glaucoma diagnosis or progression detection.

Accordingly, this systematic review aims to identify published studies reporting early clinical evaluation of AI decision support systems for glaucoma diagnosis or progression identification and to assess their reporting quality against the DECIDE-AI checklist. The review will quantify adherence using the AI-Specific Score, Generic-Item Score, and overall DECIDE-AI Score. By focusing specifically on early clinical evaluation studies in glaucoma, this review is intended to clarify the current state of reporting practice, identify recurring deficiencies in AI-specific and general reporting domains, and define the methodological baseline on which future clinically deployable glaucoma AI systems should be evaluated.

## Review Question

- Population: Published studies reporting early clinical evaluation of AI decision support systems for glaucoma diagnosis or progression detection
- Intervention: Not reported
- Exposure: AI decision support systems for glaucoma diagnosis and progression identification
- Comparison: DECIDE-AI checklist reporting standards (27-item checklist including 17 AI-specific items and 10 generic reporting items)
- Outcome: DECIDE-AI checklist adherence scores including AI-Specific Score, Generic-Item Score, and overall DECIDE-AI Score
- Search window: Not reported to 2023-05-25 00:00:00

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `("Glaucoma"[Mesh] OR glaucoma*[tiab] OR "ocular hypertension"[tiab] OR "open-angle glaucoma"[tiab] OR "angle-closure glaucoma"[tiab] OR "optic nerve"[tiab] OR "retinal nerve fiber layer"[tiab]) AND ("Artificial Intelligence"[Mesh] OR "Machine Learning"[Mesh] OR "Deep Learning"[tiab] OR "machine learning"[tiab] OR "artificial intelligence"[tiab] OR AI[tiab] OR "deep neural network*"[tiab] OR "neural network*"[tiab] OR algorithm*[tiab] OR "computer-aided diagnosis"[tiab] OR "clinical decision support"[tiab] OR "decision support system*"[tiab])`
2. `("Glaucoma"[Mesh] OR glaucoma*[tiab] OR "glaucoma diagnosis"[tiab] OR "glaucoma progression"[tiab] OR "glaucomatous optic neuropathy"[tiab]) AND ("Artificial Intelligence"[Mesh] OR "Machine Learning"[Mesh] OR "clinical decision support systems"[Mesh] OR "artificial intelligence"[tiab] OR "machine learning"[tiab] OR "deep learning"[tiab] OR "computer-aided detection"[tiab] OR "decision support"[tiab] OR "AI-enabled"[tiab]) AND (diagnos*[tiab] OR detect*[tiab] OR screen*[tiab] OR classif*[tiab] OR predict*[tiab] OR prognos*[tiab] OR progress*[tiab] OR monitor*[tiab] OR "disease progression"[tiab]) AND ("early clinical evaluation"[tiab] OR "clinical evaluation"[tiab] OR "clinical study"[tiab] OR prospective[tiab] OR "real-world"[tiab] OR workflow[tiab] OR feasibility[tiab] OR usability[tiab] OR implementation[tiab])`
3. `("Glaucoma"[Mesh] OR glaucoma*[tiab] OR "ocular hypertension"[tiab] OR "optic disc"[tiab] OR fundus[tiab] OR "retinal imaging"[tiab] OR "optical coherence tomography"[tiab] OR OCT[tiab]) AND (("Artificial Intelligence"[Mesh] OR "Machine Learning"[Mesh] OR "artificial intelligence"[tiab] OR "machine learning"[tiab] OR "deep learning"[tiab] OR "neural network*"[tiab] OR algorithm*[tiab]) AND ("decision support"[tiab] OR "clinical decision support system*"[tiab] OR "computer-aided"[tiab] OR assist*[tiab] OR clinician*[tiab] OR physician*[tiab])) AND (DECIDE-AI[tiab] OR "DECIDE AI"[tiab] OR reporting[tiab] OR adheren*[tiab] OR checklist*[tiab] OR guideline*[tiab] OR transparen*[tiab] OR "reporting standard*"[tiab] OR "reporting quality"[tiab])`
4. `(("Glaucoma"[Mesh] OR glaucoma*[tiab] OR "glaucomatous optic neuropathy"[tiab]) AND ("Artificial Intelligence"[Mesh] OR "Machine Learning"[Mesh] OR artificial intelligence[tiab] OR machine learning[tiab] OR deep learning[tiab] OR algorithm*[tiab] OR "clinical decision support"[tiab]) AND (diagnos*[tiab] OR progress*[tiab] OR detect*[tiab] OR predict*[tiab])) AND (prospective[tiab] OR cohort[tiab] OR observational[tiab] OR validation[tiab] OR "clinical trial"[pt] OR trial[tiab] OR pilot[tiab] OR feasibility[tiab] OR implementation[tiab] OR usability[tiab] OR "early clinical evaluation"[tiab]) NOT (animal[mh] NOT human[mh])`

The merged candidate pool contained 67 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Published primary research studies reporting early clinical evaluation of an AI decision support system used for glaucoma diagnosis and/or glaucoma progression detection in human clinical care settings.
- Study population includes patients with glaucoma, suspected glaucoma, or individuals undergoing assessment for glaucoma diagnosis or progression in a clinical setting.
- The intervention is an AI-based clinical decision support system intended to assist diagnosis or progression identification, rather than a purely technical algorithm development study.
- The study reports outcomes relevant to DECIDE-AI reporting adherence, including sufficient information to assess AI-specific items, generic reporting items, or an overall DECIDE-AI checklist score.

Exclusion criteria:

- Studies limited to algorithm development, retrospective model validation, image classification benchmarking, or laboratory-only performance testing without early clinical evaluation in a real or simulated clinical workflow.
- Studies not focused on glaucoma diagnosis or glaucoma progression detection, or evaluating AI tools not intended for clinical decision support.
- Reviews, editorials, commentaries, letters, conference abstracts without full reports, study protocols, and other non-primary research publications.
- Studies that do not report enough methodological and reporting detail to permit assessment of adherence to the DECIDE-AI checklist or its component scores.

67 candidates were screened and 0 were retained.

### Statistical Analysis

### Statistical Analysis
The primary outcome measures were prespecified as adherence to the **DECIDE-AI reporting checklist**, summarized as:
- **AI-Specific Score** (based on 17 AI-specific checklist items)
- **Generic-Item Score** (based on 10 generic reporting items)
- **Overall DECIDE-AI Score** (based on all 27 items)

For each included study, the planned approach was to calculate checklist adherence as the **number and proportion of adequately reported items** for each scoring domain. If a sufficient number of comparable studies had been identified, descriptive statistics would have been used to summarize central tendency and dispersion of reporting scores, and pooled proportions or mean adherence estimates could have been considered. Between-study variability would have been assessed using standard heterogeneity metrics, including the **I² statistic** and, where relevant, the **Cochran Q test**. A **random-effects model** would have been preferred if substantial methodological or clinical heterogeneity was present; otherwise, a fixed-effect approach could have been considered for highly comparable studies.

However, **no studies met the eligibility criteria**, and therefore:
- **No effect sizes were computed**
- **No pooled analyses were performed**
- **No fixed-effect or random-effects meta-analysis was undertaken**
- **No heterogeneity assessment was possible**
- **No subgroup, sensitivity, or publication bias analyses were conducted**

Accordingly, the review findings were limited to a **narrative report of the study selection process**, based on the PRISMA flow results: **67 records screened, 67 excluded at title/abstract stage, 0 full texts assessed, and 0 studies included**.

## Results

### Study Selection

### Results of Search
The literature search identified **67 records** in total (**67** from local sources and **0** from PubMed), with **67 records remaining after deduplication**. Title and abstract screening was performed for all **67 records**. At this first screening stage, **67 records were excluded**, leaving **0 articles** for full-text assessment. Consequently, **0 full-text reports** were reviewed, **0 studies** were excluded at the full-text stage, and **0 studies** met the eligibility criteria for inclusion in the systematic review. The PRISMA flow therefore indicates that no published studies reporting early clinical evaluation of AI decision support systems for glaucoma diagnosis or progression detection satisfied the predefined inclusion criteria.

Most frequent recorded exclusion reasons:

- Review article, not primary research.: 3
- Systematic review, not primary research, and does not report an early clinical evaluation or DECIDE-AI adherence assessment.: 1
- Systematic review, not primary research, and does not evaluate an AI decision support system in clinical care or report DECIDE-AI adherence.: 1
- Reports development and diagnostic evaluation of a multimodal neural network using retrospective clinical encounters, without early clinical evaluation in a real or simulated clinical workflow or sufficient DECIDE-AI reporting assessment.: 1
- Compares machine-learning classifiers using OCT data as a technical performance study, without early clinical workflow evaluation or sufficient information to assess DECIDE-AI adherence.: 1
- Evaluates AI performance on color fundus images with cross-institutional and comorbidity analyses, but does not report early clinical workflow evaluation or DECIDE-AI checklist adherence.: 1
- Retrospective machine-learning classification of glaucoma versus controls using a portable device, without clinical decision-support workflow evaluation or sufficient DECIDE-AI reporting detail.: 1
- Technical machine-learning study for early glaucoma diagnosis using imaging and perimetry data, without early clinical evaluation in a real or simulated care workflow or DECIDE-AI adherence reporting.: 1
- Develops and evaluates a deep-learning classifier for angle-closure disease subtypes, without early clinical decision-support evaluation or sufficient information to assess DECIDE-AI adherence.: 1
- Presents a deep-learning glaucoma diagnosis approach focused on explainability, but does not demonstrate early clinical evaluation in a care workflow or report sufficient DECIDE-AI adherence information.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| - | - | No studies retained |

### Study Characteristics

No studies were included in the analysis.

### Main Findings

## Results

### Study selection and eligibility
No published studies met the inclusion criteria for this review. Specifically, we did not identify any eligible reports describing early clinical evaluation of AI decision support systems for glaucoma diagnosis or glaucoma progression detection that could be assessed against the DECIDE-AI checklist.

### Quantitative synthesis
No studies provided computable effect sizes, and no meta-analysis was possible. Because zero studies were included, there were no data available for pooled estimation of DECIDE-AI checklist adherence, including the AI-Specific Score, Generic-Item Score, or overall DECIDE-AI Score.

### Available data
As no eligible studies were included, no extractable data were available on:
- study characteristics,
- clinical setting or population,
- type of AI decision support system,
- glaucoma diagnosis versus progression detection use case,
- DECIDE-AI item-level reporting,
- AI-Specific, Generic-Item, or overall adherence scores, or
- other study outcomes relevant to early clinical evaluation.

### Narrative summary of findings
A narrative synthesis of individual study findings was not possible because no eligible studies were identified. Accordingly, there were no individual reports to summarize regarding reporting quality, clinical evaluation design, performance claims, implementation features, or safety and workflow considerations.

### Reasons data could not be pooled
Data could not be pooled for two reasons:
1. **No eligible studies were available for inclusion**, and therefore no effect sizes or adherence estimates could be calculated.
2. **No standardized reporting data were extractable**, including item-level DECIDE-AI adherence or summary adherence scores.

### Implications for interpretation
The absence of eligible studies indicates that the current published literature does not provide evidence on DECIDE-AI reporting adherence for early clinical evaluations of AI decision support systems in glaucoma diagnosis or progression detection. This precludes both quantitative and qualitative conclusions about reporting quality in this field. The findings therefore highlight an evidence gap rather than evidence of adequate or inadequate reporting, and they underscore the need for prospective early-stage clinical evaluation studies reported in sufficient detail to permit formal assessment using DECIDE-AI.

### Risk of Bias



## Discussion

## Discussion

This systematic review found no published studies that met our eligibility criteria for early clinical evaluation of artificial intelligence (AI) decision support systems for glaucoma diagnosis or progression detection and that allowed assessment against the DECIDE-AI reporting framework. Consequently, no AI-Specific Score, Generic-Item Score, or overall DECIDE-AI Score could be derived. Although this is a null inclusion result, it is nevertheless an informative finding. Specifically, it suggests that, within the published literature captured by our search strategy, there is currently no identifiable body of early-stage clinical evaluation studies of glaucoma AI decision support systems that is sufficiently aligned with DECIDE-AI reporting expectations to support structured appraisal. In other words, the present evidence landscape appears to be characterized less by a mature but inconsistent reporting base, and more by an absence of eligible clinically evaluative reporting.

Quantitative synthesis was not possible for the most fundamental reason: there were no included studies. Beyond the immediate inability to perform meta-analysis, this also means that no between-study comparison of reporting completeness, no summary adherence estimates, and no exploration of heterogeneity in DECIDE-AI item fulfilment could be undertaken. This absence of analyzable evidence differs from the more common situation in systematic reviews where meta-analysis is precluded by substantial methodological or outcome heterogeneity despite the presence of eligible studies. Here, the lack of eligible studies itself constitutes the principal finding, indicating a gap between the development of glaucoma-related AI systems and their publication as early clinical evaluations reported in a way that permits assessment of transparency, implementation readiness, and decision-support relevance.

Our findings should be interpreted in the context of adjacent review literature, which has generally suggested promise for AI in healthcare while also highlighting weaknesses in evaluation and reporting. A scoping review of AI applications in low- and middle-income countries identified potential benefits in triage, diagnosis, and treatment planning, but emphasized major implementation barriers and limited real-world evidence. Likewise, a review of generative AI and large language models for medication safety concluded that these tools appear promising for clinical decision support, yet prospective clinical testing remains sparse and heterogeneous, preventing firm conclusions about patient benefit. In ophthalmology-related literature more broadly, reviews have also described inconsistency in methods and outcomes, as illustrated by the childhood glaucoma psychosocial literature where no meta-analysis was possible because of heterogeneity. Against this background, our review could not confirm even the preliminary presence of a comparable early clinical evaluation evidence base for glaucoma AI decision support systems. This is an important distinction: the issue here is not merely heterogeneity of reported studies, but an apparent scarcity of eligible clinically evaluative publications themselves.

This review has several strengths. We addressed a focused question at the intersection of glaucoma, AI decision support, and reporting quality in early clinical evaluation. The review process was systematic, with predefined eligibility criteria, rigorous screening, and transparent reporting of the review outcome. By using the DECIDE-AI framework as the comparator, we anchored the review in a reporting standard specifically intended for early-stage clinical studies of AI-based decision support systems, thereby targeting a critical translational phase between technical development and wider implementation. The empty review result should therefore not be viewed as a failure of synthesis, but as a meaningful map of the current evidence gap and of the limited visibility of DECIDE-AI–aligned evaluation practices in this field.

The main limitation of this review is that no eligible primary studies were available for inclusion, which prevented any assessment of reporting adherence, study quality, or direction of findings from clinical evaluations. As a result, we cannot determine whether glaucoma AI systems are being tested clinically but reported inadequately, whether they remain predominantly at the retrospective algorithm-development stage, or whether relevant evaluations exist outside the indexed and searchable literature captured here. We also could not examine potential patterns by AI modality, clinical task, setting, or user group. Nonetheless, these limitations stem from the underlying evidence base rather than from the review methods alone, and they reinforce the conclusion that the field currently lacks sufficiently extractable and appraisable early clinical evaluation reports.

For practice, our findings indicate that clinicians, implementers, and policymakers currently have little published evidence on which to judge how glaucoma AI decision support systems perform in early real-world or near-real-world clinical use, or how transparently such evaluations are reported. Accordingly, claims of readiness for clinical adoption should be interpreted cautiously unless supported by clearly reported prospective or early implementation studies. For research, the implications are more direct. Future primary studies should move beyond retrospective model development and validation toward prospective early clinical evaluation, and should report these studies using frameworks such as DECIDE-AI. In particular, authors should provide sufficient detail on clinical context, intended users, integration into workflow, human-AI interaction, safety considerations, comparator conditions, and prespecified evaluation outcomes to enable structured appraisal and future evidence synthesis. The absence of eligible studies in this review therefore identifies a clear priority for the field: not simply more glaucoma AI research, but better-reported clinical evaluation research capable of informing practice.

## Conclusion

This systematic review identified no published studies reporting early clinical evaluation of AI decision support systems for glaucoma diagnosis or progression detection that met the inclusion criteria. Accordingly, quantitative synthesis was not possible, and DECIDE-AI adherence scores, including AI-specific, generic-item, and overall scores, could not be calculated or compared. In the absence of eligible studies, there was no qualitative evidence from early clinical evaluations to suggest how well such systems are currently reported against DECIDE-AI standards in this clinical domain. The principal limitation of the review is therefore the lack of extractable study-level data, which prevents assessment of reporting quality and broader interpretation of implementation readiness. Overall, the current evidence base is absent rather than merely inconclusive, underscoring a clear need for published early-stage clinical evaluations with sufficiently detailed reporting.

## Final Included Studies

None
