#coding=utf8
from selenium import webdriver
import time

from pathlib import Path
import os

import csv
import json
import requests
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKC
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_PKC
from random import choice
import random
 
import hashlib

import sys
import asyncio
import time
from pyppeteer import launch
from pyppeteer_stealth import stealth



def md5(str):
    md5 = hashlib.md5()   				# 创建md5加密对象
    md5.update(str.encode('utf-8'))  	# 指定需要加密的字符串
    str_md5 = md5.hexdigest()  			# 加密后的字符串
    return str_md5


 
def get_random_imei():
    # 定义一个长度为14字符类的数字
    num = str(random.randint(10000000000000, 99999999999999))
    # 计算最后一位校验值
    num_list = list(num)
    # 数字和
    math_sum = 0
    for i in range(1, len(num_list)+1):
        # 如果是偶数
        if i % 2 == 0:
            take_two_num = int(num_list[i-1]) * 2
            # 判断乘于2之后的数，是一位还是二位，二位的话就， 
            if len(str(take_two_num)) == 2:
                for j in list(str(take_two_num)):
                    math_sum = int(j) + math_sum
            else:
                math_sum = take_two_num + math_sum
        # 如果是奇数的话，直接相加
        else:
            math_sum = int(num_list[i-1]) + math_sum
 
    # 根据math_sum得出校验位
    last_num = list(str(math_sum))[-1]
    if last_num == 0:
        check_num = 0
        imei = num + str(check_num)
        return imei
 
    else:
        check_num = 10 - int(last_num)
        imei = num + str(check_num)
        return imei
 

 

# get crypt
def encrypt(plaintext):
        """
        client 公钥进行加密
        plaintext:需要加密的明文文本，公钥加密，私钥解密
        """

        # 加载公钥
        rsa_key = RSA.import_key(open("./baidu_key/mssp_cpu_rsa_public_key.pem").read() )

        # 加密
        cipher_rsa = Cipher_PKC.new(rsa_key)
        en_data = cipher_rsa.encrypt(plaintext.encode("utf-8")) # 加密

        # base64 进行编码
        base64_text = base64.b64encode(en_data)
 
        return base64_text.decode() # 返回字符串
# get ip
def getIp():
    res = requests.get(url='http://http.tiqu.letecs.com/getip3?num=1&type=2&pro=&city=&yys=0&port=11&time=1&ts=1&ys=1&cs=1&lb=1&sb=0&pb=45&mr=1&regions=&gm=4&username=chukou01&spec=1')
    ips=json.loads(res.text)
    tmp_ip=ips["data"][0]["ip"]
    tmp_port=ips["data"][0]["port"]
    return {"ip":tmp_ip,"port":tmp_port}





def dict_reader():
	# 打开文件
	# with open("./data/test.csv", mode='rt',encoding="utf-8-sig") as f:
	#     # 基于打开的文件，创建csv.DictReader实例
	#     reader = csv.reader(f)
    #     for i in reader:  # 循环遍历出内容
    #         print(i)
    useragent = []
    with open("./data/test.csv") as file:  
        for line in file:
            # print(line)
            # string.strip()
            useragent.append(line.strip())
         

            # useragent.append(row)
        # print(useragent)
        return (choice(useragent))

# a=getIp()
# print(a)

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
#     imei=get_random_imei()
#     imei_c=encrypt(str(imei))
#     imMd5=md5(str(imei))
#     imMd5_c=encrypt(imMd5)
#     param="im="+imei_c+"&imMd5="+imMd5_c+"&aid="
#     access_url="https://cpu.baidu.com/1080/"+i+"?"+param





if __name__ == '__main__': 
    param_a=sys.argv[1]
    param_i=sys.argv[2]
    param_p=sys.argv[3]
    param_number=sys.argv[4]
    tmp_catch_path="e:\\tmp\\"+param_number
    my_file = Path(tmp_catch_path)
    if not my_file.exists():
         os.mkdir(tmp_catch_path)

    

async def main():
    # browser = await launch(headless=False)
    #{'ip': '49.76.41.188', 'port': 4218}
            i=0
#    for i in urlcodelist: 
        # for j in range(1, 500):
            # ips=getIp()
            imei=get_random_imei()
            imei_c=encrypt(str(imei))
            imMd5=md5(str(imei))
            imMd5_c=encrypt(imMd5)
            param="im="+imei_c+"&imMd5="+imMd5_c+"&aid="
            access_url="https://cpu.baidu.com/1080/"+param_a+"?"+param
            browser=await launch(
                 headless=False, 
                #  handleSIGINT=False,
                #  handleSIGHUP=False,
                #  handleSIGTERM=False,
                 userDataDir=tmp_catch_path,
                 args=[ "--no-sandbox","--proxy-server=http://"+param_i+":"+str(param_p)+""]) #http://'+ips["ip"]+':'+str(ips["port"])
            page = await browser.newPage()
            print("--proxy-server=http://"+param_i+":"+str(param_p)+"")
            await stealth(page)  # <-- Here
            useragent=dict_reader()
            await page.setUserAgent(useragent) # print(page)
            # await page.goto("https://bot.sannysoft.com/")
            print(access_url)
            await page.goto(access_url)
            # t1 = time.time()
            # time.sleep(10)  
            await asyncio.sleep(5)
            await browser.close()
asyncio.get_event_loop().run_until_complete(main())

    # print(access_url)
# ips=getIp()
# for i in urlcodelist:    
#     imei=get_random_imei()
#     imei_c=encrypt(str(imei))
#     imMd5=md5(str(imei))
#     imMd5_c=encrypt(imMd5)
#     param="im="+imei_c+"&imMd5="+imMd5_c+"&aid="
#     access_url="https://cpu.baidu.com/1080/"+i+"?"+param
#     # print(access_url)
   
#     # browser = webdriver.Chrome()#webdriver.Firefox() webdriver.Ie()
#     useragent=dict_reader()
#     option = webdriver.ChromeOptions()
#     #设置无头模式
#     # option.add_argument("--headless")
#     # option.add_experimental_option('excludeSwitches', ['enable-automation'])
#     # option.add_experimental_option('useAutomationExtension', False)
#     #设置user-agent
#     option.add_argument('user-agent='+useragent)
#     #添加代理
#     print(useragent)
    
#     option.add_argument('--proxy-server=http://'+ips["ip"]+':'+str(ips["port"])+'')
#     driver = webdriver.Chrome(options=option)
#     print('--proxy-server=http://'+ips["ip"]+':'+str(ips["port"])+'')
#     imei = get_random_imei()
#     driver.get(access_url)# get方法会一直等到页面被完全加载，然后才会继续程序
#     t1 = time.time()
#     time.sleep(500)  
#     # driver.stop_client()
#     driver.close()
     








# b=encrypt("aaa")
# print(b)