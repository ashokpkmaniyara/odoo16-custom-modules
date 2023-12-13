# -*- coding: utf-8 -*-

from odoo import models, fields


class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    landed_cost_ids = fields.One2many('landed.cost', 'landed_cost_id',
                                      help='landed costs')

    def compute_landed_cost(self):
        res = super().compute_landed_cost()
        AvgAdjustmentLines = self.env['landed.cost']
        AvgAdjustmentLines.search([('landed_cost_id', 'in', self.ids)]).unlink()

        product_values = {}

        for avg_line in self.picking_ids:
            for product in avg_line.move_line_ids:
                adjustment_lines = self.env[
                    'stock.valuation.adjustment.lines'].search(
                    [('cost_id', '=', self.id),
                     ('product_id', '=', product.product_id.id)])

                for line in adjustment_lines:
                    average = line.additional_landed_cost / line.quantity

                    if product.product_id.id not in product_values:
                        product_values[product.product_id.id] = {
                            'product_id': product.product_id.id,
                            'average': 0.0,
                        }

                    # Accumulate the average values for the same product
                    product_values[product.product_id.id]['average'] += average

        # Create the landed cost records for each product
        self.landed_cost_ids = [fields.Command.create(value) for value in
                                product_values.values()]

        return res



