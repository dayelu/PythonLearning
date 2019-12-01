with open('text/pi_digits.txt') as file_object:
    #array_line = file_object.readline()        #从输出结果我们看到这种方法类似与游标

    array_lines = file_object.readlines()
    
    array_line = file_object.readline()

print(array_line)
print(array_lines)

for line in array_lines:
	print(line.rstrip())					#rstrip()方法只能删除尾部指定的字符

str = ''
for line in array_lines:
	str += line.strip()						#strip()方法可以删除头尾空格和空行

print(str)
print(len(str))
print(str[-1])								#字符串和数组一样可以这么用，没想到吧？
print(str[2:7])								#可以把字符串看作包含一个个字符的列表