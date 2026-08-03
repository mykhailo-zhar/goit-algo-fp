import networkx as nx
import pytest

from src.dijkstra import dijkstra


@pytest.fixture
def graph():
    G = nx.Graph()

    G.add_nodes_from(["A", "B", "C", "D", "E"])
    edge_dict = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4},
    }
    for u, neighbors in edge_dict.items():
        for v, w in neighbors.items():
            G.add_edge(u, v, weight=w)

    return G


def test_dijkstra(graph):
    result = {"A": 0, "B": 5, "C": 10, "D": 8, "E": 12}
    assert dijkstra(graph, "A") == result
