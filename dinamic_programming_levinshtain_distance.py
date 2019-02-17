"""
Дополнительные материалы:
https://www.youtube.com/watch?v=rEPggzaPoUw&t=9s


Задача: расстояние редактирования

Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2,
содержащих строчные буквы латинского алфавита.

Sample Input 1:
ab
ab
Sample Output 1:
0

Sample Input 2:
short
ports
Sample Output 2:
3
"""


def levenshtein_distance(a, b):
    """
    для того чтобы узнать Расстояние Левенштейна мы сделаем матрицу
    в которой посчитаем сколько правок необходимо сделать для получения исходной
    строки
    :param a: первая строка
    :param b: вторая строка
    :return: вызываем последнее значение
    """
    f = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
    return f[len(a)][len(b)]


def main():
    n, m = input(), input()
    res = levenshtein_distance(n, m)
    print(res)


if __name__ == '__main__':
    main()
