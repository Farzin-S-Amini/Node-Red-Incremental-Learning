import json
import pickle
from creme import tree

config = json.loads(input())

savePath = config['savePath']
target = config['target']
patience = float(config['patience'])
max_depth = config['max_depth']
min_child_samples = config['min_child_samples']
confidence = config['confidence']
tie_threshold = config['tie_threshold']
	

DTClassifier = tree.DecisionTreeClassifier('gini', patience, max_depth, min_child_samples, confidence, tie_threshold)

while True:

	#wait request
	data = input()

	Xi = json.loads(data)
	y = Xi.pop(target, None)
	print(Xi)
	print(y)
	
	model = DTClassifier.fit_one(Xi, y)
	pickle.dump(model, open(savePath, 'wb'))