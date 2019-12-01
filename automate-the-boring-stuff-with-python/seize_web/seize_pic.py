import bs4,requests,sys


def list_page(url,selector,prefix = "http://desk.zol.com.cn",aim_attr = "href"):
	try:

		res = requests.get(url)
		res.raise_for_status()
		content = res.text

		bs_obj = bs4.BeautifulSoup(content)
		selects = bs_obj.select(selector)
		# print(selector)
		# print(str(len(selects)))
		# sys.exit()
		hrefs = []
		if len(selects) > 1:
			for select in selects:
				href = prefix + select.get(aim_attr)
				hrefs.append(href)
		else:
			# print(selects)
			# sys.exit()
			hrefs = selects[0].get(aim_attr)	
		return hrefs
	except Exception as e:
		print(e)
url = "http://desk.zol.com.cn/pc/"
selector = ".pic-list2 .pic"
prefix = "http://desk.zol.com.cn"
aim_attr = "href"
view_urls = list_page(url,selector)
# print(view_urls)
#selector = ".photo img"


def single_page(urls,selector,prefix = "",aim_attr = "src"):
	try:
		hrefs = []
		
		for url in urls:
			href = list_page(url,selector,prefix,aim_attr)
			hrefs.append(href)

		return hrefs

	except Exception as e:
		print(e)

# view_urls = ['http://desk.zol.com.cn/bizhi/7326_90505_2.html', 'http://desk.zol.com.cn/bizhi/7325_90496_2.html', 'http://desk.zol.com.cn/bizhi/7324_90487_2.html', 'http://desk.zol.com.cn/bizhi/7323_90478_2.html', 'http://desk.zol.com.cn/bizhi/7322_90469_2.html', 'http://desk.zol.com.cn/bizhi/7321_90460_2.html', 'http://desk.zol.com.cn/bizhi/7320_90451_2.html', 'http://desk.zol.com.cn/bizhi/7314_90405_2.html', 'http://desk.zol.com.cn/bizhi/7319_90449_2.html', 'http://desk.zol.com.cn/bizhi/7318_90434_2.html', 'http://desk.zol.com.cn/bizhi/7317_90425_2.html', 'http://desk.zol.com.cn/bizhi/7316_90416_2.html', 'http://desk.zol.com.cn/bizhi/7315_90407_2.html', 'http://desk.zol.com.cn/bizhi/7307_90340_2.html', 'http://desk.zol.com.cn/bizhi/7301_90294_2.html', 'http://desk.zol.com.cn/bizhi/6849_85484_2.html', 'http://desk.zol.com.cn/bizhi/6840_85423_2.html', 'http://desk.zol.com.cn/bizhi/6829_85300_2.html']
selector = "#bigImg"
img_urls = single_page(view_urls,selector)
# print(img_urls)

def imgs_down(urls,file_path):
	try:
		with open(file_path,"wb") as f_obj:
			for url in urls:
				f_obj.write(url)
	except Exception as e:
		print(e)

file_path = "F:/stuy_use/pic_download"
imgs_down(img_urls,file_path)