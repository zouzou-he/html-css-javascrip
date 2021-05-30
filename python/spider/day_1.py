#登录China Unix
import time
import requests
import re
login_session=requests.session()

url_token="http://account.chinaunix.net/"

headers= {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "account.chinaunix.net",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36",
    }

respons=login_session.get(url=url_token,headers=headers)
#通过正则获得token值
respons_search=re.compile(r'XSRF-TOKEN=(.*?);')
respons_value=respons_search.search(respons.headers.get( 'Set-Cookie'))

url_login='http://account.chinaunix.net/login/login'
data={
        'username': 'zouyongke',
        'password': '18316158829',
        'token': respons_value, 
        't': int(time.time())  
}
login_respons=login_session.post(url=url_login,data=data,headers=headers)\

index_url='http://account.chinaunix.net/ucenter/user/index'
index_respons=login_session.get(url=index_url,headers=headers)
print(index_respons.text)
