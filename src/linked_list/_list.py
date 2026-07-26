from typing import Any, Self

from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
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

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        """
        Reverses linked list
        """
        current, prev, node = self.head, None, None
        if current is None:
            return

        while current:
            node = current
            current = current.next

            node.next = prev
            prev = node

        self.head = prev

    def sort(self):
        """
        Sorts the linked list using insertion sort
        """

        if not (self.head and self.head.next):
            return

        nodes = self.to_node_list()
        N = len(nodes)
        for i in range(1, N):
            j = i - 1
            key = nodes[i]
            while j >= 0 and key.data < nodes[j].data:
                nodes[j + 1] = nodes[j]
                j -= 1
            nodes[j + 1] = key

        self.__reorder_list(nodes)

    def merge_with(self, other: Self):
        """
        Merges current list with the other

        Args:
            other (Self): Other linked list to merge
        """
        nodes = []
        part_a = self.to_node_list()
        part_b = other.to_node_list()

        i, j = 0, 0

        while i < len(part_a) and j < len(part_b):
            if part_a[i].data <= part_b[j].data:
                nodes.append(part_a[i])
                i += 1

            else:
                nodes.append(part_b[j])
                j += 1

        if i < len(part_a):
            nodes += part_a[i:]
        if j < len(part_b):
            nodes += part_b[j:]

        self.__reorder_list(nodes)

    def __reorder_list(self, nodes: list[Node]):
        """
        Reorders the list based on the list of nodes

        Args:
            nodes (list[Node]): the list of nodes for reordering
        """
        if not nodes:
            return

        current = nodes[0]
        for i in range(1, len(nodes)):
            current.next = nodes[i]
            current = nodes[i]

        nodes[-1].next = None
        self.head = nodes[0]

    def to_node_list(self) -> list[Node]:
        result = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return result

    def to_list(self) -> list[Any]:
        return [node.data for node in self.to_node_list()]

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
