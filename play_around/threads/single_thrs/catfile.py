import os
import find_beauty_ex_ex as fbm

from time import time

# print(os.listdir())
start_time = time()

with open("urls.txt","r") as f_obj:
	urls = f_obj.readlines()
# print(urls)

for url in urls:
	fbm.find_beauty(url.rstrip())


end_time = time()
#总耗时963.6505944728851秒！
print("总耗时"+str(end_time - start_time)+"秒！")