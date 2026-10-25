# Which visual properties matter in AV explanation displays

Crowdsourced study to decide, from the literature and from participants watching driving clips, which visual
properties of an automated-vehicle (AV) explanation display are worth personalising. The result is a ranked set of
about four properties, their usable ranges, and fixed values for everything else. A later preference optimisation
(for example [OptiCarVis](https://github.com/Shaadalam9/opticarvis-global)) then tunes only the selected properties.

The code implements the study design: a literature review gives the candidate properties, a crowdsourced study
measures which of them matter and which people disagree about, and pre-registered rules select the final set. The
crowdsourcing setup follows
[bazilinskyy/ehmi-vehicles](https://github.com/bazilinskyy/ehmi-vehicles): a [jsPsych](https://www.jspsych.org) 8
experiment served by Node.js (Express) and stored in MongoDB, deployed on Heroku, with the analysis in Python.

## Experiment
The experiment is in `public/views/experiment.html` and `public/js/experiment.js`. `app.js` serves it and stores the
data in the `entries` collection of a MongoDB database. jsPsych and its plugins are installed from npm and served by
`app.js`.

### Procedure
1. The clips of the participant are preloaded and the browser switches to full screen.
2. Device check: phones, tablets and screens smaller than 1280 × 720 px cannot continue.
3. Welcome, information sheet and consent. Declining ends the study.
4. Demographics (age, nationality, country of residence, gender, driving licence, car use, experience with driver
   assistance, self-driving rides, familiarity with head-up displays).
5. **Task C**: a baseline video of the display, then the open question "What would you want this display to show, or
   show differently?", asked before any property is named.
6. **Task A**: Best-Worst Scaling (jsPsych MaxDiff). Each trial shows 4 properties; the participant picks the most and
   least important for understanding what the car is doing and why. With 21 properties that is 16 trials.
7. **Task B**: A/B video pairs. For each property, the same situation with the property at its low and high level
   (side randomised): did you notice a difference, which would you prefer while riding, how much does it matter
   (1–7), and for each video understanding, perceived safety and mental load (1–7).
8. Five attention checks are mixed in between the trials of Tasks A and B; three wrong answers end the study
   (`finish_fail`).
9. An optional final comment, then the finish page with the participant's completion code.

Data is saved after every trial, so the answers of participants who stop early are kept. The order of trials, the BWS
version, the scene per property and the side of each level are seeded with the worker code.

### Stimuli
`study/properties.json` lists the candidate properties (from the literature review), `study/scenes.json` the driving
situations. Every scene needs, under `public/stimuli/<scene id>/`: `baseline.mp4`, and `<property id>_low.mp4` plus
`<property id>_high.mp4` for every screened-in property. The two clips of a pair must differ in that one property only.
The clips are not in git; `make_design.py` lists the ones that are missing.

After any change to the properties, scenes or settings, regenerate the design:

```bash
uv run python make_design.py
```

This writes `public/design.json`: the balanced BWS design (50 versions), the properties and scenes, and the A/B and
attention settings.

### Running the experiment
Install the dependencies with `npm install` and start the server with
`CONNECTION='<MongoDB connection string>' npm start`, then open http://localhost:3000. Without `CONNECTION` the server
stores the data in `data/entries.jsonl`, in the same shape as a MongoDB export, so the study can be tried without a
database. URL parameters:
* `debug=true`: log details to the browser console, skip the device check, allow continuing before a video ends, show
  the names of missing clips, and mark the data as debug (excluded from the analysis).
* `save_data=false`: do not send data to the server.
* `worker_code=<code>`: participant code to store with the data and show on the finish page. `PROLIFIC_PID` is used
  when present; otherwise a code is generated.

The live study runs on Heroku (`Procfile`, Node.js 22), with the connection string set as the `CONNECTION` config
variable.

## Analysis
The analysis is in the `avprops` package, started by `analysis.py`. Tested with Python 3.12.13 and
[`uv`](https://docs.astral.sh/uv/):

```bash
uv sync
uv run python analysis.py
```

### Configuration
Settings are read from `config` and secrets from `secret` in the repository folder. Both are not in git: create them
from `default.config` and `default.secret`. If there is no `config`, `default.config` is used.

`config`:
* `path_data`, `files_heroku`: folder and files with the data exported from MongoDB.
* `download_data`: export the data from MongoDB into the first of `files_heroku` before the analysis (needs
  `mongoexport` and `mongodb_uri` in `secret`).
* `bws_items_per_trial`, `bws_appearances_per_item`, `bws_design_versions`: the BWS design.
* `ab_pairs_per_participant`: A/B pairs per participant (0 = all properties); `ab_collect_ratings`: ask the three
  ratings for both videos.
* `attention_fail_at`: wrong attention answers that end the study.
* Exclusions: `exclude_debug`, `exclude_unfinished`, `attention_max_wrong`, `min_median_bws_rt_ms`,
  `max_hidden_ab_share` (share of A/B pairs during which the participant left the page).
* Selection rules: `select_n` (4), `noticed_min_share` (0.70), `matters_top_fraction` (0.5),
  `disagreement_max_majority_share` (0.75), `redundancy_min_abs_r` (0.70). Set them in the pilot, then pre-register.

`secret`:
* `mongodb_uri`: connection string of the MongoDB database, including the password.

### Running the analysis
`uv run python analysis.py` reads `files_heroku` in `path_data`; `--data <file>` reads other files, for example
`data/entries.jsonl` from a local run. To export the data by hand:
`mongoexport --uri <mongodb_uri> --collection entries --type json --out data/heroku_0.json`.

Outputs go to `_output/` (not in git, as they hold personal data):
* `participants.csv`: every participant, whether they finished, attention answers, excluded and why.
* `summary.csv`: per property the BWS score with bootstrap CI, share noticing, preference split, importance, rating
  differences with Wilcoxon tests, and its status.
* `redundant.csv`, `open_answers.csv` (for thematic coding of Task C) and `report.md`.

Every property gets a status saying where it stopped: `not noticed`, `does not matter`, `consensus: fix at low/high`,
`redundant with …`, `eligible, below cut-off`, or `selected`.

To check the analysis before real data exists, `simulate.py` writes synthetic participants with a known truth in the
same format as the server:

```bash
uv run python simulate.py --n 150
uv run python analysis.py --data data/simulated/entries.jsonl --out _output/simulated
```

### Tests

```bash
uv run pytest
```
