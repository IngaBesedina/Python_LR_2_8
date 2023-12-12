#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiplication():
    res = 1
    while True:
        num = int(input('Введите число: '))
        if num == 0:
            break
        res *= num

    return res


if __name__ == "__main__":
    mult = multiplication()
    print('Произведение чисел: ', mult)
