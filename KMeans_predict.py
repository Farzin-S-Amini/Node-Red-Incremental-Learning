from creme import cluster
import pickle
import json
import ast

#read configurations
config = json.loads(input())


while True:

	#wait request
	data = input()

	savePath = config['savePath']
	d = ast.literal_eval(ast.literal_eval(data.strip()))

	Xi = dict(enumerate(d))

	loaded_model = pickle.load(open(savePath, 'rb'))


	print(loaded_model.predict_one(Xi))
