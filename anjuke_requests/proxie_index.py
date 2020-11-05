import requests

url = 'https://www.douban.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
# }

headers = {
    'User-Agent':'https://data.bilibili.com/log/web?00111415663117502971566311750267|web_player|HTML5PlayerNew80f3c4b|play_screen||5d7aa84d7cfde580cc7f53cf756f20d6|||38505728|67671238|1|1164|4|3|2|3|80|1139|||'
}
proxy = {'http': '61.128.208.94:3128'}
# data = requests.get(url=url,headers=headers,proxies=proxy).content.decode()
data = requests.get(url=url,headers=headers)
# with open('douban.html','w') as f:
#     f.write(data)

print(data.content)