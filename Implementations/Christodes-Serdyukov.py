from pygraph.classes.graph import graph
from pygraph.algorithms.traversal import *
from pygraph.mixins.labeling import *
from collections import defaultdict
import heapq

Graph0 = graph()

nodes = [1,2,3,4,5]
edges = [[(1,2), 4], [(1,4), 5], [(1,3),2], [(1,5),4], 
    [(2,3), 6], [(2,5),3], 
    [(3,5),2], [(3,4),7], 
    [(4,5), 7], [(4,2), 3]]

Graph0.add_nodes(nodes)
#print(G.edges())
# for edge in edges:
#      Graph0.add_edge(edge[0], edge[1])

#print(Graph.edges())

Graph1 = graph()
nodes1 = [1,2,3,4,5]
edges1 = [[(1,2), 1], [(1,4), 2], [(1,3),1], [(1,5),1], 
    [(2,3), 2], [(2,5),1], 
    [(3,5),1], [(3,4),1], 
    [(4,5), 1], [(4,2), 1]]

Graph1.add_nodes(nodes1)
for edge in edges1:
    Graph1.add_edge(edge[0], edge[1])

#print(Graph1)

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
    #print(mst)
    return mst      
    
min_tree = PrimMST(Graph1, 1)

def odd_vertices(T: graph):
    odd_set = set()
    for v in T:
        if T.node_order(v) % 2 == 1:
            odd_set.add(v)        
    return odd_set
    
odd = odd_vertices(min_tree)

#traversal()

def induced_subgraph(G: graph, V: set):
    subgraph = graph()
    subgraph.add_nodes(V)
    for v in V:
        for u in G[v]:
            if u in V and (v,u) not in subgraph.edges():
                subgraph.add_edge((v,u), G.edge_weight((v,u)))
    return subgraph

def approx_TSP(G:graph, v):
    min_tree = PrimMST(G, v)
    tour = []
    H = traversal(min_tree, v, 'pre')
    for i in H:
        print(i)
        #tour.append(i)
    #tour.append(v)
    print(tour)
        
#tree = PrimMST(Graph1, 1)
#odd_vertices(tree)
#approx_TSP(Graph1, 1)
#print(induced_subgraph(Graph1, odd))