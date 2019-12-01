import bs4,requests,os,sys

def find_beauty(url_start,pic_total,filepath):
	urls = []
	
	tail = ".html"
	urls.append(url_start + tail)
	for i in range(pic_total-1):
		urls.append(url_start + "_" +str(i+2) + tail)
	pic_root = "imgs"
	if(os.path.exists(pic_root + filepath) == False):
		os.makedirs(pic_root + filepath)

	key = 0
	for url in urls:
		res = visit_web(url)
		soup = bs4.BeautifulSoup(res.text,features="html.parser")
		src = soup.select(".pic-meinv .pic-large")
		# print(src[0].get("url"))
		key = key + 1

		with open(filepath+"\\pic"+str(key)+".jpg","wb") as f_obj:
			pic_url = src[0].get("url")
			pic = visit_web(pic_url)
			for chunk in pic.iter_content(100000):
				f_obj.write(chunk)


def visit_web(url):
	res = requests.get(url)
	res.raise_for_status()
	return res

url_start = "http://www.win4000.com/mobile_detail_151842"
pic_total = 10
filepath = "suihua"
find_beauty(url_start,pic_total,filepath)
