# Рыбка Артем

# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import cProfile
import timeit

def sieve(n):
    lst = [2, 3]
    m = len(lst)
    while len(lst) < n:
        lst = []
        a = [i for i in range(m + 1)]
        a[1] = 1

        i = 2
        while i <= m:
            if a[i] != 0:
                lst.append(a[i])
                for j in range(i, m + 1, i):
                    a[j] = 0
            i += 1
        m = m + 10

    return lst[n - 1]


def my_sieve(i):
    lst = []
    n = 1
    numb = 0
    while numb <= i:
        for j in range(2, n + 1):
            if n % j == 0 and n == j:
                lst.append(n)
                numb += 1
            if n % j == 0 and n != j:
                break

        n += 1
    return lst[i - 1]


# cProfile.run("sieve(1000)")
# 426047 function calls in 0.982 seconds

# cProfile.run("my_sieve(1000)")
# 1005 function calls in 0.537 seconds


func1 = """ 
def sieve(n):
    lst = [2, 3]
    m = len(lst)
    while len(lst) < n:
        lst = []
        a = [i for i in range(m + 1)]
        a[1] = 1

        i = 2
        while i <= m:
            if a[i] != 0:
                lst.append(a[i])
                for j in range(i, m + 1, i):
                    a[j] = 0
            i += 1
        m = m + 10

    return lst[n - 1]
"""


func2 = """"
def my_sieve(i):
    lst = []
    n = 1
    numb = 0
    while numb <= i:
        for j in range(2, n + 1):
            if n % j == 0 and n == j:
                lst.append(n)
                numb += 1
            if n % j == 0 and n != j:
                break

        n += 1
    return lst[i - 1]
"""
# numbs = 20

# print(" для проверки ")
# print(f"С помощью решета {sieve(numbs)} , скорость вычисления - {timeit.timeit(stmt=func1, number=numbs)}")
# # Не хочет через программу проверять вторую функцию. Только через терминал.
# #print(f"Обычный метод {my_sieve(numbs)}, скорость вычисления -  {timeit.timeit(stmt=func2, number=numbs)}")
# print(f"Обычный метод {my_sieve(numbs)}, скорость вычисления ")

#  РЕЗУЛЬТАТЫ

# sieve
# 100 loops, best of 3: 68.8 usec per loop - от n = 20
# 100 loops, best of 3: 377 usec per loop  - от n = 40
# 100 loops, best of 3: 1.82 msec per loop  - от n = 80
# 100 loops, best of 3: 43.8 msec per loop   - от n = 300


# my_sieve
# 100 loops, best of 3: 84.4 usec per loop  - от n = 20
# 100 loops, best of 3: 327 usec per loop   - от n = 40
# 100 loops, best of 3: 1.41 msec per loop  - от n = 80
# 100 loops, best of 3: 25.7 msec per loop  - от n = 300

# ВЫВОДЫ
# Из-за того, что начальная длина массива неизвестна, приходится функцию с решетом использовать
# много раз подряд. ( Либо я не смог правильно оптимизировать решето)
# В данной реализации класический вариант поиска простых чисел
# на длинной дистанции выигрывает по времени



