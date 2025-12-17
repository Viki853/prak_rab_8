start_kolvo = int(input('Введите стартовое количество организмов: '))
srednesut_uvel = int(input('Введите среднесуточное увеличение (в процентах): '))
kolvo_dnei = int(input('Ввидите количество дней для размножения: '))

current=start_kolvo
print('№ Дня           Размер популяции')

for day in range(1,kolvo_dnei+1):
    print(f'{day}                     {current:.1f}')
    current = current + current*srednesut_uvel/100