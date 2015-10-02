"Bottom-up Mergesort"""

from AlgsSedgewickWayne.utils import __lt__, _exch, _isSorted
from AlgsSedgewickWayne.Merge import merge, _add_history

def Sort(a, array_history=None): # N lg N
  """Rearranges the array, a, in ascending order, using the natural order."""
  N = len(a)
  aux = [None for i in range(N)]
  _add_history(array_history, a, aux) # Record initial state of arrays
  sarr_sz = 1
  # First nested loop is "Size of the sub-array" executed only lg N times (lg N passes)
  while sarr_sz < N: # i.e. for (int sz=1; sz<N; sz=sz+sz)
    lo = 0
    while lo < N-sarr_sz: # i.e. for (int lo = 0; lo < N-sz; lo += sz+sz)
      mid = lo + sarr_sz - 1
      hi  = min(lo + sarr_sz + sarr_sz - 1, N-1)
      merge(a, aux, lo, mid, hi)
      _add_history(array_history, a, aux, (lo, hi, mid))
      lo += sarr_sz+sarr_sz
    sarr_sz = sarr_sz+sarr_sz # Double the size of the sub-array until we get to N
  assert _isSorted(a)

#------------------------------------------------------------------------------
# 00:34 BOTTOM-UP MERGESORT: TRACE MERGE RESULTS FOR TOP-DOWN MERGESORT
#
# BASIC PLAN:
#   * Pass through array, merging subarrays of size 1.
#   * Repeat for subarrays of size 2, 4, 8, 16, ...
#
# BOTTOM LINE: No recursion needed!
#   Bottom-up Mergesort gets the job done in lg N passes.
#   Each pass uses N compares
#   For a total cost of N lg N
#
#                                    a[]
#                                             1 1 1 1 1 1
#                         0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
#                         -------------------------------
# a           lo      hi  M E R G E S O R T E X A M P L E
# size=1
# b merge(a,  0,  0,  1)  E M   .       .               .
# c merge(a,  2,  2,  3)      G R       .               .
# e merge(a,  4,  4,  5)        . E S   .               .
# f merge(a,  6,  6,  7)        .     O R               .
# i merge(a,  8,  8,  9)        .       . E T           .
# j merge(a, 10, 10, 11)        .       .     A X       .
# m merge(a, 12, 12, 13)        .       .         M P   .
# n merge(a, 14, 14, 15)        .       .             E L
# size=2
# d merge(a,  0,  1,  3)  E G M R       .               .
# g merge(a,  4,  5,  7)          E O R S               .
# k merge(a,  8,  9, 11)                . A E T X
# o merge(a, 12, 13, 15)                .         E L M P
# sz=4: 2 sub-arrays sz 8
# h merge(a,  0,  3,  7)  E E G M O R R S               .
# p merge(a,  8, 11, 15)                . A E E L M P T X
# size=8
# q merge(a,  0,  7, 15)  A E E E E G L M M O P R R S T X


#------------------------------------------------------------------------------
# QUESTION: How many passes (over the input array) does bottom-up mergesort make in the worst-case?
# ANSWER: logorithmic

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Java version Last updated: Wed Dec 4 11:48:10 EST 2013.
