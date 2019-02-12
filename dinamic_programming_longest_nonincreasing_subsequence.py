"""
Дополниительные материалы:
http://qaru.site/questions/261858/what-is-inf-and-nan
http://pythonz.net/references/named/float/


Задача: наибольшая невозрастающая подпоследовательность

Дано целое число 1 ≤ n ≤ 10^5 и массив A[1…n], содержащий неотрицательные целые числа, не
превосходящие 10^9. Найдите наибольшую невозрастающую подпоследовательность в A. В первой
строке выведите её длину k, во второй — её индексы 1 ≤ i1 < i2 < … < ik ≤ n (таким образом,
A[i1] ≥ A[i2] ≥ … ≥ A[in]).

Наибольшая невозрастающая последовательность
ВВОД: первая строка - n, количество элементов последовательности (int, 1 <= n <= 10**5)
      вторая строка - n элементов a последовательности через пробел (a: int, 0 <= a <= 10**9)

ВЫВОД: первая строка - m, количество элементов максимальной невозрастающей подпоследовательности
       вторая строка - m элементов максимальной невозрастающей подпоследовательности

Sample Input:
5
5 3 4 4 2

Sample Output:
4
1 3 4 5
"""
import sys
from bisect import bisect_right


def longest_non_increasing_subsequence(sequence):
    sequence.reverse()
    last_number = [-float('inf')] + [float('inf')] * len(sequence)
    positions = [-1] * (len(sequence) + 1)
    previous = [-1] * len(sequence)
    length = 0

    for i in range(len(sequence)):
        pos = bisect_right(last_number, sequence[i])
        if True:
            last_number[pos] = sequence[i]
            positions[pos] = i
            previous[i] = positions[pos - 1]
            length = max(length, pos)

    index_pos = []
    pos = positions[length]
    while pos != -1:
        index_pos.append(len(sequence) - pos)
        pos = previous[pos]

    return length, index_pos


def main():
    n_ = int(input())
    sequence = [int(i) for i in input().split()]

    length, index_pos = longest_non_increasing_subsequence(sequence)
    print(length)
    print(*index_pos)


"""__________________________________________________________________________"""

# Альтернативное решение данной задачи


def fast_noninreasing(seq_list):
    """
    nlog(n) реализация алгоритма поиска максимальной невозрастающей последовательности.

    >>> fast_noninreasing([1, 2, 3, 4, 5])
    [5]
    >>> fast_noninreasing([5, 3, 4, 4, 2])
    [1, 3, 4, 5]
    >>> fast_noninreasing([5, 6, 7, 7, 6, 2, 3])
    [3, 4, 5, 7]
    >>> fast_noninreasing([5, 3, 4, 4, 2, 5, 9])
    [1, 3, 4, 5]
    >>> fast_noninreasing([2, 2, 2, 2])
    [1, 2, 3, 4]

    :param: list[>=1, <=10^5](int, >=0, <=10^9)
    :return: list of indexes of elements from noninreasing subsequence

    """
    sub_list = [-1 for _ in range(len(seq_list) + 1)]
    sub_list[0] = 10**9 + 1
    parent = [0 for _ in range(len(seq_list))]  # Для каждого элемента seq записываем его предшественника из подпосл.
    max_len = 1  # Максимальная длина подпоследовательности.
    last_index = 0  # Храним индекс из seq_list для последнего элемента, входящего в подпоследовательность.

    for i in range(len(seq_list)):
        j = search_index(sub_list, seq_list[i])
        if sub_list[j - 1] >= seq_list[i] > sub_list[j]:
            sub_list[j] = seq_list[i]
            parent[i] = sub_list[j - 1]
            if j >= max_len:
                max_len = j
                last_index = i

    # Восстановление ответа
    res_list = [0 for _ in range(max_len)]
    now_index = max_len - 1
    expect_num = seq_list[last_index]
    for i in range(last_index, -1, -1):
        if seq_list[i] != expect_num:
            continue
        res_list[now_index] = i + 1
        expect_num = parent[i]
        now_index -= 1

    return res_list


def search_index(sub_list, item):
    """
    Бинарный поиск индекса элемента в массиве sub_list, который строго меньше чем item.
    sub_list отсортирован по невозрастанию.
    Из-за специфики функции fast_nonincreasing, предполагается, что в sub_list
    всегда есть хотябы один элемент меньше чем item.
    >> search_index([5, 4, 3, 2, 1], 5)
    1
    >> search_index([10, 7, 7, 5, 5, 4, 4, 3, 3], 5)
    5
    >> search_index([1000000001, 6, 6, 6, 5, 5, 4, 4, 4, 4, -1], 3)
    10

    :param sub_list: 'list[>=1, <=10^5](int, >=0, <=10^9+1)'
    :param item: 'int, >=1, <=10**9, >sub_list[-1]'
    :return: index: int

    """
    res_index = -1  # Из условий входящих данных, последний элемент sub_list всегда меньше чем item.
    left = 0
    right = len(sub_list) - 1
    while left <= right:
        mid_index = (left + right) // 2
        if sub_list[mid_index] >= item:
            left = mid_index + 1
        else:
            res_index = mid_index
            right = mid_index - 1
    return res_index


def read_data():
    sys.stdin.readline() # пропускаем n, т.е. первая строка тут не нужна
    return [int(i) for i in sys.stdin.readline().split()]


def out_data(res_list):
    result = str(len(res_list))
    result += '\n'
    result += " ".join(str(i) for i in res_list)
    print(result)


def run():
    seq = read_data()
    res = fast_noninreasing(seq)
    out_data(res)


if __name__ == '__main__':
    run()
    # main()
