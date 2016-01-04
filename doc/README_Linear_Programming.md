# Linear Programming

## Code
  * **Brewer's Problem**
  * **Simplex Algorithm**
  * **Simplex Implementations**: LinearProgramming.py
  * **Linear Programming Reductions**

## Table of Contents for Examples
1. [A1](#A1)
```
Which of the following constraints can be modeled by one or more linear inequalties?
  * (x1)^2 + (x2)^2 + (x3)^2 <= 10
  * x1 + 2x2 + 3x3 + 4x4 + 10 <= 5x1 + 6x2 + 12x5.
  * x1 + 2x2 + 3x3 + 4x4 >= 10.
  * 16 (x1)^2  = 20
  * x1, x2, x3, x4 are unconstrained
```
2. [A2](#A2)
```
Consider the following linear programming simplex tableaux with 3 equations and 8 variables:

    maximize Z
                -  4/3 x1             -    1 x3             +  1/4 x5  -    8 x6  +    3 x7    -  Z    = -198
    ---------------------------------------------------------------------------------------------------------
                -  7/3 x1  +    1 x2  +  3/2 x3             +  1/3 x5  +    8 x6  +  3/4 x7            =   18
                -    8 x1             +    4 x3  +    1 x4  -  3/2 x5  +  2/5 x6  -    6 x7            =   24
     +    1 x0  +  5/2 x1             +  3/4 x3             +    1 x5  -  2/3 x6  -    3 x7            =   42
            x0  ,      x1  ,      x2  ,      x3  ,      x4  ,      x5  ,      x6  ,      x7           >=    0


Which variable could be the next to *enter* the basis? Check all that apply.
  * x0
  * x1
  * x2
  * x3
  * x4
  * x5
  * x6
  * x7
```
3. [A3](#A2)
```
Consider the following linear programming simplex tableaux with 5 equations and 9 variables:

    maximize Z
                           -  1/2 x2  +    2 x3             -  9/5 x5                        -  3/4 x8    -  Z    = -144
    --------------------------------------------------------------------------------------------------------------------
                           +  2/5 x2  +    6 x3  +    1 x4  -  7/4 x5                        -    9 x8            =   12
                           + 10/3 x2  +    6 x3             -    9 x5  +    1 x6             +  7/5 x8            =   12
                +    1 x1  +    2 x2  +  7/5 x3             +    2 x5                        +  7/3 x8            =   36
                           +  3/5 x2  +    1 x3             +    2 x5             +    1 x7  +  1/3 x8            =   24
     +    1 x0             +    1 x2  -  9/2 x3             -    1 x5                        -  9/2 x8            =   24
            x0  ,      x1  ,      x2  ,      x3  ,      x4  ,      x5  ,      x6  ,      x7  ,      x8           >=    0


Suppose that variable x3 is the variable chosen to enter the basis.
Which variable or variables could be the next to *leave* the basis? Check all that apply.
  * x0
  * x1
  * x2
  * x3
  * x4
  * x5
  * x6
  * x7
  * x8
```




## Examples 
### [A1](#table-of-contents-for-examples)
```
Which of the following constraints can be modeled by one or more linear inequalties?
```
* (x1)^2 + (x2)^2 + (x3)^2 <= 10
*False*    
* x1 + 2x2 + 3x3 + 4x4 + 10 <= 5x1 + 6x2 + 12x5.
*True*    
* x1 + 2x2 + 3x3 + 4x4 >= 10.
*True*    
* 16 (x1)^2  = 20
*False*    
* x1, x2, x3, x4 are unconstrained
*True*    

### [A2](#table-of-contents-for-examples)
```
Consider the following linear programming simplex tableaux with 3 equations and 8 variables:

    maximize Z
                -  4/3 x1             -    1 x3             +  1/4 x5  -    8 x6  +    3 x7    -  Z    = -198
    ---------------------------------------------------------------------------------------------------------
                -  7/3 x1  +    1 x2  +  3/2 x3             +  1/3 x5  +    8 x6  +  3/4 x7            =   18
                -    8 x1             +    4 x3  +    1 x4  -  3/2 x5  +  2/5 x6  -    6 x7            =   24
     +    1 x0  +  5/2 x1             +  3/4 x3             +    1 x5  -  2/3 x6  -    3 x7            =   42
            x0  ,      x1  ,      x2  ,      x3  ,      x4  ,      x5  ,      x6  ,      x7           >=    0


```
Which variable could be the next to *enter* the basis? Check all that apply.    
* x0
*False*    
* x1
*False*    
* x2
*False*    
* x3
*False*    
* x4
*False*    
* x5
*True*    
* x6
*False*    
* x7
*True*    

### [A3](#table-of-contents-for-examples)
```
Consider the following linear programming simplex tableaux with 5 equations and 9 variables:

    maximize Z
                           -  1/2 x2  +    2 x3             -  9/5 x5                        -  3/4 x8    -  Z    = -144
    --------------------------------------------------------------------------------------------------------------------
                           +  2/5 x2  +    6 x3  +    1 x4  -  7/4 x5                        -    9 x8            =   12
                           + 10/3 x2  +    6 x3             -    9 x5  +    1 x6             +  7/5 x8            =   12
                +    1 x1  +    2 x2  +  7/5 x3             +    2 x5                        +  7/3 x8            =   36
                           +  3/5 x2  +    1 x3             +    2 x5             +    1 x7  +  1/3 x8            =   24
     +    1 x0             +    1 x2  -  9/2 x3             -    1 x5                        -  9/2 x8            =   24
            x0  ,      x1  ,      x2  ,      x3  ,      x4  ,      x5  ,      x6  ,      x7  ,      x8           >=    0


Suppose that variable x3 is the variable chosen to enter the basis.
```
Which variable or variables could be the next to *leave* the basis? Check all that apply.    
* x0
*False*    
* x1
*False*    
* x2
*False*    
* x3
*False*    
* x4
*True*    
* x5
*False*    
* x6
*True*    
* x7
*False*    
* x8
*False*    

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
