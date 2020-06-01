# date: 30.05.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-2 / Python @GeekBrains
# HomeWork 2.2 (hw-2.1.py, hm-2.2.py, ..., hw-2.6.py)

#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

elem_count = int(input("Введите количество элементов списка:  "))
lst = []
i = 0
elem = 0
while i < elem_count:
    lst.append(input(f"Введите {i+1}-е значение списка:  "))
    i += 1
for i in range(1, len(lst), 2):
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
print(lst)
