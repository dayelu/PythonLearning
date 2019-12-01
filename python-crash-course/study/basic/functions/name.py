class  MagicDemo(object):
	"""docstring for  MagicDemo"""
	def __init__(self, *arg):
		self.arg = arg
	
	def __call__(self):
		print(*self.arg)
		print(self.arg)

instant = MagicDemo('a','b','c')
instant()
print(instant.arg)


tup = [1,3,4]
print(*tup)		# * 可以把元组，列表等等类型的数据解析出来
        		# 暂时如此理解，待日后深究

def hello():
	print("hello world!")

if __name__ == "__main__":
	hello()



