import random

chislo = random.randint(1,10) #Случайное число от 1 до 10
attempts = 0

for i in  range (1,4):
    popitka = int(input('Угадайте загаданное число: '))
    attempts += 1
    if popitka==chislo:
        print (f'Угадали! Было загадано число: {chislo}')
        break
    elif popitka<chislo:
        print('Неправильно! Число больше вашего.')
    else:
        print ('Неправильно! Число меньше вашего')

else:
    print('')
    print(f'Не угадали, было загадано число: {chislo}')