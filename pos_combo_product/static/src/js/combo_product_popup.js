/**@odoo-module **/

import AbstractAwaitablePopup from "point_of_sale.AbstractAwaitablePopup"
import Registries from "point_of_sale.Registries"


class ComboProductPopup extends AbstractAwaitablePopup {
    setup() {
        super.setup()
    }
    addToOrderLine(ev) {
        var product = this.props.products.filter(item => ev.currentTarget.dataset.id == item.id)[0];
        // Toggle the combo_selected property
        product.combo_selected = !product.combo_selected;
    }
    confirm() {
        // Filter out the selected products
        const selectedProducts = this.props.products.filter(product => product.combo_selected);
        console.log('aaaa',this.props.productsWithoutComboRequired[0]['combo_quantity'])
        // Trigger the addToOrderLine event for each selected product
        if(selectedProducts.length >= this.props.productsWithoutComboRequired[0]['combo_quantity']){
        selectedProducts.forEach(product => {
            this.env.posbus.trigger("addToOrderLine", { "product": product });
        });

        // Add a ribbon for selected products
            selectedProducts.forEach(product => {
                product.label2 = "Selected"; // You can customize the ribbon text or style
            });

        this.props.productsWithComboRequired.forEach(product => {
                    this.env.posbus.trigger("addToOrderLine", { "product": product });
                });
        // Close the popup
        this.env.posbus.trigger('close-popup', {
            popupId: this.props.id,
            response: { confirmed: true, payload: selectedProducts },
        });}
        else{
            this.showPopup("ErrorPopup", {
            title: "Error",
            body: "We need to select at least 2 items.",
        });
        }
    }
}
ComboProductPopup.template = "ComboProductPopup"
Registries.Component.add(ComboProductPopup)

