try:
	
	with open("text/test_files.txt") as f_obj:
		f_obj.readline()

except FileNotFoundError:
	print("文件不存在！")
	

