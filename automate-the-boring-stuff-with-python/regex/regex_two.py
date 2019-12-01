import re


def group_result(content,regex):
	try:
		stringRegex = re.compile(regex,re.DOTALL)	#compile()方法加上re.DOTALL参数可以匹配换行符
		# stringRegex = re.compile(regex,re.IGNORECASE)	#第二个参数（下同）传入后可进行不区分大小写搜索 
		# stringRegex = re.compile(regex,re.I)
		# stringRegex = re.compile(regex)
		match = stringRegex.search(content)

		if match != None:
			print('group result is :' + match.group())
		else:
			print('there is no result')
	except Exception as e:
		print(e)


def find_all_result(content,regex):
	try:
		stringRegex = re.compile(regex)
		res = stringRegex.findall(content)

		if res not in [None,[],""]:
			print('all result is :')
			print(res)
		else:
			print('there is no result')

	except Exception as e:
		print(e)


def define_type_match(content,	regex = r'[1-4\[a-cB-D.*+?\]]'):
	"""自定义分组,方括号内任一字符匹配"""
	#方括号内，""符号表示范围，普通的正则表达式符号不会被解释
	find_all_result(content,regex)

def nin_define_type_match(content,regex=r'[^1-4\[a-cB-D.*+?\]]'):
	"""自定义分组,方括号内任一字符匹配"""
	#在左方括号后加上"^"符号表示取反，即限定范围之外	
	find_all_result(content,regex)


def start_end(content,regex=r'^1(\d)*9$'):
	"""插入字符和美元字符"""
	# find_all_result(content,regex)
	group_result(content,regex)		# ^符号表示搜索文本必须以其后的字符开头，$ 符号表示必须以其后结尾，匹配某个子集是不够滴

def match_all(content,regex=r'<.*?>'):		#非贪心匹配
	"""圆点通配符,匹配除换行符号之外的所有字符"""
	group_result(content,regex)

# content = 'abccdssff[aAD]AB124356DA[EC*&^%$#.??'
# define_type_match(content)
# nin_define_type_match(content)

# content = ['111108840289','01111088402898','0111108840289']
# for number in content:
# 	start_end(number)


tmp_content = "112212123214235hrthj6yn n6   gregrghttps://201606mp4.11bubu.com/20160731/club-256/1/xml/91_7fe50466651e4995fb85dd2476a6d2d0.mp4->video/mp4fdsfsfasrtwthr"
start_end(tmp_content,regex=r'https(.)+\.mp4')
 
# content = '<foafojfo<w\ner\nhni\nimm>'
# match_all(content)