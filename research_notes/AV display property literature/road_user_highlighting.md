# Highlighting detected road users and hazards in in-vehicle AV displays: visual properties, levels tested, effects

Scope: AR head-up displays, simulated AR windshields and central-screen HMIs that highlight pedestrians, cyclists, vehicles and other hazards for AV occupants or drivers. Research done 2026-10-26. Full texts read (PDF) for: Colley et al. 2020, 2021, 2022; Jansen et al. 2025 (OptiCarVis, arXiv HTML); Jansen et al. 2025 (TRF); Goodge et al. 2026. All other entries are based on abstracts, publisher or index pages, or citations in other papers, and are marked that way.

## Q1. Which highlighting properties have been studied, and at what levels?

### Takeaway
The properties that have been varied in controlled studies are: display location (AR windshield vs tablet or centre screen), scope (dynamic road users only vs dynamic plus static objects; user-chosen objects), highlight transparency (alpha) and on/off visibility per element, highlight style (six types incl. bounding box and spotlight; segmentation mask vs symbol above the head), class colour coding (hue by object class), number of intention or uncertainty states, size of the marker above the pedestrian, and world-fixed vs screen-fixed anchoring of time-to-contact labels. Risk or urgency colour has mostly been studied as a ranking of visual variables, not as a manipulated highlight in an AV ride. Distance and TTC labels appear in one study, and only as an anchoring manipulation. Highlight size for whole-object masks was not varied in any study I found.

### Cited Findings

**Display location (AR windshield vs tablet or centre screen)**
- Colley, Eder, Rixen, Rukzio (2021), "Effects of Semantic Segmentation Visualization on Trust, Situation Awareness, and Cognitive Load in Highly Automated Vehicles", CHI '21, doi:10.1145/3411764.3445351. Pre-study: online, within-subjects, N=32, Unity simulation of a Tesla X ride. Five conditions: baseline, tablet dynamic, tablet dynamic+static, AR dynamic, AR dynamic+static. Preference ranks (1 = best): AR dynamic+static M=2.06, AR dynamic M=2.31, tablet dynamic+static M=3.34, tablet dynamic M=3.38, baseline M=3.91. Friedman χ²(4)=31.12, p<.001. AR dynamic+static was ranked significantly better than both tablet versions and the baseline. Participants said the tablet was "too distracting". — [Colley et al. 2021, CHI](https://doi.org/10.1145/3411764.3445351) (PDF: [uni-ulm](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/1-hci/hci-paper/2021/CHI2021_Semantic_Segmentation.pdf))
- Colley, Bräuner, Lanzer, Walch, Baumann, Rukzio (2020), "Effect of Visualization of Pedestrian Intention Recognition on Trust and Cognitive Load", AutomotiveUI '20, doi:10.1145/3409120.3410648. VR study, N=15, five conditions: AR or tablet × two or three intention-clarity states, plus a no-visualisation baseline. Raw NASA-TLX was lowest for AR three states (M=2.99) and highest for tablet two states (M=5.51). Main effect of technology: F=13.03, p<.001, with AR lower. AR three states was preferred (mean rank M=0.83) and was ranked significantly better than all other systems except AR two states. — [Colley et al. 2020, AutoUI](https://doi.org/10.1145/3409120.3410648) (PDF: [uni-ulm](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/institut/Papers/Prof_Rukzio/2020/AutoUI2020_Pedestrian_Intention-min.pdf))
- Colley et al. 2022 (IMWUT) used the AR windshield for every condition because, they argued, AR had been shown to be superior to tablet versions in their 2020 and 2021 studies. Location is therefore treated as settled in this research line. — [Colley et al. 2022, IMWUT](https://doi.org/10.1145/3534609)

**Scope: which objects are highlighted**
- Colley et al. 2021: dynamic objects (pedestrians, vehicles, cyclists) vs dynamic+static objects (adding signposts). In the pre-study, AR dynamic+static was rated best on most measures, and AR dynamic was ranked about as well (mean ranks 2.06 vs 2.31; this pair was not reported as significantly different). In the real-video study (N=41, Panoptic-DeepLab on Ulm footage, baseline vs AR dynamic+static), three participants did not want signposts visualised, and participants asked for traffic lights and stop lights to be excluded because "the meaning is hidden by the colorization". — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- Wintersberger, Nicklas, Martlbauer, Hammer, Riener (2020), "Explainable Automation: Personalized and Adaptive UIs to Foster Trust and Understanding of Driving Automation Systems", AutomotiveUI '20, doi:10.1145/3409120.3410659. N=56 watched ego-perspective AV videos, rated trust, and could freely select which objects in the scene should receive AR feedback. Situational trust correlated inversely with the desire for feedback. The authors call for adaptive interfaces. *Abstract only; which objects were chosen and how much choices varied were not verified.* — [Wintersberger et al. 2020](https://doi.org/10.1145/3409120.3410659); journal follow-up: Wintersberger et al. 2021, it – Information Technology, [doi:10.1515/itit-2020-0024](https://doi.org/10.1515/itit-2020-0024)
- Wintersberger, Frison, Riener, von Sawitzky (2019), "Fostering User Acceptance and Trust in Fully Automated Vehicles: Evaluating the Potential of Augmented Reality", PRESENCE 27(1):46–62, doi:10.1162/pres_a_00320. Driving simulator, N=26 facing forward and N=18 facing backward. AR augmentation of traffic objects that were otherwise invisible (dense fog), or of upcoming manoeuvres, increased acceptance and trust. *Abstract only. The highlight style and levels were not verified. This is AR highlighting vs none, not a property manipulation.* — [Wintersberger et al. 2019](https://doi.org/10.1162/pres_a_00320); earlier version: [Wintersberger et al. 2017, AutoUI, "Traffic Augmentation as a Means to Increase Trust in Automated Driving Systems"](https://research.jku.at/en/publications/traffic-augmentation-as-a-means-to-increase-trust-in-automated-dr/)
- Jansen, Colley, Rädler, Schwedler, Rukzio (2025), "Longitudinal effects of visualizing uncertainty of situation detection and prediction of automated vehicles on user perceptions", Transportation Research Part F 113:536–553, doi:10.1016/j.trf.2025.05.013. When asked to rank the element types (pedestrian detection in red, vehicle detection in blue, street-sign detection in yellow, pedestrian intention icons), participants differed significantly: Friedman χ²(3)=91.18, p<.001, r=0.61. Vehicle detection was the most preferred. Open answers included "Maybe just highlight all the pedestrians so I know the car is registering them, and only mark those actually crossing". — [Jansen et al. 2025, TRF](https://doi.org/10.1016/j.trf.2025.05.013)
- Colley et al. 2022 chose to highlight "all driving task-relevant traffic objects" rather than use light bands. They argued that leaving an object unhighlighted could lead users to assume it had not been detected. This is a design rationale, not a tested result. — [Colley et al. 2022](https://doi.org/10.1145/3534609)

**Highlight transparency (alpha) and visibility per element**
- Jansen, Colley, Krauß, Hirschle, Rukzio (2025), "OptiCarVis: Improving Automated Vehicle Functionality Visualizations Using Bayesian Optimization to Enhance User Experience", CHI '25, doi:10.1145/3706598.3713514. Online between-subjects study, N=117 (Prolific, US), Unity simulation with an AR windshield and an SAE L4 ride. Sixteen parameters were optimised with multi-objective Bayesian optimisation, including:
  - semantic segmentation (object highlighting): on/off, and alpha 0.1–1;
  - pedestrian intention marker: on/off, and size 0.1–0.2;
  - other road users' trajectory: on/off, alpha 0.1–1, size 0.1–0.6;
  - occluded cars: on/off;
  - also the ego trajectory, the CAD-covered area and the vehicle-status HUD.

  RGB colour, style and position were deliberately not parameterised. Objectives: perceived safety, trust, predictability, acceptance and aesthetics, plus cognitive load (NASA-TLX mental demand) to minimise. — [Jansen et al. 2025, CHI (arXiv)](https://arxiv.org/html/2501.06757v3)
- OptiCarVis expert design (8 experts, averaged): segmentation highlighting was on in 7 of 8 designs, with alpha mean 0.23 (SD 0.16, range 0.10–0.49). In the end-user custom-design condition, segmentation alpha "often had intervals above α=0.7", while the other conditions "hovered around α=0.5". — [Jansen et al. 2025, CHI](https://arxiv.org/html/2501.06757v3)

**Highlight style (mask, outline, bounding box, spotlight, marker above the head)**
- Tran, Peillard, Walsh, Moreau, Thomas (2025), "Trust and Safety in Autonomous Vehicles: Evaluating Contextual Visualizations for Highlighting, Prediction, and Anchoring", ICAT-EGVE 2025 (Eurographics), doi:10.2312/egve.20251351. Three online studies with prerecorded simulated driving videos. Study 1 compared six highlight types across five scenarios that varied in complexity and visibility. Effectiveness depended on the scenario: bounding boxes and spotlights worked better in occluded or ambiguous conditions. *Abstract only. The six types, N and effect sizes were not verified; the full text was blocked (403 / bot check).* — [Tran et al. 2025](https://diglib.eg.org/handle/10.2312/egve20251351); [HAL record](https://hal-hceres.archives-ouvertes.fr/LAB-STICC_INUIT/hal-05396377v1)
- Colley et al. 2020 chose coloured circles above pedestrians' heads over coloured bounding boxes because boxes "would have needed additional space, resulting in visual clutter". This is a design rationale, not a test. — [Colley et al. 2020](https://doi.org/10.1145/3409120.3410648)
- Colley et al. 2021, open feedback: one participant would "have preferred to only see outlines" and minimal flicker, rather than full-pixel segmentation masks. Anecdotal; outline vs mask was not tested. — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)

**Colour coding (by class vs by urgency or uncertainty)**
- Colley et al. 2021 encoded object class by hue (based on a literature analysis of segmentation colour schemes). They deliberately did not use hue for detection uncertainty or urgency; uncertainty was conveyed implicitly by flicker and missed detections. — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- Colley et al. 2022 and Jansen et al. 2025 (TRF) used pedestrians and cyclists in red, vehicles in blue and signposts in yellow. Colley et al. 2020 avoided yellow or orange for intention states because those colours "carry a warning function", and used shades of blue and purple instead. — [Colley et al. 2022](https://doi.org/10.1145/3534609); [Colley et al. 2020](https://doi.org/10.1145/3409120.3410648)
- Kunze, Summerskill, Marshall, Filtness (2018), "Augmented Reality Displays for Communicating Uncertainty Information in Automated Driving", AutomotiveUI '18, pp. 164–175. Eleven visual variables for function-specific uncertainty were tested in a sorting task (N=46, per secondary summary). Colour and animation variables, especially hue, conveyed a clear urgency order and were well received. *Abstract/summary level; N not verified in the full text.* — [Kunze et al. 2018 (Loughborough repository)](https://repository.lboro.ac.uk/articles/Augmented_reality_displays_for_communicating_uncertainty_information_in_automated_driving/9338876)

**Number of intention or uncertainty states on a pedestrian marker**
- Colley et al. 2020: two states (intention clear in purple / unclear in yellow) vs three states (crossing in blue / staying in baby-blue / unclear in yellow). AR with three states was preferred and had the lowest TLX. AR two states was not significantly worse in preference. — [Colley et al. 2020](https://doi.org/10.1145/3409120.3410648)

**Marker size**
- OptiCarVis pedestrian-intention marker size, range 0.1–0.2: expert mean 0.15 (SD 0.04). The optimisation conditions (C4–C6) "showed larger intervals, pointing to greater preference diversity". — [Jansen et al. 2025, CHI](https://arxiv.org/html/2501.06757v3)

**Distance and time-to-contact labels; anchoring**
- Tran et al. 2025, Study 3: world-fixed time-to-contact displays significantly improved trust, perceived safety and object detectability compared with screen-fixed displays. *Abstract only.* — [Tran et al. 2025](https://diglib.eg.org/handle/10.2312/egve20251351)

**Highlighting vs no highlighting / attention cueing (driver-centred HUD work)**
- Rusch, Schall, Gavin, Lee, Dawson, Vecera, Rizzo (2013), "Directing driver attention with augmented reality cues", Transportation Research Part F 16:127–137. Fixed-base simulator, N=27 middle-aged drivers. AR cues to roadside hazards gave near-significant response-time benefits, and increased response rates for pedestrians and warning signs but not for vehicles. The cues did not impair perception of non-target objects, and system false alarms and misses did not impair responses. *Abstract only. Pre-2015 and manual driving.* — [Rusch et al. 2013 (CDC Stacks)](https://stacks.cdc.gov/view/cdc/222186)
- Kim & Gabbard (2019; print 2022), "Assessing Distraction Potential of Augmented Reality Head-Up Displays for Vehicle Drivers", Human Factors 64(5):852–865, doi:10.1177/0018720819844845. Simulator, N=24, two AR pedestrian-collision-warning designs. Only one of the two improved awareness of pedestrians without visually or cognitively distracting drivers from non-augmented road elements. The authors conclude that AR interfaces can be informative or distracting depending on the perceptual form of the graphics. *Abstract-level only: which design won, and its exact form (e.g., conformal box vs "virtual shadow"), were not verified because the full text was blocked.* — [Kim & Gabbard 2019, Human Factors](https://doi.org/10.1177/0018720819844845)
- Goodge, Pollick, Brewster (2026), "ARe you watching the road? Comparing Gaze Behaviour and Hazard Prediction between Heads-Up and Heads-Down NDRT Presentation in Augmented Reality", ACM Transactions on Applied Perception, doi:10.1145/3807942. N=22 experienced drivers doing a non-driving-related task (NDRT) in AR plus a hazard-prediction task. In the Dynamic AR HUD condition, an attentional cue pointed to the hazard area. It increased fixations in the right area but gave no benefit to hazard prediction: drivers were "not able to sufficiently process the driving scene", described as look-but-fail-to-see. The authors suggest the cue may draw attention to itself, and some drivers were frustrated that it interrupted the task. — [Goodge et al. 2026, TAP](https://doi.org/10.1145/3807942) (PDF: [Glasgow eprints](https://eprints.gla.ac.uk/387337/2/387337.pdf))
- Studies cited by Goodge et al. 2026 (*not verified first-hand*):
  - Wang et al. (2022), "Inattentional blindness in augmented reality head-up display-assisted driving", International Journal of Human–Computer Interaction 38(9):837–850: inattentional blindness occurred with an AR HUD that highlighted pedestrians and increased under higher workload; non-highlighted pedestrians were recognised less often.
  - Karatas et al. (2020), IEEE Intelligent Vehicles Symposium, pp. 2158–2164: dynamic AR-HUD hazard highlighting led to earlier fixations and faster recognition than a traditional HUD.

  — [Goodge et al. 2026, related work](https://eprints.gla.ac.uk/387337/2/387337.pdf)
- de Oliveira Faria & Gabbard (2025, arXiv preprint, not peer-reviewed), "Inattentional Blindness with Augmented Reality HUDs: An On-road Study": drivers' timely detection of stimuli fell as the visual demand of the AR task rose, and AR-induced inattentional blindness was more prevalent in the central field of view. — [arXiv:2505.00879](https://arxiv.org/abs/2505.00879)
- Calvi et al. (2020), "Effectiveness of Augmented Reality Warnings on Driving Behavior Whilst Approaching Pedestrian Crossings", Accident Analysis & Prevention 147:105760. Simulator, N=46, flashing AR arrow vs arrow plus audio. *Search snippet only; results not verified.* — [doi:10.1016/j.aap.2020.105760](https://doi.org/10.1016/j.aap.2020.105760)

**Display complexity / amount of highlighted information**
- Currano, Park, Moore, Lyons, Sirkin (2021), "Little Road Driving HUD: Heads-Up Display Complexity Influences Drivers' Perceptions of Automated Vehicles", CHI '21, doi:10.1145/3411764.3445575. Online study, N=298 per secondary summary. Situation awareness fell with scene complexity and, unexpectedly, also fell with a HUD present compared with none. HUD complexity had significant effects; complexity was operationalised by item count, item categories and illuminated pixels. Driving style interacted with driving context and HUD complexity. *Abstract/secondary only; exact levels and effect directions not verified.* — [Currano et al. 2021](https://doi.org/10.1145/3411764.3445575)
- Lindemann, Lee, Rigoll (2018), "Catch My Drift: Elevating Situation Awareness for Highly Automated Driving with an Explanatory Windshield Display User Interface", Multimodal Technologies and Interaction 2(4):71; also ISMAR 2018. An explanatory windshield display, combining world-registered AR and screen-fixed elements to show perception and decisions, significantly improved SA (freeze-probe queries): a medium effect in clear weather and a large effect in poor visibility. *Bundle: perception highlighting was not isolated. Abstract only.* — [Lindemann et al. 2018, MTI](https://doi.org/10.3390/mti2040071)

### Inferences
- Properties that have been parameterised as continuous or ordinal and that people disagree about: highlight alpha/opacity, per-class or per-element visibility (scope), and marker size. These map directly onto Bayesian-optimisation (BO) dimensions; OptiCarVis already treats them that way.
- Highlight style (mask vs outline vs box vs spotlight vs marker) is categorical. It has one comparative study (Tran et al. 2025), whose result is that the best style depends on the scenario. It could be a categorical BO dimension, or it could be fixed.
- Urgency or risk colour coding has been studied for perceptual ordering (Kunze et al. 2018), not as a highlight property in an AV-occupant study. That is a gap.

### Gaps
- No study I found varies the opacity of whole-object highlights as a controlled factor (outside the BO) with trust or SA outcomes. OptiCarVis reports alpha only as an optimisation outcome.
- No peer-reviewed study found that varies distance/TTC labels on/off for occupants (Tran et al. 2025 varies anchoring only), or highlight thickness, glow, or the "relevant-only vs all detected" contrast under the same rendering style.
- Not verified, because full texts were blocked: the Tran et al. 2025 highlight types and N; the Kim & Gabbard 2019 design details; Currano et al. 2021 effect directions; Wintersberger et al. 2019/2020 object-selection data.
- Schwarz & Fastenmeier (2017, Accident Analysis & Prevention), "Augmented reality warnings in vehicles: effects of modality and specificity", is commonly cited, but I could not locate it to verify, so it is not used.

## Q2. Participants, settings, and effects on understanding/SA, trust, perceived safety, workload, takeover and preference

### Takeaway
Most evidence comes from online video or desktop-simulation studies with N of 15–298. Highlighting detected road users reliably raises subjective SA and capability assessment, often without raising workload. Trust effects are mixed or null. Over-trust, clutter, flicker and attention capture (look-but-fail-to-see) are recurring negative effects. Takeover performance has rarely been measured with perception-highlight manipulations.

### Cited Findings
- **Colley et al. 2021, real-video study (N=41, online, AR dynamic+static vs baseline):**
  - SART SA was higher with highlighting (M=21.02, SD=5.70) than baseline (M=16.61, SD=5.99); the understanding subscale was also higher (t(40)=2.19, p=.03).
  - There were no significant differences in mental load (8.85 vs 8.05), trust (Trust in Automation scale 3.32 vs 3.31) or SUS (66.89 vs 68.11).
  - All recognition-related capability ratings were significantly better with highlighting (moderate effects).
  - The highlighting created "a lot of visual clutter", but this did not significantly increase cognitive load or decrease trust.

  — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- **Colley et al. 2021, over-trust calibration:** one participant said "The visualization made me realize, how bad the recognition still works. Without any visualization I definitely trusted the system more (over-trust)." The authors argue that the salience of the highlight is beneficial because it nudges engagement. — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- **Colley, Rädler, Glimmann, Rukzio (2022), "Effects of Scene Detection, Scene Prediction, and Maneuver Planning Visualizations on Trust, Situation Awareness, and Cognitive Load in Highly Automated Vehicles"**, Proc. ACM IMWUT 6(2), Art. 49, doi:10.1145/3534609. Online between-subjects 2×2×2 design (detection × prediction × maneuver), N=216 (Prolific), real video with a simulated AR windshield.
  - Detection highlighting had a significant main effect on SART Understanding: χ²(1)=5.79, p=.016.
  - Prediction visualisations raised mental workload (M=12.40 vs 9.89 without; χ²(1)=10.78, p=.001).
  - Adding a maneuver trajectory lowered trust (3.11 vs 3.54; χ²(1)=10.12, p=.001).
  - There was no significant overall effect on SA, and pairwise differences in perceived safety were not significant.
  - Prediction-related visualisations were perceived as worse; when a visualisation was judged negatively, the AV's abilities were also judged worse. The authors conclude that "the results indicate the presence of overtrust in AVs".

  — [Colley et al. 2022, IMWUT](https://doi.org/10.1145/3534609)
- **Jansen et al. 2025, TRF (N=50, 3-day longitudinal, within-subjects, real-world videos twice a day, segmentation highlighting of pedestrians and vehicles plus pedestrian intention icons):**
  - Perceived safety and trust rose over time.
  - Ten of 25 respondents said incorrect or flickering overlays undermined trust ("A statue was indicated as a person").
  - Nine of 25 reported clutter and distraction: hues for vehicles, signs and pedestrians conflicted with real-world colours, described as "color-coded chaos", and flicker caused at least one report of headaches.
  - Participants asked for adjustable detail ("It would be good to turn up or turn down the level of detail displayed").

  — [Jansen et al. 2025, TRF](https://doi.org/10.1016/j.trf.2025.05.013)
- **OptiCarVis (N=117 online):** compared with the averaged expert design (C2), the BO-optimised designs (C4–C6) had:
  - higher perceived safety (C4 M=1.32, C5 0.95, C6 0.74 vs C2 −0.25 and custom C3 −0.70);
  - higher trust (C4 3.94 and C5 3.95 vs C2 3.04);
  - lower cognitive load (6.12–6.72 vs 9.76 for C2 and 9.03 for C3);
  - higher predictability (C4 4.03, C5 3.84 vs C2 3.10, no visualisation 3.08).

  There were no significant differences in acceptance (p=.073) or aesthetics (p=.277). The optimised designs switched many elements off, and C4 had the highest share of parameters off. Some participants felt "a little overwhelmed" when all elements were highlighted. — [Jansen et al. 2025, CHI](https://arxiv.org/html/2501.06757v3)
- **Colley, Jansen, Krauß, Rukzio (2026, accepted to AutomotiveUI '26)**, "Multi-Session User Experience Assessments of Computationally Optimized Automated Vehicle Functionality Visualizations": online, N=74, multi-session iterative MOBO. Optimised parameters improved trust, safety and predictability. The authors note shortcomings of computational optimisation for subjective measures. *arXiv abstract only; the parameters and individual-difference results were not reported on the abstract page.* — [arXiv:2607.28552](https://arxiv.org/abs/2607.28552)
- **Colley et al. 2020 (VR, N=15):** the AR pedestrian-intention visualisation reduced cognitive load. Per the abstract, all concepts and more information positively affected trust, but propensity to trust did not change from pre to post (2.40 vs 2.40). — [Colley et al. 2020](https://doi.org/10.1145/3409120.3410648)
- **Attention capture and takeover:** Goodge et al. 2026 (N=22) found that hazard cueing during an AR NDRT did not improve hazard prediction (look-but-fail-to-see). — [Goodge et al. 2026](https://doi.org/10.1145/3807942). Kim & Gabbard 2019 (N=24) found that one of two AR pedestrian-warning designs distracted from non-augmented elements. — [Kim & Gabbard 2019](https://doi.org/10.1177/0018720819844845)
- **Weak evidence, noted for completeness:** Li et al. (2025), "From Black Box to Transparency: The Impact of Multi-Level Visualization on User Trust in Autonomous Driving", Sensors 25(21):6725, doi:10.3390/s25216725. CARLA simulator, N=29, three transparency levels (Level 2 adds an AR trajectory, LiDAR and segmentation views). It did not measure trust or SA with validated scales, and the abstract and results are internally inconsistent. Not recommended as evidence. — [Li et al. 2025](https://doi.org/10.3390/s25216725)

### Inferences
- Across the Ulm studies, highlighting detection improves understanding and capability assessment more consistently than it changes trust. Trust gains appear mainly when the design is tuned (OptiCarVis) or over repeated exposure (TRF 2025).
- Clutter appears to come mostly from many hues, flicker and highlighting of irrelevant static objects (signposts, lights), not from highlighting pedestrians or vehicles per se. This suggests that scope and opacity are the levers that control it.
- Takeover performance is essentially untested for perception-highlight properties in AV-occupant studies. The takeover-related evidence comes from driver hazard-cue studies in manual or conditional automation.

### Gaps
- No peer-reviewed study found that measures objective takeover quality (time to takeover, minimum TTC) as a function of road-user highlight opacity, style or scope.
- Few studies have occupants in a real vehicle or on-road; almost all are online video, desktop simulation or VR.

## Q3. Evidence of individual differences (disagreement about the best level)

### Takeaway
Yes. There is direct evidence that people and experts disagree about highlight transparency, which elements to show, and marker size, and that feedback needs depend on individual trust. This supports personalising opacity/alpha, scope (which classes are highlighted) and marker size.

### Cited Findings
- OptiCarVis: six of 16 parameters showed high variability among the 8 experts (SD > 0.18): other-road-user trajectory alpha (p6), ego-trajectory visibility (p8), CAD-covered-area visibility and alpha (p11, p12), occluded-cars visibility (p14), and status-HUD alpha (p16). Experts said personal preference drove their alpha choices, which made a single consensus design hard. The BO conditions showed "wider intervals than C3, indicating a broad range of preferences not captured in the initial custom design phase". Pedestrian-intention size in C4–C6 "showed larger intervals, pointing to greater preference diversity". The authors also note that "some participants preferred different parameter values as they became more familiar with the environment". — [Jansen et al. 2025, CHI](https://arxiv.org/html/2501.06757v3)
- Wintersberger et al. 2020 (N=56): participants chose freely which objects to augment, and the desire for feedback correlated inversely with situational trust. The authors conclude adaptive or personalised UIs are needed. *Abstract-level.* — [Wintersberger et al. 2020](https://doi.org/10.1145/3409120.3410659)
- Jansen et al. 2025 (TRF): participants explicitly asked for adjustable level of detail. Colley et al. 2021 participants asked for "adjustable color settings", and a few wanted outlines instead of masks or no signposts. — [Jansen et al. 2025, TRF](https://doi.org/10.1016/j.trf.2025.05.013); [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- Currano et al. 2021: driving style interacted with context and HUD complexity in effects on drivers' perceptions and SA. *Abstract-level.* — [Currano et al. 2021](https://doi.org/10.1145/3411764.3445575)
- Tran et al. 2025 call for "adaptive AR interfaces" because the best highlight type depended on scenario complexity, uncertainty and context. This is a situational rather than personal difference. *Abstract-level.* — [Tran et al. 2025](https://diglib.eg.org/handle/10.2312/egve20251351)
- Colley et al. 2021 (open feedback): "Formulated opinions in the open feedback varied." — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)

### Inferences
- Strongest candidates for personalisation, ranked by the evidence:
  1. highlight opacity/alpha (OptiCarVis expert and user spread; custom designs differ from optimised ones);
  2. scope, i.e. which classes or objects are highlighted: pedestrians only, plus vehicles, plus static objects (Wintersberger 2020; Jansen 2025 TRF ranking; Colley 2021 signpost objections);
  3. marker size above pedestrians (OptiCarVis);
  4. highlight style (scenario-dependent; Tran et al. 2025; outline vs mask comments).
- Colour (class hue) has some disagreement, with requests for adjustable colours and complaints about clashes with real-world colours. OptiCarVis deliberately did not optimise colour, so there is no quantitative spread data.

### Gaps
- No study reports per-participant optimal values with a formal test of heterogeneity (e.g., a mixture or latent-class analysis). The OptiCarVis evidence is descriptive (interquartile intervals and expert SDs).
- It is unclear whether preferred values are stable over sessions; OptiCarVis notes drift with familiarity, and the AutoUI '26 multi-session paper may address this but was not verified beyond the abstract.

## Q4. Which properties showed no effect or a clear consensus?

### Takeaway
There is consensus that AR, world-registered highlighting is preferred over tablet or centre-screen rendering of the same information. Highlighting detected objects is preferred over no highlighting, and it is judged reasonable and necessary. Several outcomes were null: trust, mental load and usability for segmentation highlighting vs none, and acceptance and aesthetics across optimised designs. Consensus also exists against flicker, clutter and highlighting static infrastructure such as traffic lights.

### Cited Findings
- AR over tablet: preference and cognitive-load advantages in both Colley et al. 2020 (VR, N=15) and 2021 (online, N=32). The 2022 IMWUT study therefore adopted AR for all conditions. — [Colley et al. 2020](https://doi.org/10.1145/3409120.3410648); [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351); [Colley et al. 2022](https://doi.org/10.1145/3534609)
- Highlighting judged reasonable and necessary: pre-study reasonable M=6.06, necessary M=5.03 (7-point); real-video study 5.00 and 4.56. — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- Null effects of segmentation highlighting vs baseline on trust, mental load and SUS (N=41). — [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- Null effects in IMWUT 2022: no significant overall SA effect; no pairwise differences in perceived safety; no effect on understandability or on clarity of the next AV action. — [Colley et al. 2022](https://doi.org/10.1145/3534609)
- Null effects in OptiCarVis: acceptance (p=.073) and aesthetics (p=.277) did not differ between conditions. Most expert parameter SDs were ≤ 0.18, which the authors read as "a fair degree of alignment" for those parameters. Segmentation highlighting was turned on by 7 of 8 experts. — [Jansen et al. 2025, CHI](https://arxiv.org/html/2501.06757v3)
- Consensus against flicker and colour clutter: TRF 2025 themes (10/25 and 9/25 respondents); Colley et al. 2021 participant requests to exclude traffic lights and stop lights; TRF 2025 excluded unreliable bounding boxes to reduce flicker. — [Jansen et al. 2025, TRF](https://doi.org/10.1016/j.trf.2025.05.013); [Colley et al. 2021](https://doi.org/10.1145/3411764.3445351)
- Rusch et al. 2013: AR hazard cues did not impair perception of non-target objects, and false alarms or misses did not impair responses (manual driving, N=27). This contrasts with later inattentional-blindness findings (Wang et al. 2022 as cited by Goodge et al. 2026; Goodge et al. 2026; de Oliveira Faria & Gabbard 2025 preprint). The attention-capture cost of highlighting is therefore contested, and appears to depend on concurrent task load. — [Rusch et al. 2013](https://stacks.cdc.gov/view/cdc/222186); [Goodge et al. 2026](https://doi.org/10.1145/3807942)

### Inferences
- Properties with consensus are poor personalisation candidates and should be fixed in the study design: AR world-registered placement; no flicker (temporally smoothed detections); no highlighting of traffic lights or stop lights.
- Opacity, scope and size show real spread and no consensus, so they are the best candidates for the ~4 Bayesian-optimisation dimensions. Style (categorical), or a TTC/distance label toggle, could be the fourth, but the evidence for both is thin (Tran et al. 2025, abstract only).

### Gaps
- No study found that tests whether personalised highlighting outperforms a good fixed default for trust calibration (as opposed to trust level). Over-trust risk from optimising for trust or perceived safety is flagged by Colley et al. 2022 but has not been tested under personalisation.
