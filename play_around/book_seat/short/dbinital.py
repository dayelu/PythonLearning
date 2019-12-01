#!/usr/bin/python3
import os
import sys
import json
import pymongo
from book import SeatBook

sb = SeatBook()

myclient = pymongo.MongoClient("mongodb://XXXXXXXXXXXX:XXXX/")

# dblist = myclient.list_database_names()
# if "seats_info" not in dblist:

mydb = myclient["seats_info"]

collist = mydb.list_collection_names()

areas_col = mydb["areas"]

if "areas" not in collist:	# 判断areas表是否存在

	rooms = sb.areas_test()

	for room in rooms:		# 不存在，插入自习区域信息

		areas_col.insert_one(room)

	print("插入自习区域信息完成!")


for item in areas_col.find({},{"_id":0,"name":1,"ROW_NUMBER":1}):

	if item["ROW_NUMBER"] not in collist:	# 判断自习区域表是否存在
		
		seats = sb.spaces_info_real_time(item["name"])		

		room_col = mydb[item["ROW_NUMBER"]]		# 不存在，创建自习区域表

		for seat in seats:
			room_col.insert_one(seat)			# 向每张表插入座位信息

		print(item["name"] + "信息插入完成！")


myclient.close()	# 关闭连接




