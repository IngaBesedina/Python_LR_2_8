#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def get_student():
    """
    Запросить данные о студенте.
    """
    surname = input("Введите фамилию и инициалы: ")
    group_num = input("Введите номер группы: ")
    print('Введите оценки: ')
    grades = [int(n) for n in input().split()]

    student = {
        'name': surname,
        'group_number': group_num,
        'grades': grades
    }

    return student


def display_students(staff):
    """
    Отобразить список студентов.
    """
    # Проверить, что список студентов не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 14
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^14} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "Оценки"
            )
        )
        print(line)

        # Вывести данные о всех студентах.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>14} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group_number', ''),
                    ', '.join(str(el) for el in student.get('grades'))
                )
            )
        print(line)

    else:
        print("Список студентов пуст.")


def select_students(staff):
    # Сформировать список студентов, имеющих оценки 4 и 5.
    result = []
    for student in staff:
        if all(grade >= 4 for grade in student['grades']):
            result.append(student)

    # Возвратить список выбранных студентов.
    return result


def main():
    """
    Главная функция программы.
    """
    # Список студентов.
    students = []

    # бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            student = get_student()

            # Добавить словарь в список.
            students.append(student)
            # Сортировка по возрастанию среднего балла
            students.sort(key=lambda x: sum(x['grades']) / 5)

        elif command == 'list':
            # Отобразить всех студентов.
            display_students(students)

        elif command == 'select':
            selected = select_students(students)
            # Отобразить выбранных студентов.
            display_students(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select - запросить студентов, имеющих оценки 4, 5;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
