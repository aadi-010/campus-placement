/**
 * CampusPrep — Aptitude Practice Engine
 */
document.addEventListener('DOMContentLoaded', () => {
    const practiceArea = document.getElementById('practiceArea');
    if (!practiceArea) return;

    let questions = [];
    let currentIndex = 0;
    let selectedOptionIndex = null;
    let answeredQuestions = {}; // question_id -> { selected, is_correct, explanation }
    let sessionCorrect = 0;
    let sessionTotal = 0;
    let questionStartTime = Date.now();

    // DOM Elements
    const qStatement = document.getElementById('qStatement');
    const qOptionsList = document.getElementById('qOptionsList');
    const qDifficultyBadge = document.getElementById('qDifficultyBadge');
    const qTopicBadge = document.getElementById('qTopicBadge');
    const qIndexText = document.getElementById('qIndexText');
    const qBookmarkBtn = document.getElementById('qBookmarkBtn');
    const submitAnswerBtn = document.getElementById('submitAnswerBtn');
    const nextQBtn = document.getElementById('nextQBtn');
    const prevQBtn = document.getElementById('prevQBtn');
    const explanationDrawer = document.getElementById('explanationDrawer');
    const explanationText = document.getElementById('explanationText');
    const shortcutBox = document.getElementById('shortcutBox');
    const shortcutText = document.getElementById('shortcutText');
    const explanationResultHeader = document.getElementById('explanationResultHeader');
    const sessionScoreVal = document.getElementById('sessionScoreVal');
    const sessionProgressBar = document.getElementById('sessionProgressBar');
    const restartSessionBtn = document.getElementById('restartSessionBtn');

    // Fetch questions
    async function loadQuestions() {
        const initId = practiceArea.getAttribute('data-init-id');
        const initCat = practiceArea.getAttribute('data-init-cat') || 'all';
        const initTopic = practiceArea.getAttribute('data-init-topic') || 'all';

        let url = `/aptitude/api/questions?category=${encodeURIComponent(initCat)}&topic=${encodeURIComponent(initTopic)}`;
        try {
            const res = await fetch(url);
            const data = await res.json();
            if (data.success && data.questions.length > 0) {
                questions = data.questions;
                if (initId) {
                    const foundIdx = questions.findIndex(q => q.id == initId);
                    if (foundIdx !== -1) currentIndex = foundIdx;
                }
                renderQuestion();
            } else {
                qStatement.innerHTML = '<span style="color:var(--text-secondary)">No practice questions available for this selection.</span>';
            }
        } catch (err) {
            qStatement.innerHTML = '<span style="color:var(--danger-red)">Failed to load practice questions. Please check connection.</span>';
        }
    }

    function renderQuestion() {
        if (!questions.length || currentIndex >= questions.length) return;

        const q = questions[currentIndex];
        questionStartTime = Date.now();
        selectedOptionIndex = null;

        qStatement.innerText = `Q${currentIndex + 1}. ${q.question}`;
        qTopicBadge.innerText = q.topic;
        qIndexText.innerText = `Question ${currentIndex + 1} of ${questions.length}`;

        // Difficulty badge color
        qDifficultyBadge.innerText = q.difficulty;
        qDifficultyBadge.className = `badge badge-diff-${q.difficulty.toLowerCase()}`;

        // Bookmark button
        qBookmarkBtn.classList.toggle('bookmarked', q.is_bookmarked);
        qBookmarkBtn.innerHTML = `<i data-lucide="${q.is_bookmarked ? 'bookmark-check' : 'bookmark'}"></i>`;
        qBookmarkBtn.onclick = () => toggleBookmark(q);

        // Update progress bar
        const pct = Math.round(((currentIndex + 1) / questions.length) * 100);
        sessionProgressBar.style.width = `${pct}%`;

        // Render Options
        qOptionsList.innerHTML = '';
        const letters = ['A', 'B', 'C', 'D'];
        
        q.options.forEach((optText, idx) => {
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.innerHTML = `
                <span class="option-marker">${letters[idx]}</span>
                <span>${optText}</span>
            `;

            btn.onclick = () => {
                if (answeredQuestions[q.id]) return; // already answered
                document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
                btn.classList.add('selected');
                selectedOptionIndex = idx;
                submitAnswerBtn.disabled = false;
            };

            qOptionsList.appendChild(btn);
        });

        // Navigation state
        prevQBtn.disabled = (currentIndex === 0);
        
        // If already answered in this session
        if (answeredQuestions[q.id]) {
            restoreAnsweredState(q);
        } else {
            submitAnswerBtn.style.display = 'inline-flex';
            submitAnswerBtn.disabled = true;
            nextQBtn.style.display = 'none';
            explanationDrawer.style.display = 'none';
        }

        if (window.lucide) window.lucide.createIcons();
    }

    function restoreAnsweredState(q) {
        const record = answeredQuestions[q.id];
        const buttons = qOptionsList.querySelectorAll('.option-btn');

        buttons.forEach((btn, idx) => {
            btn.disabled = true;
            if (idx === record.correct_option) {
                btn.classList.add('correct');
            } else if (idx === record.selected) {
                btn.classList.add('incorrect');
            }
        });

        showExplanation(record.is_correct, record.explanation, record.shortcut_hint);
        submitAnswerBtn.style.display = 'none';
        nextQBtn.style.display = (currentIndex < questions.length - 1) ? 'inline-flex' : 'none';
    }

    // Submit Answer
    submitAnswerBtn.addEventListener('click', async () => {
        if (selectedOptionIndex === null) return;

        const q = questions[currentIndex];
        const timeTaken = Math.max(1, Math.round((Date.now() - questionStartTime) / 1000));

        submitAnswerBtn.disabled = true;
        submitAnswerBtn.innerText = 'Evaluating...';

        try {
            const res = await fetch('/aptitude/api/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.getCsrfToken()
                },
                body: JSON.stringify({
                    question_id: q.id,
                    selected_option: selectedOptionIndex,
                    time_taken_seconds: timeTaken
                })
            });

            const data = await res.json();
            if (data.success) {
                answeredQuestions[q.id] = {
                    selected: selectedOptionIndex,
                    is_correct: data.is_correct,
                    correct_option: data.correct_option,
                    explanation: data.explanation,
                    shortcut_hint: data.shortcut_hint
                };

                sessionTotal += 1;
                if (data.is_correct) sessionCorrect += 1;
                sessionScoreVal.innerText = `${sessionCorrect} / ${sessionTotal} (${Math.round((sessionCorrect/sessionTotal)*100)}%)`;

                restoreAnsweredState(q);
            } else {
                alert(data.error || 'Submission error');
                submitAnswerBtn.disabled = false;
                submitAnswerBtn.innerText = 'Check Answer';
            }
        } catch (err) {
            alert('Network error while evaluating answer.');
            submitAnswerBtn.disabled = false;
            submitAnswerBtn.innerText = 'Check Answer';
        }
    });

    function showExplanation(isCorrect, expl, shortcut) {
        explanationDrawer.style.display = 'block';
        if (isCorrect) {
            explanationResultHeader.innerHTML = '<span style="color:var(--success-green);"><i data-lucide="check-circle-2"></i> Correct Answer!</span>';
            explanationDrawer.style.borderLeftColor = 'var(--success-green)';
        } else {
            explanationResultHeader.innerHTML = '<span style="color:var(--danger-red);"><i data-lucide="x-circle"></i> Incorrect Answer</span>';
            explanationDrawer.style.borderLeftColor = 'var(--danger-red)';
        }

        explanationText.innerHTML = expl;

        if (shortcut && shortcut.trim()) {
            shortcutBox.style.display = 'block';
            shortcutText.innerText = shortcut;
        } else {
            shortcutBox.style.display = 'none';
        }

        if (window.lucide) window.lucide.createIcons();
    }

    async function toggleBookmark(q) {
        try {
            const res = await fetch('/api/bookmark/toggle', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.getCsrfToken()
                },
                body: JSON.stringify({ item_type: 'aptitude', item_id: q.id })
            });
            const data = await res.json();
            if (data.success) {
                q.is_bookmarked = data.bookmarked;
                qBookmarkBtn.classList.toggle('bookmarked', data.bookmarked);
                qBookmarkBtn.innerHTML = `<i data-lucide="${data.bookmarked ? 'bookmark-check' : 'bookmark'}"></i>`;
                if (window.lucide) window.lucide.createIcons();
                window.showToast(data.message, 'success');
            }
        } catch (err) {
            window.showToast('Failed to bookmark', 'error');
        }
    }

    nextQBtn.addEventListener('click', () => {
        if (currentIndex < questions.length - 1) {
            currentIndex += 1;
            renderQuestion();
        }
    });

    prevQBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex -= 1;
            renderQuestion();
        }
    });

    restartSessionBtn.addEventListener('click', () => {
        if (confirm('Restart practice session from Question 1?')) {
            currentIndex = 0;
            answeredQuestions = {};
            sessionCorrect = 0;
            sessionTotal = 0;
            sessionScoreVal.innerText = '0 / 0';
            renderQuestion();
        }
    });

    // Start loading
    loadQuestions();
});
