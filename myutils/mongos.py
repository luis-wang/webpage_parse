#coding:utf8
'''
持久化一些操作
'''
import pymongo
from datetime import datetime as dt

host = '112.124.31.180'

def my_work_life_conn():
    conn = pymongo.Connection(host=host)
    db = conn.my_work_life  # 进入指定名称的数据库
    idea = db.idea          # 获取数据库里的某个 集合
    return idea


def test1():
    print '-1- connect---------------------'
    #-1- connect
    #conn = pymongo.Connection() # 连接本机数据库
    conn = pymongo.Connection(host=host) # 连接指定IP的数据库112.124.31.180
    db = conn.test # 进入指定名称的数据库
    users = db.users # 获取数据库里的 users 集合
    #users = db['users'] # 获取数据库里的 users 集合,也可以用字典来获取
    print 'users = ', users
    
    print '-2- insert---------------------'
    #-2- insert
    u = dict(name = "user1", age = 27, addr='上海市的嘛')
    # db.users.save(u) # 用 save 也可以插入
    db.users.insert(u) # 将数据插入到 users 集合
    users = db['users']
    print 'users = ', users
    
    print '-3- query---------------------'
    #-3- query-
    u2 = db.users.find_one({"name":"user1", 'age':27})
    print 'u2 = ', u2

def dbconn():
    "返回连接对象"
    conn = pymongo.Connection(host=host) # 连接指定IP的数据库112.124.31.180
    db = conn.qutu # 进入指定名称的数据库
    imgs = db.imgs # 获取数据库里的 imgs 集合
    return imgs
    

def insert(db_imgs,ele):
    db_imgs.insert(ele)
    
def find_ele(db_imgs,ele):
    return db_imgs.find_one(ele)

def querys(db_imgs, param):
    for p in db_imgs.find({"title": {'$regex': param}}):
        print p['title'],p['img_path'],p['src']  


if __name__ == '__main__':
    print 'start...'
    
    #插入一个新的idea
    db = my_work_life_conn()
    
    '''
    idea = dict()
    idea['title'] = '好的标题1'
    idea['url'] = '好的url1 '
    idea['content'] = '好的内容1 '
    idea['date'] = dt.utcnow()
    db.insert(idea)
    '''

    res = db.find() #{"title": "好的标题1"}
    for r in res:
        print r['title'], r['date'] if r.has_key('date') else 'not set date'
        
    
    
    print 'end'
    
    
    
    
    
