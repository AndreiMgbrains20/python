"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""
'''
E.g. for script
Win-CMD 'python' or Linux-TERMINAL 'python3'
<directory>...$  python3 hw-4.6.py 3 10 6
output ...
'''

from sys import argv
from itertools import cycle, count
from random import*

script_iteration, start_number, stop_number, iteration = argv
argv_ = [int(x) for x in argv[1:]]
lst = [randint(1, 9) for i in range(4)]

print(f'  Название скрипта  : ', script_iteration)
print(f'  -----------------------------------------------')
print(f'  Начальное стартовое число           :  ', argv_[0])
print(f'  Конечное число для завершения цикла :  ', argv_[1])
print(f'  Введеное количество итераций        :  ', argv_[2])
print(f'  Случайные числа из random() :  ', lst)
print(f'  -----------------------------------------------')
print(f'  Итератор, генерирующий целые числа начиная с {argv_[0]} до {argv_[1]}:')

def count_func(a, b):
    for el in count(a):
        if el > b:
            break
        else:
            print('        ', el)

def cycle_func(my_lst, d):
    i = 0
    iter = cycle(my_lst)
    while i < d:
        print(f'      {next(iter)}     итератор, повторяющий случайные числа')
        i+=1

count_func(a=argv_[0], b=argv_[1])
cycle_func(my_lst=lst, d=argv_[2])