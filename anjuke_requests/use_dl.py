import requests
from lxml import etree
import re
import time
from openpyxl import workbook

# url = 'https://wuhan.anjuke.com/sale/rd1/?kw=南湖'
# headers = {
#     'User-Agent':'Mozilla/5.0(Windows NT 6.1;WOW64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/74.0.3729.169Safari / 537.36'
# }
# free_proxy = {'http':'111.231.91.104:8888'}
# response = requests.get(url=url,headers=headers,proxies=free_proxy)
#
# html = response.content.decode()
# print(html)
# with open('anjuke.html','w',encoding='utf8') as f:
#     f.write(html)

class SjhtSpider(object):
    def __init__(self):
        # self.url = 'https://wuhan.anjuke.com/sale/p{}-rd1/?kw={}&direct=yes#filtersort'
        self.url = 'https://cs.anjuke.com/sale/p{}-rd1/?kw={}&direct=yes#filtersort'
        self.headers = {
            'User-Agent':'Mozilla/5.0(Windows NT 6.1;WOW64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/74.0.3729.169Safari / 537.36'
        }
        self.proxy = {'http':'111.231.94.44:8888'}
        self.num = 0
        self.wb = workbook.Workbook()   # 创建Excel对象
        self.ws = self.wb.active  # 获取单签正在操作的表对象


    # 发送请求
    def get_response(self,url):
        response = requests.get(url=url,headers=self.headers,proxies=self.proxy)
        data = response.content.decode()
        # print(data)
        return data

    # 解析数据
    def parse_data(self,data):
        # 使用xpath解析想要的数据和下一页请求
        # 转换类型
        x_data = etree.HTML(data)

        room = x_data.xpath("//div[@class='house-details']/div[@class='details-item'][1]/span[1]/text()")
        size = x_data.xpath("//div[@class='house-details']/div[@class='details-item'][1]/span[2]/text()")
        floor = x_data.xpath("//div[@class='house-details']/div[@class='details-item'][1]/span[3]/text()")
        starting_time = x_data.xpath("//div[@class='house-details']/div[@class='details-item'][1]/span[4]/text()")
        site = x_data.xpath("//div[@class='house-details']/div[@class='details-item'][2]/span/text()")
        price = x_data.xpath("//div[@class='pro-price']/span[@class='price-det']/strong/text()")
        unit_price = x_data.xpath("//div[@class='pro-price']/span[@class='unit-price']/text()")


        self.w_data(room,size,floor,starting_time,site,price,unit_price)

        # 获取下一页链接
        next_page = x_data.xpath("//div[@class='multi-page']/a[@class='aNxt']/@href")
        # print(type(next_page[0]))
        if next_page:
            # print(next_page,'~'*30)
            time.sleep(1)
            next_data = self.get_response(next_page[0])
            self.parse_data(next_data)
        else:
            print("----------------已经爬完啦----------------")
            # self.save_data()

        self.num += 1

    # 写入数据到表格
    def w_data(self,room,size,floor,starting_time,site,price,unit_price):
        for i in range(len(room)):
            self.ws.append([room[i].encode("utf-8"),size[i].encode("utf-8"),floor[i].encode("utf-8"),starting_time[i].encode("utf-8"),re.sub(r'[ \n\xa0]','',site[i]).encode("utf-8"),price[i].encode("utf-8"),unit_price[i].encode("utf-8")])

        # print([room[i],size[i],floor[i],starting_time[i],re.sub(r'[ \n\xa0]','',site[i]),price[i],unit_price[i]])


    # 保存数据
    def save_data(self,file_name):
        self.wb.save(file_name+'.xlsx')

    # 启动程序
    def run(self):
        # 搜索关键字
        kw = "麓谷"
        # 起始url
        url = self.url.format('1',kw)
        file_name = "cs_lugu"
        # 发送请求
        data = self.get_response(url)
        # 添加excel写入标题
        self.ws.append(["厅室","面积","楼层","建造年限","具体位置","总价","单价"])
        # 解析数据
        self.parse_data(data)
        self.save_data(file_name)

SjhtSpider().run()
