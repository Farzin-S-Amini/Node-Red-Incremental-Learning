from creme import metrics
import pickle
import json

#read configurations
config = json.loads(input())

modelPath = config['modelPath']
target = config['target']

output = {}

while True:

	#wait request
	data = input()

	Xi = json.loads(data)
	yt = float(Xi.pop(target))

	loaded_model = pickle.load(open(modelPath, 'rb'))

	yp = loaded_model.predict_one(Xi)

	output["Predict"] = yp
	output["Truth"] = yt

	print(json.dumps(output))
