# [Tries](http://algs4.cs.princeton.edu/52trie) from re**trie**val, but pronounced "try"    

## Code
  * **R-way Tries**: TrieSt.py    
  * **Ternary Search Tries**: TST.py    
  * **Character-Based Operations** including:
    * keysWithPrefix    
    * keysThatMatch    
    * longestPrexifOf   
  * **Character-Based Operations** PatriciaST.py, Suffix Tree
  

## Table of Contents for Examples
  1. [How many (non-null) nodes does the resulting trie contain?](#ex1)    
  2. [What are the depths of the nodes corresponding to the last characters in the 7 strings?](#ex2)    

## Examples 
### [ex1](#table-of-contents-for-examples)    
**How many (non-null) nodes does the resulting trie contain?**    
```
Suppose that you insert the following sequence of 7 strings into a multiway trie (R = 3):

    223 3211 2121 13 112 221 232 

How many (non-null) nodes does the resulting trie contain (including the root node)?
```

### [ex2](#table-of-contents-for-examples)    
**What are the depths of the nodes corresponding to the last characters in the 7 strings?**    
```
Suppose that you insert the following sequence of 7 strings into a ternary search trie:

    432 542 442 343 123 342 114 

What are the depths of the nodes corresponding to the last characters in the 7 strings
(in the order the strings were inserted)? Recall: the depth of the root node is 0.

              0    1    2    3    4    5    6 
            -----------------------------------
      key    432  542  442  343  123  342  114  
    depth  
```


Copyright (C) 2002-2016 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2016 DV Klopfenstein. All rights reserved. Python translation.
