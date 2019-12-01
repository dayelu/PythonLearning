import _thread
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec,lock):
	print('loop'+str(nloop)+'开始时间：'+ctime())
	sleep(nsec)
	print('loop'+str(nloop)+'执行完成时间；'+ctime())
	lock.release()

def main():
	print('开始时间：'+ctime())
	locks = []
	nloops = range(len(loops))

	for i in nloops:
		lock = _thread.allocate_lock()
		lock.acquire()
		locks.append(lock)
	
	for i in nloops:
		_thread.start_new_thread(loop,(i,loops[i],locks[i]))
	
	for i in nloops:
		while locks[i].locked():
			pass
	print('结束时间：'+ctime())
main()
