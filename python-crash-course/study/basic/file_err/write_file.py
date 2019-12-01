with open('text/newfile.txt','w') as file_object:			#打开一个不存在的文件会自动新建这个文件
	file_object.write('wo qi shi hen ai ni')
	#array_list = file_object.readlines()				#open方法写模式（'w')立的文件对象只有写的权限


with open('text/newfile.txt') as new_file_object:			#似乎open())方法默认的方法就是读方法('r')
	content = new_file_object.readlines()

for line in content:
	print(line.strip())

with open('text/newfile.txt','a') as add_object:				#附加模式('a')，在已有内容后添加新的内容
	add_object.write('\n我可能很爱自己！么么哒。。。')
 