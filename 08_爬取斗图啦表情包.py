#!/usr/bin/env python
# encoding: utf-8
"""
@author: DingFuBo
@email: 1101623201@qq.com
@file: 08_爬取斗图啦表情包.py
@project : 爬虫练习
@ide    : PyCharm
@time: 2020/1/7 9:50
"""


import requests
from bs4 import BeautifulSoup
from lxml import etree
from urllib import request
import os
import re
import time

headers = {
    'Referer': 'http://pos.baidu.com/s?hei=250&wid=300&di=u3185678&ltu=http%3A%2F%2Fwww.doutula.com%2Farticle%2Fdetail%2F8724609&psi=e1900ed78ffe6ad926cc43831c37a973&ltr=http%3A%2F%2Fwww.doutula.com%2F&dai=3&cdo=-1&cja=false&ti=%E6%94%AF%E4%BB%98%E5%AE%9D%E8%B4%A6%E5%8D%95%E8%A1%A8%E6%83%85%20-%20%E6%96%97%E5%9B%BE%E5%A4%A7%E4%BC%9A%20-%20%E9%87%91%E9%A6%86%E9%95%BF%E8%A1%A8%E6%83%85%E5%BA%93%20-%20%E7%9C%9F%E6%AD%A3%E7%9A%84%E6%96%97%E5%9B%BE%E7%BD%91%E7%AB%99%20-%20doutula.com&cpl=3&ps=1412x999&ccd=24&ari=2&tcn=1578360992&cmi=4&tpr=1578360992303&cec=UTF-8&psr=1920x1080&dc=3&dtm=HTML_POST&cce=true&dri=1&col=zh-CN&drs=3&cfv=0&dis=0&tlm=1578355748&par=1920x1050&pss=1396x3184&chi=3&ant=0&pis=-1x-1&pcs=1396x663&exps=111000,118001,110011&rtc=42.47',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

def catch_one_page(url):
    r = requests.get(url, headers=headers)
    text = r.text

    # bs = BeautifulSoup(text, 'lxml')
    bs = BeautifulSoup(text, 'html5lib')
    imgs_div = bs.find_all('div', class_='page-content text-center')[0]
    imgs_list = imgs_div.find_all('img')
    # imgs_src = []
    # print(imgs_list[23])
    for index, img in enumerate(imgs_list):

        # img_src = img['src']
        if img.has_attr('data-original'):
            img_src = img['data-original']
            # img_src = img['data-backup']
            print("本页共有%d张图片，正在下载第%d张。。。" % (len(imgs_list), index+1))
            '''
            获取文件后缀名
            '''
            img_front_name = img['alt']
            # print(type(img_src))
            img_end_name = img_src.split('.')[-1]
            '''
            或者
            '''
            # img_end_name = os.path.splitext(img_src)
            # print(img_end_name)

            '''
            windows系统中，某些字符不能作文件名，需要替换为空字符
            '''
            img_front_name = re.sub(r'[\?？\.，。！!]', '', img_front_name)
            img_name = str(img_front_name) + '.' + str(img_end_name)
            # print(img_name)
            # print(img_src)
            # imgs_src.append(img_src)


            '''
            保存文件
            '''
            # 会报403错误
            # request.urlretrieve(img_src, './images/' + img_name)
            time.sleep(0.5)

            # print(img_name)
            res = requests.get(img_src, headers=headers)
            with open('./images/' + img_name, 'wb') as fp:
                fp.write(res.content)
            time.sleep(0.5)
        else:
            print("第%d张图片无法下载" % (index+1))
    # print(text)
    # print(len(imgs_list))
    # print(len(imgs_src))
    # print(imgs_src)



def main():
    for i in range(1, 6):
        url = 'https://www.doutula.com/photo/list/?page=%d' % i
        print("当前正在下载第%d页的图片，共有5页" % i)
        catch_one_page(url)
        print("第%d页的图片下载完成，共有5页" % i)
        # break

    # url = 'https://www.doutula.com/photo/list/?page=2'
    # catch_one_page(url)

if __name__ == '__main__':
    main()