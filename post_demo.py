


# d={testtime:'CET202206'&name=35320212200478&qaction=%D1%A7%BA%C5%B2%E9%D1%AF}

import requests
import json
import os
# import qs from 'qs'

def douban_login():
    url="http://cet.xmu.edu.cn/cet.htm"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',

        'Content-Type': "application/x-www-form-urlencoded charset=gb2312",
        # 'cookie' : '_ga=GA1.3.25565576.1665576781; _gid=GA1.3.982592079.1670599442; ASPSESSIONIDCATSBATD=GJJBKECAGBODFBDAPHGHCFEB; ASPSESSIONIDAASTAATC=NLADJHKBBNECNANAEPBHIMIF; iPlanetDirectoryPro=TZeOgAyy7TL3Q4ael2p3vq; ASPSESSIONIDACSQDCSD=LICFHJLBOLFKOAPEOKANGEIE'
    }
    data={ "tsettime" :"CET202206",
           "name":"35320212200544",
           "qaction":"%D1%A7%BA%C5%B2%E9%D1%AF"}
    data_json=json.dumps(data)
    # data_qs=qs.stringify(data)
    print(type(data_json))
    # 发送请求
    res = requests.get(url,headers=headers,data=data_json)#content.decode()
    page_text=res.text
    # 保存文件
    with open('cet4.html','w',encoding='utf-8') as f:
        f.write(res.text)
    print("SUccessfully!!!")
douban_login()

