#coding:utf8
'''

'''
import os,sys
import urllib,urllib2
from bs4 import BeautifulSoup

def down_image(src, imdir):
    "把图片保存到磁盘空间"
    try:
        urllib.urlretrieve(src, imdir)
        return 0
    except Exception,e:
        print u'下载失败:src = %s ，错误原因：%s ' %(src, str(e))
        return 1


