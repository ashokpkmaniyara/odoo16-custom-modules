/** @odoo-module **/

import PosComponent from 'point_of_sale.PosComponent';
import ProductScreen from 'point_of_sale.ProductScreen';
import { useListener } from "@web/core/utils/hooks";
import Registries from 'point_of_sale.Registries';
export class CalculatorButtons extends PosComponent {
        setup() {
          super.setup();
          useListener('click', this.onClick);
        }
        async onClick() {
            const { confirmed } = await this.showPopup("CalculatorPopup", {
                      Title: this.env._t("Calculator"),});
        }
}
CalculatorButtons.template = 'CalculatorButtons';
    ProductScreen.addControlButton({
        component: CalculatorButtons,
        condition: function() {
            return this.env.pos.config.virtual_calculator;
        }
    });
Registries.Component.add(CalculatorButtons);