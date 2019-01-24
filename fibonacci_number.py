#! Python3

"""
задачи с числом фиббоначи

в этом уроке рассмотриим несколько задач связанных с числом фиббоначи
_______________________________________________________________________________
курс лекций МФТИ:
https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0
https://www.youtube.com/watch?v=qkLLcdgJj_o&feature=youtu.be&t=3327
_______________________________________________________________________________
Используемые библиотеки и описание методов:
https://python-scripts.com/import-functools
https://pythonworld.ru/moduli/modul-functools.html

https://habr.com/en/post/257903/
https://www.quora.com/What-does-_-in-Python-mean-in-a-for-loop
_______________________________________________________________________________
Дополнительные материалы для решения задачи:
http://docplayer.ru/30969379-Proektnaya-rabota-po-matematike.html
https://en.wikipedia.org/wiki/Pisano_period﻿
https://ru.wikipedia.org/wiki/Период_Пизано

последняя функция (execution_time) является функцией обертки для того чтобы
наглядно оценить работоспособность разных алгоритмов
в дальнейшем разберем более подробно как создавать декораторы и использовать их
http://qaru.site/questions/263590/understanding-timeperfcounter-and-timeprocesstime
_______________________________________________________________________________
Задача 1: небольшое число Фибоначчи
Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи при n ≥ 2)
Sample Input:
3
Sample Output:
2
_______________________________________________________________________________
"""

# Задача 1
import time
from functools import lru_cache


def fib_iterative(n: int) -> int:
    """
    ___________________________________________________________________________
    является самой быстрой за счет линейного расчета
    ___________________________________________________________________________
    :param n: номер числа фиббоначи
    :return: число фиббоначи
    """
    fib_0, fib_1 = 0, 1
    for _ in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


def fib_recursive(n: int) -> int:
    """
    ___________________________________________________________________________
    затрачивает огромное кол-во времени на расчет каждого числа фиббоначи
    очень много повторений одних и тех же вычислений
    ___________________________________________________________________________
    :param n: номер числа фиббоначи
    :return: число фиббоначи
    """
    return n if n <= 1 else fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_recursive_with_reserve_memory(n: int) -> int:
    """
    ___________________________________________________________________________
    функция сразу резервирует необходимое количество памяти
    для расчета всей последовательности и вывода нужного числа
    ___________________________________________________________________________
    :param n: номер числа фиббоначи
    :return: число фиббоначи
    """
    fib_n = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_n[i] = fib_n[i - 1] + fib_n[i - 2]
    return fib_n[n]


@lru_cache(maxsize=None)
def fib_recursive_with_cash(n: int):
    """
    ___________________________________________________________________________
    функция запоминает все ранее посчитанные числа в памяти
    и тем самым упроцает повторный вызов функции для дальнейших расчетов
    ___________________________________________________________________________
    :param n: номер числа фиббоначи
    :return: число фиббоначи
    """
    return n if n <= 1 else fib_recursive_with_cash(n - 1) + fib_recursive_with_cash(n - 2)


def last_number_fib_iterative(n: int) -> int:
    """
    ___________________________________________________________________________
    Задача 2: последняя цифра большого числа Фибоначчи
    Дано число 1 ≤ n ≤ 10^7, необходимо найти последнюю
    цифру n-го числа Фибоначчи.
    Sample Input:
    875577
    Sample Output:
    2
    ___________________________________________________________________________
    :param n: число фиббоначи
    :return: последнее цифра числа фиббоначи
    """
    fib_0, fib_1 = 0, 1
    for _ in range(n - 1):
        fib_0, fib_1 = fib_1, (fib_0 + fib_1) % 10
    return fib_1


def fib_mod(n: int, m: int):
    """
    ___________________________________________________________________________
    Задача 3: огромное число Фибоначчи по модулю
    Даны целые числа 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5, необходимо найти остаток от
    деления n-го числа Фибоначчи на m.
    Sample Input:
    10 2
    Sample Output:
    1
    ___________________________________________________________________________
    :param n: число фиббоначи
    :param m: число
    :return: остаток
    """
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % m)
        if fib[i] == 1 and fib[i - 1] == 0:
            fib = fib[: -2]
            break
    return fib[n % len(fib)]


def execution_time(func, *args, n_iter=1):
    """
    ___________________________________________________________________________
    функция вычисляет время выполнения функции
    для того чтобы оценить скорость исполнения алгоритма
    ___________________________________________________________________________
    :param func: принимаемая функция(записывается без скобок)
    :param args: аргументы принимаемые функцией
    :param n_iter: кол-во повторений функции
    :return: среднее время исполнения функции
    """
    full_time = 0
    for i in range(n_iter):
        t0 = time.perf_counter()
        func(*args)
        full_time += (time.perf_counter() - t0)

    return full_time / n_iter


if __name__ == '__main__':
    n_fib = 39

    print("Time iterative algorithm", execution_time(fib_iterative, n_fib))
    print("Time recursive algorithm", execution_time(fib_recursive, n_fib))
    print("Time recursive_with_reserve_memory algorithm", execution_time(fib_recursive_with_reserve_memory, n_fib))
    print("Time recursive_with_cash algorithm", execution_time(fib_recursive_with_cash, n_fib))


