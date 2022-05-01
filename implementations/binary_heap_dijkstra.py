from helper_funcs import *
from collections import defaultdict
from typing import Dict, List
import timeit
import heapq as heap

def dijkstra(G, startingNode) -> Dict[int, int] & List[int]:
	"""Binary-heap based implementation of Dijkstra's 
	algorithm.

    Args:
    - G: the weighted directed graph
    - startingNode: the source vertex
  
    Returns:
    The list corresponding to the minimum distances from the soruce
    """

	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode))
 
	while pq:
		# go greedily by always extending the shorter cost nodes first
		_, node = heap.heappop(pq)
		visited.add(node)
 
		for adjNode, weight in G[node].items():
			if adjNode in visited:	continue
				
			newCost = nodeCosts[node] + weight['weight']
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heap.heappush(pq, (newCost, adjNode))
        
	return parentsMap, nodeCosts

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
        total_time += timeit.timeit(lambda: dijkstra(graph, '0'), number=1)

        dijkstra_times.append(total_time)

        print("Done {}".format(n))

    write_file(n_vertices, dijkstra_times, "heap_dijkstra_timing_results_dense")
