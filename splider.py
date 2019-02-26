# coding=utf-8
import requests
from requests.exceptions import  RequestException
import re
import json
from multiprocessing import Pool
import sys
import io

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)'
                         '</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    # print  items[0].item[2].decode('raw_unicode_escape')
    ss='\u6026\u7136\u5fc3\u52a8';
    print ss.decode('raw_unicode_escape')
    for item in items:

        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'auth':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

    pass

def write_to_file(content):
    reload(sys)

    sys.setdefaultencoding('utf-8')
    with io.open('result.txt', 'a',encoding='utf-8') as f:

        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)

    # 线程池
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])