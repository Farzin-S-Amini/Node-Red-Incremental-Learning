from creme import metrics
import pickle
import json

#read configurations
config = json.loads(input())

predict = config['predict']
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
	xt = Xi.pop(predict)
	yt = Xi.pop(target)

	print(metric.update(yt, xt))