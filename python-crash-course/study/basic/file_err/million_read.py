with open("text/pi_million_digits.txt") as file_object:
	array_lines = file_object.readlines()

str = ''
for line in array_lines:
	#print(line.rstrip())
	str += line.strip() 

print(str[2:59])
#print(str)
print(len(str))