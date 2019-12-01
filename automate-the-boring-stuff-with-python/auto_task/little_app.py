import pyautogui,os,sys,time
#打开qq
os.popen("D:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQScLauncher.exe")
time.sleep(3)
qq_login = (956, 668)
#登陆
pyautogui.click(qq_login)
time.sleep(4)
#打开微信
os.popen("D:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe")

time.sleep(3)

weixin_login = (963, 601)
#登陆
pyautogui.click(weixin_login)

time.sleep(3)

min_qq = (1532, 210)
#qq最小化
pyautogui.click(min_qq)

time.sleep(2)
#位置总是在变化琢磨不透。。。。失败
close_script = (1092, 147)
#退出脚本
pyautogui.click(close_script)

