import json
json_file = "text/write_json_file.txt"
num_list = [1,2,3,4,5,6,9]
try:
	with open(json_file,"w") as f_obj:
		json.dump(num_list,f_obj)				#除了能输入数组之外，暂时看不出猫腻
		#f_obj.write(num_list)					#TypeError: write() argument must be str, not list

except FileNotFoundError:
	print("文件不存在")



