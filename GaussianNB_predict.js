module.exports = function(RED){
	function GaussianNBPredict(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/GaussianNB_predict.py'
		node.config = {
			savePath: config.savePath || "GaussianNB.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("GaussianNB_predict", GaussianNBPredict)
}
