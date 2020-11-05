import re
import requests

base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=美女&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=美女&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&cg=girl&pn={}&rn=30&gsm=5a&1566284493256='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
}
proxy = {'http': '61.128.208.94:3128'}

def requ(n):
    page = n * 30
    data = requests.get(url=base_url.format(page),proxies=proxy,headers=headers).content.decode()
    img_urls = re.findall(r'"thumbURL":"(.*?)"',data)
    i = 1
    for img_url in img_urls:
        img_data = requests.get(url=img_url,proxies=proxy,headers=headers).content
        with open('imgs/' + str(n) + '-' + str(i) + '.jpg', 'wb') as f:
            f.write(img_data)
        i += 1

if __name__ == '__main__':
    for n in range(100):
        requ(n)


