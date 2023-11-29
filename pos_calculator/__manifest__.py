# -*- coding: utf-8 -*-
{
    "name": "POS Calculator",
    "version": "16.0.1.0.0",
    "author": "Ashokpk",
    "category": "POS",
    "description": """A simple virtual calculator with option to 
    enable/disable from PoS configurations.""",
    "depends": ["base", "point_of_sale"],
    "data": [
        'views/setting_calculator.xml',
    ],
    "assets": {
        "point_of_sale.assets": [
            'pos_calculator/static/src/js/*',
            'pos_calculator/static/src/xml/*',
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
