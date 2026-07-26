import random
from collections.abc import Callable

import pytest

from src.linked_list import LinkedList
from src.linked_list.node import Node


@pytest.fixture
def node_generator() -> Callable[[], Node]:
    def _generator() -> Node:
        return Node(random.randint(0, 100))

    return _generator


@pytest.fixture
def linked_list_generator(node_generator: Callable[[], Node]) -> LinkedList:
    def _generator(length: int) -> LinkedList:
        linked_list = LinkedList()
        for _ in range(length):
            linked_list.insert_at_end(node_generator())
        return linked_list

    return _generator
