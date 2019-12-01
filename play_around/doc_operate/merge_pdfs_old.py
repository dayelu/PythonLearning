# import PyPDF2
import re
import os
import sys
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader, PdfFileWriter



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

		part_file = part_name.split("\\")[1] + ".pdf"

		if os.path.exists(part_file) == False:

			with open(part_file,"wb") as res:
				merge_obj.write(res)

			print(part_file + "\t合并完成!")

		else:
			print(part_file + "\t文件已存在")

	except Exception as e:
		print(e)


def merge_pdfs(part_name):
	'''
		合并每一小节的 pdf 文档整合成 每章 文档
		自己写的合并方法,调用了下面自己写的一个合并两个文档的方法
		不带书签,自测耗时 11.8 s
	'''
	try:

		count = 1
		ch_sets = order_by(part_name)
		
		current_folder = os.path.dirname(__file__)
		new_name = os.path.join(current_folder, part_name.split("\\")[1] + '.pdf') # "\\" on windows, "/" on Linux

		if os.path.exists(new_name) == False:		# 这样的循环嵌套的和条件判断我内心是拒绝的，但是 达到目的是第一位

			for ch_set in ch_sets:

				if count == 1:
					merge_two_pdf( os.path.join(part_name, ch_sets[0]), os.path.join(part_name, ch_sets[1]), 'tmp' + str(count))

				elif count > 1 and count < len(ch_sets):		# 注意列表的下标总是从 0 开始
					merge_two_pdf('tmp' + str(count-1) + '.pdf', os.path.join(part_name, ch_sets[count]), 'tmp' + str(count))

					if os.path.exists('tmp' + str(count-1) + '.pdf'):
						os.remove('tmp' + str(count-1) + '.pdf')
					else:
						print("要删除的文件不存在！")

				count = count + 1

			old_name = os.path.join(current_folder, 'tmp' + str(count-2) + '.pdf')

			if os.path.exists(new_name) == False:
				os.rename(old_name,new_name)

			print(part_name.split("\\")[1] + "\t合并成功!")
		
		else:
			print(part_name.split("\\")[1] + "\t文件已存在！")

		return part_name

	except Exception as e:
		print(e)


def merge_two_pdf(pdf1,pdf2,part_name):
	'''
		自己从 书本看的照抄的 合并文件的方法
	'''
	try:

		pdf1FileObj = open(pdf1, "rb")
		pdf2FileObj = open(pdf2, "rb")

		pdf1Reader = PdfFileReader(pdf1FileObj)
		pdf2Reader = PdfFileReader(pdf2FileObj)

		pdfWriter = PdfFileWriter()

		for pageNum in range(pdf1Reader.numPages):
			pageObj = pdf1Reader.getPage(pageNum)
			pdfWriter.addPage(pageObj)

		for pageNum in range(pdf2Reader.numPages):
			pageObj = pdf2Reader.getPage(pageNum)
			pdfWriter.addPage(pageObj)

		# if os.path.exists(part_name + ".pdf") == False:
		pdfOutputFileObj = open(part_name + ".pdf","wb")
		pdfWriter.write(pdfOutputFileObj)
		
		pdfOutputFileObj.close()

		pdf1FileObj.close()
		pdf2FileObj.close()

		return part_name + ".pdf"

	except Exception as e:
		print(e)

def find_title(ch_no,chapters):
	'''
		简单粗暴地返回章节名的方法
	'''
	try:

		for chapter in chapters:

			if str(ch_no) in chapter:
				return chapter
		return False

	except Exception as e:
		print(e)


def order_by(part_name):
	'''
		简陋的章节文件重排序方法
	'''
	try:
		ch_no = 0

		ch_sets = []

		filenames = []

		sorted_chsets = []

		for current_folder,sub_folders,filenames in os.walk(part_name):

			for filename in filenames:

				# if re.search(r'\d+\.\d+',filename):

				sp_filename = filename.split(" ")

				ch_no = sp_filename[0].split('.')[0]

				ch_sets.append(int(sp_filename[0].split('.')[1]))

			ch_sets.sort()

		# 生成器方法，无需返回值只有在被循环调用的时候才会逐个去取，
		# 在数据量大的时候非常有用,
		# 但是由于知识和想象力的限制,暂时用不上

		# for ch_set in ch_sets:	
		# 	yield find_title(str(ch_no) + '.' + str(ch_set),filenames)

		for ch_set in ch_sets:
			sorted_chsets.append(find_title(str(ch_no) + '.' + str(ch_set),filenames))

		return sorted_chsets



	except Exception as e:
		print(e)


def get_chapters(root_dir):
	'''
		简单的文件遍历方法,从一个给定的目录重获取 文件夹名
	'''
	try:
		relative_sub_folders = []
		for current_folder,sub_folders,filenames in os.walk(root_dir):
			# print(current_folder)
			for sub_folder in sub_folders:
				# print(sub_folder)
				relative_sub_folders.append(os.path.join(current_folder, sub_folder))
		
		return relative_sub_folders	

	except Exception as e:
		print(e)



def merge_chpter(root_dir):
	'''
		合并小节成章
	'''
	chapters = get_chapters(root_dir)

	for chapter in chapters:
		merge_new(chapter)			# 官方文档指定方法
		# merge_pdfs(chapter)		# 自写蹩脚方法


def  merge_all(root_dir):
	'''
		合并每一小节的 pdf 文档整合成 每章 文档
		根据官方文档提供的 PdfFileMerger 类, 自测耗时 3.3 s
	'''
	try:

		merge_obj = PdfFileMerger()

		for current_folder,sub_folders,filenames in os.walk(root_dir):

			for filename in filenames:

				merge_obj.append(open(os.path.join(root_dir,filename),"rb"), filename[:-len(os.path.splitext(filename)[1])])

		filename = "final" + ".pdf"

		if os.path.exists(filename) == False:

			with open(filename,"wb") as res:
				merge_obj.write(res)

			print(filename + "\t合并完成!")

		else:
			print(filename + "\t文件已存在")

	except Exception as e:
		print(e)


root_dir="chapters"
# merge_chpter(root_dir)
merge_all(root_dir)
