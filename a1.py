import asyncio
import time


async def async_func(num):
    print(f'...start {num}')
    await asyncio.sleep(3)
    print(f'...end {num}')


async def main():
    taskA = asyncio.create_task(async_func('A'))
    taskB = asyncio.create_task(async_func('B'))
    taskC = asyncio.create_task(async_func('C'))

    await asyncio.wait([taskA, taskB, taskC])


if __name__ == '__main__':

    asyncio.run(main())