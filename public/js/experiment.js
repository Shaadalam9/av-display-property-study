// Experiment for the AV display property study, built with jsPsych 8 in the same way
// as bazilinskyy/ehmi-vehicles: URL parameters, a worker code, full screen and a device
// check, attention checks that end the study after too many mistakes, and data sent to
// the server after every trial.
//
// Timeline: preload -> full screen -> device check -> welcome and consent -> demographics
// -> baseline video + open question (Task C) -> Best-Worst Scaling (Task A, MaxDiff)
// -> A/B video pairs (Task B) -> final comment -> finish page with the worker code.
//
// URL parameters:
//   debug=true          log to the console, skip the device check, allow continuing
//                       before a video ends, and mark every row debug = true
//   save_data=false     do not send data to the server
//   worker_code=<code>  code of the participant (PROLIFIC_PID is used when present;
//                       otherwise one is generated and shown on the finish page)
'use strict';

var SAVE_DATA = true;  // save data or not

function getUrlParameter(name) {
    return new URLSearchParams(window.location.search).get(name);
}

var debug = /^true$/i.test(getUrlParameter('debug') || '');
var save_data = getUrlParameter('save_data') === null ? SAVE_DATA : /^true$/i.test(getUrlParameter('save_data'));

/**
 * Code of the participant: worker_code or PROLIFIC_PID from the URL, or a new one.
 */
function getWorkerCode() {
    var code = getUrlParameter('worker_code') || getUrlParameter('PROLIFIC_PID');
    if (code && /^[A-Za-z0-9_-]{1,64}$/.test(code)) {
        return code;
    }
    var random_num = Math.floor(Math.random() * 10000);
    return 'AV' + Date.now() + 'D' + random_num;
}
var worker_code = getWorkerCode();
if (debug) {
    console.log('worker_code', worker_code, 'save_data', save_data);
}

var excluded = false;  // set when the participant cannot or does not continue
var blurred_trials = new Set();  // trial indices during which the tab or window lost focus

var jsPsych = initJsPsych({
    on_finish: function() {
        if (excluded) return;  // keep the message on screen
        window.location = 'finish?work=' + encodeURIComponent(worker_code);
    },
    on_interaction_data_update: function(data) {
        if (data.event === 'blur') blurred_trials.add(data.trial);
    }
});

// Same participant code, same order of trials and stimuli.
jsPsych.randomization.setSeed(worker_code);

var last_saved_index = -1;  // trial_index of the last row sent to the server

/**
 * Save data. Sends only rows not sent before. Optional callback runs once the data is stored.
 */
function saveData(on_saved) {
    if (!save_data) {
        if (on_saved) on_saved();
        return;
    }
    var new_rows = jsPsych.data.get().filterCustom(function(row) { return row.trial_index > last_saved_index; });
    if (new_rows.count() === 0) {
        if (on_saved) on_saved();
        return;
    }
    last_saved_index = new_rows.last(1).values()[0].trial_index;
    var body = new_rows.json();
    var send = function(attempt) {
        fetch('experiment-data', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: body })
            .then(function(response) {
                if (!response.ok) throw new Error('HTTP ' + response.status);
                if (debug) console.log('data saved', new_rows.count(), 'rows');
                if (on_saved) on_saved();
            })
            .catch(function(err) {
                if (attempt < 3) {
                    setTimeout(function() { send(attempt + 1); }, 2000 * attempt);
                } else {
                    alert('A problem occurred while saving your answers. Please contact the researcher.');
                }
            });
    };
    send(1);
}

var save_data_block = {
    type: jsPsychCallFunction,
    func: function() { saveData(); }
};

/** Mark whether the participant left the page during this trial. */
function markHidden(data) {
    data.hidden = blurred_trials.has(data.trial_index);
}

function videoTag(src) {
    return '<div class="video-wrap"><video src="' + src + '" autoplay muted loop playsinline controls></video></div>';
}

/** In debug mode, name a missing clip on screen instead of showing a black box. */
function flagMissingVideos() {
    document.querySelectorAll('video').forEach(function(video) {
        var source = video.querySelector('source');
        // the error fires on <source> when the video uses one (video-button-response does)
        (source || video).addEventListener('error', function() {
            var note = document.createElement('div');
            note.className = 'video-missing';
            note.textContent = debug ? 'Clip not available yet: ' + (source || video).getAttribute('src')
                : 'This video could not be loaded. Please reload the page.';
            video.parentNode.style.position = 'relative';
            video.parentNode.appendChild(note);
        });
    });
}

function scaleHtml(name, points, low, high) {
    var html = '<div class="scale"><span class="anchor">' + low + '</span>';
    for (var i = 1; i <= points; i++) {
        html += '<label><input type="radio" name="' + name + '" value="' + i + '"' + (i === 1 ? ' required' : '') + '>' + i + '</label>';
    }
    return html + '<span class="anchor">' + high + '</span></div>';
}

function choiceHtml(name, options) {
    return '<div class="scale">' + options.map(function(o, i) {
        return '<label><input type="radio" name="' + name + '" value="' + o[0] + '"' + (i === 0 ? ' required' : '') + '>' + o[1] + '</label>';
    }).join('') + '</div>';
}

/**
 * Build the timeline from design.json (written by make_design.py).
 */
function buildTimeline(design) {
    jsPsych.data.addProperties({
        worker_code: worker_code,
        study_id: design.study_id,
        design_generated_at: design.generated_at,
        debug: debug,
        prolific_study_id: getUrlParameter('STUDY_ID') || '',
        prolific_session_id: getUrlParameter('SESSION_ID') || ''
    });

    var props = {};
    design.properties.forEach(function(p) { props[p.id] = p; });

    // --- per-participant assignment
    var bws_version = Math.floor(Math.random() * design.bws.versions.length);
    var bws_trials = design.bws.versions[bws_version];
    // each property's pair uses one of the scenes where its clips visibly differ
    // (design.ab.scenes, from render_stimuli.py --check)
    var scene_offset = Math.floor(Math.random() * design.scenes.length);
    var ab_plan = jsPsych.randomization.shuffle(Object.keys(props))
        .slice(0, design.ab.pairs_per_participant)
        .map(function(prop, i) {
            var allowed = design.ab.scenes[prop];
            var a_level = Math.random() < 0.5 ? 'low' : 'high';
            return { property: prop, scene: allowed[(i + scene_offset) % allowed.length],
                     a_level: a_level, b_level: a_level === 'low' ? 'high' : 'low' };
        });
    // stimulus_url (config): stimuli/ when the server has the clips, or the URL where they are hosted
    var clip = function(scene, name) { return design.stimulus_url + scene + '/' + name + '.mp4'; };
    var baseline_clip = clip(design.baseline_scene, 'baseline');

    var timeline = [];

    // --- preload, full screen, device check
    var videos = [baseline_clip];
    ab_plan.forEach(function(p) {
        videos.push(clip(p.scene, p.property + '_low'), clip(p.scene, p.property + '_high'));
    });
    timeline.push({
        type: jsPsychPreload,
        video: videos,
        show_progress_bar: true,
        continue_after_error: true,
        max_load_time: 300000,
        data: { task: 'preload' }
    });
    timeline.push({ type: jsPsychFullscreen, fullscreen_mode: true });
    if (!debug) {
        timeline.push({
            type: jsPsychBrowserCheck,
            features: ['width', 'height', 'browser', 'browser_version', 'mobile', 'os'],
            minimum_width: 1280,
            minimum_height: 720,
            inclusion_function: function(data) { return !data.mobile; },
            exclusion_message: function(data) {
                excluded = true;
                return '<h1>Unable to participate</h1><p>' + (data.mobile ? STUDY_TEXT.mobile : STUDY_TEXT.tooSmall) + '</p>';
            },
            data: { task: 'browser_check' }
        });
    }

    // --- welcome and consent
    timeline.push({
        type: jsPsychInstructions,
        pages: [STUDY_TEXT.welcome, STUDY_TEXT.consent],
        show_clickable_nav: true,
        data: { task: 'instructions', bws_version: bws_version, ab_plan: ab_plan,
                window_width_init: window.innerWidth, window_height_init: window.innerHeight }
    });
    timeline.push({
        type: jsPsychSurveyMultiChoice,
        questions: [{ prompt: STUDY_TEXT.consentQuestion, name: 'consent', options: ['Yes', 'No'], required: true }],
        data: { task: 'consent' },
        on_finish: function(data) {
            if (data.response.consent !== 'Yes') {
                excluded = true;
                saveData(function() { jsPsych.abortExperiment(STUDY_TEXT.declined); });
            }
        }
    });

    // --- demographics
    timeline.push({
        type: jsPsychSurveyText,
        preamble: '<h1>About you</h1>',
        questions: [
            { prompt: 'Age', name: 'age', required: true },
            { prompt: 'Nationality', name: 'nationality', required: true },
            { prompt: 'Country of current residence', name: 'country_residence', required: true }
        ],
        data: { task: 'demographics' },
        on_load: function() {
            // native form validation: the browser blocks submitting until the age is valid
            var age = document.querySelector('input[data-name="age"]');
            age.type = 'number';
            age.min = 18;
            age.max = 99;
            age.step = 1;
        }
    });
    timeline.push({
        type: jsPsychSurveyMultiChoice,
        preamble: '<h1>About you</h1>',
        questions: [
            { prompt: 'Gender', name: 'gender', options: ['Female', 'Male', 'Other', 'Prefer not to say'], required: true },
            { prompt: 'Do you have a driving licence?', name: 'licence', options: ['Yes', 'No'], required: true },
            { prompt: 'How often do you travel by car (as driver or passenger)?', name: 'car_frequency', options: ['Daily', 'A few times a week', 'A few times a month', 'Rarely or never'], required: true },
            { prompt: 'How much experience do you have with driver-assistance or self-driving features?', name: 'automation_experience', options: ['None', 'A little', 'Some', 'A lot'], required: true },
            { prompt: 'Have you ever ridden in a car that drives itself?', name: 'av_ride', options: ['Yes', 'No'], required: true },
            { prompt: 'How familiar are you with head-up or augmented-reality displays in cars?', name: 'ar_familiarity', options: ['Not at all', 'Slightly', 'Moderately', 'Very'], required: true }
        ],
        data: { task: 'demographics' }
    });
    timeline.push(save_data_block);

    // --- Task C: baseline video and open question
    timeline.push({
        type: jsPsychVideoButtonResponse,
        stimulus: [baseline_clip],
        prompt: '<p>' + STUDY_TEXT.baselineIntro + '</p>',
        choices: ['Continue'],
        response_allowed_while_playing: debug,
        width: 960,
        data: { task: 'baseline', scene: design.baseline_scene },
        on_load: flagMissingVideos,
        on_finish: markHidden
    });
    timeline.push({
        type: jsPsychSurveyText,
        questions: [{ prompt: STUDY_TEXT.openQuestion, name: 'open', rows: 6, columns: 80, required: true }],
        data: { task: 'open_question', scene: design.baseline_scene },
        on_finish: markHidden
    });
    timeline.push(save_data_block);

    // --- Task A and Task B trials, with the attention checks between them
    var bws_blocks = bws_trials.map(function(items, t) {
        var alternatives = items.map(function(id) {
            var p = props[id];
            return '<div class="alt"><strong>' + p.name + '</strong><br>' + p.description +
                '<br><span class="levels">' + p.low + ' &hellip; ' + p.high + '</span></div>';
        });
        return {
            type: jsPsychMaxdiff,
            preamble: '<h2>Which matters most? (' + (t + 1) + ' of ' + bws_trials.length + ')</h2>' +
                '<p>For understanding what the car is doing and why.</p>',
            alternatives: alternatives,
            labels: ['Most important', 'Least important'],
            required: true,
            data: { task: 'bws', trial: t, items: items },
            on_finish: function(data) {
                data.best = items[alternatives.indexOf(data.response.left)];
                data.worst = items[alternatives.indexOf(data.response.right)];
                markHidden(data);
            }
        };
    });

    var points = design.ab.scale_points;
    var ab_blocks = ab_plan.map(function(plan, i) {
        var html =
            '<h2>Compare the videos (' + (i + 1) + ' of ' + ab_plan.length + ')</h2>' +
            '<div class="pair"><div><h3>Video A</h3>' + videoTag(clip(plan.scene, plan.property + '_' + plan.a_level)) + '</div>' +
            '<div><h3>Video B</h3>' + videoTag(clip(plan.scene, plan.property + '_' + plan.b_level)) + '</div></div>' +
            '<div class="questions">' +
            '<p class="q">Did you notice a difference between the displays in A and B?</p>' + choiceHtml('noticed', [['yes', 'Yes'], ['no', 'No']]) +
            '<p class="q">Which would you prefer to have while riding in a car that drives itself?</p>' + choiceHtml('preferred', [['A', 'Video A'], ['B', 'Video B']]) +
            '<p class="q">How much does the difference between A and B matter to you?</p>' + scaleHtml('importance', points, 'Not at all', 'Very much');
        if (design.ab.collect_ratings) {
            var items = [['understanding', 'I understood what the car was doing and why.'],
                         ['safety', 'The car felt safe.'],
                         ['load', 'The display was distracting or hard to process.']];
            html += '<div class="ratings">' + ['A', 'B'].map(function(option) {
                return '<div><h3>Video ' + option + '</h3>' + items.map(function(item) {
                    return '<p class="q">' + item[1] + '</p>' + scaleHtml(option + '_' + item[0], points, 'Strongly disagree', 'Strongly agree');
                }).join('') + '</div>';
            }).join('') + '</div>';
        }
        html += '</div>';
        return {
            type: jsPsychSurveyHtmlForm,
            html: html,
            button_label: 'Continue',
            data: { task: 'ab', index: i, property: plan.property, scene: plan.scene, a_level: plan.a_level, b_level: plan.b_level },
            on_load: flagMissingVideos,
            on_finish: function(data) {
                var r = data.response;
                data.noticed = r.noticed === 'yes';
                data.preferred_option = r.preferred;
                data.preferred_level = r.preferred === 'A' ? plan.a_level : plan.b_level;
                data.importance = Number(r.importance);
                if (design.ab.collect_ratings) {
                    var ratings = {};
                    [['A', plan.a_level], ['B', plan.b_level]].forEach(function(pair) {
                        ratings[pair[1]] = {
                            understanding: Number(r[pair[0] + '_understanding']),
                            safety: Number(r[pair[0] + '_safety']),
                            load: Number(r[pair[0] + '_load'])
                        };
                    });
                    data.ratings = ratings;
                }
                markHidden(data);
            }
        };
    });

    // attention checks go before randomly chosen trials of either part
    var attention_wrong = 0;
    var questions = jsPsych.randomization.shuffle(ATTENTION_QUESTIONS);
    var n_trials = bws_blocks.length + ab_blocks.length;
    var slots = jsPsych.randomization.shuffle(Array.from({ length: n_trials }, function(_, k) { return k; }))
        .slice(0, Math.min(questions.length, n_trials));
    var attentionBlock = function(q, k) {
        return {
            type: jsPsychSurveyMultiChoice,
            questions: [{ prompt: q.question, name: 'attention', options: q.options, required: true }],
            data: { task: 'attention', question: q.question, expected: q.correct },
            on_finish: function(data) {
                data.correct = data.response.attention === q.correct;
                if (!data.correct) {
                    attention_wrong++;
                    if (debug) console.log('wrong attention answer, total', attention_wrong);
                    if (attention_wrong >= design.attention_fail_at) {
                        excluded = true;
                        saveData(function() { window.location = 'finish_fail'; });
                    }
                }
            }
        };
    };
    var pushTrial = function(block, k) {
        var slot = slots.indexOf(k);
        if (slot !== -1) timeline.push(attentionBlock(questions[slot], k));
        timeline.push(block);
        timeline.push(save_data_block);
    };

    timeline.push({ type: jsPsychInstructions, pages: [STUDY_TEXT.bwsIntro], show_clickable_nav: true });
    bws_blocks.forEach(function(block, k) { pushTrial(block, k); });
    timeline.push({ type: jsPsychInstructions, pages: [STUDY_TEXT.abIntro], show_clickable_nav: true });
    ab_blocks.forEach(function(block, k) { pushTrial(block, bws_blocks.length + k); });

    // --- end
    timeline.push({
        type: jsPsychSurveyText,
        questions: [{ prompt: STUDY_TEXT.finalComment, name: 'comment', rows: 5, columns: 80, required: false }],
        data: { task: 'final' }
    });
    timeline.push(save_data_block);
    timeline.push({ type: jsPsychFullscreen, fullscreen_mode: false });

    if (debug) {
        console.log('BWS version', bws_version, 'A/B plan', ab_plan, 'attention before trials', slots);
    }
    return timeline;
}

fetch('design.json', { cache: 'no-store' })
    .then(function(response) {
        if (!response.ok) throw new Error('design.json: HTTP ' + response.status);
        return response.json();
    })
    .then(function(design) { jsPsych.run(buildTimeline(design)); })
    .catch(function(err) {
        document.body.innerHTML = '<p>The study could not be loaded. Please reload the page.</p>';
        console.error(err);
    });
