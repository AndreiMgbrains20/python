# date: 29.05.2020 / Version 2
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-1 / Python @GeekBrains
# HomeWork 1.4 (hw-1.1.py, hm-1.2.py, ..., hw-1.6.py)


print('___ Задание № 4 ___________')
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
num_in = int(input("Введите целлое цисло, состоящие из более чем 2 чисел, например 359:  "))
digit_max = 0
num = num_in

while num > 0:
    digit = num % 10
    if digit > digit_max:
        digit_max = digit
        if digit_max == 9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num_in} является {digit_max}")
