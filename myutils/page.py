#coding:utf8
'''
desc :
表示某一个页面，属于站点的下一级

'''

import os,sys
import urlparse
import urllib,urllib2
from bs4 import BeautifulSoup


class Page():
    
    def __init__(self,url='',init=True):
        self.url = url
        self.next_url_rule = 'accumulation'  #累加
        
        self.soup = None
        
        if init:
            #将一个页面的所有属性保存起来，供别的模块来调用 
            self.get_page_content()
    
    def get_page_content(self):
        "下载方式可以有很多种"
        if not self.url:
            raise Exception('未设置url值')
        
        try:
            html_doc = urllib2.urlopen(self.url).read()
            html_doc = html_doc.decode('utf8')#.encode('utf8')
            self.soup = BeautifulSoup(html_doc)
        except Exception,e:
            print '解析源网页(%s)出错！原因：%s' % (self.url, str(e))
        
        
    def get_elements(self,tagname):
        "获取标签为tagname的所有元素，如：获取所有table元素"
        pass
    
    def get_element(self,tagname):
        "获取单独一个元素"
        pass
    
    def get_next_page_url(self):
        "根据本站的规则，找出当前页面地址对应的下一页地址"
        #previous_url = 'http://so.v.ifeng.com/video?q=abc&c=5&p=2'
        
        if self.next_url_rule == 'accumulation':

            pr = urlparse.urlparse(self.url)
            #print urlparse.urlsplit(self.url)
            #找到请求的参数
            queries = pr.query
            query_list = queries.split('&')
            
            next_query = ''
            next_query_list = []
            
            for query in query_list:
                if query.startswith('p='):
                    current_num = query.split('p=')[-1]
                    next_query = 'p=' + str(int(current_num)+1)
                    next_query_list.append(next_query)
                else:
                    next_query_list.append(query)
            
            query_str = '&'.join(next_query_list)
            data = (pr.scheme, pr.netloc, pr.path, pr.params, query_str, pr.fragment) 
            
            return urlparse.urlunparse(data)
            
    

if __name__ == '__main__':
    print 'start...'
    url = 'http://so.v.ifeng.com/video?q=%E8%BD%BB%E6%9D%BE%E4%B8%80%E5%88%BB&c=5&p=1'
    page = Page(url,init=False)
    #print page.soup
    print page.url
    print page.get_next_page_url()
    
    
    print 'end...'   
    