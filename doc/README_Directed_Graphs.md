# [Directed Graphs](http://algs4.cs.princeton.edu/42digraph)

## Code
  * [Digraph.py](../py/AlgsSedgewickWayne/Digraph.py)
  * [DepthFirstDirectedPaths.py](../py/AlgsSedgewickWayne/DepthFirstDirectedPaths.py)
  * Topological.py TopologicalX.py
  * **Strong Components**:    
    * 1972: TarjanSCC.py    
    * 1980s: **KosarajuSharirSCC.py**    
    * 1990s: GabowSCC.py
    * 1990s: Cheriyan-Mehlhorn: needed one-pass algorithm for LEDA.


## Table of Contents for Practice Examples
  1. [Give the sequence in which the vertices are dequeued from the (BFS) FIFO queue.](#ex1)    
  2. [Give the topological order of the vertices that results from the DFS-based topological sort algorithm.](#ex2)
  3. [Compute the strongly-connected components of the digraph using the Kosaraju-Sharir algorithm.](#ex3)    

## Examples 
### [ex1](#table-of-contents-for-examples)
**Give the sequence in which the vertices are dequeued from the (BFS) FIFO queue.**    
```
Consider the adjacency-lists representation of a digraph with 8 vertices and 13 edges:

    A:  B 
    B:  C F 
    C:  F D G 
    D:  H 
    E:  A 
    F:  E G A 
    G:  D 
    H:  G 


Here is a graphical representation of the same digraph:

    (A)------------>(B)------------>(C)------------>(D)
     ^^              |              /|              ^| 
     | \             |             / |             / | 
     |  \            |            /  |            /  | 
     |   \           |           /   |           /   | 
     |    \          |          /    |          /    | 
     |     \         |         /     |         /     | 
     |      \        |        /      |        /      | 
     |       \       |       /       |       /       | 
     |        \      |      /        |      /        | 
     |         \     |     /         |     /         | 
     |          \    |    /          |    /          | 
     |           \   |   /           |   /           | 
     |            \  |  /            |  /            | 
     |             \ | /             | /             | 
     |              \vv              v/              v 
    (E)<------------(F)------------>(G)<------------(H)



Run breadth-first search (using the adjacency-lists representation), starting from vertex A.
Give the sequence in which the vertices are dequeued from the FIFO queue.
Your answer should be a sequence of uppercase letters, starting with A.
```

### [ex2](#table-of-contents-for-examples)
**Give the topological order of the vertices that results from the DFS-based topological sort algorithm**    
```
Consider the adjacency-lists representation of a DAG with 8 vertices and 13 edges:

    A:  E F B 
    B:  G 
    C:  G B H D 
    D:  H 
    E:  
    F:  G E B 
    G:  H 
    H:  


Here is a graphical representation of the same DAG:

    (A)------------>(B)<------------(C)------------>(D)
     |\              ^\              |\              | 
     | \             | \             | \             | 
     |  \            |  \            |  \            | 
     |   \           |   \           |   \           | 
     |    \          |    \          |    \          | 
     |     \         |     \         |     \         | 
     |      \        |      \        |      \        | 
     |       \       |       \       |       \       | 
     |        \      |        \      |        \      | 
     |         \     |         \     |         \     | 
     |          \    |          \    |          \    | 
     |           \   |           \   |           \   | 
     |            \  |            \  |            \  | 
     |             \ |             \ |             \ | 
     v              v|              vv              vv 
    (E)<------------(F)------------>(G)------------>(H)



Give the topological order of the vertices that results from the DFS-based
topological sort algorithm. As usual, perform the first DFS from vertex A.
Your answer should be a sequence of 8 uppercase letters.
```

### [ex3](#table-of-contents-for-examples)
**Compute the strongly-connected components of the digraph using the Kosaraju-Sharir algorithm.**      
```
Consider the adjacency-lists representation of a digraph G with 10 vertices and 17 edges:

    A:  F 
    B:  C G A 
    C:  D G 
    D:  I 
    E:  D 
    F:  G 
    G:  H A 
    H:  C D I 
    I:  J 
    J:  E D 


Here is a graphical representation of the same digraph G:

    (A)<------------(B)------------>(C)------------>(D)<------------(E)
     |^              |              /^              ^|^              ^ 
     | \             |             / |             / | \             | 
     |  \            |            /  |            /  |  \            | 
     |   \           |           /   |           /   |   \           | 
     |    \          |          /    |          /    |    \          | 
     |     \         |         /     |         /     |     \         | 
     |      \        |        /      |        /      |      \        | 
     |       \       |       /       |       /       |       \       | 
     |        \      |      /        |      /        |        \      | 
     |         \     |     /         |     /         |         \     | 
     |          \    |    /          |    /          |          \    | 
     |           \   |   /           |   /           |           \   | 
     |            \  |  /            |  /            |            \  | 
     |             \ | /             | /             |             \ | 
     v              \vv              |/              v              \| 
    (F)------------>(G)------------>(H)------------>(I)------------>(J)



Compute the strongly-connected components of the digraph using the Kosaraju-Sharir algorithm.
Assume that the first depth-first search of Kosaraju-Sharir computes the reverse postorder of G^R:

    D E J I A G C B H F 

Give the sequence of the 10 integers in the id[] array for the vertices A through J.

       v    A  B  C  D  E  F  G  H  I  J  
    ------------------------------------
    id[v]                                 
```

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.    
