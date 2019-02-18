"""
Задача: калькулятор

У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим
числом x: заменить x на 2x, 3x или x+1. По данному целому числу 1 ≤ n ≤ 10^5 определите
минимальное число операций k, необходимое, чтобы получить n из 1. Выведите k и
последовательность промежуточных чисел.

Sample Input 1:
1
Sample Output 1:
0
1

Sample Input 2:
5
Sample Output 2:
3
1 2 4 5

Sample Input 3:
96234
Sample Output 3:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
"""


def calculator(n):
    min_oper = [0, 0]
    for i in range(2, n + 1):
        a = min_oper[i // 3] if i % 3 == 0 else float('inf')
        b = min_oper[i // 2] if i % 2 == 0 else float('inf')
        min_oper.append(min(a, b, min_oper[i - 1]) + 1)

    sequence = []
    i = n
    while i:
        sequence.append(i)
        k = min_oper[i]
        if i % 3 == 0 and min_oper[i // 3] == (k - 1):
            i //= 3
        elif i % 2 == 0 and min_oper[i // 2] == (k - 1):
            i //= 2
        else:
            i -= 1
    return min_oper[n], reversed(sequence)


def main():
    n = int(input())
    k, sequence = calculator(n)

    print(k)
    print(*sequence)


if __name__ == '__main__':
    main()