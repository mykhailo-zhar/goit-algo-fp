import pytest


@pytest.mark.parametrize("a,b", [[5, 2], [2, 5], [1, 1]])
def test_merge(a, b, linked_list_generator):
    list_a = linked_list_generator(a)
    list_b = linked_list_generator(b)

    a, b = list_a.to_list(), list_b.to_list()

    list_a.merge_with(list_b)

    assert list_a.to_list() == sorted(a + b)


@pytest.mark.parametrize("a,b", [[5, 2], [2, 5], [1, 1]])
def test_merge_random(a, b, linked_list_generator_random):
    list_a = linked_list_generator_random(a)
    list_b = linked_list_generator_random(b)

    list_a.sort()
    list_b.sort()

    a, b = sorted(list_a.to_list()), sorted(list_b.to_list())

    list_a.merge_with(list_b)

    assert list_a.to_list() == sorted(a + b)
