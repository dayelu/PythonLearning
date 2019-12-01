def modify(info):
	"""modify some information"""
	info[1] = 160
	return info

info = [100,180]
#print("before modified ，the information is :" + info)		print()函数似乎只能打印同一类型的数据
print("before modified ，the information is: ")
print(info)

modifiedInfo = modify(info)

print("after modified ，the information is : " )
print(info)

print("if we input a backup,before modified it\'s : ")
message = [100,200,300]
print(message)
print("after")
mess = modify(message[:])
print(message)

