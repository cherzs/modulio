# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

LANDING_PAGE_PORTFOLIO_MAX = 3


class PortfolioProject(models.Model):
    """Portfolio project model for showcasing client success stories."""
    
    _name = 'modulio.portfolio'
    _description = 'Portfolio Project'
    _order = 'sequence, id desc'
    _inherit = ['website.published.mixin']

    name = fields.Char(string='Project Name', required=True, translate=True)
    slug = fields.Char(string='URL Slug', help='URL-friendly name for the project')
    image = fields.Image(
        string='Image',
        max_width=1920,
        max_height=1080,
        help='Single image for portfolio grid cards and the case study page.',
    )
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
    industry = fields.Char(string='Industry', translate=True)
    
    stat_1_value = fields.Char(string='Stat 1 Value', default='+40%')
    stat_1_label = fields.Char(string='Stat 1 Label', default='Efficiency', translate=True)
    stat_2_value = fields.Char(string='Stat 2 Value', default='-70%')
    stat_2_label = fields.Char(string='Stat 2 Label', default='Admin Time', translate=True)
    stat_3_value = fields.Char(string='Stat 3 Value', default='+25%')
    stat_3_label = fields.Char(string='Stat 3 Label', default='Revenue', translate=True)
    
    sequence = fields.Integer(string='Sequence', default=10)
    is_featured = fields.Boolean(string='Featured on Homepage', default=False)
    is_landing_page = fields.Boolean(
        string='Show on landing page',
        default=False,
        help='Published projects only. At most %s can be selected; order follows Sequence.' % LANDING_PAGE_PORTFOLIO_MAX,
    )

    website_id = fields.Many2one('website', string='Website')

    card_listing_image_url = fields.Char(
        string='Listing card image URL',
        compute='_compute_card_listing_image_url',
        help='Resolved /web/image URL for /portfolio grid (QWeb-safe; do not call methods from templates).',
    )

    @api.depends('image')
    def _compute_card_listing_image_url(self):
        stock = (
            '/web/image/website.library_image_08',
            '/web/image/website.library_image_10',
            '/web/image/website.library_image_13',
        )
        for rec in self:
            if not rec.id:
                rec.card_listing_image_url = stock[0]
                continue
            base = '/web/image/modulio.portfolio/%s/' % rec.id
            if rec.image:
                rec.card_listing_image_url = base + 'image_thumbnail'
            else:
                rec.card_listing_image_url = stock[rec.id % 3]

    @api.depends('slug')
    def _compute_website_url(self):
        """Public URL for Website editor publish button."""
        for record in self:
            record.website_url = f'/portfolio/{record.slug or record.id}'

    @api.onchange('name')
    def _onchange_name_slug(self):
        if self.name and not self.slug:
            self.slug = self.name.lower().replace(' ', '-').replace('&', 'and')

    @api.constrains('is_landing_page')
    def _check_landing_page_max(self):
        """Only LANDING_PAGE_PORTFOLIO_MAX projects may have Show on landing page enabled."""
        total = self.env['modulio.portfolio'].search_count([('is_landing_page', '=', True)])
        if total > LANDING_PAGE_PORTFOLIO_MAX:
            raise ValidationError(
                _('Only %(max)s portfolio projects can be shown on the landing page. '
                  'Disable this on another project before enabling it here.')
                % {'max': LANDING_PAGE_PORTFOLIO_MAX}
            )

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
