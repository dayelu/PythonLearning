import os
import re
import sys
import time
import json
import logging
import hashlib
import smtplib
import requests
from threading import Thread, Lock
from email.utils import formataddr
from email.mime.text import MIMEText
from requests.adapters import HTTPAdapter

class SeatBook(object):
	"""
		| status |  meaning  |
		| :----: | :-------: |
		|    0   |  failure  |
		|    1   |  success  |
		|    2   | blacklist |

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
		self.sender = {'nickname':'XXXXXXXXXXXX', 'accout':'XXXXXXXXXXXX@qq.com','password':'XXXXXXXXXXXX'} # 发件人信息,邮箱密码为开启stmp服务时给与的授权码
		self.receiver = {'nickname':'XXXXXXXXXXXX', 'accout':'XXXXXXXXXXXX@qq.com'}	# 收件人信息，可以是自己的	# 收件人信息，可以是自己的_json"
		
		self.apis_json = "apis_json"
		self.seatfiles = "seatfiles"
		
		self.logs_dir = "logs"
		self.logfile = os.path.join(self.logs_dir,log_name + ".log")
		self.logger = logging.getLogger(__name__)					# 初始化一个 Logger 对象

		if not os.path.exists(self.logs_dir):
			os.makedirs(self.logs_dir)
		
		LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
		DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"                        # 日期格式
		fp = logging.FileHandler(self.logfile, encoding='utf-8')
		fs = logging.StreamHandler()
		logging.disable(logging.DEBUG)			# 禁用日志输出debug
		# basicConfig 是全局设置，无需对每个Logger对象重新设置
		# logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])
		logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])

		if not os.path.exists(self.seatfiles):
			os.makedirs(self.seatfiles)

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
			# 实践证明,将连接超时限制在 6s 之外更有机会成功,3s 基本失败,至于超时重连的时间 与 成功率的关系有待于更多的测试

			if response.status_code == 200:
				# 首先通过正则表达式去除字典中htm标签，然后把unicode码转换为中文字符
				res = re.sub(r'<br \W\W>',' ',str(response.text)).encode('utf-8').decode('unicode_escape')	
	
				json_obj = json.loads(res)		# 将字符串类型的数据转化为 python 字典类型的数据，或者说json数据

				return json_obj

		except Exception as e:
			print(e)

	def get_token(self, in_str):
		'''md5加密'''
		try:
			md5str = in_str
			m1 = hashlib.md5()
			m1.update(md5str.encode("utf-8"))
			token = m1.hexdigest()
			return token

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
			# 写入没有问题,读取 也需要加上 encoding='utf-8' 参数
			# 'gbk' codec can't decode byte 0x9f in position 541: illegal multibyte sequence
			with self.lock:
				with open(json_file,"w+",encoding='utf-8') as f_obj:
					json.dump(out_data,f_obj,ensure_ascii=False,indent =4)

			return out_data


	def reneges(self):
		''' 获取违约信息 '''
		try:

			res_data = self.login_body()

			access_token = res_data['data']['_hash_']['access_token']

			url = self.ip_addr + 'profile/reneges'

			payload = {
						'access_token' : access_token,
						'userid' : self.username
						}

			data = self.visit_net(url,payload)		

			if data['status'] == 1:
				return data['data']['list']

		except Exception as e:
			print(e)

	def profile(self):
		''' 用户基本信息 '''
		try:

			res_data = self.login_body()

			access_token = res_data['data']['_hash_']['access_token']

			url = self.ip_addr + 'profile'

			payload = {
						'access_token' : access_token,
						'userid' : self.username
						}

			data = self.visit_net(url,payload)

			if data['status'] == 1:
				return data['data']['list']

		except Exception as e:
			print(e)

	def books_info(self):
		''' 获取用户预约的空间信息 '''
		try:
			tips = {}

			res_data = self.login_body()

			access_token = res_data['data']['_hash_']['access_token']

			url = self.ip_addr + 'profile/books'

			payload = {
						'access_token' : access_token,
						'userid' : self.username
						}

			data = self.visit_net(url,payload)
							
			if data['status'] == 1:

				nowdate = time.strftime('%Y-%m-%d',time.localtime())
				last_data = data['data']['list'][0]['bookTimeSegment'][:10]

				success = "今日预约情况: 今天已预约成功！\t|\t" + '座位号: ' + data['data']['list'][0]['spaceInfo'][:-4]
				failure = "今日预约情况: 今天未预约或预约失败！"

				res = success if nowdate == last_data else failure

				return res

		except Exception as e:
			print(e)


	def book_declare(self):
		''' 预约规则 '''
		try:

			url = self.ip_addr + 'configs/book_declare'
			data = self.visit_net(url)

			return data['data']['list']

		except Exception as e:
			print(e)


	def login_body(self):
		''' 登录接口 '''

		try:
			passwd_hash = self.get_token(self.password)

			payload = {
						'username' : self.username,
						'password' : passwd_hash,
						'from' : 'mobile'
						}

			url = self.ip_addr + 'login'
			data = self.visit_net(url, payload)

			if data['status'] == 1:
				return data

			elif data['status'] == 2:		# 被拉黑
				
				self.mail(data['msg'])

				logging.error(sys._getframe().f_code.co_name + " : " \
					+ str(sys._getframe().f_lineno) +"\t|\t" + \
					data['msg'])	

				sys.exit()

		except Exception as e:
			print(e)


	def login(self):
		''' 登录 json数据文件处理接口 '''
		try:
			
			filename = "login.json"

			json_file = os.path.join(self.apis_json,filename)

			file_exist = os.path.exists(json_file)

			if file_exist:

				with open(json_file,"r") as f_obj:
					data = json.load(f_obj)

				timeArray = time.strptime(data['expire'], "%Y-%m-%d %H:%M:%S") # 将其转换为时间数组 
				expire_time = int(time.mktime(timeArray))	# 转换为时间戳 
			
			now_time = int(time.time())		# 初始化

			if file_exist and (now_time < expire_time):		# 文件存在并且 token 未失效不更新json文件

				write_result = data

			else:		# 当今仅当 login.json 文件不存在且登录成功时才 写入 数据

				in_data = self.login_body()
				out_data = in_data['data']['_hash_']

				write_result = self.json_update(json_file,in_data,out_data)

			return write_result['access_token']

		except Exception as e:
			print(e)

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

			某些时段存在返回结果为: "{'status': 0, 'msg': '获取可预约时间段', 'data': {'list': []}}" 
			说明在此接口存在对当前时间是否为预约时间的判断，如果当前时间不在规定的预约时间范围内，则不会生成 预约时间段信息
			此时间段疑似在 晚上九点 左右 直到 第二天 0点为止
			需要注意的是，这个时间段只适用于对本接口的限制，对于预约的正式接口 仍是 05:58 之后
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


	def spaces(self, seatId):
		''' 获取空间详情 '''
		try:
			url = self.ip_addr + 'spaces/' + str(seatId)
			data = self.visit_net(url)

			filename = "spaces" + str(seatId) + ".json"
			json_file = os.path.join(self.apis_json,filename)
			self.json_update(json_file,data,data)

			return data

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

			json_file = os.path.join(self.seatfiles ,room_name + ".json")

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

			write_result = self.json_update(json_file,in_data,out_data)

			return write_result

		except Exception as e:
			print(e)



	def spaces_info(self, room_name):
		''' 
			获取空间预约信息
			(仅仅为了加速 获取座位id,获取了某一时刻座位信息包括座位状态在内的所有数据，并没有体现查询座位状态的功能) 
		'''
		try:

			areaId = self.roomno_search(room_name)		

			json_file = os.path.join(self.seatfiles ,room_name + ".json")

			file_exist = os.path.exists(json_file)

			if file_exist:						# 如果存在,读

				with open(json_file,"r",encoding='utf-8') as f_obj:
					write_result = json.load(f_obj)

			else:								# 不存在,写

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

				write_result = self.json_update(json_file,in_data,out_data)

				print(json_file + "新建完毕！")

			return write_result

		except Exception as e:
			print(e)

	def create_info(self):
		'''
			新建多个自习室座位信息文件
		'''
		try:
			start_time = time.time()

			threads = []

			rooms = self.roomno_search()

			for name in rooms.keys():
				
				t = Thread(target=self.spaces_info,
					args=(name,)
					)

				threads.append(t)

			for thr in threads:
				thr.start()

			for thr in threads:
				thr.join(timeout=60)
			
			end_time = time.time()

			print("新建完毕，耗时" + str(end_time - start_time) +" s")

		except Exception as e:
			print(e)


	def seat_id_inquiry(self,seat_no):
		''' 座位号查询 '''
		try:

			res = {}

			seats_info = self.spaces_info(self.room_name)

			if (seat_no < 1) or (seat_no > len(seats_info)):

				logging.error(sys._getframe().f_code.co_name + " : " \
					+ str(sys._getframe().f_lineno) +"\t|\t" + \
					"您输入的座位号有误，" + self.room_name + '的座位号范围在 (1 - ' + \
					str(len(seats_info)) + ') 之间')

				sys.exit()
			
			seat_no = str(seat_no)

			while len(seat_no) < 3:
				seat_no = '0' + seat_no

			for seat in seats_info:
				if seat['no'] == seat_no:	# 不管写了多少次，都要注意 == 与 =
					res['seat_id'] = seat['id']
					res['area_id'] = seat['area']
			return res

		except Exception as e:
			print(e)


	def book_new(self,seat_no):
		''' 座位预约 '''
		try:

			seat_info = self.seat_id_inquiry(seat_no=seat_no)

			url = self.ip_addr + 'spaces/' + str(seat_info['seat_id']) + '/book'

			stb_data = self.space_time_buckets(seat_info['area_id'])
			
			if not stb_data:

				logging.error(sys._getframe().f_code.co_name + " : " \
						+ str(sys._getframe().f_lineno) +"\t|\t" + \
						"未获取可预约时间段参数！")

				sys.exit()

			passwd_hash = self.login()

			if not passwd_hash:

				logging.error(sys._getframe().f_code.co_name + " : " \
						+ str(sys._getframe().f_lineno) +"\t|\t" + \
						"登录异常!")

				sys.exit()

			payload = {
						'access_token' : passwd_hash,
						'userid' : self.username,
						'type' : 1,
						'id' : seat_info['seat_id'],
						'segment' : stb_data['bookTimeId']
						}

			data = self.visit_net(url,payload)

			return data

		except Exception as e:
			print(e)


	def book_final(self,seat_no):
		'''
			弃用无意义的递归方式判断登录信息是否过期
		'''
		try:

			data = self.book_new(seat_no=seat_no)

			if not data['data'] and os.path.exists("apis_json/login.json"):
				os.remove("apis_json/login.json")
				data = self.book_new(seat_no=seat_no)

			res = data['msg'] if data else None	# python 中类似其他语言的三目运算符语法
			
			seat = self.room_name + "\t" + str(seat_no) + "\t"

			logging.info(sys._getframe().f_code.co_name + " : " \
					+ str(sys._getframe().f_lineno) +"\t|\t" + \
					seat + res)

			return 	res

		except Exception as e:
			print(e)


	def mail(self,content):

		'''
			qq邮件发送，抄袭于 博客园两位博主，
			网址分别为： "https://www.cnblogs.com/xshan/p/7954317.html",
			"https://www.cnblogs.com/lovealways/p/6701662.html"
		'''
		ret=True

		try:

			msg=MIMEText(content,'plain','utf-8')
			msg['From']=formataddr([self.sender['nickname'] ,self.sender['accout']])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
			msg['To']=formataddr([self.receiver['nickname'] ,self.receiver['accout']])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
			msg['Subject']="邮件主题-座位预约结果"                # 邮件的主题，也可以说是标题

			server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
			server.login(self.sender['accout'], self.sender['password'])  # 括号中对应的是发件人邮箱账号、邮箱密码
			server.sendmail(self.sender['accout'],[self.receiver['accout'],],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
			server.quit()# 关闭连接
		except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False

			ret=False
			
		return ret


	def areas_test(self, tree=1):
		''' 获取区域信息 '''
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



def main():
	'''
		入口
	'''
	try:

		sb = SeatBook()

		flag = True

		stime = time.time()

		t = time.localtime(stime)
		five_fifty_sevnth = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 05:57:00', t),'%Y-%m-%d %H:%M:%S')))
		six_fifteen = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 06:15:00', t),'%Y-%m-%d %H:%M:%S')))
		
		while flag:

			if (int(time.time()) > six_fifteen) or int(time.time()) < five_fifty_sevnth:
				flag = False
			for item in sb.seat_nos:
				sb.book_final(item)

			etime = time.time()
			utime=round((etime-stime),2)

			print('finished in '+str(utime)+' seconds')

	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()
