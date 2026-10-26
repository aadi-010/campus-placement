/**
 * CampusPrep — Coding Lab Execution Engine
 */
document.addEventListener('DOMContentLoaded', () => {
    const codingLabSplit = document.getElementById('codingLabSplit');
    if (!codingLabSplit) return;

    const challengeId = codingLabSplit.getAttribute('data-id');
    const codeEditor = document.getElementById('codeEditor');
    const runCodeBtn = document.getElementById('runCodeBtn');
    const submitCodeBtn = document.getElementById('submitCodeBtn');
    const resetStarterCodeBtn = document.getElementById('resetStarterCodeBtn');
    const draftSaveStatus = document.getElementById('draftSaveStatus');
    const testResultsDrawer = document.getElementById('testResultsDrawer');
    const resultsStatusHeader = document.getElementById('resultsStatusHeader');
    const resultsExecutionTime = document.getElementById('resultsExecutionTime');
    const testCasesContainer = document.getElementById('testCasesContainer');

    // 1. Tab Key Indentation in Code Editor
    codeEditor.addEventListener('keydown', (e) => {
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = codeEditor.selectionStart;
            const end = codeEditor.selectionEnd;
            codeEditor.value = codeEditor.value.substring(0, start) + "    " + codeEditor.value.substring(end);
            codeEditor.selectionStart = codeEditor.selectionEnd = start + 4;
        }
    });

    // 2. Debounced Draft Auto-save
    let saveTimeout = null;
    codeEditor.addEventListener('input', () => {
        draftSaveStatus.innerText = 'Unsaved changes...';
        clearTimeout(saveTimeout);
        saveTimeout = setTimeout(saveDraft, 1500);
    });

    async function saveDraft() {
        try {
            await fetch('/coding/api/draft', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.getCsrfToken()
                },
                body: JSON.stringify({
                    challenge_id: challengeId,
                    source_code: codeEditor.value
                })
            });
            draftSaveStatus.innerText = 'Draft auto-saved';
        } catch (e) {
            draftSaveStatus.innerText = 'Save failed';
        }
    }

    // 3. Run Sample Tests
    runCodeBtn.addEventListener('click', async () => {
        setRunningState(true, 'Running Sample Tests...');

        try {
            const res = await fetch('/coding/api/run', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.getCsrfToken()
                },
                body: JSON.stringify({
                    challenge_id: challengeId,
                    source_code: codeEditor.value
                })
            });
            const data = await res.json();
            setRunningState(false);

            if (data.success) {
                renderTestResults(data.result, false);
            } else {
                alert(data.error || 'Execution error');
            }
        } catch (err) {
            setRunningState(false);
            alert('Network error while running code sandbox.');
        }
    });

    // 4. Submit Solution
    submitCodeBtn.addEventListener('click', async () => {
        setRunningState(true, 'Evaluating All Test Cases...');

        try {
            const res = await fetch('/coding/api/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.getCsrfToken()
                },
                body: JSON.stringify({
                    challenge_id: challengeId,
                    source_code: codeEditor.value,
                    language: 'python'
                })
            });
            const data = await res.json();
            setRunningState(false);

            if (data.success) {
                renderTestResults(data.result, true);
                if (data.status === 'Accepted') {
                    window.showToast('🎉 Solution Accepted! Challenge Solved.', 'success');
                } else {
                    window.showToast(`Submission finished: ${data.status}`, 'error');
                }
            } else {
                alert(data.error || 'Submission error');
            }
        } catch (err) {
            setRunningState(false);
            alert('Network error during submission.');
        }
    });

    function setRunningState(isRunning, label = '') {
        runCodeBtn.disabled = isRunning;
        submitCodeBtn.disabled = isRunning;
        if (isRunning) {
            testResultsDrawer.style.display = 'block';
            resultsStatusHeader.innerHTML = `<span style="color:var(--brand-blue)"><i data-lucide="loader-2" class="spin"></i> ${label}</span>`;
            resultsExecutionTime.innerText = '';
            testCasesContainer.innerHTML = '';
        }
        if (window.lucide) window.lucide.createIcons();
    }

    function renderTestResults(result, isFullSubmission) {
        testResultsDrawer.style.display = 'block';
        resultsExecutionTime.innerText = `${result.execution_time_ms} ms &middot; Passed ${result.passed_count}/${result.total_count} cases`;

        if (result.status === 'Accepted') {
            resultsStatusHeader.innerHTML = '<span style="color:var(--success-green);"><i data-lucide="check-circle-2"></i> Accepted (All Tests Passed)</span>';
        } else if (result.status === 'Wrong Answer') {
            resultsStatusHeader.innerHTML = '<span style="color:var(--danger-red);"><i data-lucide="x-circle"></i> Wrong Answer</span>';
        } else if (result.status === 'Time Limit Exceeded') {
            resultsStatusHeader.innerHTML = '<span style="color:var(--warning-orange);"><i data-lucide="clock"></i> Time Limit Exceeded (> 3.0s)</span>';
        } else if (result.status === 'Security Violation') {
            resultsStatusHeader.innerHTML = `<span style="color:var(--danger-red);"><i data-lucide="shield-alert"></i> ${result.error_message}</span>`;
        } else {
            resultsStatusHeader.innerHTML = `<span style="color:var(--danger-red);"><i data-lucide="alert-triangle"></i> ${result.status}</span>`;
        }

        testCasesContainer.innerHTML = '';

        result.test_results.forEach(tc => {
            const card = document.createElement('div');
            card.style.cssText = `
                padding: 10px 14px;
                border-radius: 6px;
                border: 1px solid ${tc.passed ? '#C6F6D5' : '#FED7D7'};
                background: ${tc.passed ? '#F0FFF4' : '#FFF5F5'};
                font-family: var(--font-mono);
                font-size: 0.8rem;
            `;

            let detailsHtml = `
                <div style="display:flex; justify-content:space-between; margin-bottom:4px; font-weight:700;">
                    <span style="color: ${tc.passed ? 'var(--success-green)' : 'var(--danger-red)'};">
                        ${tc.passed ? '✓ Test Case #' + tc.case_number + ' Passed' : '✗ Test Case #' + tc.case_number + ' Failed'}
                    </span>
                    <span style="color:var(--text-muted); font-size:0.75rem;">${tc.time_ms} ms</span>
                </div>
            `;

            if (!tc.is_hidden) {
                detailsHtml += `
                    <div><strong>Input:</strong> ${escapeHtml(tc.input)}</div>
                    <div><strong>Expected:</strong> ${escapeHtml(tc.expected)}</div>
                    ${tc.actual !== null ? `<div><strong>Actual:</strong> ${escapeHtml(tc.actual)}</div>` : ''}
                `;
            } else {
                detailsHtml += `<div style="color:var(--text-secondary); font-style:italic;">Hidden evaluation test case</div>`;
            }

            if (tc.error) {
                detailsHtml += `<div style="color:var(--danger-red); margin-top:4px;"><strong>Error:</strong> ${escapeHtml(tc.error)}</div>`;
            }

            card.innerHTML = detailsHtml;
            testCasesContainer.appendChild(card);
        });

        if (window.lucide) window.lucide.createIcons();
    }

    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }
});
