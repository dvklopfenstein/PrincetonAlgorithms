# Quicksort

## Code
  * [Quick](../py/AlgsSedgewickWayne/Quick.py)
  * [Quick3way](../py/AlgsSedgewickWayne/Quick3way.py) 
    => Prevent 1/2 N^2 time with duplicate keys

## Table of Contents for Examples
  1. [Run **Partitioning** Example from the Lecture, **Quicksort (19:33)**](#ex1)
  2. [Run **Partitioning** Example from the Lecture, **Duplicate Keys (11:25)**](#ex2)

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


### [ex2](#table-of-contents-for-examples)
2. Run **Partitioning** Example from the Lecture, **Duplicate Keys (11:25)**    
```
>>> test_Quick3way.py "P A B X W P P V P D P C Y Z"
```
```
 0: P A B X W P P V P D P C Y Z <= arr
    X X . . . . . . . . . . . .
 1: A P B X W P P V P D P C Y Z <= arr
    . X X . . . . . . . . . . .
 2: A B P X W P P V P D P C Y Z <= arr
    . . . X . . . . . . . . . X
 3: A B P Z W P P V P D P C Y X <= arr
    . . . X . . . . . . . . X .
 4: A B P Y W P P V P D P C Z X <= arr
    . . . X . . . . . . . X . .
 5: A B P C W P P V P D P Y Z X <= arr
    . . X X . . . . . . . . . .
 6: A B C P W P P V P D P Y Z X <= arr
    . . . . X . . . . . X . . .
 7: A B C P P P P V P D W Y Z X <= arr
    . . . . . . . X . X . . . .
 8: A B C P P P P D P V W Y Z X <= arr
    . . . X . . . X . . . . . .
 9: A B C D P P P P P V W Y Z X <= arr
    . X . X . . . . . . . . . .
10: A D C B P P P P P V W Y Z X <= arr
    . X X . . . . . . . . . . .
11: A C D B P P P P P V W Y Z X <= arr
    . . . . . . . . . . . . . .
12: A C D B P P P P P V W Y Z X <= arr
    . . X X . . . . . . . . . .
13: A C B D P P P P P V W Y Z X <= arr
    . X X . . . . . . . . . . .
14: A B C D P P P P P V W Y Z X <= arr
    . . . . . . . . . . X . . X
15: A B C D P P P P P V X Y Z W <= arr
    . . . . . . . . . . X . X .
16: A B C D P P P P P V Z Y X W <= arr
    . . . . . . . . . . X X . .
17: A B C D P P P P P V Y Z X W <= arr
    . . . . . . . . . . . . . .
18: A B C D P P P P P V Y Z X W <= arr
    . . . . . . . . . . . X . X
19: A B C D P P P P P V Y W X Z <= arr
    . . . . . . . . . . X X . .
20: A B C D P P P P P V W Y X Z <= arr
    . . . . . . . . . . . X X .
21: A B C D P P P P P V W X Y Z <= arr
```
