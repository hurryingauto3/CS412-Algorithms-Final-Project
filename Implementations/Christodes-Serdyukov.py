from collections import defaultdict
import heapq
import copy 
import networkx as nx
import time 
import random 

# Graph1 = nx.Graph()
# nodes1 = [1,2,3,4,5]
# Graph1.add_nodes_from(nodes1)
# edges1 = [(1, 2, 1), (1, 4, 2), (1, 3 ,1), (1,5,1), 
#     (2,3, 2), (2,5,1), 
#     (3,5,1), (3,4,1), 
#     (4,5, 1), (4,2, 1)]

# Graph1.add_weighted_edges_from(edges1)

# T = nx.minimum_spanning_tree(Graph1)

def complete_graph(n):
    G = nx.complete_graph(n, create_using = nx.Graph)
    for u, v, d in G.edges(data=True):
        d['weight'] = random.randrange(1, 10)
    return G

def odd_vertices(T: nx.Graph):
    odd_set = set()
    for v in T:
        if nx.degree(T, v)%2 == 1:
            odd_set.add(v)
    return odd_set

def min_match(G):
    matching = nx.Graph()
    for v in G:
        #print(v)
        mydict = {}
        for u in G[v]:
            if u not in matching and v not in matching:
                mydict[u] = G[v][u]['weight']
            
        if v != None and mydict:
            x = min(mydict, key = mydict.get)
            matching.add_node(v)
            matching.add_node(x)
            matching.add_weighted_edges_from([(v, x, G[v][u]['weight'])])
    return matching 


def chirstoalgo(G, v):
    min_tree = nx.minimum_spanning_tree(G, v)
    x = odd_vertices(min_tree)
    sub = G.subgraph(x)
    matching = min_match(sub)

    multi = nx.MultiGraph()
    multi.add_weighted_edges_from(min_tree.edges(data='weight'))
    multi.add_weighted_edges_from(matching.edges(data='weight'))
    multi.add_nodes_from(min_tree.nodes())

    e_circ = [u for u,x in nx.eulerian_circuit(multi, source=v)] 
    tsp_path = list(dict.fromkeys(e_circ))
    tsp_path.append(v)
    return tsp_path
    
runtimes = []
for i in range(1, 100):
    G1 = complete_graph(i)
    start = time.time()
    chirstoalgo(G1, 0)
    runtimes.append(time.time() - start)

print(runtimes)