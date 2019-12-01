from selenium import webdriver
import time,re
# import webbrowser as web
# help(webdriver)		#查看webdriver支持的浏览器类型

# firefox_path = "/usr/bin/firefox"		#定义火狐浏览器的路径
#注册浏览器类型
# web.register("firefox",None,web.BackgroundBrowser(firefox_path))
#打开特定浏览器
# web.get("firefox").open("https://www.baidu.com",new=0,autoraise=True)     #new:0/1/2 0：同一浏览器窗口打开 1：打开浏览器新的窗口，2：打开浏览器窗口新的tab

def ctrl_chrome(url):
	try:

		browser = webdriver.Chrome()
		browser.get(url)
		time.sleep(5)
		page_source = browser.page_source
		# print(page_source)
		url_list = re.findall('href=\"(.*?)\"',page_source,re.S)

		url_all = []
		for url in url_list:
			if "https" in url:
				# print(url)
				url_all.append(url)
		print(url_all)
		browser.close()

	except Exception as e:
		print(e)
# url = "https://www.baidu.com"
url = "https://blog.csdn.net/mtbaby/article/details/77573443"

ctrl_chrome(url)