import os
import datetime
import requests
# from tqdm import tqdm
from threading import Thread
from bs4 import BeautifulSoup


now = datetime.datetime.now()
tdate = now.strftime("%Y%m%d")

def all_pic(url_head):
    """
        所有图片下载
    """
    try:

        urls =[]

        pages = get_pages(url_head)

        for page in range(1,int(pages)+1):

          urls.append(f'{url_head}?p={page}')

        if not os.path.exists(f"bydaily/{tdate}/"):
          os.makedirs(f"bydaily/{tdate}/")

        threads = []

        for pic_url in urls:

            t = Thread(target=page_pic,
                args=(pic_url,)
                )

            threads.append(t)

        for thr in threads:
            thr.start()

        for thr in threads:
            thr.join()

    except Exception as e:
        print(e)    

def page_pic(page_url):
    """
        每页图片下载
    """
    try:

        res = requests.get(page_url, stream=True) #(1)
        soup = BeautifulSoup(res.text,features="html.parser")

        pic_urls = soup.select(".container .item .card img")

        threads = []

        for pic in pic_urls:

            t = Thread(target=download_from_url,
                args=(pic.get("src"),pic.get("src").split("/")[-1])
                )

            threads.append(t)

        for thr in threads:
            thr.start()

        for thr in threads:
            thr.join()

    except Exception as e:
        print(e)    


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
        print(e)



def download_from_url(url, dst):

    dst = f"bydaily/{tdate}/{dst}"

    response = requests.get(url, stream=True) #(1)
    
    file_size = int(response.headers['content-length']) #(2)

    if os.path.exists(dst):
        
        first_byte = os.path.getsize(dst) #(3)
    else:
        
        first_byte = 0

    if first_byte >= file_size: #(4)
        
        return file_size

    header = {"Range": f"bytes={first_byte}-{file_size}"} 
    # pbar = tqdm(
    #     total=file_size, initial=first_byte,
    #     unit='B', unit_scale=True, desc=dst)
    req = requests.get(url, headers=header, stream=True) #(5)

    with(open(dst, 'ab')) as f:

        for chunk in req.iter_content(chunk_size=100): #(6)

            if chunk:

                f.write(chunk)
                # pbar.update(1024)
    print(f"Pitture {dst} download finished!, return status code : {req.status_code}")
    # pbar.close()
    return file_size

url_head = "https://bing.ioliu.cn/"

all_pic(url_head)