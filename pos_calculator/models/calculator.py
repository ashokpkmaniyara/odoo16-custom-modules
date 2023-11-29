# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    """class for adding new boolean field in settings"""
    _inherit = 'pos.config'

    virtual_calculator = fields.Boolean(
        'Virtual Calculator', help='enable to view the calculator in pos',)


class PosCalculator(models.TransientModel):
    """class for adding new boolean field in settings"""
    _inherit = 'res.config.settings'

    virtual_calculator = fields.Boolean(
        'Virtual Calculator', help='enable to view the calculator in pos',
        related='pos_config_id.virtual_calculator', readonly=False)
