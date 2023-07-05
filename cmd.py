#coding=utf8
import os
import threading
import time
import requests
import json
urlcodelist= [
        "a492bec9",
        "adbf8c53",
        "ab395886",
        "f61eb7e5",
        "dac4afd9",
        "a3ce55d1",
        "ec58ee1d",
        "f207600d",
        "f54dbc0c",
        "f1d8629e",
        "bd991372"
        ]

# for i in urlcodelist:
#     for j in range(1, 500): 
#         print("python test.py "+i+"")
#         a = os.system("python test.py "+i+"") # 使用a接收返回值

 
def getIp():
    res = requests.get(url='http://http.tiqu.letecs.com/getip3?num=1&type=2&pro=&city=&yys=0&port=11&time=1&ts=1&ys=1&cs=1&lb=1&sb=0&pb=45&mr=1&regions=&gm=4&username=chukou01&spec=1')
    ips=json.loads(res.text)
    tmp_ip=ips["data"][0]["ip"]
    tmp_port=ips["data"][0]["port"]
    return {"ip":tmp_ip,"port":tmp_port}

def worker(number,ips):
    # for j in range(1, 500): 
    #     print("python test.py "+number+" "+ips["ip"]+" "+str(ips["port"]))
    #     # a = os.system("python test.py "+number+"") # 使用a接收返回值
    # return
    for i in urlcodelist:
        for x in range(1,10):
            print("python test.py "+i+" "+ips["ip"]+" "+str(ips["port"])+" "+i+"_"+str(x))
            a = os.system("python test.py "+i+" "+ips["ip"]+" "+str(ips["port"])+" "+i+"_"+str(x)) # 使用a接收返回值

ips=getIp()
print("python test.py  bd991372 "+ips["ip"]+" "+str(ips["port"]))
# for j in range(1, 3):
#     ips=getIp()
#     t = threading.Thread(target=worker,args=(j,ips))
#     t.start()