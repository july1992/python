# coding=utf-8
import requests
import re
from  pyquery import  PyQuery as  pq
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
    response = requests.get('http://www.weather.com.cn/weather/101020100.shtml',headers=headers)
    response.encoding = 'utf-8'

    # print(response.text)
    html = response.text
    return html

def getdatafrompyquery(html):
    doc = pq(html)
    a = doc(".crumbs.fl a").text()
    result['location'] = a
    h = doc(".t.clearfix li.sky h1").contents()
    for i,value in enumerate(h):
        # print(i,value)
        index = 'day'+str(i)
        days[index] = value

    result['days'] = days

    p = doc(".t.clearfix li.sky p.wea").contents()
    for i,value in enumerate(p):
        # print(i,value)
        index = 'wea' + str(i)
        weas[index] = value

    result['weas'] = weas

    pattern = re.compile('<li class="sky.*?<span>(.*?)</span>/<i>(.*?)</i>.*?</li>',re.S)
    items = re.findall(pattern,html)
    for i,item in enumerate(items):
        # print(i,item)
        index = 'temp' + str(i)
        temps[index] = item[0] + '/' + item[1]

    result['temps'] = temps

    # ps = doc(".win span")
    # for t in ps:
    # 	t = pq(t)
    # 	print(t.attr('title'))
    # print(ps)

    pattern = re.compile('<p class="win">.*?<span title="(.*?)".*?</span>.*?<span title="(.*?)".*?</span>.*?</p>',re.S)
    items = re.findall(pattern,html)
    for i,item in enumerate(items):
        indexs = 'wins' + str(i)
        indexe = 'wine' + str(i)
        winstarts[indexs] = item[0]
        winends[indexe] = item[1]
    # print(item)

    result['winstarts'] = winstarts
    result['winends'] = winends

    pi = doc(".win i").contents()
    for i,value in enumerate(pi):
        index = 'win' + str(i)
        wins[index] = value
        print index
        print value
        print '-------------------'

    result['wins'] = wins

    # print(result)

    return result

def getdata(html):
    pattern = re.compile('<div class="crumbs fl".*?target="_blank">(.*?)</a>.*?</div>',re.S)
    items = re.findall(pattern,html)
    print(items)
    pass

def savedata(data):
    db = MySQLdb.connect('localhost','root','root','python')
    db.set_character_set('utf8')
    # print(db)
    cursor = db.cursor()

    print(data['days']['day1'])
    # data = '上海'
    sql = 'insert into weather(location) values("上海")'
    # try:
    cursor.execute(sql)
    db.commit()
    # except:
    # db.rollback()

    cursor.close()
    db.close()

def main():
    html = gethtml()
    # getdata(html)
    result = getdatafrompyquery(html)
    # print(result)
    savedata(result)
    print('save successed')

if __name__ == '__main__':
    main()

# coding=UTF-8