import networkx as nx
import numpy as np
import random

def connected_check(graph):
    check = nx.is_strongly_connected(graph)

    if check:
        return True
    else:
        return False

def add_weights(graph):
    for u, v in graph.edges:
        graph[u][v]['weight'] = random.randint(1, 11)

    return graph

def generate_graph():
    for data in ["Sparse", "Dense", "Average"]:
        prob = None
        for i in range(1, 501):
            if data == "Dense":
                prob = 1
            elif data == "Average":
                prob = 0.5
            else:
                prob = 0.1

            print("Start {}".format(i * 10))
            graph = nx.fast_gnp_random_graph(i * 10, prob, seed=np.random, directed=True)
            
            if data != "Dense":
                res = connected_check(graph)

                if not res:
                    while res == False:
                        print("here")
                        graph = nx.fast_gnp_random_graph(i * 10, prob, seed=np.random, directed=True)
                        res = connected_check(graph)

            # add weights
            graph = add_weights(graph)

            # write to file
            fh = open(f"Graph Input Data {data}/graph_{i}.txt", 'wb')
            nx.write_weighted_edgelist(graph, fh)
            fh.close()
            print("Done {}".format(i * 10))

if __name__ == "__main__":
    generate_graph()