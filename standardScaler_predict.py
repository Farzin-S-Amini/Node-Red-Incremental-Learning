from creme import linear_model
import pickle
import json

#read configurations
config = json.loads(input())
savePath = config['savePath']

while True:

	#wait request
	data = input()

	Xi = json.loads(data)
	loaded_model = pickle.load(open(savePath, 'rb'))
	# print(Xi)

	print(json.dumps(loaded_model.transform_one(Xi)))


