# Timing, placement and global appearance properties of in-vehicle AV explanation / transparency displays

Scope note: compiled 2026-10-26 from about 25 search/fetch calls. "Verified" means I read the abstract, a press release by the authors' institution, or full text (Colley et al. 2021 CHI, Colley et al. 2022 IMWUT and the Greatbatch et al. slides were read in full text). Items marked UNVERIFIED come from memory or secondary summaries and need checking before they are cited.

## Timing: when explanations are shown (always-on vs event-triggered/adaptive vs on-demand), lead time, duration, animation

### Takeaway
The clearest evidence on timing is that explanations given **before** the AV acts beat explanations given **after** (Du/Haspiel/Robert, Univ. Michigan). Choosing between **always-on and adaptive/risk-triggered** display shows strong **individual differences**: users with low trust prefer permanent information, users with high trust prefer context-adaptive. That makes "display policy / frequency" a good candidate to personalise. I found no peer-reviewed study that varied exact lead-time values in seconds, fade durations or display duration for explanation displays.

### Cited Findings
- **Before vs after action (preliminary).** Haspiel, Du, Meyerson, Robert, Tilbury, Yang & Pradhan (2018), "Explanations and Expectations: Trust Building in Automated Vehicles," HRI '18 Companion. Within-subjects design, 8 participants × 4 AV driving conditions (32 data points). Explanations given before the AV acted produced more trust than explanations given after. — [Deep Blue record](https://deepblue.lib.umich.edu/handle/2027.42/140746?show=full); summary in [Futurity](https://www.futurity.org/trust-self-driving-car-timing-anxiety-2092272/). DOI 10.1145/3173386.3177057 (from memory, UNVERIFIED).
- **Before vs after action (full study).** Du, Haspiel, Zhang, Tilbury, Pradhan, Yang & Robert (2019), Transportation Research Part C (title "Look who's talking now: Implications of AV's explanations on driver's trust, AV preference, anxiety and mental workload" from memory, UNVERIFIED). Simulator, N=32 (11 women), UMTRI. Explanations raised trust only when given before the action. After-the-fact explanations were "not better than giving them no information at all" (Robert). Giving participants a choice was not better than telling them beforehand. Robert also notes that advance explanations need predictive ability the AV will not always have. — [UMSI press release](https://www.si.umich.edu/news/its-easier-trust-automated-vehicles-when-we-know-what-they-plan-do-ahead-time); [TechXplore PDF](https://techxplore.com/news/2019-06-easier-automated-vehicles.pdf). The TR-C DOI and lead times in seconds were not retrieved (see Gaps).
- **Content of explanation (related to timing).** Koo, Kwac, Ju, Steinert, Leifer & Nass (2015), "Why did my car just do that? Explaining semi-autonomous driving actions to improve driver understanding, trust, and performance," IJIDeM 9(4). According to a secondary summary, "why"-only messages gave the least anxiety and the highest trust. In that study the messages were given before the action (my recollection, UNVERIFIED). — secondary summary via [arXiv 2409.05731](https://arxiv.org/pdf/2409.05731). DOI 10.1007/s12008-014-0227-2 (from memory, UNVERIFIED).
- **Constant vs risk-triggered (on-road).** Kim, Yeo, Jo, Rus & Kim (2023), "What and When to Explain? On-road Evaluation of Explanations in Highly Automated Vehicles," Proc. ACM IMWUT 7(3). Real vehicle with mixed reality, passengers of L4/5 vehicles. Two factors: timing (constant vs only in risky scenarios, triggered by traffic-risk probability) and content (perception, attention, perception+attention). Visualising perception improved perceived usability, trust, perceived safety and situation awareness without extra cognitive load. Risk-triggered timing was especially useful when passengers were overwhelmed with information. N was not found in the abstract. — [MIT DSpace](https://dspace.mit.edu/handle/1721.1/152332), DOI [10.1145/3610886](https://doi.org/10.1145/3610886).
- **Permanent vs context-adaptive HMI, split by trust level.** Hartwich, Hollander, Johannmeyer & Krems (2021), "Improving passenger experience and trust in automated vehicles through user-adaptive HMIs: 'The more the better' does not apply to everyone," Frontiers in Human Dynamics. Simulator, N=50 first-time users, split into lower- and higher-trust groups. Any HMI improved perceived safety, understanding, comfort, enjoyment and trust compared with no HMI. Higher-trust users rated the context-adaptive HMI best. Lower-trust users tended to rate the permanent HMI best on safety, understanding and comfort. Overall UX favoured the adaptive HMI. The authors conclude that permanent full information "cannot be recommended as a universal standard". — [OFFIS record](https://www.offis.de/offis/publikation/improving-passenger-experience-and-trust-in-automated-vehicles-through-user-adaptive-hmis-the-more-the-better-does-not-apply-to-everyone.html), DOI [10.3389/fhumd.2021.669030](https://doi.org/10.3389/fhumd.2021.669030).
- **Same dataset, gaze.** Gaze toward the HMI went with higher trust than no HMI. The large difference in information availability between adaptive and permanent HMIs did not produce comparably large differences in gaze or trust. Users preferred the adaptive HMI. — Hollander et al. 2022, Open Psychology, [DOAJ](https://doaj.org/article/f70622e747794e698b935fd823eedcbb).
- **On-demand vs proactive in-vehicle agent.** Frontiers in Psychology (2023), simulator, N=30. Participants rated the on-demand agent as more natural and faster-responding than the proactive one. Takeover compliance was higher with on-demand explanations, but only when system reliability was high. — [Frontiers in Psychology 10.3389/fpsyg.2023.1121622](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1121622/epub). Authors not recorded (UNVERIFIED).
- **Constant warnings vs TOR-only vs gaze-adaptive HUD.** Detjen et al. (Univ. Duisburg-Essen), N=12. Constant warnings became annoying and distracting over time. Gaze-adaptive complexity reduction helped in some respects but distracted some participants. — [UDE publication page](https://hci.informatik.uni-due.de/en/publications/investigating-the-influence-of-gaze-and-context-adaptive-head-up-displays-on-take-over-requests-16621). Year and venue not recorded (UNVERIFIED).
- **Animation.** Merenda, Kim, Tanous, Gabbard, Feichtl, Misu & Suga (2018), "Augmented Reality Interface Design Approaches for Goal-directed and Stimulus-driven Driving Tasks," IEEE TVCG 24(11):2875–2885. Animated AR designs gave some gains in goal-directed navigation tasks but often cost response time and distance. The paper challenges assumptions behind world-fixed conformal design. — [ISMAR 2018 page](https://ismar2018.vgtc.org/papers/tvcg2018_pcs_paper_1040.html), DOI 10.1109/TVCG.2018.2868531.
- **Animation as an uncertainty/urgency code.** Kunze, Summerskill, Marshall & Filtness (2018 AutomotiveUI, N=46 sorting task; 2019 IJMHCI 11(2):75–97) compared 11 visual variables for an AR uncertainty display. Hue and animation-based variables conveyed a clear urgency order and were well received. Less experienced drivers benefited most in takeover performance. — [IDEAS/RePEc 2019 record](https://ideas.repec.org/a/igg/jmhci0/v11y2019i2p75-97.html); [Loughborough repository 2018 paper](https://repository.lboro.ac.uk/articles/Augmented_reality_displays_for_communicating_uncertainty_information_in_automated_driving/9338876/files/16947521.pdf) (full text returned 403, not read).

### Inferences
- **Lead time.** "Before the action" is well supported as a fixed design rule (consensus). The exact lead time in seconds is not established in the sources I found. A parameter range would have to be chosen by the study designers, not taken from the literature.
- **Display policy** (always-on / event-triggered / on-demand) is the timing property with the most direct evidence of individual differences (Hartwich et al. 2021, by trust level). It is a strong candidate for personalisation, possibly as a continuous "persistence" or "risk threshold for showing" parameter.
- **Animation** speeds up some responses but costs others (Merenda 2018), and works as an urgency code (Kunze). It seems better treated as a fixed semantic code than as a free aesthetic parameter.

### Gaps
- No peer-reviewed study found that varies explanation lead time in seconds (e.g., 2 s vs 5 s), display duration, or fade-in/out duration for AV explanations. I did not retrieve the Du et al. 2019 TR-C full text, so its exact timing and lead time are unconfirmed.
- Koo et al. 2015 was not read first-hand. The finding that "why" messages were given before the action needs checking.

## Placement: windshield AR (world-registered) vs HUD (screen-fixed) vs cluster vs central display/tablet

### Takeaway
Across studies, **AR/windshield placement beats central-stack or tablet** on situation awareness, usability, cognitive load and (partly) trust in passenger-oriented AV visualisations (Colley et al. 2021). In takeover contexts, **HUD placement (world- or screen-relative) beats head-down displays** on response measures. The evidence for **world-relative over screen-relative** is mixed and small, and Gabbard's group explicitly cautions that conformal graphics are not inherently better. Placement preferences inside the windshield vary by context and person (Riegler et al. 2022).

### Cited Findings
- **AR windshield vs tablet in the centre stack.** Colley, Eder, Rixen & Rukzio (2021), "Effects of Semantic Segmentation Visualization on Trust, Situation Awareness, and Cognitive Load in Highly Automated Vehicles," CHI '21. Two online studies: simulation (N=32) and real-world video with panoptic segmentation (N=41). Design was 2×2, technology (tablet vs AR) × visualised objects (dynamic vs dynamic+static), plus baseline.
  - Usability: AR dynamic (M=73.75) was rated better than tablet dynamic (M=64.14) and tablet dynamic+static (M=62.66).
  - Cognitive load: significant main effect of technology, lower with AR.
  - Trust: the tablet variants received significantly lower trust than the AR dynamic+static variant (tablet dynamic M=4.59, tablet dynamic+static M=4.65).
  - SART Understanding: higher with AR (M=14.41 vs 12.56).
  - The abstract summarises AR as increasing SA while keeping cognitive load low. — [Ulm PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/1-hci/hci-paper/2021/CHI2021_Semantic_Segmentation.pdf), DOI 10.1145/3411764.3445351.
- **Earlier comparison by the same group.** Colley et al. compared tablet-based vs AR pedestrian-intention visualisation in VR. The AR version was preferred and increased trust (cited in Colley et al. 2022). — [IMWUT 2022 PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/institut/Papers/Prof_Rukzio/2022/IMWUT2022_functional_hierarchy_final.pdf). Original citation not retrieved (UNVERIFIED).
- **World-relative vs screen-relative vs head-down during takeover.** Greatbatch, Kim & Doerzaph (VT/VTTI, IEEE presentation, ~2023), N=21 L3 TOR.
  - Initial response time: HDD 1.97 s, world-relative HUD 1.54 s, screen-relative HUD 1.70 s.
  - TTC: world-relative 2.71 s, screen-relative 2.34 s, HDD 2.11 s.
  - Correct action was 9× as likely with world-relative and 3.5× as likely with screen-relative, compared with HDD.
  - SA did not differ meaningfully (82.45% / 81.69% / 78.55%). — [VTTI slides PDF](https://safed.vtti.vt.edu/wp-content/uploads/2023/09/00-026-IEEE-Presentation.pdf). These are conference slides, so treat them as preliminary.
- **Conformal AR navigation.** Gabbard, Smith, Tanous, Kim & Jonas (2019), "AR DriveSim," Frontiers in Robotics and AI. A user study of two AR navigation interfaces suggests conformal AR graphics may not be inherently better than other HUD interfaces. — [Frontiers](https://www.frontiersin.org/articles/10.3389/frobt.2019.00098/full).
- **Distraction potential.** Kim & Gabbard (2022), "Assessing Distraction Potential of Augmented Reality Head-Up Displays for Vehicle Drivers," Human Factors 64(5):852–865. — [dblp](https://dblp.dagstuhl.de/pid/64/6646.html). Findings not retrieved (UNVERIFIED).
- **Peripheral light strip vs instrument cluster.** Kunze et al. argued against using the instrument cluster for uncertainty information because it could increase workload, and used a peripheral light strip plus a vibrotactile seat (as summarised in Colley et al. 2022). — [IMWUT 2022 PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/institut/Papers/Prof_Rukzio/2022/IMWUT2022_functional_hierarchy_final.pdf).
- **Light bar vs windshield display.** A simulator study (N=18) found a light bar gave better UX than a windshield display and was preferred, with both supporting high trust and neither hurting NDRA performance. — via TU/e Research Portal, "How to Display Vehicle Information to Users of Automated Vehicles When Conducting Non-Driving-Related Activities" ([TU/e record](https://research.tue.nl/en/publications/how-to-display-vehicle-information-to-users-of-automated-vehicles/)). Authors and year not recorded (UNVERIFIED; the attribution to the TU/e record comes from a search summary).
- **Personalised 3D AR windshield.** Riegler, Riener & Holzmann (2022), "Towards Personalized 3D Augmented Reality Windshield Displays in the Context of Automated Driving," Frontiers in Future Transportation 3. VR simulator, N=24. Compared multiple content-specific windows vs one main window, and participants freely adjusted the windows' visual parameters. Preferences varied with context. One main window gave better task performance and shorter takeover times, while multi-window got higher UX ratings. — [Frontiers](https://doi.org/10.3389/ffutr.2022.810698).
- **AR windshield transparency interface (TR-F).** Oliveira et al. (2020), "The influence of system transparency on trust: evaluating interfaces in a highly automated vehicle," TR Part F 72. Tested an AR windscreen overlaying hazards and the vehicle trajectory. — via search summary ([Warwick WRAP](https://wrap.warwick.ac.uk/id/eprint/139407)). Results not retrieved.
- **AR traffic augmentation and trust.** Wintersberger, Frison, Riener & von Sawitzky (2019), "Fostering User Acceptance and Trust in Fully Automated Vehicles: Evaluating the Potential of Augmented Reality," PRESENCE. — [JKU record "Traffic augmentation…"](https://research.jku.at/en/publications/traffic-augmentation-as-a-means-to-increase-trust-in-automated-dr/). A search summary reports that augmenting sensor data in the line of sight increased trust and acceptance (N=26). Not verified first-hand.

### Inferences
- The broad placement class (AR windshield vs central screen) has a fairly consistent direction (AR better on SA, load and usability) and could be **fixed** in favour of the windshield. Within the windshield, **position, number of windows and depth** show context and individual variation (Riegler 2022), which makes them candidate personalisation parameters.
- Whether graphics are world-relative or screen-relative is under-determined by the evidence. Small differences and mixed results suggest it could be an experimental factor, but it is costly to vary in a crowdsourced video study.

### Gaps
- No precise FOV coordinates (degrees of down-angle or lateral offset) recommended specifically for AV explanation content were found in this session.
- Kim & Gabbard 2022 and Merenda 2018 results were not read in full.

## Appearance: colour, contrast/luminance, opacity, diminished reality, clutter

### Takeaway
**Hue** is the strongest variable for coding urgency or uncertainty (Kunze), and AV visualisation papers commonly use blue tones for "certain/normal". For HUD **luminance contrast**, engineering guidance puts the ratio at about **1.15–1.5** (above about 4 is uncomfortable), with a 1.1 luminance ratio as the point where AR-HUD graphics start to hurt recognition of background objects. **Clutter** rises measurably as more explanation layers are added (prediction layer: clutter 4.16 vs 2.53 on a 7-point scale). I found **no peer-reviewed study of "diminished reality"** (de-emphasising the scene) for AV passengers or drivers. No AV-explanation study on colour-vision deficiency was found.

### Cited Findings
- **Hue and animation for urgency.** Kunze et al. (2018 AutoUI, N=46): among 11 visual variables, colour-based and animation-based variables, especially hue, conveyed a consistent order of urgency/uncertainty and were well received. The thesis reports high preference ratings for hue and animation changes. — [IDEAS](https://ideas.repec.org/a/igg/jmhci0/v11y2019i2p75-97.html); [Kunze thesis](https://repository.lboro.ac.uk/articles/thesis/Enhancing_user_experience_and_safety_in_the_context_of_automated_driving_through_uncertainty_communication/10266722). Results for transparency, brightness and saturation were not retrieved.
- **Example AV colour palette.** Colley et al. (2022) colour-coded pedestrians, other vehicles (blue) and signposts (yellow), and used light vs dark blue for pedestrian intention (stay vs cross). Trajectory arrows used a blue→pink gradient, with bluer meaning more certain. — [IMWUT 2022 PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/institut/Papers/Prof_Rukzio/2022/IMWUT2022_functional_hierarchy_final.pdf), DOI 10.1145/3534609.
- **Colour in segmentation.** Colley et al. (2021) surveyed colourisations used in semantic-segmentation publications and used a fixed set of class colours. — [CHI 2021 PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/1-hci/hci-paper/2021/CHI2021_Semantic_Segmentation.pdf).
- **Clutter and number of layers.** Colley, Rädler, Glimmann & Rukzio (2022), IMWUT 6(2) Art. 49. Online between-subjects study, N=216, real-world video with a simulated AR windshield. Compared detection, prediction and planning visualisations and their combinations.
  - Adding Situation Prediction raised perceived clutter (M=4.16, SD=1.85 vs M=2.53, SD=1.74; χ²(1)=37.48, p<.001).
  - Prediction visualisations were rated worse than the other levels.
  - A negative view of the visualisation lowered judged AV ability.
  - The authors note signs of overtrust. — [Ulm PDF](https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.100/institut/Papers/Prof_Rukzio/2022/IMWUT2022_functional_hierarchy_final.pdf), DOI 10.1145/3534609.
- **Salient HUD elements can distract** from critical scene parts during a TOR (Detjen et al.). — [UDE](https://hci.informatik.uni-due.de/en/publications/investigating-the-influence-of-gaze-and-context-adaptive-head-up-displays-on-take-over-requests-16621).
- **HUD contrast ratio.** Defined as (display + ambient luminance)/ambient. A clearly visible HUD image needs about 1.15–1.5, and ratios above 4 can be uncomfortable. — [Analog Devices design note](https://www.analog.com/en/design-notes/come-rain-or-come-shine1--automotive-headsup-displays-must-work-everyday.html). This is industry guidance, not peer-reviewed.
- **AR-HUD occlusion.** Hosokawa et al. (2024), IATSS Research: a luminance ratio of about 1.1 is the threshold at which an AR-HUD starts to affect recognition of background road objects. — [DOAJ](https://doaj.org/article/9bdae11495ec4f4ca9a0055f9e703e5f). Read only as a search-summary; full text UNVERIFIED.
- **Chromaticity vs luminance contrast.** A larger chromaticity difference between symbol and background lowers the luminance contrast needed. Low-luminance environments need more contrast. — [Electronics Optics & Control](https://researching.cn/articles/OJ1db8c4dae8481075). Search summary only, UNVERIFIED.
- **Older DOT guidance.** Contrast needs have not been studied empirically across representative driving situations. A 1.4:1 contrast may suffice for older drivers in the lab. — [FHWA-RD-98-057 ch.3](https://www.fhwa.dot.gov/publications/research/safety/98057/ch03.cfm).
- **Diminished reality.** No study using this term for AV in-vehicle displays was found in two targeted searches (see Gaps).
- **Information amount vs trust.** Kim et al. (2023) found that risk-triggered display helps when passengers are overwhelmed. Hartwich et al. (2021) found that "more is better" does not hold for everyone. — links above.

### Inferences
- **Colour semantics** (hue as urgency or uncertainty) works best as a fixed code to protect meaning. A **global palette or accent hue** within a semantic-safe set could be personalised. CVD-safe constraints should be built into the parameter range.
- **Overlay opacity/brightness** has a physical floor and ceiling: contrast ratio about 1.15–1.5 to be visible, and occlusion of road objects from about 1.1 luminance ratio. That supports a bounded continuous range for personalisation.
- **Amount of content / number of simultaneous elements** shows a measurable clutter cost and individual variation. It is a strong candidate dimension, for example "information density" or "which layers shown".

### Gaps
- No peer-reviewed AV study varying **overlay opacity/transparency** levels for explanation graphics was retrieved. Kunze's 11-variable study may include transparency, but its full text returned 403.
- No study found on **diminished reality / background dimming** in AV contexts. This is novel territory and has no direct empirical precedent in what I found.
- No AV-display study of **colour-vision deficiency** was found.

## Guidelines and standards

### Takeaway
The standards set legibility and glance limits, but they mostly do **not** cover AR-HUD explanation graphics. ISO 15008 explicitly excludes HUDs. NHTSA's 2 s / 12 s glance criteria apply to visual-manual tasks while driving.

### Cited Findings
- **NHTSA Visual-Manual Driver Distraction Guidelines, Phase 1 (2013, OE devices).** Single glances ≤2 s and total eyes-off-road ≤12 s per task; also limits on manual inputs. Phase 2 covers portable and aftermarket devices. — [NHTSA Strickland remarks PDF](https://www.nhtsa.gov/sites/nhtsa.gov/files/strickland-distraction_guidelines_03122012.pdf); [Autoblog 2013](https://www.autoblog.com/2013/04/25/nhtsa-voluntary-guidelines-distracted-driving/); [SWOV on Phase 2](https://swov.nl/en/publicatie/visual-manual-nhtsa-driver-distraction-guidelines-portable-and-aftermarket-devices).
- **ISO 15008:2017** (in-vehicle presentation of visual information, ergonomic specifications and test procedures). Sets minimum legibility, contrast and font-size requirements for changeable information while driving. It covers character legibility and colour recognition, and it **excludes** HUDs, camera images, maps and coding. Confirmed 2025, with a revision (CD) in progress. — [ISO 62784](https://www.iso.org/standard/62784.html); [iTeh preview](https://iteh.es/catalog/standards/iso/d07adfe7-f551-4557-bb09-7236d8491cf6/iso-15008-2017). Specific numeric values (character height in arcmin, contrast ratios) were not retrieved, so they are UNVERIFIED.
- **SAE J1757-2 (2018).** Optical measurement of automotive HUDs (w-HUD, c-HUD, with references to AR-HUD) under simulated ambient light. Gives reference values but no compliance thresholds. — [SAE Mobilus](https://saemobilus.sae.org/standards/j1757-2_201811-standard-optical-system-hud-automotive), DOI 10.4271/J1757-2_201811.

### Inferences
- In a passenger-oriented AV study (L4), the NHTSA glance limits apply less directly. They still give a reasonable bound if the display is meant for L2/L3 drivers.

### Gaps
- No content was found for **ISO 2575** (tell-tale symbols and colours: red = danger, yellow/amber = caution, green = function on, blue = high beam; this is from memory, UNVERIFIED) or the **JAMA** guideline. Specific Gabbard/Riener AR-HUD design guidelines with numeric levels were also not retrieved.

## Personalise vs fix

### Takeaway
The best-supported candidates for personalisation are **information amount / display policy (always-on vs adaptive)**, **content layout and placement within the windshield**, and probably **overlay intensity (opacity/brightness within legibility limits)** and **accent palette**. The properties to fix are explanation timing relative to the action (before), semantic colour coding (hue for urgency), and use of the windshield/AR placement class.

### Cited Findings
- Preference for adaptive vs permanent information flips with users' initial trust. — [Hartwich et al. 2021](https://doi.org/10.3389/fhumd.2021.669030).
- Preferences for windshield content parameters differ by context, and performance and UX conflict between one window and many. — [Riegler et al. 2022](https://doi.org/10.3389/ffutr.2022.810698).
- Need for transparency visualisations varies across participants (secondary summary of a trust study). — [JKU record](https://research.jku.at/en/publications/traffic-augmentation-as-a-means-to-increase-trust-in-automated-dr/). UNVERIFIED wording.
- **Direct precedent for Bayesian optimisation of AV visualisation parameters.** Colley, Jansen, Krauss & Rukzio (2026), "Multi-Session User Experience Assessments of Computationally Optimized Automated Vehicle Functionality Visualizations," arXiv:2607.28552, accepted to AutomotiveUI 2026. Multi-objective Bayesian optimisation over AV visualisation design parameters for trust and perceived safety while minimising cognitive load, N=74 online over multiple sessions. The method found parameter values that improved trust, safety and predictability. The authors note shortcomings of the method when optimising subjective measures. The parameter set was not visible in the abstract page. — [arXiv](https://arxiv.org/abs/2607.28552). A related earlier paper by Jansen/Colley et al., Jansen et al. (2025) (CHI 2025, from memory, UNVERIFIED), should be checked for the exact parameters (likely including transparency, colour and which elements are shown).
- Clutter and evaluations of the visualisation also drive capability judgements (risk of overtrust). — [Colley et al. 2022](https://doi.org/10.1145/3534609).

### Inferences
- A sensible 4-property set grounded in this evidence:
  1. Information density / layers shown (or show-policy threshold).
  2. Overlay opacity/intensity, bounded by contrast-ratio limits.
  3. Accent colour within a CVD-safe set, with urgency hue kept fixed.
  4. Vertical position or size of the screen-fixed info panel on the windshield.
- Lead time and world-vs-screen registration should be fixed or treated as between-subjects factors.
- Before finalising, check the parameter list in Jansen et al. (CHI 2025) and in arXiv:2607.28552 to avoid duplicating it and to reuse validated ranges.

### Gaps
- No study found that directly measures the **variance of preferences** for colour or opacity in AV displays. Calling them "worth personalising" is my inference, not an empirical finding.
