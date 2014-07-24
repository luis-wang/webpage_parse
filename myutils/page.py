#coding:utf8
'''
desc :
表示某一个页面，属于站点的下一级

'''

import os,sys
import urllib,urllib2
from bs4 import BeautifulSoup


class Page():
    
    def __init__(self,url=''):
        self.url = url    #属于哪一个站点
        self.soup = None
        #将一个页面的所有属性保存起来，供别的模块来调用 
        self.get_page_content()
    
    def get_page_content(self):
        "下载方式可以有很多种"
        if not self.url:
            raise Exception('未设置url值')
        
        try:
            html_doc = urllib2.urlopen(self.url).read()
            html_doc = html_doc.decode('gbk').encode('utf8')
            self.soup = BeautifulSoup(html_doc)
        except Exception,e:
            print '解析源网页(%s)出错！原因：%s' % (self.url, str(e))
        
        
    def get_elements(self,tagname):
        "获取标签为tagname的所有元素，如：获取所有table元素"
        pass
    
    def get_element(self,tagname):
        "获取单独一个元素"
        pass
    
    
    