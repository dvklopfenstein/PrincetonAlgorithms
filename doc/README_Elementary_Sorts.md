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
  3. [Run Lecture Example from **Shellsort (10:48)**](#ex3)
     > python -c 'import test_Shell as T; T.test_wk2_lec()'

## Example Contents
### [ex1](#example-contents)
1. Run Lecture Example from **Selection (6:59)**
```
> python -c 'import test_Selection as T; T.test_wk2_lec()'

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


### [ex2](#example-contents)
2. Run Lecture Example from **Insertion (9:28)**
```
> python -c 'import test_Insertion as T; T.test_wk2_lec()'
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

### [ex3](#example-contents)
3. [Run Lecture Example from **Shellsort (10:48)**](#ex3)
```
> python -c 'import test_Shell as T; T.test_wk2_lec()'
```




