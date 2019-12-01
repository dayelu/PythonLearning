import re
import os

def strmodify(str_line):
	'''
		整理文件的每一行文本内容
	'''
	try:
		str_line = '"' + str_line
		regex = r'\.\.+'
		# res = re.search(regex, str_line).group()
		# return str_line.replace(res, '"|')
		res = re.sub(regex, '"|',str_line)
		return res
	except Exception as e:
		 print(e)


def read_text(filename):
	'''
		将整理好的每一行文本内容添加进一个数组并返回
	'''
	try:
		# f_obj = open(filename, "r",encoding='UTF-8')
		# line = f_obj.readline()
		# print(line)
		# if line:
		# 	print(strmodify(line),end='')

		# while line:
		# 	line = f_obj.readline()
		# 	codes
		# 	print(strmodify(line),end='')
		final_lines = []
		with open(filename, "r", encoding='UTF-8') as f_obj:
			lines = f_obj.readlines()
		
		for line in lines:
			final_lines.append(strmodify(line))
			# print(strmodify(line), end='')
		# print(final_lines)

		return final_lines

	except Exception as e:
		print(e)
	# finally:
	# 	f_obj.close()

def write_text(filename,lines):
	'''
		将修改的内容写入新文本文件中
	'''
	try:

		# with open(filename, "a") as f_obj: 
		# 	f_obj.write(line)
		if os.path.exists(filename):	#因为是附加模式，所以在写入之前需要把以前生成的目录文件删除重写
			os.remove(filename)
		f_obj = open(filename, "a", encoding='UTF-8')		#读写乱码问题，通过添加关键字参数"encoding='UTF-8' ",可以解决目前所遇到的所有类似问题

		for line in lines:
			f_obj.write(line)
		f_obj.close()

		print("write done")

	except Exception as e:
		print(e)
		

str_line = '1.4.5 操作系统与用户之间的接口.................22'
print(strmodify(str_line))

# filename = 'test.txt'
# lines = read_text(filename)
# newfilename = 'contents.txt'
# write_text(newfilename,lines)