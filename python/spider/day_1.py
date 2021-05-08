import requests

url="https://www.hao123.com/"
headers= {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.3"
    }

respons=requests.get(url=url,headers=headers)
peint(respons.request.headers) #查看发送请求头
print(respons.headers)    #返回的请求头
print(respons.status_code) #查看状态码
print(respons.apparent_encoding) #转二进制
#print(respons.json()[])  #查看json数据
with open ("hao123.html",'w',encoding="utf-8")as f:
    f.write(respons.content.decode())