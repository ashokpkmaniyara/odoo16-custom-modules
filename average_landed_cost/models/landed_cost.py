from odoo import models, fields


class LandedCost(models.Model):
    _name = 'landed.cost'
    _description = 'Landed Cost'

    product_id = fields.Many2one('product.product', 'Product',
                              help='landed cost product')
    average = fields.Float(string='Average Landed Cost',
                           help='average landed cost of the product')
    landed_cost_id = fields.Many2one('stock.landed.cost', 'Landed Cost', help='landed cost')

