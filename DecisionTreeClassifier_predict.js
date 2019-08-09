module.exports = function(RED){
	function DecisionTreeClassifierPredict(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/DecisionTreeClassifier_predict.py'
		node.config = {
			savePath: config.savePath || "DecisionTreeClassifier.sav",
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("DecisionTreeClassifier_predict", DecisionTreeClassifierPredict)
}
