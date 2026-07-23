# Systematic Review of Automated EHR-Integrated Sepsis Alerting Systems in Hospitalized Adults (Local MetaSyn PubMed Corpus Only)

## Review Question

Among hospitalized adult patients with sepsis or at risk for sepsis, do automated sepsis alerting systems integrated into electronic health records—whether rule-based algorithms or machine-learning-based prediction methods—improve mortality and length-of-stay outcomes compared with usual care without automated alerts?

Secondary questions:
- Does effectiveness vary by clinical setting, especially ICU, emergency department, and hospital ward?
- Does effectiveness vary by prediction method, especially rule-based versus machine learning?

Date limits applied to retrieval: **1917-01-01 through 2021-12-31**.

---

## Methods

### Data source

The review was restricted to the **local MetaSyn PubMed corpus** as the only retrieval source, as required.

### Exact local corpus search queries used

The following exact queries were used in the local corpus:

1. ```
   (sepsis OR septic) AND (alert OR alerts OR alerting OR alarm) AND (electronic health record OR EHR OR electronic medical record OR EMR) AND (mortality OR "length of stay" OR hospital stay) AND (adult OR adults) AND (1917/01/01:2021/12/31[dp])
   ```

2. ```
   (sepsis OR septic) AND ((machine learning) OR predictive OR prediction OR algorithm OR surveillance) AND (electronic health record OR EHR OR electronic medical record OR EMR) AND (alert OR alerts OR decision support) AND (mortality OR "length of stay") AND (1917/01/01:2021/12/31[dp])
   ```

3. ```
   (sepsis OR severe sepsis OR septic shock) AND ((ICU OR intensive care) OR (emergency department) OR ward OR inpatient OR hospital-wide) AND (electronic alert OR electronic surveillance OR clinical decision support OR automated alert) AND (comparative OR randomized OR trial OR before-after OR interrupted time series) AND (1917/01/01:2021/12/31[dp])
   ```

### Retrieval and screening approach

Searches returned multiple candidate records on sepsis surveillance, electronic alerts, and clinical decision support. Titles/abstracts and available record sections were screened against the prespecified criteria.

### Eligibility criteria applied explicitly

#### Inclusion criteria
Primary comparative studies were eligible if they met all of the following:
- **Population:** hospitalized adults with sepsis or at risk for sepsis; pediatric populations excluded
- **Intervention:** automated sepsis alerting system integrated into the EHR
- **Algorithm type:** rule-based and machine-learning-based methods both eligible
- **Comparator:** usual care or standard practice without automated alert messages
- **Outcomes:** mortality and/or length of stay, including hospital mortality, ICU LOS, and hospital LOS

#### Exclusion criteria
Records were excluded if they were:
- reviews or commentaries
- animal studies
- case reports
- pediatric studies
- prediction-model development studies without comparative alert implementation
- non-sepsis-target studies
- non-relevant interventions such as antimicrobial susceptibility testing
- studies focused on irrelevant targets such as delirium or acute kidney injury
- noncomparative implementations without a usable usual-care/preimplementation comparator

---

## Retrieval and Screening Results

### Search yield

Each of the three local corpus queries returned **20 candidate records**. The combined retrieval set included adult hospital studies from emergency department, inpatient ward, ICU-related, and hospital-wide contexts.

### Screening summary

The retrieved set contained:
- relevant comparative adult sepsis alert studies
- noninterventional prediction-model studies
- reviews/protocols/commentaries
- non-sepsis alert papers
- records outside the clinical scope of the review

The research notes indicated that **comparative evidence was dominated by rule-based systems**, and that **machine-learning-based comparative intervention studies were not clearly identified as eligible in the corpus through 2021**.

### Included studies

Based on the available retrieved record details, **4 studies were explicitly confirmed as meeting the eligibility criteria**.

Because the provided research findings were truncated for some additional candidate records, only studies with clearly documented inclusion decisions and sufficient eligibility verification are counted here.

---

## Included Studies and Key Characteristics

| Corpus ID | Study title | Setting | Design | Alert method | Comparator | Main outcomes |
|---|---|---|---|---|---|---|
| **118963** | *Impact of an emergency department electronic sepsis surveillance system on patient mortality and length of stay* | Emergency department | Interrupted time series | Rule-based EHR surveillance/interruptive alert | Pre-alert vs post-alert | In-hospital mortality, hospital LOS |
| **2936** | *Electronic health record-based clinical decision support alert for severe sepsis: a randomised evaluation* | Inpatient wards, non-ICU | Randomized comparative evaluation | Rule-based CDS alert | Silent alert/usual care vs live alert | Mortality, LOS, ICU transfer |
| **2940** | *Development, implementation, and impact of an automated early warning and response system for sepsis* | Adult non-ICU acute inpatient units | Pre/post with multivariable adjustment | Rule-based early warning/response system | Preimplementation vs postimplementation | Mortality, ICU LOS, hospital LOS |
| **2944** | *Managing sepsis: Electronic recognition, rapid response teams, and standardized care save lives* | Hospital-wide: ED, ICU, wards | Retrospective before/after | Rule-based EHR surveillance plus alerting program | Before vs after implementation | Inpatient mortality, ICU LOS, hospital LOS |

---

## Findings by Study

### 1) Emergency department electronic surveillance system  
**Study:** [Impact of an emergency department electronic sepsis surveillance system on patient mortality and length of stay](metasyn://corpus/118963) [1]  
**Corpus ID:** **118963**

#### Eligibility basis
- Adult emergency department patients with severe sepsis or septic shock
- EHR-based automated sepsis alert
- Comparative design: patient-level interrupted time series before/after implementation
- Relevant outcomes: in-hospital mortality and LOS

#### Key details
- Study period: January 2013 to April 2015
- Intervention introduced: February 2014
- Alerts were triggered by abnormal vital signs or laboratory results

#### Main results
- Mean LOS decreased from **10.1 to 8.6 days** after alert introduction
- Adjusted time-series analysis found a **16% LOS reduction** (95% CI 5% to 25%; P=.007)
- **No effect on mortality**
- The alert had **80.4% sensitivity** and **14.6% positive predictive value**

#### Interpretation
This study suggests that a rule-based ED alert may improve **length of stay**, but not **mortality**. The authors noted likely **alert fatigue** related to low PPV, arguing that simple vital sign/laboratory rules may be insufficient to improve major clinical outcomes.

#### Evidence availability
- **Abstract-only evidence** was available from the retrieved record.

---

### 2) Randomized severe sepsis CDS alert on inpatient wards  
**Study:** [Electronic health record-based clinical decision support alert for severe sepsis: a randomised evaluation](metasyn://corpus/2936) [2]  
**Corpus ID:** **2936**

#### Eligibility basis
- Adults aged >18 years
- Hospitalized on medical and surgical inpatient wards
- ICU excluded
- EHR-generated severe sepsis alert
- Comparator: live alert versus silent alert/usual care
- Mortality and LOS reported

#### Key details
- Single-center patient-level randomized study
- 1,123 adult inpatients
- Conducted November 2014 to March 2015
- Alert was based on modified severe sepsis criteria using vital signs, labs, and physician orders
- Intervention alerts were sent to the crisis nurse and primary physician team

#### Main results
No significant differences were found between intervention and control groups for:
- new antibiotic orders within 3 hours
- intravenous fluid administration
- lactate ordering
- large-volume fluid resuscitation
- **in-hospital mortality at 30 days**
- **LOS >72 hours**
- ICU transfer within 48 hours

#### Interpretation
This randomized study did **not** show benefit of inpatient ward sepsis alerting on either mortality or LOS. Among the included studies, this is the strongest design for causal inference and weighs against a large outcome effect from simple rule-based alerting in ward patients.

#### Evidence availability
- Methods and results sections were available from the local corpus record.

---

### 3) Automated early warning and response system in non-ICU inpatients  
**Study:** [Development, implementation, and impact of an automated early warning and response system for sepsis](metasyn://corpus/2940) [3]  
**Corpus ID:** **2940**

#### Eligibility basis
- Adult non-ICU inpatients admitted to acute inpatient units
- Automated EHR monitoring of labs and vital signs in real time
- Comparative pre/post study
- Relevant mortality and LOS outcomes

#### Key details
- The system notified providers, nurses, and a rapid response coordinator when patients had at least four predefined abnormalities
- Bedside evaluation was triggered after notification
- Analysis included multivariable adjustment

#### Main results
- **Hospital LOS and ICU LOS were similar** in pre- and postimplementation periods
- All mortality measures were lower after implementation, but **none reached statistical significance**
- The intervention improved early sepsis care processes and documentation

#### Interpretation
This study suggests that EHR-based rule-triggered surveillance may improve recognition and care processes, but evidence for improvement in mortality or LOS remained **suggestive rather than definitive**.

#### Evidence availability
- Results were available from the retrieved record; outcome reporting appeared more complete than abstract-only records, but detailed numeric effect sizes for mortality/LOS were not fully available in the provided findings.

---

### 4) Hospital-wide electronic recognition and response program  
**Study:** [Managing sepsis: Electronic recognition, rapid response teams, and standardized care save lives](metasyn://corpus/2944) [4]  
**Corpus ID:** **2944**

#### Eligibility basis
- Adult patients only
- Included all units: ED, ICU, and general wards
- Automated EHR surveillance for possible sepsis
- Comparative before/after implementation
- Mortality and LOS were prespecified outcomes

#### Key details
- Retrospective review of sepsis patients treated from October 1, 2013 to November 10, 2015
- Automated surveillance applied an adjusted Modified Early Warning Signs–Sepsis Recognition Score
- For patients meeting threshold criteria, a possible sepsis page was sent to the responsible provider; ward rapid response nurses were also paged

#### Main outcomes reported in the retrieved record
- **Primary outcome:** inpatient mortality
- **Secondary outcomes:** included ICU LOS and hospital LOS

The available findings confirm inclusion and outcome relevance, but the excerpt provided did not preserve the complete numerical results.

#### Interpretation
This was a broad hospital-wide, real-world sepsis alert-and-response implementation spanning multiple settings. It is especially relevant to the review question on setting variation, but detailed effect-size extraction for mortality and LOS was limited by the available record excerpt.

#### Evidence availability
- Partial methods/results information was available.
- Full numerical results were not fully preserved in the provided findings excerpt.

---

## Synthesis of the Evidence

## Overall Effect on Mortality

Across the explicitly included studies, the most consistent finding is that **automated EHR-integrated sepsis alerts did not produce a clear or statistically robust reduction in mortality**.

- The ED interrupted time-series study found **no mortality effect** [1].
- The randomized inpatient ward study found **no difference in in-hospital mortality** [2].
- The non-ICU early warning/response system study reported mortality measures trending lower, but **not statistically significant** [3].
- The hospital-wide implementation study included mortality as its primary endpoint, but the available evidence excerpt did not preserve full numeric results [4].

### Bottom line on mortality
The available local-corpus evidence through 2021 does **not establish that automated sepsis alerts reliably reduce mortality** compared with usual care.

---

## Overall Effect on Length of Stay

The evidence for LOS is **mixed**.

- In the emergency department study, LOS improved meaningfully, with a reported **16% adjusted reduction** [1].
- In the randomized ward trial, there was **no LOS benefit** [2].
- In the non-ICU early warning/response study, **hospital and ICU LOS were similar** before and after implementation [3].
- The hospital-wide study reported ICU LOS and hospital LOS as secondary outcomes, but full numerical results were not retained in the available findings excerpt [4].

### Bottom line on LOS
Automated alerting may improve LOS in some settings, particularly the **emergency department**, but the overall evidence is inconsistent and does not show a uniform benefit across hospitalized adults.

---

## Variation by Clinical Setting

### Emergency Department
The strongest setting-specific signal of benefit came from the **ED** study:
- reduced hospital LOS
- no mortality improvement

This pattern may indicate that alerts can accelerate recognition and management earlier in the patient journey, improving throughput without clearly changing survival.

### Hospital Wards / Non-ICU Inpatients
The evidence from ward and non-ICU studies was mostly negative or inconclusive:
- randomized ward trial: no mortality or LOS benefit [2]
- non-ICU pre/post study: no significant mortality or LOS improvement [3]

This suggests that alerts on general wards may improve process measures more readily than hard outcomes.

### ICU
The review question prioritized ICU evidence, but the local-corpus evidence identified here did **not** yield a clearly eligible **ICU-specific comparative study with extractable mortality/LOS findings** among the explicitly included records. One hospital-wide study included ICU patients [4], but it was not ICU-only.

### Hospital-wide Programs
Hospital-wide alerting systems are operationally attractive and may integrate escalation pathways more effectively than alerts alone, but the available local-corpus evidence remained limited and incompletely extractable for hard outcomes.

### Bottom line by setting
- **ED:** some evidence of LOS benefit
- **Wards/non-ICU:** mostly no clear mortality or LOS benefit
- **ICU:** insufficient setting-specific comparative evidence in the explicitly included set
- **Hospital-wide:** potentially promising, but hard-outcome evidence was incomplete

---

## Variation by Prediction Method

### Rule-based systems
All explicitly included studies used **rule-based** detection logic, generally built from:
- vital signs
- laboratory thresholds
- early warning score components
- combinations of sepsis criteria and physician-order triggers

### Machine-learning systems
The search strategy explicitly targeted machine-learning studies. However, the research findings indicated that:
- machine-learning-related records were found
- the key machine-learning candidate identified was **noninterventional**
- comparative intervention evidence for ML-based sepsis alerting was **not clearly eligible** in the local corpus through 2021

### Bottom line by prediction method
The local corpus evidence available for comparative review through 2021 was **almost entirely rule-based**. As a result:
- **no meaningful rule-based versus machine-learning effectiveness comparison** could be performed
- the review question’s ML subgroup remains effectively **unanswered** within the eligible corpus evidence

---

## Can a Meta-analysis Be Performed From the Retrieved Evidence?

A formal quantitative meta-analysis would be difficult and likely inappropriate based on the retrieved evidence alone, for several reasons:

1. **Heterogeneous study designs**
   - randomized trial
   - interrupted time series
   - before/after studies
   - retrospective implementation studies

2. **Clinical heterogeneity**
   - ED-only populations
   - ward/non-ICU populations
   - hospital-wide mixed settings
   - variable baseline sepsis severity

3. **Intervention heterogeneity**
   - different alert thresholds
   - different recipient workflows
   - different linked response systems
   - some alerts were interruptive pages, others triggered coordinated bedside evaluation

4. **Incomplete numeric outcome reporting in the available records**
   - several studies were available only in abstract or partial-record form
   - sufficient event counts or summary statistics for pooled mortality/LOS analysis were not consistently available

5. **Sparse number of eligible studies with extractable outcome data**
   - only four studies were explicitly confirmed as included from the available findings
   - only one provided a clear adjusted LOS effect estimate

### Practical conclusion on meta-analysis
A **structured qualitative synthesis** is supported by the local corpus evidence. A rigorous pooled meta-analysis of mortality or LOS is **not well supported** by the available extractable data from the retrieved records.

---

## Risk-of-Bias and Evidence Limitations

## Study-level limitations

### Nonrandomized designs
Three of the four included studies were pre/post or interrupted time-series designs, making them vulnerable to:
- secular trends
- co-interventions
- changes in sepsis protocols
- staffing or workflow changes over time

### Alert implementation complexity
In several studies, the intervention was not just an alert but part of a broader response package:
- paging systems
- rapid response involvement
- bedside evaluation pathways
- documentation and order-set changes

This makes it harder to isolate the independent effect of the alert itself.

### Alert performance issues
The ED study reported a **low positive predictive value**, raising concern for:
- alert fatigue
- desensitization
- workflow burden

### Outcome reporting limitations
Some records did not preserve all numeric effect estimates for mortality and LOS, limiting comparability.

## Review-level limitations

### Restricted retrieval source
Only the local MetaSyn PubMed corpus was searched, as required. No external databases were used.

### Evidence sometimes abstract-only
At least one included study relied on **abstract-only evidence** from the local corpus record [1]. This limits extraction detail and risk-of-bias assessment.

### Incomplete full-text availability in retrieved sections
Several findings came from selected methods/results sections rather than complete full texts.

### Sparse ML evidence
Although ML studies were specifically sought, no clearly eligible comparative ML alert intervention study was confirmed among the included records. The method-comparison objective therefore remained underpowered.

### Adult-only framing
This review excluded pediatric populations by design, so findings should not be generalized to children.

---

## Overall Conclusion

Using only the local MetaSyn PubMed corpus through 2021-12-31, the evidence does **not** show a consistent improvement in **mortality** from automated EHR-integrated sepsis alerting systems compared with usual care in hospitalized adults with sepsis or at risk for sepsis.

The evidence for **length of stay** is mixed:
- one emergency department study found a meaningful reduction in LOS
- ward and non-ICU studies generally did not show clear LOS benefit

The eligible comparative evidence was overwhelmingly based on **rule-based** alert systems. No firm conclusion can be drawn about whether **machine-learning-based alerts** perform better than rule-based systems, because clearly eligible comparative ML intervention studies were not confirmed in the retrieved corpus.

By setting, the most favorable signal appeared in the **emergency department**, while inpatient ward/non-ICU results were largely neutral. ICU-specific comparative evidence remained insufficient in the explicitly included set.

Overall, the local-corpus evidence supports a cautious conclusion: **automated sepsis alerts may improve process measures and may shorten LOS in some contexts, but they have not been shown consistently to improve mortality or length of stay across hospital settings.**

---

## Included-Study List

1. **Impact of an emergency department electronic sepsis surveillance system on patient mortality and length of stay** — **Corpus ID: 118963**  
2. **Electronic health record-based clinical decision support alert for severe sepsis: a randomised evaluation** — **Corpus ID: 2936**  
3. **Development, implementation, and impact of an automated early warning and response system for sepsis** — **Corpus ID: 2940**  
4. **Managing sepsis: Electronic recognition, rapid response teams, and standardized care save lives** — **Corpus ID: 2944**

### Sources
[1] Impact of an emergency department electronic sepsis surveillance system on patient mortality and length of stay: metasyn://corpus/118963  
[2] Electronic health record-based clinical decision support alert for severe sepsis: a randomised evaluation: metasyn://corpus/2936  
[3] Development, implementation, and impact of an automated early warning and response system for sepsis: metasyn://corpus/2940  
[4] Managing sepsis: Electronic recognition, rapid response teams, and standardized care save lives: metasyn://corpus/2944