from src.linked_list import LinkedList


def test_reverse_empty_list():
    linked_list = LinkedList()
    linked_list.reverse()
    assert linked_list.to_list() == []


def test_reverse_single_element_list(linked_list_generator):
    linked_list = linked_list_generator(1)
    linked_list.reverse()
    assert linked_list.to_list() == linked_list.to_list()


def test_reverse_multiple_elements_list(linked_list_generator_random):
    linked_list = linked_list_generator_random(5)
    original_list = linked_list.to_list()
    linked_list.reverse()
    assert linked_list.to_list() == original_list[::-1]
