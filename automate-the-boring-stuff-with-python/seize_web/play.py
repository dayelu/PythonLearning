import bs4,requests

def seize_urls(root_url):
	try:

		soup = drink_soup(root_url)

		urls = soup.select("li.photo-list-padding a")

		# print(len(urls))
		for url in urls:
			full_url = "http://desk.zol.com.cn"+url.get("href")
			bsoup =  drink_soup(full_url)
			surls = bsoup.select(".photo img")
		
		print(surls)
		# print(urls)

	except Exception as e:
		print(e)


def drink_soup(root_url):
	try:
		res = requests.get(root_url)
		res.raise_for_status()
		# res.encoding = 'utf-8';
		soup = bs4.BeautifulSoup(res.text,features="html.parser")

		return soup

	except Exception as e:
		raise e

root_url = "http://desk.zol.com.cn/2880x1800/"

seize_urls(root_url)