# [Radix Sorts](http://algs4.cs.princeton.edu/51radix)

## Code
  * **Strings in Java**
  * **Key-Indexed Counting**
  * **LSD Radix Sort**: LSD.py
  * **MSD Radix Sort**: MSD.py
  * **3-way Radix Quicksort**: code.py
  * **Suffic Arrays**: code.py

## Table of Contents for Examples
  1. [What is the array immediately after performing (LSD radix sort) key-indexed counting for the second time?](#ex1)    
  2. [What is the array immediately after performing (MSD radix sort) key-indexed counting for the third time?](#ex2)    
  3. [What is the array immediately after the first partitioning step (of 3-way radix quicksort)?](#ex3)    

## Examples 
### [ex1](#table-of-contents-for-examples)    
**What is the array immediately after performing (LSD radix sort) key-indexed counting for the second time?**    
```
Suppose that you run LSD radix sort on the following array of 10 fixed-length strings:

    1333 2232 2342 1242 3211 2311 2141 1342 4343 4432 

What is the array immediately after performing key-indexed counting for the second time?
```

### [ex2](#table-of-contents-for-examples)    
**What is the array immediately after performing (MSD radix sort) key-indexed counting for the third time?**    
```
Suppose that you run MSD radix sort on the following array of 15 strings:

    2431 3421 3422 1342 3221 1313 1332 4414 2343 3143 1244 1132 1413 2333 4313 

What is the array immediately after performing key-indexed counting for the third time?
Recall that key-indexed counting sorts a subarray using the dth character as the key
and that the base cases for MSD radix sort are subarrays of size 0 or 1.
```

### [ex3](#table-of-contents-for-examples)    
**What is the array immediately after the first partitioning step (of 3-way radix quicksort)?**    
```
Suppose that you run 3-way radix quicksort (do not shuffle) on the following
array of 10 strings:

    2514 4444 4441 2433 1266 2114 2663 2221 5336 1131 

What is the array immediately after the first partitioning step?
```

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
