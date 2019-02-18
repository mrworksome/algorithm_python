"""
Задача: лестница
Даны число 1 ≤ n ≤ 10^2 ступенек лестницы и целые числа −10^4 ≤ a1, …, an ≤ 10^4, которыми
помечены ступеньки. Найдите максимальную сумму, которую можно получить, идя по лестнице
снизу вверх (от нулевой до n-й ступеньки), каждый раз поднимаясь на одну или две ступеньки.

Sample Input 1:
2
1 2
Sample Output 1:
3

Sample Input 2:
2
2 -1
Sample Output 2:
1

Sample Input 3:
3
-1 2 1
Sample Output 3:
3
"""


def stairway_up(stairs):
    previous = 0
    current = stairs[0]
    for stair in stairs[1:]:
        previous, current = current, max(previous, current) + stair
    return current


def main():
    n_ = int(input())
    stairs = [int(i) for i in input().split()]

    print(stairway_up(stairs))


if __name__ == '__main__':
    main()
