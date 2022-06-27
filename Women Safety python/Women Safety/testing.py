import pickle
scaler=pickle.load( open( "scaler.pickle", "rb" ) )
# sm=pickle.load( open( "smotesample.pickle", "rb" ) )
LRmodel=pickle.load( open( "LR_model.pickle", "rb" ) )

# data=[[-3.6808,6.7683,-8.7909,-0.11722,-0.14652,-2.1365,-8.174,-6.5134,0.19852,-0.41839,-1.0354,-15.446,0.52143,-2.5823,-0.2571,-11.204,-0.36226,0.62745,-0.96715,0.10345,-1.5865,-15.028,1.9236]]
# xdata=scaler.transform(data)
# print(xdata.shape)
# ypred=LRmodel.predict(xdata)
# print(ypred)
abnormal=[5,6,7,9,10,11,12]
txt="-10.769,-1.9572,-1.913,-0.20931,-0.18001,3.9852,-6.8841,-3.2627,-0.29314,0.17824,-1.1061,156.05,53.302,33.143,-19.588,-8.4692,1.0765,-0.84118,-0.51335,-0.37716,-41.379,9.2805,178.86"
txtlist=txt.split(",")
datalist=[float(x) for x in txtlist]
data=[]
data.append(datalist)
print(data)
xdata=scaler.transform(data)
print(xdata.shape)
ypred=LRmodel.predict(xdata)
print(ypred)

if(ypred[0] in abnormal):
    result="Abnormal"
else:
    result="Normal"
print(result)