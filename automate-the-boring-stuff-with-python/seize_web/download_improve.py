import requests,sys,random,string

def carryout():
	try:

		with open("video_urls_unique.txt","r") as f_obj:

			lines = f_obj.readlines()


		for line in lines:
			url = line.rstrip()
			download(url)


	except Exception as e:
		print(e)



def download(url):
	try:

		key = ''.join(random.sample(string.ascii_letters + string.digits, 8))

		filename = "videos/" + str(key) + ".mp4"

		video =  visit_web(url)

		with  open(filename,"wb") as f_obj:

				for chunk in video.iter_content(100000):

					f_obj.write(chunk)


	except Exception as e:
		print(e)



def visit_web(url):
	"""网页浏览器"""
	try:
		# url = "http://www.baidu.com"
		res = requests.get(url)
		# res.raise_for_status()		#自带报错效果
		# print(res.status_code)
		if res.status_code == 200:
			
			return res
		else:

			sys.exit("访问失败!")			#只要有一个失败就停止下载

	except Exception as e:
		print(e)


carryout()