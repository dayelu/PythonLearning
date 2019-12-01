import json

try:
	file = "text/write_json_file.txt"

	with open(file) as f_obj:
		# content = f_obj.read()				#暂时没看出来二者有什么区别
		content = json.load(f_obj)

	print(content)
except FileNotFoundError:
	print("文件未找到")