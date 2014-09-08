#!/usr/bin/env python
#************************************************************************
 #  Compilation:  javac BinarySearch.java
 #  Execution:    java BinarySearch whitelist.txt < input.txt
 #  Dependencies: In.java StdIn.java StdOut.java
 #  Data files:   http://algs4.cs.princeton.edu/11model/tinyW.txt
 #                http://algs4.cs.princeton.edu/11model/tinyT.txt
 #                http://algs4.cs.princeton.edu/11model/largeW.txt
 #                http://algs4.cs.princeton.edu/11model/largeT.txt
 #
 #  % java BinarySearch tinyW.txt < tinyT.txt
 #  50
 #  99
 #  13
 #
 #  % java BinarySearch largeW.txt < largeT.txt | more
 #  499569
 #  984875
 #  295754
 #  207807
 #  140925
 #  161828
 #  [367,966 total values]
 #  
 #************************************************************************/


#*
 #  The <tt>BinarySearch</tt> class provides a static method for binary
 #  searching for an integer in a sorted array of integers.
 #  <p>
 #  The <em>rank</em> operations takes logarithmic time in the worst case.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/11model">Section 1.1</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

    # Searches for the integer key in the sorted array a[].
    # @param key the search key
    # @param a the array of integers, must be sorted in ascending order
    # @return index of key in array a[] if present; -1 if not present
    def rank(key, a):
        lo = 0
        hi = len(a) - 1
        while (lo <= hi):
            #  is in a[lo..hi] or not present.
            mid = lo + (hi - lo) / 2
            if   key < a[mid]: hi = mid - 1
            elif key > a[mid]: lo = mid + 1
            else: return mid
        return -1

    # Reads in a sequence of integers from the whitelist file, specified as
    # a command-line argument. Reads in integers from standard input and
    # prints to standard output those integers that do *not* appear in the file.
    def main():
        import InputArgs
        # read the integers from a file
        data = InputArgs.getStrArray("0 1 2 3 4 5 7 9")
        int[] whitelist = in.readAllInts()

        # sort the array
        Arrays.sort(whitelist)

        # read integer key from standard input; print if not in whitelist
        while (!StdIn.isEmpty()):
            key = StdIn.readInt()
            if rank(key, whitelist) == -1)
                StdOut.println(key)

if __name__ == '__main__':
  import os
  from random import randrange
  if len(sys.argv) == 1:
    run_fin('../../thirdparty/tinyW.txt')
  elif os.path.isfile(sys.argv[1]):
    run_fin(sys.argv[1])
  elif sys.argv == 'all':
    fins = [
      '../../thirdparty/tinyW.txt',
      '../../thirdparty/tinyT.txt',
      '../../thirdparty/largeW.txt',
      '../../thirdparty/largeT.txt',]
    run_fins(fins)
  elif sys.argv[1].isdigit():
    a = [randrange(-999999, 999999) for i in range(int(sys.argv[1]))]
    a = range(int(sys.argv[1]))

# Copyright © 2002–2010, Robert Sedgewick and Kevin Wayne. 
# Java last updated: Sun Aug 31 21:38:23 EDT 2014.
