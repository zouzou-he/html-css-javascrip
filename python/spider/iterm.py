import requests
from lxml import etree
 
class DangDang(object):
    def __init__(self) :
       self.headers={
            'Host':'bang.dangdang.com',
            'onnection':'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
    
    def get_url(self,page):
        url='http://bang.dangdang.com/books/fivestars/1-%s'%page

        response=requests.get(url=url,headers=self.headers)
        if response:
            html=etree.HTML(response.text)
            iterms=html.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')
            return iterms

    def pare_iterms(self,iterms):
        for iterm in iterms:
            title=iterm.xpath('.//div[@class="name"]/a/text()')


def main():
        d=DangDang()
        for page in range(1,26):
            iterm=d.get_url(page=page)
            print(d.pare_iterms(iterms=iterm))

if __name__=='__main__':
    main()
