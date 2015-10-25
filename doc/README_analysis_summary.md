# Implementations Summary


## Sorting Summary    

| Sort        | I | S | worst  | average | best    | remarks    
| ----------- | - | - | ------ | ------- | ------- | --------------------    
| Selection   | Y |   | N^2/2  |   N^2/2 |   N^2/2 | N exchanges    
| Insertion   | Y | Y | N^2/2  |   N^2/4 |       N | use for small N or partially ordered    
| Shell       | Y |   |     ?  |       ? |       N | tight code, subquadratic     
| Merge       |   | Y | N lg N |  N lg N |  N lg N | N lg N guarantee, stable     
| Quick       | Y |   | N^2/2  | 2N ln N |  N lg N | N lg N probabilistic guarantee, fastest in practice     
| 3-way quick | Y |   | N^2/2  | 2N ln N |       N | better w/duplicate keys    
| ???         | Y | Y | N lg N |  N lg N |  N lg N | holy sorting grail     

* **I** => Inplace
* **S** => Stable

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
