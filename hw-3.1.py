# date: 04.06.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-3 / Python @GeekBrains
# HomeWork 3.1 (hw-3.1.py, hm-3.2.py, ..., hw-3.6.py)

#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func(x):
    while True:
        try:
            text = '{} {} '.format('Введите число', x, '>>>')
            a = float(input(text))
            return a
        except ValueError:
            print('Введите, пожалуйста, число!')

a = div_func('a в числителе:  ')
b = div_func('b в знаминателе, не равное 0:  ')

try:
    res = a / b
    print(f'Деление {a} / {b} = {round(res, 4)}')

except ZeroDivisionError:
    print('Деление на ноль запрещено. Задайте любое число для b не равное 0 !')