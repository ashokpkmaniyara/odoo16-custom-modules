# -*- coding: utf-8 -*-
{
    "name": "POS Create Product",
    "version": "16.0.1.0.0",
    "author": "Ashokpk",
    "category": "POS",
    "description": """Add a new Button in Pos Screen.
    Clicking on this button Needs to show all products as a list view.
    We can either create a new product from that screen or Edit the existing one.""",
    "depends": ["base", "point_of_sale"],
    "data": [
    ],
    "assets": {
        "point_of_sale.assets": [
            'pos_create_product/static/src/js/*',
            'pos_create_product/static/src/xml/*',
            'pos_create_product/static/src/css/*',
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
