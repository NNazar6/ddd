import asyncio

async def my_sleep():
    print('sleep start')
    await asyncio.sleep(3)
    print('sleep end')

async def my_work():
    print('work start')
    await asyncio.sleep(5)
    d = 2 + 3
    print('work end')

async def main():
    task1 = asyncio.create_task(my_sleep())
    task2 = asyncio.create_task(my_work())
    print('res start')
    await task1
    print('rest end')
    await task2

asyncio.run(main())