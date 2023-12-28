# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductReturn(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def product_return(self, val, order):
        order = self.env['sale.order'].browse(order)
        picking_vals = {
            'picking_type_id':
                self.env['stock.return.picking'].search([])._create_returns()[
                    1],
            'location_id': order.partner_id.property_stock_customer.id,
            'location_dest_id': self.env.ref('stock.stock_location_stock').id,
            'origin': order.name,
        }

        new_picking_vals = self.create(picking_vals)
        for i in val:
            if i['quantity'] != '' and int(i['quantity']) > 0:
                new_picking_vals['move_ids'] = [fields.Command.create({
                    'name': order.name,
                    'product_uom_qty': i['quantity'],
                    'product_id': i['product_id'],
                    "location_id": order.partner_id.property_stock_customer.id,
                    "location_dest_id": self.env.ref(
                        'stock.stock_location_stock').id,
                })]
                picking = order.picking_ids.ids
                picking.append(new_picking_vals.id)
                order.picking_ids = picking
        if new_picking_vals['move_ids']:
            return new_picking_vals
