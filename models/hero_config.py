# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ModulioHeroConfig(models.Model):
    """Singleton-style settings for the landing page hero background image."""

    _name = 'modulio.hero.config'
    _description = 'Homepage Hero Settings'

    name = fields.Char(
        string='Label',
        default='Homepage Hero',
        required=True,
        help='Internal name for this configuration record.',
    )
    image = fields.Image(
        string='Hero background',
        max_width=1920,
        max_height=1080,
        help='Full-width background image behind the hero text. Recommended: wide photo, dark enough for white text.',
    )

    @api.model
    def get_config(self):
        """Return the single hero config row (sudo for public rendering)."""
        return self.sudo().search([], limit=1)

    @api.model_create_multi
    def create(self, vals_list):
        if self.search_count([]) + len(vals_list) > 1:
            raise UserError(
                _('Only one Homepage Hero record is allowed. Edit the existing record instead.')
            )
        return super().create(vals_list)
