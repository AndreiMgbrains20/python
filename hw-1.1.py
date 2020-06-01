# date: 29.05.2020 / Version 2
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-1 / Python @GeekBrains
# HomeWork 1.1 (hw-1.1.py, hm-1.2.py, ..., hw-1.6.py)

print('___ Задание № 1 ___________')
# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 3
print(a, "тип значения", type(a))

b = 3.0
print(b, "тип значения", type(b))

c = complex(3, 2)
print(f"{c} тип значения {type(c)}, где {c.real} реальное зн-е и {c.imag} комплексное зн-е")

text = "'Это мое первое задание в Python'"
print(f"{text} тип значения {type(text)}")
int1 = int(input("Введите любое число: "))
int2 = int(input("Введите любое второе число: "))
print(f"Вы ввели числа {int1} и {int2} и их сумма равна {int1 + int2}")
word = input("Введите любой текст: ")
print(f"Ваш текст - {word}")
# дополнил
