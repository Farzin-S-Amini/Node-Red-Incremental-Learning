	 
module.exports = function(RED){
	function OneVsRestClassifierPredict(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/OneVsRestClassifier_predict.py'
		node.config = {
			savePath: config.savePath || "OneVsRestClassifier.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("OneVsRestClassifier_predict", OneVsRestClassifierPredict)
}
