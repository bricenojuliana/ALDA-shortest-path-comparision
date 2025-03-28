import time
import os
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from typing import Dict, List, Tuple
from collections import defaultdict

from algorithms import dijkstra
from algorithms import bellman_ford
from algorithms import astar
from data_generator import generate_benchmark_graphs
from config import BENCHMARK_CONFIG

class Benchmark:
    def __init__(self):
        self.results = defaultdict(list)
        self.graphs = []
        self.positions = []
    
    def generate_test_data(self):
        """Generate test graphs based on configuration"""
        self.graphs = generate_benchmark_graphs()
    
    def run_algorithm(self, algorithm: str, graph: Dict, start_node: int = 0, target_node: int = None, positions: Dict = None):
        """Run a single algorithm and measure execution time"""
        start_time = time.perf_counter()
        
        if algorithm == "dijkstra":
            result = dijkstra(graph, start_node)
        elif algorithm == "bellman_ford":
            result = bellman_ford(graph, start_node)
        elif algorithm == "astar":
            if target_node is None:
                target_node = len(graph) - 1  # Default to last node
            result = astar(graph, start_node, target_node, positions)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")
        
        execution_time = time.perf_counter() - start_time
        return result, execution_time
    
    def run_benchmark(self):
        """Run the full benchmark suite"""
        self.generate_test_data()
        
        for i, (graph, positions) in enumerate(tqdm(self.graphs, desc="Benchmark Progress")):
            size = len(graph)
            for algorithm in BENCHMARK_CONFIG["algorithms"]:
                times = []
                for _ in range(BENCHMARK_CONFIG["iterations"]):
                    _, exec_time = self.run_algorithm(
                        algorithm, 
                        graph, 
                        start_node=0,
                        target_node=size-1,
                        positions=positions
                    )
                    times.append(exec_time)
                
                median_time = np.median(times)
                self.results[algorithm].append((size, median_time))
    
    def plot_results(self):
        """Plot the benchmark results and save to file"""
        plt.figure(figsize=(10, 6))
        
        for algorithm in BENCHMARK_CONFIG["algorithms"]:
            sizes, times = zip(*self.results[algorithm])
            plt.plot(sizes, times, 'o-', label=algorithm.capitalize())
        
        plt.xlabel('Graph Size (Number of Nodes)')
        plt.ylabel('Median Execution Time (seconds)')
        plt.title('Shortest Path Algorithms Performance Comparison')
        plt.legend()
        plt.grid(True)
        
        # Save in all requested formats
        for fmt in BENCHMARK_CONFIG["plot_formats"]:
            plot_path = os.path.join(BENCHMARK_CONFIG["output_dir"], f"performance_comparison.{fmt}")
            plt.savefig(plot_path, format=fmt, bbox_inches='tight')
        
        plt.close()
    
    def save_results(self):
        """Save raw benchmark results to a text file"""
        result_path = os.path.join(BENCHMARK_CONFIG["output_dir"], "benchmark_results.txt")
        with open(result_path, 'w') as f:
            for algorithm in BENCHMARK_CONFIG["algorithms"]:
                f.write(f"{algorithm.upper()} Results:\n")
                for size, time in self.results[algorithm]:
                    f.write(f"  Nodes: {size}, Time: {time:.6f}s\n")
                f.write("\n")

def run_full_benchmark():
    """Run the complete benchmark process"""
    benchmark = Benchmark()
    benchmark.run_benchmark()
    benchmark.plot_results()
    benchmark.save_results()
    print("Benchmark completed successfully!")