#IP代理 本机ip:218.192.93.52
import requests

url='http://pv.sohu.com/cityjson'#获取ip地址的url
#设置 
#用户名：密码@代理端口号：端口号 (这个的密码不对，用的是涵道)
proxy={
    'http':'http://t10422119804320:oynsb8dh@tps194.kdlapi.com:15818',
    'https':'http://t10422119804320:oynsb8dh@tps194.kdlapi.com:15818'
}
respons=requests.get(url=url,proxy=proxy)
print(respons.text)
