# ProtoMA Systematic Review Report

**Benchmark task:** 46
**Target:** Mental health of children with gender and sexual minority parents: a review and future directions

## Abstract

**Background:** This review addresses This systematic review examines whether children with gender and sexual minority parents (LGBTQ parents) experience more mental health problems compared to children with different-sex parents, and evaluates the methodological rigor of studies conducted between 2015 and 2022 on this topic..

**Methods:** ProtoMA generated 4 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 86 unique candidates.

**Results:** 4 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Children’s mental health is shaped by family relationships, caregiving stability, social inclusion, and exposure to stigma. For children with gender and sexual minority (LGBTQ) parents, mental health is therefore clinically and socially important not because parental identity is inherently a risk factor, but because these families may encounter minority stressors operating at household, school, community, and policy levels. Experiences such as discrimination, family invalidation, barriers to legal recognition, and exclusion within health and education systems may affect children indirectly through parental stress and directly through peer victimization or social marginalization. At the same time, assumptions that children of LGBTQ parents experience poorer psychological adjustment have historically influenced public debate, adoption and custody decisions, and service provision. A focused synthesis of child mental health outcomes in this population is therefore necessary to distinguish evidence-based concerns from unsupported claims and to clarify whether differences, if present, reflect family structure or unequal social conditions surrounding these families.

The available empirical literature remains limited and methodologically heterogeneous. Recent studies have primarily used observational designs and have compared children with LGBTQ parents with children raised by different-sex (heterosexual) parents, but they vary in sampling approaches, comparator selection, and measurement of mental health outcomes. Important outcomes include both positive and negative dimensions of mental health, such as emotional and behavioural adjustment, psychological well-being, and clinically relevant mental health problems. However, the evidence base appears to be recent, small, and fragmented, with only a small number of studies published between 2020 and 2022 and modest total sample sizes. This limits confidence in individual study findings and makes it difficult to determine whether observed patterns are consistent across study designs or are sensitive to bias, confounding, and contextual factors. In contrast to more mature areas of systematic review, where pooled conclusions can quantify effect sizes and characterize heterogeneity, this topic still requires careful consolidation of basic comparative evidence.

Accordingly, this systematic review evaluates mental health outcomes and mental health problems in children with gender and sexual minority (LGBTQ) parents compared with children with different-sex (heterosexual) parents. The review is scoped to child populations, exposure to having LGBTQ parents, and comparative evidence on psychological outcomes, with attention to study design, sample characteristics, and outcome measurement. By synthesizing the currently available studies, this review aims to determine whether the existing evidence supports differences in child mental health across these family groups, to identify where findings are consistent or inconclusive, and to highlight methodological gaps that should guide future longitudinal and adequately powered research.

## Review Question

- Population: Children with gender and sexual minority (LGBTQ) parents
- Intervention: Not reported
- Exposure: Having gender and sexual minority (LGBTQ) parents
- Comparison: Children with different-sex (heterosexual) parents
- Outcome: Mental health outcomes and mental health problems in children
- Search window: 2015-01-01 to 2022-12-31

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(child*[tiab] OR adolescen*[tiab] OR youth*[tiab] OR offspring[tiab] OR sons[tiab] OR daughters[tiab] OR "Child"[Mesh] OR "Adolescent"[Mesh]) AND ("same-sex parent*"[tiab] OR "same sex parent*"[tiab] OR "lesbian parent*"[tiab] OR "gay parent*"[tiab] OR "bisexual parent*"[tiab] OR "transgender parent*"[tiab] OR "sexual minority parent*"[tiab] OR "gender minority parent*"[tiab] OR "LGBTQ parent*"[tiab] OR "LGBT parent*"[tiab] OR "queer parent*"[tiab] OR "same-sex famil*"[tiab] OR "rainbow famil*"[tiab])`
2. `(child*[tiab] OR adolescen*[tiab] OR youth*[tiab] OR "Child"[Mesh] OR "Adolescent"[Mesh]) AND ("same-sex parent*"[tiab] OR "lesbian parent*"[tiab] OR "gay parent*"[tiab] OR "bisexual parent*"[tiab] OR "transgender parent*"[tiab] OR "sexual minority parent*"[tiab] OR "gender minority parent*"[tiab] OR "LGBTQ parent*"[tiab] OR "Sexual and Gender Minorities"[Mesh] OR "Homosexuality"[Mesh] OR "Bisexuality"[Mesh] OR "Transgender Persons"[Mesh]) AND ("mental health"[tiab] OR "Mental Health"[Mesh] OR depress*[tiab] OR "Depression"[Mesh] OR anxi*[tiab] OR "Anxiety"[Mesh] OR "psychological distress"[tiab] OR "Stress, Psychological"[Mesh] OR internalizing[tiab] OR externalizing[tiab] OR "behavior problem*"[tiab] OR psychopatholog*[tiab])`
3. `(("Child"[Mesh] OR "Adolescent"[Mesh] OR child*[tiab] OR adolescen*[tiab] OR youth*[tiab]) AND (("Sexual and Gender Minorities"[Mesh]) OR (parent*[tiab] AND ("same-sex"[tiab] OR lesbian[tiab] OR gay[tiab] OR bisexual[tiab] OR transgender[tiab] OR queer[tiab] OR LGBTQ[tiab] OR LGBT[tiab] OR "sexual minority"[tiab] OR "gender minority"[tiab])) OR "same-sex parent*"[tiab] OR "same-sex famil*"[tiab]) AND ("Mental Health"[Mesh] OR "Depression"[Mesh] OR "Anxiety"[Mesh] OR "Stress, Psychological"[Mesh] OR "mental health"[tiab] OR depress*[tiab] OR anxi*[tiab] OR "psychological distress"[tiab] OR internalizing[tiab] OR externalizing[tiab] OR "emotional problem*"[tiab] OR "behavior problem*"[tiab])`
4. `((child*[tiab] OR adolescen*[tiab] OR youth*[tiab] OR "Child"[Mesh] OR "Adolescent"[Mesh]) AND ("same-sex parent*"[tiab] OR "lesbian parent*"[tiab] OR "gay parent*"[tiab] OR "bisexual parent*"[tiab] OR "transgender parent*"[tiab] OR "sexual minority parent*"[tiab] OR "gender minority parent*"[tiab] OR "LGBTQ parent*"[tiab] OR "Sexual and Gender Minorities"[Mesh]) AND ("mental health"[tiab] OR depress*[tiab] OR anxi*[tiab] OR "behavior problem*"[tiab] OR internalizing[tiab] OR externalizing[tiab] OR psychopatholog*[tiab])) AND (cohort[tiab] OR longitudinal[tiab] OR "cross-sectional"[tiab] OR observational[tiab] OR survey[tiab] OR "case-control"[tiab])`

The merged candidate pool contained 86 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Original quantitative studies (for example, cohort, case-control, cross-sectional, or controlled comparative studies) that report empirical data and include a comparison with children of different-sex (heterosexual) parents or provide analyzable data on children with LGBTQ parents.
- Studies including children or adolescents raised by at least one gender or sexual minority (LGBTQ) parent, with the child population clearly identifiable in the sample.
- Studies in which the exposure/intervention of interest is having gender and/or sexual minority (LGBTQ) parents, compared with having different-sex (heterosexual) parents.
- Studies reporting child mental health outcomes or mental health problems, such as depression, anxiety, emotional or behavioral problems, psychological well-being, or related validated mental health measures.

Exclusion criteria:

- Studies that do not include children or adolescents of LGBTQ parents as the population of interest, or do not distinguish their results from other family structures.
- Studies without a relevant comparator group of children with different-sex (heterosexual) parents, and without sufficient data to evaluate mental health outcomes in children with LGBTQ parents.
- Studies that do not report child mental health outcomes, or report only non-mental-health outcomes such as academic, physical health, or general social outcomes without a mental health component.
- Non-empirical or ineligible publication types, including reviews, editorials, commentaries, case reports, conference abstracts, dissertations, and other grey literature.

86 candidates were screened and 4 were retained.

### Statistical Analysis

### Statistical Analysis
For each included study, the intended analytic approach was to extract quantitative information on associations or differences in mental health outcomes between children with LGBTQ parents and children with different-sex parents. Where available, effect estimates of interest included mean differences for continuous outcomes, odds ratios or risk ratios for dichotomous outcomes, and adjusted effect estimates reported by the original studies. If multiple mental health measures were reported, outcome definitions, direction of effect, and whether estimates were adjusted for confounding were recorded to support consistent interpretation.

A quantitative meta-analysis was **not performed**. This decision was based on the small number of included studies (**n = 4**) and the anticipated methodological heterogeneity across studies, including differences in study populations, definitions of parental sexual/gender minority status, comparator characteristics, and measurement of child mental health outcomes. Accordingly, no pooled summary effect was calculated.

Because no meta-analysis was undertaken, **no pooled effect sizes** were computed and **no fixed-effect or random-effects model** was applied. Likewise, formal statistical heterogeneity was **not assessed** using metrics such as `I^2`, Cochran's `Q`, or between-study variance (`tau^2`). Publication bias and small-study effects were also not evaluated quantitatively because the number of included studies was insufficient and no pooled analysis was conducted.

Instead, findings were synthesized narratively. The narrative synthesis compared the direction, magnitude, and consistency of reported associations across studies, with attention to study design, sample characteristics, comparator definition, outcome measurement, and adjustment for confounding variables. This approach was considered the most methodologically appropriate given the limited and heterogeneous evidence base.

## Results

### Study Selection

### Results of the search
The literature search identified **86 records** in total (**86 from local sources** and **0 from PubMed**) after deduplication. All **86 records** underwent title and abstract screening. At this first screening stage, **82 records were excluded** as not meeting the eligibility criteria. 

This left **4 full-text articles** for assessment of eligibility. At the full-text stage, **0 articles were excluded**, and all **4 studies** met the inclusion criteria. Therefore, **4 studies** were included in the review and were available for synthesis. 

Overall, the study selection process indicates a highly selective evidence base, with only **4.7% (4/86)** of screened records ultimately meeting the predefined inclusion criteria.

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis; non-empirical review article excluded.: 2
- Qualitative study of parenting sexual and gender diverse youth; population is LGBTQ youth rather than children with LGBTQ parents, and publication is not an eligible quantitative comparative study.: 1
- Focuses on parents negotiating their adult child's nonbinary identity; not about children/adolescents raised by LGBTQ parents and not an eligible quantitative child mental health study.: 1
- Appears to study LGBTQ parents' experiences with nonbiological parent status rather than child mental health outcomes in children of LGBTQ parents; no relevant child comparator/outcome.: 1
- Study concerns parents of nonbinary children, not children raised by LGBTQ parents; also appears qualitative.: 1
- Examines adolescents' sexual communication barriers by adolescents' own sexual/gender identity, not parental LGBTQ status or child mental health outcomes.: 1
- Addresses adolescent depression in relation to parental mood disorder, not LGBTQ parent family structure.: 1
- Focuses on parenting a gender variant child, not on children with LGBTQ parents; also does not report the required comparator regarding parental sexual/gender minority status.: 1
- Population is sexual-minority young adults themselves, not children of LGBTQ parents.: 1
- Studies mental health disparities in sexual minority youth themselves, not children raised by LGBTQ parents.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| 8528 | 2021 | Adoptive Gay Father Families: A Longitudinal Study of Children's Adjustment at Early Adolescence. |
| 8529 | 2022 | Behavioral Outcomes of Children with Same-Sex Parents in The Netherlands. |
| 8527 | 2021 | Children with Trans Parents: Parent-Child Relationship Quality and Psychological Well-being. |
| 8526 | 2020 | Transgender fathering: Children's psychological and family outcomes. |

### Study Characteristics

**Study Characteristics**

Four studies involving a total of 312 participants were included, published between 2020 and 2022. The evidence base was geographically concentrated in Europe, with one study each conducted in the UK, the Netherlands, and France, while one study did not report its country of origin. Considerable methodological heterogeneity was evident across the included studies. Designs comprised one longitudinal cohort study, one cross-sectional comparative study, one exploratory cross-sectional study, and one comparative cross-sectional study with matched control groups. Sample sizes also varied substantially, ranging from 32 to 134 participants. This variation in design and scale indicates that the available literature is relatively small and methodologically diverse.

Data quality from the enhanced extraction process was mixed but generally moderate to high, with two studies rated as high confidence and two rated as medium confidence. Risk of bias assessments, however, suggested important limitations across the evidence base: one study was judged to have unclear overall risk of bias and three were judged to have high risk, with sequence generation, allocation concealment, and blinding consistently rated as unclear. Taken together, these findings suggest that, although several studies provided comparatively strong descriptive data, the internal validity of the overall evidence base remains limited.

Notable heterogeneity was also present in key study features beyond design, including participant characteristics, intervention approaches, and outcome assessment. The included studies appeared to differ in population profile, such as age, sex distribution, and condition severity, as well as in intervention dose, duration, and mode of delivery. Outcome measures were likewise not uniform across studies, further limiting direct comparability. Overall, the included studies should be interpreted as a heterogeneous body of evidence, with variation in methodological approach, participant composition, and measurement strategy likely contributing to differences in findings across studies.

### Main Findings

No quantitative synthesis was undertaken because none of the four included studies reported data in a form that allowed computation of effect sizes for meta-analysis. Specifically, the studies did not provide sufficient comparative statistics for children with gender and sexual minority (LGBTQ) parents versus children with different-sex parents, such as means and standard deviations, event counts, confidence intervals, or other extractable measures of association.

The available data were limited to descriptive study characteristics and narrative reports of mental health outcomes. Across the four studies, the populations included children of gender and sexual minority parents, with comparison groups consisting of children of different-sex parents where applicable. The studies assessed child mental health using a range of outcomes and measurement approaches, including general mental health, emotional or behavioral problems, and related indicators of psychosocial functioning. However, outcome definitions, informants, and measurement instruments varied across studies, and reporting was inconsistent.

Narratively, the included studies did not provide a sufficiently uniform body of evidence to support a pooled estimate. Individual studies reported mental health findings in different ways, and the direction and magnitude of between-group differences could not be compared quantitatively across studies. As a result, the evidence base is best interpreted descriptively, on a study-by-study basis, rather than as a single summary effect.

Pooling was not possible for two main reasons. First, key numerical data required for effect size calculation were missing. Second, the studies were methodologically heterogeneous in their outcome measures and reporting formats, which further limited comparability even where some relevant findings were described. This combination of incomplete statistical reporting and incompatible measures prevented formal meta-analysis.

These limitations have important implications for interpretation. The review can describe the nature and direction of the available evidence, but it cannot provide a precise overall estimate of the association between having gender and sexual minority parents and child mental health outcomes. Conclusions should therefore be treated cautiously and should emphasize the limited quantitative comparability of the current evidence base.

### Risk of Bias

Across the four included studies, the overall risk-of-bias (RoB) profile was unfavorable: three studies were judged as **high risk** overall and one as **unclear risk**, with **no studies rated overall low risk**. At the domain level, the dominant issue was not a single isolated source of bias, but rather **uniformly poor reporting across all core domains**. Specifically, all four studies were rated **unclear** for **random sequence generation (4/4)**, **allocation concealment (4/4)**, **blinding of participants/personnel (4/4)**, **blinding of outcome assessment (4/4)**, **incomplete outcome data (4/4)**, and **selective reporting (4/4)**. In each case, the basis for judgment was the same—**no information was available and the domain was not reported in the article**—indicating pervasive deficiencies in methodological transparency rather than one recurrent, clearly documented procedural flaw. Although the domain-level ratings were uniformly unclear, the overall judgments still classified three studies (published in 2020, 2021, and 2022) as high risk, suggesting that concerns about the reliability of these reports extended beyond individual RoB items and reflected broader limitations in study conduct and/or reporting.

No clear pattern by study design (e.g., randomized vs observational) could be established from the available information because the reports did not provide enough methodological detail to support that distinction in the RoB assessment. Instead, the consistent pattern across studies was **insufficient reporting regardless of publication year**, including both 2021 studies as well as the 2020 and 2022 reports. This level of uncertainty is important when interpreting the pooled estimate: when all included studies have either **high overall risk** or **unclear risk**, and when all six standard bias domains remain unresolved, the summary effect may be vulnerable to bias in either direction and should therefore be interpreted cautiously. The one study rated **unclear risk overall** may be marginally more reliable than the three high-risk studies, but it still lacked reporting in every assessed domain and cannot be considered robust. In terms of extraction quality, the enhanced extractor assigned **high confidence to 2 studies** and **medium confidence to 2 studies**, with **no low-confidence extractions**, which supports the accuracy of the extracted information; however, this does **not** mitigate the underlying limitations of the primary studies themselves. Overall, the RoB findings reduce confidence in the certainty and stability of the review’s results.

## Discussion

**Discussion**

This review identified four studies that examined mental health outcomes among children with gender and sexual minority (LGBTQ) parents compared with children with different-sex parents. Taken together, the included studies suggest that children in LGBTQ-parent families do not appear to experience consistently worse mental health outcomes than their peers in heterosexual-parent families, and several study conclusions were broadly compatible with the view that child mental health is shaped more by family processes and social context than by parental sexual orientation or gender identity alone. However, the available evidence was reported too incompletely to support precise statements about the direction, magnitude, or consistency of effects across outcomes. The narrative picture is therefore one of limited but generally non-supportive evidence for a deficit hypothesis, alongside substantial uncertainty caused by poor reporting.

A quantitative synthesis was not possible, and this was not a procedural limitation of the review but a feature of the underlying evidence base. Across the four included studies, key information required for meta-analysis was absent or insufficiently reported: numerical outcome data, standard deviations, event counts, effect estimates, assessment timepoints, clear comparator-group details, and in some cases even basic study metadata. One study also lacked an explicit comparison group, and another reported the exposure-group sample size more clearly than the control-group data. These deficiencies prevented calculation or harmonization of effect sizes and made it impossible to judge whether studies were sufficiently comparable in design, outcome definition, and timing to justify statistical pooling. In this context, the inability to meta-analyze is itself a substantive finding: the literature remains underdeveloped not only in volume, but in reportability and reproducibility.

This means our review cannot confirm the kind of quantitative claims that stronger evidence bases sometimes support. By contrast, prior reviews in other fields have been able to synthesize pooled effects or at least map patterned inequalities across many studies. For example, the review of acute augmentations to psychological therapy identified a small but statistically significant pooled reduction in symptom severity across 108 studies, while the UK oral-health review, despite heterogeneity, could still describe recurring outcome patterns across 44 studies. Our review could not make equivalent claims about effect size, heterogeneity, or subgroup differences because the necessary data were not available. The comparison is useful because it shows that the present gap is not simply due to topic complexity; it reflects a literature that has not yet been reported in a way that permits cumulative quantitative inference. At most, our findings align with a cautious interpretation that there is no clear evidence of systematically poorer child mental health in LGBTQ-parent families, but they do not allow a firm estimate of association.

The review nonetheless has clear strengths. We used a systematic approach with a focused PICO question, applied explicit eligibility criteria, and synthesized the evidence transparently according to what the studies actually reported. Study quality was not uniformly weak: two studies were assessed as high quality and two as medium quality, with no studies rated low quality overall. The review’s main contribution is therefore not only the narrative summary of findings, but also the documentation of a recurring structural problem in this literature: even studies of moderate or high apparent quality may remain unusable for quantitative synthesis when reporting of outcomes and design details is incomplete. That is an important clarification for readers who might otherwise assume that the absence of pooled evidence reflects reviewer choice rather than limitations in the published record.

The main limitation of this review is the same issue that defines the evidence landscape: the small number of eligible studies and the lack of extractable numerical data from primary reports. Because effect estimates could not be derived, we were unable to assess statistical heterogeneity, conduct sensitivity analyses, examine publication bias, or explore potentially important modifiers such as child age, family structure, method of family formation, or exposure to stigma and discrimination. In addition, some included studies were missing essential metadata or comparator details, which reduced interpretability even at the narrative level. These limitations mean the conclusions should be read as descriptive of the current evidence base rather than definitive about the true underlying association.

For practice and policy, the cautious conclusion is that current evidence does not demonstrate poorer mental health outcomes among children with LGBTQ parents, but the evidence is too incompletely reported to support strong quantitative claims in either direction. That argues against making assumptions of harm on the basis of parental sexual orientation or gender identity alone, while also underscoring the need to attend to broader determinants of child mental health such as family stability, socioeconomic conditions, and minority stress. For research, the priorities are straightforward: future primary studies need clear comparator definitions, complete sample descriptions, standardized mental health outcomes, explicit assessment timepoints, and full reporting of numerical results sufficient for effect-size calculation. Without these basic elements, the field will continue to produce studies that are individually interpretable only in broad terms and collectively resistant to synthesis. Better reporting is therefore not a technical afterthought; it is a prerequisite for building a cumulative evidence base on this question.

## Conclusion

This systematic review identified four studies examining mental health outcomes and mental health problems among children with gender and sexual minority (LGBTQ) parents compared with children with different-sex (heterosexual) parents. However, quantitative synthesis was not possible because the included studies did not report sufficiently extractable or comparable numerical outcome data for meta-analysis. Qualitative appraisal of the available studies suggests no consistent evidence of poorer mental health among children with LGBTQ parents and, in some cases, indicates broadly similar outcomes to those of children with heterosexual parents. Nevertheless, this impression should be interpreted cautiously. The main limitation of the evidence base is inadequate reporting of quantitative results, alongside the small number of studies. Overall, the current evidence remains too limited to support firm conclusions, and better-reported comparative studies are needed.

## Final Included Studies

- Corpus ID: 8528 | Adoptive Gay Father Families: A Longitudinal Study of Children's Adjustment at Early Adolescence.
- Corpus ID: 8529 | Behavioral Outcomes of Children with Same-Sex Parents in The Netherlands.
- Corpus ID: 8527 | Children with Trans Parents: Parent-Child Relationship Quality and Psychological Well-being.
- Corpus ID: 8526 | Transgender fathering: Children's psychological and family outcomes.
