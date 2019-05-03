list=[10, 2, 3, 8, 39, 19, 11, 100, 56]
print(len(list))
a=len(list)
if a%2==1:
        d=((a+1)/2)-1
        b=list[int(d)]
        print('Посередине находится ',b)
else:
	b=list[int(a/2-1)]
	c=list[int(a/2)]
	print('Посередине находятся два элемента: ',b,' и ',c)
