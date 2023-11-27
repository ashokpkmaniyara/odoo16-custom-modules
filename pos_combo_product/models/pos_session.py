# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    """To inherit pos session model."""
    _inherit = "pos.session"

    def _loader_params_product_product(self):
        """loading fields to the pos"""
        result = super()._loader_params_product_product()
        result['search_params']['fields'].extend(
            ['is_combo', 'combo_product_ids'])
        return result

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result.append('combo.product')
        return result

    def _loader_params_combo_product(self):
        return {
            'search_params': {
                'domain': [],
                'fields': ['pos_categ_id', 'product_ids', 'is_required',
                           'quantity'],
            },
        }

    def _get_pos_ui_combo_product(self, params):
        return self.env['combo.product'].search_read(
            **params['search_params'])
