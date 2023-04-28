"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0
Process finished with exit code 0
"""


def my_div(a, b):
    try:
        a // b
    except ZeroDivisionError:
        return print('На ноль делить нельзя')
    return print(a // b)


d = float(input('Введите первое число: '))
e = float(input('Введите второе число: '))
my_div(d, e)
