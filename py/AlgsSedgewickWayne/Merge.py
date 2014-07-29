
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

# 00:11
# MERGESORT: ONE OF TWO CLASSIC SORTING ALGORITHMS
# CRITICAL COMPONENTS IN THE WORLD'S COMPUTATIONAL INFRASTRUCTURE.A
# * Full scientific understanding of their propoerties has enables us
#   to develop them into practical system sorts.
# * Quicksort honored as one of top 1 algorithms of 20th century
#   in science and engineering.
# 
# 00:39 MERGESORT
# * Java sort for objects.
# * Perl, C++ stable sort, Python stable sort, Firefox JavaScript, ...

# 01:27 MERGESORT
# BASIC PLAN
# * Divide array into two halves.
# * **Recursively** sort each half.
# * Merge two halves.
# 
# John von Neumann credited with the invention of Mergesort.

# 01:49-04:24 ABSTRACT IN-PLACE MERGE DEMO
# GOAL: Given two sorted subarrays a[lo] to a[mid] and a[mid+1] to a[hi],
#   replace with sorted subarray a[lo] to a[hi]

# 10:58 MERGESORT: TRACE
# 11:16 MERGESORT: ANNIMATE

# 11:50 MERGESORT is just as fast in reverse order as in arbitrary order



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
def _merge(a, aux, lo, mid, hi): # 05:00-06:00

   assert _isSorted(a, lo, mid)    # precondition: a[lo .. mid]   are sorted subarrays
   assert _isSorted(a, mid+1, hi)  # precondition: a[mid+1 .. hi] are sorted subarrays

   # copy to aux[]
   for k in range(lo, hi+1):
       aux[k] = a[k]

   # merge back to a[] in sorted order
   i = lo     # index of sorted a[lo .. mid]   ( left-half)
   j = mid+1  # index of sorted a[mid+1 .. hi] (right-half)
   for k in range(lo, hi+1): # k is current entry in the sorted result
       if      i > mid:              a[k] = aux[j]; j += 1 # this copying is unnecessary
       else if j > hi:               a[k] = aux[i]; i += 1 # j ptr is exhausted
       else if less(aux[j], aux[i]): a[k] = aux[j]; j += 1
       else                          a[k] = aux[i]; i += 1

   assert _isSorted(a, lo, hi) # postcondition: a[lo .. hi] is sorted

# mergesort a[lo..hi] using auxiliary array aux[lo..hi]
def _sort(a, aux, lo, hi): # 09:07-
    if hi <= lo: return
    mid = lo + (hi - lo) / 2
    _sort(a, aux, lo, mid)      # sort the 1st half (left)
    _sort(a, aux, mid + 1, hi)  # sort the 2nd half (right)
    _merge(a, aux, lo, mid, hi) # merge sorted halves together

# Rearranges the array in ascending order, using the natural order.
# @param a the array to be sorted
def Sort(a): # 09:30
    # Do not create array in recursive _sort routine to avoid extensive cost of extra array production
    aux = new Comparable[len(a)]
    _sort(a, aux, 0, a.length-1)
    assert _isSorted(a)


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
