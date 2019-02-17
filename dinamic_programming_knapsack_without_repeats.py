"""
Задача: рюкзак
﻿
Первая строка входа содержит целые числа 1 ≤ W ≤ 10^4 и 1 ≤ n ≤ 300 — вместимость рюкзака
и число золотых слитков. Следующая строка содержит n целых чисел 0 ≤ w1, …, wn ≤ 10^5,
задающих веса слитков. Найдите максимальный вес золота, который можно унести в рюкзаке.

Sample Input:
10 3
1 4 8

Sample Output:
9
"""


def knapsack_without_repeats(capacity, weight_list):
    """
    Стоимость золота за единицу постоянна => стоимость предмета пропорциональна его весу
    Пусть стоимость за единицу = 1
    :param capacity: вместимость рюкзака
    :param weight_list: вес предметов
    :return: максимальное кол-во золота которое можем унести
    """
    cost = 1
    previous = [0] * (capacity + 1)
    for i in range(1, len(weight_list) + 1):
        current = [0]
        for w in range(1, capacity + 1):
            current.append(previous[w])
            if weight_list[i - 1] <= w:
                current[w] = max(current[w], previous[w - weight_list[i - 1]] + cost * weight_list[i - 1])
        previous = current

    return previous[capacity] // cost


def main():
    capacity, n_ = (int(i) for i in input().split())
    weight_list = [int(i) for i in input().split()]

    print(knapsack_without_repeats(capacity, weight_list))


if __name__ == '__main__':
    main()
