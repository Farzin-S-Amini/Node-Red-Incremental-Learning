from creme import metrics
import pickle
import json

#read configurations
config = json.loads(input())

modelPath = config['modelPath']
target = config['target']
m = config['metric']


if (m == "MAE"):
	metric = metrics.MAE()
elif (m == "MSE"):
	metric = metrics.MSE()
elif (m == "RMSE"):
	metric = metrics.RMSE()
elif (m == "RMSLE"):
	metric = metrics.RMSLE()
elif (m == "SMAPE"):
	metric = metrics.SMAPE()


while True:

	#wait request
	data = input()

	Xi = json.loads(data)
	yt = float(Xi.pop(target))

	loaded_model = pickle.load(open(modelPath, 'rb'))

	yp = loaded_model.predict_one(Xi)
	print("GT: ", yt)
	print("P: ", yp)

	print(metric.update(yt, yp))
