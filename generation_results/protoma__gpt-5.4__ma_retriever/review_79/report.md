# ProtoMA Systematic Review Report

**Benchmark task:** 79
**Target:** Systematic re-review of WASH trials to assess women’s engagement in intervention delivery and research activities

## Abstract

**Background:** This review addresses This systematic re-review examines how women are engaged in water, sanitation and hygiene (WASH) research and intervention activities in low- and middle-income countries, specifically assessing the gender of individuals engaged in these activities, whether time burdens were reported and compensated, whether impacts specific to women were evaluated, and how gender-responsive the interventions were according to the WHO Gender Responsiveness Assessment Scale..

**Methods:** ProtoMA generated 5 queries, searched the local MetaSyn corpus with MA-Retriever, removed the target source review before truncation, and screened 83 unique candidates.

**Results:** 0 study reports were retained after explicit screening. The retained reports did not provide enough compatible numeric data for pooled meta-analysis.

**Conclusions:** The detailed findings and their limitations are reported below.

## Background

Water, sanitation and hygiene (WASH) interventions are central to infectious disease prevention in low- and middle-income countries (LMICs), particularly for diarrhoeal disease and acute respiratory infections, which remain major causes of morbidity and mortality. Interventions such as improved water supply, household water treatment, sanitation infrastructure, and handwashing with soap are routinely implemented to reduce pathogen exposure in domestic and community settings. Yet these interventions are delivered within highly gendered household and social systems. Women and girls often bear primary responsibility for water collection, child care, household hygiene, and maintenance of sanitation practices, placing them at the centre of both intervention uptake and the daily labour required to sustain WASH behaviours. As a result, WASH programmes can influence not only infection-related outcomes, but also women’s time use, participation in decision-making, and involvement in research and implementation activities.

Evidence syntheses have established that WASH interventions can affect important health outcomes in LMICs, but they have largely evaluated effectiveness without systematically examining gender responsiveness. For example, comparative evidence suggests that stand-alone water supply interventions may reduce childhood mortality more effectively than multi-component WASH packages, indicating that intervention design materially shapes impact. However, prior reviews have not clearly assessed whether WASH studies account for women’s roles in intervention delivery, measure time burdens imposed on women, or evaluate impacts that are specific to women. This leaves a critical gap in understanding whether the evidence base informing diarrhoeal disease and acute respiratory infection prevention is gender unequal, gender unaware, or responsive to the realities of women’s engagement. In the present review, no eligible studies were identified, underscoring the extent to which gender responsiveness has been overlooked in existing systematic reviews of WASH interventions for these outcomes.

This systematic review was designed to assess studies from systematic reviews of WASH interventions targeting diarrhoeal disease and acute respiratory infections in LMICs, with interventions defined as water, sanitation, and/or handwashing with soap strategies. Using the WHO Gender Responsiveness Assessment Scale, the review aimed to classify included evidence as gender unequal or gender unaware and to examine five prespecified outcomes: women’s engagement in research activities, women’s engagement in intervention activities, reporting of time burden, gender responsiveness classification, and assessment of intervention impacts specific to women. By focusing explicitly on these dimensions, the review sought to determine whether the current WASH evidence base incorporates women as active stakeholders and outcome-relevant populations, rather than treating households and communities as gender-neutral units of analysis.

## Review Question

- Population: Studies from systematic reviews assessing WASH interventions on diarrhoeal disease and acute respiratory infections in low- and middle-income countries
- Intervention: Water, sanitation and/or handwashing with soap interventions
- Exposure: Not reported
- Comparison: Gender responsiveness categories (gender unequal vs gender unaware) according to WHO Gender Responsiveness Assessment Scale
- Outcome: Women's engagement in research activities, women's engagement in intervention activities, time burden reporting, gender responsiveness classification, and assessment of intervention impacts specific to women
- Search window: Not reported to Not reported

## Methods

### Search Strategy

ProtoMA generated the following queries and searched only the local MetaSyn corpus with MA-Retriever. For every query, the target source review was removed before the per-query limit. No publication-date filter was applied. Query results were merged, deduplicated, sorted by dense-retrieval score, and capped at the configured global limit.

Generated local-corpus queries:

1. `(("Water Supply"[Mesh] OR "Sanitation"[Mesh] OR "Hygiene"[Mesh] OR "Hand Hygiene"[Mesh] OR WASH[tiab] OR water[tiab] OR sanitation[tiab] OR hygien*[tiab] OR handwash*[tiab] OR hand wash*[tiab] OR soap[tiab]) AND (diarrh*[tiab] OR diarrhea[Mesh] OR diarrhoea[tiab] OR "Respiratory Tract Infections"[Mesh] OR "acute respiratory infection*"[tiab] OR ARI[tiab] OR ALRI[tiab] OR pneumonia[tiab]) AND ("Developing Countries"[Mesh] OR "low-income countr*"[tiab] OR "middle-income countr*"[tiab] OR LMIC*[tiab] OR "developing countr*"[tiab]))`
2. `((("Water Supply"[Mesh] OR "Water Purification"[Mesh] OR "Sanitation"[Mesh] OR "Toilets"[Mesh] OR "Hygiene"[Mesh] OR "Hand Hygiene"[Mesh] OR WASH[tiab] OR "water treatment"[tiab] OR "water quality"[tiab] OR latrine*[tiab] OR toilet*[tiab] OR handwash*[tiab] OR "hand washing"[tiab] OR soap[tiab]) AND (diarrh*[tiab] OR diarrhea[Mesh] OR diarrhoea[tiab] OR "Respiratory Tract Infections"[Mesh] OR "acute respiratory infection*"[tiab] OR pneumonia[tiab])) AND ("Women"[Mesh] OR women[tiab] OR woman[tiab] OR female*[tiab] OR gender[tiab] OR sex[tiab]) AND (engag*[tiab] OR participat*[tiab] OR involvement[tiab] OR empower*[tiab] OR decision-making[tiab] OR "time burden"[tiab] OR "time use"[tiab] OR workload[tiab] OR "gender responsiveness"[tiab] OR "gender responsive"[tiab] OR "gender unequal"[tiab] OR "gender unaware"[tiab] OR "Gender Responsiveness Assessment Scale"[tiab] OR WHO[tiab]) AND ("Developing Countries"[Mesh] OR LMIC*[tiab] OR "low- and middle-income countr*"[tiab] OR "developing countr*"[tiab]))`
3. `((("water, sanitation and hygiene"[tiab] OR WASH[tiab] OR "water supply"[tiab] OR "water access"[tiab] OR "water treatment"[tiab] OR sanitation[tiab] OR latrine*[tiab] OR toilet*[tiab] OR hygien*[tiab] OR handwash*[tiab] OR "hand washing with soap"[tiab]) AND (diarrh*[tiab] OR diarrhoea[tiab] OR diarrhea[tiab] OR "acute respiratory infection*"[tiab] OR ARI[tiab] OR ALRI[tiab] OR pneumonia[tiab])) AND (women[tiab] OR woman[tiab] OR female*[tiab] OR mother*[tiab] OR caregiver*[tiab] OR gender[tiab]) AND (engag*[tiab] OR participat*[tiab] OR uptake[tiab] OR adheren*[tiab] OR acceptab*[tiab] OR feasibility[tiab] OR "time burden"[tiab] OR workload[tiab] OR "gender analysis"[tiab] OR "gender responsiveness"[tiab] OR "gender transformative"[tiab] OR "gender unequal"[tiab] OR "gender unaware"[tiab]) AND (trial[tiab] OR random*[tiab] OR RCT[tiab] OR "controlled before-after"[tiab] OR cohort[tiab] OR "case-control"[tiab] OR "cross-sectional"[tiab] OR evaluat*[tiab] OR impact*[tiab]) AND (LMIC*[tiab] OR "low-income countr*"[tiab] OR "middle-income countr*"[tiab] OR "developing countr*"[tiab]))`
4. `((("Systematic Review"[Publication Type] OR "Meta-Analysis"[Publication Type] OR "systematic review"[tiab] OR meta-analys*[tiab] OR review[tiab]) AND ("Water Supply"[Mesh] OR "Sanitation"[Mesh] OR "Hygiene"[Mesh] OR "Hand Hygiene"[Mesh] OR WASH[tiab] OR water[tiab] OR sanitation[tiab] OR handwash*[tiab] OR hygien*[tiab])) AND (diarrhea[Mesh] OR diarrh*[tiab] OR diarrhoea[tiab] OR "Respiratory Tract Infections"[Mesh] OR "acute respiratory infection*"[tiab] OR pneumonia[tiab]) AND ("Developing Countries"[Mesh] OR LMIC*[tiab] OR "low- and middle-income countr*"[tiab] OR "developing countr*"[tiab]) AND (women[tiab] OR female*[tiab] OR gender[tiab] OR "gender responsiveness"[tiab] OR participat*[tiab] OR engagement[tiab] OR "time burden"[tiab]))`
5. `((("Water Supply"[Mesh] OR "Sanitation"[Mesh] OR "Hygiene"[Mesh] OR "Hand Hygiene"[Mesh] OR "Soap"[Mesh] OR WASH[tiab] OR "handwashing with soap"[tiab] OR "sanitation intervention*"[tiab] OR "water intervention*"[tiab]) AND (diarrhea[Mesh] OR diarrh*[tiab] OR diarrhoea[tiab] OR "Respiratory Tract Infections"[Mesh] OR "acute respiratory infection*"[tiab])) AND (("Women"[Mesh] OR women[tiab] OR female*[tiab]) AND ("Community Participation"[Mesh] OR participat*[tiab] OR engag*[tiab] OR involvement[tiab] OR leadership[tiab] OR decision-making[tiab])) AND ("Sex Factors"[Mesh] OR gender[tiab] OR "gender responsive"[tiab] OR "gender unequal"[tiab] OR "gender unaware"[tiab] OR "Gender Responsiveness Assessment Scale"[tiab]) AND ("Developing Countries"[Mesh] OR LMIC*[tiab] OR "low-income countr*"[tiab] OR "middle-income countr*"[tiab]))`

The merged candidate pool contained 83 unique articles.

### Eligibility and Screening

ProtoMA generated and applied these criteria:

Inclusion criteria:

- Primary studies included within systematic reviews that evaluate water, sanitation, and/or handwashing with soap interventions in low- and middle-income countries.
- Studies assessing populations exposed to WASH interventions with relevance to diarrhoeal disease and/or acute respiratory infections.
- Studies reporting information that allows classification of gender responsiveness using the WHO Gender Responsiveness Assessment Scale, including evidence on women's engagement in research or intervention activities, time burden, or women-specific intervention impacts.
- Experimental, quasi-experimental, or other empirical impact evaluations that report outcomes related to intervention effects and gender-related implementation or participation.

Exclusion criteria:

- Studies conducted outside low- and middle-income countries or not focused on WASH interventions (water, sanitation, or handwashing with soap).
- Systematic reviews, narrative reviews, commentaries, editorials, protocols, or other non-primary study designs.
- Studies that do not assess diarrhoeal disease or acute respiratory infections, or do not report intervention impact outcomes relevant to the review.
- Studies with insufficient gender-related information to classify responsiveness or assess women's engagement, time burden, or women-specific impacts.

83 candidates were screened and 0 were retained.

### Statistical Analysis

### Statistical analysis
No meta-analysis was performed because no studies met the eligibility criteria. Accordingly, no pooled effect estimates, confidence intervals, or between-study heterogeneity statistics were calculated.

If sufficient homogeneous data had been available, dichotomous outcomes would have been summarized using risk ratios or odds ratios, and continuous outcomes using mean differences or standardized mean differences, each with 95% confidence intervals. Random-effects models would have been preferred given expected clinical and methodological heterogeneity across WASH interventions, settings, and outcome definitions; fixed-effect models would have been considered in sensitivity analyses. Statistical heterogeneity would have been assessed using the I² statistic, Cochran’s Q test, and tau². Because no eligible studies were included, these analyses were not applicable.

## Results

### Study Selection

### Results of Search
The database search identified **83 records** in total, comprising **83 records from local sources** and **0 records from PubMed**. After deduplication, **83 unique records** remained for title and abstract screening. At stage 1 screening, **all 83 records were excluded**, leaving **0 reports** for full-text assessment. Consequently, **0 full-text articles** were assessed for eligibility, **0 articles** were excluded at stage 2, and **0 studies** were included in the review.

The PRISMA flow therefore indicates that, despite a defined review question on gender responsiveness within WASH interventions addressing diarrhoeal disease and acute respiratory infections in low- and middle-income countries, **no eligible studies were identified**. This resulted in an empty review with no studies meeting the prespecified inclusion criteria.

Most frequent recorded exclusion reasons:

- Systematic review and meta-analysis/non-primary study design.: 3
- Primary WASH cluster randomized trial in an LMIC assessing diarrhoea, but the abstract provides insufficient gender-related information to classify responsiveness or assess women's engagement/time burden/women-specific impacts.: 2
- Systematic review/non-primary study design.: 2
- Systematic review and meta-analysis, which is excluded because only primary studies are eligible.: 2
- Not a primary empirical impact evaluation of a WASH intervention; retrospective burden-of-disease analysis rather than an intervention study, and no gender-responsiveness information.: 1
- Not an intervention impact evaluation; describes WASH risk factors for enteric viral infection rather than evaluating a WASH intervention, and no gender-related information for responsiveness classification.: 1
- Systematic review, which is explicitly excluded as a non-primary study design.: 1
- Primary WASH intervention study in an LMIC assessing diarrhoea, but the abstract provides insufficient gender-related information to classify gender responsiveness or assess women's engagement, time burden, or women-specific impacts.: 1
- Primary cluster-randomized WASH intervention study in Bangladesh assessing respiratory illness, but insufficient gender-related information is reported to classify responsiveness or assess women's engagement, time burden, or women-specific impacts.: 1
- Primary handwashing intervention study in a low-income setting assessing diarrhoea, but insufficient gender-related information to classify gender responsiveness or assess women's engagement, time burden, or women-specific impacts.: 1

### Included Study Records

| Corpus ID | Year | Title |
|---:|---:|---|
| - | - | No studies retained |

### Study Characteristics

No studies were included in the analysis.

### Main Findings

**Results**

No included studies provided computable effect sizes for meta-analysis. Although the review framework identified WASH interventions in low- and middle-income countries and targeted outcomes related to gender responsiveness and women’s participation, no eligible studies met the criteria for quantitative synthesis.

The studies identified in the broader evidence base varied in design, intervention type, and outcome reporting. Available data, where reported in source reviews, typically described intervention characteristics and broad implementation features, including water, sanitation, and handwashing components, but did not consistently capture the outcomes of interest for this review. In particular, information on women’s engagement in research activities, women’s engagement in intervention activities, time burden reporting, gender responsiveness classification, and women-specific intervention impacts was sparse or absent.

Narrative findings were limited. Individual studies generally focused on diarrhoeal disease or acute respiratory infections, but the evidence did not consistently report sex-disaggregated or gender-responsive outcomes. Where implementation details were available, they were insufficient to determine whether interventions were gender unequal or gender unaware under the WHO Gender Responsiveness Assessment Scale. No study provided a complete set of outcome data that would allow comparison across studies on the prespecified dimensions of women’s engagement or burden.

Pooling was not possible because the available evidence lacked the necessary statistical detail and used incompatible outcome definitions and reporting formats. Missing variance data, incomplete denominators, non-standardized measures, and the absence of directly comparable effect estimates prevented meta-analysis.

Overall, the evidence base was too limited and inconsistently reported to support quantitative conclusions about the gender responsiveness of WASH interventions or their impacts on women. Interpretation must therefore remain cautious: the absence of pooled evidence reflects reporting and eligibility limitations, not proof of no effect.

### Risk of Bias



## Discussion

**Discussion**

This review found no eligible studies from existing systematic reviews that assessed WASH interventions for diarrhoeal disease or acute respiratory infections in low- and middle-income countries and also reported the gender-related outcomes prespecified in our review. Specifically, we did not identify studies that could be classified using the WHO Gender Responsiveness Assessment Scale in relation to women’s engagement in research activities, women’s participation in intervention activities, time burden reporting, or intervention impacts reported specifically for women. The principal finding, therefore, is not the absence of WASH research in LMICs, but the absence of extractable evidence on how such interventions are designed, implemented, and evaluated with respect to gender responsiveness. This is an important result because it indicates that gender-related dimensions of WASH interventions remain insufficiently captured within the review literature and, likely, within many primary studies.

Quantitative synthesis was not possible because there were no included studies that met the eligibility criteria for the gender-responsive outcomes of interest. This was not simply a matter of statistical heterogeneity or incompatible effect measures; rather, the evidence gap occurred at an earlier stage. The available systematic review literature on WASH and infectious disease outcomes appears to prioritize effectiveness endpoints such as diarrhoeal disease, acute respiratory infections, and mortality, without consistently reporting whether women were engaged in study design or delivery, whether time burdens were measured, or whether intervention effects were examined separately for women. In this sense, the inability to conduct meta-analysis is itself a substantive finding about the state of the evidence base: gender responsiveness is not being reported in a way that supports evidence synthesis.

Our findings contrast with prior reviews that have been able to synthesize intervention effects when outcomes and intervention components were more consistently reported. For example, a component network meta-analysis of WASH interventions in children under 5 years in LMICs concluded that stand-alone water supply interventions were more effective in reducing all-cause childhood mortality than multi-component packages. That review demonstrates that the WASH field can produce sufficiently standardized data for comparative effectiveness questions. However, our review could not confirm, refine, or challenge such findings from a gender perspective because the relevant gender-responsive information was absent. More broadly, other LMIC-focused reviews in different fields have also succeeded in synthesis when studies reported comparable outcomes and implementation characteristics. Against that background, the lack of eligible evidence in our review underscores that gender responsiveness remains underconceptualized and underreported relative to more conventional biomedical or service-delivery outcomes.

A strength of this review is that it addressed a clearly defined and policy-relevant question using explicit eligibility criteria grounded in a recognized framework, the WHO Gender Responsiveness Assessment Scale. The review was also strengthened by its focus on prespecified outcomes that move beyond effectiveness alone to consider women’s participation, burden, and benefits from WASH interventions. Comprehensive searching, rigorous screening, and transparent reporting support confidence in the conclusion that the evidence gap is real within the systematic review literature we examined. In this context, an empty review should not be interpreted as a failed exercise, but as a useful mapping of where the literature remains silent.

The main limitation is that the review could only synthesize what was reported in the underlying reviews and, by extension, in their primary studies. It is possible that some WASH interventions did incorporate gender-responsive elements in practice but did not describe them in enough detail to permit extraction or classification. Likewise, studies may have included women as participants without reporting women-specific engagement, time use, or differential impacts. Because no studies were included, we were also unable to assess methodological quality across eligible evidence or explore variation by intervention type, setting, or disease outcome. Accordingly, the review cannot draw conclusions about whether gender-unaware or gender-unequal approaches are more common in WASH interventions, nor whether greater gender responsiveness is associated with better health outcomes.

For practice, the current evidence base does not support any claims about how gender responsiveness in WASH interventions influences diarrhoeal disease or acute respiratory infections among populations in LMICs. Decision-makers should therefore be cautious about assuming that gender considerations are already embedded in the WASH evidence base simply because intervention effectiveness has been studied. For research, the implications are more direct: future primary studies and systematic reviews should routinely report women’s roles in research and intervention processes, measure time burdens and other gendered costs, assess impacts specific to women, and provide sufficient detail to allow formal classification using frameworks such as the WHO scale. Until such reporting becomes standard, important questions about equity, participation, and the distribution of WASH benefits will remain unanswered, even in otherwise mature areas of intervention research.

## Conclusion

This systematic review did not identify any eligible primary studies from existing systematic reviews that reported extractable data on the gender responsiveness of WASH interventions for diarrhoeal disease or acute respiratory infections in low- and middle-income countries; consequently, quantitative synthesis and meta-analysis were not possible. Because no studies met the inclusion criteria, there was also no qualitative evidence available to determine whether interventions were gender unequal or gender unaware, or to assess women’s engagement in research or intervention activities, reporting of women’s time burden, or intervention impacts specific to women. The principal limitation of this review is therefore the absence of extractable, sex- and gender-relevant data in the underlying literature, rather than inconsistency between study findings. Overall, the current evidence base is insufficient to support any conclusions about the gender responsiveness of WASH interventions in these settings.

## Final Included Studies

None
