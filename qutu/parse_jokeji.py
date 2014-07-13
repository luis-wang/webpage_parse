#coding:utf8
'''

'''
import os,sys
import urllib,urllib2
from bs4 import BeautifulSoup
from persistent_qutu import insert,dbconn,find_ele,jokeji_dbconn

import requests
import dhtmlparser as d
from datetime import datetime as dt

base_url = 'http://gaoxiao.jokeji.cn'


def img_downloading(imgsrc, img_path):
    #urllib.urlretrieve(imgsrc, img_path)
    r = requests.get(imgsrc, stream=True)
    print 'img_path = ', img_path
    if r.status_code == 200:
        with open(img_path, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
    else:
        print 'r.status_code = ',r.status_code
        print u'请求失败'


def down_image(imgsrc):
    "把图片保存到磁盘空间"
    global img_dir
    
    try:
        print '-1-',
        fname = imgsrc.strip().split('/')[-1]
        print '-2-',
        img_path = os.path.join(img_dir, fname)
        print '-3-',
        img_downloading(imgsrc, img_path)
        print '-4-',
    except:
        print u'下面失败:src = ',imgsrc
        print '-5-',
        
    
    return img_path
    
    

def save_img(info):
    """
    {'src':src, 'title':title, 'overview':title_word}
    """
    db_imgs = jokeji_dbconn()
    
    ele = dict(src=info['src'], 
               title=info['title'], 
               overview=info['overview'],
               date1=dt.now(),
               )
    #插入
    if not find_ele(db_imgs, ele):
        insert(db_imgs, ele)
        #把图片保存到磁盘空间
        img_path = down_image(info['src'])
        
        #更新图片文件的路径
        #update({"_id": ObjectId("52818bad705d834f989b83af")},{"$set":{u'name': u'wxd1'}})
        db_imgs.update(ele, {"$set":{u'img_path': img_path}})
        print u'已保存：',info['src']
        
    else:
        print u'重复 ：',ele['src']
        
            

def parse_to_url(to_url='', title_word=''):
    "http://gaoxiao.jokeji.cn/GrapHtml/quweigaoxiao/20140709211210.htm"
    
    html_doc = urllib2.urlopen(to_url).read()
    html_doc = html_doc.decode('gbk').encode('utf8')
    
    dom = d.parseString(html_doc)
    
    target_uls = []  #要找的目标ul
    #找出所有的ul先
    uls = dom.find('ul')
    
    #找出目标ul的列表
    for ul in uls:
        ul_content = ul.getContent()
        sub_dom = d.parseString(ul_content)
        
        #rule 1,ul下面应该找不到a标签
        aes = sub_dom.find('a')
        if len(aes) > 0:
            continue
        
        #rule 2,ul下面应该能找到b标签
        bes = sub_dom.find('b')
        if len(bes) == 0:
            continue
        
        #rule 3 ,ul下面可以找到至少一个img ,且有属性style="CURSOR: hand"
        handes = sub_dom.find('img',{"style":"CURSOR: hand"})
        if len(handes) == 0:
            continue
        
        #最后余下的应该就是目标了
        target_uls.append(ul)
    
    info = []
    #解析目标ul
    for ul in target_uls:
        text = ul.getContent()
        #找出下面所有的img标签
        sub_dom = d.parseString(text)
        imgs = sub_dom.find('img')
        
        for img in imgs:
            src = base_url + img.params['src']
            title = img.params['alt']
            
            info.append({'src':src, 'title':title, 'overview':title_word})
    
    #保存起来
    for i in info:
        #print i['src'],i['title']
        save_img(i)
        
            
                        
        

if __name__ == '__main__':
    print 'start...'
    
    urls = ['http://gaoxiao.jokeji.cn/list/list_1.htm',
            'http://www.taoqutu.com/last_1000.html', #上次获取到的位置
           ]
    end_url = 'http://www.taoqutu.com/last_1500.html'
    
    #img_dir = 'C:/data/imgs/qutu/1000_1500/'
    img_dir = 'E:/2kkkkk/jokeji/'
    
    url = urls[0]
    
    #下载起始的页面文档
    html_doc = urllib2.urlopen(url).read()
    html_doc = html_doc.decode('gbk').encode('utf8')
    
    dom = d.parseString(html_doc)
    
    #-1-,找到所有的list_list的div
    container_divs = dom.find("div", {"class": "list_list"})
    
    for div in container_divs:
        sub_doc = div.getContent()  #每个列表中的子html
        sub_dom = d.parseString(sub_doc)
        
        #找到每个小图集的，这几张图片的概述
        imgs = sub_dom.find('img')
        title_word = ''
        if len(imgs):
            title_word = imgs[0].params["alt"]
        
        print '=============title_word =========== ',title_word
        
        #这个小图集url
        to_url = base_url + sub_dom.find('a')[0].params['href']
        print '++开始爬取图集页面：%s ' % to_url
        
        parse_to_url(to_url=to_url, title_word=title_word)
        

    
    print '****'
    
    
        
        

    
    
    
    '''
    nextpage_tag = soup.find(attrs={"class": "easypagerNextpage"})
    while nextpage_tag:
        crawler_page(soup)
        
        #找下一个页面
        url = 'http://www.taoqutu.com' + nextpage_tag.get('href')
        if url == end_url:
            break
        print u'***正在解析 ：url = ',url
        
        
        html_doc = urllib2.urlopen(url).read()
        html_doc = html_doc.decode('gbk').encode('utf8')
        soup = BeautifulSoup(html_doc)
        nextpage_tag = soup.find(attrs={"class": "easypagerNextpage"})        
    '''
        
    
    #go(url)
    print 'end....'
    
    
    





