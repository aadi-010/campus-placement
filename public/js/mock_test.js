/**
 * CampusPrep — Mock Test Timed Engine
 */
document.addEventListener('DOMContentLoaded', () => {
    const workspace = document.getElementById('mockTestWorkspace');
    if (!workspace) return;

    const attemptId = workspace.getAttribute('data-attempt-id');
    let remainingSeconds = parseInt(workspace.getAttribute('data-remaining') || '0', 10);

    const questionsDataEl = document.getElementById('mockQuestionsData');
    if (!questionsDataEl) return;
    const questions = JSON.parse(questionsDataEl.textContent);

    let currentIndex = 0;

    // DOM Elements
    const countdownTimerDigits = document.getElementById('countdownTimerDigits');
    const mockQuestionStatement = document.getElementById('mockQuestionStatement');
    const mockOptionsList = document.getElementById('mockOptionsList');
    const currentTopicBadge = document.getElementById('currentTopicBadge');
    const currentQuestionNumText = document.getElementById('currentQuestionNumText');
    const markReviewCheckbox = document.getElementById('markReviewCheckbox');
    const btnNextMockQ = document.getElementById('btnNextMockQ');
    const btnPrevMockQ = document.getElementById('btnPrevMockQ');
    const btnClearSelection = document.getElementById('btnClearSelection');
    const submitTestForm = document.getElementById('submitTestForm');

    // 1. Countdown Timer
    function updateTimer() {
        if (remainingSeconds <= 0) {
            countdownTimerDigits.innerText = "00:00";
            countdownTimerDigits.style.color = "var(--danger-red)";
            alert("⏰ Time has expired! Your test is being auto-submitted.");
            submitTestForm.submit();
            return;
        }

        const mins = Math.floor(remainingSeconds / 60);
        const secs = remainingSeconds % 60;
        countdownTimerDigits.innerText = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

        if (remainingSeconds < 300) {
            countdownTimerDigits.style.color = "var(--danger-red)";
        }

        remainingSeconds -= 1;
    }

    updateTimer();
    const timerInterval = setInterval(updateTimer, 1000);

    // 2. Render Current Question
    function renderQuestion(index) {
        if (index < 0 || index >= questions.length) return;
        currentIndex = index;
        const q = questions[currentIndex];

        currentTopicBadge.innerText = q.topic;
        currentQuestionNumText.innerText = `Question ${currentIndex + 1} of ${questions.length}`;
        mockQuestionStatement.innerText = `Q${currentIndex + 1}. ${q.question}`;

        markReviewCheckbox.checked = boolVal(q.is_marked);

        // Options
        mockOptionsList.innerHTML = '';
        const letters = ['A', 'B', 'C', 'D'];

        q.options.forEach((optText, optIdx) => {
            const btn = document.createElement('button');
            btn.className = 'option-btn' + (q.selected_option === optIdx ? ' selected' : '');
            btn.innerHTML = `
                <span class="option-marker">${letters[optIdx]}</span>
                <span>${optText}</span>
            `;

            btn.onclick = () => selectOption(optIdx);
            mockOptionsList.appendChild(btn);
        });

        // Navigation state
        btnPrevMockQ.disabled = (currentIndex === 0);
        btnNextMockQ.querySelector('span').innerText = (currentIndex === questions.length - 1) ? 'Finish & Review' : 'Next';

        // Update Palette buttons
        updatePaletteUI();
    }

    function boolVal(v) {
        return v === true || v === 'true' || v === 1;
    }

    // 3. Option Selection & Answer Record
    async function selectOption(optIndex) {
        const q = questions[currentIndex];
        q.selected_option = optIndex;

        // Re-render options active state
        document.querySelectorAll('#mockOptionsList .option-btn').forEach((b, i) => {
            b.classList.toggle('selected', i === optIndex);
        });

        updatePaletteUI();
        await saveAnswerToServer(q.question_id, optIndex, q.is_marked);
    }

    // Clear Selection
    btnClearSelection.addEventListener('click', async () => {
        const q = questions[currentIndex];
        q.selected_option = null;
        document.querySelectorAll('#mockOptionsList .option-btn').forEach(b => b.classList.remove('selected'));
        updatePaletteUI();
        await saveAnswerToServer(q.question_id, null, q.is_marked);
    });

    // Mark for Review
    markReviewCheckbox.addEventListener('change', async () => {
        const q = questions[currentIndex];
        q.is_marked = markReviewCheckbox.checked;
        updatePaletteUI();
        await saveAnswerToServer(q.question_id, q.selected_option, q.is_marked);
    });

    async function saveAnswerToServer(questionId, selectedOption, isMarked) {
        try {
            const res = await fetch(`/mock-tests/api/${attemptId}/answer`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.getCsrfToken()
                },
                body: JSON.stringify({
                    question_id: questionId,
                    selected_option: selectedOption,
                    is_marked: isMarked
                })
            });
            const data = await res.json();
            if (data.expired) {
                alert('Time expired on server.');
                submitTestForm.submit();
            }
        } catch (e) {
            console.warn('Network issue recording answer:', e);
        }
    }

    function updatePaletteUI() {
        questions.forEach((q, idx) => {
            const btn = document.getElementById(`paletteBtn_${idx}`);
            if (!btn) return;

            btn.classList.toggle('current', idx === currentIndex);
            btn.classList.toggle('answered', q.selected_option !== null && q.selected_option !== undefined);
            btn.classList.toggle('marked', boolVal(q.is_marked));
        });
    }

    // Palette Click handler
    document.querySelectorAll('.palette-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const idx = parseInt(btn.getAttribute('data-index'), 10);
            renderQuestion(idx);
        });
    });

    // Next & Prev
    btnNextMockQ.addEventListener('click', () => {
        if (currentIndex < questions.length - 1) {
            renderQuestion(currentIndex + 1);
        }
    });

    btnPrevMockQ.addEventListener('click', () => {
        if (currentIndex > 0) {
            renderQuestion(currentIndex - 1);
        }
    });

    // Initialize first question
    renderQuestion(0);
});
