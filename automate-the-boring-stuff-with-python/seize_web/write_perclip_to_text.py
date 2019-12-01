import pyperclip,sys

def write(file,content):
	"""写入操作"""
	try:
		
		with open(file,"a") as f_obj:
			f_obj.write(content+"\n")

	except Exception as e:
		print(e)


def read(file):
	try:
		
		with open(file,"r") as f_obj:

			lines = f_obj.readlines()

		return lines


	except Exception as e:
		print(e)


def exec():

	try:
		file = "pyperclip.txt"
		
		content = pyperclip.paste()
		exists_content = read(file)

		if content+"\n" not in exists_content:
			with open(file,"a") as f_obj:
				f_obj.write(content+"\n")

	except Exception as e:
		print(e)


while True:
	exec()