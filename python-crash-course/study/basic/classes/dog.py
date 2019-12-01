class Dog():
#class Dog(object):		#据说这是python2编写一个类的方法,但是我试过,好像不行
 def __init__(self,name,age):	#可以理解为python的构造函数，每次实例化类时都会运行
  """"""
  self.name=name		#传入的形参储存为属性的值
  self.age=age
  self.weight=10		#为属性weight赋初始值 
  print(self)
 def run(self):
  """my dog can run fast"""
  print(self.name.title()+" can run fast! ")
#mydog=Dog("little CAT","3")
mydog=Dog("little CAT",3)
print("My dog's name is "+mydog.name.title()+".") 
#print("My dog's age is "+mydog.age+".")
print("My dog's age is "+str(mydog.age)+".")
print("My dog's weight is "+str(mydog.weight));
mydog.weight=12			#修改属性值
print("after two months my dog's weight is "+str(mydog.weight));
mydog.run()
