import time
import asyncio


async def makeCoffee():
    print('start toastBrew')
    await asyncio.sleep(2)
    print('end toastBrew')
async def toastBrew():
    print('start toastBrew')
    await asyncio.sleep(2)
    print('end toastBrew')

async def main():
    start = time.time()
    # work = asyncio.gather(makeCoffee(), toastBrew())
    # res_coffee, res_toast = await work
    end = time.time()

    task1 = asyncio.create_task(makeCoffee())
    task2 = asyncio.create_task(toastBrew())
    res_coffee = await task1
    res_toast = await task2
    print(res_coffee)
    print(res_toast)
    print(f'времени прошло{end-start:.2f} минут')

if __name__ == '__main__':
    asyncio.run(main())