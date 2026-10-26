/**
 * CampusPrep — Interview Room Engine
 */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Reveal/Hide Model Answers in Catalog
    document.querySelectorAll('.btn-reveal-answer').forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const targetBox = document.getElementById(targetId);
            if (!targetBox) return;

            const isHidden = (targetBox.style.display === 'none' || !targetBox.style.display);
            targetBox.style.display = isHidden ? 'block' : 'none';
            btn.querySelector('span').innerText = isHidden ? 'Hide Model Answer' : 'Reveal Model Answer';
            const icon = btn.querySelector('i');
            if (icon) {
                icon.setAttribute('data-lucide', isHidden ? 'chevron-up' : 'chevron-down');
                if (window.lucide) window.lucide.createIcons();
            }
        });
    });

    // 2. Mark as Reviewed in Catalog
    document.querySelectorAll('.btn-mark-reviewed').forEach(btn => {
        btn.addEventListener('click', async () => {
            const questionId = btn.getAttribute('data-id');
            try {
                const res = await fetch('/interview/api/review', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': window.getCsrfToken()
                    },
                    body: JSON.stringify({ question_id: questionId, is_reviewed: true })
                });
                const data = await res.json();
                if (data.success) {
                    btn.querySelector('span').innerText = 'Marked Reviewed';
                    btn.classList.add('btn-success');
                    window.showToast('Question marked as reviewed!', 'success');
                }
            } catch (err) {
                window.showToast('Failed to save review status', 'error');
            }
        });
    });

    // 3. Interactive Practice Mode: Reveal Comparison Drawer
    const btnRevealComparison = document.getElementById('btnRevealComparison');
    const comparisonDrawer = document.getElementById('comparisonDrawer');

    if (btnRevealComparison && comparisonDrawer) {
        btnRevealComparison.addEventListener('click', () => {
            comparisonDrawer.style.display = 'block';
            btnRevealComparison.style.display = 'none';
            if (window.lucide) window.lucide.createIcons();
        });
    }

    // 4. Save Practice Review & Notes
    const btnSavePracticeReview = document.getElementById('btnSavePracticeReview');
    const personalNotesInput = document.getElementById('personalNotesInput');

    if (btnSavePracticeReview) {
        btnSavePracticeReview.addEventListener('click', async () => {
            const questionId = btnSavePracticeReview.getAttribute('data-id');
            const notes = personalNotesInput ? personalNotesInput.value.trim() : '';

            try {
                const res = await fetch('/interview/api/review', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': window.getCsrfToken()
                    },
                    body: JSON.stringify({
                        question_id: questionId,
                        is_reviewed: true,
                        personal_notes: notes
                    })
                });
                const data = await res.json();
                if (data.success) {
                    window.showToast('Notes saved and question marked as reviewed!', 'success');
                }
            } catch (err) {
                window.showToast('Error saving notes', 'error');
            }
        });
    }
});
