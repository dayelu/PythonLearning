import requests,bs4,webbrowser,sys

try:

	# key_words = input("请输入关键字：")
	# url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=" + key_words
	# webbrowser.open(url)
	# res = requests.get(url)
	# res.raise_for_status()

	file = "html/res_baidu.html"
	with open(file) as f_obj:
		content = f_obj.read()

	# with open(file,'w') as f_obj:				#这种方法百度无法通过链接下载完整的网页！！！
	# 	content = res.text
	# 	f_obj.write(content)

	b_baidu = bs4.BeautifulSoup(content,"lxml")		#,"lxml"
	select = b_baidu.select("h3.t a")

	hrefs = []
	for item in select:
		href = item.get("href")
		hrefs.append(href)
	
	for href in hrefs:
		webbrowser.open(href)
	

except Exception as e:
	print(e)


