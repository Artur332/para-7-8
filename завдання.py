try:
    number1 = float(input('введіть число'))
    number2 = float(input('введіть число'))

    result = number1 / number2



except ZeroDivisionError:
    print('Не можна ділити на ноль')