# -*- coding: utf-8 -*-

from odoo import models, api


class CreateProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create_product(self, data, product):
        if data['name'] and data['price'] and data['cost']:
            product = self.create({
                'available_in_pos': True,
                'name': data['name'],
                'lst_price': data['price'],
                'standard_price': data['cost'],
                'pos_categ_id': int(data['category']),
                'image_1920': data['image'],
            })
            print(product.id)
            created_product = self.env['product.product'].sudo().browse(
                product.id)
            data = {
                'name': created_product['name'],
                'lst_price': created_product['lst_price'],
                'standard_price': created_product['standard_price'],
                'pos_categ_id': created_product['pos_categ_id'].id,
                'image_1920': created_product['image_1920'],
            }
            return data

    @api.model
    def edit_product(self, data, product):
        values_to_update = {}
        if 'name' in data and data['name']:
            values_to_update['name'] = data['name']
        if 'price' in data and data['price']:
            values_to_update['lst_price'] = data['price']
        if 'cost' in data and data['cost']:
            values_to_update['standard_price'] = data['cost']
        if 'category' in data and data['category']:
            values_to_update['pos_categ_id'] = int(data['category'])
        if 'image' in data and data['image']:
            values_to_update['image_1920'] = data['image']
        self.browse(int(product[0]['id'])).write(values_to_update)
        updated_product = self.env['product.product'].sudo().browse(
            int(product[0]['id']))
        data = {
            'display_name': updated_product['name'],
            'lst_price': updated_product['lst_price'],
            # 'standard_price': updated_product['standard_price'],
            'pos_categ_id': updated_product['pos_categ_id'].id,
            'image_1920': updated_product['image_1920'],
        }

        return data
