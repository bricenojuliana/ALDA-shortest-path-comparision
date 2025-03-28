import time
import statistics
from typing import Callable, Any, Tuple  # Added Tuple import here
from benchmark.benchmark import run_full_benchmark
from config.settings import BENCHMARK_CONFIG, ensure_output_dir_exists

def measure_execution_time(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """Measure execution time of a function"""
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return result, end_time - start_time

def run_with_median_time(func: Callable, iterations: int = 5, *args, **kwargs) -> Tuple[Any, float]:
    """Run a function multiple times and return the median execution time"""
    times = []
    results = []
    
    for _ in range(iterations):
        result, exec_time = measure_execution_time(func, *args, **kwargs)
        results.append(result)
        times.append(exec_time)
    
    # Return the first result (assuming deterministic functions) and median time
    return results[0], statistics.median(times)

def main():
    ensure_output_dir_exists()
    print("Starting shortest path algorithms comparison...")
    
    # Run the benchmark
    _, total_time = run_with_median_time(
        run_full_benchmark,
        iterations=1,  # The benchmark already does multiple iterations internally
    )
    
    print(f"\nBenchmark completed in {total_time:.2f} seconds")
    print(f"Results saved to: {BENCHMARK_CONFIG['output_dir']}")

if __name__ == "__main__":
    main()