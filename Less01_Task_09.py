#  Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введи a = "))
b = int(input("Введи b = "))
c = int(input("Введи c = "))

if a > b:
    if a > c:
        if c > b:
            print(f"Среднее c = {c}")
        else:
            print(f"Среднее b = {b}")
    else:
        print(f"Среднее a = {a}")

else:
    if a > c:
        print(f"Среднее a = {a}")
    else:
        if c > b:
            print(f"Среднее b = {b}")
        else:
            print(f"Среднее c = {c}")
