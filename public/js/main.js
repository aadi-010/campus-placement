/**
 * CampusPrep — Core UI & Frontend Utilities
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Lucide Icons if available
    if (window.lucide) {
        window.lucide.createIcons();
    }

    // 2. Mobile Sidebar Drawer Toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const appSidebar = document.getElementById('appSidebar');
    const sidebarBackdrop = document.getElementById('sidebarBackdrop');

    if (mobileMenuBtn && appSidebar) {
        mobileMenuBtn.addEventListener('click', () => {
            appSidebar.classList.toggle('mobile-open');
            if (sidebarBackdrop) {
                sidebarBackdrop.classList.toggle('active');
            }
        });
    }

    if (sidebarBackdrop) {
        sidebarBackdrop.addEventListener('click', () => {
            if (appSidebar) appSidebar.classList.remove('mobile-open');
            sidebarBackdrop.classList.remove('active');
        });
    }

    // 3. Global Toast Notifications Handler
    window.showToast = function(message, type = 'info') {
        let container = document.getElementById('toastContainer');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toastContainer';
            container.className = 'toast-container';
            document.body.appendChild(container);
        }

        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        
        let iconName = 'info';
        if (type === 'success') iconName = 'check-circle';
        if (type === 'error') iconName = 'alert-triangle';

        toast.innerHTML = `
            <i data-lucide="${iconName}"></i>
            <span>${message}</span>
        `;
        container.appendChild(toast);

        if (window.lucide) window.lucide.createIcons();

        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }, 3500);
    };

    // 4. Bookmark Toggle Handler
    document.querySelectorAll('.btn-bookmark').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            e.stopPropagation();

            const itemType = btn.getAttribute('data-type');
            const itemId = btn.getAttribute('data-id');

            try {
                const res = await fetch('/api/bookmark/toggle', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCsrfToken()
                    },
                    body: JSON.stringify({ item_type: itemType, item_id: itemId })
                });
                const data = await res.json();
                if (data.success) {
                    btn.classList.toggle('bookmarked', data.bookmarked);
                    const icon = btn.querySelector('i');
                    if (icon) {
                        icon.setAttribute('data-lucide', data.bookmarked ? 'bookmark-check' : 'bookmark');
                        if (window.lucide) window.lucide.createIcons();
                    }
                    showToast(data.message, 'success');
                } else {
                    showToast(data.error || 'Could not update bookmark', 'error');
                }
            } catch (err) {
                showToast('Network error while saving bookmark', 'error');
            }
        });
    });

    // Helper: Retrieve CSRF Token from meta tag or hidden input
    window.getCsrfToken = function() {
        const metaTag = document.querySelector('meta[name="csrf-token"]');
        if (metaTag) return metaTag.getAttribute('content');
        const inputTag = document.querySelector('input[name="csrf_token"]');
        if (inputTag) return inputTag.value;
        return '';
    };
});
