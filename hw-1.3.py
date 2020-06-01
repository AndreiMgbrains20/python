# date: 29.05.2020 / Version 2
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-1 / Python @GeekBrains
# HomeWork 1.3 (hw-1.1.py, hm-1.2.py, ..., hw-1.6.py)


print('___ Задание № 3 ___________')
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input("Введите число, например 3: ")
print(f"{n}+{n+n}+{n+n+n} = {int(n) + int(n+n) + int(n+n+n)}")
