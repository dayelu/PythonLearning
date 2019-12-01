import os,webbrowser
# os.system('ipconfig')
# os.system("C:")																#os.system("#COMMAND#")		相当与输入shell命令
# os.popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")	#os.popen("")	功能与上功能类似，不同的时os.popen()方法的返回值就是命令执行后的结果


# webbrowser.open("http://www.baidu.com")
# os.system("dir")	

sys_res = os.system("ls")						#os.system()只要执行就会立即在控制台返回结果，可以用于执行，不适于需要条件判断的程序中    
popen_res = os.popen("ls")


print('system()方法输出'+str(sys_res))

print("popen()方法输出",end="")
print(popen_res.readlines())

print("当前所在目录："+os.getcwd())

# print("返回上一级目录："+os.chdir("/home/"))
# print(os.chdir("../hhhhhhhh"))			os.chdir() 方法执行成功后没有返回值或者返回值为空，如果执行失败，即进入不存在的目录就会报错
print(os.chdir("../") == None)

print("返回上一级目录：")

os.chdir("../")

print("当前所在目录："+os.getcwd())


#现时所用文件操作不多，暂不深究，他日有心------>
#python文件操作的具体其他十分有用的方法详见os库。。。。。