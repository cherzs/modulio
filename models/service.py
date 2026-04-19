# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

LANDING_PAGE_SERVICE_MAX = 4


class ModulioService(models.Model):
    """Website service page: content and images managed from Website > Configuration."""

    _name = 'modulio.service'
    _description = 'Website Service'
    _order = 'sequence, id'
    _inherit = ['website.published.mixin']

    name = fields.Char(string='Title', required=True, translate=True)
    slug = fields.Char(
        string='URL Slug',
        required=True,
        index=True,
        help='Used in URL: /services/<slug> (e.g. accounting, hr, odoo).',
    )
    sequence = fields.Integer(string='Sequence', default=10)
    is_landing_page = fields.Boolean(
        string='Show on landing page',
        default=False,
        help='Published services only. At most %s can be selected; order follows Sequence.' % LANDING_PAGE_SERVICE_MAX,
    )

    image = fields.Image(
        string='Hero / Card Image',
        max_width=1920,
        max_height=1080,
        help='Shown on the service detail hero and listing card.',
    )

    tag_1 = fields.Char(string='Tag 1', translate=True)
    tag_2 = fields.Char(string='Tag 2', translate=True)
    tag_3 = fields.Char(string='Tag 3', translate=True)

    card_number = fields.Char(string='Card Number', default='01', help='e.g. 01, 02')
    short_description = fields.Text(string='Short Description', translate=True)
    feature_1 = fields.Char(string='Feature 1', translate=True)
    feature_2 = fields.Char(string='Feature 2', translate=True)
    feature_3 = fields.Char(string='Feature 3', translate=True)

    content = fields.Html(string='Body', translate=True, sanitize=False)

    stat_1_value = fields.Char(string='Stat 1 Value', default='75%')
    stat_1_label = fields.Char(string='Stat 1 Label', translate=True)
    stat_2_value = fields.Char(string='Stat 2 Value', default='100%')
    stat_2_label = fields.Char(string='Stat 2 Label', translate=True)
    stat_3_value = fields.Char(string='Stat 3 Value', default='50+')
    stat_3_label = fields.Char(string='Stat 3 Label', translate=True)
    stat_4_value = fields.Char(string='Stat 4 Value')
    stat_4_label = fields.Char(string='Stat 4 Label', translate=True)

    website_id = fields.Many2one('website', string='Website')

    @api.depends('slug')
    def _compute_website_url(self):
        """Public URL for Website editor publish button."""
        for service in self:
            service.website_url = f'/services/{service.slug}' if service.slug else '#'

    _sql_constraints = [
        ('modulio_service_slug_unique', 'unique(slug)', 'The URL slug must be unique.'),
    ]

    @api.onchange('name')
    def _onchange_name_slug(self):
        if self.name and not self.slug:
            self.slug = (
                self.name.lower()
                .replace(' ', '-')
                .replace('&', 'and')
                .replace('/', '-')
            )

    @api.constrains('is_landing_page')
    def _check_service_landing_page_max(self):
        total = self.env['modulio.service'].search_count([('is_landing_page', '=', True)])
        if total > LANDING_PAGE_SERVICE_MAX:
            raise ValidationError(
                _('Only %(max)s services can be shown on the landing page. '
                  'Disable this on another service before enabling it here.')
                % {'max': LANDING_PAGE_SERVICE_MAX}
            )
