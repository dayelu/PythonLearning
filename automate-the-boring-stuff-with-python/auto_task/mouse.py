import pyautogui,time,pyperclip

numbers = ""
for i in range(200):
	numbers = numbers + str(i) + "\n"

pyperclip.copy(numbers)
# print(pyperclip.paste())
time.sleep(5)
# pyautogui.click()
distance = 200

pyautogui.scroll(100)					#滚动鼠标

while False:
# while distance > 0:
	pyautogui.dragRel(distance,0,duration=0.2)
	distance = distance - 5
	pyautogui.dragRel(0,distance,duration=0.3)				#拖拽鼠标
	pyautogui.dragRel(-distance,0,duration=0.2)
	distance = distance -5
	pyautogui.dragRel(0,-distance,duration=0.2)