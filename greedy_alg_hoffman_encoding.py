#! Python3

"""
Дополнительный материал к задаче:

https://younglinux.info/python/feature/enumerate
https://pythonworld.ru/moduli/modul-collections.html
https://docs.python.org/3/library/heapq.html
https://stackoverrun.com/ru/q/8841341


Задача: кодирование Хаффмана
По данной непустой строке s длины не более 10^4, состоящей из строчных букв
латинского алфавита, постройте оптимальный беспрефиксный код. В первой строке
выведите количество различных букв k, встречающихся в строке, и размер
получившейся закодированной строки. В следующих k строках запишите коды букв
в формате "letter: code". В последней строке выведите закодированную строку.

Sample Input 1:
a
Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad
Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""

import heapq
from collections import namedtuple, Counter


class Node(namedtuple('Node', ['left', 'right'])):
    """
    1*)создание дерева с двумя потомками кодирующие левую сторону 0 и правую сторону 1
    """
    def walk(self, encoding, binary_code):
        self.left.walk(encoding, binary_code + '0')
        self.right.walk(encoding, binary_code + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    """
    2*)каждый символ кодируется рекурсивно накопленным двоичным кодом
    """
    def walk(self, encoding, binary_code):
        encoding[self.char] = binary_code or '0'


def hoffman_encoding_oop(s: str) -> dict:
    """
    рассмотрим написание кодиирования Хоффмана используя ООП
    ____________________________________________________________________________
    1*) напишем для начала класс кодирующий бинарное дерево Node
    2*) крайний случай: если в строке есть только один тип символов, он кодируется нулем
    3*) len(heap) используется для правильного сравнения элементов
    4*) второй элемент в куяк всегда уникальный
    5*) Node(left, right) - новые узлы накапливают иинформацию о своих потомках
    6*) рекурсивная прогулка по всему дереву
    ____________________________________________________________________________
    :param s: строка получаем на вход для кодирования
    :return: словарь с зашифрованными буквами
    """
    heap = []
    for freq, char in Counter(s).items():
        heap.append((char, len(heap), Leaf(char)))
    heapq.heapify(heap)
    count = len(heap)

    while len(heap) >= 2:
        min_freq, _min_count, left = heapq.heappop(heap)
        min2_freq, _min2_count, right = heapq.heappop(heap)

        heapq.heappush(heap, (min_freq + min2_freq, count, Node(left, right)))
        count += 1

    encoding_dict = {}
    if heap:
        [(_freq, _count, root)] = heap
        root.walk(encoding_dict, '')

    return encoding_dict


def hoffman_encoding_func(s: str) -> dict:
    """
    Функциональный подход к написанию кодирования Хоффмана
    ____________________________________________________________________________
    1)после создания словаря генерируем список состоящий из всех символов стороки
    2)генерируем кучу далее устанавливаем крайний случай при len(s) == 1
    достаем элемент и кладем значение символа в словарь со значение 0
    3) (min_char + min2_char) - новые узлы накапливают информацию о своих потомках
    4) 0 для min_char, 1 для min2_char
    5) код каждого потомка начинается с 0/1
    ____________________________________________________________________________
    :param s: строка получаем на вход для кодирования
    :return: словарь с зашифрованными буквами
    """
    encoding_dict = {}
    heap = [(freq, char) for char, freq in Counter(s).items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        _freq, char = heapq.heappop(heap)
        encoding_dict[char] = str(0)

    while len(heap) >= 2:
        min_freq, min_char = heapq.heappop(heap)
        min2_freq, min2_char = heapq.heappop(heap)

        heapq.heappush(heap, (min_freq + min2_freq, min_char + min2_char))

        for i, char_string in enumerate([min_char, min2_char]):
            for char in char_string:
                if char in encoding_dict:
                    encoding_dict[char] = str(i) + encoding_dict[char]
                else:
                    encoding_dict[char] = str(i)
    return encoding_dict


def main():
    s = input()
    encoding_dict = hoffman_encoding_func(s)
    # encoding_dict = hoffman_encoding_oop(s)

    encoding_str = ''.join([encoding_dict[char] for char in s])
    print(len(encoding_dict), len(encoding_str))
    for value, key in sorted(encoding_dict.items()):
        print(f'{key}: {value}')
    print(encoding_str)


if __name__ == '__main__':
    main()
