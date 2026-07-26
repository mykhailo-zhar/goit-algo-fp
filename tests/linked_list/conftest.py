import random

import pytest

from src.linked_list import LinkedList


@pytest.fixture
def linked_list_generator() -> LinkedList:
    def _generator(length: int) -> LinkedList:
        linked_list = LinkedList()
        for i in range(length):
            linked_list.insert_at_end(i)
        return linked_list

    return _generator


@pytest.fixture
def linked_list_generator_random() -> LinkedList:
    def _generator(length: int) -> LinkedList:
        linked_list = LinkedList()
        for _ in range(length):
            linked_list.insert_at_end(random.randint(0, 100))
        return linked_list

    return _generator
