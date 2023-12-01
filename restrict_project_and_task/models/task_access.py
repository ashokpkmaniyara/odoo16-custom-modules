# -*- coding: utf-8 -*-
from odoo import models, fields


class TaskForm(models.Model):
    _inherit = 'project.task'

    access_limited_user_ids = fields.Many2many(
        'res.users', string='Access Limited Users',
        help='select the limited users',relation='access_limited_user_task',
        domain=lambda self: [("groups_id", "=", self.env.ref(
            "restrict_project_and_task.group_view_limited_projects_and_tasks").id)])
