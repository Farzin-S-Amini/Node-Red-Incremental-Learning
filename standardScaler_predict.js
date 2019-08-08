module.exports = function(RED){
	function StandardScalerPredict(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/standardScaler_predict.py'
		node.config = {
			savePath: config.savePath || "StandardScaler.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("StandardScaler_predict", StandardScalerPredict)
}
