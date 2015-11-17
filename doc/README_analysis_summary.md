# Implementations Summary

  * [**Sorting Summary**](#sorting-summary)
  * [**ST(Search Tree) implementations**](#stsearch-tree-implementations)
  * [Time complexity for Python structures](https://wiki.python.org/moin/TimeComplexity)

## Sorting Summary    

| Sort        | I | S | worst  | average | best    | Xspc | remarks
| ----------- |---|---| ------ | ------- | ------- | ---- | --------------------
| Selection   | Y |   | N^2/2  |   N^2/2 |   N^2/2 |      | N exchanges
| Insertion   | Y | Y | N^2/2  |   N^2/4 |       N |   1  | use for small N or partially ordered
| Shell       | Y |   |     ?  |       ? |       N |      | tight code, subquadratic
| Merge       |   | Y | N lg N |  N lg N |  N lg N |   N  | N lg N guarantee, stable
| Quick       | Y |   | N^2/2  | 2N ln N |  N lg N |c lg N| N lg N probabilistic guarantee, fastest in practice
| 3-way quick | Y |   | N^2/2  | 2N ln N |       N |      | better w/duplicate keys
| heapsort    | ? | N |2N lg N | 2N lg N |       N |   1  | 
| ???         | Y | Y | N lg N |  N lg N |  N lg N |      | holy sorting grail

* **I** => Inplace
* **S** => Stable

TBD: Quicksort worst/avg = 1.39 N lg N ?
TBD: lg or ln?

## ST(Search Tree) implementations

| implementation                | WC search | WC insert | WC delete | AC search hit | AC insert | AC delete | ordered it? | key i/f
| --------------                | --------- | --------- | --------- | ------------- | --------- | --------- | ----------- | -------
| seq search (unordered list)   |   N       |      N    |      N    |       N/2     |   N       |    N/2    |     no      | equals()
| binary search (ordered array) |  lg N     |      N    |      N    |      lg N     |  N/2      |    N/2    |    yes      | compareTo()
| BST                           |   N       |      N    |      N    |    1.38 ln N  | 1.38 lg N |     ?     |    yes      | compareTo()
| red-black BST                 | 2 lg N    |    2 lg N |    2 lg N |    1.00 ln N  | 1.00 lg N | 1.00 lg N |    yes      | compareTo()
| separate chaining             |   lg N    |      lg N |      lg N |    3 - 5*     | 3 - 5*    | 3 - 5*    |     no      | equals()
| linear probing                |   lg N    |      lg N |      lg N |    3 - 5*     | 3 - 5*    | 3 - 5*    |     no      | equals()

* **WC** => worst-case cost (after N inserts)
* **AC** => average-case cost (after N random inserts)
* **ordered it** => ordered iterator
* * => under uniform hashing assumption


## Single source shortest-paths implementations

| algorithm                 | restriction        | typical | worst   | extra space
| ------------------------- | ------------------ | ------- | ------- | -----------
| topological sort          | no directed cycles | E + V   | E + V   | V
| Dijkstra (binary heap)    | no neg. weights    | E log V | E log V | V
| Bellman-Ford              | no neg. cycles     | E V     | E V     | V
| Bellman-Ford (queue-based)| no neg. cycles     | E + V   | E + V   | V

* **cg**: Works with a graph which has cycles
* **nw**: Works with a graph which has negative weights
* **nc**: works with a graph which has negative cycles

* **Remark 1.** Directed cycles make the problem harder
* **Remark 2.** Negative weights make the problem harder
* **Remark 3.** Negative cycles makes the problem intractable

| cg | nw | nc |
| -- | -- | -- |
|  N |  Y |  x |
|  Y |  N |  N |
|  Y |  Y |  N |
|  Y |  Y |  N |
