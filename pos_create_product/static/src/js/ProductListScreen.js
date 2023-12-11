odoo.define('pos_create_product.ProductListScreen', function(require) {
    'use strict';
    const { Gui } = require('point_of_sale.Gui');
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } =require("@web/core/utils/hooks");
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');
    var core = require('web.core');
    const { onMounted, onWillUnmount, useState, useRef } = owl;
    class ProductListScreen extends PosComponent {
        setup(){
            super.setup();

            this.state = {search: null,
                            product:this.env.pos.db.product_by_id};
            useListener('click-createProduct', this.onClick);
            useListener('click-editProduct', this.editChanges);
            this.searchWordInputRef = useRef('search-word-input-product');
        }

        back() {
            this.env.pos.db.product_by_id = this.state.product
            this.showScreen('ProductScreen');
        }
        async onClick() {
            try {
                var categories = Object.values(this.env.pos.db.category_by_id)
                Gui.showPopup('CreateProduct', {
                    categories,
                });
            } catch (error) {
                console.error(error);
            }
        }
        async editChanges(productId) {
            console.log('ffffff',productId.detail.productId)
            var categories = Object.values(this.env.pos.db.category_by_id)
            const products = await this.rpc({
                model: 'product.product',
                method: 'search_read',
                domain: [['id', '=', productId.detail.productId]],
                fields: ['image_1920','name', 'pos_categ_id', 'lst_price', 'standard_price'],
            });
            Gui.showPopup('CreateProduct', {
                products,
                categories,
            });
        }

        async updateProductList(event) {
            this.state.search = event.target.value;
            this.env.pos.db.product_by_id = await this.rpc({
                   model: 'product.product',
                    method: 'search_read',
                    domain: [['name','ilike',this.state.search]],
                    fields: ['display_name', 'default_code', 'pos_categ_id','lst_price'],
            })
             this.showScreen('ProductListScreen', {
                products: this.env.pos.db.product_by_id,
            });
            this.render(true);
        }
        _clearSearch() {
        this.searchWordInputRef.el.value = "";
        this.state.search = "";
        this.render(true);
        }
    };
ProductListScreen.template = 'ProductListScreen';
Registries.Component.add(ProductListScreen);
return ProductListScreen;
});