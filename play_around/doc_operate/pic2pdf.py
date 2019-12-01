import os
import sys
from fpdf import FPDF
from threading import Thread, Lock


lock = Lock()

def collect_chapter(chapter_name,part_name):
	'''
		由于不图片格式校验时出现的不明原因，用文件遍历的方式好像不行，所有单独列出
	'''
	try:		
		file_dir = "pdfs/"
		pdf = FPDF('P','cm', (20,15))

		re_path = ''
		# for current_folder,sub_folders,filenames in os.walk(part_name + "/" + chapter_name + "/"):
		for current_folder,sub_folders,filenames in os.walk(os.path.join(part_name,chapter_name)):	# 不要再用这种 平台不兼容 而且很丑陋的方式

			for filename in filenames:
				img = os.path.join(current_folder,filename)
				pdf.add_page()
				pdf.image(img,(20-16.93)/2, (15-12.7)/2)

			with lock:

				if(os.path.exists(file_dir) == False):
					os.makedirs(file_dir)

				re_path = file_dir + part_name.split('\\')[1]		# on Windows
				# re_path = file_dir + part_name.split('/')[1]		# on Linux， don't recognise the double slash  ('//') 

				if(os.path.exists(re_path) == False):
					os.makedirs(re_path)

		# pdf.output(re_path + "/" + chapter_name + ".pdf", "F")		# 不要再用这种 平台不兼容 而且很丑陋的方式
		pdf.output(os.path.join(re_path, chapter_name + ".pdf"), "F")

		print(chapter_name + "\t整合完成！")

	except Exception as e:
		print(e)

def down_part(part_name="."):
	
	try:
		threads = []
		chapters = []

		for current_folder,sub_folders,filenames in os.walk(part_name):
			# print(sub_folders)
			# chapters = sub_folders[:]			# 即使时保存列表的副本，在被保存的列表被释放后，副本也会被释放，可以推测副本引用是原列表的指针副本
			for sub_folder in sub_folders:
				chapters.append(sub_folder)

		for chapter in chapters:

			# collect_chapter(chapter,part_name)		# 

			t = Thread(
						target=collect_chapter,
						args=(chapter, part_name)
						)

			threads.append(t)

		for thread in threads:
			thread.start()

		for thread in threads:
			thread.join()

	except Exception as e:
		print(e)


def get_parts(root_dir="imgs"):

	try:
		parts = []

		for current_folder,sub_folders,filenames in os.walk(root_dir):

			return sub_folders

	except Exception as e:
		print(e)

def parts_down(root_dir="imgs"):

	try:

		parts = get_parts(root_dir)

		for part in parts:

			part = os.path.join(root_dir,part)

			down_part(part)

	except Exception as e:
		print(e)

parts_down()