#Написати програму, яка приймає число та відрізає від нього останню цифру.
# Наприклад: 10 -> 1, 100 -> 10, 25143 -> 2514

str = input("Enter the number : ")

l = len(str)

Final_string = ""

for i in range(0,l-1):
    Final_string = Final_string + str[i]

print(Final_string)



