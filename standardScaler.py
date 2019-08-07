import json
from creme import preprocessing

config = json.loads(input())
target = config['target']

scaler = preprocessing.StandardScaler()

while True:

	#wait request
	data = input()
	Xi = json.loads(data)
	print(Xi)
	y = Xi.pop(target, None)
	Xi = scaler.fit_one(Xi).transform_one(Xi)
	if (y != None):
		Xi['y'] = y

	print(Xi)

