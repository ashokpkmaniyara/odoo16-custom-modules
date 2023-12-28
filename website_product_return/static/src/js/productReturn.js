odoo.define('website_product_return.return', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.ProductReturnForm = publicWidget.Widget.extend({
        selector: '#sale_return_form',
        events: {
                'click .js_add_cart_json': 'onClickQuantity',
                'click #submit': 'onClickReturn',
            },

        onClickQuantity: function (ev) {
            var $link = $(ev.currentTarget);
            var $input = $link.closest('.input-group').find("input");
            var min = parseFloat($input.data("min") || 0);
            var max = parseFloat($input.data("max") || Infinity);
            var previousQty = parseFloat($input.val() || 0, 10);
            var quantity = ($link.has(".fa-minus").length ? -1 : 1) + previousQty;
            var newQty = quantity > min ? (quantity < max ? quantity : max) : min;

            if (newQty !== previousQty) {
                $input.val(newQty).trigger('change');
            }
            return false;
        },
        onClickReturn: function (ev) {
            var order = []
            var val = []
            $("tr.return_line").each(function(){
                var el = $(this)
                order = el.find(".quantity").data('order-id')
                val.push({'product_id': el.find(".quantity").data("product-id"),
                      'quantity': el.find(".quantity").val(),})
            });
            this._rpc({
            model: 'stock.picking',
            method: 'product_return',
            args: [val,order],
            }).then(function(result){
                if (result){
                    location.reload();
                }
            })
        },
    })
});
