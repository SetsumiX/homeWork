import math
import threading
from random import randint

file_path = input("Путь для создания файла >>> ")
with open(file_path, "w") as file: # Генерация и запись рандомных чисел
    nums = [randint(1, 20) for _ in range(10)]

    for num in nums:
        file.write(f"{num}\n")

def is_simple(num): # Проверка на простое число (скопировано с инета. p.s. Зачем создавать велосипед, если он уже создан)
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def write_simple_nums(path): # Проверка из файла на простоту чисел, а так же запись в новый текстовый файл
    simp_nums = []

    with open(path, "r") as file:
        for num in file:
            if is_simple(int(num)):
                simp_nums.append(int(num))

    print(simp_nums)

    with open("simpleNums.txt", "w") as file:
        for num in simp_nums:
            file.write(f"{num}\n")

def write_factorial_nums(path): # Запись уже произведённых математических изменений чисел(возведение факториала каждого числа)
    nums = []

    with open(path, "r") as file:
        for num in file:
            nums.append(int(num))

    with open("numsFacrorial.txt", "w") as file:
        for num in nums:
            file.write(f"{math.factorial(num)}\n")

thread_simple = threading.Thread(target=write_simple_nums, args=(file_path,))
thread_factorial = threading.Thread(target=write_factorial_nums, args=(file_path,))

thread_simple.start()
thread_factorial.start()

thread_simple.join()
thread_factorial.join()