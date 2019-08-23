from creme import optim
from creme import linear_model
from creme import multiclass
import pickle
import json

#read configurations
config = json.loads(input())
init = 0

savePath = config['savePath']
target = config['target']
l2 = config['l2']
opt = config['optimizer']
lr = config['lr']
AdaBound_lr = config['AdaBound_lr']
rho = config['rho']
beta_1 = config['beta_1']
beta_2 = config['beta_2']
eps =  config['eps']
gamma = config['gamma']
final_lr = config['final_lr']
alpha = config['alpha']
FTRL_l1 =  config['FTRL_l1']
FTRL_l2 = config['FTRL_l2']


if (opt == "AdaBound"):
	optimizer = optim.AdaBound(lr, beta_1, beta_2, eps, gamma, final_lr)
elif (opt == "AdaDelta"):
	optimizer = optim.AdaDelta(rho, eps)
elif (opt == "AdaGrad"):
	optimizer = optim.AdaGrad(lr, eps)
elif (opt == "Adam"):
	optimizer = optim.Adam(lr, beta_1, beta_2, eps)
elif (opt == "FTRLProximal"):
	optimizer = optim.FTRLProximal(alpha, beta, l1, l2)
elif (opt == "Momentum"):
	optimizer = optim.Momentum(lr, rho)
elif (opt == "RMSProp"):
	optimizer = optim.RMSProp(lr, rho, eps)
elif (opt == "VanillaSGD"):
	optimizer = optim.VanillaSGD(lr)
elif (opt == "NesterovMomentum"):
	optimizer = optim.NesterovMomentum(lr, rho)
else:
	optimizer = None

log_reg = linear_model.LogisticRegression(optimizer, l2= l2)
OVRClassifier = multiclass.OneVsRestClassifier(log_reg)

output = {}

while True:

	#wait request
	data = input()

	Xi = json.loads(data)
	y = float(Xi.pop(target))

	output["Predict"] = OVRClassifier.predict_one(Xi)
	output["Truth"] = y

	model = OVRClassifier.fit_one(Xi, y)
	pickle.dump(model, open(savePath, 'wb'))

	print(json.dumps(output))