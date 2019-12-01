import bs4,requests,os,random,string,sys,pyperclip

def download(filepath,filename,pic_url):
	"""下载器"""
	#下载位置
	try:
		pic_root = "imgs/"
		path = pic_root + filepath
		if(os.path.exists(path) == False):
			os.makedirs(path)

		file = path+"/pic" + filename + ".jpg"
		
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



def seize_content_bak(url):
	""""获取下载信息"""
	try:
		res = visit_web(url)

		soup = bs4.BeautifulSoup(res.text,features="html.parser")

		video_list = soup.select(".zj_list_ont dd a")

		for asign in video_list:
			# print(asign.get("href"))
			print(asign.get("title") + "\t")
		return res
		
	except Exception as e:
		print(e)

url = "http://exam.cabplink.com/class/play.aspx?lid=4388"

seize_content_bak(url)



# url_start = pyperclip.paste()

# result = find_beauty(url_start)

