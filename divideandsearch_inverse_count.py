"""

Задача: число инверсий

Задача подсчета инверсий называется «Проблема Йоданесс»
На основе рекурсивного алгоритма сортировки слиянием
﻿
Первая строка содержит число 1 ≤ n ≤ 10^5, вторая — массив A[1…n], содержащий
натуральные числа, не превосходящие 10^9. Необходимо посчитать число пар
индексов 1 ≤ i < j ≤ n, для которых A[i] > A[j]. (Такая пара элементов
называется инверсией массива. Количество инверсий в массиве является в некотором
смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию
массиве инверсий нет вообще, а в массиве, упорядоченном по
убыванию, инверсию образуют каждые два элемента.)

Sample Input:
5
2 3 9 2 9

Sample Output:
2
"""


def inversions_count(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list, 0
    middle_index = len(unsorted_list) // 2

    left_list, left_list_inv_count = inversions_count(unsorted_list[:middle_index])
    right_list, right_list_inv_count = inversions_count(unsorted_list[middle_index:])

    merged_list, current_merge_inv_count = merge(left_list, right_list)
    return merged_list, (left_list_inv_count + right_list_inv_count + current_merge_inv_count)


def merge(left_list, right_list):
    merged_list = []
    i, j = 0, 0
    current_merge_inv_count = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            current_merge_inv_count += (len(left_list) - i)
            j += 1
    merged_list.extend(left_list[i:] + right_list[j:])
    return merged_list, current_merge_inv_count


def main():
    n_ = input()
    unsorted_list = [int(i) for i in input().split()]

    sorted_list_, inv_count = inversions_count(unsorted_list)
    print(inv_count)


if __name__ == '__main__':
    main()
