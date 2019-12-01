import name

class Construc():
	def __init__(self,name):
		self.name = name

	def __call__(self):
		print(self.name)

obj =  Construc("wang")
fname = obj()
print(obj.name)

obj1 =  Construc("张")
f_namr = obj1.__call__()
print(obj1.name)



def test():
	print("今天天气好晴朗")

fobj = test

print(type(fobj.__name__))