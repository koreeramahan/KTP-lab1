a=float(input('Введите число a:\n'))
b=float(input('Введите число b:\n'))
c=float(input('Введите число с:\n'))
d=float(input('Введите число d:\n'))
f=float(input('Введите число f:\n'))
if a==0:
    print('Ошибка, нельзя делить на 0')
else:
    vyr=abs(a-b*c*(d**3)+((c**5)-(a**2))/a+(f**3)*(a-213))
    print(vyr)
