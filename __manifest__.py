# -*- coding: utf-8 -*-
{
    "name": "Modulio Website - Landing Page",
    "version": "18.0.2.7.0",
    "summary": "Modulio Landing Page - Accounting Systems & Odoo Expert",
    "description": """
Professional landing page for Modulio - Meridian Style Design

Features:
- Modern, clean design inspired by Meridian Consulting
- Dark Navy gradient hero with stats grid
- Numbered service cards with features list
- Client testimonials section
- Grid-based "Why Choose Us" section
- How We Work process steps
- Portfolio/Work cards with case study metrics
- Gradient CTA with contact info
- Minimal footer
- Dark/Light mode support
- Responsive design

Brand Identity:
- Navy: #0f1729
- Coral: #f26c5f
- Cream: #f5f3ef
    """,
    "category": "Website",
    "author": "Modulio",
    "website": "https://modulio.id",
    "license": "LGPL-3",
    "depends": [
        "website",
        "crm",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/hero_config_data.xml",
        "views/backend/hero_config_views.xml",
        "views/backend/portfolio_views.xml",
        "views/backend/service_views.xml",
        "views/backend/website_menus.xml",
        "views/service_dynamic.xml",
        "views/snippets/s_hero.xml",
        "views/snippets/s_services.xml",
        "views/snippets/s_testimonials.xml",
        "views/snippets/s_portfolio.xml",
        "views/snippets/s_pain_points.xml",
        "views/snippets/s_process.xml",
        "views/snippets/s_cta_form.xml",
        "views/snippets/snippets_options.xml",
        "views/landing_page_template.xml",
        "views/portfolio_page.xml",
        "views/service_pages.xml",
        "views/thank_you_page.xml",
        "views/layout.xml",
        "data/website_menu.xml",
        "data/services_demo.xml",
        "data/demo_data.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "modulio_website/static/src/scss/modulio_theme.scss",
            "modulio_website/static/src/scss/snippets.scss",
            "modulio_website/static/src/js/modulio.js",
        ],
    },
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": True,
    "auto_install": False,
}
