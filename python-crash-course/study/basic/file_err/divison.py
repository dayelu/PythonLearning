while True:
	num1 = input("请输入被除数：")

	if num1 == 'q':
		print("拜拜！")
		break

	num2 = input("请输入除数：")

	if num2 == 'q':
		print("拜拜！")
		break
	try:
		res = int(num1)/int(num2)

	except ZeroDivisionError:
		print("除数不能为0")
	else:
		print(str(res))