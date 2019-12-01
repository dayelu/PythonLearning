import pyautogui
# pyautogui.size()
print("按 CTRL + C 退出。")
try:
	x,y = pyautogui.size()			#这也行？？？
	position_str = "x: " + str(x).rjust(4) + " y: " + str(y).rjust(4)
	print(position_str,end = "")
	# print("\b" * len(position_str),end="",flush=True)
	print(pyautogui.position())

	pyautogui.click(pyautogui.position())


	# for i in range(10):						#这也是。。。
	# while True:

		# pyautogui.moveRel(100,100,duration=0.25)
		# print(pyautogui.position())						#打印鼠标位置
		# pyautogui.moveTo(200,100,duration=0.25)			#将鼠标从当前位置立即移动到指定位置
		# print(pyautogui.position())
		# pyautogui.moveRel(200,200,duration=0.25)		#从代码开始的地方开始按正方形移动
		# print(pyautogui.position())
		# pyautogui.moveTo(100,200,duration=0.25)
		# print(pyautogui.position())

except KeyboardInterrupt:							#没什么用，根本检测不到CTRL+C中断
	print("\nDone.")