from re import compile

def find_result(content,regex):
	try:
		stringRegex = compile(regex)
		match = stringRegex.search(content)

		if match != None:
			print('result is :' + match.group())
		else:
			print('there is no result')
	except Exception as e:
		print(e)


def match_times(content,regex=r'3{3}5{2,}6{,5}'):
	"""匹配次数"""
	find_result(content,regex)	#regex规则：1.三次2.两到无线次数2.零到5次
	


def greedy(content,regex=r'(Ha){3,5}'):		#关于为什么要括号分组，下面有一个生动的例子
	"""贪心匹配（没有问号默认最长匹配）"""
	find_result(content,regex)

def non_greedy(content,regex=r'(Ha){3,5}?'):
	"""非贪心匹配(最短匹配，区别就是代表次数的大括号后面加一个问号，区别于一个或零个匹配的问号)"""
	find_result(content,regex)


# content = ['333335566666','33355555666','33355666666','335']
# content = 'HaHaHaHaHa'
content = 'HaHaHaHaHaaaaaaaa'


# for number in  content:
# 	match_times(number)
 
greedy(content,regex=r'Ha{3,5}')
# non_greedy(content)