# Рыбка Артем

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_NUMBER = 2
MAX_NUMBER = 99

my_list = {a: 0 for a in range(2, 10)}

for i in range(MIN_NUMBER, MAX_NUMBER + 1):
    for n in range(2, 10):
        if i % n == 0:
            temp = {n: my_list.get(n)+1}
            my_list.update(temp)

print(my_list)
