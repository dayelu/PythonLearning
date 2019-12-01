import bs4,requests,os,sys,pyperclip
from time import time
def find_beauty(url_start):
	'''main'''
	try:
		start_time = time()
		if "http" not in url_start:
			sys.exit("链接错误！")

		urls = seize_content(url_start,type='urls')

		for url in urls:
		#下载图片
			res = seize_content(url)
			download(res['title'],res['now_page'],res['pic_url'])

		# with open("urls.txt","a") as f_obj:
		# 	f_obj.write(url_start+"\n")
		end_time = time()
		print("下载耗时："+str(end_time - start_time)+"秒！")

	except Exception as e:
		print(e)


def seize_content(url,type='content'):
	""""获取下载信息"""
	try:
		res = visit_web(url)

		soup = bs4.BeautifulSoup(res.text,features="html.parser")

		if type == 'urls':
			scrolls = soup.select(".scroll-img-cont li a")
			res = []
			for scroll in scrolls:
				res.append(scroll.get("href"))

		else:
			res = {}	#定义一个空字典类型
			res['title'] = soup.select(".Bigimg .ptitle h1")[0].getText()
			res['now_page'] = soup.select(".Bigimg .ptitle span")[0].getText()

			if "wallpaper_detail" in url:
				attr = "src"
			else:
				attr = "url"

			res['pic_url'] = soup.select(".pic-meinv .pic-large")[0].get(attr)

		return res
		
	except Exception as e:
		print(e)





# import requests
# import tqdm
#  def download_from_url(url, dst):
#     response = requests.get(url, stream=True) #(1)
#     file_size = int(response.headers['content-length']) #(2)			from 公众号:进击的coder,头文件里没有发回这个信息咋办？？？？？
#     if os.path.exists(dst):
#         first_byte = os.path.getsize(dst) #(3)
#     else:
#         first_byte = 0
#     if first_byte >= file_size: #(4)
#         return file_size
#     header = {"Range": f"bytes={first_byte}-{file_size}"} 
#     pbar = tqdm(
#         total=file_size, initial=first_byte,
#         unit='B', unit_scale=True, desc=dst)
#     req = requests.get(url, headers=header, stream=True) #(5)
#     with(open(dst, 'ab')) as f:
#         for chunk in req.iter_content(chunk_size=1024): #(6)
#             if chunk:
#                 f.write(chunk)
#                 pbar.update(1024)
#     pbar.close()
#     return file_size





def download(filepath,filename,pic_url):
	"""下载器"""
	#下载位置
	try:
		pic_root = "imgs/"
		path = pic_root + filepath
		if(os.path.exists(path) == False):
			os.makedirs(path)

		suffix = pic_url.split('.')[-1]

		file = path+"/pic" + filename + '.' + suffix
		
		if(os.path.exists(file) == False):
			
			with open(file,"wb") as f_obj:
				pic = visit_web(pic_url)
				for chunk in pic.iter_content(chunk_size=1024):
					f_obj.write(chunk)

	except Exception as e:
		print(e)

def visit_web(url):
	"""网页浏览器"""
	try:
		# header = {"Range": f"bytes={first_byte}-{file_size}"} 
		# res = requests.get(url,headers=header, stream=True)
		res = requests.get(url, stream=True)
		res.raise_for_status()

		return res

	except Exception as e:
		print(e)


# url_start = pyperclip.paste()

# result = find_beauty(url_start)



# import aiohttp
# import asyncio
# from tqdm import tqdmx
# async def fetch(session, url, dst, pbar=None, headers=None):
#     if headers:
#         async with session.get(url, headers=headers) as req:
#             with(open(dst, 'ab')) as f:
#                 while True:
#                     chunk = await req.content.read(1024)
#                     if not chunk:
#                         break
#                     f.write(chunk)
#                     pbar.update(1024)
#             pbar.close()
#     else:
#         async with session.get(url) as req:
#             return req


# async def async_download_from_url(url, dst):
#     '''异步'''
#     async with aiohttp.connector.TCPConnector(limit=300, force_close=True, enable_cleanup_closed=True) as tc:
#         async with aiohttp.ClientSession(connector=tc) as session:
#             req = await fetch(session, url, dst)

#             file_size = int(req.headers['content-length'])
#             print(f"获取视频总长度:{file_size}")
#             if os.path.exists(dst):
#                 first_byte = os.path.getsize(dst)
#             else:
#                 first_byte = 0
#             if first_byte >= file_size:
#                 return file_size
#             header = {"Range": f"bytes={first_byte}-{file_size}"}
#             pbar = tqdm(
#                 total=file_size, initial=first_byte,
#                 unit='B', unit_scale=True, desc=dst)
#             await fetch(session, url, dst, pbar=pbar, headers=header)