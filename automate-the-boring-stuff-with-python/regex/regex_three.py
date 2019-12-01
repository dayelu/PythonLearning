import re

def replace_str(content,regex,replace):
	"""正则替换"""
	try:
		namesRegex = re.compile(regex)
		find = namesRegex.findall(content)
		match = namesRegex.search(content)
		find_group = match.group()
		print(find_group)
		print(find)
		res = namesRegex.sub(replace,content)
		print(res)
	except Exception as e:
		print(e)

content = 'Agent Alice gave the secret document to Agent Bob.'
# replace = 'dayelue'
# regex = r'Agent \w'			#贪心匹配,匹配以 Agent和空格开头, 后面接一个或多个数字字符下划线的字符串)
# regex = r'Agent \w+'			#非贪心匹配


regex = r'Agent (\w)\w*'
replace = r'\1***'			#sub()的第一个参数,不需要输入额外的专业字符,\1 表示第一个分组

replace_str(content,regex,replace)