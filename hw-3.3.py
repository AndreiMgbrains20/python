# date: 04.06.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-3 / Python @GeekBrains
# HomeWork 3.3 (hw-3.1.py, hm-3.2.py, ..., hw-3.6.py)

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    if x >= y and y >= z:
        return x + y
    elif x > y and x < z:
        return x + z
    else:
        return y + z

print(my_func(float(input('# 1-й вариант my_func\nВведите 1-е число: ')), float(input('Введите 2-е число: ')), float(input("Введите 3-е число: "))))


def my_func1(x, y, z):
    sqc = [x, y, z]
    sqc.remove(min(x, y, z))
    print(f'Сумма чисел {min(sqc)} и {max(sqc)} = {sum(sqc)}')
my_func1(float(input('\n# 2-й вариант с min() \nВведите 1-е число: ')), float(input('Введите 2-е число: ')), float(input("Введите 3-е число: ")))