

def digui(length):
	if length == 1:
		return 1
	else:
		return length + digui(length-1)


print(digui(10))
