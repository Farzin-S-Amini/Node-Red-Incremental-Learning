module.exports = function(RED){
	function EvaluateNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/Evaluate.py'
		node.config = {
			target: config.target || 'y',
			modelPath: config.modelPath || "LinearRegression.sav"
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("Evaluate", EvaluateNode)
}
