import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"checking {item} in store")
    time.sleep(3) # this is a blocking operation
    return f"{item} stock: 42"


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "cheese")
        print(result)
        
asyncio.run(main())