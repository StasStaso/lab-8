def getMax(x,y):

    if x > y:
        return  x
    else:
        return  y

x = int(input('x= '))
y = int(input('y= '))
z = int(input('z= '))

result = round((getMax(x, z) + getMax(x + y, x * y)) / getMax(x + y, x * y) ** 2,3)

print('Результат: {0}'.format(result))
