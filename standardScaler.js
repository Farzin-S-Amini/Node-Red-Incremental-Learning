module.exports = function(RED){
	function StandardScalerNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/standardScaler.py'
		node.config = {
			target: config.target || 'y',
			savePath: config.savePath || "StandardScaler.sav"
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("StandardScaler", StandardScalerNode)
}
