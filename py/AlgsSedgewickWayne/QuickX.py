
#************************************************************************
 #  Compilation:  javac QuickX.java
 #  Execution:    java QuickX N
 #
 #  Uses the Bentley-McIlroy 3-way partitioning scheme,
 #  chooses the partitioning element using Tukey's ninther,
 #  and cuts off to insertion sort.
 #
 #  Reference: Engineering a Sort Function by Jon L. Bentley
 #  and M. Douglas McIlroy. Softwae-Practice and Experience,
 #  Vol. 23 (11), 1249-1265 (November 1993).
 #
 #************************************************************************/

#*
 #  The <tt>QuickX</tt> class provides static methods for sorting an
 #  array using an optimized version of quicksort (using Bentley-McIlroy
 #  3-way partitioning, Tukey's ninther, and cutoff to insertion sort).
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
    _sort(a, 0, len(a) - 1)

def _sort(a, lo, hi):
    N = hi - lo + 1

    # cutoff to insertion sort
    CUTOFF = 8  # cutoff to insertion sort, must be >= 1
    if N <= CUTOFF:
        _insertionSort(a, lo, hi)
        return

    # use median-of-3 as partitioning element
    elif N <= 40:
        m = _median3(a, lo, lo + N/2, hi)
        _exch(a, m, lo)

    # use Tukey ninther as partitioning element
    else:
        eps = N/8
        mid = lo + N/2
        m1 = _median3(a, lo, lo + eps, lo + eps + eps)
        m2 = _median3(a, mid - eps, mid, mid + eps)
        m3 = _median3(a, hi - eps - eps, hi - eps, hi)
        ninther = _median3(a, m1, m2, m3)
        _exch(a, ninther, lo)

    # Bentley-McIlroy 3-way partitioning
    i = lo; j = hi+1
    p = lo; q = hi+1
    v = a[lo]
    while (True):
        i += 1
        while _less(a[i], v):
            if i == hi: break
            i += 1
        j -= 1
        while _less(v, a[j]):
            if j == lo: break
            j -= 1

        # pointers cross
        if i == j and a[i] == v:
            p += 1
            _exch(a, p, i)
        if i >= j: break

        _exch(a, i, j)
        if _eq(a[i], v):
          p += 1
          _exch(a, p, i)
        if _eq(a[j], v):
          q -= 1
          _exch(a, q, j)


    i = j + 1
    for k in range(lo, p+1): _exch(a, k, j); j -= 1
    #for (int k = hi; k >= q; k--:
    for k in range(hi, q-1, -1): _exch(a, k, i); i += 1

    _sort(a, lo, j)
    _sort(a, i, hi)


# sort from a[lo] to a[hi] using insertion sort
def _insertionSort(a, lo, hi):
    for i in range(lo, hi+1):
        j = i
        while j > lo  and _less(a[j], a[j-1]):
            _exch(a, j, j-1)
            j -= 1


# return the index of the median element among a[i], a[j], and a[k]
def _median3(a, i, j, k):
    return (_less(a[i], a[j]) if
           (_less(a[j], a[k]) if  j else _less(a[i], a[k]) if k else i) else
           (_less(a[k], a[j]) if  j else _less(a[k], a[i]) if k else i))

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
def _isSorted(a):
    for i in range(1, len(a)):
        if _less(a[i], a[i-1]): return False
    return True

#*
 # Reads in a sequence of strings from standard input; quicksorts them
 # (using an optimized version of quicksort);
 # and prints them to standard output in ascending order.
 #/
#def main(String[] args):
#    String[] a = StdIn.readAllStrings()
#    QuickX.sort(a)
#    show(a)



# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# java Last updated: Sun Feb 2 06:06:56 EST 2014.
