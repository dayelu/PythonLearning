import re

def regex_steps(content):
	"""正则表达式的一般步骤"""
	try:
		#phoneNumRgex = re.compile(r'\d{3}-\d{3}-\d{4}')
		# phoneNumRgex = re.compile('\\d{3}-\\d{3}-\\d{4}')		#在正则表达式前加上一个小写的 r 可以将该字符串标记为原始字符（转义符除外）,而不用这种使用使用双斜杠转义字符将斜杠的办法
		phoneNumRgex = re.compile(r'\*\?\+')		#三大符号的匹配要使用转义字符
		mo = phoneNumRgex.search(content)	#regex对象的seach()方法查找传入的字符串，如果找到了将返回一个Match对象.没找到将返回None
		print('phone number found :' + mo.group())

	except Exception as e:
		print(e)

def regex_gruop(content):
	try:
		# phoneNumRgex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')	#使用括号来进行分组
		phoneNumRgex = re.compile(r'\(\d{3}\)-(\d{3})-(\d{4})')	#如果需要搜索带括号的字符串，则需使用转义字符将扩号转义
		mo = phoneNumRgex.search(content)
		if mo != None:
			# print('the find result is :' + mo.group(3))				#group()方法不带参数则返回所有分组，带参数表示需要返回的第几个分组，如例表示第三个分组
			print('the find result is :' + mo.group())
			middle,tail = mo.groups()		#敲黑板，多重复值，没见过吧
			print(mo.groups())										#groups()方法一次性返回所有 |分组|
		else:
			print("There is no result")
	except Exception as e:
		print(e)


def grep_match(content):
	"""管道（ | ）匹配"""
	try:
		stringRegex = re.compile(r'dayelu is a (shuai|good|handsome)')	#指定前缀，查找多个模式之一
		match = stringRegex.search(content)
		if match != None:
			print('The find result is :'+ match.group())		#只会返第一次出现的匹配文本
		else:
			print('There is no result.')
	except Exception as e:
		# raise e 		#可以定位错误行时使用
		print(e)
	

def match_many_times(content):
	"""零次一次多次匹配三大符号"""
	try:
		stringRegex = re.compile(r'(3)*(2)?(0)+')		
		#1.表示三个符号 【之前】 出现的次数
		#2.在需要搜索的字符串串中找这三个 【连续】字符串串的结果
		match = stringRegex.search(content)

		if(match != None):
			print('result is:' + match.group())
			# print(match.groups())
		else:
			print('There is no result.')

	except Exception as e:
		# raise e
		print(e)

# content  = 'My number is 415-333-2324'
# contents  = 'My number is (415)-333-2324'
# content = 'dayelu is a handsome man , that\'s true'
content = '*?+'
# numbers = ['6666666660','3333333222000','333333300000000','333333320000','333333321']		#还有，正则匹配似乎只限于字符串匹配

regex_steps(content)
# regex_gruop(contents)
# grep_match(content)
# for number in numbers:
# 	match_many_times(number)




