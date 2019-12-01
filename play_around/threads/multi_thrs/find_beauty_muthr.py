import requests,sys,pyperclip,os
from bs4 import BeautifulSoup
from threading import Thread
from time import time


def download(file_dir,filename,pic_url):
	"""下载器"""
	#下载位置
	try:
		file_name = "/pic" + filename
		file = file_dir+ file_name + ".jpg"

		if(os.path.exists(file) == False):
			with open(file,"wb") as f_obj:
				pic = visit_web(pic_url)
				for chunk in pic.iter_content(chunk_size=1024):
					f_obj.write(chunk)

	except Exception as e:
		print(e)


def download_dir(cdown_name):
	"""下载器"""
	#下载位置
	try:
		pic_root = "imgs/"
		file_dir = pic_root + cdown_name
		if(os.path.exists(file_dir) == False):
			os.makedirs(file_dir)

		return file_dir

	except Exception as e:
		print(e)



def multhr(url_start):
	try:

		start_time = time()

		urls_content = download_urls(url_start)
		threads = []

		for url_content in urls_content:		#添加n个图片下载进程

			file_dir = download_dir(url_content['title'])  #创建下载目录文件夹

			t = Thread(target=download,				#传递的是方法名，可以看作变量，不能带引号
				args=(file_dir,url_content['now_page'],url_content['pic_url'])
				)
			threads.append(t)
		
		for thr in threads:
			thr.start()

		for thr in threads:
			thr.join(timeout=60)		#超过60秒停止阻塞，放弃治疗

		end_time = time()
		print("下载耗时："+str(end_time - start_time)+"秒！")
	
	except Exception as e:
		print(e)

def download_urls(url_start):
	'''下载一个主题所需的全部内容'''
	res = []
	try:
		if "http" not in url_start:
			sys.exit("链接错误！")

		urls = seize_content(url_start,type='urls')

		for url in urls:
		#下载图片
			res.append(seize_content(url))
			
		return res

	except Exception as e:
		print(e)



def seize_content(url,type='content'):
	""""获取下载信息"""
	try:
		res = visit_web(url)

		soup = BeautifulSoup(res.text,features="html.parser")

		if type == 'urls':
			scrolls = soup.select(".scroll-img-cont li a")
			res = []
			for scroll in scrolls:
				res.append(scroll.get("href"))

		else:
			res = {}	#定义一个空字典类型
			res['title'] = soup.select(".Bigimg .ptitle h1")[0].getText()
			res['now_page'] = soup.select(".Bigimg .ptitle span")[0].getText()

			if "wallpaper_detail" in url:
				attr = "src"
			else:
				attr = "url"

			res['pic_url'] = soup.select(".pic-meinv .pic-large")[0].get(attr)

		return res
		
	except Exception as e:
		print(e)


def visit_web(url):
	"""网页浏览器"""
	try:
		res = requests.get(url, stream=True)
		res.raise_for_status()

		return res

	except Exception as e:
		print(e)


# url_start = pyperclip.paste()

# multhr(url_start)



