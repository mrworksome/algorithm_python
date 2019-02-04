"""
Дополнительные материалы:


Задача: двоичный поиск
﻿
В первой строке даны целое число 1 ≤ n ≤ 10^5 и массив A[1…n] из n различных
натуральных чисел, не превышающих 10^9, в порядке возрастания,
во второй — целое число 1 ≤ k ≤ 10^5 и k натуральных чисел b1,…,bk,
не превышающих 10^9. Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n,
для которого A[j]=bi, или −1, если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
"""
import sys
from bisect import bisect_left


def binary_search(number_list, key):
    """
    :param number_list: упорядоченный массив
    :param key: ключ по которому осуществляется поиск
    :return:
    """
    left_bound = 0
    right_bound = len(number_list)

    while left_bound < right_bound:
        middle = (left_bound + right_bound) // 2

        if key == number_list[middle]:
            return middle + 1
        elif key < number_list[middle]:
            right_bound = middle
        else:
            left_bound = middle + 1
    return -1


def b_search_bisect(number_list, key):
    """
    реализация того же алгоритма путем уже встроенного метода в Python 3
    :param number_list: упорядоченный массив
    :param key: ключ по которому осуществляется поиск
    :return:
    """
    left_bound = bisect_left(number_list, key)
    if left_bound < len(number_list) and number_list[left_bound] == key:
        return left_bound + 1
    else:
        return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n_, *a = next(reader)
    k_, *b = next(reader)

    answer_list = [binary_search(a, number) for number in b]
    # answer_list = [b_search_bisect(a, number) for number in b]
    print(*answer_list)


if __name__ == '__main__':
    main()