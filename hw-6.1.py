'''
date: 14.06.2020 / Version 1
author: AndreiM
https://github.com/AndreiMgbrains20/python/
lesson-6 / Python @GeekBrains
HomeWork 6.1 (hw-6.1.py, ..., hw-6.5.py)

1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.

'''

# красный - желтый - зеленый - желтый - красный... 7-2-7-1-2-...(сек.)


from time import sleep

class TrafficLight:
    __color = ['# Красный #', '# Желтый #', '# Зеленый #', '# Зеленый-3x #', '# Желтый - красный / ночной режим #']

    def running(self):
        i = 0
        while i < 5:
            print(f'Светофор переключается ...\n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            elif i == 3:
                sleep(1)
            elif i == 4:
                sleep(2)
            i += 1
        print(f'Цикл выполнен без ошибок!')

t = TrafficLight()
t.running()


'''
# Vers. 2

import time
from time import sleep
from tkinter import *

tk=Tk()
w=Canvas(tk, width=200, height=180) #window
w.pack()
tk.title("Светофор")

def red(a):
        red=w.create_oval(15,5,60,50, fill='red')
        tk.update()
        time.sleep(0.1 * a)
def redb(a):
        red=w.create_oval(15,5,60,50, fill='silver')
        tk.update()
        time.sleep(0.1 * a)
def yel(a):
        amber=w.create_oval(15,55,60,100, fill='yellow')
        tk.update()
        time.sleep(0.1 * a)
def yelb(a):
        amber=w.create_oval(15,55,60,100, fill='silver')
        tk.update()
        time.sleep(0.1 * a)
def green(a):
        green=w.create_oval(15,105,60,150, fill='green')
        tk.update()
        time.sleep(0.1 * a)
def greenb(a):
        green=w.create_oval(15,105,60,150, fill='silver')
        tk.update()
        time.sleep(0.1 * a)
def lights():
    red=w.create_oval(15,5,60,50, fill="silver")
    yel=w.create_oval(15,55,60,100, fill ="silver")
    green=w.create_oval(15,105,60,150, fill="silver")

i=0
while i < 1: #один проход... затем закрыть окно
    i += 1

    lights()
    red(70)
    redb(1)
    yel(20)
    yelb(1)
    green(70)
    greenb(2)
    green(10)
    greenb(2)
    green(10)
    greenb(2)
    green(10)
    greenb(2)
    yel(20)
    yelb(1)

tk.mainloop()
print("All Threads done well ... Exiting")

'''