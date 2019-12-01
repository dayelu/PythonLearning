import os
import re
import sys
import time
import json
import logging
import hashlib
import requests
from threading import Thread, Lock
from requests.adapters import HTTPAdapter

class SeatBook(object):
	"""

	"""
def __init__(self,username='XXXXXXXXXXXX',password='XXXXXXXXXXXX',room_name='负1楼4自习室',seat_nos=[34, 35, 36, 32]):
		'''
			初始化常用的类变量，避免频繁调用和新建函数参数
		'''
		self.ip_addr = "XXXXXXXXXXXX"
		self.username = username
		self.password = password
		self.room_name =  room_name
		self.seat_nos = seat_nos
		self.lock = Lock()

		self.apis_json = "apis_json"
		
		self.logs_dir = "logs"
		self.logfile = os.path.join(self.logs_dir,log_name + ".log")
		self.logger = logging.getLogger(__name__)					# 初始化一个 Logger 对象

		if not os.path.exists(self.logs_dir):
			os.makedirs(self.logs_dir)
		
		LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
		DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"                        # 日期格式
		fp = logging.FileHandler(self.logfile, encoding='utf-8')
		fs = logging.StreamHandler()
		# logging.disable(logging.DEBUG)			# 禁用日志输出debug
		# basicConfig 是全局设置，无需对每个Logger对象重新设置
		logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])
		# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])

		if not os.path.exists(self.apis_json):
			os.makedirs(self.apis_json)


	def visit_net(self,*network):
		''' 网络访问接口 '''
		try:

			if (len(network) > 2 ) or (len(network) < 1 ):
				
				logging.error(sys._getframe().f_code.co_name + " : " \
					+ str(sys._getframe().f_lineno) +"\t|\t" + \
					"参数错误，至少有一个参数")

				sys.exit()

			url = network[0]
			payload = None if len(network) == 1 else network[1]

			session = requests.Session()	# 创建一个session会话

			session.mount('http://',HTTPAdapter(max_retries=3))
			session.mount('https://',HTTPAdapter(max_retries=3))	# 绑定一个 HTTPHTTPAdapter 对象，设置重连次数

			response = session.get(url,params=payload,timeout=(6,3))	# 设置连接（connect）超时为 6s，响应超时（read）为 3s 

			if response.status_code == 200:
				# 首先通过正则表达式去除字典中htm标签，然后把unicode码转换为中文字符
				res = re.sub(r'<br \W\W>',' ',str(response.text)).encode('utf-8').decode('unicode_escape')	
	
				json_obj = json.loads(res)		# 将字符串类型的数据转化为 python 字典类型的数据，或者说json数据

				return json_obj

		except Exception as e:
			print(e)


	def json_update(self,json_file,in_data,out_data):
		''' 
			json 数据更新 
			in_data : 传递 网络数据
			out_data : 写入文件的 数据
		'''
		flag = None if in_data == None else in_data['status']

		if flag:

			with self.lock:
				with open(json_file,"w+",encoding='utf-8') as f_obj:
					json.dump(out_data,f_obj,ensure_ascii=False,indent =4)

			return out_data


	def areas(self, tree=1):
		''' 获取区域信息 '''
		try:

			filename = "areas.json"
			room_names = []
			rooms = {}

			json_file = os.path.join(self.apis_json,filename)

			if os.path.exists(json_file):					# 如果存在,读

				with open(json_file,"r",encoding='utf-8') as f_obj:
					write_result = json.load(f_obj)
			else:											# 不存在,写

				payload = { 'tree' : tree }
				url = self.ip_addr + 'areas'

				in_data = self.visit_net(url,payload)
				area_info = in_data['data']['list'][0]['_child']

				for child in area_info:

					if '_child' in child.keys():

						for item in child['_child']:
							room_names.append(item['name'])
							rooms[item['name']] = item['id']

				out_data = rooms

				write_result = self.json_update(json_file,in_data,out_data)

			return write_result

		except Exception as e:
			print(e)

	def space_days(self, areaId):
		''' 获取可预约日期 '''
		try:
			url = self.ip_addr + 'space_days/' + str(areaId)

			filename = "space_days.json"
			json_file = os.path.join(self.apis_json,filename)
			file_exist = os.path.exists(json_file)

			nowdate = time.strftime('%Y-%m-%d',time.localtime())

			if file_exist:
				with open(json_file,"r") as f_obj:
					data = json.load(f_obj)

			if file_exist and (data['day'] == nowdate):		# 果如存在 且 当前日期格式字符串与json文件中一致 则不更新
				write_result = data

			else:

				in_data = self.visit_net(url)
				out_data = in_data['data']['list'][0]

				write_result = self.json_update(json_file,in_data,out_data)

			return write_result

		except Exception as e:
			print(e)


	def space_time_buckets(self, areaId):
		''' 
			获取可预约时间段
		'''
		try:
			url = self.ip_addr + 'space_time_buckets'

			data = self.space_days(areaId)

			payload = {
			'area' : areaId,
			'day' : data['day']
			}

			if data['day'] in [0,None]:

				logging.error(sys._getframe().f_code.co_name + " : " \
					+ str(sys._getframe().f_lineno) +"\t|\t" + \
					"未获取可预约日期参数!")	

				sys.exit()

			filename = "space_time_buckets.json"
			json_file = os.path.join(self.apis_json,filename)
			file_exist = os.path.exists(json_file)

			if file_exist:		# 如果存在 读

				with open(json_file,"r") as f_obj:
					json_data = json.load(f_obj)

			# 如果存在 且相关参数 未改变 不更新json文件
			if file_exist and (json_data['area'] == areaId and json_data['day'] == data['day']): 

				write_result = json_data
			
			else:			# 其他情况写

				in_data = self.visit_net(url,payload)

				if in_data['status'] == 0:

					logging.error(sys._getframe().f_code.co_name + " : " \
							+ str(sys._getframe().f_lineno) +"\t|\t" + \
							"当前时间不处于预约时间段,请于第二天 5:58 后重试!")

					sys.exit()

				out_data = in_data['data']['list'][0]

				write_result = self.json_update(json_file,in_data,out_data)

			return write_result

		except Exception as e:
			print(e)


	def roomno_search(self,room_name=None):
		''' 自习室/走廊 号 （基于原始areas.json文件）'''
		try:

			rooms =  self.areas()

			if not room_name:
				return rooms

			if room_name not in rooms.keys():

				logging.error(sys._getframe().f_code.co_name + " : " \
					+ str(sys._getframe().f_lineno) +"\t|\t" + \
					"您的输入有误,自习室名仅有如下几个: " + \
					"(" + ", ".join(rooms.keys()) + ")")

				sys.exit()
			else:
				return rooms[room_name]

		except Exception as e:
			print(e)


	def spaces_info_real_time(self, room_name):
		''' 
			获取实时空间预约信息
		'''
		try:

			areaId = self.roomno_search(room_name)

			data = self.space_time_buckets(areaId)

			if not data:

				logging.error(sys._getframe().f_code.co_name + " : " \
					+ str(sys._getframe().f_lineno) +"\t|\t" + \
					"未获取可预约时间段参数！")

				sys.exit()

			url = self.ip_addr + 'spaces_old'

			payload = {
						 'area' : areaId,
						 'day' : data['day'],
						 'endTime' : data['endTime'],
						 'segment' : data['bookTimeId'],
						 'startTime' : data['startTime'],
						}

			in_data = self.visit_net(url,payload)

			out_data = in_data['data']['list']

			return out_data

		except Exception as e:
			print(e)


	def areas_test(self, tree=1):
		''' 获取实时区域信息 '''
		try:

			room_names = []

			payload = { 'tree' : tree }
			url = self.ip_addr + 'areas'

			in_data = self.visit_net(url,payload)
			area_info = in_data['data']['list'][0]['_child']

			for child in area_info:

				if '_child' in child.keys():

					for item in child['_child']:
						
						room_names.append(item)

			return room_names

		except Exception as e:
			print(e)
