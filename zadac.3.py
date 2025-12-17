n = int(input('Введите целое натуральное число: '))
s=0

for i in range (1,n+1):
    if i%2==1:
        s+=i
    else:
        s -=i
print (f'Значение знакопеременной суммы: {s}')