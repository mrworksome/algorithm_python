
"""
Создаем класс для шифрования шифром Цезаря
"""


class CaesarCipher:
    def __init__(self, shift: int):
        """
        :param shift: сдвиг алфавита на определенную длину
        """
        encoder = ['0' for _ in range(26)]
        decoder = ['0' for _ in range(26)]
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message: str):
        """
        :param message: сообщение
        :return: декодирование сообщение
        """
        return self._transform(message, self._forward)

    def decrypt(self, secret_msg: str):
        """
        :param secret_msg: заштфрованное сообщение
        :return: декодирование сообщение
        """
        return self._transform(secret_msg, self._backward)

    @staticmethod
    def _transform(original: str, code: str):
        """
        Утилита для выполнения преобразования на основе заданной строки кода.
        :param original: получаемая строка
        :param code:
        :return: str
        """
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index 0 - 25
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    first_msg = 'THE EAGLE IS IN PLAY; MEET AT JOE S.'
    coded = cipher.encrypt(first_msg)
    print('Secret msg: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)
