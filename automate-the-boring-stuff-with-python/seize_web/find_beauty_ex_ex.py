import bs4,requests,os,random,string,sys,pyperclip

#不正规的递归用法，返回值并没有返回来影响结果，后续可有更深入研究
def find_beauty(url_start):
	"""实用但貌似有巨大隐患的野路子"""
	try:
		if "http" not in url_start:
			sys.exit("链接错误！")

		res = seize_content(url_start)
		#下载图片
		download(res['title'],res['now_page'],res['pic_url'])

		if res['now_page'] == res['total_paegs']:
			print("complete!") 
			# return 222222222222222
		else:
			# print("3333333333333333")
			# return "continue"
			find_beauty(res['next_page_url'])
		# return 1000000000
	except Exception as e:
		print(e)


def seize_content(url):
	""""获取下载信息"""
	try:
		res = visit_web(url)

		soup = bs4.BeautifulSoup(res.text,features="html.parser")
		#定义一个空字典类型
		res = {}
		res['title'] = soup.select(".Bigimg .ptitle h1")[0].getText()
		res['now_page'] = soup.select(".Bigimg .ptitle span")[0].getText()
		res['total_paegs'] = soup.select(".Bigimg .ptitle em")[0].getText()

		res['next_page_url'] = soup.select(".pic-meinv a")[0].get("href")

		if "wallpaper_detail" in url:
			attr = "src"
		else:
			attr = "url"

		res['pic_url'] = soup.select(".pic-meinv .pic-large")[0].get(attr)

		return res
		
	except Exception as e:
		print(e)

def download(filepath,filename,pic_url):
	"""下载器"""
	#下载位置
	try:
		# pic_root = "imgs\\"
		pic_root = "imgs/"
		path = pic_root + filepath
		if(os.path.exists(path) == False):
			os.makedirs(path)

		# file = path+"\\pic"+filename+".jpg"
		file = path+"/pic" + filename + ".jpg"
		
		# and os.path.getsize(file)
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

# http://www.win4000.com/wallpaper_detail_149920_2.html
# http://www.win4000.com/meinv162559.html
# url_start = "http://www.win4000.com/wallpaper_detail_151225.html"
# url_start = "http://www.win4000.com/wallpaper_detail_140417.html"
url_start = pyperclip.paste()
result = find_beauty(url_start)
# print(result)

