# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website


class ModulioHomepage(Website):
    """Override Website controller to serve custom homepage."""

    @http.route(['/'], type='http', auth='public', website=True, sitemap=True)
    def index(self, **kwargs):
        """Render Modulio landing page as homepage."""
        return request.render('modulio_website.landing_page', {})


class ModulioPages(http.Controller):
    """Controller for Modulio custom pages."""

    @http.route('/services', type='http', auth='public', website=True)
    def services_list(self, **kwargs):
        """Display services listing page (dynamic records + fallback)."""
        services = request.env['modulio.service'].sudo().search(
            [('website_published', '=', True)],
            order='sequence, id',
        )
        return request.render('modulio_website.services_list_page', {
            'services': services,
        })

    @http.route('/services/<string:service>', type='http', auth='public', website=True)
    def service_page(self, service, **kwargs):
        """Display service detail page (database record overrides static templates)."""
        Service = request.env['modulio.service'].sudo()
        dynamic = Service.search([
            ('website_published', '=', True),
            '|',
            ('slug', '=', service),
            ('id', '=', int(service) if service.isdigit() else 0),
        ], limit=1)
        if dynamic:
            return request.render('modulio_website.service_dynamic_page', {
                'service': dynamic,
            })

        service_templates = {
            'accounting': 'modulio_website.service_accounting_page',
            'hr': 'modulio_website.service_hr_page',
            'odoo': 'modulio_website.service_odoo_page',
            'erp': 'modulio_website.service_odoo_page',
            'web-app': 'modulio_website.service_odoo_page',
            'integration': 'modulio_website.service_odoo_page',
        }

        template = service_templates.get(service)
        if not template:
            return request.not_found()

        return request.render(template, {
            'service_slug': service,
        })

    @http.route('/portfolio', type='http', auth='public', website=True)
    def portfolio_list(self, category=None, **kwargs):
        """Display portfolio listing page with optional category filter."""
        domain = [('website_published', '=', True)]
        
        if category:
            domain.append(('category_id.slug', '=', category))
        
        projects = request.env['modulio.portfolio'].sudo().search(
            domain, order='sequence, id desc'
        )
        categories = request.env['modulio.portfolio.category'].sudo().search([])
        
        return request.render('modulio_website.portfolio_page', {
            'projects': projects,
            'categories': categories,
            'current_category': category,
        })

    @http.route('/portfolio/<string:slug>', type='http', auth='public', website=True)
    def portfolio_detail(self, slug, **kwargs):
        """Display individual portfolio project page."""
        project = request.env['modulio.portfolio'].sudo().search([
            ('website_published', '=', True),
            '|', ('slug', '=', slug), ('id', '=', int(slug) if slug.isdigit() else 0)
        ], limit=1)
        
        if not project:
            return request.not_found()
        
        related_projects = request.env['modulio.portfolio'].sudo().search([
            ('website_published', '=', True),
            ('id', '!=', project.id),
            ('category_id', '=', project.category_id.id if project.category_id else False)
        ], limit=3)
        
        return request.render('modulio_website.portfolio_detail_page', {
            'project': project,
            'related_projects': related_projects,
        })

    @http.route('/contactus-thank-you', type='http', auth='public', website=True)
    def contact_thank_you(self, **kwargs):
        """Display thank you page after contact form submission."""
        return request.render('modulio_website.contact_thank_you_page', {})

    @http.route('/contact/submit', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def contact_submit(self, **kwargs):
        """Handle contact form submission and create CRM lead."""
        contact_name = kwargs.get('contact_name', '')
        company_name = kwargs.get('company_name', '')
        email = kwargs.get('email', '')
        phone = kwargs.get('phone', '')
        message = kwargs.get('message', '')
        
        # Create CRM Lead
        lead_vals = {
            'name': f"Website Contact: {contact_name}",
            'contact_name': contact_name,
            'partner_name': company_name,
            'email_from': email,
            'phone': phone,
            'description': message,
            'type': 'lead',
        }
        
        request.env['crm.lead'].sudo().create(lead_vals)
        
        return request.redirect('/contactus-thank-you')
