import math

while True:
    print("""
1. Конвертувати градуси в радіани.
2. Конвертувати радіани в градуси.
    """)
    user_input = input('Виберіть яку операцію бажаєте зробити: ')

    if user_input == '1':
        x = int(input('Введіть значення у градусах:'))

        y = math.radians(x)

        print(y, 'радіана')
    elif user_input == '2':
            a= int(input('Введіть значення у радіанах:'))
            b = math.degrees(a)
            print(b, 'градусів')
    else:
        print('Будь ласка, зробіть вибір - введіть 1 або 2')







