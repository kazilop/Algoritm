# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь...

a = int(input("Введи трехзначное число = "))

print(f"Сумма чисел = {a // 100 + (a // 10) % 10 + a % 10}")
print(f"Произведение чисел = {(a // 100) * ((a // 10) % 10) * (a % 10)}")
