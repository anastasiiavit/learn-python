#Написати програму, що конвертує гривню в доллар (або навпаки, за бажанням, але вкажіть що сами обрали!)
# по заданому в программі курсу. Округліть до двох цифр після крапки.

Currencies = {"USD": 1.0, "UAH": 37.07}
x=int(input('Введіть суму у UAH:'))
y=37.05

print(round(x/y, 2),"USD")