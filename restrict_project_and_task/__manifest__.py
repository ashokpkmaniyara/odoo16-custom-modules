# -*- coding: utf-8 -*-
{
    "name": "Restrict Project and Task",
    "version": "16.0.1.0.0",
    "author": "Ashokpk",
    "category": "Project",
    "description": """Restrict project and task to group users""",
    "depends": ["project"],
    "data": [
        'security/security.xml',
        'data/record_rules.xml',
        'views/project_access_view.xml',
        'views/task_access_view.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
    "post_init_hook": "_post_init_hook",
    "uninstall_hook": "_uninstall_hook",
}
