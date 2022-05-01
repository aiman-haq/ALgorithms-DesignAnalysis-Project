from collections import defaultdict
from typing import List
from helper_funcs import *
import timeit

def bellman_ford(graph, src) -> List[int]:
    """Bellman-Ford algorithm.

    Args:
    - graph: the weighted directed graph
    - src: the soruce vertex
  
    Returns:
    The list corresponding to the minimum distances from the soruce
    """

    # intialize the distance array and predecessor array
    dist = defaultdict(lambda: float('inf'))
    
    # Mark the source vertex
    dist[src] = 0

    # relax edges |V| - 1 times
    for _ in range(len(graph)):
        # for each edge in the graph
        for s, adj_lst in graph.items():
            for adj_node, w in adj_lst.items():
                # relax the edge
                if dist[s] != float("Inf") and dist[s] + w['weight'] < dist[adj_node]:
                    dist[adj_node] = dist[s] + w['weight']

    # detect negative cycle
    for s, adj_lst in graph.items():
        for adj_node, w in adj_lst.items():
            if dist[s] != float("Inf") and dist[s] + w['weight'] < dist[adj_node]:
                print("Graph contains negative weight cycle")
                return

    # no negative weight cycle found
    return dist  
    
# driver code
if __name__ == "__main__":
    # list to record times
    bford_times = []
    n_vertices = [i for i in range(10, 1200, 10)]

    # execute all the tests
    for n in n_vertices:
        print("Start {}".format(n))
        # load the graph
        graph = read_graph(int(n / 10))

        # setup timer
        total_time = 0
        total_time += timeit.timeit(lambda: bellman_ford(graph, '0'), number=1)

        bford_times.append(total_time)

        print("Done {}".format(n))

    write_file(n_vertices, bford_times, "bford_timing_results_dense")