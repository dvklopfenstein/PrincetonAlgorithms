
 #************************************************************************
 #  Compilation:  javac Quick.java
 #  Execution:    java Quick < input.txt
 #  Dependencies: StdOut.java StdIn.java
 #  Data files:   http:#algs4.cs.princeton.edu/23quicksort/tiny.txt
 #                http:#algs4.cs.princeton.edu/23quicksort/words3.txt
 #
 #  Sorts a sequence of strings from standard input using quicksort.
 #   
 #  % more tiny.txt
 #  S O R T E X A M P L E
 #
 #  % java Quick < tiny.txt
 #  A E E L M O P R S T X                 [ one string per line ]
 #
 #  % more words3.txt
 #  bed bug dad yes zoo ... all bad yet
 #       
 #  % java Quick < words3.txt
 #  all bad bed bug dad ... yes yet zoo    [ one string per line ]
 #
 #
 #  Remark: For a type-safe version that uses static generics, see
 #
 #    http:#algs4.cs.princeton.edu/23quicksort/QuickPedantic.java
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
# 00:49 QUICKSORT
# * Java sort for primitive types.
# * C qsort, Unix, Visual C++, Python, Matlab, Chrome JavaScript, ...

#*
#  The <tt>Quick</tt> class provides static methods for sorting an
#  array and selecting the ith smallest element in an array using quicksort.
#  <p>
#  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne
#/

# Rearranges the array in ascending order, using the natural order.
# @param a the array to be sorted
def Sort(a, array_history=None):
  import random
  random.shuffle(a)  # TBD... Really????
  _sort(a, 0, len(a) - 1)

# quicksort the subarray from a[lo] to a[hi]
def _sort(a, lo, hi):
  if hi <= lo: return;
  j = _partition(a, lo, hi)
  _sort(a, lo, j-1)
  _sort(a, j+1, hi)
  assert _isSorted(a, lo, hi)

# partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi]
# and return the index j.
def _partition(a, lo, hi):
  i = lo
  j = hi + 1
  v = a[lo]
  while True:

      # find item on lo to swap
      i += 1
      while _less(a[i], v):
          if i == hi: break
          i += 1

      # find item on hi to swap
      j -= 1
      while _less(v, a[j]):
          if j == lo: break      # redundant since a[lo] acts as sentinel
          j -= 1

      # check if pointers cross
      if i >= j: break;

      _exch(a, i, j)

  # put partitioning item v at a[j]
  _exch(a, lo, j)

  # now, a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
  return j

#*
# Rearranges the array so that a[k] contains the kth smallest key;
# a[0] through a[k-1] are less than (or equal to) a[k]; and
# a[k+1] through a[N-1] are greater than (or equal to) a[k].
# @param a the array
# @param k find the kth smallest
#/
def Select(a, k):
  import random
  if k < 0 and k >= len(a):
      raise Exception("Selected element out of bounds")
  random.shuffle(a)
  lo = 0, 
  hi = len(a) - 1
  while hi > lo:
      i = _partition(a, lo, hi)
      if   i > k: hi = i - 1
      elif i < k: lo = i + 1
      else: return a[i]
  return a[lo]



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
def _isSorted(a, lo=None, hi=None):
  if lo is None and hi is None:
    lo = 0
    hi = len(a)
  for i in range(lo + 1, hi+1):
      if _less(a[i], a[i-1]): return False
  return True


#*
# Reads in a sequence of strings from standard input; quicksorts them; 
# and prints them to standard output in ascending order. 
# Shuffles the array and then prints the strings again to
# standard output, but this time, using the select method.
#/
def main():
  import InputArgs
  import random
  ARR = InputArgs.getStrArray()
  Sort(ARR);
  print ' '.join(ARR)

  # shuffle
  random.shuffle(ARR)

  # display results again using select
  print
  print ' '.join(ARR)


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Last updated: Thu Oct 10 11:43:17 EDT 2013.G0
