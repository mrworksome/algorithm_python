# Python3
"""
Дополнительный материал к задаче:
работа со словарями
https://www.ibm.com/developerworks/ru/library/l-python_part_4/index.html
https://stackoverflow.com/a/509295/1587961﻿

Задача: декодирование Хаффмана
Восстановите строку по её коду и беспрефиксному коду символов.
В первой строке входного файла заданы два целых числа k и l через пробел
— количество различных букв, встречающихся в строке, и размер получившейся
закодированной строки, соответственно. В следующих k строках записаны коды букв
в формате "letter: code". Ни один код не является префиксом другого. Буквы могут
быть перечислены в любом порядке. В качестве букв могут встречаться лишь
строчные буквы латинского алфавита; каждая из этих букв встречается в строке
хотя бы один раз. Наконец, в последней строке записана закодированная
строка. Исходная строка и коды всех букв непусты. Заданный код таков, что
закодированная строка имеет минимальный возможный размер.
В первой строке выходного файла выведите строку s. Она должна состоять из
строчных букв латинского алфавита. Гарантируется, что длина правильного ответа
не превосходит 10^4 символов.

Sample Input 1:
1 1
a: 0
0
Sample Output 1:
a

Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
Sample Output 2:
abacabad
"""


# альтернативное решение задачи используя метод строки .startswith()
# count_char, len_str = map(int, input().split())
# encoding_dict = {}
# for _ in range(count_char):
#     key, value = input().split(':')
#     encoding_dict[key] = value.strip()
# encoding_str = input()
# while len(encoding_str):
#     for key in encoding_dict:
#         if encoding_str.startswith(encoding_dict[key]):
#             print(key, sep='', end='')
#             encoding_str = encoding_str[len(encoding_dict[key]):]


def hoffman_decode(hoffman_table, encoding_str):
    """
    ____________________________________________________________________________
    при приеме переменных мы разворачиваем наш hoffman_table для того чтобы
    мы могли итерироваться по кодированным значениям и потом смогли
    достать значение кодирования

    1) создаем две пустые строки в которые будем записывать декодиированную стр
    и последовательность из символов строки
    2) итерируемся по строке добавляя каждый символ в нашу последовательность
    3) если полученная последовательность есть в нашем словаре то записываем её
    в decode_str
    ____________________________________________________________________________
    :param hoffman_table: словарь со значениями кодировки
    :param encoding_str: закодированная строка
    :return: декодированную строку
    """
    decode_str = ''
    sequence = ''
    for char in encoding_str:
        sequence += char
        if sequence in list(hoffman_table.keys()):
            decode_str += hoffman_table.get(sequence)
            sequence = ''
    return decode_str


def main():
    k, _l = map(int, input().split())
    hoffman_table = dict(input().split(': ')[::-1] for _ in range(k))
    encoding_str = input()
    print(hoffman_decode(hoffman_table, encoding_str))


if __name__ == '__main__':
    main()

