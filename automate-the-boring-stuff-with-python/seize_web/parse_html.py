import requests,bs4,pyperclip

try:
	# url = pyperclip.paste()
	# res = requests.get(url)
	# res.res_for_status()
	# parse = bs4.BeautifulSoup(res.text)
	text = "html/read_file3.html"
	with open(text) as txt_obj:
		parse = bs4.BeautifulSoup(txt_obj.read(),"lxml")				#或者直接解析本地html文件

	pElems = parse.select('h1')
	elem1 = str(pElems[0])
	print(elem1)
	p_elem1 = pElems[0].getText()			#读取标签之内文本信息
	# p_elem1 = pElems[0].attrs
	# p_elem1 = pElems[0].get("src")
	print(p_elem1)

except Exception as e:
	print(e)