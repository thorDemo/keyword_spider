import requests
from bs4 import BeautifulSoup
from random import sample
from lib.databases import KeyWords
from threadpool import makeRequests, ThreadPool


def rand_char():
    char = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(sample(char, 5))


def get_key(x):
    temp = rand_char()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': '%s.sz-linghang.com' % temp,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.142 Safari/537.36',
    }

    response = requests.get(url='http://temp.sz-linghang.com', headers=headers)
    soup = BeautifulSoup(response.content, 'html5lib')
    title = soup.title.string
    keyword = str(title).split('：')[0]
    try:
        KeyWords.insert({'words': keyword}).execute()
        print( '\033[1;32m %s \t\t关键词插入' % keyword)
    except Exception as e:
        print('\033[1;31m %s \t\t关键词重复' % keyword)


pool = ThreadPool(20)

make_requests = makeRequests(get_key, range(1, 100000))
[pool.putRequest(req) for req in make_requests]
pool.wait()

# file = open('key.txt', 'w+', encoding='utf8')
# data = KeyWords.select().where(KeyWords.id > 0)
# for line in data:
#     print(line.words)
#     file.write('%s\n' % line.words)
# file.close()
#
# file = open('C:/Users/Thor/Desktop/ip.txt', 'r', encoding='utf-8')
#
# for line in file:
#     print( 'iptables -I INPUT -s %s -j DROP' % line.strip())
