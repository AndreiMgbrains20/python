"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""


from functools import reduce

lst = [el for el in range(100, 1001) if el % 2 == 0]
#lst = [2, -3, 1.10133,]
print(f'  Список случайных чисел, сформерованный random от 100 до 1000, включая число 1000 :\n  {lst}')

lst_prod = lambda prev_el, el: prev_el * el
prod = round(reduce(lst_prod, lst),2)
print(f'  1й вариант произведение чисел с lambda :\n  {prod}   \n  Overflow by a big list if you want convert to float()...')
#print(f'  Произведение чисел равно = {prod:.3e}')

def my_func(prev_el, el):
    return prev_el * el

print('  2й вариант решения с my_func :\n ', reduce(my_func, lst))