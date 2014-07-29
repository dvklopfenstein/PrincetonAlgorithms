
 #************************************************************************
 #  Compilation:  javac Merge.java
 #  Execution:    java Merge < input.txt
 #  Dependencies: StdOut.java StdIn.java
 #  Data files:   http:#algs4.cs.princeton.edu/22mergesort/tiny.txt
 #                http:#algs4.cs.princeton.edu/22mergesort/words3.txt
 #   
 #  Sorts a sequence of strings from standard input using mergesort.
 #   
 #  % more tiny.txt
 #  S O R T E X A M P L E
 #
 #  % java Merge < tiny.txt
 #  A E E L M O P R S T X                 [ one string per line ]
 #    
 #  % more words3.txt
 #  bed bug dad yes zoo ... all bad yet
 #  
 #  % java Merge < words3.txt
 #  all bad bed bug dad ... yes yet zoo    [ one string per line ]
 #  
 #************************************************************************/

 #*
 #  The <tt>Merge</tt> class provides static methods for sorting an
 #  array using mergesort.
 #  <p>
 #  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/22mergesort">Section 2.2</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #  For an optimized version, see {@link MergeX}.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

# stably merge a[lo .. mid] with a[mid+1 ..hi] using aux[lo .. hi]
 def _merge(a, aux, lo, mid, hi):

    # precondition: a[lo .. mid] and a[mid+1 .. hi] are sorted subarrays
    assert isSorted(a, lo, mid)
    assert isSorted(a, mid+1, hi)

    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = a[k]

    # merge back to a[]
    int i = lo, j = mid+1;
    for k in range (lo, hi+1):
        if      i > mid:              a[k] = aux[j++]; j += 1  # this copying is unnecessary
        else if j > hi:               a[k] = aux[i++]; i += 1
        else if less(aux[j], aux[i]): a[k] = aux[j++]; j += 1
        else                          a[k] = aux[i++]; i += 1

    # postcondition: a[lo .. hi] is sorted
    assert isSorted(a, lo, hi)

# mergesort a[lo..hi] using auxiliary array aux[lo..hi]
def _sort(a, aux, lo, hi):
    if hi <= lo: return
    mid = lo + (hi - lo) / 2
    _sort(a, aux, lo, mid)
    _sort(a, aux, mid + 1, hi)
    _merge(a, aux, lo, mid, hi)

 #*
 # Rearranges the array in ascending order, using the natural order.
 # @param a the array to be sorted
 #/
def Sort(a):
    aux = new Comparable[len(a)]
    _sort(a, aux, 0, a.length-1)
    assert isSorted(a)


#**********************************************************************
#  Helper sorting functions
#**********************************************************************/

# is v < w ?
def _less(v, w): v < w
    
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
      hi = len(a)
    for i range(lo + 1, hi+1):
        if (_less(a[i], a[i-1])) return False
    return True


#**********************************************************************
#  Index mergesort
#**********************************************************************/
# stably merge a[lo .. mid] with a[mid+1 .. hi] using aux[lo .. hi]
def _merge(a, index, aux, lo, mid, hi):

    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = index[k]

    # merge back to a[]
    int i = lo, j = mid+1;
    for k in range(lo, hi+1):
        if      i > mid:                     index[k] = aux[j]; j += 1
        else if j > hi:                      index[k] = aux[i]; i += 1
        else if _less(a[aux[j]], a[aux[i]]): index[k] = aux[j]; j += 1
        else                                 index[k] = aux[i]; i += 1

 #*
 # Returns a permutation that gives the elements in the array in ascending order.
 # @param a the array
 # @return a permutation <tt>p[]</tt> such that <tt>a[p[0]]</tt>, <tt>a[p[1]]</tt>,
 #    ..., <tt>a[p[N-1]]</tt> are in ascending order
 #/
def indexSort(a):
    N = len(a)
    index = [None for i in range(N)]
    for i in range(N):
        index[i] = i

    aux = [None for i in range(N)]
    _sort(a, index, aux, 0, N-1)
    return index;

# mergesort a[lo..hi] using auxiliary array aux[lo..hi]
def _sort(a, index, aux, lo, hi):
    if (hi <= lo) return;
    mid = lo + (hi - lo) / 2;
    _sort(a, index, aux, lo, mid);
    _sort(a, index, aux, mid + 1, hi)
    merge(a, index, aux, lo, mid, hi)

#*
# Reads in a sequence of strings from standard input; mergesorts them; 
# and prints them to standard output in ascending order. 
#/
def main():
  import InputArgs
  a = InputArgs.getStrArray()
  Sort(a)
  print ' '.join(a)


if __name__ == '__main__':
  main()


# Copyright © 2002–2010, Robert Sedgewick and Kevin Wayne. 
# Last updated: Fri Feb 14 17:45:37 EST 2014.
