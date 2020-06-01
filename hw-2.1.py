# date: 30.05.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-2 / Python @GeekBrains
# HomeWork 2.1 (hw-2.1.py, hm-2.2.py, ..., hw-2.6.py)

#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

lst = ["Hello world", object, -3, 7j, 2+6j, True, 100.5]
for i in lst:
    print(f"{i} относится к {type(i)}")

