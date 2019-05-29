# Сформировать из введенного числа обратное по
# порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

numb = int(input("Введи число: "))

i = 1
k = 1
new = 0

while i != 0:

    i = numb % 10
    numb = (numb - numb % 10) / 10

    if i != 0 and numb >= 0:
        new = new * k + i

    if i == 0 and numb > 0:
        new = new * k
        i = 1
    k = 10

print(int(new))
