#coding:utf8
'''
desc :

'''
from decruft import Document
import urllib2

urls = ['http://www.baidu.com',
        'ftp://ftp.zlatkovic.com/libxml/',
        'ftp://ftp.zlatkovic.com/libxml/md5sum.txt',
        'http://www.cnblogs.com/trump/archive/2013/06/25/3154478.html',
        'http://blog.sina.com.cn/s/blog_4b5039210102dtg6.html', #失败
        'http://blog.csdn.net/ithomer/article/details/7529022', #403错误
        'http://www.guao.hk/tag/google-china'] 


if __name__ == '__main__':
    print 'start...'
    f = urllib2.urlopen(urls[-1])
    #print 'f = ',f.read()
    
    print Document(f.read()).summary()
    
    print 'end...'