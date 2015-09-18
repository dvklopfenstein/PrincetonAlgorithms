# Stacks and Queues

## Code
  * [Selection Sort](../py/AlgsSedgewickWayne/Selection.py)
  * [Insertion Sort](../py/AlgsSedgewickWayne/Insertion.py)
  * [Shell Sort](../py/AlgsSedgewickWayne/Shell.py)

## Visualization Description
There are two ways to view the progression of a sort:

  1. The concise way: One print of the array state per iteration. It looks like this:    
     0: 7 10 5 3 8 4 2 9 6    
     1: 2 10 5 3 8 4 7 9 6    
     ...

  2. The verbose but visually pleasing way of viewing the sort progression.

     The second way of visualizing includes one "paragraph" for each
     iteration. There are horizontal "bars" made of '*'s showing 
     how large each element is. This helps dyslexics and tired people
     to not be confused as to which element is bigger when viewing a 
     ton of numbers or letters all at once. As we proceed through each paragragh,
     notice that the bars begin to lined up in smallest to biggest order.
     This is the verbose, but descriptive way to see the progression of the sort.

## Example Table of Contents
  1. [Run Lecture Example from **Selection (6:59)**](#ex1)    
     > python -c 'import test_Selection as T; T.test_wk2_lec()'

  2. [Run Lecture Example from **Insertion (9:28)**](#ex2)    
     > python -c 'import test_Insertion as T; T.test_wk2_lec()'

  2a. [Run Best Case Example from **Insertion (9:28)**](#ex2a); Array is already sorted    

  3. [Run Lecture Example from **Shellsort (10:48)**](#ex3)    
     > python -c 'import test_Shell as T; T.test_wk2_lec()'

## Example Contents
### [ex1](#stacks-and-queues)
1. Run Lecture Example from **Selection (6:59)**
```
> python -c 'import test_Selection as T; T.test_wk2_lec()'
```
```
SELECTION SORT
 0: 7 10 5 3 8 4 2 9 6
 1: 2 10 5 3 8 4 7 9 6
 2: 2 3 5 10 8 4 7 9 6
 3: 2 3 4 10 8 5 7 9 6
 4: 2 3 4 5 8 10 7 9 6
 5: 2 3 4 5 6 10 7 9 8
 6: 2 3 4 5 6 7 10 9 8
 7: 2 3 4 5 6 7 8 9 10
 8: 2 3 4 5 6 7 8 9 10
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
 1: 7 5 10 3 8 4 2 9 6
 2: 5 7 10 3 8 4 2 9 6
 3: 5 7 3 10 8 4 2 9 6
 4: 5 3 7 10 8 4 2 9 6
 5: 3 5 7 10 8 4 2 9 6
 6: 3 5 7 8 10 4 2 9 6
 7: 3 5 7 8 4 10 2 9 6
 8: 3 5 7 4 8 10 2 9 6
 9: 3 5 4 7 8 10 2 9 6
10: 3 4 5 7 8 10 2 9 6
11: 3 4 5 7 8 2 10 9 6
12: 3 4 5 7 2 8 10 9 6
13: 3 4 5 2 7 8 10 9 6
14: 3 4 2 5 7 8 10 9 6
15: 3 2 4 5 7 8 10 9 6
16: 2 3 4 5 7 8 10 9 6
17: 2 3 4 5 7 8 9 10 6
18: 2 3 4 5 7 8 9 6 10
19: 2 3 4 5 7 8 6 9 10
20: 2 3 4 5 7 6 8 9 10
21: 2 3 4 5 6 7 8 9 10

 0 INSERTION SORT: SEED 183182: 7 10 5 3 8 4 2 9 6
 0 INSERTION SORT: SEED 183182( 0):   7 ******
 0 INSERTION SORT: SEED 183182( 1): *10 *********
 0 INSERTION SORT: SEED 183182( 2): * 5 ****
 0 INSERTION SORT: SEED 183182( 3):   3 **
 0 INSERTION SORT: SEED 183182( 4):   8 *******
 0 INSERTION SORT: SEED 183182( 5):   4 ***
 0 INSERTION SORT: SEED 183182( 6):   2 *
 0 INSERTION SORT: SEED 183182( 7):   9 ********
 0 INSERTION SORT: SEED 183182( 8):   6 *****

 1 INSERTION SORT: SEED 183182: 7 5 10 3 8 4 2 9 6
 1 INSERTION SORT: SEED 183182( 0): * 7 ******
 1 INSERTION SORT: SEED 183182( 1): * 5 ****
 1 INSERTION SORT: SEED 183182( 2):  10 *********
 1 INSERTION SORT: SEED 183182( 3):   3 **
 1 INSERTION SORT: SEED 183182( 4):   8 *******
 1 INSERTION SORT: SEED 183182( 5):   4 ***
 1 INSERTION SORT: SEED 183182( 6):   2 *
 1 INSERTION SORT: SEED 183182( 7):   9 ********
 1 INSERTION SORT: SEED 183182( 8):   6 *****

 2 INSERTION SORT: SEED 183182: 5 7 10 3 8 4 2 9 6
 2 INSERTION SORT: SEED 183182( 0):   5 ****
 2 INSERTION SORT: SEED 183182( 1):   7 ******
 2 INSERTION SORT: SEED 183182( 2): *10 *********
 2 INSERTION SORT: SEED 183182( 3): * 3 **
 2 INSERTION SORT: SEED 183182( 4):   8 *******
 2 INSERTION SORT: SEED 183182( 5):   4 ***
 2 INSERTION SORT: SEED 183182( 6):   2 *
 2 INSERTION SORT: SEED 183182( 7):   9 ********
 2 INSERTION SORT: SEED 183182( 8):   6 *****

 3 INSERTION SORT: SEED 183182: 5 7 3 10 8 4 2 9 6
 3 INSERTION SORT: SEED 183182( 0):   5 ****
 3 INSERTION SORT: SEED 183182( 1): * 7 ******
 3 INSERTION SORT: SEED 183182( 2): * 3 **
 3 INSERTION SORT: SEED 183182( 3):  10 *********
 3 INSERTION SORT: SEED 183182( 4):   8 *******
 3 INSERTION SORT: SEED 183182( 5):   4 ***
 3 INSERTION SORT: SEED 183182( 6):   2 *
 3 INSERTION SORT: SEED 183182( 7):   9 ********
 3 INSERTION SORT: SEED 183182( 8):   6 *****

 4 INSERTION SORT: SEED 183182: 5 3 7 10 8 4 2 9 6
 4 INSERTION SORT: SEED 183182( 0): * 5 ****
 4 INSERTION SORT: SEED 183182( 1): * 3 **
 4 INSERTION SORT: SEED 183182( 2):   7 ******
 4 INSERTION SORT: SEED 183182( 3):  10 *********
 4 INSERTION SORT: SEED 183182( 4):   8 *******
 4 INSERTION SORT: SEED 183182( 5):   4 ***
 4 INSERTION SORT: SEED 183182( 6):   2 *
 4 INSERTION SORT: SEED 183182( 7):   9 ********
 4 INSERTION SORT: SEED 183182( 8):   6 *****

 5 INSERTION SORT: SEED 183182: 3 5 7 10 8 4 2 9 6
 5 INSERTION SORT: SEED 183182( 0):   3 **
 5 INSERTION SORT: SEED 183182( 1):   5 ****
 5 INSERTION SORT: SEED 183182( 2):   7 ******
 5 INSERTION SORT: SEED 183182( 3): *10 *********
 5 INSERTION SORT: SEED 183182( 4): * 8 *******
 5 INSERTION SORT: SEED 183182( 5):   4 ***
 5 INSERTION SORT: SEED 183182( 6):   2 *
 5 INSERTION SORT: SEED 183182( 7):   9 ********
 5 INSERTION SORT: SEED 183182( 8):   6 *****

 6 INSERTION SORT: SEED 183182: 3 5 7 8 10 4 2 9 6
 6 INSERTION SORT: SEED 183182( 0):   3 **
 6 INSERTION SORT: SEED 183182( 1):   5 ****
 6 INSERTION SORT: SEED 183182( 2):   7 ******
 6 INSERTION SORT: SEED 183182( 3):   8 *******
 6 INSERTION SORT: SEED 183182( 4): *10 *********
 6 INSERTION SORT: SEED 183182( 5): * 4 ***
 6 INSERTION SORT: SEED 183182( 6):   2 *
 6 INSERTION SORT: SEED 183182( 7):   9 ********
 6 INSERTION SORT: SEED 183182( 8):   6 *****

 7 INSERTION SORT: SEED 183182: 3 5 7 8 4 10 2 9 6
 7 INSERTION SORT: SEED 183182( 0):   3 **
 7 INSERTION SORT: SEED 183182( 1):   5 ****
 7 INSERTION SORT: SEED 183182( 2):   7 ******
 7 INSERTION SORT: SEED 183182( 3): * 8 *******
 7 INSERTION SORT: SEED 183182( 4): * 4 ***
 7 INSERTION SORT: SEED 183182( 5):  10 *********
 7 INSERTION SORT: SEED 183182( 6):   2 *
 7 INSERTION SORT: SEED 183182( 7):   9 ********
 7 INSERTION SORT: SEED 183182( 8):   6 *****

 8 INSERTION SORT: SEED 183182: 3 5 7 4 8 10 2 9 6
 8 INSERTION SORT: SEED 183182( 0):   3 **
 8 INSERTION SORT: SEED 183182( 1):   5 ****
 8 INSERTION SORT: SEED 183182( 2): * 7 ******
 8 INSERTION SORT: SEED 183182( 3): * 4 ***
 8 INSERTION SORT: SEED 183182( 4):   8 *******
 8 INSERTION SORT: SEED 183182( 5):  10 *********
 8 INSERTION SORT: SEED 183182( 6):   2 *
 8 INSERTION SORT: SEED 183182( 7):   9 ********
 8 INSERTION SORT: SEED 183182( 8):   6 *****

 9 INSERTION SORT: SEED 183182: 3 5 4 7 8 10 2 9 6
 9 INSERTION SORT: SEED 183182( 0):   3 **
 9 INSERTION SORT: SEED 183182( 1): * 5 ****
 9 INSERTION SORT: SEED 183182( 2): * 4 ***
 9 INSERTION SORT: SEED 183182( 3):   7 ******
 9 INSERTION SORT: SEED 183182( 4):   8 *******
 9 INSERTION SORT: SEED 183182( 5):  10 *********
 9 INSERTION SORT: SEED 183182( 6):   2 *
 9 INSERTION SORT: SEED 183182( 7):   9 ********
 9 INSERTION SORT: SEED 183182( 8):   6 *****

10 INSERTION SORT: SEED 183182: 3 4 5 7 8 10 2 9 6
10 INSERTION SORT: SEED 183182( 0):   3 **
10 INSERTION SORT: SEED 183182( 1):   4 ***
10 INSERTION SORT: SEED 183182( 2):   5 ****
10 INSERTION SORT: SEED 183182( 3):   7 ******
10 INSERTION SORT: SEED 183182( 4):   8 *******
10 INSERTION SORT: SEED 183182( 5): *10 *********
10 INSERTION SORT: SEED 183182( 6): * 2 *
10 INSERTION SORT: SEED 183182( 7):   9 ********
10 INSERTION SORT: SEED 183182( 8):   6 *****

11 INSERTION SORT: SEED 183182: 3 4 5 7 8 2 10 9 6
11 INSERTION SORT: SEED 183182( 0):   3 **
11 INSERTION SORT: SEED 183182( 1):   4 ***
11 INSERTION SORT: SEED 183182( 2):   5 ****
11 INSERTION SORT: SEED 183182( 3):   7 ******
11 INSERTION SORT: SEED 183182( 4): * 8 *******
11 INSERTION SORT: SEED 183182( 5): * 2 *
11 INSERTION SORT: SEED 183182( 6):  10 *********
11 INSERTION SORT: SEED 183182( 7):   9 ********
11 INSERTION SORT: SEED 183182( 8):   6 *****

12 INSERTION SORT: SEED 183182: 3 4 5 7 2 8 10 9 6
12 INSERTION SORT: SEED 183182( 0):   3 **
12 INSERTION SORT: SEED 183182( 1):   4 ***
12 INSERTION SORT: SEED 183182( 2):   5 ****
12 INSERTION SORT: SEED 183182( 3): * 7 ******
12 INSERTION SORT: SEED 183182( 4): * 2 *
12 INSERTION SORT: SEED 183182( 5):   8 *******
12 INSERTION SORT: SEED 183182( 6):  10 *********
12 INSERTION SORT: SEED 183182( 7):   9 ********
12 INSERTION SORT: SEED 183182( 8):   6 *****

13 INSERTION SORT: SEED 183182: 3 4 5 2 7 8 10 9 6
13 INSERTION SORT: SEED 183182( 0):   3 **
13 INSERTION SORT: SEED 183182( 1):   4 ***
13 INSERTION SORT: SEED 183182( 2): * 5 ****
13 INSERTION SORT: SEED 183182( 3): * 2 *
13 INSERTION SORT: SEED 183182( 4):   7 ******
13 INSERTION SORT: SEED 183182( 5):   8 *******
13 INSERTION SORT: SEED 183182( 6):  10 *********
13 INSERTION SORT: SEED 183182( 7):   9 ********
13 INSERTION SORT: SEED 183182( 8):   6 *****

14 INSERTION SORT: SEED 183182: 3 4 2 5 7 8 10 9 6
14 INSERTION SORT: SEED 183182( 0):   3 **
14 INSERTION SORT: SEED 183182( 1): * 4 ***
14 INSERTION SORT: SEED 183182( 2): * 2 *
14 INSERTION SORT: SEED 183182( 3):   5 ****
14 INSERTION SORT: SEED 183182( 4):   7 ******
14 INSERTION SORT: SEED 183182( 5):   8 *******
14 INSERTION SORT: SEED 183182( 6):  10 *********
14 INSERTION SORT: SEED 183182( 7):   9 ********
14 INSERTION SORT: SEED 183182( 8):   6 *****

15 INSERTION SORT: SEED 183182: 3 2 4 5 7 8 10 9 6
15 INSERTION SORT: SEED 183182( 0): * 3 **
15 INSERTION SORT: SEED 183182( 1): * 2 *
15 INSERTION SORT: SEED 183182( 2):   4 ***
15 INSERTION SORT: SEED 183182( 3):   5 ****
15 INSERTION SORT: SEED 183182( 4):   7 ******
15 INSERTION SORT: SEED 183182( 5):   8 *******
15 INSERTION SORT: SEED 183182( 6):  10 *********
15 INSERTION SORT: SEED 183182( 7):   9 ********
15 INSERTION SORT: SEED 183182( 8):   6 *****

16 INSERTION SORT: SEED 183182: 2 3 4 5 7 8 10 9 6
16 INSERTION SORT: SEED 183182( 0):   2 *
16 INSERTION SORT: SEED 183182( 1):   3 **
16 INSERTION SORT: SEED 183182( 2):   4 ***
16 INSERTION SORT: SEED 183182( 3):   5 ****
16 INSERTION SORT: SEED 183182( 4):   7 ******
16 INSERTION SORT: SEED 183182( 5):   8 *******
16 INSERTION SORT: SEED 183182( 6): *10 *********
16 INSERTION SORT: SEED 183182( 7): * 9 ********
16 INSERTION SORT: SEED 183182( 8):   6 *****

17 INSERTION SORT: SEED 183182: 2 3 4 5 7 8 9 10 6
17 INSERTION SORT: SEED 183182( 0):   2 *
17 INSERTION SORT: SEED 183182( 1):   3 **
17 INSERTION SORT: SEED 183182( 2):   4 ***
17 INSERTION SORT: SEED 183182( 3):   5 ****
17 INSERTION SORT: SEED 183182( 4):   7 ******
17 INSERTION SORT: SEED 183182( 5):   8 *******
17 INSERTION SORT: SEED 183182( 6):   9 ********
17 INSERTION SORT: SEED 183182( 7): *10 *********
17 INSERTION SORT: SEED 183182( 8): * 6 *****

18 INSERTION SORT: SEED 183182: 2 3 4 5 7 8 9 6 10
18 INSERTION SORT: SEED 183182( 0):   2 *
18 INSERTION SORT: SEED 183182( 1):   3 **
18 INSERTION SORT: SEED 183182( 2):   4 ***
18 INSERTION SORT: SEED 183182( 3):   5 ****
18 INSERTION SORT: SEED 183182( 4):   7 ******
18 INSERTION SORT: SEED 183182( 5):   8 *******
18 INSERTION SORT: SEED 183182( 6): * 9 ********
18 INSERTION SORT: SEED 183182( 7): * 6 *****
18 INSERTION SORT: SEED 183182( 8):  10 *********

19 INSERTION SORT: SEED 183182: 2 3 4 5 7 8 6 9 10
19 INSERTION SORT: SEED 183182( 0):   2 *
19 INSERTION SORT: SEED 183182( 1):   3 **
19 INSERTION SORT: SEED 183182( 2):   4 ***
19 INSERTION SORT: SEED 183182( 3):   5 ****
19 INSERTION SORT: SEED 183182( 4):   7 ******
19 INSERTION SORT: SEED 183182( 5): * 8 *******
19 INSERTION SORT: SEED 183182( 6): * 6 *****
19 INSERTION SORT: SEED 183182( 7):   9 ********
19 INSERTION SORT: SEED 183182( 8):  10 *********

20 INSERTION SORT: SEED 183182: 2 3 4 5 7 6 8 9 10
20 INSERTION SORT: SEED 183182( 0):   2 *
20 INSERTION SORT: SEED 183182( 1):   3 **
20 INSERTION SORT: SEED 183182( 2):   4 ***
20 INSERTION SORT: SEED 183182( 3):   5 ****
20 INSERTION SORT: SEED 183182( 4): * 7 ******
20 INSERTION SORT: SEED 183182( 5): * 6 *****
20 INSERTION SORT: SEED 183182( 6):   8 *******
20 INSERTION SORT: SEED 183182( 7):   9 ********
20 INSERTION SORT: SEED 183182( 8):  10 *********

21 INSERTION SORT: SEED 183182: 2 3 4 5 6 7 8 9 10
21 INSERTION SORT: SEED 183182( 0):   2 *
21 INSERTION SORT: SEED 183182( 1):   3 **
21 INSERTION SORT: SEED 183182( 2):   4 ***
21 INSERTION SORT: SEED 183182( 3):   5 ****
21 INSERTION SORT: SEED 183182( 4):   6 *****
21 INSERTION SORT: SEED 183182( 5):   7 ******
21 INSERTION SORT: SEED 183182( 6):   8 *******
21 INSERTION SORT: SEED 183182( 7):   9 ********
21 INSERTION SORT: SEED 183182( 8):  10 *********

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


### [ex3](#stacks-and-queues)
3. Run Lecture Example from **Shellsort (10:48)**
```
> python -c 'import test_Shell as T; T.test_wk2_lec()'
```
```
SHELL SORT LEC EX RESULT: A E E L M O P R S T X

 0: M O L E E X A S P R T
 1: E O L E M X A S P R T
 2: E O A E M X L S P R T
 3: E O A E M R L S P X T
 4: E A O E M R L S P X T
 5: A E O E M R L S P X T
 6: A E E O M R L S P X T
 7: A E E M O R L S P X T
 8: A E E M O L R S P X T
 9: A E E M L O R S P X T
10: A E E L M O R S P X T
11: A E E L M O R P S X T
12: A E E L M O P R S X T
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





