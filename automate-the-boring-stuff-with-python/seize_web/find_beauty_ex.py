import bs4,requests,os,random,string,sys

def find_beauty(url_start,pic_total,filepath):
	
	try:

		tail = ".html"
		url = url_start + tail

		pic_url = seize(url)
		download(filepath,pic_url)

		for i in range(pic_total-1):
			
			url = url_start + "_" +str(i+2) + tail

			pic_url = seize(url)

			download(filepath,pic_url)

	except Exception as e:
		print(e)


def seize(url):
	"""抓取下载链接"""
	try:
		res = visit_web(url)
		soup = bs4.BeautifulSoup(res.text,features="html.parser")
		src = soup.select(".pic-meinv .pic-large")
		pic_url = src[0].get("src")
		
		return pic_url

	except Exception as e:
		print(e)


def download(filepath,pic_url):
	"""下载器"""
	#下载位置
	try:
		# pic_root = "imgs\\"
		pic_root = "imgs/"
		path = pic_root + filepath
		if(os.path.exists(path) == False):
			os.makedirs(path)

		key = ''.join(random.sample(string.ascii_letters + string.digits, 8))			#产生8位随机字符串

		# file = path+"\\pic"+str(key)+".jpg"
		file = path+"/pic"+str(key)+".jpg"
		
		if(os.path.exists(file) == False):
			
			with open(file,"wb") as f_obj:
				pic = visit_web(pic_url)
				for chunk in pic.iter_content(100000):
					f_obj.write(chunk)


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


url_start = "http://www.win4000.com/mobile_detail_136118"
pic_total = 14
filepath = "beauty"

find_beauty(url_start,pic_total,filepath)
