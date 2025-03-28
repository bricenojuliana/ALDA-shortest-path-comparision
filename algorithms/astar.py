import heapq
from typing import Dict, List, Tuple, Callable
from math import sqrt
from config.settings import PATH_FINDING_CONFIG

def euclidean_heuristic(node: int, target: int, node_positions: Dict[int, Tuple[float, float]]) -> float:
    """Euclidean distance heuristic for A* algorithm"""
    x1, y1 = node_positions.get(node, (0, 0))
    x2, y2 = node_positions.get(target, (0, 0))
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def astar(
    graph: Dict[int, List[Tuple[int, int]]], 
    start: int, 
    target: int,
    node_positions: Dict[int, Tuple[float, float]] = None,
    heuristic: Callable = None
) -> Dict[int, int]:
    """
    A* algorithm for shortest path between start and target nodes
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
        start: Starting node
        target: Target node
        node_positions: Optional dictionary of node coordinates for heuristic
        heuristic: Optional heuristic function (defaults to Euclidean if node_positions provided)
    
    Returns:
        Dictionary of shortest distances from start to each visited node
    """
    if heuristic is None and node_positions is not None:
        heuristic = lambda n: euclidean_heuristic(n, target, node_positions)
    elif PATH_FINDING_CONFIG["heuristic"] == "euclidean" and node_positions is not None:
        heuristic = lambda n: euclidean_heuristic(n, target, node_positions)
    else:
        heuristic = lambda n: 0  # Default to Dijkstra if no heuristic
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start)
    
    came_from = {}
    distances = {start: 0}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == target:
            break
            
        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                distances[neighbor] = tentative_g_score
    
    return distances