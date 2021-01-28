import logging
import asyncio
from loguru import logger
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
from time import sleep


def foo():
    logger.info("foo_sync started")
    sleep(0.5)
    logger.info("foo_sync finished")

def bar():
    logger.info("bar_sync started")
    sleep(0.5)
    logger.info("bar_sync finished")

def run_sync():
    logger.info("Start sync")
    foo()
    bar()

async def foo():
    logger.info("async foo_sync started")
    await asyncio.sleep(0.5)
    logger.info("async foo_sync finished")

async def bar():
    logger.info("async bar_sync started")
    await asyncio.sleep(0.5)
    logger.info("async bar_sync finished")

async def run_async():
    logger.info("Start async")
    await foo()
    await bar()

def run_main_async():
    logger.info("Starting main")
    coros = [
        foo(),
        bar(),
    ]
    fut = asyncio.wait(coros)
    asyncio.run(fut)
    logger.info("Finishing main")


if __name__ == "__main__":
    run_main_async()
