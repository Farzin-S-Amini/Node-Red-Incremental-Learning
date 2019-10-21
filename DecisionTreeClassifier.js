module.exports = function(RED){
	function DecisionTreeClassifierNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/DecisionTreeClassifier.py'
		node.config = {
			target: config.target || 'y',
			savePath: config.savePath || "DecisionTreeClassifier.sav",
			patience: parseInt(config.patience) || 10,
			max_depth: parseInt(config.max_depth) || 5,
			min_child_samples: parseInt(config.min_child_samples) || 20,
			confidence: Number(config.confidence) || 1e-05,
			tie_threshold: Number(config.tie_threshold) || 0.05
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("DecisionTreeClassifier", DecisionTreeClassifierNode)
}
