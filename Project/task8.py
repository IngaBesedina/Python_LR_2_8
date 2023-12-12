#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    num = int(input('Введите целое число: '))

    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        print('Число 0')


def positive():
    print('Положительное число')


def negative():
    print('Отрицательное число')


if __name__ == "__main__":
    test()
