#coding=utf-8
#!/usr/bin/python

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story王旭东</title></head>
<body>
<p class="title2"><b>The Dormouse's story</b></p>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""



soup = BeautifulSoup(html_doc)

#原样输出，但是会格式化
#-----------------------------------
#print(soup.prettify())

# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#.....
#    ...
#   </p>
#  </body>
# </html>


print 'soup.title= ', soup.title
# <title>The Dormouse's story</title>

print 'soup.title.name=', soup.title.name
# u'title'

print 'soup.title.string=',soup.title.string
# u'The Dormouse's story'


print 'soup.title.parent.name=', soup.title.parent.name
# u'head'

print 'soup.title.parent.string = ', soup.title.parent.string

print 'soup.p = ',soup.p

# <p class="title"><b>The Dormouse's story</b></p>

print 'soup.p[\'class\']=', soup.p['class']
soup.p['class']
# u'title'

print 'soup.a = ', soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

#找出所有的a标签
print "soup.find_all('a')=", soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print 'soup.find(id="link3")=', soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

print '================='

print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...

text1="""

<li><a href="/html/photo03/18932.html" target="_blank"><span>2013-10-09</span>丝袜骚妻喝醉了，全射到她的丝袜上【18P】</a></li>

<li><a href="/html/photo03/18931.html" target="_blank"><span>2013-10-09</span>丰满人妻 【32P】</a></li>

<li><a href="/html/photo03/18930.html" target="_blank"><span>2013-10-09</span>丰满少妇的野外自拍 【18P】</a></li>
"""

print '-----------------------------------'
soup = BeautifulSoup(text1)
for link in soup.find_all('a'):
    print(link.get('href'))
    print link.span.string
    print link.contents[0].string, link.contents[1]
    print '\n\n'
    
text2="""
<span class="next">下一篇:<a href=/html/photo03/18931.html>1丰满人妻 【32P】</a></span>
<span class="next">下一篇:<a href=/html/photo03/18931.html>2丰满人妻 【32P】</a></span>
<span class="nexts">下一篇:<a href=/html/photo03/18931.html>2rrrrr</a></span>
<span class="nexts">下一篇:<a href=/html/photo03/18931.html>3rrrrr</a></span>

<p class="class1">1</p>
<p class="class1 class2">2</p>
<p class="class2">3</p>
"""  
soup = BeautifulSoup(text2)
#print soup.find(class="next").a.get('href')

#这样可以找到含有next属性的所有标签
list_next = soup.findAll(True, 'next')[0].a.get('href')

print list_next


'''
In [2]: soup = bs4.BeautifulSoup('<div class="foo bar"></div>')

In [3]: soup(attrs={'class': 'bar'})
Out[3]: [<div class="foo bar"></div>]


soup.findAll(True, {'class': re.compile(r'\bclass1\b')})
'''














