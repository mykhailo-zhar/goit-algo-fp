from typing import Any, Self

from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        self.length += 1
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            self.length -= 1
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        self.length -= 1
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        """Реверсує однозв'язний список, змінюючи посилання між вузлами."""
        current, prev, node = self.head, None, None
        if current is None:
            return

        while current:
            node = current
            current = current.next

            node.next = prev
            prev = node

        self.head = prev

    def __get_j_node(self, starting_node: Node, unsorted_node: Node) -> Node:
        cur = starting_node
        while cur.next != unsorted_node:
            cur = cur.next
        return cur

    def sort(self):
        """Сортує однозв'язний список алгоритмом сортування вставками."""

        if not (self.head and self.head.next):
            return

        j_node = self.head
        unsorted_node = self.head.next
        while unsorted_node:
            # Обрати вузол який потрібно відортувати
            key = unsorted_node

            # Переходимо до наступної unsorted_node
            unsorted_node = unsorted_node.next

            if j_node.data < key.data:
                j_node = key
                continue

            # Направляємо передостанню ноду на нову несортовану
            j_node.next = unsorted_node

            # Починаємо з початку Linked list для пошуку insertion
            last_node = None
            current_node = self.head

            # Знаходимо першу вузол, що задовільняє умові
            while key.data > current_node.data:
                last_node = current_node
                current_node = current_node.next

            # Шукаємо новий передостанній вузол після місця де ми вставили key
            j_node = self.__get_j_node(current_node, unsorted_node)

            # Вставляємо node
            key.next = current_node
            if last_node:
                last_node.next = key
                continue

            # У випадку відсутності передостаннього вузла: key - старт списку
            self.head = key

    def merge_with(self, other: Self):
        """Об'єднує поточний відсортований список з іншим у один відсортований.

        Args:
            other: інший відсортований однозв'язний список.
        """
        a_node = self.head
        b_node = other.head

        if not b_node:
            return
        if not a_node:
            self.head = b_node
            return

        last: Node = None

        # При перевірці даних на початку приймаємо рішення з вузла якого списку починати merge
        if a_node.data <= b_node.data:
            last = a_node
            a_node = a_node.next
        else:
            self.head = b_node
            last = b_node
            b_node = b_node.next

        while a_node and b_node:
            if a_node.data <= b_node.data:
                # Попередній вузол посилається на поточний
                # Поточний стає попереднім
                last.next = a_node
                last = a_node
                a_node = a_node.next
            else:
                last.next = b_node
                last = b_node
                b_node = b_node.next

        # На відміну від масивів, якщо залишаються елементи то достатньо перекинути вузол на таку node
        if a_node:
            last.next = a_node

        if b_node:
            last.next = b_node

    def to_list(self) -> list[Any]:
        cur = self.head
        result = []
        while cur:
            result.append(cur.data)
            cur = cur.next

        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
