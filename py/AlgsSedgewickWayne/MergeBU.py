

#************************************************************************
 #  Compilation:  javac MergeBU.java
 #  Execution:    java MergeBU < input.txt
 #  Dependencies: StdOut.java StdIn.java
 #  Data files:   http://algs4.cs.princeton.edu/22mergesort/tiny.txt
 #                http://algs4.cs.princeton.edu/22mergesort/words3.txt
 #   
 #  Sorts a sequence of strings from standard input using
 #  bottom-up mergesort.
 #   
 #  % more tiny.txt
 #  S O R T E X A M P L E
 #
 #  % java MergeBU < tiny.txt
 #  A E E L M O P R S T X                 [ one string per line ]
 #    
 #  % more words3.txt
 #  bed bug dad yes zoo ... all bad yet
 #  
 #  % java MergeBU < words3.txt
 #  all bad bed bug dad ... yes yet zoo    [ one string per line ]
 #
 #************************************************************************/

#*
 #  The <tt>MergeBU</tt> class provides static methods for sorting an
 #  array using bottom-up mergesort.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

# stably merge a[lo..mid] with a[mid+1..hi] using aux[lo..hi]
def _merge(a, aux, lo, mid, hi):

    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = a[k]

    # merge back to a[]
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        if   i > mid:               a[k] = aux[j]; j += 1 # this copying is unneccessary
        elif j > hi:                a[k] = aux[i]; i += 1
        elif _less(aux[j], aux[i]): a[k] = aux[j]; j += 1
        else:                       a[k] = aux[i]; i += 1


#*
 # Rearranges the array in ascending order, using the natural order.
 # @param a the array to be sorted
 #/
def Sort(a, array_history=None):
    N = len(a)
    aux = [None for i in range(N)]
    n = 1
    while n < N: 
        i = 0
        while i < N-n:
            lo = i
            m  = i+n-1
            hi = min(i+n+n-1, N-1)
            _merge(a, aux, lo, m, hi)
            i += n+n
        n = n+n
    assert _isSorted(a)

#**********************************************************************
#  Helper sorting functions
#**********************************************************************/

# is v < w ?
def _less(v, w): return v < w

# exchange a[i] and a[j]
def _exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap


#**********************************************************************
#  Check if array is sorted - useful for debugging
#**********************************************************************/
def _isSorted(a):
    for i in range(1, len(a)):
        if _less(a[i], a[i-1]): return False
    return True

#*
 # Reads in a sequence of strings from standard input; bottom-up
 # mergesorts them; and prints them to standard output in ascending order. 
 #/
#def main(String[] args):
#    String[] a = StdIn.readAllStrings()
#    MergeBU.sort(a)
#    show(a)


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Last updated: Wed Dec 4 11:48:10 EST 2013.
