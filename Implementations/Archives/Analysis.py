import time
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
    
    n_values = np.array([i for i in range(n)])
    n_ = 0

    while(n_ < n):
        cs_sum_time = 0
        G = complete_graph(n)
        G_ = copy.deepcopy(G)
        r = 0
        while (r < repeat):
            #Recording time for christofides
            start = time.time()
            chirstoalgo(G, 1)
            cs_sum_time = time.time() - start
            G = copy.deepcopy(G_)
            #Recording time for held-karp
            start = time.time()
            chirstoalgo(G, 1)
            hk_sum_time = time.time() - start
            G = copy.deepcopy(G_)
            #Recording time for Nearest Neighbor
            start = time.time()
            chirstoalgo(G, 1)
            nn_sum_time = time.time() - start
            G = copy.deepcopy(G_)
            #Recording time for Pairwise Exchange
            start = time.time()
            chirstoalgo(G, 1)
            pe_sum_time = time.time() - start
            G = copy.deepcopy(G_)
            r += 1
        cs_runtimes.append(cs_sum_time/repeat)
        hk_runtimes.append(cs_sum_time/repeat)
        nn_runtimes.append(cs_sum_time/repeat)
        pe_runtimes.append(cs_sum_time/repeat)        
        n_ += 1
    

    
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
    