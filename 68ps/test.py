#coding:utf8
'''
desc :

'''

from myutils.site import Site
from myutils.page import Page
from bs4.element import Tag


if __name__ == '__main__':
    url = 'http://www.68ps.com/down/down_bz.asp?pageno=2'
    mysite = Site(url)
    
    startpage = Page(url)
    startpage.get_page_content()
    #print startpage.soup
    soup = startpage.soup
    
    all_target_a = soup.find_all(attrs={"class": "in-center4"})
    #print 'len = ', len(all_target_a)
    
    for i in all_target_a:
        if i.name == 'a':    
            print i.get('href'),i.string
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
