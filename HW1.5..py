#Написати програму, яка приймає число та повідомляє яка в ньому остання цифра.
# Наприклад: 10 -> 0, 100 -> 0, 25143 -> 3

n = int(input('Input the number:'))
a = n % 10
print( a)