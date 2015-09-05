# QuickUnion

## Code
  * [QuickUnionUF](../QuickUnionUF.py)

## Example Contents
  1. [Force the state of QuickUnion and visualize](#ex1)
  2. [Recreate demo from Quick Union (7:50) lecture](ex2)
  3. [TBD]
  4. [TBD]

## Examples
1. <a href="ex1"> Force the state of QuickUnion and visualize:</a> From the cmdline...   
```
> python -c 'import QuickUnionUF as Q; Q.QuickUnionUF(10).wr_png_tree_state([0, 9, 6, 5, 4, 2, 6, 1, 0, 5])'
```    
![QuickUnionUF state](./images/state_QuickUnionUF_0_9_6_5_4_2_6_1_0_5.png)


2. <a href="ex2">Recreate demo from Quick Union (7:50) lecture](ex2):</a> From the cmdline...
```
> python -c 'import test_QuickUnionUF as T; T.test_week1_lecture()
```    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  2  3  4  5  6  7  8  9 Initial values    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  2  3  3  5  6  7  8  9 union(4-3) [0] [1] [2] [3, 4] [5] [6] [7] [8] [9]    
![QU](./images/QU_demo_step0.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  2  8  3  5  6  7  8  9 union(3-8) [0] [1] [2] [5] [6] [7] [8, 3, 4] [9]    
![QU](./images/QU_demo_step1.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  2  8  3  5  5  7  8  9 union(6-5) [0] [1] [2] [5, 6] [7] [8, 3, 4] [9]    
![QU](./images/QU_demo_step2.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  2  8  3  5  5  7  8  8 union(9-4) [0] [1] [2] [5, 6] [7] [8, 9, 3, 4]    
![QU](./images/QU_demo_step3.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  1  8  3  5  5  7  8  8 union(2-1) [0] [1, 2] [5, 6] [8, 9, 3, 4] [7]    
![QU](./images/QU_demo_step4.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  1  8  3  5  5  7  8  8 union(8-9) [0] [1, 2] [5, 6] [8, 9, 3, 4] [7]    
![QU](./images/QU_demo_step5.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  1  8  3  0  5  7  8  8 union(5-0) [0, 5, 6] [1, 2] [8, 9, 3, 4] [7]    
![QU](./images/QU_demo_step6.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  0  1  1  8  3  0  5  1  8  8 union(7-2) [0, 5, 6] [1, 2, 7] [8, 9, 3, 4]    
![QU](./images/QU_demo_step7.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  1  1  1  8  3  0  5  1  8  8 union(6-1) [8, 9, 3, 4] [0, 1, 2, 5, 6, 7]    
![QU](./images/QU_demo_step8.png)    
IDX:  0  1  2  3  4  5  6  7  8  9    
val:  1  8  1  8  3  0  5  1  8  8 union(7-3) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
![QU](./images/QU_demo_step9.png)    


