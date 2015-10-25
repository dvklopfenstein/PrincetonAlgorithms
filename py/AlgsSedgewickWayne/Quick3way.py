"""Speed up quicksort in the presence of duplicate keys."""

import random
import collections as cx

def Sort(a, array_history=None, shuffle=True):
  """Rearranges the array, a, in ascending order, using the natural order."""
  if shuffle: # Make shuffle optional to better visualize while learning
    random.shuffle(a)
  _sort(a, 0, len(a) - 1, array_history)
  assert _isSorted(a)
  if array_history is not None: _add_history(array_history, a) # For visualization

def _sort(a, lo, hi, array_history):
  """quicksort the subarray a[lo .. hi] using 3-way partitioning."""
  if hi <= lo: 
    return
  lt = lo
  gt = hi
  v  = a[lo]
  i  = lo
  while (i <= gt):
    if a[i] < v:
      if array_history is not None: _add_history(array_history, a, (lt, gt, i))
      _exch(a, lt, i)
      lt += 1
      i  += 1
    elif a[i] > v:
      if array_history is not None: _add_history(array_history, a, (lt, gt, i))
      _exch(a, i, gt)
      gt -= 1
    else: i += 1

  # a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi].
  _sort(a, lo, lt-1, array_history)
  _sort(a, gt+1, hi, array_history)
  assert _isSorted(a, lo, hi)




#**********************************************************************
#  Helper sorting functions
#**********************************************************************/
def _less(v, w): return v < w
def _eq(v, w): return v == w
def _exch(a, i, j): a[i], a[j] = a[j], a[i]

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


def _add_history(array_history, a, anno=None):
  """For visualizing array history."""
  if array_history is not None: 
    anno_a = None
    if anno is not None:
      lt, gt, i = anno
      anno_a = cx.OrderedDict([(lt, '-'), (gt, '+'), (i, '>')])
    array_history.add_history(a, anno_a, name="arr")

#######################################################################
# Duplicate Keys (11:25) Algs 1, Week 3
#######################################################################

# WITH DUPLICATE KEYS:
# Mergesort: Always between 1/2 N lg N and N lg N compares
# Quicksort: Goes QUADRATIC unless partitioning stops on equal keys!

# DUPLICATE KEYS: THE PROBLEM
# MISTAKE: Put all items equal to the partitioning item on one side
# CONSEQUENCE: ~ 1/2 N^2 compares when all keys equal.
#                *                            *
#  B A A B A B B B C C C  A A A A A A A A A A A
#
# RECOMMENDED: Stop scans on items euql to the partitioning item.
# CONSEQUENCE: ~N lg N compares when all keys equal.
#             *                     *
#  B A A B A B C C B C B  A A A A A A A A A A A
#
# DESIRABLE: Put all items equal to the partitioning item in place.
#        * * * * *        * * * * * * * * * * *
#  A A A B B B B B C C C  A A A A A A A A A A A

# 3-WAY PARTITIONING 03:25
# GOAL: Partition array into 3 parts so that:
#   * Entries between lt and gt equal to partition item v
#   * No larger entries to the left of lt
#   * No smaller entries to the right of gt
#          _________________________________
#   before |v|___________________________|_|
#           |                             |
#           lo                            hi
#
#          _________________________________
#   after  |___<v______|____=v____|___>v___|
#           |           |        |        |
#           lo          lt       gt       hi
#
# DUTCH NATIONAL FLAG PROBLEM. [Edsger Dijkstra]
#   * Conventional wisdon until mid 1990s: not worth doing (putting all keys together)
#   * New approach discovered when fixing mistake in C library qsort()
#   * Now incorporated into qsort() and Java system sort.

#          _______________________________________
#   after  |___<v______|_=v__|XXXXXXXXXX|___>v___|
#           |           |     |        |        |
#           lo          lt    i        gt       hi
#
# INVARIANTS:
# * Everything to the right of gt is greater than the partitioning element
# * Everything to the left  of lt is less    than the partitioning element
# * Everything between lt and i   is equal   to   the partitioning element
# * Everything between  i and gt  has not yet been seen

# QUESTION: Using a 3-way partitioning with quicksort is most effective
# when the input has which of the following properties?
#   NO  all items distinct
#   YES a few distinct items
#   NO  items in strictly increasing order
#   NO  items in strictly decreasing orer

#######################################################################
# System Sorts (11:50) Algs 1, Week 3
#######################################################################
# Sorting algorithms are essential in a broad variety of applications:
#   Obvious Applications:
#     * Sort a list of names.
#     * Organize a MP3 library.
#     * Display Google PageRank results.
#     * List RSS feed in reverse chronological order.
#   Problems become easy once items are sorted
#     * Find the median
#     * Binary search in a database
#     * Identify statistical outliers.
#     * Find duplicates in a mailing list.
#   Non-obvious applications
#     * Data compression.
#     * Computer graphics.
#     * Computational biology.
#     * Load balancing on a parallel computer.

# Java Arrays.sort uses:
# Mergesort for objects (because maybe space is not an issue)
# Quicksort for primitive types (because maybe performance is most important)

# QUESTION: Why does Array.sort() in Java use mergesort instead of 
# quicksort when sorting reference types?
#   YES stability
#       N log N guaranteed perfoormance
#   YES both A and B
#       neither A and B
# EXPLANATION: The Java API for Arrays.sort() for reference types 
# requires that it is stable and that it offers guaranteed N log N performance.
# Neither of these are properties of standard quicksort.

# WAR STORY (C QSORT FUNCTION) 03:57
# AT&T Bell Labs (1991). Allan Wilks and Rick Becker discovered that a
# qsort() call that should have taken a few minutes was consuming 
# hours of CPU time. QUADRATIC
#
# At the time, almost all qsort() implementations based on those in:
# * Version 7 Unix (1979): quadratic time to sort organ-pipe arrays.
# * BSD Unix (1983): quadratic time to sort random arrays of 0s and 1s.

# Sedgewick & Wayne have killer input for Java sort(250000.txt) which will cause 
# it to run in quadratic time.

# APPLICATIONS HAVE DIVERSE ATTRIBUTES: 09:07
#   * Stable?
#   * Parallel?
#   * Deterministic?
#   * Keys all distict?
#   * Multiple key types?
#   * Linked list or arrays?
#   * Large or small items?
#   * Is your array randomly ordered?
#   * Need guaranteed performance?
#
# QUESTION: Is the system sort good enough?
# ANSWER: Usually


# SORTING SUMMARY: I=inplace, S=stable
#             I S worst   average    best   remarks
#             - - -----   -------    ----   --------------------
# Selection   X   N^2/2     N^2/2    N^2/2  N exchanges
# Insertion   X X N^2/2     N^2/4        N  use for small N or partially ordered
# Shell       X       ?         ?        N  tight code, subquadratic
# Merge         X N lg N   N lg N   N lg N  N lg N guarantee, stable
# Quick       X   N^2/2   2N ln N   N lg N  N lg N probabilistic guarantee, fastest in practice
# 3-way quick X   N^2/2   2N ln N        N  better w/duplicate keys
# ???         X X N lg N   N lg N   N lg N  holy sorting grail

# TRUE: Given an array of N items and a parititoning item, it is straightforward 
# to *stably* 3-way partition the array using only a linear number of compares 
# and an auxiliary array of length N.
# EXPLANATION: Copy the items to the auxiliary array; count the number of items 
# { less than, equal to, greater than } the partitioning item; scan through 
# the array from left-to-right, and copy the items back to the original array 
# using the counts to identify their locations.
# ???WHY STABLE???

# TRUE: The number of compares to 3-way quicksort an array of N equal keys is ~ N.
# EXPLANATION: The sort is complete after the first partitioning step.

# TRUE: The primary advantage of 3-way quicksort (over standard quicksort) 
# is improved performance when the array has many items with equal keys.
# EXPLANTION: 3-way quicksort makes a linear number of compares in cases 
# where the standard version of quicksort makes a linearithmic number 
# of compares ,e.g., N equal keys.

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Last updated: Tue Sep 24 11:52:34 EDT 2013.
