import asyncio
from random import randint

async def nums_create(num):
    await asyncio.sleep(2)

    if num == 0:
        print("Чисел нет")
        return None

    arr = [randint(1, 100) for _ in range(num)]
    print("Список чисел -", arr)
    return arr

async def _sum(arr):
    print(f"Сумма чисел ровна, {sum(arr)}")
    return sum(arr)

async def aver(arr):
    print(f"Среднее арифметическое чисел, {sum(arr)/len(arr)}")
    return sum(arr)/len(arr)


async def main():
    num = int(input("Введите какое количество чисел сгенерировать >>> "))
    arr = await nums_create(num)
    if arr == None:
        print("Нет чисел для обработки")
        return None
    task_1 = asyncio.create_task(_sum(arr))
    task_2 = asyncio.create_task(aver(arr))
    await task_1
    await task_2

asyncio.run(main())