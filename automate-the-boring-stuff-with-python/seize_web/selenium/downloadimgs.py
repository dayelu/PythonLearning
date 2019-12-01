import requests,bs4,time
from selenium import webdriver

browser = webdriver.Firefox()

try:
	browser.get("http://pvp.qq.com/web201605/wallpaper.shtml")

	next_page = browser.find_element_by_class_name("downpage")
	totalpage = browser.find_element_by_class_name("totalpage")

	content = browser.find_element_by_id("Work_List_Container_267733")

	next_page.click()


	print(content.text)

except Exception as e:
	print(e)
finally:
	browser.close()