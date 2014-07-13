#coding:utf8
'''
desc :

'''
import os,sys
from datetime import datetime as dt
#加入myutils相关的包
utilpath = str(__file__).split('my_work_life')[0]
sys.path.append(os.path.join(utilpath,'myutils'))
from mongos import my_work_life_conn



def insert_idea(db):
    "插入一个新的idea"
    idea = {}
    
    url = 'http://qiwsir.github.io/qw.html'
    title = '两性健康'
    
    content = """
http://www.iyaya.com/yuer/zhinan-597
http://www.xywy.com/dzjk/nrsj/
http://health.pclady.com.cn/malehealth/
http://health.pclady.com.cn/healthzq/
"""
    
    idea['title']   = title
    idea['url']     = url
    idea['content'] = content.strip()
    
    idea['date'] = dt.utcnow()
    db.insert(idea)    

if __name__ == '__main__':
    print '开始执行....'
    db = my_work_life_conn()
    insert_idea(db)
    

    print '\n执行成功....'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
