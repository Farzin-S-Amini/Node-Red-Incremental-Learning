from creme import cluster
import pickle
import json
import ast

#read configurations
config = json.loads(input())
savePath = config['savePath']
n_clusters = config['n_clusters']
halflife = config['halflife']
sigma = config['sigma']
mu = config['mu']
random_state = config['randomState']

k_means = cluster.KMeans(n_clusters=n_clusters, halflife=halflife, mu=mu, sigma=sigma, random_state=random_state)

output = {}

while True:

	#wait request
	data = input()

	Xi = json.loads(data)

	output["Predict"] = k_means.predict_one(Xi)

	model = k_means.fit_one(Xi)
	pickle.dump(model, open(savePath, 'wb'))

	print(json.dumps(output))

