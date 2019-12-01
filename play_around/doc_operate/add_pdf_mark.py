#首先通过 pip 安装 pypdf2 和 pdfbookmarker
#然后通过命令行或者python os 驱动程序运行
import os
import re


def offset_page(file,offset,stdfile):
	"""
		针对中国古籍没有阿拉伯数字只有中国汉字的目录标题的特殊情况
	"""
	divisions = []
	pages = []
	count = 0
	try:
		with open(file,"r") as r_file:
			marks = r_file.readlines()
		# 根据分隔符把目录名和页码分割成两个数组
		for mark in marks:
			divisions.append(mark.split("|"))

		# 调整实际页码
		for div in divisions:
			#添加调整目录分级符,默认起始位都为一级
			puls_count = '+'

			div[0] = puls_count + div[0] 

			pages.append(int(div[1].rstrip())+offset)
		#替换原页码
		for page in pages:
			divisions[count][1] = "|" + str(page) + "\n"
			count = count + 1



		#生成标准文件
		if os.path.exists(stdfile):
			os.remove(stdfile)

		a_obj = open(stdfile,"a")

		for div in divisions:
			a_obj.write(div[0]+div[1])

		a_obj.close()

		'''异常处理及程序优化日后改进'''
		return 'new_content.txt'

	except Exception as e:
		print(e)

def modify_page(file,offset,stdfile):
	'''
		根据偏移量修改实际页码(针对一般目录章节标题形如　１.1.1　的情景)
		以下函数　math_title_no() ，count_dot()　为关联函数
	'''
	divisions = []
	pages = []
	count = 0
	try:
		with open(file,"r",encoding='utf-8') as r_file:
			marks = r_file.readlines()
		# 根据分隔符把目录名和页码分割成两个数组
		for mark in marks:
			divisions.append(mark.split("\"|"))

		# 调整实际页码
		for div in divisions:
			#添加调整目录分级符,默认起始位都为一级
			puls_count = '+'

			title_no = math_title_no(div[0])

			dot_count = count_dot(title_no)

			for i in range(0,dot_count):	#用count()函数统计字符在字符串中出现的次数
				puls_count += '+'
			div[0] = puls_count + div[0] 

			pages.append(int(div[1].rstrip())+offset)
		#替换原页码
		for page in pages:
			divisions[count][1] = "\"|" + str(page) + "\n"
			count = count + 1
		#生成标准文件
		if os.path.exists(stdfile):
			os.remove(stdfile)

		a_obj = open(stdfile,"a",encoding='utf-8')

		for div in divisions:
			a_obj.write(div[0]+div[1])

		a_obj.close()
		
		'''异常处理及程序优化日后改进'''
		return 'new_content.txt'

	except Exception as e:
		print(e)

def math_title_no(str):
	''' 
		获得标题序号
	'''
	try:
		# res = re.match(r'(\d.*)+',str)	# 符号 " . " 代表任意字符
		res = re.match(r'"(\d+\.*)+',str)
		if res:
			return res.group()
		else:
			return None;

	except Exception as e:
		print(e)


def count_dot(title_no):
	''' 
		通过标题序号的特点，如 1.1.1 ，首先统计其标点的个数 
	'''
	try:
		if title_no:
			dot_count = title_no.count(".")
		else:
			dot_count = 0
		return dot_count

	except Exception as e:
		print(e)


def add_mark(filename,content_file):
	'''
		调用命令行参数(未使用)
	'''
	try:
		res = os.popen('pdfbm' + filename + content_file)
		print(res)
	except Exception as e:
		print(e)


# file = 'new_js.txt'
# offset = 21
# stdfile = 'new_content.txt'
# modify_page(file,offset,stdfile)

