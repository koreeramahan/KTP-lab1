a=[10, 2, "a", 8, 39, 19, 11, '100', 56]
a1 = list(filter(lambda x: int(x) % 2, a))
if a1:
    print ('Нечетные числа: ')
    for i in a1: print(i)
else:
    print('Нет нечетных чисел')
