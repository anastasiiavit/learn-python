#Програма приймає два числа та повідомяляє яке за них більше та на скільки (7 більше 5 на 2)

x= int(input("Введіть перше число:"))
y= int(input("Введіть друге число:"))
if x>y:
    print(x, "більше", y, "на", x-y)
elif y>x:
    print(y, "більше", x, "на", y-x)
