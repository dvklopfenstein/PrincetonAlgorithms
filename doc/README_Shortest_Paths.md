# [Shortest Paths](http://algs4.cs.princeton.edu/44sp)

## Code     
[summary](README_analysis_summary.md#single-source-shortest-paths-implementations)
  * **Shortest Paths APIs**:
    [DirectedEdge.py](../py/AlgsSedgewickWayne/DirectedEdge.py) and
    [EdgeWeightedDigraph.py](../py/AlgsSedgewickWayne/EdgeWeightedDigraph.py)    
  * **Shortest Path Properties**:
    [AcyclicSP.py](../py/AlgsSedgewickWayne/AcyclicSP.py)
  * **Dijkstras Algorithm**:
    DijkstraSP.py
  * **Edge-Weighted DAGs**:
    [AcyclicSP.py](../py/AlgsSedgewickWayne/AcyclicSP.py),
    AcyclicLP.py, and
    CPM.py (Critical path method)
  * **Negative Weights**: BellmanFordSP

## Table of Contents for Practice Examples
  1. [Suppose that you run Dijkstra's algorithm to compute the shortest paths
from E to every other vertex. Give the sequence of 8 integers in the
distTo array immediately after vertex G is relaxed.](#ex1)    
  2. [Suppose that you run the acyclic shortest paths algorithm to compute the shortest
paths from A to every other vertex using the following topological order A B F G H C D E 
Give the sequence of 8 integers in the distTo array immediately after
vertex H is relaxed.](#ex2)    
  3. [Suppose that you run the Bellman-Ford algorithm to compute the shortest paths
from D to every other vertex. Give the sequence of 8 integers in the distTo
array immediately after the end of three passes of the algorithm (pass 0, 1, and 2).
Each pass consists of relaxing the 13 edges in the order given above.](#ex3)    

## Examples 
### [ex1](#table-of-contents-for-examples)    
**Suppose that you run Dijkstra's algorithm to compute the shortest paths
from E to every other vertex. Give the sequence of 8 integers in the
distTo array immediately after vertex G is relaxed.**    
```
Consider the following edge-weighted digraph with 8 vertices and 13 edges.

    v->w  weight
    ------------
    B->A    16
    B->F     9
    C->B     1
    D->C    21
    E->A    33
    E->B     7
    E->F    23
    F->C    63
    F->G    12
    G->C    48
    G->D    22
    G->H    31
    H->D     5


Here is a graphical representation of the same edge-weighted digraph:

    (A)<-----16-----(B)<-----1------(C)<-----21-----(D) 
     ^              ^|              ^^              ^^  
     |             / |             / |             / |  
     |            /  |            /  |            /  |  
     |           /   |           /   |           /   |  
     |          /    |          /    |          /    |  
     |         /     |         /     |         /     |  
     |        /      |        /      |        /      |  
     33      7       9       63      48      22      5  
     |      /        |      /        |      /        |  
     |     /         |     /         |     /         |  
     |    /          |    /          |    /          |  
     |   /           |   /           |   /           |  
     |  /            |  /            |  /            |  
     | /             | /             | /             |  
     |/              v/              |/              |  
    (E)------23---->(F)------12---->(G)------31---->(H) 



Suppose that you run Dijkstra's algorithm to compute the shortest paths
from E to every other vertex. Give the sequence of 8 integers in the
distTo[] array immediately after vertex G is relaxed.

Here is the distTo[] array before E is relaxed:

           v     A   B   C   D   E   F   G   H 
    ------------------------------------------
    distTo[v]    -   -   -   -   0   -   -   - 
```

### [ex2](#table-of-contents-for-examples)    
**Suppose that you run the acyclic shortest paths algorithm to compute the shortest
paths from A to every other vertex using the following topological order A B F G H C D E 
Give the sequence of 8 integers in the distTo array immediately after
vertex H is relaxed.**
```Consider the following edge-weighted DAG with 8 vertices and 13 edges.

    v->w  weight
    ------------
    A->B    17
    A->E    30
    A->F    42
    B->C    38
    B->F    16
    B->G    34
    C->D    19
    F->E     1
    F->G    16
    G->C     0
    G->H     3
    H->C     0
    H->D    18


Here is a graphical representation of the same edge-weighted digraph:

    (A)------17---->(B)------38---->(C)------19---->(D) 
     |\              |\              ^^              ^  
     | \             | \             | \             |  
     |  \            |  \            |  \            |  
     |   \           |   \           |   \           |  
     |    \          |    \          |    \          |  
     |     \         |     \         |     \         |  
     |      \        |      \        |      \        |  
     30      42      16      34      0       0       18 
     |        \      |        \      |        \      |  
     |         \     |         \     |         \     |  
     |          \    |          \    |          \    |  
     |           \   |           \   |           \   |  
     |            \  |            \  |            \  |  
     |             \ |             \ |             \ |  
     v              vv              v|              \|  
    (E)<-----1------(F)------16---->(G)------3----->(H) 



Suppose that you run the acyclic shortest paths algorithm to compute the shortest
paths from A to every other vertex using the following topological order:

    A B F G H C D E 

Give the sequence of 8 integers in the distTo[] array immediately after
vertex H is relaxed.

Here is the distTo[] array before A is relaxed:

           v     A   B   C   D   E   F   G   H 
    ------------------------------------------
    distTo[v]    0   -   -   -   -   -   -   - 
```

### [ex3](#table-of-contents-for-examples)    
**Suppose that you run the Bellman-Ford algorithm to compute the shortest paths
from D to every other vertex. Give the sequence of 8 integers in the distTo
array immediately after the end of three passes of the algorithm (pass 0, 1, and 2).
Each pass consists of relaxing the 13 edges in the order given above.**
```
Consider the following edge-weighted digraph with 8 vertices and 13 edges.

    v->w  weight
    ------------
    A->B     3
    A->E    30
    B->C     2
    C->G    16
    D->H    13
    D->C     7
    D->G    25
    F->C     2
    F->B    18
    F->A    38
    F->E    71
    G->F     3
    H->G    17


Here is a graphical representation of the same edge-weighted digraph:

    (A)------3----->(B)------2----->(C)<-----7------(D) 
     |^              ^              ^|              /|  
     | \             |             / |             / |  
     |  \            |            /  |            /  |  
     |   \           |           /   |           /   |  
     |    \          |          /    |          /    |  
     |     \         |         /     |         /     |  
     |      \        |        /      |        /      |  
     30      38      18      2       16      25      13 
     |        \      |      /        |      /        |  
     |         \     |     /         |     /         |  
     |          \    |    /          |    /          |  
     |           \   |   /           |   /           |  
     |            \  |  /            |  /            |  
     |             \ | /             | /             |  
     v              \|/              vv              v  
    (E)<-----71-----(F)<-----3------(G)<-----17-----(H) 



Suppose that you run the Bellman-Ford algorithm to compute the shortest paths
from D to every other vertex. Give the sequence of 8 integers in the distTo[]
array immediately after the end of three passes of the algorithm (pass 0, 1, and 2).
Each pass consists of relaxing the 13 edges in the order given above.

Here is the distTo[] array before the beginning of pass 0:

           v     A   B   C   D   E   F   G   H 
    ------------------------------------------
    distTo[v]    -   -   -   0   -   -   -   - 
```

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.    
