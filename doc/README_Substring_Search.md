# [Substring Search](http://algs4.cs.princeton.edu/53substring)

## Code
  * **Introduction to Substring Search**
  * **Brute-Force Substring Search**
  * **Knuth-Morris-Pratt**: [KMP.py](../py/AlgsSedgewickWayne/KMP.py)
  * **Boyer-Moore**: BoyerMoore.py
  * **Rabin-Karp**: RabinKarp.py

## Table of Contents for Examples
  q0. [test_KMP.py ababac aabdacaababacdaa](#ex0)    
  q1. [KMP DFA: What is sequence of values in the row of the DFA corresponding to the character 'B'?](#ex1)    
  q2. [Boyer-Moore: What is the sequence of characters in the text that is compared with the last character in the pattern?](#ex2)    
  q3. [Rabin-Karp](#ex3)    

## Examples 
### [ex0](#table-of-contents-for-examples)
1. Run KMP: 
```
>>> test_KMP.py ababac aabdacaababacdaa
```
Shows the 1st occurance of the pattern(ababac) in the text(aabdacaababacdaa)
```
text:    aabdacaababacdaa
pattern:        ababac
```
And prints the DFA (Deterministic finite state automatom) created using the pattern
```
     a b a b a c
     0 1 2 3 4 5 <- Current State
a -> 1 1 3 1 5 1
b -> 0 2 0 4 0 4
c -> 0 0 0 0 0 6
```

### [ex1](#table-of-contents-for-examples)
**KMP DFA: What is sequence of values in the row of the DFA corresponding to the character 'B'?**    
```
Consider the Knuth-Morris-Pratt DFA for the following string of length 8:

     A B A B A A A C 

What is sequence of values in the row of the DFA corresponding to
the character 'B'? For reference, here is the partially-completed DFA:

       0  1  2  3  4  5  6  7 
       ----------------------
    A  1  1  3  1  5  6  7  1 
    B  ?  ?  ?  ?  ?  ?  ?  ? 
    C  0  0  0  0  0  0  0  8 
```

### [ex2](#table-of-contents-for-examples)
**Boyer-Moore: What is the sequence of characters in the text that is compared with the last character in the pattern?**    
```
Suppose that you run the Boyer-Moore algorithm (using only the mismatched character heuristic)
to search for the pattern

         H E R S A N D 

in the text

         F O U L O N H U S B A N D S A N D B R O T H E R S A N D Y O 

What is the sequence of characters in the text that is compared with the
last character in the pattern?
```

### [ex3](#table-of-contents-for-examples)
**Rabin-Karp**    
```
What is the Rabin-Karp hash function of text[4..10] over the decimal
alphabet with R = 10 and using the modulus Q = 83?

       j      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 
    --------------------------------------------------------------------
    text[j]   7  6  3  2  3  2  ?  ?  9  5  1  5  3  3  9  0  6  7  0  9  

The digits labeled with a ? are suppressed (and are not needed to solve the problem).
Assume that the hash function of text[3..9] is 64 and that you have precomputed
1000000 (mod 83) = 16.
```

Copyright (C) 2002-2016 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2016 DV Klopfenstein. All rights reserved. Python translation.
