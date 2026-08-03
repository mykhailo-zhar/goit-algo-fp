import heapq
from dataclasses import dataclass
from typing import Self

import networkx as nx


@dataclass
class NodeInfo:
    node: str = None
    distance: float = float("inf")

    def __lt__(self, other: Self):
        return self.distance < other.distance

    def __gt__(self, other: Self):
        return self.distance > other.distance

    def __repr__(self) -> str:
        return f"NodeInfo({self.node.__repr__(), self.distance})"


def dijkstra(G: nx.Graph, vertex):
    """
    Dijkstra algorithm

    Args:
        G (nx.Graph): A graph
        vertex (node): A node to calculate distances from

    Returns:
        dict[node, float]: A dictionary of distances to nodes
    """
    # Convert every node in graph to a dictionary with vertecies
    distances = {node: NodeInfo(node, float("inf")) for node in G.nodes}
    distances[vertex].distance = 0

    # Convert vertecies list to heap
    unvisited = list(distances.values())

    while unvisited:
        # Every vertex on heap already has knowledge about their distance
        # Optimized from O(N) using min linear search to O(logN) using heap
        heapq.heapify(unvisited)
        current_vertex: NodeInfo = heapq.heappop(unvisited)

        if current_vertex.distance == float("inf"):
            break

        for _, neighbor, weight in G.edges(nbunch=current_vertex.node, data="weight"):
            new_distance = current_vertex.distance + weight

            if new_distance < distances[neighbor].distance:
                distances[neighbor].distance = new_distance

    return {vertex.node: vertex.distance for vertex in distances.values()}
