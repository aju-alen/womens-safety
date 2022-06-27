from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import paho.mqtt.client as paho
from datetime import datetime
import math

datas=""


def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    global datas
    try:
        datas=msg.payload.decode("utf-8")
        print(datas)
        datalist=datas.split(",")
    except:
        datas=""
    
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.hivemq.com", 1883)
client.subscribe("womensafety", qos=1)
client.loop_start()


scaler=pickle.load( open( "scaler.pickle", "rb" ) )
# sm=pickle.load( open( "smotesample.pickle", "rb" ) )
LRmodel=pickle.load( open( "LR_model.pickle", "rb" ) )
@csrf_exempt 
def Predict_activity(request):
    print("datas===>",datas)
    mqlist=datas.split(",")
   
    abnormal=[5,6,7,9,10,11,12]
    txt="-9.3631,-0.028048000000000003,-1.5078,-0.14652,-0.11302999999999999,0.10527,-9.6546,0.87249,-0.19109,-0.7167,0.63654,0.5593899999999999,0.72835,-0.59567,-2.7074,-9.4626,-0.2648,-0.8549,-0.6694,0.16164,-0.0055158,-0.5515800000000001,-0.71662"
    txtlist=txt.split(",")
    datalist=[float(x) for x in txtlist]
    try:
        datalist[0]=float(mqlist[0])
        datalist[1]=float(mqlist[1])
        datalist[2]=float(mqlist[2])
        datalist[8]=float(mqlist[3])
        datalist[9]=float(mqlist[4])
        datalist[10]=float(mqlist[5])
    except:
        pass
    data=[]
    data.append(datalist)
    print(data)
    xdata=scaler.transform(data)
    # print(xdata.shape)
    ypred=LRmodel.predict(xdata)
    print(ypred)

    if(ypred[0] in abnormal):
        result="Abnormal"
    else:
        result="Normal"
    print(result)
   
    data={}
    
    data["result"]=result
    #data["temp"]=mqlist[6]+" "+"°C"
    #data["hrate"]=mqlist[7]+" "+"bpm"
    data["temp"]=str(32)+" "+"°C"
    
    data["hrate"]=str(70)+" "+"bpm"
    print(data)
    return JsonResponse(data,safe=False)


    



