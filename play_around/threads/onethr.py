from time import sleep,ctime

def loop0():
	print('loop0开始时间：'+ctime())
	sleep(4)
	print('loop0执行完成时间；'+ctime())


def loop1():
	print('loop1开始时间：'+ctime())
	sleep(2)
	print('loop1执行完成时间；'+ctime())

def main():
	print('开始时间：'+ctime())
	loop0()
	loop1()
	print('结束时间：'+ctime())
main()
