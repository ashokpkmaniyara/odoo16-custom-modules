# -*- coding: utf-8 -*-
from odoo import fields, models


class ComboProduct(models.Model):
    """To add list of combo products"""
    _name = "combo.product"
    _description = "Combo Product"

    product_tmpl_id = fields.Many2one(
        "product.template", help="Product id")
    pos_categ_id = fields.Many2one(
        "pos.category", string='Product category',
        help="select the product category", required=True)
    product_ids = fields.Many2many(
        "product.product", help="select the product",
        required=True, domain="[('product_tmpl_id.pos_categ_id', "
                              + "'=', pos_categ_id)]")
    is_required = fields.Boolean("Is Required",
                                 help="enable to make it as required")
    quantity = fields.Integer(string="Quantity", help="specify the quantity",
                              default=1)
