#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    return input('Введите строку: ')


def test_input(st):
    return st.isdigit() or st[0] == '-'


def str_to_int(st):
    return int(st)


def print_int(value):
    print('Целое число: ', value)


if __name__ == "__main__":
    input_value = get_input()
    if test_input(input_value):
        int_value = str_to_int(input_value)
        print_int(int_value)
    else:
        print('Невозможно преобразовать в целое число')
