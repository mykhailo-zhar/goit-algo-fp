import pytest

from src.tree.heap2tree import heap_to_tree
from src.tree.searches import bfs, dfs


@pytest.fixture
def tree():
    arr = [i for i in range(32)]
    return heap_to_tree(arr)


@pytest.mark.parametrize("search_algorithm", [bfs, dfs])
def test_search(search_algorithm, tree):

    assert search_algorithm(tree, 31).val == 31
