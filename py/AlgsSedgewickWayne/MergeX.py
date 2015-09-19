"""MERGESORT WITH PRACTICAL IMPROVEMENTS.

  * Mergesort is too complicated for tiny arrays)
  * Recursive nature of sort means that there will be lots of sub-arrays to be sorted.
"""

#************************************************************************
 #  Compilation:  javac MergeX.java
 #  Execution:    java MergeX < input.txt
 #  Dependencies: StdOut.java StdIn.java
 #  Data files:   http://algs4.cs.princeton.edu/22mergesort/tiny.txt
 #                http://algs4.cs.princeton.edu/22mergesort/words3.txt
 #
 #  Sorts a sequence of strings from standard input using an
 #  optimized version of mergesort.
 #
 #  % more tiny.txt
 #  S O R T E X A M P L E
 #
 #  % java MergeX < tiny.txt
 #  A E E L M O P R S T X                 [ one string per line ]
 #
 #  % more words3.txt
 #  bed bug dad yes zoo ... all bad yet
 #
 #  % java MergeX < words3.txt
 #  all bad bed bug dad ... yes yet zoo    [ one string per line ]
 #
 #************************************************************************/

#*
 #  The <tt>MergeX</tt> class provides static methods for _sorting an
 #  array using an optimized version of mergesort.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/22mergesort">Section 2.2</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

import copy

def _merge(src, dst, lo, mid, hi):

    # precondition: src[lo .. mid] and src[mid+1 .. hi] are _sorted subarrays
    assert _isSorted(src, lo, mid)
    assert _isSorted(src, mid+1, hi)

    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        if    i > mid:              dst[k] = src[j]; j += 1
        elif  j > hi:               dst[k] = src[i]; i += 1
        elif _less(src[j], src[i]): dst[k] = src[j]; j += 1   # to ensure stability
        else:                       dst[k] = src[i]; i += 1

    # postcondition: dst[lo .. hi] is _sorted subarray
    assert _isSorted(dst, lo, hi)

def _sort(src, dst, lo, hi):
    # if (hi <= lo) return;
    CUTOFF = 7
    if hi <= lo + CUTOFF:
        _insertionSort(dst, lo, hi)
        return
    mid = lo + (hi - lo) / 2
    _sort(dst, src, lo, mid)
    _sort(dst, src, mid+1, hi)

    # if (!less(src[mid+1], src[mid])) {
    #    for (int i = lo; i <= hi; i++) dst[i] = src[i];
    #    return;
    # }

    # using System.arraycopy() is a bit faster than the above loop
    if  not _less(src[mid+1], src[mid]):
        System.arraycopy(src, lo, dst, lo, hi - lo + 1)
        return

    _merge(src, dst, lo, mid, hi)

#*
 # Rearranges the array in ascending order, using the natural order.
 # @param a the array to be _sorted
 #/
def Sort(a, array_history=None):
    aux = copy.deepcopy(a)
    _sort(aux, a, 0, len(a)-1)
    assert _isSorted(a)


# _sort from a[lo] to a[hi] using insertion sort
def _insertionSort(a, lo, hi):
    for i in range(lo, hi+1):
        j = i
        while j > lo and _less(a[j], a[j-1]):
            _exch(a, j, j-1)
            j -= 1


# exchange a[i] and a[j]
def _exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap

# is a[i] < a[j]?
def _less(a, b): return a < b

#**********************************************************************
#  Check if array is _sorted - useful for debugging
#**********************************************************************/
def _isSorted(a, lo=None, hi=None):
    if lo is None and hi is None:
      lo = 0
      hi = len(a) - 1
    for i in range( lo + 1, hi+1):
        if _less(a[i], a[i-1]): return False
    return True

#*
 # Reads in a sequence of strings from standard input; mergesorts them
 # (using an optimized version of mergesort);
 # and prints them to standard output in ascending order.
 #/
#def main():
#    String[] a = StdIn.readAllStrings()
#    MergeX.sort(a)
#    show(a)


# Copyright 2002-2010, Robert Sedgewick and Kevin Wayne.
# Java Last updated: Fri Feb 14 17:45:37 EST 2014.
