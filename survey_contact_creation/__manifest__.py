# -*- coding: utf-8 -*-
{
    'name': "Contact Creation",
    'version': '16.0.1.0.0',
    'depends': ['survey'],
    'author': "Ashokpk",
    'category': 'Survey',
    'description': """Contact Creation from Survey""",
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/contact_relation_view.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
