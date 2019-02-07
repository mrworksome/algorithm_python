"""
Дополнительные материалы:
https://habr.com/en/sandbox/29775/
https://algs4.cs.princeton.edu/23quicksort/
https://stackoverflow.com/questions/18262306/quicksort-with-python
https://ru.wikipedia.org/wiki/Дерево_отрезков



Задача: точки и отрезки
В первой строке задано два целых числа 1 ≤ n ≤ 50000 и 1 ≤ m ≤ 50000 — количество отрезков
и точек на прямой, соответственно. Следующие n строк содержат по два целых числа ai и bi
(ai ≤ bi) — координаты концов отрезков. Последняя строка содержит m целых чисел — координаты
точек. Все координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку,
если она находится внутри него или на границе. Для каждой точки в порядке появления во вводе
выведите, скольким отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11

Sample Output:
1 0 0
"""

import sys


def dots_and_segments(bounds_and_dots, dots_count):
    """
    ____________________________________________________________________________
    1) для начала отсортируем массив, соответственно отрезки и точки отсортируются
    по значениям и упростят нахождение входит ли точка в эти отрезки
    2) создадим пямять для записи результатов и счетчик вхождений
    3) проитеррируемся по отсортированному массиву и если значние точки будет
    находиться между концами отрезков то наш счетчик запишет его в ответ
    ____________________________________________________________________________
    :param bounds_and_dots: отрезки (с их значениями лев и прав границы)
    :param dots_count: кол-во точек
    :return: скольким отрезкам принадлежит точка
    """
    bounds_and_dots.sort()
    result = [0] * dots_count
    current = 0
    for dot in bounds_and_dots:
        current -= dot[1]
        if dot[1] == 0:
            result[dot[2]] = current
    return result


def input_and_processing(reader):
    """
    ____________________________________________________________________________
    по очередно добавим левые и правые стороны отрезков со значениям
    где (-1 левый конец отрезка) а (1 правый конец отрезка)
    для значений точек по которым будем итеррироваться мы сделаем tuple из 3х
    значений (сама точка, 0 - будет указателем того что это точка и
    3е значение порядковый номер точки по появлению во вводе из условия задачи
    ____________________________________________________________________________
    :param reader: прочтение строки со значениями
    :return: отрезки (с их значениями лев и прав границы) и кол-во точек
    """
    n, m = next(reader)
    bounds_and_dots = []
    for _ in range(n):
        left, right = next(reader)
        bounds_and_dots.append((left, -1))
        bounds_and_dots.append((right, 1))

    input_dots = [int(i) for i in next(reader)]
    for i in range(len(input_dots)):
        bounds_and_dots.append((input_dots[i], 0, i))
    return bounds_and_dots, m


def dots_and_segments_2(heap_dots_and_bounds, n_dots):
    """
    :param heap_dots_and_bounds: отрезки и точки
    :param n_dots: кол-во точек
    :return: скольким отрезкам принадлежит точка
    """
    result_work = [0] * n_dots
    heap_dots_and_bounds.sort()
    current_work = 0
    for x, type_obj, i in heap_dots_and_bounds:
        if type_obj == 0:
            result_work[i] = current_work
        elif type_obj < 0:
            current_work += 1
        else:
            current_work -= 1
    return result_work


def input_and_processing_2(reader_line):
    """
    ____________________________________________________________________________
    распределяем значения отрезков и точек
    для -1, 1 это левый и i, -i для фиксации крайних значений отрезка
    учитываем случай, когда отрезки вкладываются друг в друга, и
    координаты их концов совпадают для начал отрезков будем класть номер
    со знаком "+", чтобы они шли в прямом порядке,
    а для правых концов -- со знаком "-", чтобы порядок инвертировался.
    ____________________________________________________________________________
    :param reader_line: функция принимающая данные и обрабатывающих
    :return: массив с точками и отрезками
    """
    n_counts, n_dots = reader_line()
    heap_dots_and_bounds = []
    for i in range(n_counts):
        left_x, right_x = reader_line()
        if left_x <= right_x:
            heap_dots_and_bounds.append((left_x, -1, i))
            heap_dots_and_bounds.append((right_x, 1, -i))
    for i, dots_x in enumerate(reader_line()):
        heap_dots_and_bounds.append((dots_x, 0, i))
    return heap_dots_and_bounds, n_dots


def main_2():
    reader_line = (lambda: (map(int, sys.stdin.readline().split())))
    heap_dots_and_bounds, n_dots = input_and_processing_2(reader_line)
    print(*dots_and_segments_2(heap_dots_and_bounds, n_dots))


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    bounds_and_dots, dots_count = input_and_processing(reader)
    print(*dots_and_segments(bounds_and_dots, dots_count))


if __name__ == '__main__':
    main()
    main_2()
