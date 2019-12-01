import webbrowser,sys,pyperclip,requests
# url = "https://www.baidu.com"
url = pyperclip.paste()

# print(url)
# sys.exit()
						#requests.get()方法下载一个网页
# if res.status_code == requests.codes.ok:		#ok表示状态码200，请求成功
try:
	res = requests.get(url)	
	res.raise_for_status()						#raise_for_status()方法在下载文件出错时会抛出异常
	file = 'html/read_file3.html'
	# with open(file,'wb') as f_obj:				#保存Unicode编码格式
		# for chunk in res.iter_content():
			# f_obj.write(chunk)
			
	with open(file,'w') as f_obj:				#效果看起来一样，但是非二进制写入，可能会有乱码问题
		text_content = res.text
		f_obj.write(text_content)
	# text_content = res.text
	# length = len(text_content)
	# print(length)
	# print(text_content[100:600])
except Exception as e:
	print(e)



# webbrowser.open(url)
