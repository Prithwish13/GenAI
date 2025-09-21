import asyncio
import time

async def brew(name):
    print(f"Brewing {name}.....")
    await asyncio.sleep(4)
    print(f"{name} is ready")
    
async def main():
    await asyncio.gather(
        brew("Masala Tea"),
        brew("Green Tea"),
        brew("Milk Tea")
    )
    
asyncio.run(main())