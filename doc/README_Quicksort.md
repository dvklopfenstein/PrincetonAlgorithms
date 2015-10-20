# Quicksort

## Code
  * [Quick](../py/AlgsSedgewickWayne/Quick.py)
  * [Quick3way](../py/AlgsSedgewickWayne/Quick3way.py) 
    => Prevent 1/2 N^2 time with duplicate keys

## Table of Contents for Examples
  1. [Run Lecture Example from **Quicksort (19:33)**](#ex1)

## Examples
### [ex1](#table-of-contents-for-examples)
1. Run Lecture Example from **Quicksort (19:33)]**
```
>>> test_Quick_partition.py "K R A T E L E P U I M Q C X O S"
```
```
 0: K R A T E L E P U I M Q C X O S <= arr
    . X . . . . . . . . . . X . . .
 1: K C A T E L E P U I M Q R X O S <= arr
    . . . X . . . . . X . . . . . .
 2: K C A I E L E P U T M Q R X O S <= arr
    . . . . . X X . . . . . . . . .
 3: K C A I E E L P U T M Q R X O S <= arr
    X . . . . X . . . . . . . . . .
 4: E C A I E K L P U T M Q R X O S <= arr

QUICKSORT PARTITION RESULT: E C A I E K L P U T M Q R X O S
```
