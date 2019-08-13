module.exports = function(RED){
	function GaussianNBNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/GaussianNB.py'
		node.config = {
			target: config.target || 'y',
			savePath: config.savePath || "GaussianNB.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("GaussianNB", GaussianNBNode)
}
