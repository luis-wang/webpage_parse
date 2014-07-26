#coding:utf8
'''
凤凰网视频

'''
import os,sys,time
import urllib,urllib2
from bs4 import BeautifulSoup

import requests
import dhtmlparser as d
from datetime import datetime as dt

from myutils.page import Page
from myutils import download_util as down

#save_img_dir = r'E:\2kkkkk\0\videos'
#exe_path = r'E:\Python34\Scripts\you-get.exe'

save_img_dir = r'C:\data\videos\img'
save_video_dir = r'C:\data\videos'
exe_path = r'C:\Python34\Scripts\you-get.exe'

def get_resources(mydic):
    #1.先下载图片
    imgsrc = mydic['img']
    imgname = imgsrc.split('/')[-1]
    
    imdir = os.path.join(save_img_dir, imgname)
    down.down_image(imgsrc, imdir)
    
    #2.下载视频
    cmd = exe_path + ' '
    cmd += '-o ' + save_video_dir + ' '
    cmd += mydic['video_url']
    
    try:
        os.system(cmd)
    except Exception,e:
        print u'下载出错：%s' % str(e)
    
    


if __name__ == '__main__':

    url = 'http://so.v.ifeng.com/video?q=%E8%BD%BB%E6%9D%BE%E4%B8%80%E5%88%BB&c=5&p=1'
    first_num = 0
    stop_num = 100
    
    #循环每个页面
    has_next_page = True
    
    while first_num <= stop_num:
        print u'解析url:',url
        page = Page(url)
        soup = page.soup        
        
        #所有的div，包含了视频图片信息的
        divs = soup.find_all(attrs={'class':'s_r_list'})
        if len(divs) == 0:
            print u'未找到视频信息，停止操作'
            break
        
        for div in divs:
            mydic = {}
            
            a = div.find('a')
            #print u'视频地址：', a.get('href')
            mydic['video_url'] = a.get('href')
            
            img = div.find('img')
            #print u'缩略图地址：', img.get('src')
            mydic['img'] = img.get('src')
            
            vtime = div.find(attrs={'class':'s_r_time'})
            duration = vtime.string
            #print u'视频时长：',vtime.string
            mydic['duration'] = vtime.string
            
            
            #开始去下载
            get_resources(mydic)
            #print '--------------------------------'
        
        url = page.get_next_page_url()
        first_num += 1
        time.sleep(1)









