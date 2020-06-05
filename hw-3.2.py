# date: 04.06.2020 / Version 1
# author: AndreiM
# https://github.com/AndreiMgbrains20/python/
# lesson-3 / Python @GeekBrains
# HomeWork 3.2 (hw-3.1.py, hm-3.2.py, ..., hw-3.6.py)

#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_args(name, surname, byear, lcity, email, phone):
    print('\nДанные пользователя:  1. имя | 2. фамилия | 3. год рождения | 4. город проживания | 5. email | 6. тел.')
    return '  '.join([name, surname, byear, lcity, email, phone])

print(user_args(name=input('Введите имя:  '),
                surname=input('фамилию:  '),
                byear=input('год рождения:  '),
                lcity=input('город проживания:  '),
                email=input('email @:  '),
                phone=input('телефон:  +')))

