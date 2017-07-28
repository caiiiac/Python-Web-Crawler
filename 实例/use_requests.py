import requests

# 京东
# url = "https://item.jd.com/2330392.html"
# try:
# 	r = requests.get(url)
# 	r.raise_for_status()
# 	r.encoding = r.apparent_encoding
# 	print(r.text[:1000])
# except:
# 	print("爬虫失败")


# 亚马逊
# url = "https://www.amazon.cn/gp/product/B0094DVNT6"
# try:
# 	kv = {'User-Agent' : 'Mozilla/5.0'}
# 	r = requests.get(url, headers=kv)
# 	r.raise_for_status()
# 	r.encoding = r.apparent_encoding
# 	print(r.text[:1000])
# except:
# 	print("爬虫失败")


# 百度搜索
# keyword = "Python"
# try:
# 	kv = {'wd' : keyword}
# 	r = requests.get("http://www.baidu.com/s", params = kv)
# 	print(r.requests.url)
# 	r.raise_for_status()
# 	print(len(r.text))
# except:
# 	print("爬虫失败")


# 图片爬取
import os
# url = "http://www.pp3.cn/uploads/201610/2016103006.jpg"
# root = "/Users/caiiiac/Desktop/"
# path = root + url.split('/')[-1]

# try:
# 	if not os.path.exists(root):
# 		os.mkdir(root)
# 	if not os.path.exists(path):
# 		r = requests.get(url)
# 		with open(path, 'wb') as f:
# 			f.write(r.content)
# 			f.close()
# 			print('文件保存成功')
# 	else :
# 		print('文件已经存在')
# except:
# 	print('爬虫失败')



#IP地址查询全代码
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
	r = requests.get(url+'202.204.80.112')
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text)
except:
	print("爬取失败")