# -*- coding: utf-8 -*-
{
    'name': "Website Product Return",
    'version': '16.0.1.0.0',
    'depends': ['website','sale','stock'],
    'author': "Ashokpk",
    'category': 'website',
    'description': """Module for returning multiple product from website.""",
    'data':[
        'views/portal_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_product_return/static/src/js/productReturn.js'
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
