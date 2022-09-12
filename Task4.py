#Програма приймає два числа та змінює їх місцями (a стає b, b стає a).
# Бонус: зробити це, не використовуючи третьої змінної

x=int(input('Input first number:'))
y=int(input('Input second number:'))
x,y = y,x
print(x)
print(y)