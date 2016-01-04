# Regular Expressions

## Code
  * **Regular Expressions**
  * **REs (Regular Expression) and NFAs (Nondeterministic Finite Automaton)**
  * **NFA Simulation**: 
    NFA.py, 
    [DirectedDFS.py](../py/AlgsSedgewickWayne/DepthFirstPaths.py)
  * **NFA Construction**
  * **Regular Expression Applications**: GREP.py

## Table of Contents for Examples
  1. [NFA states after reading characters](#Q1)    
  2. [Edges in NFA generated epsilon-transition digraph?](#Q2)    

## Examples 
### [Q1](#table-of-contents-for-examples)    
**NFA states after reading characters**    
```
Consider the NFA for the regular expression

     ( ( C ( A * | B ) ) * B ) 

with match transitions

     0        1        2        3        4        5        6        7        8        9        10       11       12       13      
    (()      (()      (C)----->(()      (A)----->(*)      (|)      (B)----->())      ())      (*)      (B)----->())      ( )


and epsilon transitions

    0->1
    1->10
    1->2
    3->7
    3->4
    4->5
    5->6
    5->4
    6->8
    8->9
    9->10
    10->11
    10->1
    12->13


Give the set of states (in ascending order) that the NFA could be in after reading
the following sequence of 6 characters:

     C A C C C B 
```

### [Q2](#table-of-contents-for-examples)    
**Edges in NFA generated epsilon-transition digraph?**    
```
Compute the NFA that corresponds to the following regular expression using
the NFA construction algorithm described in lecture and in the textbook:

     ( A | ( ( B D * ) C ) * ) 

Here are the match transitions:

     0        1        2        3        4        5        6        7        8        9        10       11       12       13      
    (()      (A)----->(|)      (()      (()      (B)----->(D)----->(*)      ())      (C)----->())      (*)      ())      ( )


Which of the following are edges in the epsilon-transition digraph?

  0->3
  7->8
  7->6
  12->3
  1->4
  3->12
  11->3
```

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
