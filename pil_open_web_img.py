#coding:utf8
'''

'''

#!/usr/bin/python
import requests
from StringIO import StringIO
from PIL import Image
import profile

def testRequest():
    image_name = 'test1.jpg'
    url = 'http://example.com/image.jpg'

    r = requests.get(url, stream=True)
    with open(image_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

def testRequest2():
    image_name = 'test2.jpg'
    url = 'http://jbcdn2.b0.upaiyun.com/2013/12/jbblog-logo.png'

    r = requests.get(url)

    i = Image.open(StringIO(r.content))
    #i.save(image_name)
    i.show()

if __name__ == '__main__':
    #profile.run('testUrllib()')
    #profile.run('testUrllib2()')
    profile.run('testRequest2()')

