print('Введите 10 чисел последовательно (каждое на новой строке): ')

all_even = True

for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        all_even = False

if all_even:
    print('YES. Все числа четные')
else:
    print('NO. Не все числа четные')