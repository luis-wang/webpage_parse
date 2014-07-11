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
    
    url = 'http://www.celeryproject.org/'
    title = 'celery 分布式的任务队列'
    
    content = """
Celery: Distributed Task Queue
Celery is an asynchronous task queue/job queue based on distributed message passing.    It is focused on real-time operation, but supports scheduling as well.
The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet,    or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).
Celery is used in production systems to process millions of tasks a day.


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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
