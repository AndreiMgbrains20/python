# date: 30.05.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-2 / Python @GeekBrains
# HomeWork 2.3 (hw-2.1.py, hm-2.2.py, ..., hw-2.6.py)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input("Введите месяц в виде целого числа:  "))
seas_lst = ['зима', 'весна', 'лето', 'осень']
seas_dict = {1: 'зиме',
             2: 'весне',
             3: 'лету',
             4: 'осени'}
month_lst = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if month == 1 or month == 12 or month == 2:
    print(f"Месяц {month_lst[month - 1]} относится к {seas_dict.get(1)} (dict)")
    print(f"{seas_lst[0]} (list)")
elif month == 3 or month == 4 or month ==5:
    print(f"Месяц {month_lst[month - 1]} относится к {seas_dict.get(2)} (dict)")
    print(f"{seas_lst[1]} (list)")
elif month == 6 or month == 7 or month == 8:
    print(f"Месяц {month_lst[month - 1]} относится к {seas_dict.get(3)} (dict)")
    print(f"{seas_lst[2]} (list)")
elif month == 9 or month == 10 or month == 11:
    print(f"Месяц {month_lst[month - 1]} относится к {seas_dict.get(4)} (dict)")
    print(f"{seas_lst[3]} (list)")
else:
    print("Такого месяца не существует. Введите целое число от 1-12")
