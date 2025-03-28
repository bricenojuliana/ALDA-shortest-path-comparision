from typing import Dict, List, Tuple

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Bellman-Ford algorithm for shortest paths in a weighted graph (can handle negative weights)
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
        start: Starting node
    
    Returns:
        Dictionary of shortest distances from start to each node
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Relax all edges |V| - 1 times
    for _ in range(len(graph) - 1):
        updated = False
        for node in graph:
            if distances[node] == float('inf'):
                continue
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    updated = True
        if not updated:
            break
    
    # Check for negative weight cycles
    for node in graph:
        if distances[node] == float('inf'):
            continue
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances