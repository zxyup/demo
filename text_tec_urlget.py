# encoding:utf-8
import requests
import base64

# 获取access_token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Xe9yjUPOYftfyvq0FtglRuYG&client_secret=qH5VefXorovx7ulGDgEdEfXt2CCFroGk'
response = requests.get(host).json()['access_token']
if response:
    print(response)

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('123.jpg', 'rb')
# 将图片编码改为base64格式
img = base64.b64encode(f.read())

params = {"image":img}
access_token = response
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
