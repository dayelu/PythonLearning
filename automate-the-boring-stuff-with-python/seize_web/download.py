import requests,sys,random,string

def carryout():
	try:

		with open("video_urls.txt","r") as f_obj:

			lines = f_obj.readlines()


		for line in lines:
			url = line.rstrip()
			download(url)


	except Exception as e:
		print(e)




def download(url):
	try:

		key = ''.join(random.sample(string.ascii_letters + string.digits, 8))

		filename = "videos/" + str(key) + ".mp4"

		with  open(filename,"wb") as f_obj:

				video =  visit_web(url)

				for chunk in video.iter_content(100000):

					f_obj.write(chunk)


	except Exception as e:
		print(e)



def visit_web(url):
	"""网页浏览器"""
	try:
		res = requests.get(url)
		res.raise_for_status()
		return res

	except Exception as e:
		print(e)


carryout()