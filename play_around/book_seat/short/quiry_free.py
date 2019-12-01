import time
import pymongo
from book import SeatBook
from threading import Thread,Lock

class SeatFree(object):
	"""docstring for SeatFree"""
	def __init__(self):
		super(SeatFree, self).__init__()
		self.sb = SeatBook(log_name="quiry_free")
		
		self.myclient = pymongo.MongoClient("mongodb://XXXXXXXXXXXX:XXXX/")

		self.mydb = self.myclient["seats_free"]
		self.mycol = self.mydb['seats']
		
	def insert_free(self,room_name):
		'''
			非使用状态座位信息入库
		'''
		try:
			
			content = self.sb.spaces_info_real_time(room_name)
			# data = {}		放在外层时，由于一直是同一个对象，所以会存在“_id”重复问题
			for item in content:
				data = {}
				if item['status'] != 6:		# 1 : 空闲 2:已预约	6 : 使用中
					data["area_name"] = item["area_name"]
					data["name"] = item["name"]
					data["status_name"] = item["status_name"]
					data["status"] = item["status"]
					data["time"] = int(time.time())
					
					self.mycol.insert_one(data)


		except Exception as e:
			print(e)


	def quiry_seat(self,func):
		'''
			查询同一时，个自习区域的位置信息
		'''
		try:
			nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			
			if func == self.find_free:
				print("\n查询时间" + nowtime + "\n")
			else:
				print("\n入库时间" + nowtime + "\n")

			start_time = time.time()

			threads = []

			rooms = self.sb.roomno_search()

			for name in rooms.keys():
				
				t = Thread(target=func,
					args=(name,)
					)

				threads.append(t)

			for thr in threads:
				thr.start()

			for thr in threads:
				thr.join(timeout=60)
			
			end_time = time.time()
			
			if func == self.insert_free:
				print("入库完毕，耗时" + str(end_time - start_time) +" s")
			else:
				print("\n查询完毕，耗时" + str(end_time - start_time) +" s.\n")

		except Exception as e:
			print(e)
		finally:
			self.myclient.close()

	def find_free(self,room_name):
		'''
			查询某个自习室的空位置
		'''
		try:
			data = {}
			content = self.sb.spaces_info_real_time(room_name)
			
			for item in content:
				if item['status'] == 1:		# 1 : 空闲 2:已预约	6 : 使用中
					print(room_name + "\t" +item['no'])

		except Exception as e:
			print(e)


def main():

	try:
		stime = time.time()
		t = time.localtime(stime)
		six_thirsty = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 06:30:00', t),'%Y-%m-%d %H:%M:%S')))
		twenty_two = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 22:00:00', t),'%Y-%m-%d %H:%M:%S')))


		if (int(time.time()) > six_thirsty) and int(time.time()) < twenty_two:

			sf = SeatFree()
			sf.quiry_seat(sf.insert_free)
		# sf.quiry_seat(sf.find_free)

	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()
