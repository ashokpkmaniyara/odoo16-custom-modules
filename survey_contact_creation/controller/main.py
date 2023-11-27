# -*- coding: utf-8 -*-

from odoo.addons.survey.controllers.main import Survey
from odoo import http


class ContactCreate(Survey):

    def survey_submit(self, survey_token, answer_token, **post):
        """function to create new partners if we click submit button in
        survey"""
        res = super(ContactCreate, self).survey_submit(survey_token,
                                                       answer_token, **post)
        user_input = http.request.env['survey.user_input'].search([], limit=1)
        partner_details = {}
        # only enter if we click submit button in survey
        if user_input.state == 'done':
            for input_line in user_input.user_input_line_ids:
                contact_relation = http.request.env['contact.relation'].search([
                    ('question_id', '=', input_line.question_id.id)])
                # mapping the user data into res.partner fields
                if contact_relation:
                    contact_field = contact_relation.contact_field_id
                    field_name = http.request.env['ir.model.fields'].search([
                        ('id', '=', contact_field.id)]).name
                    partner_details[field_name] = input_line.value_char_box
            # creating partner, if it has name field filled
            if partner_details['name']:
                http.request.env['res.partner'].sudo().create(partner_details)
        return res
