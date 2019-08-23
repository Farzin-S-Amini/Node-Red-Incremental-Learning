module.exports = function(RED){
	function RegressionMetricNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/RegressionMetric.py'
		node.config = {
			target: config.target || 'y',
			predict: config.predict || 'Predict',
			metric: config.metric || "MAE"
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("RegressionMetric", RegressionMetricNode)
}
