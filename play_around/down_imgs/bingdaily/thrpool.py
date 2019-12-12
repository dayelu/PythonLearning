import os
import time
import logging
import datetime
import requests
import concurrent.futures
from bs4 import BeautifulSoup

logfile = "thrpool1.log"
logger = logging.getLogger(__name__)                   # 初始化一个 Logger 对象

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(lineno)d - %(funcName)s - %(threadName)s - %(thread)d - %(message)s"    # 日志格式化输出
# LOG_FORMAT = "%(funcName)s - %(threadName)s - %(thread)d - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"                        # 日期格式
fp = logging.FileHandler(logfile, encoding='utf-8')
fs = logging.StreamHandler()
logging.disable(logging.DEBUG)          # 禁用日志输出debug
# basicConfig 是全局设置，无需对每个Logger对象重新设置
logging.basicConfig(
            # filename=logfile,
            # filemode='w',
            level=logging.DEBUG,
            format=LOG_FORMAT,
            datefmt=DATE_FORMAT,
            handlers=[fp, fs]       # 控制控制台输出与否
            )



start = time.time()
now = datetime.datetime.now()
tdate = now.strftime("%Y%m%d")

if not os.path.exists(f"bydaily1/{tdate}/"):
  os.makedirs(f"bydaily1/{tdate}/")


def get_pages(url_head):
    """
        获取每日壁纸总页数
    """
    try:

        res = requests.get(url_head, stream=True) #(1)

        soup = BeautifulSoup(res.text,features="html.parser")

        pages = soup.select(".page span")[0].getText().split(" / ")[1]

        return int(pages)

    except Exception as e:
        logging.error(e)

def download_from_url(url, dst):

    try:

        dst = f"bydaily1/{tdate}/{dst}"

        response = requests.get(url, stream=True) #(1)
        
        file_size = int(response.headers['content-length']) #(2)

        if os.path.exists(dst):
            
            first_byte = os.path.getsize(dst) #(3)
        else:
            
            first_byte = 0

        if first_byte >= file_size: #(4)
            
            return file_size

        header = {"Range": f"bytes={first_byte}-{file_size}"} 

        req = requests.get(url, headers=header, stream=True) #(5)

        with(open(dst, 'ab')) as f:

            for chunk in req.iter_content(chunk_size=100): #(6)

                if chunk:

                    f.write(chunk)

        # logging.info("nothing wrong")

        print(f"Pitture {dst} download finished!")

        return file_size

    except Exception as e:
        logging.info(e)


def thrpools(page_url):

    try:

        res = requests.get(page_url, stream=True) #(1)
        soup = BeautifulSoup(res.text,features="html.parser")

        pic_urls = soup.select(".container .item .card img")

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

            futus = [executor.submit(download_from_url, pic.get("src"), pic.get("src").split("/")[-1]) for pic in pic_urls]

            for future in futus:
                future.result(timeout=30)

    except concurrent.futures.TimeoutError as e:
        logging.error(e)


def all_pic_by_pool(url_head):
    """
        所有图片下载
    """
    try:

        pages = get_pages(url_head)
        urls =[f'{url_head}?p={page}' for page in range(1,int(pages)+1)]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            
            futus = [executor.submit(thrpools, pic_url) for pic_url in urls]

            for future in futus:
                future.result(timeout=30)

    except concurrent.futures.TimeoutError as e:
        logging.error(e)

url_head = "https://bing.ioliu.cn/"

# thrpools(url_head)
all_pic_by_pool(url_head)


end = time.time()
utime = int(end - start)
print(f"\n总耗时，{utime}s.")
