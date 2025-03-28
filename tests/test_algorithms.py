import pytest
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.astar import astar


@pytest.fixture
def sample_graph():
    # A simple graph for testing
    return {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }

@pytest.fixture
def sample_graph_positions():
    # Positions for A* heuristic
    return {
        0: (0, 0),
        1: (1, 1),
        2: (1, -1),
        3: (2, 0)
    }

def test_dijkstra(sample_graph):
    distances = dijkstra(sample_graph, 0)
    assert distances == {0: 0, 1: 3, 2: 1, 3: 4}

def test_bellman_ford(sample_graph):
    distances = bellman_ford(sample_graph, 0)
    assert distances == {0: 0, 1: 3, 2: 1, 3: 4}

def test_astar(sample_graph, sample_graph_positions):
    distances = astar(sample_graph, 0, 3, sample_graph_positions)
    assert distances[3] == 4  # Should match Dijkstra/Bellman-Ford for this simple case

def test_algorithms_consistency(sample_graph, sample_graph_positions):
    """Test that all algorithms produce the same result for a simple graph"""
    dijkstra_dist = dijkstra(sample_graph, 0)
    bf_dist = bellman_ford(sample_graph, 0)
    astar_dist = astar(sample_graph, 0, 3, sample_graph_positions)
    
    # Check that distances to node 3 match
    assert dijkstra_dist[3] == bf_dist[3] == astar_dist[3]