# Рыбка Артем

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000

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

print(main_data)
print(f"Minimal index= {min_item_index}, Maximal index= {max_item_index}")

main_data[min_item_index], main_data[max_item_index] = main_data[max_item_index], main_data[min_item_index]
print(main_data)
