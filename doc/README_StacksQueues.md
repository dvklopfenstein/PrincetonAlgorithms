# Stacks and Queues

## Code
  * [Stack](../py/AlgsSedgewickWayne/Stack.py)
  * [ResizingArrayStack.py](../py/AlgsSedgewickWayne/ResizingArrayStack.py)
  * [Queue.py](../py/AlgsSedgewickWayne/Queue.py)
  * [ResizingArrayQueue.py](../py/AlgsSedgewickWayne/ResizingArrayQueue.py)

## Example Table of Contents
  1. [Run Stack lecture Quiz](#ex1)    
  1a. [Confirm "0 - 1 - 2 - 3 4 - - 5 6 - 7 8 9 - - - -" leaves "0 1 2 4 3 6 9 8 7 5"](#ex1a)    
  2. [Run Queue](#ex2)

## Example Contents
### [ex1](#example-contents)
1. Run Stack lecture Quiz, **Stacks (16:24)**, at 05:17 
```
> python -c 'import test_Stack as T; T.test_Stack_lec_quiz()'

   Pass GIVEN(1 2 3 4 5 - - - - -) -> ACTUAL(5 4 3 2 1)
   Pass GIVEN(1 2 5 - 3 4 - - - -) -> ACTUAL(5 4 3 2 1)
 **FAIL GIVEN(5 - 1 2 3 - 4 - - -) -> ACTUAL(5 3 4 2 1) EXPECTED(5 4 3 2 1)
   Pass GIVEN(5 - 4 - 3 - 2 - 1 -) -> ACTUAL(5 4 3 2 1)

```    

### [ex1a](#example-contents)
```
test_Stack.py "0 - 1 - 2 - 3 4 - - 5 6 - 7 8 9 - - - -"
```
```
INPUT: 0 - 1 - 2 - 3 4 - - 5 6 - 7 8 9 - - - -
             PUSH 0          +STACK: 0
         0 <-POP  -          -STACK:
             PUSH 1          +STACK: 1
         1 <-POP  -          -STACK:
             PUSH 2          +STACK: 2
         2 <-POP  -          -STACK:
             PUSH 3          +STACK: 3
             PUSH 4          +STACK: 4 3
         4 <-POP  -          -STACK: 3
         3 <-POP  -          -STACK:
             PUSH 5          +STACK: 5
             PUSH 6          +STACK: 6 5
         6 <-POP  -          -STACK: 5
             PUSH 7          +STACK: 7 5
             PUSH 8          +STACK: 8 7 5
             PUSH 9          +STACK: 9 8 7 5
         9 <-POP  -          -STACK: 8 7 5
         8 <-POP  -          -STACK: 7 5
         7 <-POP  -          -STACK: 5
         5 <-POP  -          -STACK:
(0 left on stack)
```

### [ex2](#example-contents)
2. Run Queue


