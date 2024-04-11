import asyncio
import aiohttp
import time
urls = []


async def fetch(session, url):
    async with session.get(url) as response:
        return str(await response.text())


tasks=[]
async def main():
    for i in range(50):
        urls.append('https://www.google.com')
        urls.append('https://en.wikipedia.org/wiki/Terracotta')
    timeStart = time.time()
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)
    timeFinish = time.time()
    timeElapsed = timeFinish - timeStart
    print(timeElapsed)


asyncio.get_event_loop().run_until_complete(main())