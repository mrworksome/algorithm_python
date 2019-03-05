"""
Задача:Скобки в коде

Проверить, правильно ли расставлены скобки в данном коде.
Вход. Исходный код программы.
Выход. Проверить, верно ли расставлены скобки. Если нет, выдать индекс первой ошибки.

Вы разрабатываете текстовый редактор для программистов и хотите реализовать
проверку корректности расстановки скобок. В коде могут встречаться скобки []{}().
Из них скобки [,{ и ( считаются открывающими, а соответству- ющими им
закрывающими скобками являются ],} и ). В случае, если скобки расставлены
неправильно, редактор должен также сообщить пользователю первое место, где
обнаружена ошибка. В первую очередь необходимо найти закрывающую скобку, для
которой либо нет соответствующей открывающей (например, скобка ] в строке “]()”),
либо же она закрывает не соответствующую ей откры- вающую скобку (пример: “()[}”).
Если таких ошибок нет, необходи- мо найти первую открывающую скобку, для которой
нет соответствующей закрывающей (пример: скобка ( в строке “{}([]”).
Помимо скобок, исходный код может содержать символы латин- ского алфавита,
цифры и знаки препинания.

"""


def check_brackets(sequence):
    """
    1) создаем словарь из скобок который будем проверять
    2) если
    :param sequence: последовательность(проверяемая строка)
    :return: номер вхождения в котором выявлена ошибка или все верно
    """
    dict_brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    first_left_brackets_pos = 0

    for i, char in enumerate(sequence, 1):
        if char in dict_brackets.values():
            stack.append(char)

            if first_left_brackets_pos == 0:
                first_left_brackets_pos = i

        elif char in dict_brackets:
            if (not stack) or dict_brackets[char] != stack.pop():
                return i

            if not stack:
                first_left_brackets_pos = 0

    return first_left_brackets_pos if stack else "Success"


def main():
    sequence = input()
    print(check_brackets(sequence))


if __name__ == '__main__':
    main()
