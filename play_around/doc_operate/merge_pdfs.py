import re
import os
import sys
from PyPDF2 import PdfFileMerger

def  merge_new(part_name):
	'''
		合并每一小节的 pdf 文档整合成 每章 文档
		根据官方文档提供的 PdfFileMerger 类, 自测耗时 3.3 s
	'''
	try:

		ch_sets = order_by(part_name)

		merge_obj = PdfFileMerger()

		for pdf in ch_sets:
			# with open(pdf,"rb") as pdf_obj:
			# 	merge_obj.append(pdf_obj)		# 这种方法会导致无法读取到页面内容,至于为什么有待研究

			merge_obj.append(open(os.path.join(part_name,pdf),"rb"), pdf[:-len(os.path.splitext(pdf)[1])])

		directory = "chapters"

		if os.path.exists(directory) == False:
			os.mkdir(directory)

		part_file = part_name.split("\\")[1] + ".pdf"

		filepath = os.path.join(directory,part_file)

		if os.path.exists(filepath) == False:

			with open(filepath,"wb") as res:
				merge_obj.write(res)

			print(part_file + "\t合并完成!")

		else:
			print(part_file + "\t文件已存在")

	except Exception as e:
		print(e)


def order_by(part_name):
	'''
		简陋的章节文件重排序方法(使用lambda表达式作为sorted()函数的key的简便写法)
		(居然还有这种操作！！！！)
	'''
	try:

		file_list = os.listdir(part_name)	# 有简单的 ls 方法可以查看当前目录内容就不要用 os.walk()遍历方法了

		arr = sorted(file_list, key=lambda x : int(x.split("讲")[0][1:]))

		return arr

	except Exception as e:
		print(e)


def merge_chpters(root_dir):
	'''
		合并小节成章
	'''
	chapters = os.listdir(root_dir)

	for chapter in chapters:
		merge_new(os.path.join(root_dir,chapter))			# 官方文档指定方法


def  merge_all(root_dir,pdf_name):
	'''
		合并每一小节的 pdf 文档整合成 每章 文档
		（不能根据章排序，有待改进）
		根据官方文档提供的 PdfFileMerger 类, 自测耗时 3.3 s
	'''
	try:

		merge_obj = PdfFileMerger()

		filenames = os.listdir(root_dir)

		for filename in filenames:

			merge_obj.append(open(os.path.join(root_dir,filename),"rb"), filename[:-len(os.path.splitext(filename)[1])])

		pdf_name = pdf_name + ".pdf"

		if os.path.exists(pdf_name) == False:

			with open(pdf_name,"wb") as res:
				merge_obj.write(res)

			print(pdf_name + "\t合并完成!")

		else:
			print(pdf_name + "\t文件已存在")

	except Exception as e:
		print(e)


# root_dir="徐小湛线性代数–课件"
# root_dir="概率论与数理统计-课件"
# merge_chpters(root_dir)

# root_dir="chapters"
# filename = "徐小湛线性代数"
# merge_all(root_dir,filename)


