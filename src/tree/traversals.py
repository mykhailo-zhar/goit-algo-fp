from collections import deque

from .tree import Node


def brighten_color(rgb: tuple, factor=0.1):
    return tuple(int(r + (255 - r) * factor) for r in rgb)


def rgb_to_hex(rgb):
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


INITIAL_COLOR = (10, 10, 10)


def bfs(tree: Node, value = None):
    """
    Breadth first search. Brightens the nodes during the search.

    Args:
        tree (Node): Tree to search
        value (Any): Value of the tree

    Returns:
        Node: Tree node with value
    """

    nodes = deque([tree])

    color = INITIAL_COLOR

    while nodes:
        node = nodes.pop()
        node.color = rgb_to_hex(color)
        color = brighten_color(color)

        if node.val == value:
            node.color = "#FF0000"
            return node

        if node.left:
            nodes.appendleft(node.left)
        if node.right:
            nodes.appendleft(node.right)

    return None


def dfs(tree: Node, value = None):
    """
    Depth first search. Brightens the nodes during the search.

    Args:
        tree (Node): Tree to search
        value (Any): Value of the tree

    Returns:
        Node: Tree node with value
    """
    nodes = deque([tree])

    color = INITIAL_COLOR

    while nodes:
        node = nodes.popleft()
        node.color = rgb_to_hex(color)
        color = brighten_color(color)

        if node.val == value:
            node.color = "#FF0000"
            return node

        if node.left:
            nodes.appendleft(node.left)
        if node.right:
            nodes.appendleft(node.right)

    return None
