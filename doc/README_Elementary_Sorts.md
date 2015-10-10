# Stacks and Queues

## Code
  * [Selection Sort](../py/AlgsSedgewickWayne/Selection.py)
  * [Insertion Sort](../py/AlgsSedgewickWayne/Insertion.py)
  * [Shell Sort](../py/AlgsSedgewickWayne/Shell.py)
  * [Shuffling](../py/AlgsSedgewickWayne/Knuth.py) using the Knuth Shuffle
  * **Convex Hull**, an application of sort
    * Point2D, used by Graham scan
    * Graham scan

## Visualization Description
There are two ways to view the progression of a sort:

  1. The concise way: One print of the array state per iteration.     

| X | There is a difference between the last state and the current state    
| . | There is NO difference between the last state and the current state     

It looks like this:    

```
     0: 33 49 51 64 92 71 70 42 63 59  # Initial state of array
        .. .. .. .. XX XX .. .. .. ..  # Shows matches and mismatches between lines
     1: 33 49 51 64 71 92 70 42 63 59  # 1st Exchange
        .. .. .. .. .. XX XX .. .. ..
     2: 33 49 51 64 71 70 91 42 63 59  # 2nd Exchange
     ...
```

  2. The verbose but visually pleasing way of viewing the sort progression.

     The second way of visualizing includes one "paragraph" for each
     iteration. There are horizontal "bars" made of '*'s showing 
     how large each element is. This helps dyslexics and tired people
     to not be confused as to which element is bigger when viewing a 
     ton of numbers or letters all at once. As we proceed through each paragragh,
     notice that the bars begin to lined up in smallest to biggest order.
     This is the verbose, but descriptive way to see the progression of the sort.

## Table of Contents for Examples
  1. [Run Lecture Example from **Selection (6:59)**](#ex1) (N^2)     
  2. [Run Lecture Example from **Insertion (9:28)**](#ex2) (N^2/4)    
  2a. [Run Best Case Example from **Insertion (9:28)**](#ex2a); Array is already sorted (N)   
  2b. [Run Worst Case Example from **Insertion (9:28)**](#ex2b); Array is sorted in descending order   
  2c. [Run Paritally-sorted Example from **Insertion (9:28)**](#ex2c); 
      Array has inversions: a pair of keys out order (N)
  3. [Run Lecture Example from **Shellsort (10:48)**](#ex3) (WC=O(N^(3/2), Avg~k*N?)   
  4. [Visualize various intermediate states from various sorts: **Selection, Insertion, and Shell**](#ex4)

## Examples
### [ex1](#stacks-and-queues)
1. Run Lecture Example from **Selection (6:59)**
```
> python -c 'import test_Selection as T; T.test_wk2_lec()'
```
```
SELECTION SORT
 0: 7 10 5 3 8 4 2 9 6
    X .. . . . . X . .
 1: 2 10 5 3 8 4 7 9 6
    . X X XX . . . . .
 2: 2 3 5 10 8 4 7 9 6
    . . X .. . X . . .
 3: 2 3 4 10 8 5 7 9 6
    . . . X X XX . . .
 4: 2 3 4 5 8 10 7 9 6
    . . . . X .. . . X
 5: 2 3 4 5 6 10 7 9 8
    . . . . . X XX . .
 6: 2 3 4 5 6 7 10 9 8
    . . . . . . X X XX
 7: 2 3 4 5 6 7 8 9 10
    . . . . . . . . ..
 8: 2 3 4 5 6 7 8 9 10
    . . . . . . . . ..
 9: 2 3 4 5 6 7 8 9 10

 0 SELECTION SORT: 7 10 5 3 8 4 2 9 6
 0 SELECTION SORT( 0): * 7 ******
 0 SELECTION SORT( 1):  10 *********
 0 SELECTION SORT( 2):   5 ****
 0 SELECTION SORT( 3):   3 **
 0 SELECTION SORT( 4):   8 *******
 0 SELECTION SORT( 5):   4 ***
 0 SELECTION SORT( 6): * 2 *
 0 SELECTION SORT( 7):   9 ********
 0 SELECTION SORT( 8):   6 *****

 1 SELECTION SORT: 2 10 5 3 8 4 7 9 6
 1 SELECTION SORT( 0):   2 *
 1 SELECTION SORT( 1): *10 *********
 1 SELECTION SORT( 2):   5 ****
 1 SELECTION SORT( 3): * 3 **
 1 SELECTION SORT( 4):   8 *******
 1 SELECTION SORT( 5):   4 ***
 1 SELECTION SORT( 6):   7 ******
 1 SELECTION SORT( 7):   9 ********
 1 SELECTION SORT( 8):   6 *****

 2 SELECTION SORT: 2 3 5 10 8 4 7 9 6
 2 SELECTION SORT( 0):   2 *
 2 SELECTION SORT( 1):   3 **
 2 SELECTION SORT( 2): * 5 ****
 2 SELECTION SORT( 3):  10 *********
 2 SELECTION SORT( 4):   8 *******
 2 SELECTION SORT( 5): * 4 ***
 2 SELECTION SORT( 6):   7 ******
 2 SELECTION SORT( 7):   9 ********
 2 SELECTION SORT( 8):   6 *****

 3 SELECTION SORT: 2 3 4 10 8 5 7 9 6
 3 SELECTION SORT( 0):   2 *
 3 SELECTION SORT( 1):   3 **
 3 SELECTION SORT( 2):   4 ***
 3 SELECTION SORT( 3): *10 *********
 3 SELECTION SORT( 4):   8 *******
 3 SELECTION SORT( 5): * 5 ****
 3 SELECTION SORT( 6):   7 ******
 3 SELECTION SORT( 7):   9 ********
 3 SELECTION SORT( 8):   6 *****

 4 SELECTION SORT: 2 3 4 5 8 10 7 9 6
 4 SELECTION SORT( 0):   2 *
 4 SELECTION SORT( 1):   3 **
 4 SELECTION SORT( 2):   4 ***
 4 SELECTION SORT( 3):   5 ****
 4 SELECTION SORT( 4): * 8 *******
 4 SELECTION SORT( 5):  10 *********
 4 SELECTION SORT( 6):   7 ******
 4 SELECTION SORT( 7):   9 ********
 4 SELECTION SORT( 8): * 6 *****

 5 SELECTION SORT: 2 3 4 5 6 10 7 9 8
 5 SELECTION SORT( 0):   2 *
 5 SELECTION SORT( 1):   3 **
 5 SELECTION SORT( 2):   4 ***
 5 SELECTION SORT( 3):   5 ****
 5 SELECTION SORT( 4):   6 *****
 5 SELECTION SORT( 5): *10 *********
 5 SELECTION SORT( 6): * 7 ******
 5 SELECTION SORT( 7):   9 ********
 5 SELECTION SORT( 8):   8 *******

 6 SELECTION SORT: 2 3 4 5 6 7 10 9 8
 6 SELECTION SORT( 0):   2 *
 6 SELECTION SORT( 1):   3 **
 6 SELECTION SORT( 2):   4 ***
 6 SELECTION SORT( 3):   5 ****
 6 SELECTION SORT( 4):   6 *****
 6 SELECTION SORT( 5):   7 ******
 6 SELECTION SORT( 6): *10 *********
 6 SELECTION SORT( 7):   9 ********
 6 SELECTION SORT( 8): * 8 *******

 7 SELECTION SORT: 2 3 4 5 6 7 8 9 10
 7 SELECTION SORT( 0):   2 *
 7 SELECTION SORT( 1):   3 **
 7 SELECTION SORT( 2):   4 ***
 7 SELECTION SORT( 3):   5 ****
 7 SELECTION SORT( 4):   6 *****
 7 SELECTION SORT( 5):   7 ******
 7 SELECTION SORT( 6):   8 *******
 7 SELECTION SORT( 7): * 9 ********
 7 SELECTION SORT( 8):  10 *********

 8 SELECTION SORT: 2 3 4 5 6 7 8 9 10
 8 SELECTION SORT( 0):   2 *
 8 SELECTION SORT( 1):   3 **
 8 SELECTION SORT( 2):   4 ***
 8 SELECTION SORT( 3):   5 ****
 8 SELECTION SORT( 4):   6 *****
 8 SELECTION SORT( 5):   7 ******
 8 SELECTION SORT( 6):   8 *******
 8 SELECTION SORT( 7):   9 ********
 8 SELECTION SORT( 8): *10 *********

 9 SELECTION SORT: 2 3 4 5 6 7 8 9 10
 9 SELECTION SORT( 0):   2 *
 9 SELECTION SORT( 1):   3 **
 9 SELECTION SORT( 2):   4 ***
 9 SELECTION SORT( 3):   5 ****
 9 SELECTION SORT( 4):   6 *****
 9 SELECTION SORT( 5):   7 ******
 9 SELECTION SORT( 6):   8 *******
 9 SELECTION SORT( 7):   9 ********
 9 SELECTION SORT( 8):  10 *********

```    


### [ex2](#stacks-and-queues)
2. Run Lecture Example from **Insertion (9:28)**
```
> python -c 'import test_Insertion as T; T.test_wk2_lec()'
```
```
 0: 7 10 5 3 8 4 2 9 6
    . X XX . . . . . .
 1: 7 5 10 3 8 4 2 9 6
    X X .. . . . . . .
 2: 5 7 10 3 8 4 2 9 6
    . . X XX . . . . .
 3: 5 7 3 10 8 4 2 9 6
    . X X .. . . . . .
 4: 5 3 7 10 8 4 2 9 6
    X X . .. . . . . .
 5: 3 5 7 10 8 4 2 9 6
    . . . X XX . . . .
 6: 3 5 7 8 10 4 2 9 6
    . . . . X XX . . .
 7: 3 5 7 8 4 10 2 9 6
    . . . X X .. . . .
 8: 3 5 7 4 8 10 2 9 6
    . . X X . .. . . .
 9: 3 5 4 7 8 10 2 9 6
    . X X . . .. . . .
10: 3 4 5 7 8 10 2 9 6
    . . . . . X XX . .
11: 3 4 5 7 8 2 10 9 6
    . . . . X X .. . .
12: 3 4 5 7 2 8 10 9 6
    . . . X X . .. . .
13: 3 4 5 2 7 8 10 9 6
    . . X X . . .. . .
14: 3 4 2 5 7 8 10 9 6
    . X X . . . .. . .
15: 3 2 4 5 7 8 10 9 6
    X X . . . . .. . .
16: 2 3 4 5 7 8 10 9 6
    . . . . . . X XX .
17: 2 3 4 5 7 8 9 10 6
    . . . . . . . X XX
18: 2 3 4 5 7 8 9 6 10
    . . . . . . X X ..
19: 2 3 4 5 7 8 6 9 10
    . . . . . X X . ..
20: 2 3 4 5 7 6 8 9 10
    . . . . X X . . ..
21: 2 3 4 5 6 7 8 9 10

 0 INSERTION SORT: : 7 10 5 3 8 4 2 9 6
 0 INSERTION SORT: ( 0):   7 ******
 0 INSERTION SORT: ( 1): *10 *********
 0 INSERTION SORT: ( 2): * 5 ****
 0 INSERTION SORT: ( 3):   3 **
 0 INSERTION SORT: ( 4):   8 *******
 0 INSERTION SORT: ( 5):   4 ***
 0 INSERTION SORT: ( 6):   2 *
 0 INSERTION SORT: ( 7):   9 ********
 0 INSERTION SORT: ( 8):   6 *****

 1 INSERTION SORT: : 7 5 10 3 8 4 2 9 6
 1 INSERTION SORT: ( 0): * 7 ******
 1 INSERTION SORT: ( 1): * 5 ****
 1 INSERTION SORT: ( 2):  10 *********
 1 INSERTION SORT: ( 3):   3 **
 1 INSERTION SORT: ( 4):   8 *******
 1 INSERTION SORT: ( 5):   4 ***
 1 INSERTION SORT: ( 6):   2 *
 1 INSERTION SORT: ( 7):   9 ********
 1 INSERTION SORT: ( 8):   6 *****

 2 INSERTION SORT: : 5 7 10 3 8 4 2 9 6
 2 INSERTION SORT: ( 0):   5 ****
 2 INSERTION SORT: ( 1):   7 ******
 2 INSERTION SORT: ( 2): *10 *********
 2 INSERTION SORT: ( 3): * 3 **
 2 INSERTION SORT: ( 4):   8 *******
 2 INSERTION SORT: ( 5):   4 ***
 2 INSERTION SORT: ( 6):   2 *
 2 INSERTION SORT: ( 7):   9 ********
 2 INSERTION SORT: ( 8):   6 *****

 3 INSERTION SORT: : 5 7 3 10 8 4 2 9 6
 3 INSERTION SORT: ( 0):   5 ****
 3 INSERTION SORT: ( 1): * 7 ******
 3 INSERTION SORT: ( 2): * 3 **
 3 INSERTION SORT: ( 3):  10 *********
 3 INSERTION SORT: ( 4):   8 *******
 3 INSERTION SORT: ( 5):   4 ***
 3 INSERTION SORT: ( 6):   2 *
 3 INSERTION SORT: ( 7):   9 ********
 3 INSERTION SORT: ( 8):   6 *****

 4 INSERTION SORT: : 5 3 7 10 8 4 2 9 6
 4 INSERTION SORT: ( 0): * 5 ****
 4 INSERTION SORT: ( 1): * 3 **
 4 INSERTION SORT: ( 2):   7 ******
 4 INSERTION SORT: ( 3):  10 *********
 4 INSERTION SORT: ( 4):   8 *******
 4 INSERTION SORT: ( 5):   4 ***
 4 INSERTION SORT: ( 6):   2 *
 4 INSERTION SORT: ( 7):   9 ********
 4 INSERTION SORT: ( 8):   6 *****

 5 INSERTION SORT: : 3 5 7 10 8 4 2 9 6
 5 INSERTION SORT: ( 0):   3 **
 5 INSERTION SORT: ( 1):   5 ****
 5 INSERTION SORT: ( 2):   7 ******
 5 INSERTION SORT: ( 3): *10 *********
 5 INSERTION SORT: ( 4): * 8 *******
 5 INSERTION SORT: ( 5):   4 ***
 5 INSERTION SORT: ( 6):   2 *
 5 INSERTION SORT: ( 7):   9 ********
 5 INSERTION SORT: ( 8):   6 *****

 6 INSERTION SORT: : 3 5 7 8 10 4 2 9 6
 6 INSERTION SORT: ( 0):   3 **
 6 INSERTION SORT: ( 1):   5 ****
 6 INSERTION SORT: ( 2):   7 ******
 6 INSERTION SORT: ( 3):   8 *******
 6 INSERTION SORT: ( 4): *10 *********
 6 INSERTION SORT: ( 5): * 4 ***
 6 INSERTION SORT: ( 6):   2 *
 6 INSERTION SORT: ( 7):   9 ********
 6 INSERTION SORT: ( 8):   6 *****

 7 INSERTION SORT: : 3 5 7 8 4 10 2 9 6
 7 INSERTION SORT: ( 0):   3 **
 7 INSERTION SORT: ( 1):   5 ****
 7 INSERTION SORT: ( 2):   7 ******
 7 INSERTION SORT: ( 3): * 8 *******
 7 INSERTION SORT: ( 4): * 4 ***
 7 INSERTION SORT: ( 5):  10 *********
 7 INSERTION SORT: ( 6):   2 *
 7 INSERTION SORT: ( 7):   9 ********
 7 INSERTION SORT: ( 8):   6 *****

 8 INSERTION SORT: : 3 5 7 4 8 10 2 9 6
 8 INSERTION SORT: ( 0):   3 **
 8 INSERTION SORT: ( 1):   5 ****
 8 INSERTION SORT: ( 2): * 7 ******
 8 INSERTION SORT: ( 3): * 4 ***
 8 INSERTION SORT: ( 4):   8 *******
 8 INSERTION SORT: ( 5):  10 *********
 8 INSERTION SORT: ( 6):   2 *
 8 INSERTION SORT: ( 7):   9 ********
 8 INSERTION SORT: ( 8):   6 *****

 9 INSERTION SORT: : 3 5 4 7 8 10 2 9 6
 9 INSERTION SORT: ( 0):   3 **
 9 INSERTION SORT: ( 1): * 5 ****
 9 INSERTION SORT: ( 2): * 4 ***
 9 INSERTION SORT: ( 3):   7 ******
 9 INSERTION SORT: ( 4):   8 *******
 9 INSERTION SORT: ( 5):  10 *********
 9 INSERTION SORT: ( 6):   2 *
 9 INSERTION SORT: ( 7):   9 ********
 9 INSERTION SORT: ( 8):   6 *****

10 INSERTION SORT: : 3 4 5 7 8 10 2 9 6
10 INSERTION SORT: ( 0):   3 **
10 INSERTION SORT: ( 1):   4 ***
10 INSERTION SORT: ( 2):   5 ****
10 INSERTION SORT: ( 3):   7 ******
10 INSERTION SORT: ( 4):   8 *******
10 INSERTION SORT: ( 5): *10 *********
10 INSERTION SORT: ( 6): * 2 *
10 INSERTION SORT: ( 7):   9 ********
10 INSERTION SORT: ( 8):   6 *****

11 INSERTION SORT: : 3 4 5 7 8 2 10 9 6
11 INSERTION SORT: ( 0):   3 **
11 INSERTION SORT: ( 1):   4 ***
11 INSERTION SORT: ( 2):   5 ****
11 INSERTION SORT: ( 3):   7 ******
11 INSERTION SORT: ( 4): * 8 *******
11 INSERTION SORT: ( 5): * 2 *
11 INSERTION SORT: ( 6):  10 *********
11 INSERTION SORT: ( 7):   9 ********
11 INSERTION SORT: ( 8):   6 *****

12 INSERTION SORT: : 3 4 5 7 2 8 10 9 6
12 INSERTION SORT: ( 0):   3 **
12 INSERTION SORT: ( 1):   4 ***
12 INSERTION SORT: ( 2):   5 ****
12 INSERTION SORT: ( 3): * 7 ******
12 INSERTION SORT: ( 4): * 2 *
12 INSERTION SORT: ( 5):   8 *******
12 INSERTION SORT: ( 6):  10 *********
12 INSERTION SORT: ( 7):   9 ********
12 INSERTION SORT: ( 8):   6 *****

13 INSERTION SORT: : 3 4 5 2 7 8 10 9 6
13 INSERTION SORT: ( 0):   3 **
13 INSERTION SORT: ( 1):   4 ***
13 INSERTION SORT: ( 2): * 5 ****
13 INSERTION SORT: ( 3): * 2 *
13 INSERTION SORT: ( 4):   7 ******
13 INSERTION SORT: ( 5):   8 *******
13 INSERTION SORT: ( 6):  10 *********
13 INSERTION SORT: ( 7):   9 ********
13 INSERTION SORT: ( 8):   6 *****

14 INSERTION SORT: : 3 4 2 5 7 8 10 9 6
14 INSERTION SORT: ( 0):   3 **
14 INSERTION SORT: ( 1): * 4 ***
14 INSERTION SORT: ( 2): * 2 *
14 INSERTION SORT: ( 3):   5 ****
14 INSERTION SORT: ( 4):   7 ******
14 INSERTION SORT: ( 5):   8 *******
14 INSERTION SORT: ( 6):  10 *********
14 INSERTION SORT: ( 7):   9 ********
14 INSERTION SORT: ( 8):   6 *****

15 INSERTION SORT: : 3 2 4 5 7 8 10 9 6
15 INSERTION SORT: ( 0): * 3 **
15 INSERTION SORT: ( 1): * 2 *
15 INSERTION SORT: ( 2):   4 ***
15 INSERTION SORT: ( 3):   5 ****
15 INSERTION SORT: ( 4):   7 ******
15 INSERTION SORT: ( 5):   8 *******
15 INSERTION SORT: ( 6):  10 *********
15 INSERTION SORT: ( 7):   9 ********
15 INSERTION SORT: ( 8):   6 *****

16 INSERTION SORT: : 2 3 4 5 7 8 10 9 6
16 INSERTION SORT: ( 0):   2 *
16 INSERTION SORT: ( 1):   3 **
16 INSERTION SORT: ( 2):   4 ***
16 INSERTION SORT: ( 3):   5 ****
16 INSERTION SORT: ( 4):   7 ******
16 INSERTION SORT: ( 5):   8 *******
16 INSERTION SORT: ( 6): *10 *********
16 INSERTION SORT: ( 7): * 9 ********
16 INSERTION SORT: ( 8):   6 *****

17 INSERTION SORT: : 2 3 4 5 7 8 9 10 6
17 INSERTION SORT: ( 0):   2 *
17 INSERTION SORT: ( 1):   3 **
17 INSERTION SORT: ( 2):   4 ***
17 INSERTION SORT: ( 3):   5 ****
17 INSERTION SORT: ( 4):   7 ******
17 INSERTION SORT: ( 5):   8 *******
17 INSERTION SORT: ( 6):   9 ********
17 INSERTION SORT: ( 7): *10 *********
17 INSERTION SORT: ( 8): * 6 *****

18 INSERTION SORT: : 2 3 4 5 7 8 9 6 10
18 INSERTION SORT: ( 0):   2 *
18 INSERTION SORT: ( 1):   3 **
18 INSERTION SORT: ( 2):   4 ***
18 INSERTION SORT: ( 3):   5 ****
18 INSERTION SORT: ( 4):   7 ******
18 INSERTION SORT: ( 5):   8 *******
18 INSERTION SORT: ( 6): * 9 ********
18 INSERTION SORT: ( 7): * 6 *****
18 INSERTION SORT: ( 8):  10 *********

19 INSERTION SORT: : 2 3 4 5 7 8 6 9 10
19 INSERTION SORT: ( 0):   2 *
19 INSERTION SORT: ( 1):   3 **
19 INSERTION SORT: ( 2):   4 ***
19 INSERTION SORT: ( 3):   5 ****
19 INSERTION SORT: ( 4):   7 ******
19 INSERTION SORT: ( 5): * 8 *******
19 INSERTION SORT: ( 6): * 6 *****
19 INSERTION SORT: ( 7):   9 ********
19 INSERTION SORT: ( 8):  10 *********

20 INSERTION SORT: : 2 3 4 5 7 6 8 9 10
20 INSERTION SORT: ( 0):   2 *
20 INSERTION SORT: ( 1):   3 **
20 INSERTION SORT: ( 2):   4 ***
20 INSERTION SORT: ( 3):   5 ****
20 INSERTION SORT: ( 4): * 7 ******
20 INSERTION SORT: ( 5): * 6 *****
20 INSERTION SORT: ( 6):   8 *******
20 INSERTION SORT: ( 7):   9 ********
20 INSERTION SORT: ( 8):  10 *********

21 INSERTION SORT: : 2 3 4 5 6 7 8 9 10
21 INSERTION SORT: ( 0):   2 *
21 INSERTION SORT: ( 1):   3 **
21 INSERTION SORT: ( 2):   4 ***
21 INSERTION SORT: ( 3):   5 ****
21 INSERTION SORT: ( 4):   6 *****
21 INSERTION SORT: ( 5):   7 ******
21 INSERTION SORT: ( 6):   8 *******
21 INSERTION SORT: ( 7):   9 ********
21 INSERTION SORT: ( 8):  10 *********

```

### [ex2a](#stacks-and-queues)
2a. Run Best Case Example from **Insertion (9:28)**; Array is already sorted    
```
> python -c 'import test_Insertion as T; T.test_wk2_lec_best()'    
```
```
INSERTION BEST SORT: RESULT A E E L M O P R S T X
 0: A E E L M O P R S T X

 0 INSERTION BEST SORT:: A E E L M O P R S T X
 0 INSERTION BEST SORT:( 0):  A  *
 0 INSERTION BEST SORT:( 1):  E  ***
 0 INSERTION BEST SORT:( 2):  E  ***
 0 INSERTION BEST SORT:( 3):  L  ****
 0 INSERTION BEST SORT:( 4):  M  *****
 0 INSERTION BEST SORT:( 5):  O  ******
 0 INSERTION BEST SORT:( 6):  P  *******
 0 INSERTION BEST SORT:( 7):  R  ********
 0 INSERTION BEST SORT:( 8):  S  *********
 0 INSERTION BEST SORT:( 9):  T  **********
 0 INSERTION BEST SORT:(10):  X  ***********

```

### [ex2b](#stacks-and-queues)
2b. Run Worst Case Example from **Insertion (9:28)**; Array is sorted in descending order   
```
python -c 'import test_Insertion as T; T.test_wk2_lec_worst()'
```
```
INSERTION WORST SORT: RESULT A E E L M O P R S T X
 0: X T S R P O M L E E A
    X X . . . . . . . . .
 1: T X S R P O M L E E A
    . X X . . . . . . . .
 2: T S X R P O M L E E A
    X X . . . . . . . . .
 3: S T X R P O M L E E A
    . . X X . . . . . . .
 4: S T R X P O M L E E A
    . X X . . . . . . . .
 5: S R T X P O M L E E A
    X X . . . . . . . . .
 6: R S T X P O M L E E A
    . . . X X . . . . . .
 7: R S T P X O M L E E A
    . . X X . . . . . . .
 8: R S P T X O M L E E A
    . X X . . . . . . . .
 9: R P S T X O M L E E A
    X X . . . . . . . . .
10: P R S T X O M L E E A
    . . . . X X . . . . .
11: P R S T O X M L E E A
    . . . X X . . . . . .
12: P R S O T X M L E E A
    . . X X . . . . . . .
13: P R O S T X M L E E A
    . X X . . . . . . . .
14: P O R S T X M L E E A
    X X . . . . . . . . .
15: O P R S T X M L E E A
    . . . . . X X . . . .
16: O P R S T M X L E E A
    . . . . X X . . . . .
17: O P R S M T X L E E A
    . . . X X . . . . . .
18: O P R M S T X L E E A
    . . X X . . . . . . .
19: O P M R S T X L E E A
    . X X . . . . . . . .
20: O M P R S T X L E E A
    X X . . . . . . . . .
21: M O P R S T X L E E A
    . . . . . . X X . . .
22: M O P R S T L X E E A
    . . . . . X X . . . .
23: M O P R S L T X E E A
    . . . . X X . . . . .
24: M O P R L S T X E E A
    . . . X X . . . . . .
25: M O P L R S T X E E A
    . . X X . . . . . . .
26: M O L P R S T X E E A
    . X X . . . . . . . .
27: M L O P R S T X E E A
    X X . . . . . . . . .
28: L M O P R S T X E E A
    . . . . . . . X X . .
29: L M O P R S T E X E A
    . . . . . . X X . . .
30: L M O P R S E T X E A
    . . . . . X X . . . .
31: L M O P R E S T X E A
    . . . . X X . . . . .
32: L M O P E R S T X E A
    . . . X X . . . . . .
33: L M O E P R S T X E A
    . . X X . . . . . . .
34: L M E O P R S T X E A
    . X X . . . . . . . .
35: L E M O P R S T X E A
    X X . . . . . . . . .
36: E L M O P R S T X E A
    . . . . . . . . X X .
37: E L M O P R S T E X A
    . . . . . . . X X . .
38: E L M O P R S E T X A
    . . . . . . X X . . .
39: E L M O P R E S T X A
    . . . . . X X . . . .
40: E L M O P E R S T X A
    . . . . X X . . . . .
41: E L M O E P R S T X A
    . . . X X . . . . . .
42: E L M E O P R S T X A
    . . X X . . . . . . .
43: E L E M O P R S T X A
    . X X . . . . . . . .
44: E E L M O P R S T X A
    . . . . . . . . . X X
45: E E L M O P R S T A X
    . . . . . . . . X X .
46: E E L M O P R S A T X
    . . . . . . . X X . .
47: E E L M O P R A S T X
    . . . . . . X X . . .
48: E E L M O P A R S T X
    . . . . . X X . . . .
49: E E L M O A P R S T X
    . . . . X X . . . . .
50: E E L M A O P R S T X
    . . . X X . . . . . .
51: E E L A M O P R S T X
    . . X X . . . . . . .
52: E E A L M O P R S T X
    . X X . . . . . . . .
53: E A E L M O P R S T X
    X X . . . . . . . . .
54: A E E L M O P R S T X

 0 INSERTION WORST SORT:: X T S R P O M L E E A
 0 INSERTION WORST SORT:( 0): *X  ***********
 0 INSERTION WORST SORT:( 1): *T  **********
 0 INSERTION WORST SORT:( 2):  S  *********
 0 INSERTION WORST SORT:( 3):  R  ********
 0 INSERTION WORST SORT:( 4):  P  *******
 0 INSERTION WORST SORT:( 5):  O  ******
 0 INSERTION WORST SORT:( 6):  M  *****
 0 INSERTION WORST SORT:( 7):  L  ****
 0 INSERTION WORST SORT:( 8):  E  ***
 0 INSERTION WORST SORT:( 9):  E  ***
 0 INSERTION WORST SORT:(10):  A  *

 1 INSERTION WORST SORT:: T X S R P O M L E E A
 1 INSERTION WORST SORT:( 0):  T  **********
 1 INSERTION WORST SORT:( 1): *X  ***********
 1 INSERTION WORST SORT:( 2): *S  *********
 1 INSERTION WORST SORT:( 3):  R  ********
 1 INSERTION WORST SORT:( 4):  P  *******
 1 INSERTION WORST SORT:( 5):  O  ******
 1 INSERTION WORST SORT:( 6):  M  *****
 1 INSERTION WORST SORT:( 7):  L  ****
 1 INSERTION WORST SORT:( 8):  E  ***
 1 INSERTION WORST SORT:( 9):  E  ***
 1 INSERTION WORST SORT:(10):  A  *

 2 INSERTION WORST SORT:: T S X R P O M L E E A
 2 INSERTION WORST SORT:( 0): *T  **********
 2 INSERTION WORST SORT:( 1): *S  *********
 2 INSERTION WORST SORT:( 2):  X  ***********
 2 INSERTION WORST SORT:( 3):  R  ********
 2 INSERTION WORST SORT:( 4):  P  *******
 2 INSERTION WORST SORT:( 5):  O  ******
 2 INSERTION WORST SORT:( 6):  M  *****
 2 INSERTION WORST SORT:( 7):  L  ****
 2 INSERTION WORST SORT:( 8):  E  ***
 2 INSERTION WORST SORT:( 9):  E  ***
 2 INSERTION WORST SORT:(10):  A  *

 3 INSERTION WORST SORT:: S T X R P O M L E E A
 3 INSERTION WORST SORT:( 0):  S  *********
 3 INSERTION WORST SORT:( 1):  T  **********
 3 INSERTION WORST SORT:( 2): *X  ***********
 3 INSERTION WORST SORT:( 3): *R  ********
 3 INSERTION WORST SORT:( 4):  P  *******
 3 INSERTION WORST SORT:( 5):  O  ******
 3 INSERTION WORST SORT:( 6):  M  *****
 3 INSERTION WORST SORT:( 7):  L  ****
 3 INSERTION WORST SORT:( 8):  E  ***
 3 INSERTION WORST SORT:( 9):  E  ***
 3 INSERTION WORST SORT:(10):  A  *

 4 INSERTION WORST SORT:: S T R X P O M L E E A
 4 INSERTION WORST SORT:( 0):  S  *********
 4 INSERTION WORST SORT:( 1): *T  **********
 4 INSERTION WORST SORT:( 2): *R  ********
 4 INSERTION WORST SORT:( 3):  X  ***********
 4 INSERTION WORST SORT:( 4):  P  *******
 4 INSERTION WORST SORT:( 5):  O  ******
 4 INSERTION WORST SORT:( 6):  M  *****
 4 INSERTION WORST SORT:( 7):  L  ****
 4 INSERTION WORST SORT:( 8):  E  ***
 4 INSERTION WORST SORT:( 9):  E  ***
 4 INSERTION WORST SORT:(10):  A  *

 5 INSERTION WORST SORT:: S R T X P O M L E E A
 5 INSERTION WORST SORT:( 0): *S  *********
 5 INSERTION WORST SORT:( 1): *R  ********
 5 INSERTION WORST SORT:( 2):  T  **********
 5 INSERTION WORST SORT:( 3):  X  ***********
 5 INSERTION WORST SORT:( 4):  P  *******
 5 INSERTION WORST SORT:( 5):  O  ******
 5 INSERTION WORST SORT:( 6):  M  *****
 5 INSERTION WORST SORT:( 7):  L  ****
 5 INSERTION WORST SORT:( 8):  E  ***
 5 INSERTION WORST SORT:( 9):  E  ***
 5 INSERTION WORST SORT:(10):  A  *

 6 INSERTION WORST SORT:: R S T X P O M L E E A
 6 INSERTION WORST SORT:( 0):  R  ********
 6 INSERTION WORST SORT:( 1):  S  *********
 6 INSERTION WORST SORT:( 2):  T  **********
 6 INSERTION WORST SORT:( 3): *X  ***********
 6 INSERTION WORST SORT:( 4): *P  *******
 6 INSERTION WORST SORT:( 5):  O  ******
 6 INSERTION WORST SORT:( 6):  M  *****
 6 INSERTION WORST SORT:( 7):  L  ****
 6 INSERTION WORST SORT:( 8):  E  ***
 6 INSERTION WORST SORT:( 9):  E  ***
 6 INSERTION WORST SORT:(10):  A  *

 7 INSERTION WORST SORT:: R S T P X O M L E E A
 7 INSERTION WORST SORT:( 0):  R  ********
 7 INSERTION WORST SORT:( 1):  S  *********
 7 INSERTION WORST SORT:( 2): *T  **********
 7 INSERTION WORST SORT:( 3): *P  *******
 7 INSERTION WORST SORT:( 4):  X  ***********
 7 INSERTION WORST SORT:( 5):  O  ******
 7 INSERTION WORST SORT:( 6):  M  *****
 7 INSERTION WORST SORT:( 7):  L  ****
 7 INSERTION WORST SORT:( 8):  E  ***
 7 INSERTION WORST SORT:( 9):  E  ***
 7 INSERTION WORST SORT:(10):  A  *

 8 INSERTION WORST SORT:: R S P T X O M L E E A
 8 INSERTION WORST SORT:( 0):  R  ********
 8 INSERTION WORST SORT:( 1): *S  *********
 8 INSERTION WORST SORT:( 2): *P  *******
 8 INSERTION WORST SORT:( 3):  T  **********
 8 INSERTION WORST SORT:( 4):  X  ***********
 8 INSERTION WORST SORT:( 5):  O  ******
 8 INSERTION WORST SORT:( 6):  M  *****
 8 INSERTION WORST SORT:( 7):  L  ****
 8 INSERTION WORST SORT:( 8):  E  ***
 8 INSERTION WORST SORT:( 9):  E  ***
 8 INSERTION WORST SORT:(10):  A  *

 9 INSERTION WORST SORT:: R P S T X O M L E E A
 9 INSERTION WORST SORT:( 0): *R  ********
 9 INSERTION WORST SORT:( 1): *P  *******
 9 INSERTION WORST SORT:( 2):  S  *********
 9 INSERTION WORST SORT:( 3):  T  **********
 9 INSERTION WORST SORT:( 4):  X  ***********
 9 INSERTION WORST SORT:( 5):  O  ******
 9 INSERTION WORST SORT:( 6):  M  *****
 9 INSERTION WORST SORT:( 7):  L  ****
 9 INSERTION WORST SORT:( 8):  E  ***
 9 INSERTION WORST SORT:( 9):  E  ***
 9 INSERTION WORST SORT:(10):  A  *

10 INSERTION WORST SORT:: P R S T X O M L E E A
10 INSERTION WORST SORT:( 0):  P  *******
10 INSERTION WORST SORT:( 1):  R  ********
10 INSERTION WORST SORT:( 2):  S  *********
10 INSERTION WORST SORT:( 3):  T  **********
10 INSERTION WORST SORT:( 4): *X  ***********
10 INSERTION WORST SORT:( 5): *O  ******
10 INSERTION WORST SORT:( 6):  M  *****
10 INSERTION WORST SORT:( 7):  L  ****
10 INSERTION WORST SORT:( 8):  E  ***
10 INSERTION WORST SORT:( 9):  E  ***
10 INSERTION WORST SORT:(10):  A  *

11 INSERTION WORST SORT:: P R S T O X M L E E A
11 INSERTION WORST SORT:( 0):  P  *******
11 INSERTION WORST SORT:( 1):  R  ********
11 INSERTION WORST SORT:( 2):  S  *********
11 INSERTION WORST SORT:( 3): *T  **********
11 INSERTION WORST SORT:( 4): *O  ******
11 INSERTION WORST SORT:( 5):  X  ***********
11 INSERTION WORST SORT:( 6):  M  *****
11 INSERTION WORST SORT:( 7):  L  ****
11 INSERTION WORST SORT:( 8):  E  ***
11 INSERTION WORST SORT:( 9):  E  ***
11 INSERTION WORST SORT:(10):  A  *

12 INSERTION WORST SORT:: P R S O T X M L E E A
12 INSERTION WORST SORT:( 0):  P  *******
12 INSERTION WORST SORT:( 1):  R  ********
12 INSERTION WORST SORT:( 2): *S  *********
12 INSERTION WORST SORT:( 3): *O  ******
12 INSERTION WORST SORT:( 4):  T  **********
12 INSERTION WORST SORT:( 5):  X  ***********
12 INSERTION WORST SORT:( 6):  M  *****
12 INSERTION WORST SORT:( 7):  L  ****
12 INSERTION WORST SORT:( 8):  E  ***
12 INSERTION WORST SORT:( 9):  E  ***
12 INSERTION WORST SORT:(10):  A  *

13 INSERTION WORST SORT:: P R O S T X M L E E A
13 INSERTION WORST SORT:( 0):  P  *******
13 INSERTION WORST SORT:( 1): *R  ********
13 INSERTION WORST SORT:( 2): *O  ******
13 INSERTION WORST SORT:( 3):  S  *********
13 INSERTION WORST SORT:( 4):  T  **********
13 INSERTION WORST SORT:( 5):  X  ***********
13 INSERTION WORST SORT:( 6):  M  *****
13 INSERTION WORST SORT:( 7):  L  ****
13 INSERTION WORST SORT:( 8):  E  ***
13 INSERTION WORST SORT:( 9):  E  ***
13 INSERTION WORST SORT:(10):  A  *

14 INSERTION WORST SORT:: P O R S T X M L E E A
14 INSERTION WORST SORT:( 0): *P  *******
14 INSERTION WORST SORT:( 1): *O  ******
14 INSERTION WORST SORT:( 2):  R  ********
14 INSERTION WORST SORT:( 3):  S  *********
14 INSERTION WORST SORT:( 4):  T  **********
14 INSERTION WORST SORT:( 5):  X  ***********
14 INSERTION WORST SORT:( 6):  M  *****
14 INSERTION WORST SORT:( 7):  L  ****
14 INSERTION WORST SORT:( 8):  E  ***
14 INSERTION WORST SORT:( 9):  E  ***
14 INSERTION WORST SORT:(10):  A  *

15 INSERTION WORST SORT:: O P R S T X M L E E A
15 INSERTION WORST SORT:( 0):  O  ******
15 INSERTION WORST SORT:( 1):  P  *******
15 INSERTION WORST SORT:( 2):  R  ********
15 INSERTION WORST SORT:( 3):  S  *********
15 INSERTION WORST SORT:( 4):  T  **********
15 INSERTION WORST SORT:( 5): *X  ***********
15 INSERTION WORST SORT:( 6): *M  *****
15 INSERTION WORST SORT:( 7):  L  ****
15 INSERTION WORST SORT:( 8):  E  ***
15 INSERTION WORST SORT:( 9):  E  ***
15 INSERTION WORST SORT:(10):  A  *

16 INSERTION WORST SORT:: O P R S T M X L E E A
16 INSERTION WORST SORT:( 0):  O  ******
16 INSERTION WORST SORT:( 1):  P  *******
16 INSERTION WORST SORT:( 2):  R  ********
16 INSERTION WORST SORT:( 3):  S  *********
16 INSERTION WORST SORT:( 4): *T  **********
16 INSERTION WORST SORT:( 5): *M  *****
16 INSERTION WORST SORT:( 6):  X  ***********
16 INSERTION WORST SORT:( 7):  L  ****
16 INSERTION WORST SORT:( 8):  E  ***
16 INSERTION WORST SORT:( 9):  E  ***
16 INSERTION WORST SORT:(10):  A  *

17 INSERTION WORST SORT:: O P R S M T X L E E A
17 INSERTION WORST SORT:( 0):  O  ******
17 INSERTION WORST SORT:( 1):  P  *******
17 INSERTION WORST SORT:( 2):  R  ********
17 INSERTION WORST SORT:( 3): *S  *********
17 INSERTION WORST SORT:( 4): *M  *****
17 INSERTION WORST SORT:( 5):  T  **********
17 INSERTION WORST SORT:( 6):  X  ***********
17 INSERTION WORST SORT:( 7):  L  ****
17 INSERTION WORST SORT:( 8):  E  ***
17 INSERTION WORST SORT:( 9):  E  ***
17 INSERTION WORST SORT:(10):  A  *

18 INSERTION WORST SORT:: O P R M S T X L E E A
18 INSERTION WORST SORT:( 0):  O  ******
18 INSERTION WORST SORT:( 1):  P  *******
18 INSERTION WORST SORT:( 2): *R  ********
18 INSERTION WORST SORT:( 3): *M  *****
18 INSERTION WORST SORT:( 4):  S  *********
18 INSERTION WORST SORT:( 5):  T  **********
18 INSERTION WORST SORT:( 6):  X  ***********
18 INSERTION WORST SORT:( 7):  L  ****
18 INSERTION WORST SORT:( 8):  E  ***
18 INSERTION WORST SORT:( 9):  E  ***
18 INSERTION WORST SORT:(10):  A  *

19 INSERTION WORST SORT:: O P M R S T X L E E A
19 INSERTION WORST SORT:( 0):  O  ******
19 INSERTION WORST SORT:( 1): *P  *******
19 INSERTION WORST SORT:( 2): *M  *****
19 INSERTION WORST SORT:( 3):  R  ********
19 INSERTION WORST SORT:( 4):  S  *********
19 INSERTION WORST SORT:( 5):  T  **********
19 INSERTION WORST SORT:( 6):  X  ***********
19 INSERTION WORST SORT:( 7):  L  ****
19 INSERTION WORST SORT:( 8):  E  ***
19 INSERTION WORST SORT:( 9):  E  ***
19 INSERTION WORST SORT:(10):  A  *

20 INSERTION WORST SORT:: O M P R S T X L E E A
20 INSERTION WORST SORT:( 0): *O  ******
20 INSERTION WORST SORT:( 1): *M  *****
20 INSERTION WORST SORT:( 2):  P  *******
20 INSERTION WORST SORT:( 3):  R  ********
20 INSERTION WORST SORT:( 4):  S  *********
20 INSERTION WORST SORT:( 5):  T  **********
20 INSERTION WORST SORT:( 6):  X  ***********
20 INSERTION WORST SORT:( 7):  L  ****
20 INSERTION WORST SORT:( 8):  E  ***
20 INSERTION WORST SORT:( 9):  E  ***
20 INSERTION WORST SORT:(10):  A  *

21 INSERTION WORST SORT:: M O P R S T X L E E A
21 INSERTION WORST SORT:( 0):  M  *****
21 INSERTION WORST SORT:( 1):  O  ******
21 INSERTION WORST SORT:( 2):  P  *******
21 INSERTION WORST SORT:( 3):  R  ********
21 INSERTION WORST SORT:( 4):  S  *********
21 INSERTION WORST SORT:( 5):  T  **********
21 INSERTION WORST SORT:( 6): *X  ***********
21 INSERTION WORST SORT:( 7): *L  ****
21 INSERTION WORST SORT:( 8):  E  ***
21 INSERTION WORST SORT:( 9):  E  ***
21 INSERTION WORST SORT:(10):  A  *

22 INSERTION WORST SORT:: M O P R S T L X E E A
22 INSERTION WORST SORT:( 0):  M  *****
22 INSERTION WORST SORT:( 1):  O  ******
22 INSERTION WORST SORT:( 2):  P  *******
22 INSERTION WORST SORT:( 3):  R  ********
22 INSERTION WORST SORT:( 4):  S  *********
22 INSERTION WORST SORT:( 5): *T  **********
22 INSERTION WORST SORT:( 6): *L  ****
22 INSERTION WORST SORT:( 7):  X  ***********
22 INSERTION WORST SORT:( 8):  E  ***
22 INSERTION WORST SORT:( 9):  E  ***
22 INSERTION WORST SORT:(10):  A  *

23 INSERTION WORST SORT:: M O P R S L T X E E A
23 INSERTION WORST SORT:( 0):  M  *****
23 INSERTION WORST SORT:( 1):  O  ******
23 INSERTION WORST SORT:( 2):  P  *******
23 INSERTION WORST SORT:( 3):  R  ********
23 INSERTION WORST SORT:( 4): *S  *********
23 INSERTION WORST SORT:( 5): *L  ****
23 INSERTION WORST SORT:( 6):  T  **********
23 INSERTION WORST SORT:( 7):  X  ***********
23 INSERTION WORST SORT:( 8):  E  ***
23 INSERTION WORST SORT:( 9):  E  ***
23 INSERTION WORST SORT:(10):  A  *

24 INSERTION WORST SORT:: M O P R L S T X E E A
24 INSERTION WORST SORT:( 0):  M  *****
24 INSERTION WORST SORT:( 1):  O  ******
24 INSERTION WORST SORT:( 2):  P  *******
24 INSERTION WORST SORT:( 3): *R  ********
24 INSERTION WORST SORT:( 4): *L  ****
24 INSERTION WORST SORT:( 5):  S  *********
24 INSERTION WORST SORT:( 6):  T  **********
24 INSERTION WORST SORT:( 7):  X  ***********
24 INSERTION WORST SORT:( 8):  E  ***
24 INSERTION WORST SORT:( 9):  E  ***
24 INSERTION WORST SORT:(10):  A  *

25 INSERTION WORST SORT:: M O P L R S T X E E A
25 INSERTION WORST SORT:( 0):  M  *****
25 INSERTION WORST SORT:( 1):  O  ******
25 INSERTION WORST SORT:( 2): *P  *******
25 INSERTION WORST SORT:( 3): *L  ****
25 INSERTION WORST SORT:( 4):  R  ********
25 INSERTION WORST SORT:( 5):  S  *********
25 INSERTION WORST SORT:( 6):  T  **********
25 INSERTION WORST SORT:( 7):  X  ***********
25 INSERTION WORST SORT:( 8):  E  ***
25 INSERTION WORST SORT:( 9):  E  ***
25 INSERTION WORST SORT:(10):  A  *

26 INSERTION WORST SORT:: M O L P R S T X E E A
26 INSERTION WORST SORT:( 0):  M  *****
26 INSERTION WORST SORT:( 1): *O  ******
26 INSERTION WORST SORT:( 2): *L  ****
26 INSERTION WORST SORT:( 3):  P  *******
26 INSERTION WORST SORT:( 4):  R  ********
26 INSERTION WORST SORT:( 5):  S  *********
26 INSERTION WORST SORT:( 6):  T  **********
26 INSERTION WORST SORT:( 7):  X  ***********
26 INSERTION WORST SORT:( 8):  E  ***
26 INSERTION WORST SORT:( 9):  E  ***
26 INSERTION WORST SORT:(10):  A  *

27 INSERTION WORST SORT:: M L O P R S T X E E A
27 INSERTION WORST SORT:( 0): *M  *****
27 INSERTION WORST SORT:( 1): *L  ****
27 INSERTION WORST SORT:( 2):  O  ******
27 INSERTION WORST SORT:( 3):  P  *******
27 INSERTION WORST SORT:( 4):  R  ********
27 INSERTION WORST SORT:( 5):  S  *********
27 INSERTION WORST SORT:( 6):  T  **********
27 INSERTION WORST SORT:( 7):  X  ***********
27 INSERTION WORST SORT:( 8):  E  ***
27 INSERTION WORST SORT:( 9):  E  ***
27 INSERTION WORST SORT:(10):  A  *

28 INSERTION WORST SORT:: L M O P R S T X E E A
28 INSERTION WORST SORT:( 0):  L  ****
28 INSERTION WORST SORT:( 1):  M  *****
28 INSERTION WORST SORT:( 2):  O  ******
28 INSERTION WORST SORT:( 3):  P  *******
28 INSERTION WORST SORT:( 4):  R  ********
28 INSERTION WORST SORT:( 5):  S  *********
28 INSERTION WORST SORT:( 6):  T  **********
28 INSERTION WORST SORT:( 7): *X  ***********
28 INSERTION WORST SORT:( 8): *E  ***
28 INSERTION WORST SORT:( 9):  E  ***
28 INSERTION WORST SORT:(10):  A  *

29 INSERTION WORST SORT:: L M O P R S T E X E A
29 INSERTION WORST SORT:( 0):  L  ****
29 INSERTION WORST SORT:( 1):  M  *****
29 INSERTION WORST SORT:( 2):  O  ******
29 INSERTION WORST SORT:( 3):  P  *******
29 INSERTION WORST SORT:( 4):  R  ********
29 INSERTION WORST SORT:( 5):  S  *********
29 INSERTION WORST SORT:( 6): *T  **********
29 INSERTION WORST SORT:( 7): *E  ***
29 INSERTION WORST SORT:( 8):  X  ***********
29 INSERTION WORST SORT:( 9):  E  ***
29 INSERTION WORST SORT:(10):  A  *

30 INSERTION WORST SORT:: L M O P R S E T X E A
30 INSERTION WORST SORT:( 0):  L  ****
30 INSERTION WORST SORT:( 1):  M  *****
30 INSERTION WORST SORT:( 2):  O  ******
30 INSERTION WORST SORT:( 3):  P  *******
30 INSERTION WORST SORT:( 4):  R  ********
30 INSERTION WORST SORT:( 5): *S  *********
30 INSERTION WORST SORT:( 6): *E  ***
30 INSERTION WORST SORT:( 7):  T  **********
30 INSERTION WORST SORT:( 8):  X  ***********
30 INSERTION WORST SORT:( 9):  E  ***
30 INSERTION WORST SORT:(10):  A  *

31 INSERTION WORST SORT:: L M O P R E S T X E A
31 INSERTION WORST SORT:( 0):  L  ****
31 INSERTION WORST SORT:( 1):  M  *****
31 INSERTION WORST SORT:( 2):  O  ******
31 INSERTION WORST SORT:( 3):  P  *******
31 INSERTION WORST SORT:( 4): *R  ********
31 INSERTION WORST SORT:( 5): *E  ***
31 INSERTION WORST SORT:( 6):  S  *********
31 INSERTION WORST SORT:( 7):  T  **********
31 INSERTION WORST SORT:( 8):  X  ***********
31 INSERTION WORST SORT:( 9):  E  ***
31 INSERTION WORST SORT:(10):  A  *

32 INSERTION WORST SORT:: L M O P E R S T X E A
32 INSERTION WORST SORT:( 0):  L  ****
32 INSERTION WORST SORT:( 1):  M  *****
32 INSERTION WORST SORT:( 2):  O  ******
32 INSERTION WORST SORT:( 3): *P  *******
32 INSERTION WORST SORT:( 4): *E  ***
32 INSERTION WORST SORT:( 5):  R  ********
32 INSERTION WORST SORT:( 6):  S  *********
32 INSERTION WORST SORT:( 7):  T  **********
32 INSERTION WORST SORT:( 8):  X  ***********
32 INSERTION WORST SORT:( 9):  E  ***
32 INSERTION WORST SORT:(10):  A  *

33 INSERTION WORST SORT:: L M O E P R S T X E A
33 INSERTION WORST SORT:( 0):  L  ****
33 INSERTION WORST SORT:( 1):  M  *****
33 INSERTION WORST SORT:( 2): *O  ******
33 INSERTION WORST SORT:( 3): *E  ***
33 INSERTION WORST SORT:( 4):  P  *******
33 INSERTION WORST SORT:( 5):  R  ********
33 INSERTION WORST SORT:( 6):  S  *********
33 INSERTION WORST SORT:( 7):  T  **********
33 INSERTION WORST SORT:( 8):  X  ***********
33 INSERTION WORST SORT:( 9):  E  ***
33 INSERTION WORST SORT:(10):  A  *

34 INSERTION WORST SORT:: L M E O P R S T X E A
34 INSERTION WORST SORT:( 0):  L  ****
34 INSERTION WORST SORT:( 1): *M  *****
34 INSERTION WORST SORT:( 2): *E  ***
34 INSERTION WORST SORT:( 3):  O  ******
34 INSERTION WORST SORT:( 4):  P  *******
34 INSERTION WORST SORT:( 5):  R  ********
34 INSERTION WORST SORT:( 6):  S  *********
34 INSERTION WORST SORT:( 7):  T  **********
34 INSERTION WORST SORT:( 8):  X  ***********
34 INSERTION WORST SORT:( 9):  E  ***
34 INSERTION WORST SORT:(10):  A  *

35 INSERTION WORST SORT:: L E M O P R S T X E A
35 INSERTION WORST SORT:( 0): *L  ****
35 INSERTION WORST SORT:( 1): *E  ***
35 INSERTION WORST SORT:( 2):  M  *****
35 INSERTION WORST SORT:( 3):  O  ******
35 INSERTION WORST SORT:( 4):  P  *******
35 INSERTION WORST SORT:( 5):  R  ********
35 INSERTION WORST SORT:( 6):  S  *********
35 INSERTION WORST SORT:( 7):  T  **********
35 INSERTION WORST SORT:( 8):  X  ***********
35 INSERTION WORST SORT:( 9):  E  ***
35 INSERTION WORST SORT:(10):  A  *

36 INSERTION WORST SORT:: E L M O P R S T X E A
36 INSERTION WORST SORT:( 0):  E  ***
36 INSERTION WORST SORT:( 1):  L  ****
36 INSERTION WORST SORT:( 2):  M  *****
36 INSERTION WORST SORT:( 3):  O  ******
36 INSERTION WORST SORT:( 4):  P  *******
36 INSERTION WORST SORT:( 5):  R  ********
36 INSERTION WORST SORT:( 6):  S  *********
36 INSERTION WORST SORT:( 7):  T  **********
36 INSERTION WORST SORT:( 8): *X  ***********
36 INSERTION WORST SORT:( 9): *E  ***
36 INSERTION WORST SORT:(10):  A  *

37 INSERTION WORST SORT:: E L M O P R S T E X A
37 INSERTION WORST SORT:( 0):  E  ***
37 INSERTION WORST SORT:( 1):  L  ****
37 INSERTION WORST SORT:( 2):  M  *****
37 INSERTION WORST SORT:( 3):  O  ******
37 INSERTION WORST SORT:( 4):  P  *******
37 INSERTION WORST SORT:( 5):  R  ********
37 INSERTION WORST SORT:( 6):  S  *********
37 INSERTION WORST SORT:( 7): *T  **********
37 INSERTION WORST SORT:( 8): *E  ***
37 INSERTION WORST SORT:( 9):  X  ***********
37 INSERTION WORST SORT:(10):  A  *

38 INSERTION WORST SORT:: E L M O P R S E T X A
38 INSERTION WORST SORT:( 0):  E  ***
38 INSERTION WORST SORT:( 1):  L  ****
38 INSERTION WORST SORT:( 2):  M  *****
38 INSERTION WORST SORT:( 3):  O  ******
38 INSERTION WORST SORT:( 4):  P  *******
38 INSERTION WORST SORT:( 5):  R  ********
38 INSERTION WORST SORT:( 6): *S  *********
38 INSERTION WORST SORT:( 7): *E  ***
38 INSERTION WORST SORT:( 8):  T  **********
38 INSERTION WORST SORT:( 9):  X  ***********
38 INSERTION WORST SORT:(10):  A  *

39 INSERTION WORST SORT:: E L M O P R E S T X A
39 INSERTION WORST SORT:( 0):  E  ***
39 INSERTION WORST SORT:( 1):  L  ****
39 INSERTION WORST SORT:( 2):  M  *****
39 INSERTION WORST SORT:( 3):  O  ******
39 INSERTION WORST SORT:( 4):  P  *******
39 INSERTION WORST SORT:( 5): *R  ********
39 INSERTION WORST SORT:( 6): *E  ***
39 INSERTION WORST SORT:( 7):  S  *********
39 INSERTION WORST SORT:( 8):  T  **********
39 INSERTION WORST SORT:( 9):  X  ***********
39 INSERTION WORST SORT:(10):  A  *

40 INSERTION WORST SORT:: E L M O P E R S T X A
40 INSERTION WORST SORT:( 0):  E  ***
40 INSERTION WORST SORT:( 1):  L  ****
40 INSERTION WORST SORT:( 2):  M  *****
40 INSERTION WORST SORT:( 3):  O  ******
40 INSERTION WORST SORT:( 4): *P  *******
40 INSERTION WORST SORT:( 5): *E  ***
40 INSERTION WORST SORT:( 6):  R  ********
40 INSERTION WORST SORT:( 7):  S  *********
40 INSERTION WORST SORT:( 8):  T  **********
40 INSERTION WORST SORT:( 9):  X  ***********
40 INSERTION WORST SORT:(10):  A  *

41 INSERTION WORST SORT:: E L M O E P R S T X A
41 INSERTION WORST SORT:( 0):  E  ***
41 INSERTION WORST SORT:( 1):  L  ****
41 INSERTION WORST SORT:( 2):  M  *****
41 INSERTION WORST SORT:( 3): *O  ******
41 INSERTION WORST SORT:( 4): *E  ***
41 INSERTION WORST SORT:( 5):  P  *******
41 INSERTION WORST SORT:( 6):  R  ********
41 INSERTION WORST SORT:( 7):  S  *********
41 INSERTION WORST SORT:( 8):  T  **********
41 INSERTION WORST SORT:( 9):  X  ***********
41 INSERTION WORST SORT:(10):  A  *

42 INSERTION WORST SORT:: E L M E O P R S T X A
42 INSERTION WORST SORT:( 0):  E  ***
42 INSERTION WORST SORT:( 1):  L  ****
42 INSERTION WORST SORT:( 2): *M  *****
42 INSERTION WORST SORT:( 3): *E  ***
42 INSERTION WORST SORT:( 4):  O  ******
42 INSERTION WORST SORT:( 5):  P  *******
42 INSERTION WORST SORT:( 6):  R  ********
42 INSERTION WORST SORT:( 7):  S  *********
42 INSERTION WORST SORT:( 8):  T  **********
42 INSERTION WORST SORT:( 9):  X  ***********
42 INSERTION WORST SORT:(10):  A  *

43 INSERTION WORST SORT:: E L E M O P R S T X A
43 INSERTION WORST SORT:( 0):  E  ***
43 INSERTION WORST SORT:( 1): *L  ****
43 INSERTION WORST SORT:( 2): *E  ***
43 INSERTION WORST SORT:( 3):  M  *****
43 INSERTION WORST SORT:( 4):  O  ******
43 INSERTION WORST SORT:( 5):  P  *******
43 INSERTION WORST SORT:( 6):  R  ********
43 INSERTION WORST SORT:( 7):  S  *********
43 INSERTION WORST SORT:( 8):  T  **********
43 INSERTION WORST SORT:( 9):  X  ***********
43 INSERTION WORST SORT:(10):  A  *

44 INSERTION WORST SORT:: E E L M O P R S T X A
44 INSERTION WORST SORT:( 0):  E  ***
44 INSERTION WORST SORT:( 1):  E  ***
44 INSERTION WORST SORT:( 2):  L  ****
44 INSERTION WORST SORT:( 3):  M  *****
44 INSERTION WORST SORT:( 4):  O  ******
44 INSERTION WORST SORT:( 5):  P  *******
44 INSERTION WORST SORT:( 6):  R  ********
44 INSERTION WORST SORT:( 7):  S  *********
44 INSERTION WORST SORT:( 8):  T  **********
44 INSERTION WORST SORT:( 9): *X  ***********
44 INSERTION WORST SORT:(10): *A  *

45 INSERTION WORST SORT:: E E L M O P R S T A X
45 INSERTION WORST SORT:( 0):  E  ***
45 INSERTION WORST SORT:( 1):  E  ***
45 INSERTION WORST SORT:( 2):  L  ****
45 INSERTION WORST SORT:( 3):  M  *****
45 INSERTION WORST SORT:( 4):  O  ******
45 INSERTION WORST SORT:( 5):  P  *******
45 INSERTION WORST SORT:( 6):  R  ********
45 INSERTION WORST SORT:( 7):  S  *********
45 INSERTION WORST SORT:( 8): *T  **********
45 INSERTION WORST SORT:( 9): *A  *
45 INSERTION WORST SORT:(10):  X  ***********

46 INSERTION WORST SORT:: E E L M O P R S A T X
46 INSERTION WORST SORT:( 0):  E  ***
46 INSERTION WORST SORT:( 1):  E  ***
46 INSERTION WORST SORT:( 2):  L  ****
46 INSERTION WORST SORT:( 3):  M  *****
46 INSERTION WORST SORT:( 4):  O  ******
46 INSERTION WORST SORT:( 5):  P  *******
46 INSERTION WORST SORT:( 6):  R  ********
46 INSERTION WORST SORT:( 7): *S  *********
46 INSERTION WORST SORT:( 8): *A  *
46 INSERTION WORST SORT:( 9):  T  **********
46 INSERTION WORST SORT:(10):  X  ***********

47 INSERTION WORST SORT:: E E L M O P R A S T X
47 INSERTION WORST SORT:( 0):  E  ***
47 INSERTION WORST SORT:( 1):  E  ***
47 INSERTION WORST SORT:( 2):  L  ****
47 INSERTION WORST SORT:( 3):  M  *****
47 INSERTION WORST SORT:( 4):  O  ******
47 INSERTION WORST SORT:( 5):  P  *******
47 INSERTION WORST SORT:( 6): *R  ********
47 INSERTION WORST SORT:( 7): *A  *
47 INSERTION WORST SORT:( 8):  S  *********
47 INSERTION WORST SORT:( 9):  T  **********
47 INSERTION WORST SORT:(10):  X  ***********

48 INSERTION WORST SORT:: E E L M O P A R S T X
48 INSERTION WORST SORT:( 0):  E  ***
48 INSERTION WORST SORT:( 1):  E  ***
48 INSERTION WORST SORT:( 2):  L  ****
48 INSERTION WORST SORT:( 3):  M  *****
48 INSERTION WORST SORT:( 4):  O  ******
48 INSERTION WORST SORT:( 5): *P  *******
48 INSERTION WORST SORT:( 6): *A  *
48 INSERTION WORST SORT:( 7):  R  ********
48 INSERTION WORST SORT:( 8):  S  *********
48 INSERTION WORST SORT:( 9):  T  **********
48 INSERTION WORST SORT:(10):  X  ***********

49 INSERTION WORST SORT:: E E L M O A P R S T X
49 INSERTION WORST SORT:( 0):  E  ***
49 INSERTION WORST SORT:( 1):  E  ***
49 INSERTION WORST SORT:( 2):  L  ****
49 INSERTION WORST SORT:( 3):  M  *****
49 INSERTION WORST SORT:( 4): *O  ******
49 INSERTION WORST SORT:( 5): *A  *
49 INSERTION WORST SORT:( 6):  P  *******
49 INSERTION WORST SORT:( 7):  R  ********
49 INSERTION WORST SORT:( 8):  S  *********
49 INSERTION WORST SORT:( 9):  T  **********
49 INSERTION WORST SORT:(10):  X  ***********

50 INSERTION WORST SORT:: E E L M A O P R S T X
50 INSERTION WORST SORT:( 0):  E  ***
50 INSERTION WORST SORT:( 1):  E  ***
50 INSERTION WORST SORT:( 2):  L  ****
50 INSERTION WORST SORT:( 3): *M  *****
50 INSERTION WORST SORT:( 4): *A  *
50 INSERTION WORST SORT:( 5):  O  ******
50 INSERTION WORST SORT:( 6):  P  *******
50 INSERTION WORST SORT:( 7):  R  ********
50 INSERTION WORST SORT:( 8):  S  *********
50 INSERTION WORST SORT:( 9):  T  **********
50 INSERTION WORST SORT:(10):  X  ***********

51 INSERTION WORST SORT:: E E L A M O P R S T X
51 INSERTION WORST SORT:( 0):  E  ***
51 INSERTION WORST SORT:( 1):  E  ***
51 INSERTION WORST SORT:( 2): *L  ****
51 INSERTION WORST SORT:( 3): *A  *
51 INSERTION WORST SORT:( 4):  M  *****
51 INSERTION WORST SORT:( 5):  O  ******
51 INSERTION WORST SORT:( 6):  P  *******
51 INSERTION WORST SORT:( 7):  R  ********
51 INSERTION WORST SORT:( 8):  S  *********
51 INSERTION WORST SORT:( 9):  T  **********
51 INSERTION WORST SORT:(10):  X  ***********

52 INSERTION WORST SORT:: E E A L M O P R S T X
52 INSERTION WORST SORT:( 0):  E  ***
52 INSERTION WORST SORT:( 1): *E  ***
52 INSERTION WORST SORT:( 2): *A  *
52 INSERTION WORST SORT:( 3):  L  ****
52 INSERTION WORST SORT:( 4):  M  *****
52 INSERTION WORST SORT:( 5):  O  ******
52 INSERTION WORST SORT:( 6):  P  *******
52 INSERTION WORST SORT:( 7):  R  ********
52 INSERTION WORST SORT:( 8):  S  *********
52 INSERTION WORST SORT:( 9):  T  **********
52 INSERTION WORST SORT:(10):  X  ***********

53 INSERTION WORST SORT:: E A E L M O P R S T X
53 INSERTION WORST SORT:( 0): *E  ***
53 INSERTION WORST SORT:( 1): *A  *
53 INSERTION WORST SORT:( 2):  E  ***
53 INSERTION WORST SORT:( 3):  L  ****
53 INSERTION WORST SORT:( 4):  M  *****
53 INSERTION WORST SORT:( 5):  O  ******
53 INSERTION WORST SORT:( 6):  P  *******
53 INSERTION WORST SORT:( 7):  R  ********
53 INSERTION WORST SORT:( 8):  S  *********
53 INSERTION WORST SORT:( 9):  T  **********
53 INSERTION WORST SORT:(10):  X  ***********

54 INSERTION WORST SORT:: A E E L M O P R S T X
54 INSERTION WORST SORT:( 0):  A  *
54 INSERTION WORST SORT:( 1):  E  ***
54 INSERTION WORST SORT:( 2):  E  ***
54 INSERTION WORST SORT:( 3):  L  ****
54 INSERTION WORST SORT:( 4):  M  *****
54 INSERTION WORST SORT:( 5):  O  ******
54 INSERTION WORST SORT:( 6):  P  *******
54 INSERTION WORST SORT:( 7):  R  ********
54 INSERTION WORST SORT:( 8):  S  *********
54 INSERTION WORST SORT:( 9):  T  **********
54 INSERTION WORST SORT:(10):  X  ***********

```

### [ex2c](#stacks-and-queues)
2c. Run Paritally-sorted Example from **Insertion (9:28)**
    Array has inversions: a pair of keys out order
```
> python -c 'import test_Insertion as T; T.test_wk2_lec_partial()'
```
```
INSERTION PARTIAL SORT: RESULT A E E L M O P R S T X
 0: A E E L M O T R X P S
    . . . . . . X X . . .
 1: A E E L M O R T X P S
    . . . . . . . . X X .
 2: A E E L M O R T P X S
    . . . . . . . X X . .
 3: A E E L M O R P T X S
    . . . . . . X X . . .
 4: A E E L M O P R T X S
    . . . . . . . . . X X
 5: A E E L M O P R T S X
    . . . . . . . . X X .
 6: A E E L M O P R S T X

 0 INSERTION PARTIAL SORT:: A E E L M O T R X P S
 0 INSERTION PARTIAL SORT:( 0):  A  *
 0 INSERTION PARTIAL SORT:( 1):  E  ***
 0 INSERTION PARTIAL SORT:( 2):  E  ***
 0 INSERTION PARTIAL SORT:( 3):  L  ****
 0 INSERTION PARTIAL SORT:( 4):  M  *****
 0 INSERTION PARTIAL SORT:( 5):  O  ******
 0 INSERTION PARTIAL SORT:( 6): *T  **********
 0 INSERTION PARTIAL SORT:( 7): *R  ********
 0 INSERTION PARTIAL SORT:( 8):  X  ***********
 0 INSERTION PARTIAL SORT:( 9):  P  *******
 0 INSERTION PARTIAL SORT:(10):  S  *********

 1 INSERTION PARTIAL SORT:: A E E L M O R T X P S
 1 INSERTION PARTIAL SORT:( 0):  A  *
 1 INSERTION PARTIAL SORT:( 1):  E  ***
 1 INSERTION PARTIAL SORT:( 2):  E  ***
 1 INSERTION PARTIAL SORT:( 3):  L  ****
 1 INSERTION PARTIAL SORT:( 4):  M  *****
 1 INSERTION PARTIAL SORT:( 5):  O  ******
 1 INSERTION PARTIAL SORT:( 6):  R  ********
 1 INSERTION PARTIAL SORT:( 7):  T  **********
 1 INSERTION PARTIAL SORT:( 8): *X  ***********
 1 INSERTION PARTIAL SORT:( 9): *P  *******
 1 INSERTION PARTIAL SORT:(10):  S  *********

 2 INSERTION PARTIAL SORT:: A E E L M O R T P X S
 2 INSERTION PARTIAL SORT:( 0):  A  *
 2 INSERTION PARTIAL SORT:( 1):  E  ***
 2 INSERTION PARTIAL SORT:( 2):  E  ***
 2 INSERTION PARTIAL SORT:( 3):  L  ****
 2 INSERTION PARTIAL SORT:( 4):  M  *****
 2 INSERTION PARTIAL SORT:( 5):  O  ******
 2 INSERTION PARTIAL SORT:( 6):  R  ********
 2 INSERTION PARTIAL SORT:( 7): *T  **********
 2 INSERTION PARTIAL SORT:( 8): *P  *******
 2 INSERTION PARTIAL SORT:( 9):  X  ***********
 2 INSERTION PARTIAL SORT:(10):  S  *********

 3 INSERTION PARTIAL SORT:: A E E L M O R P T X S
 3 INSERTION PARTIAL SORT:( 0):  A  *
 3 INSERTION PARTIAL SORT:( 1):  E  ***
 3 INSERTION PARTIAL SORT:( 2):  E  ***
 3 INSERTION PARTIAL SORT:( 3):  L  ****
 3 INSERTION PARTIAL SORT:( 4):  M  *****
 3 INSERTION PARTIAL SORT:( 5):  O  ******
 3 INSERTION PARTIAL SORT:( 6): *R  ********
 3 INSERTION PARTIAL SORT:( 7): *P  *******
 3 INSERTION PARTIAL SORT:( 8):  T  **********
 3 INSERTION PARTIAL SORT:( 9):  X  ***********
 3 INSERTION PARTIAL SORT:(10):  S  *********

 4 INSERTION PARTIAL SORT:: A E E L M O P R T X S
 4 INSERTION PARTIAL SORT:( 0):  A  *
 4 INSERTION PARTIAL SORT:( 1):  E  ***
 4 INSERTION PARTIAL SORT:( 2):  E  ***
 4 INSERTION PARTIAL SORT:( 3):  L  ****
 4 INSERTION PARTIAL SORT:( 4):  M  *****
 4 INSERTION PARTIAL SORT:( 5):  O  ******
 4 INSERTION PARTIAL SORT:( 6):  P  *******
 4 INSERTION PARTIAL SORT:( 7):  R  ********
 4 INSERTION PARTIAL SORT:( 8):  T  **********
 4 INSERTION PARTIAL SORT:( 9): *X  ***********
 4 INSERTION PARTIAL SORT:(10): *S  *********

 5 INSERTION PARTIAL SORT:: A E E L M O P R T S X
 5 INSERTION PARTIAL SORT:( 0):  A  *
 5 INSERTION PARTIAL SORT:( 1):  E  ***
 5 INSERTION PARTIAL SORT:( 2):  E  ***
 5 INSERTION PARTIAL SORT:( 3):  L  ****
 5 INSERTION PARTIAL SORT:( 4):  M  *****
 5 INSERTION PARTIAL SORT:( 5):  O  ******
 5 INSERTION PARTIAL SORT:( 6):  P  *******
 5 INSERTION PARTIAL SORT:( 7):  R  ********
 5 INSERTION PARTIAL SORT:( 8): *T  **********
 5 INSERTION PARTIAL SORT:( 9): *S  *********
 5 INSERTION PARTIAL SORT:(10):  X  ***********

 6 INSERTION PARTIAL SORT:: A E E L M O P R S T X
 6 INSERTION PARTIAL SORT:( 0):  A  *
 6 INSERTION PARTIAL SORT:( 1):  E  ***
 6 INSERTION PARTIAL SORT:( 2):  E  ***
 6 INSERTION PARTIAL SORT:( 3):  L  ****
 6 INSERTION PARTIAL SORT:( 4):  M  *****
 6 INSERTION PARTIAL SORT:( 5):  O  ******
 6 INSERTION PARTIAL SORT:( 6):  P  *******
 6 INSERTION PARTIAL SORT:( 7):  R  ********
 6 INSERTION PARTIAL SORT:( 8):  S  *********
 6 INSERTION PARTIAL SORT:( 9):  T  **********
 6 INSERTION PARTIAL SORT:(10):  X  ***********

```

### [ex3](#stacks-and-queues)
3. Run Lecture Example from **Shellsort (10:48)**
```
> python -c 'import test_Shell as T; T.test_wk2_lec()'
```
```
SHELL SORT LEC EX RESULT: A E E L M O P R S T X

 0: M O L E E X A S P R T
    X . . . X . . . . . .
 1: E O L E M X A S P R T
    . . X . . . X . . . .
 2: E O A E M X L S P R T
    . . . . . X . . . X .
 3: E O A E M R L S P X T
    . X X . . . . . . . .
 4: E A O E M R L S P X T
    X X . . . . . . . . .
 5: A E O E M R L S P X T
    . . X X . . . . . . .
 6: A E E O M R L S P X T
    . . . X X . . . . . .
 7: A E E M O R L S P X T
    . . . . . X X . . . .
 8: A E E M O L R S P X T
    . . . . X X . . . . .
 9: A E E M L O R S P X T
    . . . X X . . . . . .
10: A E E L M O R S P X T
    . . . . . . . X X . .
11: A E E L M O R P S X T
    . . . . . . X X . . .
12: A E E L M O P R S X T
    . . . . . . . . . X X
13: A E E L M O P R S T X

 0 SHELL SORT LEC EX: M O L E E X A S P R T
 0 SHELL SORT LEC EX( 0): *M  *****
 0 SHELL SORT LEC EX( 1):  O  ******
 0 SHELL SORT LEC EX( 2):  L  ****
 0 SHELL SORT LEC EX( 3):  E  ***
 0 SHELL SORT LEC EX( 4): *E  ***
 0 SHELL SORT LEC EX( 5):  X  ***********
 0 SHELL SORT LEC EX( 6):  A  *
 0 SHELL SORT LEC EX( 7):  S  *********
 0 SHELL SORT LEC EX( 8):  P  *******
 0 SHELL SORT LEC EX( 9):  R  ********
 0 SHELL SORT LEC EX(10):  T  **********

 1 SHELL SORT LEC EX: E O L E M X A S P R T
 1 SHELL SORT LEC EX( 0):  E  ***
 1 SHELL SORT LEC EX( 1):  O  ******
 1 SHELL SORT LEC EX( 2): *L  ****
 1 SHELL SORT LEC EX( 3):  E  ***
 1 SHELL SORT LEC EX( 4):  M  *****
 1 SHELL SORT LEC EX( 5):  X  ***********
 1 SHELL SORT LEC EX( 6): *A  *
 1 SHELL SORT LEC EX( 7):  S  *********
 1 SHELL SORT LEC EX( 8):  P  *******
 1 SHELL SORT LEC EX( 9):  R  ********
 1 SHELL SORT LEC EX(10):  T  **********

 2 SHELL SORT LEC EX: E O A E M X L S P R T
 2 SHELL SORT LEC EX( 0):  E  ***
 2 SHELL SORT LEC EX( 1):  O  ******
 2 SHELL SORT LEC EX( 2):  A  *
 2 SHELL SORT LEC EX( 3):  E  ***
 2 SHELL SORT LEC EX( 4):  M  *****
 2 SHELL SORT LEC EX( 5): *X  ***********
 2 SHELL SORT LEC EX( 6):  L  ****
 2 SHELL SORT LEC EX( 7):  S  *********
 2 SHELL SORT LEC EX( 8):  P  *******
 2 SHELL SORT LEC EX( 9): *R  ********
 2 SHELL SORT LEC EX(10):  T  **********

 3 SHELL SORT LEC EX: E O A E M R L S P X T
 3 SHELL SORT LEC EX( 0):  E  ***
 3 SHELL SORT LEC EX( 1): *O  ******
 3 SHELL SORT LEC EX( 2): *A  *
 3 SHELL SORT LEC EX( 3):  E  ***
 3 SHELL SORT LEC EX( 4):  M  *****
 3 SHELL SORT LEC EX( 5):  R  ********
 3 SHELL SORT LEC EX( 6):  L  ****
 3 SHELL SORT LEC EX( 7):  S  *********
 3 SHELL SORT LEC EX( 8):  P  *******
 3 SHELL SORT LEC EX( 9):  X  ***********
 3 SHELL SORT LEC EX(10):  T  **********

 4 SHELL SORT LEC EX: E A O E M R L S P X T
 4 SHELL SORT LEC EX( 0): *E  ***
 4 SHELL SORT LEC EX( 1): *A  *
 4 SHELL SORT LEC EX( 2):  O  ******
 4 SHELL SORT LEC EX( 3):  E  ***
 4 SHELL SORT LEC EX( 4):  M  *****
 4 SHELL SORT LEC EX( 5):  R  ********
 4 SHELL SORT LEC EX( 6):  L  ****
 4 SHELL SORT LEC EX( 7):  S  *********
 4 SHELL SORT LEC EX( 8):  P  *******
 4 SHELL SORT LEC EX( 9):  X  ***********
 4 SHELL SORT LEC EX(10):  T  **********

 5 SHELL SORT LEC EX: A E O E M R L S P X T
 5 SHELL SORT LEC EX( 0):  A  *
 5 SHELL SORT LEC EX( 1):  E  ***
 5 SHELL SORT LEC EX( 2): *O  ******
 5 SHELL SORT LEC EX( 3): *E  ***
 5 SHELL SORT LEC EX( 4):  M  *****
 5 SHELL SORT LEC EX( 5):  R  ********
 5 SHELL SORT LEC EX( 6):  L  ****
 5 SHELL SORT LEC EX( 7):  S  *********
 5 SHELL SORT LEC EX( 8):  P  *******
 5 SHELL SORT LEC EX( 9):  X  ***********
 5 SHELL SORT LEC EX(10):  T  **********

 6 SHELL SORT LEC EX: A E E O M R L S P X T
 6 SHELL SORT LEC EX( 0):  A  *
 6 SHELL SORT LEC EX( 1):  E  ***
 6 SHELL SORT LEC EX( 2):  E  ***
 6 SHELL SORT LEC EX( 3): *O  ******
 6 SHELL SORT LEC EX( 4): *M  *****
 6 SHELL SORT LEC EX( 5):  R  ********
 6 SHELL SORT LEC EX( 6):  L  ****
 6 SHELL SORT LEC EX( 7):  S  *********
 6 SHELL SORT LEC EX( 8):  P  *******
 6 SHELL SORT LEC EX( 9):  X  ***********
 6 SHELL SORT LEC EX(10):  T  **********

 7 SHELL SORT LEC EX: A E E M O R L S P X T
 7 SHELL SORT LEC EX( 0):  A  *
 7 SHELL SORT LEC EX( 1):  E  ***
 7 SHELL SORT LEC EX( 2):  E  ***
 7 SHELL SORT LEC EX( 3):  M  *****
 7 SHELL SORT LEC EX( 4):  O  ******
 7 SHELL SORT LEC EX( 5): *R  ********
 7 SHELL SORT LEC EX( 6): *L  ****
 7 SHELL SORT LEC EX( 7):  S  *********
 7 SHELL SORT LEC EX( 8):  P  *******
 7 SHELL SORT LEC EX( 9):  X  ***********
 7 SHELL SORT LEC EX(10):  T  **********

 8 SHELL SORT LEC EX: A E E M O L R S P X T
 8 SHELL SORT LEC EX( 0):  A  *
 8 SHELL SORT LEC EX( 1):  E  ***
 8 SHELL SORT LEC EX( 2):  E  ***
 8 SHELL SORT LEC EX( 3):  M  *****
 8 SHELL SORT LEC EX( 4): *O  ******
 8 SHELL SORT LEC EX( 5): *L  ****
 8 SHELL SORT LEC EX( 6):  R  ********
 8 SHELL SORT LEC EX( 7):  S  *********
 8 SHELL SORT LEC EX( 8):  P  *******
 8 SHELL SORT LEC EX( 9):  X  ***********
 8 SHELL SORT LEC EX(10):  T  **********

 9 SHELL SORT LEC EX: A E E M L O R S P X T
 9 SHELL SORT LEC EX( 0):  A  *
 9 SHELL SORT LEC EX( 1):  E  ***
 9 SHELL SORT LEC EX( 2):  E  ***
 9 SHELL SORT LEC EX( 3): *M  *****
 9 SHELL SORT LEC EX( 4): *L  ****
 9 SHELL SORT LEC EX( 5):  O  ******
 9 SHELL SORT LEC EX( 6):  R  ********
 9 SHELL SORT LEC EX( 7):  S  *********
 9 SHELL SORT LEC EX( 8):  P  *******
 9 SHELL SORT LEC EX( 9):  X  ***********
 9 SHELL SORT LEC EX(10):  T  **********

10 SHELL SORT LEC EX: A E E L M O R S P X T
10 SHELL SORT LEC EX( 0):  A  *
10 SHELL SORT LEC EX( 1):  E  ***
10 SHELL SORT LEC EX( 2):  E  ***
10 SHELL SORT LEC EX( 3):  L  ****
10 SHELL SORT LEC EX( 4):  M  *****
10 SHELL SORT LEC EX( 5):  O  ******
10 SHELL SORT LEC EX( 6):  R  ********
10 SHELL SORT LEC EX( 7): *S  *********
10 SHELL SORT LEC EX( 8): *P  *******
10 SHELL SORT LEC EX( 9):  X  ***********
10 SHELL SORT LEC EX(10):  T  **********

11 SHELL SORT LEC EX: A E E L M O R P S X T
11 SHELL SORT LEC EX( 0):  A  *
11 SHELL SORT LEC EX( 1):  E  ***
11 SHELL SORT LEC EX( 2):  E  ***
11 SHELL SORT LEC EX( 3):  L  ****
11 SHELL SORT LEC EX( 4):  M  *****
11 SHELL SORT LEC EX( 5):  O  ******
11 SHELL SORT LEC EX( 6): *R  ********
11 SHELL SORT LEC EX( 7): *P  *******
11 SHELL SORT LEC EX( 8):  S  *********
11 SHELL SORT LEC EX( 9):  X  ***********
11 SHELL SORT LEC EX(10):  T  **********

12 SHELL SORT LEC EX: A E E L M O P R S X T
12 SHELL SORT LEC EX( 0):  A  *
12 SHELL SORT LEC EX( 1):  E  ***
12 SHELL SORT LEC EX( 2):  E  ***
12 SHELL SORT LEC EX( 3):  L  ****
12 SHELL SORT LEC EX( 4):  M  *****
12 SHELL SORT LEC EX( 5):  O  ******
12 SHELL SORT LEC EX( 6):  P  *******
12 SHELL SORT LEC EX( 7):  R  ********
12 SHELL SORT LEC EX( 8):  S  *********
12 SHELL SORT LEC EX( 9): *X  ***********
12 SHELL SORT LEC EX(10): *T  **********

13 SHELL SORT LEC EX: A E E L M O P R S T X
13 SHELL SORT LEC EX( 0):  A  *
13 SHELL SORT LEC EX( 1):  E  ***
13 SHELL SORT LEC EX( 2):  E  ***
13 SHELL SORT LEC EX( 3):  L  ****
13 SHELL SORT LEC EX( 4):  M  *****
13 SHELL SORT LEC EX( 5):  O  ******
13 SHELL SORT LEC EX( 6):  P  *******
13 SHELL SORT LEC EX( 7):  R  ********
13 SHELL SORT LEC EX( 8):  S  *********
13 SHELL SORT LEC EX( 9):  T  **********
13 SHELL SORT LEC EX(10):  X  ***********

```


### [ex4](#stacks-and-queues)
4. Visualize various intermediate states from various sorts **Selection, Insertion, and Shell**

I found the rendition of intermediate states seen below in the block_str variable
from various sorts difficult to visualize. It is a sea of letters and words and 
hard to tell straight out which word is 'bigger', so I wrote some small visualizing code.
```
def test_849965():
  """Visualize arrays in columns."""
	# The column on the left contains an input array of 16
  # strings to be sorted; the column on the right contains the
  # strings in sorted order; each of the other 6 columns
  # contains the array at some intermediate step during either
  # insertion sort, selection sort, or shellsort (with different
  # columns potentially corresponding to different algorithms).

  # Unsorted                                         Sorted
  # col0   col1   col2   col3   col4   col5   col6   col7
  block_str = """
    slug   loon   crab   mule   carp   carp   carp   carp   
    crab   crab   hawk   crab   crab   crab   crab   crab   
    lynx   carp   lynx   lynx   hawk   frog   frog   frog   
    toad   frog   slug   toad   lynx   hawk   hawk   hawk   
    wren   mule   toad   wren   slug   loon   loon   loon   
    hawk   hawk   wren   hawk   toad   lynx   lynx   lynx   
    carp   lynx   carp   carp   wolf   mink   mink   mink   
    wolf   toad   wolf   wolf   wren   wolf   mule   mule   
    loon   worm   loon   loon   loon   wren   wren   pony   
    pony   pony   pony   pony   pony   pony   pony   slug   
    swan   mink   swan   swan   swan   swan   swan   swan   
    frog   tuna   frog   frog   frog   toad   toad   toad   
    worm   wren   worm   worm   worm   worm   worm   tuna   
    mule   slug   mule   slug   mule   mule   wolf   wolf   
    mink   swan   mink   mink   mink   slug   slug   worm   
    tuna   wolf   tuna   tuna   tuna   tuna   tuna   wren   
"""
  blk_visualizer(block_str)
```

```
> python -c 'import visualize_blktxt as T; T.test_849965()'
```
```
0  0 slug **********
0  1 crab **
0  2 lynx ******
0  3 toad ************
0  4 wren ****************
0  5 hawk ****
0  6 carp *
0  7 wolf **************
0  8 loon *****
0  9 pony *********
0 10 swan ***********
0 11 frog ***
0 12 worm ***************
0 13 mule ********
0 14 mink *******
0 15 tuna *************

1  0 loon *****
1  1 crab **
1  2 carp *
1  3 frog ***
1  4 mule ********
1  5 hawk ****
1  6 lynx ******
1  7 toad ************
1  8 worm ***************
1  9 pony *********
1 10 mink *******
1 11 tuna *************
1 12 wren ****************
1 13 slug **********
1 14 swan ***********
1 15 wolf **************

2  0 crab **
2  1 hawk ****
2  2 lynx ******
2  3 slug **********
2  4 toad ************
2  5 wren ****************
2  6 carp *
2  7 wolf **************
2  8 loon *****
2  9 pony *********
2 10 swan ***********
2 11 frog ***
2 12 worm ***************
2 13 mule ********
2 14 mink *******
2 15 tuna *************

3  0 mule ********
3  1 crab **
3  2 lynx ******
3  3 toad ************
3  4 wren ****************
3  5 hawk ****
3  6 carp *
3  7 wolf **************
3  8 loon *****
3  9 pony *********
3 10 swan ***********
3 11 frog ***
3 12 worm ***************
3 13 slug **********
3 14 mink *******
3 15 tuna *************

4  0 carp *
4  1 crab **
4  2 hawk ****
4  3 lynx ******
4  4 slug **********
4  5 toad ************
4  6 wolf **************
4  7 wren ****************
4  8 loon *****
4  9 pony *********
4 10 swan ***********
4 11 frog ***
4 12 worm ***************
4 13 mule ********
4 14 mink *******
4 15 tuna *************

5  0 carp *
5  1 crab **
5  2 frog ***
5  3 hawk ****
5  4 loon *****
5  5 lynx ******
5  6 mink *******
5  7 wolf **************
5  8 wren ****************
5  9 pony *********
5 10 swan ***********
5 11 toad ************
5 12 worm ***************
5 13 mule ********
5 14 slug **********
5 15 tuna *************

6  0 carp *
6  1 crab **
6  2 frog ***
6  3 hawk ****
6  4 loon *****
6  5 lynx ******
6  6 mink *******
6  7 mule ********
6  8 wren ****************
6  9 pony *********
6 10 swan ***********
6 11 toad ************
6 12 worm ***************
6 13 wolf **************
6 14 slug **********
6 15 tuna *************

7  0 carp *
7  1 crab **
7  2 frog ***
7  3 hawk ****
7  4 loon *****
7  5 lynx ******
7  6 mink *******
7  7 mule ********
7  8 pony *********
7  9 slug **********
7 10 swan ***********
7 11 toad ************
7 12 tuna *************
7 13 wolf **************
7 14 worm ***************
7 15 wren ****************

```

