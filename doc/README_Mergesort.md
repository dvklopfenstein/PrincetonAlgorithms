# Mergesort

## Code
  * [Merge](../py/AlgsSedgewickWayne/Merge.py) => Top-down Mergesort
  * MergeX => Top-down Mergesort with practical improvements
  * [MergeBU](../py/AlgsSedgewickWayne/MergeBU.py) => Bottom-up Mergesort (no recursion)

## Table of Contents for Examples
  1. [Run Mergesort (Top-Down)](#ex1)
  2. [Run Mergesort (Bottom-Up)](#ex2)

## Examples
### [ex1](#table-of-contents-for-examples)
1. Run Top-Down Mergesort example
```
python -c 'import test_Merge as T; T.test_14238()'
```
```
 0: 80 97 50 29 23 83 66 67 43 47 41 42 <= arr
 0: __ __ __ __ __ __ __ __ __ __ __ __ <= aux

 1: *  +  .. .. .. .. .. .. .. .. .. .. <= arr (0 *), (1 +)
    .. .. .. .. .. .. .. .. .. .. .. .. <= arr compare
 1: 80 97 50 29 23 83 66 67 43 47 41 42 <= arr
    XX XX .. .. .. .. .. .. .. .. .. .. <= aux compare
 1: 80 97 __ __ __ __ __ __ __ __ __ __ <= aux

 2: -  *  +  .. .. .. .. .. .. .. .. .. <= arr (0 -), (2 +), (1 *)
    X. XX XX .. .. .. .. .. .. .. .. .. <= arr compare
 2: 50 80 97 29 23 83 66 67 43 47 41 42 <= arr
    .. .. XX .. .. .. .. .. .. .. .. .. <= aux compare
 2: 80 97 50 __ __ __ __ __ __ __ __ __ <= aux

 3: .. .. .. *  +  .. .. .. .. .. .. .. <= arr (3 *), (4 +)
    .. .. .. .X .X .. .. .. .. .. .. .. <= arr compare
 3: 50 80 97 23 29 83 66 67 43 47 41 42 <= arr
    .. .. .. XX XX .. .. .. .. .. .. .. <= aux compare
 3: 80 97 50 29 23 __ __ __ __ __ __ __ <= aux

 4: .. .. .. -  *  +  .. .. .. .. .. .. <= arr (3 -), (5 +), (4 *)
    .. .. .. .. .. .. .. .. .. .. .. .. <= arr compare
 4: 50 80 97 23 29 83 66 67 43 47 41 42 <= arr
    .. .. .. .X .X XX .. .. .. .. .. .. <= aux compare
 4: 80 97 50 23 29 83 __ __ __ __ __ __ <= aux

 5: -  .. *  .. .. +  .. .. .. .. .. .. <= arr (0 -), (5 +), (2 *)
    XX XX XX XX XX XX .. .. .. .. .. .. <= arr compare
 5: 23 29 50 80 83 97 66 67 43 47 41 42 <= arr
    X. XX XX .. .. .. .. .. .. .. .. .. <= aux compare
 5: 50 80 97 23 29 83 __ __ __ __ __ __ <= aux

 6: .. .. .. .. .. .. *  +  .. .. .. .. <= arr (6 *), (7 +)
    .. .. .. .. .. .. .. .. .. .. .. .. <= arr compare
 6: 23 29 50 80 83 97 66 67 43 47 41 42 <= arr
    .. .. .. .. .. .. XX XX .. .. .. .. <= aux compare
 6: 50 80 97 23 29 83 66 67 __ __ __ __ <= aux

 7: .. .. .. .. .. .. -  *  +  .. .. .. <= arr (6 -), (8 +), (7 *)
    .. .. .. .. .. .. XX .X XX .. .. .. <= arr compare
 7: 23 29 50 80 83 97 43 66 67 47 41 42 <= arr
    .. .. .. .. .. .. .. .. XX .. .. .. <= aux compare
 7: 50 80 97 23 29 83 66 67 43 __ __ __ <= aux

 8: .. .. .. .. .. .. .. .. .. *  +  .. <= arr (9 *), (10 +)
    .. .. .. .. .. .. .. .. .. .X .X .. <= arr compare
 8: 23 29 50 80 83 97 43 66 67 41 47 42 <= arr
    .. .. .. .. .. .. .. .. .. XX XX .. <= aux compare
 8: 50 80 97 23 29 83 66 67 43 47 41 __ <= aux

 9: .. .. .. .. .. .. .. .. .. -  *  +  <= arr (9 -), (11 +), (10 *)
    .. .. .. .. .. .. .. .. .. .. .X .X <= arr compare
 9: 23 29 50 80 83 97 43 66 67 41 42 47 <= arr
    .. .. .. .. .. .. .. .. .. .X .X XX <= aux compare
 9: 50 80 97 23 29 83 66 67 43 41 47 42 <= aux

10: .. .. .. .. .. .. -  .. *  .. .. +  <= arr (6 -), (11 +), (8 *)
    .. .. .. .. .. .. .X XX XX .X XX X. <= arr compare
10: 23 29 50 80 83 97 41 42 43 47 66 67 <= arr
    .. .. .. .. .. .. XX .X XX .. .X .X <= aux compare
10: 50 80 97 23 29 83 43 66 67 41 42 47 <= aux

11: -  .. .. .. .. *  .. .. .. .. .. +  <= arr (0 -), (11 +), (5 *)
    .. .. XX XX X. X. XX XX XX XX XX X. <= arr compare
11: 23 29 41 42 43 47 50 66 67 80 83 97 <= arr
    XX XX XX XX XX XX .X XX XX .X XX X. <= aux compare
11: 23 29 50 80 83 97 41 42 43 47 66 67 <= aux

14238 RESULT: [23, 29, 41, 42, 43, 47, 50, 66, 67, 80, 83, 97]
```

### [ex2](#table-of-contents-for-examples)
2. Run Bottom-Up Mergesort (Bottom-Up) 
```
$ python -c 'import test_MergeBU as T; T.test_193860()'
```
```
 0: 25 94 79 41 19 84 66 67 90 37 <= arr
 0: __ __ __ __ __ __ __ __ __ __ <= aux

 1: *  +  .. .. .. .. .. .. .. .. <= arr (0 *), (1 +)
    .. .. .. .. .. .. .. .. .. .. <= arr compare
 1: 25 94 79 41 19 84 66 67 90 37 <= arr
    XX XX .. .. .. .. .. .. .. .. <= aux compare
 1: 25 94 __ __ __ __ __ __ __ __ <= aux

 2: .. .. *  +  .. .. .. .. .. .. <= arr (2 *), (3 +)
    .. .. XX XX .. .. .. .. .. .. <= arr compare
 2: 25 94 41 79 19 84 66 67 90 37 <= arr
    .. .. XX XX .. .. .. .. .. .. <= aux compare
 2: 25 94 79 41 __ __ __ __ __ __ <= aux

 3: .. .. .. .. *  +  .. .. .. .. <= arr (4 *), (5 +)
    .. .. .. .. .. .. .. .. .. .. <= arr compare
 3: 25 94 41 79 19 84 66 67 90 37 <= arr
    .. .. .. .. XX XX .. .. .. .. <= aux compare
 3: 25 94 79 41 19 84 __ __ __ __ <= aux

 4: .. .. .. .. .. .. *  +  .. .. <= arr (6 *), (7 +)
    .. .. .. .. .. .. .. .. .. .. <= arr compare
 4: 25 94 41 79 19 84 66 67 90 37 <= arr
    .. .. .. .. .. .. XX XX .. .. <= aux compare
 4: 25 94 79 41 19 84 66 67 __ __ <= aux

 5: .. .. .. .. .. .. .. .. *  +  <= arr (8 *), (9 +)
    .. .. .. .. .. .. .. .. XX XX <= arr compare
 5: 25 94 41 79 19 84 66 67 37 90 <= arr
    .. .. .. .. .. .. .. .. XX XX <= aux compare
 5: 25 94 79 41 19 84 66 67 90 37 <= aux

 6: -  *  .. +  .. .. .. .. .. .. <= arr (0 -), (3 +), (1 *)
    .. XX XX XX .. .. .. .. .. .. <= arr compare
 6: 25 41 79 94 19 84 66 67 37 90 <= arr
    .. .. XX XX .. .. .. .. .. .. <= aux compare
 6: 25 94 41 79 19 84 66 67 90 37 <= aux

 7: .. .. .. .. -  *  .. +  .. .. <= arr (4 -), (7 +), (5 *)
    .. .. .. .. .. XX .X XX .. .. <= arr compare
 7: 25 41 79 94 19 66 67 84 37 90 <= arr
    .. .. .. .. .. .. .. .. .. .. <= aux compare
 7: 25 94 41 79 19 84 66 67 90 37 <= aux

 8: -  .. .. *  .. .. .. +  .. .. <= arr (0 -), (7 +), (3 *)
    XX XX XX XX XX XX XX X. .. .. <= arr compare
 8: 19 25 41 66 67 79 84 94 37 90 <= arr
    .. XX XX XX .. XX .X XX .. .. <= aux compare
 8: 25 41 79 94 19 66 67 84 90 37 <= aux

 9: -  .. .. .. .. .. .. *  .. +  <= arr (0 -), (9 +), (7 *)
    .. .. XX XX .X XX XX X. XX .X <= arr compare
 9: 19 25 37 41 66 67 79 84 90 94 <= arr
    XX XX XX XX XX XX XX X. XX XX <= aux compare
 9: 19 25 41 66 67 79 84 94 37 90 <= aux

BOTTOM-UP MERGESORT RESULT: [19, 25, 37, 41, 66, 67, 79, 84, 90, 94]
```
