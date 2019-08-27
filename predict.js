module.exports = function(RED){
	function PredictNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/predict.py'
		node.config = {
			modelPath: config.modelPath || "LogisticRegression.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("Predict", PredictNode)
}
