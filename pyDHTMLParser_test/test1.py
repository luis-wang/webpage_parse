#coding:utf8
'''

'''

import dhtmlparser as d

dom = d.parseString("""
    <root>
    <element name="xex" > eeeee <b>this is bold</b> </element>
    <element name="xex" > eeeee <b>this is bold</b> </element>
    </root>
""")
print '--2--'
print dom
print '--1--'
print dom.getTagName()
print '--3--'
print dom.childs[1].getTagName(),dom.childs[1].childs
print '--4--'
print dom.find("element")
print '--5--模糊查找 一个元素'
print dom.find("", fn = lambda x: "name" in x.params and x.params["name"] == "xex")
print '--6-- 类似pymongo的操作方式 ，而且属性的大小 不会限制 '
print dom.find("element", {"name":"xex"}) 
ele_tag = dom.find("element", {"NAME":"xex"})
print ele_tag  # parameter names (not values!) are case insensitive
print 'isTag() = ',len(ele_tag), ele_tag[0].isTag(), ele_tag[0].isOpeningTag()
print 'prettify() = ',ele_tag[0].prettify()
print 'getTagName() = ',ele_tag[0].getTagName()
print 'getContent() = ', ele_tag[0].getContent(), ele_tag[0].params["name"]



