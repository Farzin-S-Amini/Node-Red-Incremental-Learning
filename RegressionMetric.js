module.exports = function(RED){
	function RegressionMetricNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/RegressionMetric.py'
		node.config = {
			target: config.target || 'y',
			modelPath: config.modelPath || "LinearRegression.sav",
			metric: config.metric || "MAE"
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("RegressionMetric", RegressionMetricNode)
}
