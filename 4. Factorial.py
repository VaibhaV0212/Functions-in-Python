def fact(a):
    b = 1
    while a >= 1:
        b *= a
        a -= 1
    return b


#fact(4)
for i in range(1, 11):
    print('Factorial of {} is {}'.format(i, fact(i)))
