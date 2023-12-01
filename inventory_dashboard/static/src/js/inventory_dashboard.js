/* @odoo-module */

import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
import { loadJS } from "@web/core/assets"
import { getColor } from "@web/views/graph/colors"
import { ChartRenderer } from "./chart_renderer"

const { Component, onWillStart, useState } = owl

export class InventoryDashboard extends Component {
    setup(){
    // to load the initial datas
        this.orm = useService("orm")
        this.useAction = useService('action')
        this.state = useState({
            period: 0,
            type: "inventory_valuation",
        })
        this.domain = []
        onWillStart(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js")
            await this.loadChartData()
            await this.loadWarehouseChartData()
            await this.loadTransferChartData()
        })
    }
    // to change the values based on selected period
    async onChangePeriod() {
        this.domain = []
        await this.loadChartData()
    }
    // to change the values based on selected type
    async onChangeType() {
        this.domain = []
        await this.loadChartData()
    }
    // to load dashboard data
    async loadChartData() {
        this.state.current_date = moment().subtract(this.state.period, 'days').format('DD/MM/YYYY')
        if (this.state.type === "incoming_stock") {
            if (this.state.period > 0) {
                this.domain.push(["date", ">", this.state.current_date])
            }
            await this.getChartData("Incoming Stock", "get_stock_incoming", "# of Quantity", [0, this.domain])
        } else if (this.state.type === "outgoing_stock") {
            if (this.state.period > 0) {
                this.domain.push(["date", ">", this.state.current_date])
            }
            await this.getChartData("Outgoing Stock", "get_stock_outgoing", "# of Quantity", [0, this.domain])
        } else if (this.state.type === "internal_transfer") {
            if (this.state.period > 0) {
                this.domain.push(["date", ">", this.state.current_date])
            }
            await this.getChartData("Internal Transfer", "get_internal_transfer", "# of Quantity", [0, this.domain])
        } else if (this.state.type === "average_expense") {
            this.domain = []
            if (this.state.period > 0) {
                this.domain.push(["create_date", ">", this.state.current_date])
            }
            await this.getChartData("Average Expense", "get_average_expense", "$", [0, this.domain])
        } else if (this.state.type === "inventory_valuation") {
            this.domain = []
            if (this.state.period > 0) {
                this.domain.push(["create_date", ">", this.state.current_date])
            }
            await this.getChartData("Inventory Valuation", "get_inventory_valuation", "$", [0, this.domain])
        }
    }
    // get data from model functions.
    async getChartData(chartTitle, apiMethod, chartLabel, domain) {
        this.state.primaryChartTitle = chartTitle
        const result = await this.orm.call("inventory.dashboard", apiMethod, domain)
        this.state.ChartConfig = {
            id: "main_chart",
            data: {
                labels: result.labels,
                datasets: [{
                    label: chartLabel,
                    data: result.data,
                    backgroundColor: result.labels.map((_, index) => getColor(index)),
                }]
            },
//            options: {
//                responsive: true,
//                plugins: {
//                    legend: {
//                        position: 'bottom',
//                    },
//                    title: {
//                        display: true,
//                        text: this.props.title,
//                        position: 'bottom',
//                  }
//               }
//            },
        }
        this.env.bus.trigger('renderEvent', { "config": this.state.ChartConfig })
    }
    // get data for warehouse chart
    async loadWarehouseChartData() {
        this.state.warehouseChartTitle = "Warehouse Stock"
        const result = await this.orm.call("inventory.dashboard", "get_stock_location", [0])
        this.state.warehouseChartConfig = {
            id: "warehouse_chart",
            data: {
                labels: result.labels,
                datasets: [{
                    label: "# of Quantities",
                    data: result.data,
                    backgroundColor: result.labels.map((_, index) => getColor(index)),
                }]
            },
        }
        this.env.bus.trigger('renderEvent', { "config": this.state.warehouseChartConfig })
    }
    // get all transfers data
    async loadTransferChartData() {
        this.state.transferChartTitle = "Transfers"
        const result = await this.orm.call("inventory.dashboard", "get_stock_move", [0])
        this.state.transferChartConfig = {
            id: "transfer_chart",
            data: {
                labels: result.labels,
                datasets: [{
                    label: "# of Transfers",
                    data: result.data,
                    backgroundColor: result.labels.map((_, index) => getColor(index)),
                }]
            },
        }
        this.env.bus.trigger('renderEvent', { "config": this.state.transferChartConfig })
    }
    viewTransfer(){
        this.useAction.doAction({
            type:'ir.actions.act_window',
            name:'Operation Types',
            res_model:'stock.picking.type',
            domain:[],
            views:[[false,'list'],[false,'form']]
        })
    }
    viewLocation(){
        this.useAction.doAction({
            type:'ir.actions.act_window',
            name:'Locations',
            res_model:'stock.location',
            domain:[],
            views:[[false,'list'],[false,'form']]
        })
    }
}

InventoryDashboard.template = "inventory_dashboard.InventoryDashboard"
InventoryDashboard.components = { ChartRenderer }
registry.category("actions").add("inventory_dashboard", InventoryDashboard)
