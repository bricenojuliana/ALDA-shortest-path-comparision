import os
from typing import List, Dict, Tuple

# Benchmark configurations
BENCHMARK_CONFIG = {
    "graph_sizes": [10, 20, 30, 40, 50, 75, 100, 150, 200, 300, 400, 500, 750, 1000],  # More frequent increments
    "density_range": (0.1, 0.3),              # Slightly reduced density for larger graphs
    "weight_range": (1, 100),                 # Edge weight range
    "iterations": 3,                          # Reduced iterations for faster benchmarking
    "algorithms": ["dijkstra", "bellman_ford", "astar"],
    "output_dir": os.path.join(os.path.dirname(__file__), "../benchmark/results"),
    "plot_formats": ["png", "svg"],
    "timeout": 60,                            # Timeout in seconds per algorithm per graph
}

# Path finding configurations
PATH_FINDING_CONFIG = {
    "heuristic": "euclidean",
    "default_start_node": 0,                  # Always start from node 0
    "default_target_ratio": 0.9,              # Target node at 90% of graph size
}

def ensure_output_dir_exists():
    """Ensure the benchmark output directory exists"""
    os.makedirs(BENCHMARK_CONFIG["output_dir"], exist_ok=True)