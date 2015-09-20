"""Shell Sort"""

import sys
from AlgsSedgewickWayne.utils import _isSorted, __lt__, _exch

def Sort(ARR, array_history=None, sort_seq=None):
  """Rearranges the array, ARR, in ascending order, using the natural order."""
  # array_history; Used in tests. When true prints ASCII Art demonstrating the sort
  N = len(ARR)

  # 3x+1 increment sequence:  [1, 4, 13, 40, 121, 364, 1093, ...
  ha = get_sort_seq(N, sort_seq)
  print ha

  for h in reversed(ha):
    # h-sort the array (insertion sort)
    for i in range(h,N):
      j = i
      while j >= h and __lt__(ARR[j], ARR[j-h]):
        if array_history is not None:
          array_history.add_history(ARR, {j:'*', j-h:'*'} )
        _exch(ARR, j, j-h)
        j -= h
    assert _isHsorted(ARR, h)
  assert _isSorted(ARR)
  if array_history is not None:
    array_history.add_history(ARR, None)



def _isHsorted(a, h):
  """is the array h-sorted?"""
  for i in range(h,len(a)):
    if __lt__(a[i], a[i-h]): 
      return False
  return True

def get_sort_seq(N, sort_seq=None):
  """Get sort sequence."""
  if sort_seq is None:
    # Use 3x+1 increment sequence
    ha = [1]
    while (ha[-1] < N/3):
      ha.append(3*ha[-1] + 1)
    return ha
  return sort_seq # Use user-provided sequence

##########################################################################
# Alg1 Week 2 Lecture Shellsort
##########################################################################
#
# SHELLSORT OVERVIEW
# 00:21 Insertion sort is inefficient because elements only move one
# element at a time, even though we know that they have a long way to go.
#
# 00:27 The idea behind Shell sort is we will move entries several entries
# at a time using an h-sorted array.
#   An h-sorted array is h interleaved sorted subsequences.
#
# SHELLSORT [Shell 1959] h-sort for decreasing sequence of values of h.
#
# 01:44 H-SORTING 01:44-02:22
# How to h-sort an array? Insertion sort, with stride length h.
#
# 02:38 WHY INSERTION SORT?
#   * Big increments   => small subarray
#   * Small increments => array is big, but nearly in order (so fast using insertion sort).
#
# 04:58 SHELLSORT: INTUITION
# PROPOSITION: A g-sorted array remains g-sorted after h-sorting it.
# CHALLENGE:   Prove this fact--it's more subtle than you'd think!
# Each element moves only a little bit; how Shellsort gains its efficiency
#
# 05:31 SHELLSORT: WHICH INCREMENT SEQUENCE TO USE?
# We will use 3x+1 (Knuth's choice in the 1960s)
# Finding the best increment sequence is an open research area.

# 08:35 SHELLSORT: ANALYSIS
# The analysis of Shellsort is still open.
#
# PROPOSITION: The worst-case number of compares used by shellsort with
# the 3x+1 increments is O(N^(3/2)).  In practice, it is much less than that.
#
# 08:55 PROPERTY: Number of compares used by shellsort with the 3x+1
# increments is at most by a small multiple of N times the number of increments used.
#
#  |    N   | cmp  |N^1.289|2.5*N*lg(N)
#  ---------+------+-------+------+
#  |  5,000 |   93 |    58 |  106 |
#  | 10,000 |  209 |   143 |  230 |
#  | 20,000 |  467 |   349 |  495 |
#  | 40,000 | 1022 |   855 | 1059 |
#  | 80,000 | 2266 |  2089 | 2257 |
#
# REMARK: Accurate model has not yet been discovered (!)

# 09:23 WHY ARE WE INTERESTED IN SHELLSORT?
# Example of simple idea leading to substantial performance gains.
#
# USEFUL IN PRACTICE:
# * FAST unless array size is huge.
# * Tiny, fixed footprint for code (used in embedded systems).
# * Hardware sort prototype
#
# 09:52 LEADS TO A LOT OF INTERESTING QUESTIONS (Intellectual Challenge):
# Simple algorithm, nontrivial performance, interesting questions.
# * Asymptotic growth rate?
# * Best sequence of increments?
#   Open problem: find a better increment sequence
# * Average-case performance?
#
# LESSON: Some good algorithms are still waiting discovery (special inc seq?)

# QUESTION: How many compares does shellsort (using the 3x+1 increment
# sequence) make on an input array that is *already sorted?
# ANSWER: linearithmic (look at table above)
# EXPLANATION: Since successive increment values of h differ by at least a
# a factor of 3, there are ~log_3(N) increment values. For each increment
# value h, the array is already h-sorted so it will make ~ N compares.

# QUESTION: The number of compares to Shellsort (with Knuth's 3x+1
# increments) a sorted array of N distinct keys is ~ N log_3 N.
# ANSWER(False): Each pass uses approximately N compares.
# There are ~ log_3 N passes because the increments go up by
# (roughly) a factor of 3

# QUESTION: The number of compares to Shellsort (with Knuth's 3x+1 increments) 
# an array of length N depends only on N (and not on the items in the array).
# ANSWER: False. The number of compares to Shellsort the array { 1, 2, 3 } is 2; 
# the number of compares to Shellsort the array { 3, 2, 1 } is three.

# QUESTION: An array of N distinct keys that is both 2-sorted and 3-sorted 
# can be 1-sorted in one insertion-sort pass, using only N compares.
# ANSWER: True. Since the array is 2- and 3-sorted, it is also k-sorted 
# for every k >= 2. Thus, while an item can be larger than the item to 
# its immediate right, it cannot be larger than the item k to
# its right for any k >= 2.


########################################################
### Stability (Week 3 Lecture "Stability")
########################################################
#
#-------------------------------------------------------
# 04:41 PROPOSITION: Shellsort IS NOT stable.
#
# NOTE ON TABLE BELOW: Items depicted as A1 and A2 in the example
# below have the same key, "A".  The 1 and 2 following the "A"
# are denote that A1 was 1st and A2 was 2nd.
#
# PROOF BY COUNTEREXAMPLE: Long distance exchange might move
# an item past some equal item.
#
#
# NOTE: if "__lt__" in the "Sort" routine were "less than or equal to",
# it would not work.
#

#  h    0   1   2   3   4
# -----------------------
#      B1  B2  B3  B4  A1
#  4  >A1  B2  B3  B4 >B1
#  1   A1  B2  B3  B4  B1
#      A1  B2  B3  B4  B1
#

#************************************************************************
#  Compilation:  javac Shell.java
#  Execution:    java Shell < input.txt
#  Dependencies: StdOut.java StdIn.java
#  Data files:   http:#algs4.cs.princeton.edu/21sort/tiny.txt
#                http:#algs4.cs.princeton.edu/21sort/words3.txt
#
#  Sorts a sequence of strings from standard input using shellsort.
#
#  Uses increment sequence proposed by Sedgewick and Incerpi.
#  The nth element of the sequence is the smallest integer >= 2.5^n
#  that is relatively prime to all previous terms in the sequence.
#  For example, incs[4] is 41 because 2.5^4 = 39.0625 and 41 is
#  the next integer that is relatively prime to 3, 7, and 16.
#
#  % more tiny.txt
#  S O R T E X A M P L E
#
#  % java Shell < tiny.txt
#  A E E L M O P R S T X                 [ one string per line ]
#
#  % more words3.txt
#  bed bug dad yes zoo ... all bad yet
#
#  % java Shell < words3.txt
#  all bad bed bug dad ... yes yet zoo    [ one string per line ]
#
#
#************************************************************************/

#*
#  The <tt>Shell</tt> class provides static methods for sorting an
#  array using Shellsort with Knuth's increment sequence (1, 4, 13, 40, ...).
#  <p>
#  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne
#/

