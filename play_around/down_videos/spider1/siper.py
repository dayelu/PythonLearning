import requests
# from selenium import webdriver
from bs4 import BeautifulSoup

url = "http://exam.cabplink.com/user/MyCourse.aspx"

# url = "http://exam.cabplink.com/class/play.aspx?lid=4407"
# url = "http://playvideo.qcloud.com/getplayinfo/v2/1251470151/4564972818880053538"

req_headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control": "max-age=0",
	"Connection": "keep-alive",
	"Cookie": "tencentSig=421573632; _qddaz=QD.qduf47.j7ut72.jutw9wo9; UM_distinctid=16a5ccaf2bd8fa-0f2028b1ad097f-7a1437-1fa400-16a5ccaf2be691; learn=RegCode=cdf66666-d9a8-4061-b9df-2ac443f17f94; _qdda=3-1.r4qrh; _qddab=3-9fjtek.juz4f32t; CNZZDATA1257180565=1862432647-1556343810-http%253A%252F%252Fexam.cabplink.com%252F%7C1556343810; ASP.NET_SessionId=cuxi4gjajmdxhvvg0ga5ga1s; _qddamta_4008188688=3-0; tencentSig=1590563840; LearnFormCookie=User=n%00i%00d%00a%00y%00e%006%006%006%00&Id=9969febc-2bcf-41c2-ba8a-9b1240cfde33&Expires=2019/4/30 3:00:00&Code=Jaxd9SV9qlxh%2fXFlwWZehz%2fWKJst99LTSKFbjXEYEVChjsHeq0FeRnr%2bcFbdrEz3HLjeQSFFZxV%2bX3XvlYfMDDiyT9%2btQ5g%2bH7TJyFuY7VRsiIeDxXFZWlhZRVvBex9%2f&AuthSingle=497a29da-7a15-4888-a60a-440bed60ebaa&SiteDomain=exam.cabplink.com",
	"Host": "exam.cabplink.com",
	"Referer": "http://exam.cabplink.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
	"Upgrade-Insecure-Requests": "1"
}

# req_headers = {
# 	"Origin": "http://exam.cabplink.com",
# 	"Referer": "http://exam.cabplink.com/class/play.aspx?lid=4407",
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
# }

res = requests.get(url,headers=req_headers)

soup = BeautifulSoup(res.text,features="html.parser")

courses = soup.select(".kec_zj_lingtk01 a")

# print(courses)
for course in courses:
		# print("http://exam.cabplink.com/"+course.get("href") + "\t" + course.get("tips"))
		print(course.get("tips"))


# browser = webdriver.Chrome()

# browser.get(url)

# browser.add_cookie({})

# print(data)