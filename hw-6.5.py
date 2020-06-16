'''
Version 1
HomeWork 6.5 (hw-6.1.py, hw-6.2.py, ..., hw-6.5.py)

5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''

class Stationary:
    def __init__(self, title):
        self.title = title  #attribute

    def draw(self):  #methode
        return
        # return 'Запуск отрисовки'
        # return self.title

class Pen(Stationary):  #child class
    def draw(self):
        return f'Вы выбрали {self.title}. Запуск отрисовки ручкой...'

class Pencil(Stationary):
    def draw(self):
        return f'Вы выбрали {self.title}. Запуск отрисовки карандашом...'

class Handle(Stationary):
    def draw(self):
        return f'Вы выбрали {self.title}. Запуск отрисовки маркером...'


pen = Pen('Pen (ручку)')
pencil = Pencil('Pencil (карандаш)')
handle = Handle('Handle (маркер)')
print(pen.draw())
print(pencil.draw())
print(handle.draw())