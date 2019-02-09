"""
Дополнительные материалы:
https://neerc.ifmo.ru/wiki/index.php?title=Сортировка_подсчётом
https://www.youtube.com/watch?v=ukTBUyTOZs4


Задача: сортировка подсчётом
Первая строка содержит число 1 ≤ n ≤ 10^4, вторая — n натуральных чисел,
не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.

Sample Input:
5
2 3 9 2 9
Sample Output:
2 2 3 9 9
"""


def count_sort(list_to_sort, max_value):
    counter = [0] * max_value

    for element in list_to_sort:
        counter[element - 1] += 1
    for i in range(1, max_value):
        counter[i] += counter[i - 1]

    sorted_list = [0] * len(list_to_sort)
    for element in reversed(list_to_sort):
        sorted_list[counter[element - 1] - 1] = element
        counter[element - 1] -= 1
    return sorted_list


def main():
    n_ = int(input())
    list_to_sort = [int(i) for i in input().split()]
    print(*count_sort(list_to_sort, 10))


if __name__ == '__main__':
    main()
