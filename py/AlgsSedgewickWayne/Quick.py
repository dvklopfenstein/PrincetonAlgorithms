"""Quicksort"""

import random
import collections as cx

def Sort(a, array_history=None):
  _add_history(array_history, a) # Record initial state of array
  random.shuffle(a)  # Needed to ensure performance will be good. 05:56
  _sort(a, 0, len(a) - 1, array_history)

def _sort(a, lo, hi, array_history):
  """quicksort the subarray from a[lo] to a[hi]."""
  if hi <= lo: return;
  j = _partition(a, lo, hi)
  _add_history(array_history, a, (lo, hi))
  _sort(a, lo, j-1, array_history)
  _sort(a, j+1, hi, array_history)
  assert _isSorted(a, lo, hi)

def _partition(a, lo, hi, array_history=None):
  """partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi]"""
  # and return the index j.
  i = lo
  j = hi + 1
  v = a[lo]
  while True:

      # find item on lo to swap
      i += 1
      while _less(a[i], v):
          if i == hi: break
          i += 1 # Increment i as long it is pointing to val < v

      # find item on hi to swap
      j -= 1
      while _less(v, a[j]):
          if j == lo: break   # redundant since a[lo] acts as sentinel
          j -= 1 # Decrement j as long as it is pointing to va > v

      # check if pointers cross
      if i >= j: break;
      if array_history is not None: _add_history(array_history, a, (i, j))
      _exch(a, i, j)

  # put partitioning item v at a[j]
  if array_history is not None: _add_history(array_history, a, (i, j))
  _exch(a, lo, j)
  if array_history is not None: _add_history(array_history, a, (i, j))

  # now, a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
  # j now points to partitioning element, after it has moved to its new spot
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




def _add_history(array_history, a, anno=None):
  """For visualizing array history."""
  if array_history is not None: 
    anno_a = None
    if anno is not None:
      lo, hi = anno
      anno_a = cx.OrderedDict([(lo, '-'), (hi, '+')])
    array_history.add_history(a,   anno_a, name="arr")

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


########################################################
### Stability (Alg 1, Week 3 Lecture)
########################################################
# QUICK SORT IS AN EFFICIENT, BUT UNSTABLE, SORTING ALGORITHM.
# (From Week 3 "Stability" Lecture 05:33)
#
# 05:33 QUESTION: Given an array of points, which of the following
# approaches would be **least useful** for removing duplicate points?
# Assume the point data type has the following three orders:
#  * A natural order that compares by x-coord and breaks ties by y-coord
#  * One comparator that compares by x-coord
#  * One comparator that compares by y-coord
# ANSWER: mergesort by x-coordinate, quicksort by y-coordinate.
#    NO: quicksort by the natural order
#    NO: quicksort by x-coordinate; mergesort by y-coordinate
#    NO: mergesort by x-coordinate; mergesort by y-coordinate
# EXPLANATION: Since quicksort is not stable, if you mergesort by x-coord
# and then quicksort by y-coord, there is no guarantee that equal points
# will be adjacent in the sorted order.
#

########################################################
### Quicksort (Alg 1, Week 3 Lecture)
########################################################
# Quicksort is named as one of the most important algorihms in the 20th century.
# Invented in 1961 by Tony Hoare:
#   Sir Charles Antony Richard Hoare, 1980 Turing Award
#
#-------------------------------------------------------
# INVARIANT: Nothing to the left  of i is greater than a[lo] (partitioning element)
# INVARIANT: Nothing to the right of j is greater than a[lo] (partitioning element)
#-------------------------------------------------------
# QUICKSORT:
# A recursive method, like Mergesort.
# Quicksort does the recursion AFTER  it does the work.
# Mergesort does the recursion BEFORE it does the work.
#
# BASIC PLAN:
# * SHUFFLE the array randomly.
# * PARTITION so that for some j
#   * entry a[j] is in place
#   * no larger entry to the left of j
#   * no smaller entry to the right of j
# * SORT each piece recursively.
#
# INPUT      Q  U  I  C  K  S  O  R  T  E  X  A  M  P  L  E
# SHUFFLE    K  R  A  T  E  L  E  P  U  I  M  Q  C  X  O  S
#            |
#            +--------------+
#                           |
# PARTITION  E  C  A  I  E  K  L  P  U  T  M  Q  R  X  O  S
#            |<-- < K -->|     |<------- > K ------------>|
#
# SORT LEFT  A  C  E  E  I
# SORT RIGHT                   L  M  O  P  Q  R  S  T  U  X
# RESULT     A  C  E  E  I  K  L  M  O  P  Q  R  S  T  U  X
#
#-------------------------------------------------------
# 01:44-04:20 QUICKSORT PARTITIONING DEMO
#-------------------------------------------------------
# 06:24-7:00 QUICKSORT TRACE
#                                             1 1 1 1 1 1
#             lo  j   hi  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
#             ----------  -------------------------------
# INITIAL VALUES          Q U I C K S O R T E X A M P L E
# RANDOM SHUFFLE          K R A T E L E P U I M Q C X O S
#             0   5  15   E C A I E(K)L P U T M Q R X O S
#             0   3   4   E C A(E)I
#             0   2   2   A C(E)                        .
#             0   0   1  (A)C                           .
#          *  1       1    (C)                          .
#          *  1       4           (I)                   .
#             6   6  15              (L) P U T M Q R X O S
#             7   9  15                 M(O)P T Q R X U S
#             7   7   8                (M)O
#          *  8       8                  (O)
#            10  13  15                       S Q R(T)U X
#            10  12  12                       R Q(S)
#            10  11  11                       Q(R)
#          * 10      10                      (Q)
#            14  14  15                              (U)X
#          * 15      15                                (X)
# RESULT                  A C E E I K L M O P Q R S T U X
#
#  *  There is no partition for subarrays of size 1
# ( ) Identifies "partition element"
#
#-------------------------------------------------------
# 07:00-07:29 QUICKSORT ANIMATION
#-------------------------------------------------------
# 07:29-09:16 QUICKSORT IMPLEMENTATION DETAILS
#
# PARTITIONING IN-PLACE: Using an extra array makes partitioning easier
# (and stable), but is not worth the cost.  Quicksort's advantage
# over mergesort is sorting in place.
#
# TERMINATING THE LOOP: Testing whether the pointers cross is
# a bit trickier that it might seem, particularly w/duplicate keys.
#
# STAYING IN BOUNDS: The (j == lo) test is redundant:
#   partitioning element will stop the loop.
# The (i == hi) test is not redundant.
#
# PRESERVING RANDOMNESS: Shuffling is needed for performance guarantee.
# The two sub-arrays will remain random;y sorted.
#
# EQUAL KEYS: When duplicates are present, it is (counter-intuitively)
# better to stop on keys equal to the partitioning item's key.
#
#-------------------------------------------------------
# 09:40 MERGESORT: EMPIRICAL ANALYSIS
#
# RUNNING TIME ESTIMATES:
# * Laptop executes 10^8 compares/second.
# * Supercomputer executes 10^12 compares/second.
#         _______________________________________________________________________________________________________
#         |      insertion sort (N^2)       |    mergesort (N lg(N))          |    quicksort (N lg(N))          |
#         |---------------------------------|---------------------------------|---------------------------------|
# computer|thousand |  million  |  billion  |thousand |  million  |  billion  |thousand |  million  |  billion  |
# :------:|:-------:|:---------:|:---------:|:-------:|:---------:|:---------:|:-------:|:---------:|:---------:|
#   home  | instant | 2.8 hours | 317 years | instant | 1 second  |  18 min   | instant | 0.6 sec   |  12 min   |
#   super | instant |  1 second |   1 week  | instant |  instant  | instant   | instant |  instant  | instant   |
#
# LESSON 1: Good algorithms are better than supercomputers.
# LESSON 2: Great algorithms are better tha good ones.

#-------------------------------------------------------
# 10:25 QUICKSORT: BEST-CASE ANAYSIS
#
# Number of compares:
#   BEST  CASE:  ~N lg N  compares
#   WORST CASE: ~ 1/2 N^2 Random shufle puts items exactly in order
#
#-------------------------------------------------------
# 10:25 QUICKSORT: AVERAGE-CASE ANAYSIS
#
# 11:16 PROPOSITION: The average number of compares C(N) to quicksort
# an array of N distict keys is ~2N ln N (and the number of exchanges
# is ~ 1/3 N ln N
#
# PROOF: C(N) satisfies the recurrenc C(0)=C(1)=0 for N >= 2:
#      partitioning                  left    right
#           |                         |      |
# C(N) = (N + 1) + /C(0) + C(N-1)\ + /C(1) + C(N-2)\ + ... + /C(N-1) + C(0)\
#                 (---------------) (---------------)       (---------------)
#                  \     N       /   \     N       /         \       N     /
#
# * Multiply both sides by N and collect terms:
#
#     N*C(N) = N(N+1) + 2(C(0) + C(1) + ... + C(N-1))
#
# * Subtract this from the same equatoin for N-1:
#
#     N*C(N) - (N-1)*C(N-1) = 2*N + 2*C(N-1)
#
# * Rearrange the terms and divide by N(N+1) (kind of a magic step):
#
#       C(N)    C(N-1)     2        (Eq A)
#      ----- =  ------ + -----
#      N + 1      N      N + 1
#
# * 13:38 Repeatedly apply Eq A (equation telescopes):
#
#               C(N-2)     2       2
#            =  ------ + ----- + -----  <- subst. prev eq. (Eq A)
#                N - 1     N     N + 1
#
#               C(N-3)     2       2       2
#            =  ------ + ----- + ----- + -----
#                N - 2   N - 1     N     N + 1
#
#               2   2   2           2
#            =  - + - + - + ... + -----
#               3   4   5         N + 1
#
# * 13:49 Approximate sum by an integral:
#
#                     / 1   1   1         1  \
#       C(N) = 2(N+1)(  - + - + - + ... ----- )
#                     \ 3   4   5       N + 1/
#
#                          N+1 / 1    \
#            ~ 2(N+1)*integral(  - dx  )
#                            3 \ x    /
#
# * 14:05 Finally, the desired result AVERAGE NUMBER OF COMPARISONS:
#
#      C(N) = 2(N+1)*ln(N) ~ 1.39 N lg N

#-------------------------------------------------------
# 15:12 QUICKSORT: SUMMARY OF PERFORMANCE CHARACTERISTICS
#
# WORST CASE: Number of compares is quadratic
#   * N + (N-1) + (N-2) +...+ 1 ~ 1/2 N^2
#   * More likely that your computer is struck by lightening bolt.
#
# AVERAGE CASE: Number of compares is ~ 1.39 N lg N
#   * 39% more compares than mergesort.
#   * BUT faster than mergesort in practice because of less data movement.
#
# RANDOM SHUFFLE:
#   * Probabilistic guarantee agaist worst case.
#   * Basis for math model that caan be validated with experiments.
#
# CAVEAT EMPTOR: Many textbook implementations go QUADRATIC if array:
#   * Is sorted or reverse sorted.
#   * Has many duplicates (even if randomized!)

#-------------------------------------------------------
# 16:25 QUICKSORT PROPERTIES
#
# PROPOSITION: Quicksort is an IN-PLACE sorting algorithm.
#
# PROOF:
# * Partitioning: constant extra space.
# * Deph of recursion: logarithmic exra space (with high probability)
#   ** Can guarantee logarithmic depth by recurring on
#      smaller subarray before larger subarray.
#      Not really necessary no-a-days if you do the random shuffle.

#-------------------------------------------------------
# 17:24 QUICKSORT: PRACTICAL IMPROVEMENTS
#
# INSERTION SORT SMALL SUBARRAYS (Improves running time 10%-20%)
# * Even quicksort has too much overhead for tiny subarrays.
# * Cutoff o insertion sort for ~ 10 items
# * NOTE: Could delay insertion sort until one pass at end.
#
# 18:22 MEDIAN OF SAMPLE:
# * Best choice of pivot item = median
# * Estimate true median by taking median of sample.
# * Median-of-3 (random) items.
#                 ~ 12/7  N ln N compares  (slightly fewer)
#                 ~ 12/35 N ln N exchanges (slightly more)
#

#-------------------------------------------------------
# QUESTION: What is the expected running time of randomized quicksort
#   when the input is already sorted?
# ANSWER: linearithmic
# EXPLANATIN: Without the shuffle, quicksorting an array of N distict
# keys is quadratic.  That's one reason why it's important to 
# shuffle the array.


########################################################
### Duplicate Keys (Alg 1, Week 3 Lecture)
########################################################
#
# QUICKSORT WITH DUPLICATE KEYS:
# * Algorithm goes quadratic unless partitioning stops on equal keys!
# * 1990s C user found this defect in qsort()
#   (Several textbook and system implementations also have this defect)
#


# #************************************************************************/
# #  The <tt>Quick</tt> class provides static methods for sorting an
# #  array and selecting the ith smallest element in an array using quicksort.
#  <p>
#  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne
#/

# Rearranges the array in ascending order, using the natural order.
# @param a the array to be sorted

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

# Reads in a sequence of strings from standard input; quicksorts them;
# and prints them to standard output in ascending order.
# Shuffles the array and then prints the strings again to
# standard output, but this time, using the select method.
#def main():
#  import InputArgs
#  import random
#  ARR = InputArgs.getStrArray()
#  Sort(ARR);
#  print ' '.join(ARR)
#
#  # shuffle
#  random.shuffle(ARR)
#
#  # display results again using select
#  print
#  print ' '.join(ARR)

# TRUE: The maximum number of times that any one item is involved in a 
# compare when quicksorting an array of N items is linear.
# EXPLANATION: When an item is the partitioning item, it is
# involved in no more than N+1 compares, at which point it
# is never compared again. When an item is not the
# partitioning item, it can be compared to a partitioning
# item no more than twice (to the partitioning item), at
# which point the partitioning item is fixed (and never
# compared against the item again).

# FALSE: The expected number of compares to find a median of an array 
# of N distinct keys using quickselect is ~ 2N.
# EXPLANATION: The expected number of compares is ~ (2 + 2 ln 2) N. 
# In fact, no compare-based algorithm can find a median using fewer than 2N compares.

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2015, DV Klopfenstein, Python implementation and visualization
# Java Last updated: Thu Oct 10 11:43:17 EDT 2013
