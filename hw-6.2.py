'''
Version 1
HomeWork 6.2 (hw-6.1.py, hw-6.2.py, ..., hw-6.5.py)

2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т

'''


class Road:
    def __init__(self, _length, _width):  # _private. Constructor.
        self.length = _length
        self.width = _width
        print(' Create obj. Road ...')

    def calc_weight(self):
        self.weigth = 25 #kg
        self.thickn = 5 #thikness high in cm!
        calc = self.length * self.width * self.weigth * self.thickn
        print(f' Для строительства дороги L-{self.length}м. и W-{self.weigth}м. при толщине асфальта в {self.thickn} см.'
              f'\n необходимо = {calc/1000} т. (масса асфальта)  т')

c = Road(5000, 20) #_length = 5000m, #_weidth = 20m
c.calc_weight()