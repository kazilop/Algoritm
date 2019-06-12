# Рыбка Артем

# Проанализировать скорость и сложность одного любого алгоритма из разработанных в
# рамках домашнего задания первых трех уроков.

import timeit
import cProfile

mycode = """
def my_sum(n):  # Сумма n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    result = 1
    summ = 1

    for i in range(0, n - 1):
        result = result / 2 * (-1 ** n)
        summ = summ + result
    return summ
"""

# 100 loops, best of 3: 34.3 usec per loop - для 100
# 100 loops, best of 3: 369 usec per loop  - для 1000
# 100 loops, best of 3: 3.66 msec per loop - для 10000


my_code_two = """
def my_sum_two(n):
    i = 0
    array = [0 for _ in range(n)]
    array[0] = 1
    while i < n - 1:
        array[i + 1] = array[i] * (-0.5)
        i += 1

    return sum(array)
   """
n1 = 100000
n2 = 1000000
n3 = 10000000

print("Функция my_sum(n)")
print(f"Для {n1} время  = {timeit.timeit(stmt=mycode, number=n1):.5f}")
print(f"Для {n2} время  = {timeit.timeit(stmt=mycode, number=n2):.5f}")
print(f"Для {n3} время  = {timeit.timeit(stmt=mycode, number=n3):.5f}")

print("* " * 20)

print("Функция my_sum_two(n)")
print(f"Для {n1} время  = {timeit.timeit(stmt=my_code_two, number=n1):.5f}")
print(f"Для {n2} время  = {timeit.timeit(stmt=my_code_two, number=n2):.5f}")
print(f"Для {n3} время  = {timeit.timeit(stmt=my_code_two, number=n3):.5f}")


# cProfile.run('my_sum(1000000)')
# cProfile.run('my_sum_two(10000000)')

# ВЫВОД
# Обе функции получились линейно-зависимые O(n)
# Скорость работы, примерно, одинаковая

# cProfile работает, только нужно достать из тройных ковычек функции




