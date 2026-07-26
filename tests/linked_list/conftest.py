from collections.abc import Callable

import pytest

from src.linked_list import LinkedList


@pytest.fixture
def linked_list_generator(linked_list_generator_custom) -> LinkedList:
    def _generator(length: int) -> LinkedList:
        return linked_list_generator_custom(length, lambda x: x)

    return _generator


@pytest.fixture
def linked_list_generator_custom() -> LinkedList:
    def _generator(length: int, callable: Callable[[int], int]) -> LinkedList:
        linked_list = LinkedList()
        for i in range(length):
            linked_list.insert_at_end(callable(i))
        return linked_list

    return _generator
