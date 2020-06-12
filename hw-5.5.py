'''
Vers. 1
HomeWork 5.5 (hw-5.1.py, hm-5.2.py, ..., hw-5.7.py)

5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

'''

filename = 'text_5.txt'

def summ():
    try:
        with open(filename, 'w+', encoding='utf-8') as f:
            line = input('Введите числа через пробел:   ')
            f.writelines(line)
            numb = line.split()
            print(sum(map(float, numb)))
    except IOError:
        print('Error. Невозможно создать файл')
    except ValueError:
        print('Вы ввели недопустимый формат. Необходимо вводить только числа!')
summ()