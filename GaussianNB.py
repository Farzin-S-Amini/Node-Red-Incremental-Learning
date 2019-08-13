import json
import pickle
from creme import naive_bayes

config = json.loads(input())

savePath = config['savePath']
target = config['target']
	

GaussianNB_classifier = naive_bayes.GaussianNB()

while True:

	#wait request
	data = input()

	Xi = json.loads(data)
	y = Xi.pop(target, None)
	print(Xi)
	print(y)
	
	model = GaussianNB_classifier.fit_one(Xi, y)
	pickle.dump(model, open(savePath, 'wb'))