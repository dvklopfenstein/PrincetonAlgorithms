# [Maximum Flow and Minimum Cut](http://algs4.cs.princeton.edu/64maxflow)

## Code
  * **Introduction to Mincut and Maxflow**    
  * **Ford-Fulkerson Algorithm**
  * **Maxflow-mincut Theorem**
  * **Running Time Analysis**
  * **Python Implementation**:
    [FlowEdge.py](../py/AlgsSedgewickWayne/FlowEdge.py), 
    FlowNetwork.py, and
    FordFulkerson.py
  * **Maxflow Applications**: code.py

## Table of Contents for Examples
  1. [Give the sequence of vertices in the final augmenting path discovered by the Ford-Fulkerson algorithm](#ex1)
  2. [Given a maxflow, what is the corresponding mincut?](#ex2)
  3. [Which of the following statements about maxflow and mincut are guaranteed to be true in any flow network?](#ex3)
     [3.1](#ex3p1) If all edge capacities are integral, then any maxflow is an 
           integer-valued flow, i.e., f(e) is an integer for every edge e.
 
     [3.2](#ex3p2) If all edge capacities are integral, then there exists 
           an integer-valued maxflow f, i.e., f(e) is an integer for every edge e.
 
     [3.3](#ex3p3) Let G be a network that contains two antiparallel 
          edges e = v->w and e' = w->v. 
          Then, in any maxflow f, either f(e) = 0 or f(e') = 0 (or both).
 
     [3.4](#ex3p4) The Ford-Fulkerson algorithm can be used to find a maximum matching 
          in a bipartite graph in time proportional to V (E + V).
 
     [3.5](#ex3p5) Let (A, B) be a mincut in G. Suppose that one 
           edge e from A to B of capacity x > 0 is deleted. Then, the 
           capacity of the mincut in the modified network G' decrease by exactly x units.

## Examples 
### [ex1](#table-of-contents-for-examples)
Final Augmenting Path    
```
Suppose that you are computing a max flow from the source vertex A to the
sink vertex J in the flow network given below:

    edge   flow  /  capacity
    ------------------------
    A->B      9  /   9
    A->F      6  /  15
    A->G     26  /  26
    B->C     11  /  11
    C->D      8  /   8
    C->G      9  /   9
    D->E      5  /   8
    D->I      0  /  13
    D->J     34  /  42
    E->J      5  /   5
    F->G      6  /  15
    G->B      2  /  10
    G->H     39  /  39
    H->C      6  /   9
    H->D     31  /  31
    H->I      2  /   9
    I->J      2  /  10


Here is a graphical representation of the same flow network:                                                                                          


      (A)-------9/9------>(B)------11/11----->(C)-------8/8------>(D)-------5/8------>(E) 
       |\                  ^                  /^                  ^|\                  |  
       | \                 |                 / |                 / | \                 |  
       |  \                |                /  |                /  |  \                |  
       |   \               |               /   |               /   |   \               |  
       |    \              |              /    |              /    |    \              |  
       |     \             |             /     |             /     |     \             |  
       |      \            |            /      |            /      |      \            |  
       |       \           |           /       |           /       |       \           |  
       |        \          |          /        |          /        |        \          |  
      6/15     26/26      2/10      9/9       6/9      31/31      0/13     34/42      5/5 
       |          \        |        /          |        /          |          \        |  
       |           \       |       /           |       /           |           \       |  
       |            \      |      /            |      /            |            \      |  
       |             \     |     /             |     /             |             \     |  
       |              \    |    /              |    /              |              \    |  
       |               \   |   /               |   /               |               \   |  
       |                \  |  /                |  /                |                \  |  
       |                 \ | /                 | /                 |                 \ |  
       v                  v|v                  |/                  v                  vv  
      (F)-------6/15----->(G)------39/39----->(H)-------2/9------>(I)-------2/10----->(J) 



Starting from the given flow (of value 41), give the sequence of vertices in the
next (and final) augmenting path discovered by the Ford-Fulkerson algorithm.
```
```
The correct answer is: A F G C H I J


augmenting path:     A->F->G->C->H->I->J
bottleneck capacity: 6
value of flow:       47

Here is the final flow network:

    edge   flow  /  capacity
    ------------------------
    A->B      9  /   9
    A->F     12  /  15
    A->G     26  /  26
    B->C     11  /  11
    C->D      8  /   8
    C->G      3  /   9
    D->E      5  /   8
    D->I      0  /  13
    D->J     34  /  42
    E->J      5  /   5
    F->G     12  /  15
    G->B      2  /  10
    G->H     39  /  39
    H->C      0  /   9
    H->D     31  /  31
    H->I      8  /   9
    I->J      8  /  10


Here is a graphical representation of the final flow network:                                                                                          


      (A)-------9/9------>(B)------11/11----->(C)-------8/8------>(D)-------5/8------>(E) 
       |\                  ^                  /^                  ^|\                  |  
       | \                 |                 / |                 / | \                 |  
       |  \                |                /  |                /  |  \                |  
       |   \               |               /   |               /   |   \               |  
       |    \              |              /    |              /    |    \              |  
       |     \             |             /     |             /     |     \             |  
       |      \            |            /      |            /      |      \            |  
       |       \           |           /       |           /       |       \           |  
       |        \          |          /        |          /        |        \          |  
     12/15     26/26      2/10      3/9       0/9      31/31      0/13     34/42      5/5 
       |          \        |        /          |        /          |          \        |  
       |           \       |       /           |       /           |           \       |  
       |            \      |      /            |      /            |            \      |  
       |             \     |     /             |     /             |             \     |  
       |              \    |    /              |    /              |              \    |  
       |               \   |   /               |   /               |               \   |  
       |                \  |  /                |  /                |                \  |  
       |                 \ | /                 | /                 |                 \ |  
       v                  v|v                  |/                  v                  vv  
      (F)------12/15----->(G)------39/39----->(H)-------8/9------>(I)-------8/10----->(J) 
```

### [ex2](#table-of-contents-for-examples)
Coressponging mincut
```
Consider the flow network with 10 vertices and 17 edges:

    edge   flow  /  capacity
    ------------------------
    A->B     15  /  15
    A->F      6  /   6
    A->G      8  /  16
    H->B      3  /  14
    B->G      3  /   7
    B->C     15  /  15
    C->H      0  /  11
    C->D     15  /  18
    D->H      0  /  13
    D->I      0  /  10
    D->E      8  /   8
    D->J      7  /  15
    E->J      8  /  14
    F->G      6  /  13
    G->H     17  /  17
    H->I     14  /  18
    I->J     14  /  14


Here is a graphical representation of the same flow network:                                                                                          


      (A)------15/15----->(B)------15/15----->(C)------15/18----->(D)-------8/8------>(E) 
       |\                  |^                  |                  /|\                  |  
       | \                 | \                 |                 / | \                 |  
       |  \                |  \                |                /  |  \                |  
       |   \               |   \               |               /   |   \               |  
       |    \              |    \              |              /    |    \              |  
       |     \             |     \             |             /     |     \             |  
       |      \            |      \            |            /      |      \            |  
       |       \           |       \           |           /       |       \           |  
       |        \          |        \          |          /        |        \          |  
      6/6       8/16      3/7       3/14      0/11      0/13      0/10      7/15      8/14
       |          \        |          \        |        /          |          \        |  
       |           \       |           \       |       /           |           \       |  
       |            \      |            \      |      /            |            \      |  
       |             \     |             \     |     /             |             \     |  
       |              \    |              \    |    /              |              \    |  
       |               \   |               \   |   /               |               \   |  
       |                \  |                \  |  /                |                \  |  
       |                 \ |                 \ | /                 |                 \ |  
       v                  vv                  \vv                  v                  vv  
      (F)-------6/13----->(G)------17/17----->(H)------14/18----->(I)------14/14----->(J) 




The flow given above is a maxflow from A to J. What is the corresponding mincut?
List the vertices on the s side of mincut in alphabetical order.
```
```
The correct answer is: A B F G H I


min cut:         A B F G H I 
value of flow:   29
capacity of cut: 29
```

### [ex3](#table-of-contents-for-examples)
Maxflow/Mincut factoids    

3.1 False: If all edge capacities are integral, then any maxflow is an 
     integer-valued flow, i.e., f(e) is an integer for every edge e.    
*The integrality theorem implies that such a maxflow exists, but not every maxflow has this property.*    

3.2 True: If all edge capacities are integral, then there exists 
     an integer-valued maxflow f, i.e., f(e) is an integer for every edge e.    
*This is the integrality theorem.*    

3.3 False: Let G be a network that contains two antiparallel 
    edges e = v->w and e' = w->v. 
    Then, in any maxflow f, either f(e) = 0 or f(e') = 0 (or both).    
*There always exists a maxflow with that property, but not
every maxflow has it. Consider a network with these edges
and capacities: s->v (2), v->w (2), w->v (1), w->t (1).
Then, the flow f that sets f(e) = capacity for every edge is
a maxflow but the antiparallel edges v->w and w->v each have
positive flow.*    

3.4 True: The Ford-Fulkerson algorithm can be used to find a maximum matching 
    in a bipartite graph in time proportional to V (E + V).
*The matching problem can be formulated as a maxflow problem
in a network with V + 2 vertices and E + 2V edges and for
which the value of the maxflow is at most V. Thus, the
Ford-Fulkerson algorithm will terminate after at most V
augmentations. We can find an augmenting path in time
proportional to E + V via BFS or DFS.*    

3.5 True: Let (A, B) be a mincut in G. Suppose that one 
      edge e from A to B of capacity x > 0 is deleted. Then, the 
      capacity of the mincut in the modified network G' decrease by exactly x units.
*The capacity of the cut (A, B) decreases by exactly x units
(and the capacity of every other cut decreases by at most
x).*    

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
