# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input("Введи кол-во элементов n= "))
result = 1
summ = 1

for i in range(0, n-1):

    result = result/2 * (-1 ** n)
    summ = summ + result

print(summ)
