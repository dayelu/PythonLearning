def volume(shape,*three):		#此种方式传直将被保存在一个元组里面
	"""return the volume of a cubic shape""" 
	#three[0] = 10		元组元素不可改变,除非覆盖
	#three = (4,4,4,)	多一个逗号,就会使得结果稍有变动,python函数内部机制是咋样的,英吹斯汀
	#three = (4,4,4,10)
	three = (4,4,4)
	info = {
		'shape':shape,
		'volume':three[0]*three[1]*three[2]
		}
	return info

#print("the var info in the funciton is: ")
#print(info)				maybe also have global and tmp var

#print("there is info you need")
#print(volume('cuboid',3,3,3))
