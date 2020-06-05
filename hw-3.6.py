# date: 04.06.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-3 / Python @GeekBrains
# HomeWork 3.6 (hw-3.1.py, hm-3.2.py, ..., hw-3.6.py)

#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(text):
    lst = []
    for i in range(len(text)):
        lst.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(lst)
print(int_func(input('#Вариант 1-й \nВведите строку с текстом:    ').split()))


def int_func2(text):
    return text.title()

print(int_func2(input('#Вариант 2-й \nВведите строку с текстом:    ')))


