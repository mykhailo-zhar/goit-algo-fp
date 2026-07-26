import random

from src.linked_list import LinkedList


def test_sort_empty():
    linked_list = LinkedList()
    linked_list.sort()
    assert linked_list.to_list() == []


def test_sort(linked_list_generator):
    linked_list = linked_list_generator(5)
    original_list = linked_list.to_list()
    linked_list.sort()
    assert linked_list.to_list() == sorted(original_list)


def test_sort_random(linked_list_generator_custom):
    linked_list = linked_list_generator_custom(5, lambda x: random.randint(1, 100))
    original_list = linked_list.to_list()
    linked_list.sort()
    assert linked_list.to_list() == sorted(original_list)
