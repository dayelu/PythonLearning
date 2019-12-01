import os
os.chdir("../")
dir = os.getcwd()			#当前目录
print(dir)
print(os.listdir(dir))		#os.listdir() 方法返回文件名字字符串的列表

# os.chdir('C:\\windows\\System32')	#改变路径,相当于cd命令
formal_path = os.path.join('usr','bin','spam')
print(formal_path)
os.chdir('/home/')
dir_ch = os.getcwd()
print(dir_ch)
os.makedirs('test_makedirs')
