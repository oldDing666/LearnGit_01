#!/usr/bin/env python
# encoding: utf-8
"""
@author: DingFuBo
@email: 1101623201@qq.com
@file: 03_爬取笔趣阁小说.py
@project : 爬虫练习
@ide    : PyCharm
@time: 2020/1/2 9:54
"""

import requests
from bs4 import BeautifulSoup
import time

headers = {
    'Referer': 'https://www.52bqg.com/modules/article/authorarticle.php?author=%C3%A8%C4%E5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url = 'https://www.biqumo.com/8_8521/'
domain_url = 'https://www.biqumo.com'


def main():
    r = requests.get(url, headers=headers, timeout=500)

    text = r.content.decode('gbk')

    # print(text)

    # bs = BeautifulSoup(text, 'lxml')
    bs = BeautifulSoup(text, 'html5lib')
    #
    divs = bs.find_all('div', class_='listmain')[0]
    # print(divs)
    dl = bs.find_all('dl')[0]
    # print(dl)

    dds = dl.find_all('dd')[12:]
    unit_len = len(dds)
    count = 1
    for dd in dds:
        # print(dd)
        title = list(dd.stripped_strings)[0]
        # print(title)
        a = dd.find('a')
        # print(a['href'])
        content_url = domain_url + a['href']
        # print(content_url)
        one_page_content = catch_one_page(content_url)
        write_one_page(one_page_content)
        print('共有%d个内容, 已经下完%d个, 完成进度%.2lf%%' % (unit_len, count, (count/unit_len)*100))
        count += 1
        # time.sleep(0.5)
        # break


def catch_one_page(url):

    r = requests.get(url, headers=headers)
    text = r.content.decode('gbk')

    bs = BeautifulSoup(text, 'html5lib')
    divs = bs.find('div', class_='content')

    one_page_content = ''
    div_title_temp = divs.find('h1')
    div_title = list(div_title_temp.stripped_strings)[0]
    one_page_content +=div_title
    one_page_content += '\n'
    one_page_content += '\n'
    # print(div_title)
    # print()

    div_content_temp = divs.find_all('div', id='content')[0]
    div_contents = list(div_content_temp.stripped_strings)[1:]
    div_contents = div_contents[:-4]
    for div_content in div_contents:
        # print(div_content)
        one_page_content += div_content
        one_page_content += '\n'
        one_page_content += '\n'
    #     print()
    # print('*'*30)
    # print('*'*30)
    # print('*'*30)
    one_page_content += '*'*30 + '\n'+ '*'*30 + '\n'+ '*'*30 + '\n'+ '\n'+ '\n'+ '\n'
    return one_page_content

def write_one_page(text):
    with open('庆余年_3.txt', 'a', encoding='utf-8') as fp:
        fp.write(text)

if __name__ == '__main__':
    # url_2 = 'https://www.biqumo.com/8_8521/4936412.html'
    # url_2 = 'https://www.biqumo.com/8_8521/4937133.html'
    # print(catch_one_page(url_2))
    # write_one_page(catch_one_page(url_2))
    main()