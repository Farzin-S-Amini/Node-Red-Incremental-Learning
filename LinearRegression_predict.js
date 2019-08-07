	 
module.exports = function(RED){
	function LinearRegressionPredict(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/LinearRegression_predict.py'
		node.config = {
			savePath: config.savePath || "LinearRegression.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("LinearRegression_predict", LinearRegressionPredict)
}
