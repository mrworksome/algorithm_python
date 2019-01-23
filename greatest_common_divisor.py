#! Python 3
# В фаиле рассмотриим возможные варианты получения наибольшего общего делителя
"""
Алгори́тм Евкли́да — эффективный алгоритм для нахождения наибольшего общего
делителя двух целых ПРОСТЫХ чисел (или общей меры двух отрезков)

число называется простым если его можно представить в виде произведения
1 и самого себя

Решето эратосфена:
https://ru.wikipedia.org/wiki/Решето_Эратосфена
https://www.youtube.com/watch?v=3I6OjxoeSS8
https://stepik.org/lesson/13229/step/1?unit=3415

Лекции МФТИ по алгоритмам:
https://www.youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0
http://judge.mipt.ru/mipt_cs_on_python3/

Лекции по алгоритмам и Python от Computer Science Center:
https://www.youtube.com/channel/UC0YHNueF-3Nh3uQT0P4YQZw
_______________________________________________________________________________
Задача: наибольший общий делитель
По данным двум числам 1 ≤ a, b ≤ 2 * 10^9 найдите их наибольший общий делитель.

Sample Input 1:
18 35
Sample Output 1:
1

Sample Input 2:
14159572 63967072
Sample Output 2:
4

"""
# Введение
from time import time
from math import gcd as gcd_standard


def siev_of_eratosthenes(n: int):
    """
    посик всеъ простых чисел до нужного числа n
    резервируем память для нахождениия всех простых чисел

    сложность алгоритма nlog(logn) при составлении таблицы из n элементов

    :param n: барьерное число
    :return: список простых чисел
    """
    assert n > 1
    sequence = [True] * n
    sequence[0] = sequence[1] = False
    for k in range(2, n):
        if sequence[k]:
            for m in range(2 * k, n, k):
                sequence[m] = False
    for k in range(n):
        print(k, '-', "простое" if sequence[k] else "составное")


# Пример создания алгоритма


def gcd_iterative(a: int, b: int) -> int:
    """
    
    используя множественное присваивания алгоритм последовательно находит
    GSD двух чисел и не хранит в памяти лишние значения тем самым
    он находит достаточно быстро это значение

    :param a: первое значения ключа
    :param b: второе значения ключа
    :return: наибольший общий делитель
    """
    assert a > 0 and b > 0
    while a != 0:
        a, b = b % a, a
        return b


def gcd_recursive(a: int, b: int) -> int:
    """
    используя функцию которая сама себя вызывает алгоритм тратит очень
    огромное кол-во памяти (алгориитм похож на матрешку)
    :param a: первое значения ключа
    :param b: второе значения ключа
    :return: наибольший общий делитель
    """

    return gcd_recursive(b % a, a) if a else b

# тестирование


if __name__ == '__main__':

    # a, b = (int(i) for i in input().split())  считывание данных с клавиатуры

    start_time = time()
    gcd_standard(14159572, 63967072)
    end_time = time()
    elapsed_1 = end_time - start_time
    print('standard', elapsed_1)

    start_time = time()
    gcd_iterative(14159572, 63967072)
    end_time = time()
    elapsed_2 = end_time - start_time
    print('iterative', elapsed_2)

    start_time = time()
    gcd_recursive(14159572, 63967072)
    end_time = time()
    elapsed_3 = end_time - start_time
    print('recursive', elapsed_3)

    print("Best time Algorithms:  ", min(elapsed_3, elapsed_2, elapsed_1))

