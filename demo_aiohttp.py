import asyncio
from dataclasses import dataclass
from asyncio import CancelledError
from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    ip_field: str

SERVICES = [
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
]

async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()

async def fetch_ip(service: Service) -> str:
    """
    :param service:
    :return:
    """
    my_ip = "Not found"

    async with ClientSession() as session:
        result = await fetch(session, service.url)

    logger.info(f"Got result for {service.name}, result {result}")
    my_ip = result[service.ip_field]
    return my_ip

async def get_my_ip():
    coros = [fetch_ip(s) for s in SERVICES]
    done, pending = await asyncio.wait(
        coros,
        timeout=3,
        return_when=asyncio.FIRST_COMPLETED,
    )
    print(done)
    print(pending)
    for c in pending:
        logger.info("Cancelling task")
        c.cancel()
    for fut in done:
        my_ip = fut.result()
        break
    else:
        logger.warning("No ip")
    logger.info(f"Got my ip {my_ip}")

    # res = asyncio.run(coro)
    # print(res)

def run_main():
    asyncio.run(get_my_ip())

if __name__ == '__main__':
    run_main()