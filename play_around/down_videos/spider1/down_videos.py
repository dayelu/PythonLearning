from threading import Thread
import bs4,requests,os,random,string,sys


def download(name,url):
	"""下载器"""
	#下载位置
	try:
		# video_root = "videos/"
		# if(os.path.exists(video_root) == False):
		# 	os.makedirs(video_root)

		# key = ''.join(random.sample(string.ascii_letters + string.digits, 8))			#产生8位随机字符串
# 
		# file = video_root+"/"+str(key)+".mp4"
		file = name+".mp4"
		
		if(os.path.exists(file) == False):
			
			with open(file,"wb") as f_obj:
				pic = visit_web(url)
				for chunk in pic.iter_content(100000):
					f_obj.write(chunk)
		print("视频"+ file +"下载成功")

	except Exception as e:
		print(e)

def visit_web(url):
	"""网页浏览器"""
	try:
		res = requests.get(url)
		res.raise_for_status()
		return res

	except Exception as e:
		print(e)



def read_lsit(file):
	'''读取下载文件链接'''
	content = []
	try:
		with open(file,"r") as obj:
			lines = obj.readlines()

		for line in lines:
			content.append(line.rstrip())

		return content

	except Exception as e:
		print(e)


def  multi_task_down(names,urls):
	try:
		
		threads = []
		
		videos_dict = video_dict(names,urls)

		# sys.exit(videos_dict)

		for name,url in videos_dict.items():

			t = Thread(
				target=download,
				args=(name,url)
				)

			threads.append(t)

		for thread in threads:
			thread.start()

		for thread in threads:
			thread.join()

	except Exception as e:
		print(e)



# def  multi_task_down(file):
# 	try:
		
# 		urls = read_lsit(file)

# 		for url in urls:
# 			download(url)

# 	except Exception as e:
# 		print(e)

# multi_task_down("videos.txt")


def del_rs(file):
	lines = []
	with open(file,"r",encoding='UTF-8-sig') as f_obj:
		content = f_obj.readlines()

	with open(file,"w",encoding='UTF-8-sig') as f_obj:
		
		for line in content:
			f_obj.write(line.rstrip())


def video_dict(names,urls):
	i = 0
	videos_dict = {}
	
	with open(names,"r",encoding='UTF-8-sig') as f_obj:
		names_list = f_obj.readlines()

	with open(urls,"r") as f_obj:
		urls_list = f_obj.readlines()

	for name in names_list:
		videos_dict[name.rstrip()] = urls_list[i].rstrip()
		i = i+1

	return videos_dict

multi_task_down("names.txt","videos.txt")

# del_rs("names.txt")