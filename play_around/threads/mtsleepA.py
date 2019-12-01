import _thread
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
	_thread.start_new_thread(loop0,())
	_thread.start_new_thread(loop1,())
	sleep(6)	#由于没有让主线程等待子线程执行完成再继续执行的代码，主线程会直接终止并退出
	print('结束时间：'+ctime())
main()
