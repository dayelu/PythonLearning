from re import compile

def group_result(content,regex):
	try:
		stringRegex = compile(regex)
		match = stringRegex.search(content)

		if match != None:
			print('group result is :' + match.group())
		else:
			print('there is no result')
	except Exception as e:
		print(e)


def find_all_result(content,regex):
	try:
		stringRegex = compile(regex)
		res = stringRegex.findall(content)		#findall方法不返回一个match对象，而是返回一个字符串串列表，若正则表达式没有分组,返回的是查找到的文本的列表;若分组则返回一个个包含分组元组的列表

		if res != None:
			print('all result is :')
			print(res)
		else:
			print('there is no result')

	except Exception as e:
		print(e)


def find_one(content,regex=r'131\d{8}'):
	group_result(content,regex)

def find_all(content,regex=r'131\d{8}'):
	find_all_result(content,regex)

def find_all_tuple(content,regex=r'(131)(\d{8})'):
	find_all_result(content,regex)

content = 'my No. is : 13167808080,his is 13190908989'

find_one(content)
find_all(content)
find_all_tuple(content)