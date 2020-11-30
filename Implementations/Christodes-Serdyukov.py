from pygraph.classes.graph import graph
from pygraph.algorithms.traversal import *
from pygraph.mixins.labeling import *
from collections import defaultdict
import heapq

Graph = graph()

nodes = [1,2,3,4,5]
edges = [[(1,2), 4], [(1,4), 5], [(1,3),2], [(1,5),4], 
    [(2,3), 6], [(2,5),3], 
    [(3,5),2], [(3,4),7], 
    [(4,5), 7], [(4,2), 3]]

Graph.add_nodes(nodes)
#print(G.edges())
for edge in edges:
     Graph.add_edge(edge[0], edge[1])

#print(Graph.edges())

def PrimMST(G: graph, v):
    mst = graph()
    mst.add_node(v)
    Edges = []   
    for i in G[v]:
        Edges.append((G.edge_weight((v,i)), v, i))
    heapq.heapify(Edges)

    while Edges:
        cost, start, end = heapq.heappop(Edges)
        if end not in mst:
            mst.add_node(end)
            mst.add_edge((start,end), cost)
            for to_next in G[end]:
                if to_next not in mst:
                    heapq.heappush(Edges, (G.edge_weight((end, to_next)), end, to_next))  
    print(mst)
    return mst      
    
min_tree = PrimMST(Graph, 1)

def odd_vertices(T: graph):
    odd_set = set()
    for v in T:
        if T.node_order(v) % 2 == 1:
            odd_set.add(v)        
    print(odd_set)
    
#odd_vertices(min_tree)

#traversal()

def induced_subgraph(G: graph, V: set):
    pass

def approx_TSP(G:graph, v):
    min_tree = PrimMST(G, v)
    tour = []
    H = traversal(min_tree, v, 'pre')
    for i in H:
        tour.append(i)
    tour.append(v)
    print(tour)
        

approx_TSP(Graph, 1)