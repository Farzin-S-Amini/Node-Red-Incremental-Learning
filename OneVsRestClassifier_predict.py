from creme import linear_model
import pickle
import json

#read configurations
config = json.loads(input())


while True:

	#wait request
	data = input()

	savePath = config['savePath']

	Xi = json.loads(data)
	loaded_model = pickle.load(open(savePath, 'rb'))
	print(Xi)

	print(loaded_model.predict_one(Xi))


