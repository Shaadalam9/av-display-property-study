# Optimisation and personalisation of AV visualisation parameters (Bayesian / preferential BO) and individual differences in display preferences

Compiled 2026-10-26. Sources were read through arXiv HTML pages, author PDFs and publisher pages. Anything marked UNVERIFIED was not checked against a primary source in this session.

## Q1. OptiCarVis and related Colley / Jansen / Rukzio MOBO work on AV visualisations: parameters, objectives, iterations, results

### Takeaway
OptiCarVis tuned **16 parameters**: 7 on/off visibility toggles plus 9 continuous alpha and size values, applied to 7 visualisation elements. Colour and position were held fixed on purpose. The parameters came from prior AV-visualisation work. On safety, trust, predictability and cognitive load, the MOBO-optimised designs beat both the one-size-fits-all expert design and the users' own custom designs. Final parameter values varied widely between participants, and a 2026 multi-session follow-up found that this between-person spread persisted. Both papers therefore point to personalised rather than uniform optima.

### Cited Findings
**Citation:** Jansen, P., Colley, M., Krauß, S., Hirschle, D., Rukzio, E. (2025). *OptiCarVis: Improving Automated Vehicle Functionality Visualizations Using Bayesian Optimization to Enhance User Experience.* CHI '25, Article 85, 23 pp. DOI 10.1145/3706598.3713514. It won a CHI 2025 Honorable Mention. — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1); [Ulm HCI awards](https://www.uni-ulm.de/en/in/mi/hci/awards)

**Parameters (Table 1, quoted as reported):**

| # | Parameter | Range |
|---|---|---|
| p1 | Semantic segmentation visibility | Bool [0,1] |
| p2 | Semantic segmentation alpha | [0.1, 1] |
| p3 | Pedestrian intention visibility | Bool [0,1] |
| p4 | Pedestrian intention size | [0.1, 0.2] |
| p5 | Trajectory visibility | Bool [0,1] |
| p6 | Trajectory alpha | [0.1, 1] |
| p7 | Trajectory size | [0.1, 0.6] |
| p8 | Ego trajectory visibility | Bool [0,1] |
| p9 | Ego trajectory alpha | [0.1, 1] |
| p10 | Ego trajectory size | [0.1, 0.6] |
| p11 | CAD-covered area visibility | Bool [0,1] |
| p12 | CAD-covered area alpha | [0.1, 1] |
| p13 | CAD-covered area size | [0.2, 0.8] |
| p14 | Occluded cars visibility | Bool [0,1] |
| p15 | Vehicle status HUD visibility | Bool [0,1] |
| p16 | Vehicle status HUD alpha | [0.1, 1] |

Source: [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1).

Two inconsistencies in the paper:
- The table labels p4 as an alpha value, although the name says size.
- Section 5.1.1 refers to "nine continuous design parameters" with five levels each. — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**How the parameters were chosen and justified:**
- Elements came from prior AV visualisation work: Kunze et al. 2018; Colley et al. 2020, 2021a, 2022b, 2024b; Müller et al. 2022; Currano et al. 2021; Riegler et al. 2019. The element set builds on Colley et al.'s functional split into "Situation Detection", "Situation Prediction" and "Trajectory Planning". — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)
- Visibility was modelled as a continuous value and thresholded at 0.5, because BO works more efficiently on continuous parameters. — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)
- Size bounds keep elements from becoming invisible or overlapping. Alpha starts at 0.1 because elements are nearly invisible below that. — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)
- Excluded on purpose:
  - RGB colour, to avoid unintended meanings such as orange read as a warning.
  - Positions of the CAD spheres and the HUD.
  - Rotations, which are set by object orientation.
  - Alpha for occluded cars, which are a simple outline.
  - Alpha for pedestrian intention, to avoid dark-blue/cyan confusion.

  — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**Objectives:**
- Maximised: perceived safety, trust (Körber TiA items), predictability, acceptance, aesthetics.
- Minimised: cognitive load (NASA-TLX mental subscale).
- All six were normalised to [−1, 1].

— [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**Optimiser setup:**
- BoTorch 0.9.2, multi-output GP, qEHVI with q = 1, 512 MC samples.
- Settings follow Chan et al. 2022.
- Iterations: 5 sampling + 10 optimisation = 15 for cold start; 10 for warm start.
- Early stopping triggers if all objectives are rated at maximum.

— [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**Study design:**
- N = 117, Prolific, US participants, between-subjects. Group sizes: C1 21, C2 19, C3 19, C4 18, C5 22, C6 18.
- C1: no visualisation.
- C2: expert "one-size-fits-all" design, the mean of 8 experts' parameter settings.
- C3: end-user custom design.
- C4: cold-start MOBO.
- C5: warm start from the expert design.
- C6: warm start from the participant's own custom design.
- Optimisation used a 33 s simulated drive; final ratings used a 3 min drive.

— [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**Results:**
- Perceived safety: C4 M = 1.32, C5 0.95 and C6 0.74 were better than C2 (−0.25) and/or C3 (−0.70).
- Cognitive load: lower in C4–C6 than in C2 and C3.
- Trust: C4 (3.94) and C5 (3.95) were higher than C2 (3.04).
- Predictability: C4 (4.03) beat C1–C3.
- Acceptance and aesthetics: not significant (acceptance p = 0.073). The abstract nonetheless claims improved acceptance.
- No differences among C4–C6, so warm start gave no advantage and H2 was rejected.
- 12 of 57 HITL participants (21.05%) hit the perfect-score early stop.

— [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**Individual differences in the optima (Sec. 5.2):**
- The HITL conditions showed wider confidence intervals on final parameters than the custom-design condition. The authors read this as "a broad range of preferences not captured in the initial custom design phase."
- Many elements ended up switched off under MOBO, especially in the cold start.
- Custom designs tended to keep elements on (alpha often > 0.7), possibly "out of curiosity". MOBO designs hovered around alpha ≈ 0.5.
- Pedestrian-intention size showed especially diverse preferences.
- Some participants turned the HUD on while most did not, and "the intervals do not fully capture each user's unique choices."

— [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**Dimensionality:** The authors did not plot the Pareto front because 16 dimensions are hard to visualise. They also warn that an interface exposing all parameters "could become overwhelming" and that frequent queries cause fatigue. — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)

**Follow-up study:** Colley, M., Jansen, P., Krauss, S., Rukzio, E. (2026). *Multi-Session User Experience Assessments of Computationally Optimized Automated Vehicle Functionality Visualizations.* Accepted to AutomotiveUI 2026; DOI listed as 10.1145/3828157.3828785. — [arXiv 2607.28552](https://arxiv.org/abs/2607.28552)
- Design: same 16 parameters and ranges, N = 74, US, three consecutive days. On day 1, C4 ran 15 iterations and C5/C6 ran 10. On days 2 and 3, one MOBO round per day, compared with a frozen day-1 design. The paper also states "20 iterations on day one", which conflicts with this. — [arXiv 2607.28552](https://arxiv.org/html/2607.28552)
- Results with continued MOBO: lower cognitive load, and higher aesthetics (5.97 vs 4.83), usefulness (6.29 vs 4.93), satisfying (6.13 vs 4.59) and ownership (6.00 vs 3.80). Cold start beat the static expert and custom designs on trust, predictability and safety. — [arXiv 2607.28552](https://arxiv.org/html/2607.28552)
- Warm start: C5 reached about 95% of its day-1 gain in about 7 evaluations, with no final-design advantage. — [arXiv 2607.28552](https://arxiv.org/html/2607.28552)
- Between-participant dispersion of final designs "stayed substantial across days", meaning the optimiser converged to personalised designs. The authors call this analysis preliminary because the logs are incomplete. — [arXiv 2607.28552](https://arxiv.org/html/2607.28552)
- The authors acknowledge limits of optimising subjective measures: inconsistency, fatigue, single-item measures. — [arXiv 2607.28552](https://arxiv.org/html/2607.28552)

### Inferences
- OptiCarVis's parameter types (visibility, opacity, size per element) are a direct precedent for a path ribbon, road-user highlights and labels. Its decision to exclude colour on semantic grounds is a precedent to cite if colour is dropped, or to argue against explicitly if colour is kept.
- OptiCarVis used multi-objective rating-based BO, not pairwise preferential BO. Its 16-D space with 10–15 evaluations per person is very sparse coverage. That 21% early-stopped and that many elements were switched off suggests the optimiser largely explored on/off structure. A 4-parameter pairwise study is a deliberately lower-dimensional design.
- The wide between-person spread of optima in both papers is the most direct AV-specific evidence that personalisation is warranted.

### Gaps
- Per-parameter statistics on between-participant variance (Figure 10 values) were not extracted. The papers give no ranking of which of the 16 parameters mattered most.
- I did not verify the published DOI of the AutomotiveUI 2026 paper against the ACM DL.

## Q2. Human-in-the-loop and preferential BO in HCI: how many parameters were tractable, and guidance on dimensionality

### Takeaway
Human-in-the-loop BO studies in HCI typically use 2–7 parameters when each query is a pairwise comparison or a single slider. Higher dimensions (10–16) appear only with richer queries such as plane or gallery search, with priors or warm starts, or with rating-based multi-objective BO, and even then with caveats. Pairwise comparison alone is repeatedly described as slow to converge, which argues for keeping a pairwise study to about 4 dimensions.

### Cited Findings
**Chan et al. (2022):** Chan, L., Liao, Y.-C., Mo, G. B., Dudley, J. J., Cheng, C.-L., Kristensson, P. O., Oulasvirta, A. *Investigating Positive and Negative Qualities of Human-in-the-Loop Optimization for Designing Interaction Techniques.* CHI '22. DOI 10.1145/3491102.3501850. — [Aalto project page](https://userinterfaces.aalto.fi/dit/); [PDF](https://www.pokristensson.com/pubs/ChanEtAlCHI2022.pdf)
- Task: 3D touch (Go-Go) design with **4 continuous parameters**: x1 Distance Threshold D, x2 Scale Factor k, x3 Activation-Vibration Gap G, x4 Vibration Amplitude A. The activation point ranged from 15 cm before to 5 cm beyond the target, and amplitude was capped at 2.6 g. Two objectives: completion time and spatial error. — [PDF](https://www.pokristensson.com/pubs/ChanEtAlCHI2022.pdf)
- Optimiser: BoTorch, multi-output GP, qEHVI with q = 1, 10 restarts, 1024 restart candidates, 512 MC samples. Each designer evaluated **40 designs, the first 10 random**. Designer-led participants tried up to 830 designs. N = 40 novice designers, between-subjects. — [PDF](https://www.pokristensson.com/pubs/ChanEtAlCHI2022.pdf)
- The paper names three strategies for taming parameter spaces:
  1. Assign or eliminate parameters using the literature, e.g. HiveFive narrowed its ranges from theory and fixed values in a 3-person pilot.
  2. Divide and conquer, one parameter at a time.
  3. Reduce dimensionality with a model, e.g. ErgonomicsTouch reduced to 4 curve parameters with bounds set in a 5-user pilot.

  It also notes that transfer functions need "two to ten" parameters. — [PDF](https://www.pokristensson.com/pubs/ChanEtAlCHI2022.pdf)
- Results, from the Aalto press release (not checked against the paper's numbers): designers found better solutions with optimiser help, especially novices, but reported less creativity and ownership. — [Aalto news](https://aalto.fi/en/news/designers-find-better-solutions-with-computer-assistance-but-sacrifice-creative-touch)

**Koyama et al. (2017):** Koyama, Y., Sato, I., Sakamoto, D., Igarashi, T. *Sequential Line Search for Efficient Visual Design Optimization by Crowds.* ACM TOG 36(4) 48 (SIGGRAPH 2017). DOI 10.1145/3072959.3073598. — [preprint](https://koyama.xyz/project/sequential_line_search/download/preprint.pdf)
- The paper argues that pairwise comparison (Brochu et al. 2007) yields little information per query, so many iterations are needed. It replaces pairwise queries with 1-D slider queries to crowd workers.
- Design spaces: photo enhancement **6-D**; BRDF **3-D and 7-D**. Results are shown after **15 iterations**, with **7 microtasks per iteration**. Photo results approached similar enhancement after the "first 4 or 5 iterations".
- It reports that Brochu et al. 2010 handled **4- and 12-D** animation spaces only by adding domain-specific prior knowledge.
- The authors explicitly ignore demographic differences in preference, citing Reinecke & Gajos 2014.

— [preprint](https://koyama.xyz/project/sequential_line_search/download/preprint.pdf)

**Koyama, Sato, Goto (2020):** *Sequential Gallery for Interactive Visual Design Optimization.* ACM TOG 39(4) (SIGGRAPH 2020); DOI not verified here.
- Plane search (2-D subspace per query) on 10-D and 12-D problems. Users were satisfied after about 4–10 iterations.
- On synthetic 5-D, 10-D and 15-D functions it was significantly better than line search. In the first few iterations of high-D problems the BO "performed almost pure exploration".
- Brochu's pairwise method was omitted from the comparison because it "consistently requires much more iterations".

— [arXiv 2005.04107](https://arxiv.org/pdf/2005.04107)

**Dudley, Jacques, Kristensson (2019):** *Crowdsourcing Interface Feature Design with Bayesian Optimization.* CHI '19, 1–12. DOI 10.1145/3290605.3300482. Crowdsourced BO refined interface features for 2D map search, mobile VR and web AR. — [Cambridge repository](https://www.repository.cam.ac.uk/items/f31bc7b9-535b-44a5-b913-248b7f4feac7); [St Andrews portal](https://research-portal.st-andrews.ac.uk/en/publications/crowdsourcing-interface-feature-design-with-bayesian-optimization/). The number of parameters and workers is UNVERIFIED.

**Liao et al. (2024):** Liao, Y.-C., Mo, G. B., Dudley, J. J., Cheng, C.-L., Chan, L., Kristensson, P. O., Oulasvirta, A. *Practical approaches to group-level multi-objective Bayesian optimization in interaction technique design.* Collective Intelligence 3(1). DOI 10.1177/26339137241241313. It proposes deriving a group design from individual optimisation data and using group data to initialise optimisation for new users. — [Aalto](https://aaltodoc.aalto.fi/items/5cceb0f1-3be8-4d3b-a798-ec505eb5297e/full)

**Liao et al. (2023):** *Interaction design with multi-objective Bayesian optimization.* IEEE Pervasive Computing 22(1), 29–38. Content UNVERIFIED; citation taken from a search snippet only.

**Li, Liao, Holz (2025):** *Efficient Visual Appearance Optimization by Learning from Prior Preferences* (Meta-PO). UIST '25.
- The paper says pure preferential BO needs many comparison rounds, which suits designers more than everyday users.
- Meta-PO learns from prior users' preference models and reached satisfactory results in **5.86 iterations** when a user's goal matched the population's, and about **8** when goals diverged.
- The number of parameters was not extracted.

— [arXiv 2507.15355](https://arxiv.org/abs/2507.15355)

### Inferences
- **Pairwise precedents:** Brochu 2007 (about 3-D) and SLS (3–7-D) set a precedent of single-digit dimensionality. Pairwise answers carry less information per query than slider or plane queries. With roughly 15–30 comparisons per crowd worker, 4 parameters sits in the well-supported range. 10+ dimensions has been viable only with richer query types or priors.
- **Warm start:** Population priors (Meta-PO, Liao 2024 group initialisation) are a documented way to cut per-person iterations, and they suit a crowdsourced study that first pools data. OptiCarVis, however, found no final-design benefit from warm start.

### Gaps
- I found no paper giving a formal rule for the number of dimensions per number of pairwise comparisons. Brochu et al. 2007 (NIPS) and González et al. 2017 *Preferential Bayesian Optimization* (ICML) were not checked directly in this session (UNVERIFIED).
- The exact parameter counts in Dudley et al. 2019 and Meta-PO were not extracted.

## Q3. Evidence of individual differences in AV HMI and display preferences

### Takeaway
There is direct experimental evidence that preferred information amount depends on initial trust (Hartwich et al. 2021), and OptiCarVis shows widely spread optimal parameter values. Evidence on age and gender is mostly about acceptance, trust and information sources rather than display-parameter preferences. I found no study linking specific display parameters to age, gender or culture.

### Cited Findings
**Hartwich, F., Hollander, C., Johannmeyer, D., Krems, J. F. (2021).** *Improving Passenger Experience and Trust in Automated Vehicles Through User-Adaptive HMIs: "The More the Better" Does Not Apply to Everyone.* Frontiers in Human Dynamics 3. DOI 10.3389/fhumd.2021.669030. — [Frontiers](https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2021.669030/full)
- Design: driving simulator, N = 50 first-time users aged 20–38. Three within-subjects conditions:
  - no HMI;
  - a permanent full HMI with traffic overview and manoeuvre announcement;
  - a context-adaptive HMI, where the full mode appeared in only 9 complex situations (about 26% of the ride).
- Trust groups were formed by a median split on initial trust (Mdn = 65/100).
- HMI × trust-group interactions were significant for perceived safety (p = .042), understanding (p = .010), comfort (p = .025) and UEQ attractiveness (p = .025).
  - The lower-trust group did best with the permanent full information.
  - The higher-trust group did best with the adaptive, reduced HMI.
  - There was no interaction on trust itself.
- The authors conclude that permanent full information "cannot be recommended as a universal standard". The sample skewed young and female, so age and gender could not be analysed.

**Other individual-difference findings:**
- OptiCarVis between-participant spread (see Q1). — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1); [arXiv 2607.28552](https://arxiv.org/html/2607.28552)
- Driver age may limit how far AV explanations build trust. — [Sustainability 13(4) 1948, "Drivers' Age and Automated Vehicle Explanations", DOI 10.3390/su13041948](https://doi.org/10.3390/su13041948). Authors and details were not read (UNVERIFIED beyond the search summary).
- Greenwood & Baldwin (2022), Frontiers in Psychology, N = 404:
  - Age affected preferred information sources about automation; gender did not.
  - Older respondents and women felt less technically sophisticated.
  - Men reported greater subjective understanding but had no greater objective knowledge.

  — [PMC9169717](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9169717/)
- Hoff & Bashir's trust model, as summarised by others (UNVERIFIED as a primary read): dispositional factors such as culture and age, and learned factors such as experience, affect trust in automation. — cited via [Hartwich et al. 2021](https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2021.669030/full)
- Koyama et al. 2017 explicitly set aside demographic preference differences, citing Reinecke & Gajos 2014, which showed demographic differences in visual-appeal judgements of websites. — [SLS preprint](https://koyama.xyz/project/sequential_line_search/download/preprint.pdf)

### Inferences
- **Amount of information:** The strongest justification for personalising "amount or visibility of information" properties (number of highlights, labels, ribbon presence) is trust-dependent preference (Hartwich 2021) plus OptiCarVis's spread of on/off and size optima. Measuring propensity to trust as a covariate is well motivated.
- **Age, gender, culture:** Effects on specific display properties are plausible but not established. They should be framed as exploratory moderators.

### Gaps
- I found no AV-specific study tying age, gender, culture or experience to preferred values of particular visual properties (opacity, colour, label density, timing).
- I did not obtain cross-cultural AV HMI display-preference evidence. OptiCarVis lists other cultures as future work.

## Q4. Studies that ranked or screened visual properties by importance before optimisation (expert workshops, MaxDiff/BWS, conjoint)

### Takeaway
No reviewed BO study ran a formal importance screening (MaxDiff/BWS or conjoint) of HMI properties before optimising. Parameter sets were chosen from prior literature plus designer judgement, sometimes narrowed by small pilots, and in OptiCarVis expert input supplied default values but did not select the parameters. Conjoint and BWS have been used for AV purchase attributes and driving styles, not for in-cabin display features.

### Cited Findings
- **OptiCarVis:** parameters came from prior work. Eight experts supplied parameter values, averaged into the C2 design and the C5 warm start, but did not rank which parameters to include. — [arXiv 2501.06757](https://arxiv.org/html/2501.06757v1)
- **Chan et al. 2022:** surveys how CHI systems fix parameter spaces: from literature and theory, 3- to 5-person pilots, divide-and-conquer, or model-based reduction. — [PDF](https://www.pokristensson.com/pubs/ChanEtAlCHI2022.pdf)
- **Conjoint and BWS in AV research** target purchase or acceptance attributes rather than HMI elements:
  - a Japanese BWS study with 1,048 drivers on automation level, price, running cost and range — [IAEE abstract](https://iaee.org/en/publications/proceedingsabstractpdf.aspx?id=17145);
  - a BWS study of driving-style preferences — [DLR elib 106517](https://elib.dlr.de/106517);
  - choice-based conjoint segmenting buyers of self-driving cars — [Marketing & Menedzsment](https://journals.lib.pte.hu.testing.qulto.eu/index.php/mm/article/view/6731).

  Details beyond the search summaries were UNVERIFIED.
- **Closest HMI example:** 900 Korean drivers ranked the top-3 most useful eHMI message types per scenario. Preferred messages varied by scenario. This is a ranking design, not BWS, and covers external rather than in-cabin HMI. — [AHFE 2025 open access](https://openaccess.cms-conferences.org/publications/book/978-1-964867-62-5/article/978-1-964867-62-5_32)

### Inferences
- A BWS or MaxDiff screening of candidate display properties (ribbon, highlights, labels, colours, timing), or a short pilot comparing importance or preference variance, would be novel relative to the BO literature reviewed here. It would also be a stronger justification than choosing from the literature alone.
- **Selection criterion:** Chan et al.'s framing supports choosing about 4 properties by (a) prior-work relevance, (b) expected between-person variance, since only high-variance properties benefit from personalisation, and (c) independence and absence of semantic constraints, which is the logic OptiCarVis used to exclude colour.

### Gaps
- I found no published MaxDiff, BWS or conjoint study on in-vehicle AV explanation-display features. The search was limited to two queries, so this absence is not conclusive.
