#python2支持的raw_input()等同于python3中的input方法，把输入的内容当作字符串处理

#message = raw_input("Tell me something, and I will repeat it back to you: ")
#print(message)
msg = input("please input your name\n")
print(msg)
#age = input('please input your age\n')	返回的是字符串
age = input("please input your age\n")

if int(age) <= 18:	#将类型转换成整数型，否则报错
 print('小屁孩！')
else:
 print('这么大了一点事都不懂')
