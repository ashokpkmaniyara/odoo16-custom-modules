/** @odoo-module **/

import Registries from "point_of_sale.Registries";
const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
const {useState} = owl
export class CalculatorPopup extends AbstractAwaitablePopup{
    setup() {
      this.state = useState({
        user_input : '',
        value: '',
      })
      super.setup();
    }
    sendInput(input){
        const lastChar = this.state.user_input.slice(-1);
        const operators = ['+','-','/','%','*']
        if(typeof+input=='number' && !isNaN(input)){
            this.state.user_input+=input
        }
        else if(input=='.' && lastChar!='.'){
            const data = this.state.user_input.split(/['+','\-','/','%','*']/)
            console.log(data)
            data.forEach(element => {
                // Check if the element contains more than one period
                const periodCount = element.split('.').length - 1;
                if (periodCount < 1) {
                    console.log('aaa');
                    this.state.user_input += input;
                }
            });
        }
        else if (operators.includes(input) && operators.includes(lastChar) === false) {
            this.state.user_input += input;
        }
        else if(input=='C'){
            this.state.user_input = '';
        }
        else if(input=='Backspace'){
            this.state.user_input = this.state.user_input.slice(0, -1);
        }
        else if(input=='='){
            this.calculateResult();
            this.state.user_input = String(this.state.value);
        }
        else{}
    }
    calculateResult() {
        try {
            const userInputForEval = this.state.user_input.replace(/%/g, '*(1/100)');
            this.state.value = eval(userInputForEval);
        } catch (error) {
            this.state.value = 'Error';
        }
    }
}
CalculatorPopup.template = 'CalculatorPopup';
Registries.Component.add(CalculatorPopup);
