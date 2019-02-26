# coding=utf-8
import requests
import re
from pyquery import PyQuery as pq
import MySQLdb

# 查询天气
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

result = {}
days = {}
weas = {}
temps = {}
wins = {}
winstarts = {}
winends = {}

def gethtml():
    response = requests.get('http://www.gamedog.cn/gonglue/20161117/1948775.html',headers=headers)
    response.encoding = 'utf-8'

    # print(response.text)
    html = response.text
    return html

def getdatafrompyquery(html):

    str = '<div class="news_neirong">'
    content = html.partition(str)[2]

    # print content

    pattern = re.compile('<p.*?>(.*?)</p>',re.S)
    # pattern = re.compile('<p>(.*?)</p>',re.S)
    # pattern = re.compile('<p align="center">(.*?)</p>',re.S)
    # pattern = re.compile('<div class="news_neirong"><p>(.*?)</p></div>',re.S)
    # pattern = re.compile('<div class="news_neirong">.*?</div>',re.S)
    items = re.findall(pattern,html)
    for i,item in enumerate(items):
        print item

    return content

def main():
    html = gethtml()
    # getdata(html)
    result = getdatafrompyquery(html)
    # print(result)
    # savedata(result)
    print('save successed')

if __name__ == '__main__':
    main()

# coding=UTF-8