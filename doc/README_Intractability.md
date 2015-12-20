# Intractability

## Code
  * **Introduction to Intractability**
  * **Search Problems**
  * **P vs. NP**
  * **Classifying Problems**
  * **NP-Completeness**
  * **Coping with Intractability**

## Table of Contents for Examples
  1. [which of the following problems are known to be in P Check all that apply](#q1a)
    * PRIMALITY: given an N-bit integer x, is x prime?    
    * EULER-CYCLE: given an undirected graph, find a simple cycle that visits every edge exactly once.    
    * LSOLVE: given a system of N variables and N linear equations, find a solution.    
    * EULER-PATH: given an undirected graph, find a simple path that visits every edge exactly once.    
    * HAMILTON-CYCLE: given an undirected graph, find a simple cycle that visits every vertex exactly once.    

  2. [Suppose that a search problem x is NP-complete. Which of the following statements can you infer?](#q2a)
    * if X cannot be solved in polynomial time, then neither can FACTOR (and every other problem in NP).    
    * if X can be solved in polynomial time, then so can FACTOR (and every other problem in NP).    
    * All search problems polynomial reduce to X.    
    * X cannot be solved in polynomial time.    
    * X polynomial reduces to SAT.    

  3. [What is the definition of the complexity class NP?](#q3a)
    * All search problems.    
    * All problems not solvable in polynomial space.    
    * All search problems that are not solvable in polynomial time.    
    * All problems not solvable in polynomial time.    
    * All problems solvable in exponential time.    

## Examples 
### [q1a](#table-of-contents-for-examples)
1. Known to be in **P**:    
    * PRIMALITY: given an N-bit integer x, is x prime?    
    * EULER-CYCLE: given an undirected graph, find a simple cycle that visits every edge exactly once.    
    * LSOLVE: given a system of N variables and N linear equations, find a solution.    
    * EULER-PATH: given an undirected graph, find a simple path that visits every edge exactly once.    
**Not P**:    
    * HAMILTON-CYCLE: given an undirected graph, find a simple cycle that visits every vertex exactly once.    

### [q2a](#table-of-contents-for-examples)
2. Regarding search problem X, which is NP-complete:    
    * **F**: if X cannot be solved in polynomial time, then neither can FACTOR (and every other problem in NP).    
    * **T**: if X can be solved in polynomial time, then so can FACTOR (and every other problem in NP).    
    * **T**: All search problems polynomial reduce to X.    
    * **F**: X cannot be solved in polynomial time.    
    * **T**: X polynomial reduces to SAT.    

### [q3a](#table-of-contents-for-examples)
3. What is the definition of the complexity class NP?
    * **T**: All search problems.    
    * **F**: All problems not solvable in polynomial space.    
    * **F**: All search problems that are not solvable in polynomial time.    
    * **F**: All problems not solvable in polynomial time.    
    * **F**: All problems solvable in exponential time.    

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
