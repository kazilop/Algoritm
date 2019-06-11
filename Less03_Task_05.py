# Рыбка Артем

# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 100

min_item_index = 0
max_item_index = 0

main_data = [random.randint(MIN_ITEM, MAX_ITEM) for __ in range(SIZE)]

print(main_data)
print("*" * 30)

numb = float("inf") * -1
for i, data in enumerate(main_data):
    if data > numb and data < 0:
        numb = data
        index = i

print(f"Максимальный отрицательный элемент {numb} c индексом {index}")