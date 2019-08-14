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
	print(Xi)

	print(loaded_model.predict_one(Xi))


