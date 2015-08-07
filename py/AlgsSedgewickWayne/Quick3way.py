
#************************************************************************
 #  Compilation:  javac Quick3way.java
 #  Execution:    java Quick3way < input.txt
 #  Dependencies: StdOut.java StdIn.java
 #  Data files:   http://algs4.cs.princeton.edu/23quicksort/tiny.txt
 #                http://algs4.cs.princeton.edu/23quicksort/words3.txt
 #
 #  Sorts a sequence of strings from standard input using 3-way quicksort.
 #
 #  % more tiny.txt
 #  S O R T E X A M P L E
 #
 #  % java Quick3way < tiny.txt
 #  A E E L M O P R S T X                 [ one string per line ]
 #
 #  % more words3.txt
 #  bed bug dad yes zoo ... all bad yet
 #
 #  % java Quick3way < words3.txt
 #  all bad bed bug dad ... yes yet zoo    [ one string per line ]
 #
 #************************************************************************/

#*
 #  The <tt>Quick3way</tt> class provides static methods for sorting an
 #  array using quicksort with 3-way partitioning.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

#*
 # Rearranges the array in ascending order, using the natural order.
 # @param a the array to be sorted
 #/
def Sort(a, array_history=None):
    import random
    random.shuffle(a)
    _sort(a, 0, len(a) - 1)
    assert _isSorted(a)

# quicksort the subarray a[lo .. hi] using 3-way partitioning
def _sort(a, lo, hi):
    if hi <= lo: return
    lt = lo
    gt = hi
    v  = a[lo]
    i  = lo
    while (i <= gt):
        if   a[i] < v:
          _exch(a, lt, i)
          lt += 1
          i  += 1
        elif a[i] > v:
          _exch(a, i, gt)
          gt -= 1
        else: i += 1

    # a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi].
    _sort(a, lo, lt-1)
    _sort(a, gt+1, hi)
    assert _isSorted(a, lo, hi)



#**********************************************************************
#  Helper sorting functions
#**********************************************************************/

# is v < w ?
def _less(v, w): return v < w

# does v == w ?
def _eq(v, w): return v == w

# exchange a[i] and a[j]
def _exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap


#**********************************************************************
#  Check if array is sorted - useful for debugging
#**********************************************************************/
def _isSorted(a, lo=None, hi=None):
    if lo is None and hi is None:
      lo = 0
      hi = len(a) - 1
    for i in range(lo + 1, hi+1):
        if _less(a[i], a[i-1]): return False
    return True


#*
 # Reads in a sequence of strings from standard input; 3-way
 # quicksorts them; and prints them to standard output in ascending order.
 #/
# def main(String[] args):
#     String[] a = StdIn.readAllStrings()
#     Quick3way.sort(a)
#     show(a)



# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Last updated: Tue Sep 24 11:52:34 EDT 2013.
