from src.tree.heap2tree import heap_to_tree
from src.tree.tree import Node


def test_tree_from_heap_notes():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    result = heap_to_tree([0, 1, 10, 3, 4, 5])
    assert result.val == 0
    assert result.right.left.val == 10
