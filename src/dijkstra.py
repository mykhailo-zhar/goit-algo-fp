import heapq

import networkx as nx


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
    distances = {node: float("inf") for node in G.nodes}
    distances[vertex] = 0

    # Convert vertecies list to heap
    unvisited = [(0, vertex)]

    while unvisited:
        # Every vertex on heap already has knowledge about their distance
        # Optimized from O(N) using min linear search to O(logN) using heap
        current_distance, current_vertex = heapq.heappop(unvisited)

        if current_distance == float("inf"):
            break

        for _, neighbor, weight in G.edges(nbunch=current_vertex, data="weight"):
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(unvisited, (new_distance, neighbor))

    return distances
