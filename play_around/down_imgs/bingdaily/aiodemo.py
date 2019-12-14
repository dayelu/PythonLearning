import os
import sys
import time
import uvloop
import logging
import asyncio
import aiohttp
import datetime
from bs4 import BeautifulSoup

logfile = "coro2.log"
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

if not os.path.exists(f"bydaily2/{tdate}/"):
  os.makedirs(f"bydaily2/{tdate}/")


async def page_pic_async(session, page_url):
    """
        每页图片下载
    """
    try:
        async with session.get(page_url) as resp:
            resp_text = await resp.text()
            soup = BeautifulSoup(resp_text,features="html.parser")
            pic_urls = soup.select(".container .item .card img")

        tasks = [asyncio.create_task(download_from_url_async(session, pic.get("src"),pic.get("src").split("/")[-1]) ) for pic in pic_urls]

        for task in tasks:
            await task

    except Exception as e:
        logging.info(e)



async def download_from_url_async(session, url, dst):

    try:

        dst = f"bydaily2/{tdate}/{dst}"

        async with session.get(url) as resp:
            file_size = int(resp.headers['content-length'])

        if os.path.exists(dst):
            
            first_byte = os.path.getsize(dst)
        else:
            
            first_byte = 0

        if first_byte >= file_size:
            
            return file_size

        header = {"Range": f"bytes={first_byte}-{file_size}"}

        async with session.get(url, headers=header) as res:
            with(open(dst, 'ab')) as f:
                while True:
                    chunk = await res.content.read(100)
                    if not chunk:
                        break
                    f.write(chunk)


        print(f"Pitture {dst} download finished!")

        return file_size

    except Exception as e:
        logging.info(e)

async def get_pages_async(session, url_head):
    """
        获取每日壁纸总页数
    """
    try:
        async with session.get(url_head) as resp:
            resp_text = await resp.text()
        
        soup = BeautifulSoup(resp_text, features="html.parser")

        pages = soup.select(".page span")[0].getText().split(" / ")[1]

        return int(pages)

    except Exception as e:
        logging.info(e)

url_head = "https://bing.ioliu.cn/"


async def all_pic_async(session, url_head):
    """
        所有图片下载
    """
    try:

        pages = await get_pages_async(session, url_head)

        urls =[f'{url_head}?p={page}' for page in range(1,int(pages)+1)]

        tasks = [asyncio.create_task(page_pic_async(session, pic_url)) for pic_url in urls]
        for task in tasks:
            await task

    except Exception as e:
        logging.info(e)

async def main():
    url_head = "https://bing.ioliu.cn/"
    timeout = aiohttp.ClientTimeout(total=5*60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        await all_pic_async(session, url_head)


if __name__ == '__main__':

    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

    #asyncio.run(main())

end = time.time()
utime = int(end - start)
print(f"\n总耗时，{utime}s.")

