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

while True:

	#wait request
	data = input()
	print("mu: ", mu)

	d = ast.literal_eval(ast.literal_eval(data.strip()))
	print(type(d))
	print(d)
	# print(list(eval(data)))
	# print(type(list(eval(data))))
	Xi = dict(enumerate(d))
	print(Xi)
	# print(Xi)
	k_means.fit_one(Xi)

	pickle.dump(k_means, open(savePath, 'wb'))

