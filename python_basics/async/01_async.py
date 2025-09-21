import asyncio

async def brew_tea():
    print("Brewing tea...")
    await asyncio.sleep(2)  # Simulate time taken to brew tea
    print("Tea is ready!")
    
asyncio.run(brew_tea())