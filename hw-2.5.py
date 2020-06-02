# date: 30.05.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-2 / Python @GeekBrains
# HomeWork 2.5 (hw-2.1.py, hm-2.2.py, ..., hw-2.6.py)

#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

#Version 2

lst = [7, 5, 3, 3, 2]
print("Набор натуральных чисел по условию: ", lst)
number = int(input("Введите число, например 3 или 8 или 1:   "))
c = lst.count(number)
for element in lst:
    if c > 0:
        i = lst.index(number)
        lst.insert(i+c, float(number)) #float для проверки
        break
    else:
        if number > element:
            j = lst.index(element)
            lst.insert(j, number)
            break
        elif number < lst[len(lst) - 1]:
            lst.append(number)
print(lst)
