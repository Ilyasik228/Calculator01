import logging

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Что сделать с данными операторами?")
print("+ Сложить, - Вычесть, * Умножить, / Поделить")
opera = input("Требуемая операция: ")

if opera == "+":
    print("Сумма чисел равна: ", num1 + num2)
elif opera == "-":
    print("Разность чисел равна: ", num1 - num2)
elif opera == "*":
    try:
        if num2 == 0:
            logging.error("Не умножайте на ноль")
            raise ZeroDivisionError("Умножение на ноль")
        print("Умножение чисел равно:", num1 * num2)
    except ZeroDivisionError:
        print("Ошибка")
elif opera == "/":
    try:
        if num2 == 0:
            logging.error("Не делите на ноль")
            raise ZeroDivisionError("Деление на ноль")
        print("Деление чисел равно:", num1 / num2)
    except ZeroDivisionError:
        print("Ошибка")
else:
    print("Не ломайте мой код, пожалуйста")