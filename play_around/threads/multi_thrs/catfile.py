import os
# import find_beauty_muthr as fbm
from time import time
from find_beauty_muthr import multhr

from threading import Thread


# print(os.listdir())
start_time = time()

with open("urls.txt","r") as f_obj:
	urls = f_obj.readlines()
# print(urls)
threads = []

for url in urls:
	t = Thread(target=multhr,					#传递的是方法名，可以看作变量，不能带引号
				args=(url.rstrip(),)			#虽然只有一个参数，但是这个逗号却必不可少
				)
	threads.append(t)

for thr in threads:
	thr.start()

for thr in threads:
	thr.join(timeout=60)		#超过60秒停止阻塞，放弃治疗

end_time = time()
#总耗时718.5326063632965秒！
print("总耗时"+str(end_time - start_time)+"秒！")

#合并总耗时总耗时102.13938188552856秒！
#io 同步索的问题未解决，有待大规模提升