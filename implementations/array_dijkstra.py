from helper_funcs import *
from typing import List
import math
import timeit

def minDistance(dist, pq) -> int:
    """Function to perform EXTRACT_MIN operation on the underlying
    array representation of the priority queue.

    ref: https://www.programiz.com/dsa/dijkstra-algorithm
    
    Args:
    - dist: the list maintaining the minimum distances
    - pq: the priority queue
  
    Returns:
    The integer index corresponding to the minimum vertex.
    """

    # Initialize minimum distance for next node
    min = math.inf

    # do linear search for min distance node
    for u in range(len(dist)):
        # must have min distance and must be unvisited
        if dist[u] < min and pq[u] == False:
            min = dist[u]
            min_index = u

    return min_index
 

def dijkstra(graph, src) -> List[int]:
    """Array-based implementation of Dijkstra's algorithm.

    ref: https://www.programiz.com/dsa/dijkstra-algorithm
    
    Args:
    - graph: the weighted directed input graph
    - src: the source vertex
  
    Returns:
    The list corresponding to the minimum distances from the source.
    """

    # number of vertices
    n = len(graph)
    
    # initialize the distances and pq    
    dist = [math.inf] * n
    dist[src] = 0
    pq = [False] * n

    # iterate |V| - 1 times
    for _ in range(n):
        # extract the min node
        x = minDistance(dist, pq)

        # mark the node as visited
        pq[x] = True

        # for all vertices adjacent to this node
        for adjNode, weight in graph[str(x)].items():
            if pq[int(adjNode)] == True:
                continue
            
            newCost = dist[x] + weight['weight']
            if dist[int(adjNode)] > newCost:
                # relax the edge
                dist[int(adjNode)] = newCost

    return dist

# driver code
if __name__ == "__main__":
    # list to record times
    dijkstra_times = []
    n_vertices = [i for i in range(10, 3510, 10)]

    # execute all the tests
    for n in n_vertices:
        print("Start {}".format(n))
        # load the graph
        graph = read_graph(int(n / 10))

        # setup timer
        total_time = 0
        total_time += timeit.timeit(lambda: dijkstra(graph, 0), number=1)

        dijkstra_times.append(total_time)

        print("Done {}".format(n))

    write_file(n_vertices, dijkstra_times, "array_dijkstra_timing_results_dense")