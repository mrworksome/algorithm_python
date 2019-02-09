"""
Задача: наибольшая последовательнократная подпоследовательность

Дано целое число 1 ≤ n ≤ 10^3 и массив A[1…n] натуральных чисел,
не превосходящих 2*10^9.
Выведите максимальное 1 ≤ k ≤ n, для которого найдётся подпоследовательность
1 ≤ i1 < i2 < … < ik ≤ n длины k, в которой каждый элемент делится на предыдущий
(формально: для  всех 1 ≤ j < k, A[i(j)]|A[i(j+1)].

Sample Input:
4
3 6 7 12
Sample Output:
3
"""


def longest_multiple_subsequence(sequence):
    lengths = [1] * len(sequence)
    for i in range(len(sequence)):
        for j in range(i):
            if (sequence[i] % sequence[j] == 0) and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
    return max(lengths)


def main():
    n_ = int(input())
    sequence = [int(i) for i in input().split()]

    print(longest_multiple_subsequence(sequence))


if __name__ == '__main__':
    main()