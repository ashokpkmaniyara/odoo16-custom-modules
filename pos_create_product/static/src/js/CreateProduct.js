odoo.define('pos_product_creation.product_create_popup', function(require) {
    'use strict';

    const { useState, useRef} = owl;
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    class CreateProduct extends AbstractAwaitablePopup {
        setup() {
            super.setup();
            const category = this.props.categories;
            const product = this.props.products;
            console.log('prod',product)

            this.nameInput = useRef('name');
            this.priceInput = useRef('price');
            this.costInput = useRef('cost');
            this.categoryInput = useRef('category');
            this.imageInput = useRef('image');

            this.state = useState({
                name: "",
                price: "",
                cost: "",
                category:3,
                image: "",
            });

        }

        back() {
            this.env.posbus.trigger('close-popup', {
                popupId: this.props.id,
            });
        }

        updateState(ev) {
            const fieldName = ev.target.name;
            if (fieldName === 'image') {
                const fileInput = ev.target;
                const file = fileInput.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onloadend = () => {
                        const base64Data = reader.result.split(',')[1];
                        this.state.image = base64Data;
                    };
                    reader.readAsDataURL(file);
                }
                } else {
                    this.state[fieldName] = ev.target.value;
                }
        }

        async load_server_data(){
            const loadedData = await this.env.services.rpc({
                model: 'pos.session',
                method: 'load_pos_data',
                args: [[odoo.pos_session_id]],
            });
            await this.env.pos._loadProductProduct(loadedData['product.product']);
            return this.env.pos.after_load_server_data();
        }

        async createEditProduct() {
            console.log('edit=',this.props.products)
            console.log('create=',this.props.categories)
            console.log('state=',this.state)
            console.log('this1=',this)
            this.rpc({
                    model: 'product.product',
                    method: this.props.products ? 'edit_product' : 'create_product',
                    args: [this.state,this.props.products]
                }).then((data) => {
                    if(data){
                        console.log(this.props.products)
                        if(!data['standard_price']){
                        if(this.state.name){
                            this.env.pos.db.product_by_id[this.props.products[0]['id']]['display_name'] = this.state.name}
                        if(parseFloat(this.state.price)){
                        this.env.pos.db.product_by_id[this.props.products[0]['id']]['lst_price'] = parseFloat(this.state.price)}
                        if(this.state.category){
                        this.env.pos.db.product_by_id[this.props.products[0]['id']]['pos_categ_id'] = this.state.category}}
                        this.load_server_data();
//                        this.showScreen('ProductScreen')
                        this.env.posbus.trigger('close-popup', {
                            popupId: this.props.id,
                        });
                    }else{
                        this.showPopup("ErrorPopup", {
                            title: "Error",
                            body: "We need to fill all items.",
                        })
                    }
                })
        }
    }
    CreateProduct.template = 'CreateProduct';
    Registries.Component.add(CreateProduct);

    return CreateProduct;
});
