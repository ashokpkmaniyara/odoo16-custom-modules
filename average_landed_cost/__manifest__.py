# -*- coding: utf-8 -*-
{
    "name": "Average Landed Cost",
    "version": "16.0.1.0.0",
    "author": "Ashokpk",
    "category": "Inventory",
    "description": """Average landed cost""",
    "depends": ["base","stock","purchase","sale_management"],
    "data": [
        'security/ir.model.access.csv',
        'views/landed_cost_view.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
