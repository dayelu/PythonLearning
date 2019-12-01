def words_count(file_name):
	try:

		with open(file_name) as article_object:
			#content = article_object.readlines()				#readlines()用多了,把read()都给忘了
			content = article_object.read()
			content_array = content.split()						#split()通过空格将字符串分割成若干部分，并将这些部分存在一个列表里
			cnt = str(len(content_array))
		#print(str)
		print("这本书有" + cnt + "个字！")

	except FileNotFoundError:
		pass													#不做任何操作
		# print("文件未找到！")


#file_name = "Secrets of Radar.txt"
file_name = "text/divison11111.py"
words_count(file_name)
