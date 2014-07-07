#coding:utf8
'''

'''
import os,sys
import urllib,urllib2
from bs4 import BeautifulSoup
from persistent_qutu import insert,dbconn,find_ele


img_dir = 'E:/2kkkkk/qutu/'

def down_image(src, imgid):
    "把图片保存到磁盘空间"
    try:
        #src = 'http://i1.taoqutu.com/2014/07/06110832568.jpg'
        fname = str(src.split('taoqutu.com')[1]).replace('/','-')[1:]
        img_path = os.path.join(img_dir, fname)
        urllib.urlretrieve(src, img_path)
    except:
        print '下面失败:src = ',src
        
    
    return img_path
    
    

def save_img(img, img_tag):
    db_imgs = dbconn()
     
    #所有的图片都有id
    if img.get('id'):
        ele = dict(id = img.get('id'), 
                   width = img.get('width'), 
                   height = img.get('height'),
                   title = img.get('alt'),
                   src = img.get('src'),
                   tag = img_tag,
                   )
        if not find_ele(db_imgs,ele):
            insert(db_imgs, ele)
            #print '成功插入:',ele
            #把图片保存到磁盘空间
            img_path = down_image(img.get('src'), img.get('id'))
            
            #更新图片文件的路径
            #update({"_id": ObjectId("52818bad705d834f989b83af")},{"$set":{u'name': u'wxd1'}})
            db_imgs.update(ele, {"$set":{u'img_path': img_path}})
            print '已保存：',img.get('src')
            
        else:
            print '已经存在 ：',ele
                
                
def crawler_page(soup):
    
    for i in soup.find_all(attrs={"class": "itembox"}):
        img_info = i.find('img')
        
        img_tag = i.find(attrs={"class": "xinxi"})
        if img_tag:
            imgtag = img_tag.string
        else:
            imgtag = ''
        
        #保存下来
        if img_info:
            save_img(img_info, imgtag)
                        
        

if __name__ == '__main__':
    print 'start...'
    urls = ['http://www.taoqutu.com/',
            'http://www.taoqutu.com/last_200.html', #上次获取到的位置
           ]
    
    url = urls[-1]
    
    #下载起始的页面文档
    html_doc = urllib2.urlopen(url).read()
    html_doc = html_doc.decode('gbk').encode('utf8')
    soup = BeautifulSoup(html_doc)      
    
    nextpage_tag = soup.find(attrs={"class": "easypagerNextpage"})
    while nextpage_tag:
        crawler_page(soup)
        
        #找下一个页面
        url = 'http://www.taoqutu.com' + nextpage_tag.get('href')
        print '***正在解析 ：url = ',url
        
        
        html_doc = urllib2.urlopen(url).read()
        html_doc = html_doc.decode('gbk').encode('utf8')
        soup = BeautifulSoup(html_doc)
        nextpage_tag = soup.find(attrs={"class": "easypagerNextpage"})        
        
        
    
    #go(url)
    print 'end....'
    
    
    





