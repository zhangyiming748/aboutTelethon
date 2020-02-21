import asyncio
async def simple_async():
    print("first")
    await asyncio.sleep(1)
    print("send")
asyncio.run(simple_async())