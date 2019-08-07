	 
module.exports = function(RED){
	function KMeansNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/KMeans.py'
		node.config = {
			savePath: config.savePath || "KMeans.sav",
			n_clusters: parseInt(config.n_clusters) || 2,
			halflife: Number(config.halflife) || 0.5,
			sigma: Number(config.sigma) || 1,
			mu: Number(config.mu) || 0,
			randomState: Number(config.randomState) || 20
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("KMeans", KMeansNode)
}
