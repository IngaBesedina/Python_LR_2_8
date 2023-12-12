#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def cylinder():
    def circle(r):
        return math.pi*r**2

    radius = float(input('Радиус цилиндра: '))
    height = float(input('Высота цилиндра: '))

    side_area = 2*math.pi*radius*height

    answer = input('Посчитать полную площадь цилиндра? (y/n) ')
    if answer == 'y':
        full_area = side_area + 2*circle(radius)
        print(f'Полная площадь: {full_area:.2f}')
    elif answer == 'n':
        print(f'Площадь боковой поверхности цилиндра: {side_area:.2f}')
    else:
        print('Неверный ввод')


if __name__ == "__main__":
    cylinder()
