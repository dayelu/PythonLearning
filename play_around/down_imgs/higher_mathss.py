import os
import sys
import requests
from bs4 import BeautifulSoup
from threading import Thread, Lock

lock = Lock()

def get_chapters(url):

	try:
		response = requests.get(url)
		soup = BeautifulSoup(response.text,features="html.parser")

		inital_content = soup.select('a[href]')		# 筛选所有 带有 href 属性的 a 标签

		for item in inital_content:

			if 'http://xuxzmail.blog.163.com/blog/static/' in item.get("href"):
				print(item.get("href"))

			# 比较无奈的做法，首先打印出相似的链接，然后手动筛选，并将最后结果保存到 chapters.txt 文件中


	except Exception as e:
		print(e)


def put_all_chapters(chapterfile):
	
	try:
		threads = []

		with open(chapterfile,"r") as f_obj:
			chapter_urls = f_obj.readlines()

		for chapter_url in chapter_urls:

			# get_ppts(chapter_url.strip())		# 循环顺序执行，用于排错调试

			t = Thread(
						target=get_ppts,
						args=(chapter_url.strip(),)
				)

			threads.append(t)


		for thread in threads:
			thread.start() 

		for thread in threads:
			thread.join(timeout=60)

	except Exception as e:
		print(e)


def get_ppts(chapter_url):

	try:
		i = 1
		
		threads = []
		
		response = requests.get(chapter_url)
		soup = BeautifulSoup(response.text,features="html.parser")
		
		ppts = soup.select('.m-3 .nbw-blog img')
		
		if ppts == []:	# 极个别特例，能在浏览器查找，但是却不能获取内容，前端知识不牢，暂不研究
			ppts = soup.select('img[alt="10.1 对弧长的曲线积分 - Calculus - 高等数学"]')

		chapter_name = soup.select('.m-3 .nbw-ryt .left .nbw-bitm .title .tcnt')[0].getText()

		for ppt in ppts:

			filename = chapter_name + str(i)
		
			# print(ppt.get('src'))
			# download(chapter_name,filename,ppt.get('src'))	# 循环顺序执行，用于排错调试

			t = Thread(
						target=download,
						args=(chapter_name,filename,ppt.get('src'))
						)

			threads.append(t)

			i = i + 1

		for thr in threads:
			thr.start()

		for thr in threads:
			thr.join(timeout=60)		#超过60秒停止阻塞，放弃治疗

		print(chapter_name + '\t下载完成')

	except Exception as e:
		print(e)


def download(filepath,filename,pic_url):
	"""下载器"""
	#下载位置
	try:
		pic_root = "imgs/"
		path = pic_root + filepath
		with lock:
			if(os.path.exists(path) == False):
				os.makedirs(path)

		suffix = pic_url.split('.')[-1]

		file = os.path.join(path, (filename + '.' +suffix))

		if(os.path.exists(file) == False):

			with open(file,"wb") as f_obj:
				pic = requests.get(pic_url)
				for chunk in pic.iter_content(100000):
					f_obj.write(chunk)

	except Exception as e:
		print(e)
	

# url = "http://xuxzmail.blog.163.com/blog/static/2513191620073297190462/"
# url = "http://xuxzmail.blog.163.com/blog/static/25131916200732971633378/"
# get_ppts(url)

chapterfile = "chapters.txt"
put_all_chapters(chapterfile)