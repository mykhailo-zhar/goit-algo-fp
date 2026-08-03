from collections import deque

from src.tree.heap2tree import heap_to_tree
from src.tree.tree import Node


def traversal(tree: Node):
    nodes = deque([tree])
    while nodes:
        node = nodes.pop()
        if node.left:
            nodes.appendleft(node.left)
        if node.right:
            nodes.appendleft(node.left)

        assert (
            min(
                [
                    node.val,
                    node.left and node.left.val or node.val,
                    node.right and node.right.val or node.val,
                ]
            )
            == node.val
        )


def test_heap_to_tree_from_notes():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    result = heap_to_tree([0, 1, 10, 3, 4, 5])
    assert result.val == 0
    assert result.right.left.val == 10


def test_heap_to_tree():
    nodes = [i for i in range(32, 0, -1)]
    tree = heap_to_tree(nodes)
    traversal(tree)
