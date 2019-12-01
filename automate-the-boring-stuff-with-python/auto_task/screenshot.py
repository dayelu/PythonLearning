import pyautogui

im = pyautogui.screenshot()	#获取一个快照对象
im.save("cut.png")			#保存快照

key1 = pyautogui.center(pyautogui.locateOnScreen("pic1.png"))	#获取按钮截图在快照中的位置，并确定这个方块区域的几何中
key2 = pyautogui.center(pyautogui.locateOnScreen("pic2.png"))

print(key1)
print(key2)
print("开始点击按钮一")
pyautogui.doubleClick(key1)
pyautogui.PAUSE = 3
print("开始点击按钮2")
pyautogui.doubleClick(key2)
print("完成")