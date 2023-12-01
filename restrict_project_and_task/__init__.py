# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID
from . import models


def _post_init_hook(cr, registry):
    # Retrieve the record rules to archive
    env = api.Environment(cr, SUPERUSER_ID, {})
    project_model_id = env['ir.model'].search(
        [('model', '=', 'project.project')]).id
    task_model_id = env['ir.model'].search([('model', '=', 'project.task')]).id
    project_record_rules = env['ir.rule'].search(
        [('model_id', '=', project_model_id),
         ('name', '!=', 'View Limited Projects')])
    task_record_rules = env['ir.rule'].search(
        [('model_id', '=', task_model_id),
         ('name', '!=', 'Limited Access Task')])

    # Archive the record rules
    for project_record_rules in project_record_rules:
        project_record_rules.active = False

    for task_record_rules in task_record_rules:
        task_record_rules.active = False


def _uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    project_model_id = env['ir.model'].search(
        [('model', '=', 'project.project')]).id
    task_model_id = env['ir.model'].search([('model', '=', 'project.task')]).id
    project_record_rules = env['ir.rule'].search(
        [('model_id', '=', project_model_id), ('active', '=', False)])
    task_record_rules = env['ir.rule'].search(
        [('model_id', '=', task_model_id), ('active', '=', False)])

    # UnArchive the record rules
    for project_record_rules in project_record_rules:
        project_record_rules.active = True

    for task_record_rules in task_record_rules:
        task_record_rules.active = True
