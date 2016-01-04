# [Reductions](http://algs4.cs.princeton.edu/65reductions)

## Code
  * **Introduction to Reductions**
  * **Designing Algorithms**
  * **Establishing Lower Bounds**
  * **Classifying Problems**

## Table of Contents for Examples
  1. [linear-time reduced](#Q1)    
  2. [asymptotic complexity](#Q2)    
  3. [3-SUM linear-time reduces to 3-COLLINEAR](#Q3)    

## Examples 
### [Q1](#table-of-contents-for-examples)
**linear-time reduced**    
```
Which of the following problems can be linear-time reduced
*from* element distinctness: Given an array of N real
numbers, are they all distinct? Assume the quadratic
decision tree model of computation. Check all that apply.

  * Given N coins and a balance scale, determine if the coins all weigh different amounts.
  * Given two arrays of N real numbers, find one that appears in each array.
  * Given an array of N real numbers, find one that occurs more than N/10 times.
  * Given an array of N real numbers, find a median.
  * Given an array of N real numbers, find one that occurs most frequently.
```
[A1](#A1)

### [Q2](#table-of-contents-for-examples)
**asymptotic complexity**    
```
Which problems are known to have the same asymptotic
complexity as multiplying two N-bit integers? Check all that
apply.
  * Multiplying an N-bit integer by 17.
  * Computing the remainder when dividing one N-bit integer into an N-bit integer.
  * Squaring an N-bit integer.
  * Computing the square root of an N-bit integer, and rounding it down to the nearest integer.
  * Computing the quotient when dividing one N-bit integer into a 2N-bit integer.
```
[A2](#A2)

### [Q3](#table-of-contents-for-examples)
**3-SUM linear-time reduces to 3-COLLINEAR**    
```
Suppose that 3-SUM has a N^(3/2) lower bound and that 3-SUM
linear-time reduces to 3-COLLINEAR. Which of the following
can you infer? Check all that apply.

  * If 3-COLLINEAR can be solved in N^(3/2) time, then so can 3-SUM.
  * If 3-COLLINEAR cannot be solved in N^(5/3) time, then neither can 3-SUM.
  * 3-SUM can be solved in N^(3/2) time.
  * If 3-SUM cannot be solved in N^(5/3) time, then neither can 3-COLLINEAR.
  * If 3-SUM can be solved in N^(3/2) time, then so can 3-COLLINEAR.
```
[A3](#A3)


### [A1](#table-of-contents-for-examples)
**linear-time reduced**    
```
Which of the following problems can be linear-time reduced
*from* element distinctness: Given an array of N real
numbers, are they all distinct? Assume the quadratic
decision tree model of computation. Check all that apply.
```
* Given N coins and a balance scale, determine if the coins all weigh different amounts.
*True*    
* Given two arrays of N real numbers, find one that appears in each array.
*True*    
* Given an array of N real numbers, find one that occurs more than N/10 times.
*False*    
* Given an array of N real numbers, find a median.
*False*    
* Given an array of N real numbers, find one that occurs most frequently.
*True*    
[A1](#A1)

### [A2](#table-of-contents-for-examples)
**asymptotic complexity**    
```
Which problems are known to have the same asymptotic
complexity as multiplying two N-bit integers? Check all that
apply.
```
* Multiplying an N-bit integer by 17.
*False*    
* Computing the remainder when dividing one N-bit integer into an N-bit integer.
*True*    
* Squaring an N-bit integer.
*True*    
* Computing the square root of an N-bit integer, and rounding it down to the nearest integer.
*True*    
* Computing the quotient when dividing one N-bit integer into a 2N-bit integer.
*True*    
[A2](#A2)

### [A3](#table-of-contents-for-examples)
**3-SUM linear-time reduces to 3-COLLINEAR**    
```
Suppose that 3-SUM has a N^(3/2) lower bound and that 3-SUM
linear-time reduces to 3-COLLINEAR. Which of the following
can you infer? Check all that apply.
```
* If 3-COLLINEAR can be solved in N^(3/2) time, then so can 3-SUM.
*True*    
* If 3-COLLINEAR cannot be solved in N^(5/3) time, then neither can 3-SUM.
*False*    
* 3-SUM can be solved in N^(3/2) time.
*False*    
* If 3-SUM cannot be solved in N^(5/3) time, then neither can 3-COLLINEAR.
*True*    
* If 3-SUM can be solved in N^(3/2) time, then so can 3-COLLINEAR.
*False*    
[A3](#A3)

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
