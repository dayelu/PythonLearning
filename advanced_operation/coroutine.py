import time
import asyncio
import aiohttp
import requests

async def func():			# 协程函数: 定义形式为 async def 的函数;
	
	start = time.time()
	# print('hello')

	tasks = []

	for x in range(1,4):
		tasks.append(asyncio.create_task(funa(x*2)))

	for task in tasks:
		await task

	# task1 = asyncio.create_task(funa(3))
	# task2 = asyncio.create_task(funa(5))
	# task3 = asyncio.create_task(funa(6))
	# await funa()			# await语法来挂起自身的协程，并等待另一个协程完成直到返回结果

	# await task1
	# await task2
	# await task3

	# await asyncio.sleep(1)
	# asyncio.sleep(1)	#RuntimeWarning: coroutine 'sleep' was never awaited
	# print('world')
	print('finished in {} s'.format(time.time() - start))

async def funa(sec):
	await asyncio.sleep(sec)


async def main(url):

	async with aiohttp.ClientSession() as session:
	    async with session.get(url) as resp:
	        print(resp.status)
	        print(await resp.text())






def seizes(url):
	response = requests.get(url)
	print(response.text)


asyncio.run(func())


url = 'https://aiohttp.readthedocs.io/en/stable/client_quickstart.html'

seizes(url)

asyncio.run(main(url))