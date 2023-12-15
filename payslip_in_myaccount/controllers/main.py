# -*- coding: utf-8 -*-
from odoo.addons.portal.controllers import portal

from odoo import exceptions
from odoo.http import Controller, route, request
from odoo.tools import consteq


class Payslips(Controller):

    @route('/my/payslip', auth='user', website=True)
    def fetch_payslip(self):
        payslip = request.env['hr.payslip'].sudo().search(
            [('employee_id', '=', request.env.user.employee_id.id)])
        return request.render('payslip_in_myaccount.my_payslip_portal',
                              {'payslip': payslip})

    @route(['/my/payslip/pdf/<int:payslip_id>'], type='http', auth="public",
           website=True)
    def print_payslip(self, payslip_id, access_token=None, **kw):
        """ Print payslip for employees, using either access rights or access token
        to be sure customer has access """
        try:
            payslip_sudo = self._payslip_check_access(payslip_id,
                                                            access_token=access_token)
        except exceptions.AccessError:
            return request.redirect('/my')

        # printing report with sudo
        print('aaa',payslip_id)
        pdf = request.env['ir.actions.report'].sudo()._render_qweb_pdf(
            'payslip_in_myaccount.action_payslip_report_detail', [payslip_sudo.id])[0]
        pdfhttpheaders = [
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf)),
        ]
        return request.make_response(pdf, headers=pdfhttpheaders)

    def _payslip_check_access(self, payslip_id, access_token=None):
        payslip = request.env['hr.payslip'].browse([payslip_id])
        payslip_sudo = payslip.sudo()
        try:
            payslip.check_access_rights('read')
            payslip.check_access_rule('read')
        except exceptions.AccessError:
            if not access_token or not consteq(payslip_sudo.payslip_id.access_token, access_token):
                raise
        return payslip_sudo


class PayslipCount(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'payslip_count' in counters:
            values['payslip_count'] = request.env[
                'hr.payslip'].sudo().search_count(
                [('employee_id', '=', request.env.user.employee_id.id)])
        return values
