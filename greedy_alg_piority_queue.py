# Python 3
"""
Дополнительный материал к задаче:
https://www.intuit.ru/studies/courses/100/100/lecture/2927
https://docs.python.org/3/library/heapq.html




Задача: очередь с приоритетами
Первая строка входа содержит число операций 1 ≤ n ≤ 10^5. Каждая из последующих
n строк задает операцию одного из следующих двух типов:
Insert x, где 0 ≤ x ≤ 10^9 — целое число;
ExtractMax.
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает
максимальное число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:
200
500

"""
import sys
import heapq
import random


class PriorityQueueHandMade:
    queue = []

    def _shift_down(self, i):
        """
        операция просеивания вниз по d-ичному дереву
        Time complexity: O(log(n)), where n = len(self.queue)
        """
        while 2 * i + 1 < len(self.queue):
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2
            j = left_child_index

            if right_child_index < len(self.queue) and self.queue[right_child_index] > self.queue[left_child_index]:
                j = right_child_index

            if self.queue[i] >= self.queue[j]:
                break

            self.queue[j], self.queue[i] = self.queue[i], self.queue[j]
            i = j

    def _shift_up(self, i: int):
        """
        операция просеивания вверх
        Time complexity: O(log(n)), where n = len(self.queue)
        :param i:
        :return:
        """
        while self.queue[i] > self.queue[int((i - 1) / 2)]:
            self.queue[i], self.queue[int((i - 1) / 2)] = self.queue[int((i - 1) / 2)], self.queue[i]
            i = int((i - 1) / 2)

    def insert(self, priority):
        """
        используем вставку в конец и просеиваем в вверх
        :param priority: приоритет вставки
        """
        self.queue.append(priority)
        self._shift_up(len(self.queue) - 1)

    def extract_max(self):
        """
        извлекаем максимум из нашей кучи
        :return:
        """
        max_queue = self.queue[0]
        self.queue[0] = self.queue[-1]
        del self.queue[-1]
        self._shift_down(0)
        return max_queue


class PriorityQueueStandardLibrary:
    """
    1) после создания массива, преобразуем его в кучу
    2) далее по средствам метода .heappush() помещаем значение в кучу и сохраняем
    инвариантное значение кучи (- priority) потому что у нас мин куча
    3) и чтобы вытащить максимальное значениие достаем из кучи (- минимальное значение кучи)
    """
    queue = []
    heapq.heapify(queue)

    def insert(self, priority):
        heapq.heappush(self.queue, -priority)

    def extract_max(self):
        return -heapq.heappop(self.queue)


def tester(n_iter = 100):
    commands_list = ['Insert', 'ExtractMax']
    for i in range(n_iter):
        n = random.randint(0, 10 ** 5)

        priority_queue_hand_made = PriorityQueueHandMade()
        priority_queue_standard = PriorityQueueStandardLibrary()

        for _ in range(n):
            line = random.choice(commands_list)

            if line == 'Insert':
                value = random.randint(0, 10 ** 5)
                priority_queue_hand_made.insert(value)
                priority_queue_standard.insert(value)
            else:
                len_1 = len(priority_queue_hand_made.queue)
                len_2 = len(priority_queue_standard.queue)

                if (len_1 == 0 and len_2 != 0) or (len_1 != 0 and len_2 == 0):
                    raise RuntimeError

                if len_1 > 0 and len_2 > 0:
                    assert priority_queue_hand_made.extract_max() == priority_queue_standard.extract_max()

        print('Successful iteration!')


def main():
    priority_queue = PriorityQueueHandMade()
    # priority_queue = PriorityQueueStandardLibrary()
    n_ = input()
    for line in sys.stdin.readlines():

        if line.startswith('Insert'):
            _command, n = line.split()
            priority_queue.insert(int(n))
        else:
            print(priority_queue.extract_max())


if __name__ == '__main__':
    main()
    # tester()


