import random
from typing import Dict, List, Tuple
import networkx as nx
import numpy as np
from config import BENCHMARK_CONFIG

def generate_random_graph(
    num_nodes: int, 
    density: float, 
    weight_range: Tuple[int, int] = (1, 10),
    allow_negative: bool = False
) -> Tuple[Dict[int, List[Tuple[int, int]]], Dict[int, Tuple[float, float]]]:
    """
    Generate a random graph with node positions (for A* heuristic)
    
    Args:
        num_nodes: Number of nodes in the graph
        density: Probability of edge creation between nodes
        weight_range: Range for random edge weights
        allow_negative: Whether to allow negative edge weights
    
    Returns:
        Tuple of (adjacency_list, node_positions)
    """
    G = nx.gnp_random_graph(num_nodes, density, directed=True)
    adjacency_list = {node: [] for node in range(num_nodes)}
    
    min_weight, max_weight = weight_range
    node_positions = {node: (random.uniform(0, 100), random.uniform(0, 100)) for node in range(num_nodes)}
    
    for u, v in G.edges():
        if allow_negative:
            weight = random.randint(-max_weight, max_weight)
            while weight == 0:  # Ensure no zero-weight edges
                weight = random.randint(-max_weight, max_weight)
        else:
            weight = random.randint(min_weight, max_weight)
        adjacency_list[u].append((v, weight))
    
    return adjacency_list, node_positions

def generate_benchmark_graphs():
    """Generate graphs based on benchmark configuration"""
    graphs = []
    for size in BENCHMARK_CONFIG["graph_sizes"]:
        density = random.uniform(*BENCHMARK_CONFIG["density_range"])
        weight_range = BENCHMARK_CONFIG["weight_range"]
        graph, positions = generate_random_graph(size, density, weight_range)
        graphs.append((graph, positions))
    return graphs