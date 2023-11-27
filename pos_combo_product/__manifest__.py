# -*- coding: utf-8 -*-
{
    "name": "POS Combo Product",
    "version": "16.0.1.0.0",
    "author": "Ashokpk",
    "category": "POS",
    "description": """This module helps to create combo products inside product 
    template page and sell those product on POS.""",
    "depends": ["base", "point_of_sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_combo_product/static/src/js/combo_product_popup.js",
            "pos_combo_product/static/src/js/models.js",
            "pos_combo_product/static/src/js/order_line_component.js",
            "pos_combo_product/static/src/js/order_line_model.js",
            "pos_combo_product/static/src/js/product_item.js",
            "pos_combo_product/static/src/css/product_item.css",
            "pos_combo_product/static/src/xml/pos_combo_product_popup.xml",
            "pos_combo_product/static/src/xml/pos_order_line.xml",
            "pos_combo_product/static/src/xml/pos_order_receipt.xml",
            "pos_combo_product/static/src/xml/pos_product_item.xml",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
