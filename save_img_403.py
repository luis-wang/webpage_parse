#coding:utf8
'''
desc :

'''

import urllib2,cookielib

site= "http://gaoxiao.jokeji.cn/UpFilesnew/2014/7/13/201471323337704.jpg"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)
page = ''
try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    s = e.fp.read().decode('gbk').encode('utf8')
    print s
    
'''
file = open(str(image_number), "wb")
            file.write(urlopen(image_url).read())
            file.close()
'''
if page:
    content = page.read()
    
    f = open('930.jpg','wb')
    f.write(content)
    f.close()
    
    
    print content
else:
    print '获取失败'
















