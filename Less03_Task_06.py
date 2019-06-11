# Рыбка Артем

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

min_item_index = 0
max_item_index = 0

main_data = [random.randint(MIN_ITEM, MAX_ITEM) for __ in range(SIZE)]
i = 0
temp_min = main_data[0]
temp_max = main_data[0]

while i < len(main_data):
    if temp_max > main_data[i]:
        max_item_index = i
        temp_max = main_data[i]
    if temp_min < main_data[i]:
        min_item_index = i
        temp_min = main_data[i]
    i += 1

if max_item_index > min_item_index:
    start = min_item_index
    end = max_item_index
else:
    start = max_item_index
    end = min_item_index

summ = 0
for i in range(start + 1, end):
    summ = summ + main_data[i]
print(main_data)
print(f"Minimal index= {min_item_index}, Maximal index= {max_item_index}")
print(f"Сумма = {summ}")
