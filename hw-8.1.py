'''
date: 20.06.2020 / Version 1
author: AndreiM
https://github.com/AndreiMgbrains20/python/
lesson-8 / Python @GeekBrains
HomeWork 8.1 (hw-8.1.py, ..., hw-8.7.py)


1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

'''

from datetime import datetime

class DataClass:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        try:
            #day_pruf = datetime(2020, 2, 30)
            if 1 <= day <= 31:
                if 1 <= month <= 12:
                    if 2020 >= year >= 0:
                        return f'Все верно'
                    else:
                        return f'Неправильный год'
                else:
                    return f'Неправильный месяц'
            else:
                return f'Неправильный день'
        except ValueError:
            return (f'Такого дня не существует в этом месяце в указанном году')

    def __str__(self):
        return f'Текущая дата {DataClass.extract(self.day_month_year)}'

now = datetime.now()
print(now.strftime('form datetime.now() --> %d - %m - %Y'))
today = DataClass('22 - 6 - 2020')
print(today)
print('valid (11, 11, 2022) : ', DataClass.valid(11, 11, 2022))
print('valid (11, 13, 2020) : ', DataClass.valid(11, 13, 2020))
print('valid (33, 12, 2020) : ', DataClass.valid(33, 12, 2020))
print('valid (30, 2, 2020) : ', DataClass.valid(20, 2, 2020))
print('valid today (21, 6, 2020) : ', today.valid(21, 6, 2020))
print('DataClass extract (12 - 10 - 2018) : ', DataClass.extract('12 - 10 - 2018'))
print('today extract', today.extract('11 - 11 - 2020'))