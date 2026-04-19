# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PortfolioProject(models.Model):
    """Portfolio project model for showcasing client success stories."""
    
    _name = 'modulio.portfolio'
    _description = 'Portfolio Project'
    _order = 'sequence, id desc'
    _inherit = ['website.published.mixin']

    name = fields.Char(string='Project Name', required=True, translate=True)
    slug = fields.Char(string='URL Slug', help='URL-friendly name for the project')
    image = fields.Image(string='Cover Image', max_width=1920, max_height=1080)
    image_thumbnail = fields.Image(
        string='Thumbnail',
        related='image',
        max_width=600,
        max_height=400,
        store=True
    )
    description = fields.Text(string='Short Description', translate=True)
    content = fields.Html(string='Full Content', translate=True, sanitize=False)
    
    category_id = fields.Many2one(
        'modulio.portfolio.category',
        string='Category',
        ondelete='set null'
    )
    
    client_name = fields.Char(string='Client Name')
    client_logo = fields.Image(string='Client Logo', max_width=200, max_height=100)
    industry = fields.Char(string='Industry', translate=True)
    
    stat_1_value = fields.Char(string='Stat 1 Value', default='+40%')
    stat_1_label = fields.Char(string='Stat 1 Label', default='Efficiency', translate=True)
    stat_2_value = fields.Char(string='Stat 2 Value', default='-70%')
    stat_2_label = fields.Char(string='Stat 2 Label', default='Admin Time', translate=True)
    stat_3_value = fields.Char(string='Stat 3 Value', default='+25%')
    stat_3_label = fields.Char(string='Stat 3 Label', default='Revenue', translate=True)
    
    sequence = fields.Integer(string='Sequence', default=10)
    is_featured = fields.Boolean(string='Featured on Homepage', default=False)
    
    website_id = fields.Many2one('website', string='Website')

    @api.model
    def _compute_website_url(self):
        for record in self:
            record.website_url = f'/portfolio/{record.slug or record.id}'

    @api.onchange('name')
    def _onchange_name_slug(self):
        if self.name and not self.slug:
            self.slug = self.name.lower().replace(' ', '-').replace('&', 'and')


class PortfolioCategory(models.Model):
    """Category for portfolio projects."""
    
    _name = 'modulio.portfolio.category'
    _description = 'Portfolio Category'
    _order = 'sequence, name'

    name = fields.Char(string='Category Name', required=True, translate=True)
    slug = fields.Char(string='URL Slug')
    icon = fields.Char(string='Icon Class', help='CSS class for icon')
    color = fields.Char(string='Color', default='#1b3d5a')
    sequence = fields.Integer(string='Sequence', default=10)
    
    project_ids = fields.One2many(
        'modulio.portfolio',
        'category_id',
        string='Projects'
    )
    project_count = fields.Integer(
        string='Project Count',
        compute='_compute_project_count'
    )

    def _compute_project_count(self):
        for category in self:
            category.project_count = len(category.project_ids)
