	 
module.exports = function(RED){
	function OneVsRestClassifierNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/OneVsRestClassifier.py'
		node.config = {
			savePath: config.savePath || "OneVsRestClassifier.sav",
			target: config.target || 'y',
			l2: Number(config.l2) || 0,
			optimizer: config.optimizer,
			lr: Number(config.lr) || 0.1,
			AdaBound_lr: Number(config.AdaBound_lr) || 0.001,
			rho: Number(config.rho) || 0.9,
			beta_1: Number(config.beta_1) || 0.9,
			beta_2: Number(config.beta_2) || 0.999,
			eps: Number(config.eps) || 1e-08,
			gamma: Number(config.gamma) || 0.001,
			final_lr: Number(config.final_lr) || 0.1,
			alpha: Number(config.alpha) || 0.05,
			beta: Number(config.beta) || 1.0,
			FTRL_l1: Number(config.FTRL_l1) || 0.0,
			FTRL_l2: Number(config.FTRL_l2) || 1.0
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("OneVsRestClassifier", OneVsRestClassifierNode)
}
