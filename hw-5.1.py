'''
date: 10.06.2020 / Version 1
author: AndreiM
https://github.com/AndreiMgbrains20/python/
lesson-5 / Python @GeekBrains
HomeWork 5.1 (hw-5.1.py, hm-5.2.py, ..., hw-5.7.py)


1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

filename = 'text_1.txt'

my_text = []
print('Введите текст и нажмите Enter. Для выхода нажмите Enter, оставив пуcтую строку')
while True:
    try:
        line = input('Введите текст (новую строку):  ')
        if line == '':
            print(my_text)
            exit()
        else:
            newline = line + '\n'
            my_text.append(newline)
                                    #r+	Для чтения и записи
                                    #w+ Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
                                    #a+ Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем.
            with open(filename, 'a+', encoding='utf-8') as f:
                f.writelines(my_text)
                #f.close()   уже выполняется автоматически при использовании 'with'

    except FileNotFoundError:
        print(f'Error. Невозможно открыть или создать файл')
