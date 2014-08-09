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
# 07:15 ASSERTIONS: Statement to test assumptions about your program (assert)
# * Helps detect logic bugs
# * Documents code.

#------------------------------------------------------------------------------
# 10:20 MERGESORT: TRACE MERGE RESULTS FOR TOP-DOWN MERGESORT
#
# Start with a big problem to solve (a), then 
#   divide it in half (h) and 
#   divide it in half (d) and 
#   divide it in half (b) and sort
# First thing we actually do is (b), then (c)
# 
#                                    a[]
#                                             1 1 1 1 1 1
#                         0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
#                         ------------------------------- 
# a           lo      hi  M E R G E S O R T E X A M P L E
# b merge(a,  0,  0,  1)  E M     . .                   . 
# c merge(a,  2,  2,  3)      G R . .                   .
# d merge(a,  0,  1,  3)  E G M R . .                   .
# e merge(a,  4,  4,  5)          E S                   .
# f merge(a,  6,  6,  7)              O R               .
# g merge(a,  4,  5,  7)          E O R S               .
# h merge(a,  0,  3,  7)  E E G M O R R S               .
# i merge(a,  8,  8,  9)                  E T           .
# j merge(a, 10, 10, 11)                      A X       .
# k merge(a,  8,  9, 11)                  A E T X
# m merge(a, 12, 12, 13)                          M P   .
# n merge(a, 14, 14, 15)                              E L
# o merge(a, 12, 13, 15)                          E L M P
# p merge(a,  8, 11, 15)                  A E E L M P T X
# q merge(a,  0,  7, 15)  A E E E E G L M M O P R R S T X

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
# * Was a problem that took us quadratic time using insertion sort and selection sort.
#   Now N lg N
# 
# PROOF SKETCH: The number of compares and array accesses 
#   * C(N): COMPARES
#   * A(N): ARRAY ACCESSES
# to mergesort an array of size N satisy the recurrences:
# 
#   C(N) <= C(ceiling(N/2)) + C(floor(N/2)) +   N for N > 1, with C(1)=0.
#               |                  |            |
#           left-half         right-half      merge
#               |                  |            |
#   A(N) <= A(ceiling(N/2)) + A(floor(N/2)) + 6*N for N > 1, with A(1)=0.

#------------------------------------------------------------------------------
# 15:44 WE WILL SOLVE THR RECURRENCE WITH N IS A POWER OF 2. 
# <- results holds for all N; Can proove by induction
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
#                                                    Cost of merge: 
#                                                    (where compares are)
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
# 
# TELESCOPE NOTE: 1st term on RHS(D(N/2)(N/2))
# is exactly the same as LHS(D(N)/N), so can apply same formula
#  D(N)/N = 2*D(N/2)/N    + 1              divide both sides by N
#         =   D(N/2)(N/2) + 1              algebra

#  PROOF:
#
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
# We need auxiliary array for the last merge
#
# PROOF: The array aux[] needs to be of size N for the last merge.
# 
# DEFINITION: A sorting algorithm is IN-PLACE if it uses <= c*log(N) extra memory.
# EXAMPLE: Insertion sort, selection sort, shellsort.
# 
# WAITING TO BE DISCOVERED: An IN-PLACE MERGE that is simple enough to be practical.

#------------------------------------------------------------------------------
# 20:37 MERGESORT: PRACTICAL IMPROVEMENTS
#
# TECHNIQUE 1: USE INSERTION SORT FOR SMALL SUBARRAYS: (~20% faster)
#   * Mergesort has too much overhead for tiny subarrays.
#   * Cuttoff to insertion sort for ~ 7 items.
# 
# TECHNIQUE 2:  21:51 STOP IF ALREADY SORTED
# * Is biggest item in first half <= smallest item in second half?
# * Helps for partially-ordered arrays.
# 
# TECHNIQUE 3: 22:31 ELIMINATE THE COPY TO THE AUXILIARY ARRAY
# Mind-bending: ONly for experts
# Save time (but not space) by switching the role of the input and 
# auxiliary array in each recursive call.
# 
# QUESTION: How many compares does mergesort - the pure version without
# any optimizations - make to sort an input array that is already sorted?
# ANSWER: linearithmic
# It makes ~(1/2)*N*lg(N) compares, which is the best case for mergesort.
# We note that the optimized version that checks whether a[mid] <= a[mod+1]
# only requires ~N compares.


########################################################
### Stability (Week 3 Lecture "Stability")
########################################################
# 
#-------------------------------------------------------
# 05:00 PROPOSITION: Merge operation IS STABLE.
# 
# PROOF: Takes from left subarray if equal keys.
#


########################################################
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
  # Expect that left-half is sorted.
  # Expect that right-half is sorted.
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

  # Expect that now the entire list is sorted.
  assert _isSorted(a, lo, hi) # postcondition: a[lo .. hi] is sorted


# mergesort a[lo..hi] using auxiliary array aux[lo..hi]
def _sort_init(a, aux, lo, hi): # 09:07-
  # 20:47 MERGESORT PRACTICAL IMPROVEMENTS (**SEE MergeX.py for code containing improvements)
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
  # if a[mid] <= a[mid+1]: return  TBD use "less"
  _merge_init(a, aux, lo, mid, hi) # merge sorted halves together

# Rearranges the array in ascending order, using the natural order.
# @param a the array to be sorted
def Sort(a, array_history=None): # 09:30
  # NOTE: Do not create array in recursive _sort routine 
  # to avoid extensive cost of extra array production
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

  # Maintain 3 variables:
  #   i: Current entry on left-half
  #   j: Current entry on left-half
  #   k: Current entry in the sorted result

  # merge back to a[]
  i = lo     # Start LEFT-HAND-POINTER  at left-most side of Left-sided  list
  j = mid+1  # Start RIGHT-HAND-POINTER at left-most side of Right-sided list
  for k in range(lo, hi+1):
    # If left-half list has been completely examined
    if   i > mid:                     index[k] = aux[j]; j += 1
    # If right-half list has been completely examined
    elif j > hi:                      index[k] = aux[i]; i += 1
    # If current value at right-half < current value at right-half, copy smaller val.
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
  a = InputArgs.getStrArray("S O R T E X A M P L E")
  Sort(a)
  print ' '.join(map(str,a))


if __name__ == '__main__':
  main()


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Based on java which was Last updated: Fri Feb 14 17:45:37 EST 2014
