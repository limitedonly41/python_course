import vk_api

vk_session = vk_api.VkApi('+79XXXXXXXXXX', 'password')
vk_session.auth()
vk = vk_session.get_api()





















# import asyncio
# from time import time, sleep
#
# from random import randint
#
# start = time()
#
#
# async def scrape(a):
#     await asyncio.sleep(1)
#
#     print(randint(1,a))
#
# def scrape_sync(a):
#     sleep(1)
#
#     print(randint(1,a))
#
# def start_async():
#     coros=[
#         scrape(5),
#         scrape(15),
#         scrape(25),
#         scrape(35),
#     ]
#     fut = asyncio.wait(coros)
#     asyncio.run(fut)
#
# def start_sync():
#     scrape_sync(5)
#     scrape_sync(15)
#     scrape_sync(25)
#     scrape_sync(35)
#
# if __name__ == '__main__':
#     start_async()
#     end_async = time()-start
#     end = time()
#     start_sync()
#     print(end_async)
#     print(time() - end)