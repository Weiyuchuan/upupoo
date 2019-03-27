import requests,re
from lxml import etree
import os


header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for i in range(50):
    url = 'http://wallpaper.upupoo.com/store/browVi/1-0-0-{}.htm'.format(i)
    response = requests.get(url,headers=header)
    # print(response.content.decode('utf-8'))
    req = etree.HTML(response.content.decode('utf-8'))
    url_list = req.xpath('//div[@class="mask"]/a/@href')
    title_list = req.xpath('//div[@class="bigBoxBtm"]/p/text()')
    # print(url_list)
    for url,title in zip(url_list,title_list):
        base_url='http://wallpaper.upupoo.com'+url
        # print(title)
        # print(base_url)
        resp = requests.get(url=base_url,headers=header).text
        # print(resp.content.decode('utf-8'))
        url_2 = re.findall("var video = loadVideo\('(.*?)',",resp)[0]
        print(url_2)
        # print(html_1.body())
        content = requests.get(url=url_2,headers=header).content
        try:

            with open('./upupo桌面视频/{}.mp4'.format(title),"wb")as f:
                f.write(content)
        except:
            pass