/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

// ======================
// THEME TOGGLE BUTTON
// ======================
publicWidget.registry.ModulioThemeToggle = publicWidget.Widget.extend({
    selector: '.theme-toggle',
    events: {
        'click': '_onToggleTheme',
    },

    start: function () {
        this._syncTheme();
        return this._super.apply(this, arguments);
    },

    _syncTheme: function () {
        const savedTheme = localStorage.getItem('modulio-theme');
        const isDark = savedTheme === 'dark';
        
        // Ensure both html and body have correct class
        if (isDark) {
            document.documentElement.classList.add('dark-mode');
            document.body.classList.add('dark-mode');
        } else {
            document.documentElement.classList.remove('dark-mode');
            document.body.classList.remove('dark-mode');
        }
    },

    _onToggleTheme: function (ev) {
        ev.preventDefault();
        ev.stopPropagation();
        
        // Check current state from localStorage (source of truth)
        const currentTheme = localStorage.getItem('modulio-theme');
        const switchToDark = currentTheme !== 'dark';
        
        // Apply to both html and body
        if (switchToDark) {
            document.documentElement.classList.add('dark-mode');
            document.body.classList.add('dark-mode');
            localStorage.setItem('modulio-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark-mode');
            document.body.classList.remove('dark-mode');
            localStorage.setItem('modulio-theme', 'light');
        }
    },
});

// ======================
// NAVBAR SCROLL EFFECT
// ======================
publicWidget.registry.ModulioNavbar = publicWidget.Widget.extend({
    selector: '#modulioNavbar',

    start: function () {
        this._onScroll = this._updateNavbar.bind(this);
        window.addEventListener('scroll', this._onScroll);
        this._updateNavbar();
        return this._super.apply(this, arguments);
    },

    destroy: function () {
        window.removeEventListener('scroll', this._onScroll);
        this._super.apply(this, arguments);
    },

    _updateNavbar: function () {
        const scrolled = window.scrollY > 60;
        if (scrolled) {
            this.el.classList.add('solid');
        } else {
            this.el.classList.remove('solid');
        }
    },
});

// ======================
// COUNTER ANIMATION
// ======================
publicWidget.registry.ModulioCounters = publicWidget.Widget.extend({
    selector: '.hero-section',

    start: function () {
        const counters = this.el.querySelectorAll('.counter-value');
        if (!counters.length) return this._super.apply(this, arguments);

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    this._animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach((c) => observer.observe(c));
        return this._super.apply(this, arguments);
    },

    _animateCounter: function (el) {
        const targetText = el.textContent || '';
        const match = targetText.match(/(\d+)/);
        if (!match) return;

        const target = parseInt(match[0]);
        const suffix = targetText.replace(match[0], '');
        let start = null;
        const duration = 2000;

        const step = (timestamp) => {
            if (!start) start = timestamp;
            const progress = Math.min((timestamp - start) / duration, 1);
            const current = Math.floor(progress * target);
            el.textContent = current + suffix;
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    },
});

// ======================
// REVEAL ANIMATION
// ======================
publicWidget.registry.ModulioReveal = publicWidget.Widget.extend({
    selector: '#wrap',
    
    start: function () {
        const revealItems = this.el.querySelectorAll('.modulio-reveal');
        if (!revealItems.length) return this._super.apply(this, arguments);

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        revealItems.forEach((ri) => observer.observe(ri));
        return this._super.apply(this, arguments);
    },
});
