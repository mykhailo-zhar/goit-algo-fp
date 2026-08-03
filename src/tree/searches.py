from collections import deque

from .tree import Node


def dim_color(rgb: tuple, factor=0.95):
    return tuple(int(r * factor) for r in rgb)


def rgb_to_hex(rgb):
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def bfs(tree: Node, value):
    nodes = deque([tree])

    color = (255, 255, 255)

    while nodes:
        node = nodes.pop()
        node.color = rgb_to_hex(color)
        color = dim_color(color)

        if node.val == value:
            node.color = "#FF0000"
            return node

        if node.left:
            nodes.appendleft(node.left)
        if node.right:
            nodes.appendleft(node.right)

    return None


def dfs(tree: Node, value):
    nodes = deque([tree])

    color = (255, 255, 255)

    while nodes:
        node = nodes.popleft()
        node.color = rgb_to_hex(color)
        color = dim_color(color)

        if node.val == value:
            node.color = "#FF0000"
            return node

        if node.left:
            nodes.appendleft(node.left)
        if node.right:
            nodes.appendleft(node.right)

    return None
