# [Substring Search](http://algs4.cs.princeton.edu/53substring)

## Code
  * **Introduction to Substring Search**
  * **Brute-Force Substring Search**
  * **Knuth-Morris-Pratt**: [KMP.py](../AlgsSedgewickWayne/KMP.py)
  * **Boyer-Moore**: BoyerMoore.py
  * **Rabin-Karp**: RabinKarp.py

## Table of Contents for Examples
  1. [test_KMP.py ababac aabdacaababacdaa](#ex1)

## Examples 
### [ex1](#table-of-contents-for-examples)
1. KMP Example
Running a pattern match
```
>>> test_KMP.py ababac aabdacaababacdaa
```
Shows the 1st occurance of the pattern in the text
```
text:    aabdacaababacdaa
pattern:        ababac
```
And prints the DFA(Deterministic finite state automatom) created using the pattern
```
     a b a b a c
     0 1 2 3 4 5 <- Current State
a -> 1 1 3 1 5 1
b -> 0 2 0 4 0 4
c -> 0 0 0 0 0 6
```


Copyright (C) 2002-2016 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2016 DV Klopfenstein. All rights reserved. Python translation.
