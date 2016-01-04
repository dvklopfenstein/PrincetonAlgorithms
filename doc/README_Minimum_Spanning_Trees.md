# [Minimum Spanning Trees](http://algs4.cs.princeton.edu/43mst)

## Code
  * **Introduction to MSTs** 
    [Applications using MSTs](https://www.ics.uci.edu/~eppstein/gina/mst.html)
  * **Greedy Algorithm**
  * **Edge-Weighted Graph API**: 
    [Edge.py](../py/AlgsSedgewickWayne/Edge.py), 
    [EdgeWeightedGraph.py](../py/AlgsSedgewickWayne/EdgeWeightedGraph.py)
  * **Kruskal's Algorithm**: [KruskalMST.py](../py/AlgsSedgewickWayne/KruskalMST.py)
  * **Prim's Algorithm**:
    [LazyPrimMST.py](../py/AlgsSedgewickWayne/LazyPrimMST.py) and
    PrimMST.py
  * **MST Context**

## Table of Contents for Practice Examples
  1. [Give the sequence of edges in the MST in the order that Kruskal's algorithm discovers them.](#ex1)    
  2. [Give the sequence of edges in the MST in the order that Prim's algorithm adds them to the MST, when starting Prim's algorithm from vertex H.](#ex2)    
  3. [MST factoids](#ex3)    
Which of the following statements about minimum spanning
trees (MSTs) are guaranteed to be true in any edge-weighted
graph G? Assume that G is connected and has no parallel edge
or self-loops. Do not assume the edge weights are distinct
unless this is specifically stated. Check all that apply.    

    3.1. Assume that G contains at least 2 vertices. Let T
         be a MST of G. Then, T contains a lightest edge in G.    
          
    3.2  Let T and T' be two MSTs of G. Then, if T contains k edges
         of weight w, then so does T'. In other words, T and T' have
         the same sorted list of edge weights.    
          
    3.3  If edge e is not in any MST of G, then edge e is the unique
         heaviest edge on some cycle C in G.    
          
    3.4  Let w(e) > 0 denote the weight of edge e in G. Then, T is a
         maximum spanning tree of G if and only if T is a minimum
         spanning tree in the edge-weighted graph G' with weights
         w'(e) = -w(e).    
          
    3.5  Assume that the edge weights in G are distinct. If the
         heaviest edge e is in the MST T, then e is a cut edge (i.e.,
         deleting edge e from G disconnects the graph).    

## Examples 
### [ex1](#table-of-contents-for-examples)
**Give the sequence of edges in the MST in the order that Kruskal's algorithm discovers them.**    
```
Consider the following edge-weighted graph with 10 vertices and 17 edges:

    v-w  weight
    -----------
    B-A    11
    A-F    10
    A-G     8
    G-B     7
    B-H     6
    C-B     5
    D-C    16
    C-I     3
    H-C     2
    E-D    14
    D-I     9
    E-J    15
    E-I    13
    G-F     1
    H-G    12
    I-H     4
    J-I    17


Here is a graphical representation of the same graph:

    (A)------11-----(B)------5------(C)------16-----(D)------14-----(E)
     |\              |\              |\              |              /| 
     | \             | \             | \             |             / | 
     |  \            |  \            |  \            |            /  | 
     |   \           |   \           |   \           |           /   | 
     |    \          |    \          |    \          |          /    | 
     |     \         |     \         |     \         |         /     | 
     |      \        |      \        |      \        |        /      | 
     10      8       7       6       2       3       9       13      15
     |        \      |        \      |        \      |      /        | 
     |         \     |         \     |         \     |     /         | 
     |          \    |          \    |          \    |    /          | 
     |           \   |           \   |           \   |   /           | 
     |            \  |            \  |            \  |  /            | 
     |             \ |             \ |             \ | /             | 
     |              \|              \|              \|/              | 
    (F)------1------(G)------12-----(H)------4------(I)------17-----(J)



Give the sequence of edges in the MST in the order that Kruskal's algorithm discovers them.
To specify an edge, use its weight.
```

### [ex1](#table-of-contents-for-examples)
**Give the sequence of edges in the MST in the order that Prim's algorithm adds them to the MST, when starting Prim's algorithm from vertex H.**    
```
Consider the following edge-weighted graph with 10 vertices and 17 edges.

    v-w  weight
    -----------
    A-F      13
    G-A       3
    A-B       2
    B-C      15
    G-B       6
    C-H      16
    D-C      11
    C-I       7
    G-C       5
    J-D      10
    E-D       9
    I-D       4
    J-E       8
    F-G       1
    G-H      17
    I-H      12
    I-J      14


Here is a graphical representation of the same graph:

    (A)------2------(B)------15-----(C)------11-----(D)------9------(E)
     |\              |              /|\              |\              | 
     | \             |             / | \             | \             | 
     |  \            |            /  |  \            |  \            | 
     |   \           |           /   |   \           |   \           | 
     |    \          |          /    |    \          |    \          | 
     |     \         |         /     |     \         |     \         | 
     |      \        |        /      |      \        |      \        | 
     13      3       6       5       16      7       4       10      8 
     |        \      |      /        |        \      |        \      | 
     |         \     |     /         |         \     |         \     | 
     |          \    |    /          |          \    |          \    | 
     |           \   |   /           |           \   |           \   | 
     |            \  |  /            |            \  |            \  | 
     |             \ | /             |             \ |             \ | 
     |              \|/              |              \|              \| 
    (F)------1------(G)------17-----(H)------12-----(I)------14-----(J)



Give the sequence of edges in the MST in the order that Prim's algorithm adds them to the MST,
when starting Prim's algorithm from vertex H. To specify an edge, use its weight.
```

### [ex1](#table-of-contents-for-examples)
**MST factoids**    
3.1. Assume that G contains at least 2 vertices. Let T
be a MST of G. Then, T contains a lightest edge in G.    
*True: Assume (for the sake of contradiction) that T is a MST that does not contain any lightest edge of G. Let e be any lightest edge of G. Adding e to T creates a cycle C. Let f be any other edge in the cycle. Replacing f with e in T yields a lighter spanning tree (a contradiction).*    
          
3.2  Let T and T' be two MSTs of G. Then, if T contains k edges
of weight w, then so does T'. In other words, T and T' have
the same sorted list of edge weights.    
*True: This is a tricky one. Let T and T' be two MSTs of G that have different sorted arrays of edge weights; moreover, among all such pairs of MSTs, assume that T and T' have as many edges in common as possible. Let e be any edge that is in T but not in T'. Consider the cut (A, B) defined by deleting edge e from T. Adding edge e to T' creates a cycle C. Let f be some other edge in the cycle C that crosses the cut (A, B). Note that f is not in T because e is the only edge in T that crosses the cut. Observe that w(e) = w(f): if w(f) < w(e), then we could improve T by replacing edge e with edge f; if w(e) < w(f), then we could improve T' by replacing edge f with edge e. Now, the tree T'' = T' + e - f is a MST and has the same sorted array of edge weights as T'. But T'' has more edges in common with T than T' (a contradiction).*    
          
3.3  If edge e is not in any MST of G, then edge e is the unique
heaviest edge on some cycle C in G.    
*True: We prove the contrapositive. Suppose that e is not the unique heaviest edge on any cycle of G. We need to show that edge e is in some MST. Let T be a MST that does not contain edge e. Adding e to T creates a cycle C. Let f be some edge other than e that is a heaviest edge in C. Replacing f with e in T yields another MST, which contains e (as desired). We also note that the converse of the original statement is true.*    
          
3.4  Let w(e) > 0 denote the weight of edge e in G. Then, T is a
maximum spanning tree of G if and only if T is a minimum
spanning tree in the edge-weighted graph G' with weights
w'(e) = -w(e).    
*True:Maximizing the sum of weights in G is equivalent to minimizing the sum of the weights in G'. We also note that every MST algorithm that we have considered works correctly with arbitrary weights (positive, negative, or zero), so we can solve the maximum spanning tree problem efficiently.*    
          
3.5  Assume that the edge weights in G are distinct. If the
heaviest edge e is in the MST T, then e is a cut edge (i.e.,
deleting edge e from G disconnects the graph).    
*True: Consider the cut (A, B) defined by deleting the heaviest edge e from the MST T. Assume (for the sake of contradiction) that e is not a cut edge. Then, there is another edge f in G that crosses the cut. Thus, replacing edge f with edge e in T results in a lighter spanning tree (a contradiction).*    


Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.     
