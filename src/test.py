import requests
from lxml import etree

#获取源码
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
html = requests.get("https://blog.csdn.net/it_xf?viewmode=contents" , headers = headers)

#打印源码
#print(html.text)

etree_html = etree.HTML(html.text)
content = etree_html.xpath('//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/article/a/div[1]/h4/text()')
for each in content:
    replace = each.replace('\n', '').replace(' ', '')
    if replace == '\n' or replace == '':
        continue
    else:
        print(replace)