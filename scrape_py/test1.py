#coding:utf8
'''
desc :
例子：http://zesty.ca/scrape/
文档:http://zesty.ca/python/scrape.html

'''

from scrape import *

url = 'http://www.baidu.com'
url = 'http://news.baidu.com/'
url = 'http://www.baidu.com/s?wd=猥亵&tn=SE_hldp01240_66rmgh5q'
url = 'http://www.s1979.com/tupian/china/201308/0697157506_33.html'
url = 'http://www.csdn.net/article/2014-07-24/2820837'

#go(self, url, data='', redirects=10, referrer=True, charset=None)
#ss = s.go(url,charset='gbk')
ss = s.go(url)

#print s.doc
#<Region 0:25751>
#print s.headers

d = s.doc
#print d.content[:70]
#print d.text[:100]
print d.text #将所有的文字显示出来，不包括多余的符号





















