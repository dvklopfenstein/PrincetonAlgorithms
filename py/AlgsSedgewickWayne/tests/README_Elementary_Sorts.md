# Stacks and Queues

## Code
  * [Selection Sort](../Selection.py)

## Visualization Description
There are two ways to view the progression of a sort:

  1. The concise way: One print of the array state per iteration. It looks like this:    
     0: 7 10 5 3 8 4 2 9 6    
     1: 2 10 5 3 8 4 7 9 6    

  2. The verbose but visually pleasing way of viewing the sort progression.

The second way of visualizing includes one "paragraph" for each
iteration. There are horizontal "bars" made of '*'s showing 
how large each element is. This helps dyslexics and tired people
to not be confused as to which element is bigger when viewing a 
ton of numbers or letters all at once. As we proceed through each paragragh,
notice that the bars begin to lined up in smallest to biggest order.
This is the verbose, but descriptive way to see the progression of the sort.

## Example Table of Contents
  1. [Run Lecture Example from **Selction (6:59)**](#ex1)

## Example Contents
### [ex1](#example-contents)
1. Run Lecture Example from **Selction (6:59)**
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


