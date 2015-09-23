"""Speed up quicksort in the presence of duplicate keys."""

import random

def Sort(a, array_history=None):
"""Rearranges the array, a, in ascending order, using the natural order."""
  random.shuffle(a)
  _sort(a, 0, len(a) - 1)
  assert _isSorted(a)

def _sort(a, lo, hi):
"""quicksort the subarray a[lo .. hi] using 3-way partitioning."""
  if hi <= lo: 
    return
  lt = lo
  gt = hi
  v  = a[lo]
  i  = lo
  while (i <= gt):
    if a[i] < v:
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


# def main(String[] args):
#     String[] a = StdIn.readAllStrings()
#     Quick3way.sort(a)
#     show(a)

#######################################################################
# Duplicate Keys (11:25) Algs 1, Week 3
#######################################################################

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

# QUESTION: Why does Array.sort() in Java use mergesort instead of 
# quicksort when sorting reference types?
#   YES stability
#       N log N guaranteed perfoormance
#   YES both A and B
#       neither A and B

# WAR STORY (C QSORT FUNCTION)
# AT&T Bell Labs (1991). Allan Wilks and Rick Becker discovered that a
# qsort() call that should have taken a few minutes was consuming 
# hours of CPU time.
#
# At the time, almost all qsort() implementations based on those in:
# * Version 7 Unix (1979): quadratic time to sort organ-pipe arrays.
# * BSD Unix (1983): quadratic time to sort random arrays of 0s and 1s.

# Selection   X   N^2/2     N^2/2    N^2/2  N exchanges
# Insertion   X X N^2/2     N^2/4        N  use for small N or partially ordered
# Shell       X       ?         ?        N  tight code, subquadratic
# Merge         X N lg N   N lg N   N lg N  N lg N guarantee, stable
# Quick       X   N^2/2   2N ln N   N lg N  N lg N probabilistic guarantee, fastest in practice
# 3-way quick X   N^2/2   2N ln N        N  better w/duplicate keys
# ???         X X N lg N   N lg N   N lg N  holy sorting grail

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Last updated: Tue Sep 24 11:52:34 EDT 2013.
