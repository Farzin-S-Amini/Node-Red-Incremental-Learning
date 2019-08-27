from creme import linear_model
import pickle
import json

#read configurations
config = json.loads(input())
modelPath = config['modelPath']

while True:

	#wait request
	data = input()

	Xi = json.loads(data)

	loaded_model = pickle.load(open(modelPath, 'rb'))
	print(Xi)

	print(loaded_model.predict_one(Xi))
