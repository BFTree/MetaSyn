# Systematic Review / Scoping-Style Evidence Synthesis of Evaluation Methods for Synthetic Structured Health Data (MetaSyn PubMed Corpus Only, 2018-01-01 to 2024-07-31)

## Review Question

This evidence synthesis examined whether the research community has reached any consensus on standardized methods for evaluating synthetic structured health-related or medical data, with particular attention to:

1. how utility is assessed,
2. how privacy is assessed,
3. whether privacy is given equal weight to utility, and
4. what gaps or weaknesses remain in current evaluation practice.

The synthesis was restricted strictly to the local MetaSyn PubMed corpus. No external databases or retrieval sources were used.

## Methods

### Data source and date limits

- **Retrieval source:** local MetaSyn PubMed corpus only
- **Search window:** 2018-01-01 through 2024-07-31
- **Target evidence type:** English-language primary research studies on **synthetic structured health/medical data** where generated outputs were **actually evaluated**
- **Exclusions:** reviews, surveys, protocols, non-English publications, poster abstracts, studies without evaluation of generated output, and studies using unstructured data such as images or text

### Exact local corpus search queries used

Two focused searches were run over the local MetaSyn PubMed corpus.

**Query 1**
```text
("synthetic data" OR "synthetic electronic health records" OR "synthetic health data" OR "synthetic medical data") AND (evaluation OR utility OR privacy) AND (health OR medical OR EHR OR claims) AND 2018:2024
```

- **Returned candidate records:** 20

**Query 2**
```text
((synthetic AND (tabular OR structured OR longitudinal OR EHR OR electronic health record* OR administrative health OR claims)) AND (health OR medical OR clinical) AND (privacy OR disclosure OR membership inference OR utility OR fidelity OR evaluation OR benchmark OR framework)) AND 2018:2024
```

- **Returned candidate records:** 20

### Retrieval results and deduplication

Across both searches, there were **27 unique candidate records** after overlap review.

### Screening approach

Screening was conducted against the stated eligibility criteria using the local corpus retrieval output and the available record-level information. Where only title/abstract-level information was available, screening and synthesis were treated as **abstract-based** and this is stated explicitly below.

## Retrieval and Screening Results

### Unique retrieved candidate records

The two searches together yielded the following unique Corpus IDs:

57829, 73639, 4982, 75141, 4849, 4850, 4837, 73343, 73641, 4863, 73412, 75094, 4838, 73201, 4848, 73473, 4867, 4845, 4859, 75096, 75051, 4842, 4986, 75142, 72166, 73643, 4834.

### Screening decisions

#### Excluded records

The following records were excluded based on the eligibility criteria:

- **Corpus ID 57829** — *Synthetic data generation methods for longitudinal and time series health data: a systematic review.*  
  **Reason:** systematic review; not primary research.

- **Corpus ID 72166** — *The Use of Electronic Health Records in Physiotherapy Practice: Protocol for a Scoping Review.*  
  **Reason:** protocol; not primary research on synthetic data evaluation.

- **Corpus ID 73201** — *Privacy-, linguistic-, and information-preserving synthesis of clinical documentation through generative agents.*  
  **Reason:** unstructured text/clinical documentation.

- **Corpus ID 73643** — *De-identification is not enough: a comparison between de-identified and synthetic clinical notes.*  
  **Reason:** unstructured clinical notes/text.

- **Corpus ID 75142** — *Synthesize Extremely High-dimensional Longitudinal Electronic Health Records via Hierarchical Autoregressive Language Model.*  
  **Reason:** appears to be a duplicate/variant record of Corpus ID 4986.

- **Corpus ID 73412** — *Synthetic data production for biomedical research.*  
  **Reason:** insufficient indication from available record-level information that this is an eligible primary study evaluating generated synthetic structured health data; conservatively excluded.

- **Corpus ID 4837** — *The Problem of Fairness in Synthetic Healthcare Data.*  
  **Reason:** insufficient indication from available record-level information that the paper met the review’s requirement for direct evaluation of generated synthetic structured outputs on privacy and/or utility grounds; conservatively excluded.

#### Included records

**20 studies** were included on a title/abstract-based screen as primary research on synthetic structured health/medical data with evaluation of outputs on utility and/or privacy dimensions.

Because full-text sections were not consistently available in the corpus evidence used for this synthesis, several study-level inferences below are based on **abstract/title-level information only**.

## Characteristics of the Included Evidence

### Broad study types represented

The included evidence clustered into four broad groups:

1. **Generation-method papers with evaluation of synthetic EHR/claims/tabular data**
   - Examples include synthetic EHR, longitudinal records, hospital claims, and administrative health data generation studies such as [Synthetic electronic health records generated with variational graph autoencoders](metasyn://corpus/4982) [1], [Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications](metasyn://corpus/75141) [2], [A method for generating synthetic longitudinal health data](metasyn://corpus/73343) [3], and [Generating synthetic data from administrative health records for drug safety and effectiveness studies](metasyn://corpus/4834) [4].

2. **Evaluation-framework or benchmarking papers**
   - These include [A comprehensive evaluation framework for synthetic medical tabular data generation](metasyn://corpus/73639) [5], [Comprehensive evaluation framework for synthetic tabular data in health: fidelity, utility and privacy analysis of generative models with and without privacy guarantees](metasyn://corpus/73641) [6], [Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions](metasyn://corpus/4863) [7], and [Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation](metasyn://corpus/4849) [8].

3. **Privacy-focused evaluation papers**
   - Examples include [Membership inference attacks against synthetic health data](metasyn://corpus/4867) [9], [Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation](metasyn://corpus/4842) [10], and [Evaluating Privacy and Utility in Synthetic EHR Data Generation for Adverse Drug Event Detection](metasyn://corpus/75051) [11].

4. **Utility/actionability/application-focused papers**
   - Examples include [Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology](metasyn://corpus/4838) [12], [Spot the difference: comparing results of analyses from real patient data and synthetic derivatives](metasyn://corpus/4845) [13], [Evaluation of Synthetic Data Generation Methods for Medical Tabular Data: Representation of Distribution Tails](metasyn://corpus/75094) [14], and [How Useful Is Synthetic Data in Developing Predictive Models for Health?](metasyn://corpus/75096) [15].

### Data types represented

The review question was limited to structured data, and the included studies were predominantly about:

- tabular medical data,
- EHR data,
- longitudinal EHR,
- hospital claims data,
- administrative health records,
- epidemiologic or registry-like structured data.

This body of evidence is therefore mainly about **structured/tabular/longitudinal health data**, not text or image generation.

## Main Findings

## 1. Consensus on standardized evaluation methods: no clear field-wide consensus

Across the 2018-01-01 to 2024-07-31 local MetaSyn PubMed corpus evidence, the literature does **not** show a mature, field-wide consensus on a single standardized method for evaluating synthetic structured health data.

The strongest direct signal comes from [Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions](metasyn://corpus/4863) [7], which explicitly identified a **lack of standardized and objective evaluation and benchmarking strategy**. That statement aligns closely with the overall pattern across the included studies.

### What the literature does show instead

Rather than consensus, the evidence suggests:

- **heterogeneous evaluation practice**,  
- **multiple partially overlapping dimensions**, and
- **emerging framework-building efforts** rather than established standards.

The framework-oriented papers—especially [A comprehensive evaluation framework for synthetic medical tabular data generation](metasyn://corpus/73639) [5], [Comprehensive evaluation framework for synthetic tabular data in health: fidelity, utility and privacy analysis of generative models with and without privacy guarantees](metasyn://corpus/73641) [6], [Synthetic Tabular Data Evaluation in the Health Domain Covering Resemblance, Utility, and Privacy Dimensions](metasyn://corpus/4863) [7], and [Creating High-Quality Synthetic Health Data: Framework for Model Development and Validation](metasyn://corpus/4849) [8]—look less like evidence of consensus already achieved and more like evidence that the field recognizes the problem and is actively trying to solve it.

### Nature of the non-consensus

The lack of consensus appears on several levels:

- **which dimensions must always be evaluated,**
- **which privacy metrics are sufficient,**
- **which utility metrics are most meaningful,**
- **whether trade-off analysis must be explicit,**
- **how to compare models across studies,**
- **whether privacy guarantees should be empirical, formal, or both.**

No single metric set emerged from the retrieved corpus as a universally adopted standard.

## 2. Utility assessment is broader, more common, and generally more mature than privacy assessment

### Utility was evaluated in many different ways

The included studies show that utility assessment is often multi-layered and application-specific. Utility-related evaluations appear to include:

- **statistical resemblance/fidelity** to real data,
- **preservation of structure or relationships** in tabular/longitudinal records,
- **downstream predictive performance**,
- **epidemiologic or analytic reproducibility**,
- **use-case actionability**,
- **performance in specialized settings**, such as adverse drug event detection, drug safety/effectiveness studies, and representation of rare events or distribution tails.

Examples from the included corpus include:

- [Evaluation of Synthetic Data Generation Methods for Medical Tabular Data: Representation of Distribution Tails](metasyn://corpus/75094) [14], which indicates attention to how well synthetic data preserve difficult but important aspects of the original distribution.
- [How Useful Is Synthetic Data in Developing Predictive Models for Health?](metasyn://corpus/75096) [15], which suggests a downstream predictive modeling perspective.
- [Exploring the utility of synthetic data to extract more value from sensitive health data assets: A focused example in perinatal epidemiology](metasyn://corpus/4838) [12], which suggests analytic or epidemiologic utility.
- [Spot the difference: comparing results of analyses from real patient data and synthetic derivatives](metasyn://corpus/4845) [13], which directly suggests comparison of substantive analytical outputs between real and synthetic data.
- [Actionability of Synthetic Data in a Heterogeneous and Rare Health Care Demographic: Adolescents and Young Adults With Cancer](metasyn://corpus/73473) [16], which indicates practical usefulness in a rare and heterogeneous subgroup context.

### Utility assessment appears more operationalized than privacy assessment

Even where there is no standard, utility assessment appears relatively more developed because it can be examined through many established analytic lenses:

- model performance,
- preservation of distributions,
- subgroup behavior,
- reproducibility of findings,
- downstream task success.

This diversity is a strength in one sense, but it also contributes to non-comparability across studies.

## 3. Privacy assessment is present, but less consistently emphasized and less standardized

Privacy is clearly part of the literature, but it is less uniformly incorporated than utility and is often narrower in scope.

### Privacy-focused approaches identified in the corpus

The included studies indicate several privacy evaluation modes:

- **identity disclosure risk**, as in [Evaluating Identity Disclosure Risk in Fully Synthetic Health Data: Model Development and Validation](metasyn://corpus/4842) [10];
- **membership inference attack vulnerability**, as in [Membership inference attacks against synthetic health data](metasyn://corpus/4867) [9];
- **joint privacy-and-utility assessment**, as in [Evaluating Privacy and Utility in Synthetic EHR Data Generation for Adverse Drug Event Detection](metasyn://corpus/75051) [11];
- **comparisons involving models with and without privacy guarantees**, as suggested by [Comprehensive evaluation framework for synthetic tabular data in health: fidelity, utility and privacy analysis of generative models with and without privacy guarantees](metasyn://corpus/73641) [6].

### Privacy assessment seems more fragmented

The privacy literature in the retrieved corpus does not point to a common agreed core battery equivalent to a universal benchmark. Instead, studies appear to use selected privacy checks such as:

- disclosure risk estimation,
- membership inference attacks,
- privacy-threshold criteria,
- privacy-guarantee comparisons.

An especially concrete example from the retrieval notes is [A method for generating synthetic longitudinal health data](metasyn://corpus/73343) [3], which reportedly used **dual utility evaluation plus a privacy threshold of 0.09**. This is useful evidence that privacy can be quantified explicitly, but it also illustrates the problem: such thresholds are not clearly shown to be widely standardized across the field.

## 4. Privacy is usually not given equal weight to utility

The balance of evidence suggests that **privacy is not generally given equal weight to utility** in the evaluation of synthetic structured health data.

### Why this conclusion follows from the included studies

First, many included titles are explicitly utility-oriented or application-oriented, while a smaller subset is explicitly privacy-oriented. Utility appears in studies about:

- predictive modeling,
- actionability,
- epidemiologic value,
- analytic similarity,
- tail representation,
- use-case substitution of linked elements,
- AI applications.