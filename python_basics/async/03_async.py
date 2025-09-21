import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url, ssl=False) as response:
        print(f"Fetched {url} with {response.status}") 
        
        
async def main():
    urls = ["https://httpbin.org/delay/4"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks) # this * is unpacking the list of tasks
        
        
asyncio.run(main())