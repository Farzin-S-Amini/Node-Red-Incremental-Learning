	 
module.exports = function(RED){
	function MNLogisticRegressionPredict(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/MNLogisticRegression_predict.py'
		node.config = {
			savePath: config.savePath || "MNLogisticRegression.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("MNLogisticRegression_predict", MNLogisticRegressionPredict)
}
