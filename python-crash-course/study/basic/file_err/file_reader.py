with open('text/pi_digits.txt') as file_object:  #使用with关键字可以使得文件在不需要访问的时候将其关闭，此举可以避免使用close()
	contents = file_object.read()       #read()到达文件末尾时会返回一个空字符 ，输出是会显示换行的效果
#	print(contents)                     #使用此方式输出会多一个空行
	print(contents.rstrip())	    #使用.rstrip()去除空行

