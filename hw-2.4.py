# date: 30.05.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-2 / Python @GeekBrains
# HomeWork 2.4 (hw-2.1.py, hm-2.2.py, ..., hw-2.6.py)

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

intxt = input("Введите строку. Новая строка - через пробел:  ")
lst = ' '.join(intxt.split())  #Если задано случайно более 1 пробела
txt = []
num = 1
for elem in range(lst.count(' ') + 1):
    txt = lst.split()
    if len(str(txt)) <= 10:
        print(f" {num}. {txt[elem]}")
        num += 1
    else:
        print(f"{num}. {txt[elem] [0:10]}")
        num += 1