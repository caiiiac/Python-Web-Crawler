import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r. text

soup = BeautifulSoup(demo, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.a)

# print(soup.a.name)
# print(soup.a.parent.name)

# 属性
# print(soup.a.attrs)
# print(soup.a.attrs['class'])
# print(type(soup.a.attrs))

# tag的NavigableString
# print(soup.p)
# print(soup.p.string)
# print(type(soup.p.string))

# tag的Comment
#newsoup = BeautifulSoup("<b><!--This is a comment.--></b><p>This is not a comment</p>","html.parser")
#print(newsoup.b.string)
#print(type(newsoup.b.string)
#print(newsoup.p.string)
#print(type(newsoup.p.string))

# 标签树的下行遍历
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])

# 遍历儿子节点
# for child in soup.body.children:
# 	print(child)

# 遍历子孙节点
# for child in soup.body.descendants:
# 	print(child)

# 上行遍历
# print(soup.title.parent)

# for parent in soup.a.parents:
# 	if parent is None:
# 		print(parent)
# 	else:
# 		print(parent.name)

# 平行遍历
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.previous_sibling.previous_sibling)
# print(soup.a.parent)

# 遍历后续节点
# for sibling in soup.a.next_siblings:
# 	print(sibling)

# 遍历前续节点
# for sibling in soup.a.previous_siblings:
# 	print(sibling)

# prettify
# print(soup.prettify())
# print(soup.a.prettify())


# 信息提取
# <>.find_all(name, attrs, recursive, string, **kwargs)
# .name : 对标签名称的检索字符串
# .attrs : 对标签属性值的检索字符串,可标注属性检索
# .recursive : 是否对子孙全部检索,默认True
# .string : <>...</>中字符串区域的检索字符串

# .name 
# for link in soup.find_all('a'):
	# print(link.get('href'))

# 对标签名称的检索
# print(soup.find_all(['a','b']))

# for tag in soup.find_all(True):
# 	print(tag.name)

# import re
# for tag in soup.find_all(re.compile('b')):
# 	print(tag.name)

# .attrs
# print(soup.find_all('p','course'))
# print(soup.find_all(id='link1'))

# import re
# print(soup.find_all(id='link'))
# print(soup.find_all(id=re.compile('link')))


# .recursive
# print(soup.find_all('a',recursive=False))


# .string
# import re
# print(soup.find_all(string='Basic Python'))
# print(soup.find_all(string=re.compile('python')))

# <tag>(..)  等价于  <tag>.find_all(..)
# soup(..)   等价于 soup.find_all(..)
print(soup('a'))