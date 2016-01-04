# [Undirected Graphs](http://algs4.cs.princeton.edu/41graph/)

## Code
  * [Graph.py](../py/AlgsSedgewickWayne/Graph.py)    
  * [DepthFirstPaths.py](../py/AlgsSedgewickWayne/DepthFirstPaths.py)    
  * [BreadthFirstPaths.py](../py/AlgsSedgewickWayne/BreadthFirstPaths.py)    
  * [CC.py](../py/AlgsSedgewickWayne/CC.py) for Connected Components    

## Table of Contents for Examples
  0.0. [Run Graph Example](#ex0p0) on [tinyG.txt](../thirdparty/tinyG.txt)
  0.1. [Run BreadthFirstPaths](#ex0p1) on [tinyG.txt](../thirdparty/tinyG.txt)
  1. [Give the sequence in which depth-first search discovers (marks) the vertices.](#ex1)    
  2. [Give the sequence in which the vertices are dequeued (BFS) from the FIFO queue.](#ex2)    
  3. [Give the sequence of the 10 integers in the id[] array for the vertices.](#ex3)

## Examples 
### [ex0p0](#table-of-contents-for-examples)
Run Graph Example on [tinyG.txt](../thirdparty/tinyG.txt)
```
test_Graph.py ../thirdparty/tinyG.txt
```
![Graph_tinyG.png](images/Graph_tinyG.png)    
```
13 vertices, 13 edges
0: 6 2 1 5
1: 0
2: 0
3: 5 4
4: 5 6 3
5: 3 4 0
6: 0 4
7: 8
8: 7
9: 11 10 12
10: 9
11: 9 12
12: 11 9
```

### [ex0p1](#table-of-contents-for-examples)
Run BreadthFirstPaths on [tinyG.txt](../thirdparty/tinyG.txt)
```
test_BreadthFirstPaths.py ../thirdparty/tinyCG.txt 0
```
```
6 vertices, 8 edges
0: 1 2 5
1: 0 2
2: 0 1 3 4
3: 2 4 5
4: 2 3
5: 0 3
0 to 0 (0):  0
0 to 1 (1):  0-1
0 to 2 (1):  0-2
0 to 3 (2):  0-2-3
0 to 4 (2):  0-2-4
0 to 5 (1):  0-5
```

### [ex1](#table-of-contents-for-examples)
**Give the sequence in which depth-first search discovers (marks) the vertices.**    
```
Consider the adjacency-lists representation of a graph with 8 vertices and 9 edges:

    A:  F B E 
    B:  F A 
    C:  G F 
    D:  H G 
    E:  A 
    F:  G A B C 
    G:  F C D 
    H:  D 


Here is a graphical representation of the same graph:

    (A)-------------(B)             (C)             (D)
     |\              |              /|              /| 
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
     |              \|/              |/              | 
    (E)             (F)-------------(G)             (H)



Run depth-first search (using the adjacency-lists representation) from vertex A. Give the sequence
in which depth-first search discovers (marks) the vertices. This is known as the preorder.
Your answer should be a sequence of 8 uppercase letters, with each letter separated
by whitespace.
```
```
The correct answer is: A F G C D H B E

Here is a trace of the depth-first search:

dfs(A)
  dfs(F)
    dfs(G)
      check F
      dfs(C)
        check G
        check F
      C done
      dfs(D)
        dfs(H)
          check D
        H done
        check G
      D done
    G done
    check A
    dfs(B)
      check F
      check A
    B done
    check C
  F done
  check B
  dfs(E)
    check A
  E done
A done
check B
check C
check D
check E
check F
check G
check H


The preorder is the order in which depth-first search discovers (marks) the vertices.
```

### [ex2](#table-of-contents-for-examples)
**Give the sequence in which the vertices are dequeued (BFS) from the FIFO queue.**    
```
Consider the adjacency-lists representation of a graph with 8 vertices and 10 edges:

    A:  E B 
    B:  E A F 
    C:  D F 
    D:  C G H 
    E:  A B 
    F:  C G B 
    G:  D H F 
    H:  G D 


Here is a graphical representation of the same graph:

    (A)-------------(B)             (C)-------------(D)
     |              /|              /               /| 
     |             / |             /               / | 
     |            /  |            /               /  | 
     |           /   |           /               /   | 
     |          /    |          /               /    | 
     |         /     |         /               /     | 
     |        /      |        /               /      | 
     |       /       |       /               /       | 
     |      /        |      /               /        | 
     |     /         |     /               /         | 
     |    /          |    /               /          | 
     |   /           |   /               /           | 
     |  /            |  /               /            | 
     | /             | /               /             | 
     |/              |/               /              | 
    (E)             (F)-------------(G)-------------(H)



Run breadth-first search (using the adjacency-lists representation) from vertex A.
Give the sequence in which the vertices are dequeued from the FIFO queue.
Your answer should be a sequence of uppercase letters (starting with A).
```
```
The correct answer is: A E B F C G D H

Here is a trace of the breadth-first search:

enqueue A
dequeue A
   enqueue E
   enqueue B
dequeue E
   check A
   check B
dequeue B
   check E
   check A
   enqueue F
dequeue F
   enqueue C
   enqueue G
   check B
dequeue C
   enqueue D
   check F
dequeue G
   check D
   enqueue H
   check F
dequeue D
   check C
   check G
   check H
dequeue H
   check G
   check D


Here are the shortest paths and distances:

A to A (0):  A
A to B (1):  A-B
A to C (3):  A-B-F-C
A to D (4):  A-B-F-C-D
A to E (1):  A-E
A to F (2):  A-B-F
A to G (3):  A-B-F-G
A to H (4):  A-B-F-G-H


Here is the shortest-paths tree from A:

    (A)------------>(B)             (C)------------>(D)
     |               |              ^                  
     |               |             /                   
     |               |            /                    
     |               |           /                     
     |               |          /                      
     |               |         /                       
     |               |        /                        
     |               |       /                         
     |               |      /                          
     |               |     /                           
     |               |    /                            
     |               |   /                             
     |               |  /                              
     |               | /                               
     v               v/                                
    (E)             (F)------------>(G)------------>(H)
```



### [ex3](#table-of-contents-for-examples)
**Give the sequence of the 10 integers in the id[] array for the vertices.**    
```
(seed = 287555)
Consider the adjacency-lists representation of a graph with 10 vertices and 11 edges:

    A:  F B 
    B:  F A 
    C:  G 
    D:  I E J H 
    E:  D J 
    F:  A B 
    G:  C 
    H:  I D 
    I:  D H J 
    J:  D I E 


Here is a graphical representation of the same graph:

    (A)-------------(B)             (C)             (D)-------------(E)
     |              /               /               /|\              | 
     |             /               /               / | \             | 
     |            /               /               /  |  \            | 
     |           /               /               /   |   \           | 
     |          /               /               /    |    \          | 
     |         /               /               /     |     \         | 
     |        /               /               /      |      \        | 
     |       /               /               /       |       \       | 
     |      /               /               /        |        \      | 
     |     /               /               /         |         \     | 
     |    /               /               /          |          \    | 
     |   /               /               /           |           \   | 
     |  /               /               /            |            \  | 
     | /               /               /             |             \ | 
     |/               /               /              |              \| 
    (F)             (G)             (H)-------------(I)-------------(J)



Compute the connected components of the graph using the depth-first search
algorithm (and start numbering connected component ids with 0). Give the
sequence of the 10 integers in the id[] array for the vertices A through J.

       v    A  B  C  D  E  F  G  H  I  J  
    ------------------------------------
    id[v]                    
```
```
The correct answer is: 0 0 1 2 2 0 1 2 2 2


   v    A  B  C  D  E  F  G  H  I  J  
------------------------------------
id[v]   0  0  1  2  2  0  1  2  2  2  

Here is a trace of the depth-first search:


connected component 0
---------------------
dfs(A)
  dfs(F)
    check A
    dfs(B)
      check F
      check A
    B done
  F done
  check B
A done
---------------------

check B

connected component 1
---------------------
dfs(C)
  dfs(G)
    check C
  G done
C done
---------------------


connected component 2
---------------------
dfs(D)
  dfs(I)
    check D
    dfs(H)
      check I
      check D
    H done
    dfs(J)
      check D
      check I
      dfs(E)
        check D
        check J
      E done
    J done
  I done
  check E
  check J
  check H
D done
---------------------

check E
check F
check G
check H
check I
check J
```


Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
