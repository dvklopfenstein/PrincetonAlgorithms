#!/usr/bin/env python


#************************************************************************
# Top-Down Mergesort
#************************************************************************


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

#------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------
# 01:27 MERGESORT
# BASIC PLAN
# * Divide array into two halves.
# * **Recursively** sort each half.
# * Merge two halves.
# 
# John von Neumann credited with the invention of Mergesort.

#------------------------------------------------------------------------------
# 01:49-04:24 ABSTRACT IN-PLACE MERGE DEMO
# GOAL: Given two sorted subarrays a[lo] to a[mid] and a[mid+1] to a[hi],
#   replace with sorted subarray a[lo] to a[hi]

# 10:58 MERGESORT: TRACE
# 11:16 MERGESORT: ANIMATION

# 11:50 MERGESORT is just as fast in reverse order as in arbitrary order

#------------------------------------------------------------------------------
# 12:09 MERGESORT: EMPIRICAL ANALYSIS
# RUNNING TIME ESTIMATES:
# * Laptop executes 10^8 compares/second.
# * Supercomputer executes 10^12 compares/second.
#         _____________________________________________________________________
#         |      insertion sort (N^2)       |    mergesort (N lg(N))          |
#         |---------------------------------|---------------------------------|
# computer|thousand |  million  |  billion  |thousand |  million  |  billion  |
# :------:|:-------:|:---------:|:---------:|:-------:|:---------:|:---------:|
#   home  | instant | 2.8 hours | 317 years | instant | 1 second  |  18 min   |
#   super | instant |  1 second |   1 week  | instant |  instant  | instant   |
# 
# BOTTOM LINE: Good algorithms are better than supercomputers.

#------------------------------------------------------------------------------
# 13:15 MERGESORT: NUMBER OF COMPARES AND ARRAY ACCESSES
# PROPOSITION: Mergesort uses at most:
#     N lg N  compares and
#   6 N lg N  accesses 
# to sort any array of size N.
# 
# PROOF SKETCH: The number of compares C(N) and array accesses A(N)
# to mergesort an array of size N satisy the recurrences:
# 
#   C(N) <= C(ceiling(N/2)) + C(floor(N/2)) +   N for N > 1, with C(1)=0.
# 
#           left-half         right-half      merge
# 
#   A(N) <= A(ceiling(N/2)) + A(floor(N/2)) + 6*N for N > 1, with A(1)=0.

#------------------------------------------------------------------------------
# 15:44 WE WILL SOLVE THR RECURRENCE WITH N IS A POWER OF 2. <- results holds for all N
#
#   D(N) <= 2*D(N/2) + N, for N>1, with D(1) = 0.

#------------------------------------------------------------------------------
# 17:16 DIVIDE-AND-CONQUER RECURRENCE: PROOF BY PICTURE
# 
# PROPOSITION: Id D(N) satisfies D(N) <= 2*D(N/2) + N, for N>1, with D(1) = 0,
# then D(N) = N lg N:
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# PROOF 1: PROOF BY PICTURE [assuming N is a power of 2]
# 
#    ^                    D(N)                       N          = N
#    |    
#    |         D(N/2)             D(N/2)             2(N/2)     = N
#  lg N  
#    |     D(N/4)   D(N/4)    D(N/4)    D(N/4)       4(N/4)     = N
#    |   
#    |    |<-----------D(N/2^k)------------->|       2^k(N/2^k) = N
#    |   
#    V   D(2) D(2) D(2) D(2) D(2) D(2) D(2) D(2)     N/2(2)     = N
#                                                    ----------------
#                                                              N lg N
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 17:26 PROOF 2: PRROF BY EXPANSION
#  D(N)   = 2*D(N/2) + N                   given
#  D(N)/N = 2*D(N/2)/N    + 1              divide both sides by N
#         =   D(N/2)(N/2) + 1              algebra
#         =   D(N/4)(N/4) + 1 + 1          apply to first term
#         =   D(N/8)(N/8) + 1 + 1 + 1      apply to first term again
#         ...
#         =   D(N/N)(N/N) + 1 + 1 +...+ 1  stop applying. D(1) = 0
#         = lg(N)
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 18:20  PROOF 3: PROOF BY INDUCTION
# * Base case: N = 1
# * Inductive hypothesis: D(N) =    N*lg(N)
# * GOAL: Show that      D(2N) = (2N)*lg(2N)
# 
#   D(2*N) = 2*D(N) + 2*N            given
#          = 2*N*lg(N) + 2*N         inductive hypothesis
#          = 2*N(lg(2N) - 1) + 2*N   algebra
#          = 2*N*lg(2*N)             QED

#------------------------------------------------------------------------------
# 19:00 MERGESORT ANALYSIS: MEMORY
# PROPOSITION: Mergesort uses extra space proportional to N.
# PRROF: The array aux[] needs to be of size N for the last merge.
# 
# DEFINITION: A sorint algorithm is IN-PLACE if it uses <= c*log(N) extra memory.
# EXAMPLE: Insertion sort, selection sort, shellsort.
# 
# WAITING TO BE DISCOVERED: An in-place merge that is simple enough to be practical.

#------------------------------------------------------------------------------
# 20:37 MERGESORT: PRACTICAL IMPORVEMENTS
# USE INSERTION SORT FOR SMALL SUBARRAYS:
#   * Mergesort has too much overhead for tiny subarrays.
#   * Cuttoff to insertion sort for ~ 7 items.
# 
# 21:51 STOP IF ALREADY SORTED
# * Is biggest item in first half <= smallest item in second half?
# * Helps for partially-ordered arrays.
# 
# 22:31 ELEIMINATE THE COPY TO THE AUXILIARY ARRAY
# Mind-bending: ONly for experts
# Save time (but not space) by switching the role of the input and 
# auxiliary array in each recursive call.
# 
# QUESTION: How many compares does mergesort - the pure version without
# any optimizations - make to sort an input array that is already sorted?
# ANSWER: linearithmic
# It makes (1/2)*N*lg(N) compares, which is the best case for mergesort.
# We note that the optimized version that checks whether a[mid] <= a[mod+1]
# only requires ~N compares.


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
def _merge_init(a, aux, lo, mid, hi): # 05:00-06:00
  assert _isSorted(a, lo, mid)    # precondition: a[lo .. mid]   are sorted subarrays
  assert _isSorted(a, mid+1, hi)  # precondition: a[mid+1 .. hi] are sorted subarrays

  # copy to aux[]
  for k in range(lo, hi+1):
      aux[k] = a[k]

  # merge back to a[] in sorted order
  i = lo     # index of sorted a[lo .. mid]   ( left-half)
  j = mid+1  # index of sorted a[mid+1 .. hi] (right-half)
  for k in range(lo, hi+1): # k is current entry in the sorted result
      if   i > mid:               a[k] = aux[j]; j += 1 # this copying is unnecessary
      elif j > hi:                a[k] = aux[i]; i += 1 # j ptr is exhausted
      elif _less(aux[j], aux[i]): a[k] = aux[j]; j += 1
      else:                       a[k] = aux[i]; i += 1

  assert _isSorted(a, lo, hi) # postcondition: a[lo .. hi] is sorted

# mergesort a[lo..hi] using auxiliary array aux[lo..hi]
def _sort_init(a, aux, lo, hi): # 09:07-
  # 20:47 MERGESORT PRACTICAL IMPROVEMENTS
  # * Mergesort is too complicated for tiny arrays)
  # * Recursive nature of sort means that there will be lots of sub-arrays to be sorted.
  if hi <= lo: return
  #CUTOFF = 7
  #if hi <= lo + CUTOFF - 1:
  #  import Insertion
  #  Insertion.Sort(a, lo, hi) # Simple and efficient for small sub-arrays
  #  return

  mid = lo + (hi - lo) / 2
  _sort_init(a, aux, lo, mid)      # sort the 1st half (left)
  _sort_init(a, aux, mid + 1, hi)  # sort the 2nd half (right)
  # 21:51 IMPROVEMENT: Stop if already sorted
  # if a[mid] <= a[mid+1]: return  TBD use _less
  _merge_init(a, aux, lo, mid, hi) # merge sorted halves together

# Rearranges the array in ascending order, using the natural order.
# @param a the array to be sorted
def Sort(a, array_history=None): # 09:30
  # Do not create array in recursive _sort routine to avoid extensive 
  # cost of extra array production
  aux = [None for i in range(len(a))]
  _sort_init(a, aux, 0, len(a)-1)
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
def _isSorted(a, lo=None, hi=None):
  if lo is None and hi is None:
    lo = 0
    hi = len(a) - 1
  for i in range(lo + 1, hi+1):
    if (_less(a[i], a[i-1])): return False
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
  i = lo 
  j = mid+1
  for k in range(lo, hi+1):
    if   i > mid:                     index[k] = aux[j]; j += 1
    elif j > hi:                      index[k] = aux[i]; i += 1
    elif _less(a[aux[j]], a[aux[i]]): index[k] = aux[j]; j += 1
    else:                             index[k] = aux[i]; i += 1

# Returns a permutation that gives the elements in the array in ascending order.
# @param a the array
# @return a permutation <tt>p[]</tt> such that <tt>a[p[0]]</tt>, <tt>a[p[1]]</tt>,
#    ..., <tt>a[p[N-1]]</tt> are in ascending order
def indexSort(a):
  N = len(a)
  index = [None for i in range(N)]
  for i in range(N):
      index[i] = i

  aux = [None for i in range(N)]
  _sort(a, index, aux, 0, N-1)
  return index

# mergesort a[lo..hi] using auxiliary array aux[lo..hi]
def _sort(a, index, aux, lo, hi):
  if hi <= lo: return
  mid = lo + (hi - lo) / 2;
  _sort(a, index, aux, lo, mid)
  _sort(a, index, aux, mid + 1, hi)
  merge(a, index, aux, lo, mid, hi)

# Reads in a sequence of strings from standard input; mergesorts them; 
# and prints them to standard output in ascending order. 
def main():
  import InputArgs
  a = InputArgs.getStrArray()
  Sort(a)
  print ' '.join(a)


if __name__ == '__main__':
  main()


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Last updated: Fri Feb 14 17:45:37 EST 2014
