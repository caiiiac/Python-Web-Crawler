import re

# search 在字符串中搜索匹配的第一个位置
# match = re.search(r'[1-9]\d{5}', 'BIT 100081')

# match 从开始位置起匹配
# match = re.match(r'[1-9]\d{5}', '100081 BIT')
# if match:
	# print(match.group(0))

# findall 以列表类型返回全部匹配子串
# ls = re.findall(r'[1-9]\d{5}', 'BIT 100081  TSU100084')
# print(ls)

# split 将字符串按照正则表达式匹配结果进行分割,返回列表
# ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
# print(ls)

# finditer 返回匹配结果的迭代类型
# for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
# 	if m:
# 		print(m.group(0))

# sub 替换所有匹配子串,返回替换后的字符串
# str = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
# print(str)

# 面向对象式用法
pat = re.compile(r'[1-9]\d{5}')
rst =  pat.search('BIT 100081')
if rst:
	print(rst.group(0))