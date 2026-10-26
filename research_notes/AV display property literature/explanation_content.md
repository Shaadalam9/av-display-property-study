# Explanation content properties for occupants of automated vehicles

Scope: what information explanation and transparency displays show to AV occupants, how much of it, and the measured effects. Sources were checked on 2026-10-26. When a full text was read, the note says so. Items labelled "UNVERIFIED (secondary)" come only from search snippets or citing papers, and should be checked before they are cited in a paper.

## Q1. Explanation type: "why" vs "how/what", reason-for-action vs descriptive

### Takeaway
The best-controlled evidence (Koo et al. 2015) finds that "why" (reason) messages are preferred and raise acceptance. "How/what"-only messages are the worst for driving behaviour. "How + why" gives the safest driving but more negative feelings. This is an early inverted-U signal for message amount. Explanation timing matters at least as much as content: explanations given before the action raise trust, and explanations given after the action do no better than none (Du et al. 2019). Explanations for take-over requests (TORs) improve perceived understanding but not trust.

### Cited Findings
- **Koo, Kwac, Ju, Steinert, Leifer & Nass (2015).** "Why did my car just do that? Explaining semi-autonomous driving actions to improve driver understanding, trust, and performance." *Int. J. Interactive Design and Manufacturing* 9(4). DOI 10.1007/s12008-014-0227-2. (full text read) — [PDF](https://www.wendyju.com/publications/WhyDidMyCarJustDoThat.pdf)
  - **Design:** 2 (why: yes/no) x 2 (how: yes/no) between-subjects. N = 64 university students (32 M, 32 F, aged 18–27, mean 21.1), in a STISIM simulator with an auto-braking function. Messages were voice alerts about 1 s after braking began:
    - "Car is braking." (how)
    - "Obstacle ahead." (why)
    - "Car is braking due to obstacle ahead." (how + why)
    - no message (control)
  - **Acceptance:** main effect of why, F(1,60)=4.79, p<.05. Acceptance was higher with why information (M=24.32) than without it (M=21.35).
  - **Emotional valence:** how x why interaction, F(1,60)=5.90. Feelings were least positive for how+why and most positive when the how message was absent.
  - **Driving:** interaction on road-edge excursions, F(1,60)=6.92, p<.01. How-only drove worst (M=2.81 excursions) and how+why drove safest (M=1.06).
  - **Authors' interpretation:** how+why "creates the greatest cognitive load" and "may be too much information to process while driving". They call this a quantity problem and propose "concurred abbreviation".
  - **Reporting issues in the paper:**
    - The paper prints p<0.001 for F(1,60)=5.90, which does not match an F of that size.
    - The valence index is built from "anxious/annoyed/frustrated" while the figure caption says higher = more positive. Treat the direction as the authors' narrative.
- **Du, Haspiel, Zhang, Tilbury, Pradhan, Yang & Robert (2019).** "Look who's talking now: Implications of AV's explanations on driver's trust, AV preference, anxiety and mental workload." *Transportation Research Part C*. Within-subjects simulator study, N=32, four conditions:
  - no explanation
  - explanation before the AV acted
  - explanation after the AV acted
  - explanation plus driver approve/disapprove option
  - **Result:** explanations before the action gave higher trust and AV preference. There was no difference in anxiety or workload. — [arXiv 1905.08878](https://arxiv.org/pdf/1905.08878); [SSRN](https://papers.ssrn.com/abstract=3392063); [Deep Blue](https://deepblue.lib.umich.edu/items/052ece74-9f21-4983-9955-f365b9730d70)
  - **Lead author's comment (press):** after-the-fact information is "not better than giving them no information at all". Offering a choice did not beat advance notice. — [Research Live](https://www.research-live.com/article/features/put-your-trust-in-an-automated-car/id/5062162); [U-M SI news](https://www.si.umich.edu/news/its-easier-trust-automated-vehicles-when-we-know-what-they-plan-do-ahead-time)
  - **Pilot:** Haspiel et al. (2018, HRI companion) had N=8 and found the same before > after pattern (preliminary). — [Deep Blue](https://deepblue.lib.umich.edu/handle/2027.42/140746?show=full)
  - **Authors' limitations:** results are averaged across participants and ignore desire for control and personality. They propose adaptive interfaces that adjust explanation timing and degree of autonomy to the driver. — [arXiv 1905.08878](https://arxiv.org/pdf/1905.08878) (as summarised in search snippet)
- **Körber, Prasch & Bengler (2018).** "Why do I have to drive now? Post hoc explanations of takeover requests." *Human Factors* 60(3), 305–323. DOI 10.1177/0018720817747730. N=40, explanation group vs control. Explanations of the TOR reason did not change trust or acceptance but increased perceived understanding. — UNVERIFIED (secondary): findings come from a TUM repository abstract that I could not confirm as this exact paper. [mediaTUM](https://mediatum.ub.tum.de/node?id=1438211)
- **Ha, Kim, Seo & Lee (2020).** "Effects of explanation types and perceived risk on trust in autonomous vehicles." *Transportation Research Part F* 73, 271–280. Compared explanation types (reportedly simple feedback vs attributional) under different perceived risk. — UNVERIFIED (secondary): I confirmed the citation only. I could not retrieve the conditions or results. [Lab listing](https://app.rndcircle.io/lab/c4ed1f48-6853-470a-b8ef-d523d5caf0a8/papers/page/3)
- **Shen, Jiang, Chen & Campbell (2020/2022).** "To explain or not to explain: A study on the necessity of explanations for autonomous vehicles." arXiv 2006.11684 (Best Paper, NeurIPS 2022 TEA workshop; workshop paper, not a journal). People agree that explanations are needed in near-crash events. Opinions diverge for ordinary or anomalous situations, depending on driver type. They release 1,103 annotated BDD-A clips. — [arXiv](https://arxiv.org/abs/2006.11684)
- **Kaufman, Broukhim, Kirsh & Weibel (2025).** "What did my car say? Impact of autonomous vehicle explanation errors and driving context on comfort, reliance, satisfaction, and driving confidence." CHI 2025, DOI 10.1145/3706598.3713088. N=232.
  - Explanation errors lowered comfort relying on the AV, confidence and explanation satisfaction, and raised preference for taking control. Errors also lowered ratings of the AV's driving ability even though the driving was identical.
  - Higher harm or difficulty amplified the effect of errors.
  - — [arXiv 2409.05731](https://arxiv.org/abs/2409.05731v3)

### Inferences
- **Reason content is the strongest single message type:** "why" (the reason for the action, e.g. "Obstacle ahead") is the most supported. Action-only ("Car is braking") is the weakest. This is consistent with Koo and with later citing work that describes how-information as a possible overload ([Colley et al. 2022](https://doi.org/10.1145/3534609) related work).
- **Timing should be held constant:** explanations should come before or with the action. For a display-personalisation study, timing is better fixed at "before" than optimised, because it has a clear best level.
- **Accuracy is a precondition:** wrong explanations cost more than missing ones (Kaufman 2025).

### Gaps
- Koo used voice, not visual text. I found no study that crosses why/how content with a visual-text modality for passengers in L4.
- I could not access the Ha et al. 2020 and Körber et al. 2018 results.

## Q2. Level of transparency / information density, and evidence of an inverted-U or clutter effect

### Takeaway
More information is not reliably better. The SAT model (Chen et al.) sets out three levels: (1) what the agent is doing, (2) why, and (3) what it projects. In non-automotive tasks, higher SAT levels often raise SA and trust without adding workload. In AV visualisation studies, adding prediction or planning layers increased workload and perceived clutter, and sometimes lowered trust (Colley et al. 2022). HUDs, and more complex scenes, lowered SA (Currano et al. 2021). Koo's how+why result points the same way. The evidence supports a "moderate content, highest-value layers first" design with large individual variation, rather than a clean, replicated inverted-U.

### Cited Findings
- **Colley, Rädler, Glimmann & Rukzio (2022).** "Effects of scene detection, scene prediction, and maneuver planning visualizations on trust, situation awareness, and cognitive load in highly automated vehicles." *Proc. ACM IMWUT* 6(2), Art. 49. DOI 10.1145/3534609. (full text read) — [PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/institut/Papers/Prof_Rukzio/2022/IMWUT2022_functional_hierarchy_final.pdf)
  - **Design:** 2x2x2 between-subjects (detection on/off, prediction on/off, maneuver/ego-trajectory on/off) on a simulated AR windshield over real-world video. N=216 Prolific participants (mean age 26).
  - **Workload:** prediction raised mental workload (M 12.40 vs 9.89, p=.001).
  - **Trust:** showing the maneuver trajectory lowered trust (M 3.11 vs 3.54, p=.001).
  - **Clutter:** prediction raised perceived visual clutter (M 4.16 vs 2.53, p<.001) and lowered rated necessity.
  - **Understanding:** detection raised the SART Understanding subscale (p=.016).
  - **Overall SA and understandability:** no significant effect.
  - **Perceived safety:** only a three-way interaction.
  - **Authors' conclusion:** prediction visualisations were "perceived as worse", and the results indicate overtrust.
- **Colley, Eder, Rixen & Rukzio (2021).** "Effects of semantic segmentation visualization on trust, situation awareness, and cognitive load in highly automated vehicles." CHI 2021. Simulation N=32 plus video N=41. The AR segmentation display increased subjective SA, kept cognitive load low, and did not increase trust. — [PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/1-hci/hci-paper/2021/CHI2021_Semantic_Segmentation.pdf); summary also in [Colley 2022 related work](https://doi.org/10.1145/3534609)
- **Currano, Park, Moore, Lyons & Sirkin (2021).** "Little road driving HUD: Heads-up display complexity influences drivers' perceptions of automated vehicles." CHI 2021, Art. 511. DOI 10.1145/3411764.3445575. Online N=298, three HUD conditions (none, minimal, complex) across two scenes.
  - SA fell with scene complexity, and was lower with a HUD than without one.
  - Effects of HUD complexity depended on how dynamic the scene was and on the participant's driving style. The authors argue the HUD should adapt to both.
  - — [ACM/unpaywall](https://unpaywall.org/10.1145%2F3411764.3445575); summarised in [Colley 2022](https://doi.org/10.1145/3534609) and [CEUR citing paper](https://ceur-ws.org/Vol-3300/short_5226.pdf)
- **SAT model:** Chen et al. (2014, ARL technical report) define Level 1 (current actions and plans), Level 2 (reasoning) and Level 3 (projected outcomes). — [DTIC ADA600351](https://apps.dtic.mil/sti/pdfs/ADA600351.pdf)
- **Mercado, Rupp, Chen, Barnes, Barber & Procci (2016).** "Intelligent agent transparency in human–agent teaming for multi-UxV management." *Human Factors* 58(3), 401–415. DOI 10.1177/0018720815621206. Varied SAT level in a multi-robot task (not driving). — [SAGE](https://journals.sagepub.com/doi/reader/10.1177/0018720815621206). Specific results UNVERIFIED (not retrieved).
- **DST Group review:** across five SAT studies, transparency did not seem to affect response time or subjective workload. Some studies found that extra transparency information worsened performance. — [DST-Group-TR-3413](https://www.dst.defence.gov.au/sites/default/files/publications/documents/DST-Group-TR-3413.pdf)
- **Selkowitz, Lakhmani & Chen (2017):** higher SAT level gave greater SA and trust, with no workload or usability difference (robot squad-member context, not driving). — UNVERIFIED (secondary via search snippet; [UCF STARS](https://stars.library.ucf.edu/scopus2015/5210))
- **Häuslschmid, von Bülow, Pfleging & Butz (2017).** "Supporting trust in autonomous driving." IUI 2017. Compared a world-in-miniature view and a chauffeur avatar showing the car's situation interpretation. The world in miniature raised trust most, and participants disagreed strongly on whether such a display was necessary. — [PDF](https://www.medien.ifi.lmu.de/pubdb/publications/pub/haeuslschmid2017iui/haeuslschmid2017iui.pdf); summarised in [Colley 2022](https://doi.org/10.1145/3534609)
- **Schneider, Hois, Rosenstein, Ghellal, Theofanou-Fülbier & Gerlicher (2021).** "ExplAIn yourself! Transparency for positive UX in autonomous driving." CHI 2021.
  - Explanations via AR windshield and an LED strip raised UX for first-time users.
  - Adding a post-hoc smartphone explanation did not raise it further.
  - — summarised in [Colley 2022](https://doi.org/10.1145/3534609); original not retrieved.

### Inferences
- **Which layer to show:** the "which layer" choice (perception, prediction, planning) acts like an information-density property.
  - Perception/detection highlighting seems cheap and helpful for understanding.
  - Prediction overlays carry clear clutter and workload costs.
  - Planned-trajectory overlays may lower trust in a passenger video setting.
- **Shape of the effect:** an inverted-U is plausible but not formally demonstrated. No study I found varied density across three or more ordered levels and fitted a curvilinear effect for AV occupants.
- **Implication for the study:** this gap suits a preference-learning study that treats density as a continuous parameter.

### Gaps
- I found no AV study that explicitly varies SAT Level 1/2/3 as text content for passengers (the SAT evidence comes from military and robot tasks).
- I did not retrieve the Mercado 2016 numbers.
- Currano's per-condition SA numbers were not retrieved.

## Q3. Vehicle-state information: system confidence/uncertainty, mode, TOR cues

### Takeaway
Showing automation uncertainty or confidence improves calibration, SA and take-over safety in several studies (Beller 2013; Helldin 2013; Kunze 2019). Visual uncertainty displays can raise workload and monitoring glances (Kunze 2019). Results on trust differ: Beller found higher trust, and Helldin reportedly found lower trust, which is consistent with calibration rather than a simple increase.

### Cited Findings
- **Beller, Heesen & Vollrath (2013).** "Improving the driver–automation interaction: An approach using automation uncertainty." *Human Factors* 55(6), 1130–1141. DOI 10.1177/0018720813482327.
  - **Design:** simulator study with a between-subjects uncertainty symbol (an anthropomorphic "confused face with open palms") and within-subjects automation reliability.
  - **Results:** longer time-to-collision on automation failure, better SA and better knowledge of fallibility, higher trust and acceptance.
  - — [SAGE](https://journals.sagepub.com/doi/10.1177/0018720813482327); [MetaTOC](https://metatoc.com/papers/1355-improving-the-driver-automation-interaction-an-approach-using-automation-uncertainty). Abstract-level only.
- **Helldin, Falkman, Riveiro & Davidsson (2013).** "Presenting system uncertainty in automotive UIs for supporting trust calibration in autonomous driving." AutomotiveUI '13, 210–217. DOI 10.1145/2516540.2516554.
  - Showed a bar display of the system's ability to operate.
  - Drivers took over faster and did more secondary tasks.
  - Colley 2022 summarises Helldin as finding lower trust with uncertainty shown, while another secondary source says trust was higher. — UNVERIFIED and CONFLICTING (secondary only): [Colley 2022 related work](https://doi.org/10.1145/3534609) vs search snippet.
- **Kunze, Summerskill, Marshall & Filtness (2019).** "Automation transparency: Implications of uncertainty communication for human-automation interaction and interfaces." *Ergonomics* 62(3), 345–360.
  - **Display:** a stylised heartbeat plus a numeric uncertainty display.
  - **Benefits:** better trust calibration and SA, safer takeovers, and gaze adjusted to the uncertainty level.
  - **Cost:** significantly increased workload, and non-driving tasks were harder to do.
  - — [Loughborough repository](https://dspace.lboro.ac.uk/2134/35904)
- **Kunze et al. (AR uncertainty and peripheral cues).** Hue conveyed urgency best among visual variables. The authors argued against the instrument cluster (workload) and used a light strip and vibrotactile seat. — summarised in [Colley 2022](https://doi.org/10.1145/3534609); [Lboro AR uncertainty PDF](https://repository.lboro.ac.uk/articles/Augmented_reality_displays_for_communicating_uncertainty_information_in_automated_driving/9338876/files/16947521.pdf)
- **Kunze et al., function-specific uncertainty (IGI).** The take-over benefit depended on driving experience, and less experienced drivers benefited most. — UNVERIFIED (secondary snippet): [IGI Global](https://www.igi-global.com/article/function-specific-uncertainty-communication-in-automated-driving/231846)
- **Follow-up literature:** visually conveyed uncertainty increased perceived effort through more monitoring glances. — UNVERIFIED (secondary, source paper not identified)
- **Colley et al. (2023), uncertainty trajectory paper (IMWUT 2023).** Exists but was not retrieved. — [PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/1-hci/hci-paper/2023/IMWUT_2023_Uncertainty_Trajectory_final.pdf)

### Inferences
- **Showing confidence:** "show system confidence (on/off, or granularity)" is a well-supported content property. Its expected effect is better calibration rather than higher trust.
- **Encoding:** a continuous visual display costs workload. Peripheral, ambient or colour-hue encodings are proposed to reduce this.

### Gaps
- I found no study isolating speed or driving-mode display as an explanation property for passengers.
- The Helldin trust direction needs checking in the original.

## Q4. Modality: text vs icons vs auditory vs combined; text size in HUDs

### Takeaway
Combined (multimodal) explanations tend to give the highest trust and perceived transparency with no workload penalty in the one recent L4 passenger study found. Speech has been studied as an anthropomorphic, trust-raising channel. I found no peer-reviewed AV occupant study on HUD text size or legibility.

### Cited Findings
- **Pradhan, Hungund & Onyeukwu (2026).** "Trust-building in Level 4 automation by intent communication: In-vehicle HMI design, passenger trust, and visual attention." New England UTC report 01938993 (technical report, not peer-reviewed).
  - N=36 rear-seat passengers in a simulator, comparing auditory, visual and multimodal HMIs that announced perception and intent 5 s before each maneuver.
  - Trust rose in all three conditions.
  - Multimodal gave higher trust and perceived transparency than visual, with no workload or usability penalty.
  - Trust was negatively correlated with time spent watching the display.
  - — [ROSA P](https://rosap.ntl.bts.gov/view/dot/93332)
- **Forster, Naujoks & Neukum (2017).** "Increasing anthropomorphism and trust in automated driving functions by adding speech output." IEEE IV 2017, 365–372. — Citation confirmed via [Crossref-listed citing work](https://api.crossref.org/works/10.1145%2F3342197.3344545); findings UNVERIFIED.
- **el Jouhri et al. (2023).** "The influence of a color themed HMI on trust and take-over performance in automated vehicles." *Frontiers in Psychology* 14:1128285. DOI 10.3389/fpsyg.2023.1128285.
  - L3, N=45. An auditory baseline was compared with colour-themed ambient displays.
  - The colour-themed HMI was rated more trustworthy and improved task understanding, with no take-over performance change.
  - — [Frontiers](https://dx.doi.org/10.3389/fpsyg.2023.1128285) (details from search snippet; full text not parsed)
- **Koo et al. (2015)** delivered all explanations as voice. Content effects there are tied to the auditory channel. — [PDF](https://www.wendyju.com/publications/WhyDidMyCarJustDoThat.pdf)

### Inferences
- **Modality as a variable:** modality is a strong design variable but is awkward to vary in a visual crowdsourced study. Within visual displays, text vs icon vs both is the comparable dimension, and I found no direct AV occupant comparison of it.

### Gaps
- No verified study on text size or legibility of explanation text in HUDs or windshield displays for occupants.
- No verified text-vs-icon comparison for AV explanations.

## Q5. Personalisation and individual differences; consensus vs disagreement

### Takeaway
Many studies report large individual differences in how much explanation people want: by driver type, experience, prior trust and driving style. Several call explicitly for adaptive or personalised explanations. Only a few test adaptation, and none that I found adapts visual explanation amount in AVs with preference learning, which leaves room for the planned BO study.

### Cited Findings
- **Currano et al. (2021):** HUD complexity effects depended on the participant's self-reported driving style, and the authors recommend an adaptive HUD. — [Colley 2022 summary](https://doi.org/10.1145/3534609); [ACM](https://unpaywall.org/10.1145%2F3411764.3445575)
- **Häuslschmid et al. (2017):** participants' opinions "varied strongly" on whether a situation-interpretation display was necessary. — [Colley 2022](https://doi.org/10.1145/3534609)
- **Shen et al. (2020/2022):** need for explanation differs by driver type except in near-crash events. — [arXiv](https://arxiv.org/abs/2006.11684)
- **Kaufman et al. (2025):** prior trust and expertise were positively associated with outcome ratings. The authors recommend "contextually adaptive and personalized" explanations. — [arXiv/CHI 2025](https://arxiv.org/abs/2409.05731v3)
- **Du et al. (2019):** propose adapting explanation timing and degree of autonomy to driver characteristics. A cross-cultural follow-up examines cultural and personality differences. — [arXiv](https://arxiv.org/pdf/1905.08878); [Deep Blue cross-cultural](https://deepblue.lib.umich.edu/handle/2027.42/142564?show=full)
- **Adaptive personalised explainability (arXiv 2504.13856, 2025).** In a simulated self-driving task, preferences across explanation modes (written, decision tree, feature importance) did not always match performance. An adaptive strategy balancing the two gave significant performance gains. — [arXiv](https://arxiv.org/pdf/2504.13856) (preprint; authors and venue not verified)
- **Automated valet parking study (MDPI *Sustainability* 16(1):63, 2024).** "Analysing the effects of scenario-based explanations on automated vehicle HMIs." New vs frequent users had different explanation preferences, and new users benefited more from guided explanations. — UNVERIFIED (search snippet only; page returned 403): [MDPI](https://www.mdpi.com/2071-1050/16/1/63); [CiteDrive](https://www.citedrive.com/en/discovery/analysing-the-effects-of-scenario-based-explanations-on-automated-vehicle-hmis-from-objective-and-subjective-perspectives)
- **Kunze et al.:** less experienced drivers benefited most from uncertainty communication. — UNVERIFIED: [IGI](https://www.igi-global.com/article/function-specific-uncertainty-communication-in-automated-driving/231846)

### Inferences
- **Consensus**, where several sources agree:
  1. Reason ("why") content beats action-only content (Koo; cited approvingly by later work).
  2. Explanations before the action beat explanations after it (Du 2018/2019).
  3. Uncertainty or confidence information improves calibration and take-over behaviour (Beller, Kunze, Helldin).
  4. Adding visual layers adds workload and clutter, especially prediction overlays (Colley 2022; Kunze 2019; Koo how+why).
- **Disagreement or open questions:**
  - Whether transparency raises or lowers trust: Beller up; Helldin reportedly down; Colley 2021 none; Colley 2022 trajectory lowered it.
  - Whether "more" helps SA: SAT studies yes; Currano HUD presence lowered SA.
  - Whether combined how+why is net positive: safer driving but worse affect.
- **Candidate visual properties for BO personalisation**, given high individual variance and no single best level:
  1. explanation detail/density (none → icon → short why-text → why+how)
  2. perception-highlight amount (number or salience of detected objects)
  3. prediction/trajectory overlay (off ↔ full)
  4. confidence/uncertainty display granularity (off/binary/continuous)
  5. text size or legibility (no prior evidence, so a weaker basis)
- **Fix, don't personalise:** timing (fix at "before") and accuracy are better held constant than personalised.

### Gaps
- No peer-reviewed study found that personalises AV explanation display properties through preference elicitation or Bayesian optimisation.
- Age-specific explanation preferences in AVs were not found within this search budget.
- Moderators other than experience, trust and driving style (trust propensity scales, need for cognition) were not verified in AV studies.
- Wintersberger, Na Du's later explanation work and Omeiza et al.'s survey of explainable autonomous driving were not retrieved in this pass.
