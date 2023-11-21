import time
import asyncio
import httpx


async def download(current):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail{current}'
    async with httpx.AsyncClient() as client:
        result = await client.get(url)
        if result.status_code == 200:
            my_res = result.json()
            print(my_res['drinks'], current)
        else:
            print(result.status_code)
        print(f'Результат №{current}')

def print_info(info, current):
    # print(f'Имя {info['first_name]}, {info['last_name]}, E-mail: {info['email']}')
    print(info[current]['strDrink'])
async def main():
    user_count = int(input('Cewie ?swe '))

    current = 0
    while current < user_count:
        task = asyncio.create_task(download(current))
        await task
        current += 1
    print('Done')


asyncio.run(main())
