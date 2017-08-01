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
print(soup.title.parent)

for parent in soup.a.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)