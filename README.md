---
CS412 Final Project\
  Travelling Salesman Problem\
  Implementations and Analysis of Various Solutions
---

![image](images/title.png)

Introduction
============

The travelling salesman problem has a long history of being a problem of
interest in the field of algorithms. It has garnered much attention and
there has been a lot of work that has been done on it. In this project
we will set out to establish the details of this problem and why it is
so tough. We will then investigate 4 algorithms that have become well
known in being useful for solving this problem. One of them produces an
exact solution and the rest use approximation techniques. We will be
using theory and implementation to test the runtimes of this problem and
will then present our research in an appropriate format.

Proof: TSP $\in$ NP-hard
------------------------

Design Techniques
=================

Exact Solution
--------------

The exact solution of the travelling salesman problem requires that that
each Hamiltonian cycle is travelled and the minimum path of those cycles
is found. However, this is an extremely large problem as there will be
$n!$ cycles for a complete graph of size $n$. The dynamic programming
approach called the Held-Karp algorithm reduces this time complexity to
$O(n^22^n)$. It does so by dividing the problem into sub problems. A
very simple method is to visulize this idea using a tree.

#### 

Let us begin this explanation, without loss of generality, with a
complete graph, $K_4,$ that does not contain loops.

Starting from vertex a, or any vertex to maintain generality, we can
build a decision tree that traverses each path, this represents the the
power set of the graph

The idea behind the exhaustive, brute-force approach is to traverse each
path in the tree and then decide, this creates a very large problem to
solve. The idea behind the dynamic approach is to start from the level 4
of the tree, which means we are now at the last vertex in the path and
the next vertex from that completes the cycle and takes us back to the
source node. This forms the smallest sub problem in the dynamic program.
The next step would be go a level higher in the tree, which means we
will now check the path length if we are reaching the source node from
vertex $v$ and, we are reaching reaching vertex, $v$, from vertex, $u$
s.t. $u,v \in V$ where $V$ is the set of all vertices. We will keep
doing this, and at each level we will decide the minimum path length of
between n paths that are emerging from one vertex, this is done until
the source node of the tree is reached, resulting in the minimum path.
The dynamic algorithm can be generalised as a cost function, $g$, as
follows: $$g(i, S) = min_{k\in S} \bigg\{c_{ik} + g(k, S-\{k\})\bigg\}$$
s.t. $i$ is the source vertex, $S$ is the set of all vertices, $c_{ik}$
is the cost of some going from vertex $i$ to $k$.

### Held-Karp Algorithm

 Approximate Solutions
---------------------

### Nearest Neighbour Algorithm

### Pairwise Exchange Method

### Christofides--Serdyukov Algorithm

Theoretical Runtime Analysis and Comparison
===========================================

Empirical Runtime Analysis and Comparison
=========================================

Conclusion
==========

References
==========

1.  <https://www.researchgate.net/publication/289195926_On_the_Nearest_Neighbor_Algorithms_for_the_Traveling_Salesman_Problem>

2.  <https://en.wikipedia.org/wiki/Travelling_salesman_problem#:~:text=The%20travelling%20salesman%20problem%20>

3.  Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and
    Clifford Stein. 2009. Introduction to Algorithms, Third Edition
    (3rd. ed.)

4.  David L. Applegate, Robert E. Bixby, Vasek Chvatal, and William J.
    Cook. 2007. The Traveling Salesman Problem: A Computational Study.
    Princeton University Press, USA.
