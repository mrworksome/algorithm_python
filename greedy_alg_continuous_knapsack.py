#! Python3

"""
Задача: непрерывный рюкзак
Первая строка содержит количество предметов 1 ≤ n ≤ 10^3 и вместимость рюкзака
0 ≤ W ≤ 2 * 10^6. Каждая из следующих n строк задаёт стоимость 0 ≤ ci ≤ 2 * 10^6 и объём
0 < wi ≤ 2 * 10^6 предмета (n, W, ci, wi — целые числа). Выведите максимальную стоимость
частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при
этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх
знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.000
"""

import sys
import heapq


def list_continuous_knapsack(item_list: list, capacity: int) -> float:
    """
    1) сортируем предметы по ценности
    2) проходимся по item_list циклом, в котором если масса предмета
    меньше вместимости рюкзака то укладываем его в рюкзак
    :param item_list: cost, weight
    :param capacity: вместимость
    :return: возращаем максимальную стоимость которую может вместить этот раюкзак
    """
    item_list.sort(key=lambda x: x[0] / x[1], reverse=True)
    full_cost = 0
    for cost, weight in item_list:
        if weight < capacity:
            full_cost += cost
            capacity -= weight
        else:
            full_cost += cost / weight * capacity
            break
    return float("{:3f}".format(full_cost))


def heapified_continuous_knapsack(item_list: list, capacity: int):
    """
    1) преобразуем список из входных данных через кучи
    (- cost) - взят для того, чтобы первым получить наибольшее значение из кучи
    и положить его в рюкзак
    2) берем из кучи наибольшее значение
    3) в цикле испольщуем с противоположным знаком  значение  - cost_per_weight
    потому что оно отрицательное, в рюкзак мы можем положить только положительное
    :param item_list: cost, weight
    :param capacity: вместимость
    :return: возращаем максимальную стоимость которую может вместить этот раюкзак
    """
    item_heap = [(-cost / weight, weight) for cost, weight in item_list]
    heapq.heapify(item_heap)

    full_cost = 0
    while item_heap and capacity:
        cost_per_weight, weight = heapq.heappop(item_heap)
        weight_reduction = min(weight, capacity)

        full_cost += abs(cost_per_weight) * weight_reduction
        capacity -= weight_reduction
    return float("{:3f}".format(full_cost))


def advanced_input():
    """
    получаем входные значения для получения значений стоиимости и веса предметов
    :return: вмесимость рюкзака, массив предметов
    """
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    item_list = list(reader)

    assert len(item_list) == n
    return capacity, item_list


def main():
    capacity, item_list = advanced_input()
    print(list_continuous_knapsack(item_list, capacity))
    print(heapified_continuous_knapsack(item_list, capacity))


if __name__ == '__main__':
    main()
