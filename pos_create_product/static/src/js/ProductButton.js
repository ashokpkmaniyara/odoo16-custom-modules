odoo.define('pos_create_product.ProductButton', function (require) {
   'use strict';
const { Gui } = require('point_of_sale.Gui');
const PosComponent = require('point_of_sale.PosComponent');
const { identifyError } = require('point_of_sale.utils');
const ProductScreen = require('point_of_sale.ProductScreen');
const { useListener } = require("@web/core/utils/hooks");
const Registries = require('point_of_sale.Registries');
const PaymentScreen = require('point_of_sale.PaymentScreen');
class ProductButton extends PosComponent {
    setup() {
       super.setup();
       useListener('click', this.onClick);
   }
    async onClick() {
        var self = this;
        var products = Object.values(this.env.pos.db.product_by_id)
        console.log(products)
         self.showScreen('ProductListScreen', {
            products: products,
        });

    }
}
ProductButton.template = 'ProductButton';
ProductScreen.addControlButton({
    component: ProductButton,
    condition: function() {
       return true;
    },
});
Registries.Component.add(ProductButton);
return ProductButton;
});