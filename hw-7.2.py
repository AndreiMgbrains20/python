'''
Version 2
HomeWork 7.2 (hw-7.1.py, ..., hw-7.3.py)


2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

'''
#Vers.2

#abstact

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):   #constructor
    @abstractmethod
    def consum(self):
        pass

class Clothes(MyAbstractClass):
    def __init__(self, par='MyAbstractClass'):
        self.par = par
        print('------- class Clothes  ', par)

    @property
    def consum_Coat(self, par):
        pass

    @property
    def consum_Suite(self, par):
        pass

    @property
    def consum(self):
        print('------- consum')
        return round(self.consum_Coat + self.consum_Suite, 2)

class Coat(Clothes):
    @property
    def consum(self):
        res = round(self.par / 6.5 + 0.5, 2)
        Clothes.consum_Coat = res
        return f' Необходимо ткани на пальто - {self.par}, размером - {res}'

class Suite(Clothes):
    @property
    def consum(self):
        res = round(self.par * 2 + 0.3, 2)   #костюм без подкладки, обычный - *2. С покладкой - *4.9
        Clothes.consum_Suite = res
        return f' Необходимо ткани на костюм - {self.par}, размером - {res}'

#на пальто - 1,5м ширина ткани (рулон). 4м длина ткани на рост - высокий. Размер 56. XXL.
#на костюм - 1.брюки 1,5м ширина ткани (рулон). 1,9м длина ткани и 2.Жакет 0,9м ширина и 4,2м длина ткани (без прокладки) на рост - высокий
#предусматриваем на костюм, всего - 1,5м ширина рулона и 4м длина (1,9 + 2,1). Размер 56. XXL.

o = Clothes()
c = Coat(56) #размер - рост до 180см, охват талии/груди - до 120. Размер 56 (XXL)
print(c.consum)
s = Suite(3) #размер - рост до 180см, охват талии/груди - до 120 (XXL) = 1.8+1.2 = 3
print(s.consum)
print(f' Расход ткани всего = {o.consum}')




'''
Vers.1

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_sq_c(self):
        return self.v / 6.5 + 0.5

    def get_sq_s(self):
        return self.h * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f' Общее количество ткани:  {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.sq_c = self.v / 6.5 + 0.5

    def __str__(self):
        return f' пл. ткани на пальто:  {self.sq_c}'

class Suite(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.sq_s = self.h * 2 + 0.3

    def __str__(self):
        return f' пл. ткани на кастюм:  {self.sq_s}'

#на польто - 1,5м ширина ткани (рулон). 4м длина ткани на рост - высокий
coat = Coat(1.5, 4)

#на кастюм - 1.брюки 1,5м ширина ткани (рулон). 1,9м длина ткани и 2.Жакет 0,9м ширина и 4,2м длина ткани (без прокладки) на рост - высокий
#предусматриваем жакет с прокладкой, всего - 1,5м ширина рулона и 6,1м длина (1,9 + 4,2)
suite = Suite(1.5, 6.1)

print(' Coat через class', coat)
print(' coat через class child', coat.get_sq_c())
print(' coat... property sq tot', coat.get_sq_full)

print(' Suite через class', suite)
print(' suite через class child', suite.get_sq_s())
print(' suite... property sq tot', suite.get_sq_full)
'''
