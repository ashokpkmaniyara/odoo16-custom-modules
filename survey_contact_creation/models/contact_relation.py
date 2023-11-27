# -*- coding: utf-8 -*-
from odoo import models, fields


class ContactRelation(models.Model):
    _name = 'contact.relation'

    question_id = fields.Many2one('survey.question', 'Question',
                                  help='select a question', required=1,
                                  domain="[('survey_id', '=', survey_id)]")
    contact_field_id = fields.Many2one('ir.model.fields', 'Contact Fields',
                                       help='select a contact', required=1,
                                       ondelete='cascade',
                                       domain="[('model', '=', 'res.partner')]")
    survey_id = fields.Many2one('survey.survey', string='Survey')


class SurveyForm(models.Model):
    _inherit = 'survey.survey'

    contact_rel_ids = fields.One2many('contact.relation', 'survey_id',
                                      'Contact Relation')
