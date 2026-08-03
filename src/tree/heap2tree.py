import heapq
from typing import Any

from .tree import Node


def heap_to_tree(heap: list[Any]) -> Node:
    if not heap:
        return None
    local_heap = heap[:]
    heapq.heapify(local_heap)

    nodes = [Node(x) for x in local_heap]

    j = 0
    for i in range(1, len(local_heap)):
        if i % 2 == 1:
            nodes[j].left = nodes[i]
        else:
            nodes[j].right = nodes[i]
            j += 1

    return nodes[0]
