a = input('Ваше число:')
sum = 0
while a != 'sum':
    num = int(a)
    sum += num
    a = input('Ваше число:')
print('Сумма введенных чисел:', sum)
