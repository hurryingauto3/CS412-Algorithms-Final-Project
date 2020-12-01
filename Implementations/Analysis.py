import timeit
import matplotlib.pyplot as plt
import numpy as np
from functools import partial
import networkx as nx
from collections import defaultdict
import heapq
import copy 

def complete_graph(n):
    G = nx.complete_graph(n, create_using = nx.Graph)
    for u, v, d in G.edges(data=True):
        d['weight'] = random.randrange(0, 10)
    return G

def Empirical_Analysis(n, repeat):
    
    hk_runtimes = []
    nn_runtimes = []
    cs_runtimes = []
    pe_runtimes = []
    
    n_values = np.array([i for i in range(1, n)])
    
    for i in n_values:
        
        G = complete_graph(i)
        start_time = time.time()
        chirstoalgo(G, 1)
        cs_runtimes.append((time.time()-start_time))
        
        
#         nn_runtimes.append(min(timeit.Timer(partial(n_neighbors, G)).repeat(3, repeat))/repeat)
#         cs_runtimes.append(min(timeit.Timer(chirstoalgo(G, 1)).repeat(3, repeat))/repeat)
#         if (i < 10):
#             hk_runtimes.append(min(timeit.Timer(partial(held_karp, G)).repeat(3, repeat))/repeat)

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(n_values, hk_runtimes)
    axs[0, 0].set_title("Held-Karp")
    axs[1, 0].plot(n_values, nn_runtimes)
    axs[1, 0].set_title("Nearest Neighbor")
    axs[0, 1].plot(n_values, cs_runtimes)
    axs[0, 1].set_title("Christofides")
    axs[1, 1].plot(n_values, pe_runtimes)
    axs[1, 1].set_title("Pairwise Exchange")
    fig.tight_layout()
    plt.show()
    
    return
    