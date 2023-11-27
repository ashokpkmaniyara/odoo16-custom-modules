from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    product_ref = fields.Char(string='Ref')

    def _prepare_invoice_line(self, sequence):
        return super(SaleOrder, self)._prepare_invoice_line(
            product_ref=self.product_ref, sequence=sequence
        )


class InvoiceLine(models.Model):
    _inherit = 'account.move.line'

    product_ref = fields.Char(string='Ref')
