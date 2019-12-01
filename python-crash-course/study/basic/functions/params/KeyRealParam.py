def getName(name,call):
 """Greeting"""		#文档注释
 print("Hello," + name + ",you are " + call);

name=input("please enter your name:\n")
#关键字实参
getName(call='Hero',name = name)
