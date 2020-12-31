def getResult(i):
    if i == 0:
        return 0
    elif i == 1 or i == 2:
        return 9
    else:
        return getResult(i - 1) + getResult(i - 2) + getResult(i - 3)

n = int(input('n= '))
print('x{0} = {1}'.format(n, getResult(n)))
