# -*- coding: utf-8 -*-
{
    "name": "Payslip in MyAccount",
    "version": "16.0.1.0.0",
    "author": "Ashokpk",
    "category": "payroll",
    "description": """Employees can see their Payslips in My Account
                    Can Print the Payslip details from Portal""",
    "depends": ["hr_payroll_community","hr",],
    "data": [
        'views/portal_template.xml',
        'views/report_detail_action.xml',
        'views/payslip_detail_template.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
