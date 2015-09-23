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

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Last updated: Tue Sep 24 11:52:34 EDT 2013.
