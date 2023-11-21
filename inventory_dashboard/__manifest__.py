# -*- coding: utf-8 -*-
{
    'name': 'Inventory Dashboard',
    'version': '16.0.1.0.0',
    'category': 'Inventory',
    'author': 'Ashokpk',
    'depends': ['base', 'stock'],
    'description': '''Inventory Dashboard''',
    'license': 'LGPL-3',
    'installable': True,
    'data': [
        'views/dashboard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'inventory_dashboard/static/src/xml/inventory_dashboard.xml',
            'inventory_dashboard/static/src/js/inventory_dashboard.js',
            'inventory_dashboard/static/src/xml/chart_renderer.xml',
            'inventory_dashboard/static/src/js/chart_renderer.js',
        ],
    },
}
