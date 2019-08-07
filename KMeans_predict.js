	 
module.exports = function(RED){
	function KMeansPredictNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/KMeans_predict.py'
		node.config = {
			savePath: config.savePath || "KMeans.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("KMeans_predict", KMeansPredictNode)
}
