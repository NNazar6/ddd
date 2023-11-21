import time
import asyncio


async def count(counter):
    print(f'Количество записей в списке {len(counter)}')
    while True:
        await asyncio.sleep(2)
        counter.append(1)
async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'Прошла 1 секунда. Элементов в списке {len(counter)}')
async def print_every_5sec():
    while True:
        await asyncio.sleep(5)
        print(f'Прошлo 5 секунд.')
async  def print_every_10sec():
    while True:
        await asyncio.sleep(10)
        print(f'Прошлo 10 секунд.')
async def main():
    counter = []
    task1 = asyncio.create_task(count(counter))
    task2 = asyncio.create_task(print_every_sec(counter))
    task3 = asyncio.create_task(print_every_5sec())
    task4 = asyncio.create_task(print_every_10sec())
    await task1
    await task2
    await task3
    await task4

asyncio.run(main())
# async def main():
#     counter = list()
#     count(counter)
#     print_every_sec(counter)
#
# main()