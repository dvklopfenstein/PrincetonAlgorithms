"""Alg1 Week2 Lecture Insertion Sort"""

from AlgsSedgewickWayne.utils import _isSorted, __lt__, _exch

def Sort(ARR, array_history=None):
  """Rearranges the array in ascending order, using the natural order."""
  N = len(ARR)
  # 00:57 Everything to the left is in acending order
  #       Everything to the right, we have not seen at all
  for i in range(N):
    j = i
    # Exchange the curr Elem with every element to the left that is > 01:21
    while j > 0 and __lt__(ARR[j], ARR[j-1]):
      if array_history is not None: array_history.add_history(ARR, {j:'*', j-1:'*'})
      _exch(ARR, j, j-1)
      j -= 1
    assert _isSorted(ARR, 0, i)
  assert _isSorted(ARR);
  if array_history is not None: array_history.add_history(ARR, None)





def indexSort(ARR, array_history=None):
  """Do not change ARR, return a new sorted version of ARR."""
  N = len(ARR)
  index = range(N)
  for i in range(N):
    j = i
    while j > 0 and __lt__(ARR[index[j]], ARR[index[j-1]]):
      _exch(index, j, j-1)
      if array_history is not None: array_history.add_history(ARR, {j:'*', j-1:'*'})
      j -= 1
  return index

#************************************************************************
#  Compilation:  javac Insertion.java
#  Execution:    java Insertion < input.txt
#  Dependencies: StdOut.java StdIn.java
#  Data files:   http:#algs4.cs.princeton.edu/21sort/tiny.txt
#                http:#algs4.cs.princeton.edu/21sort/words3.txt
#
#  Sorts a sequence of strings from standard input using insertion sort.
#
#  % more tiny.txt
#  S O R T E X A M P L E
#
#  % java Insertion < tiny.txt
#  A E E L M O P R S T X                 [ one string per line ]
#
#  % more words3.txt
#  bed bug dad yes zoo ... all bad yet
#
#  % java Insertion < words3.txt
#  all bad bed bug dad ... yes yet zoo   [ one string per line ]
#
#************************************************************************/

#*
#  The <tt>Insertion</tt> class provides static methods for sorting an
#  array using insertion sort.
#  <p>
#  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne
#/

# SIMULATION: 00:32 to 02:40
#
# ALGORITHM: Ptr scans from Left to Right
# INVARIANTS: 02:50
#   * Entries to the left or Ptr (inc Ptr) are in ascending order
#   * Entries to the right of Ptr have not yet been seen
# PROPOSITION: 04:27 To sort a randomly-ordered array with distinct keys:
#   ~ 1/4*N^2 compares  on average
#   ~ 1/4*N^2 exchanges on average
# PROOF: 05:16 Expect each entry to move halfway back below the diagonal on the average
#
# INSERTION SORT: BEST CASE AND WORST CASE: 06:10
# BEST CASE 06:12: If the array is in ascending order,
#   insertion sort makes N-1 compares and 0 exchanges
#   A E E L , O P R S T X
# WORST CASE 06:37: If the array is in descending order (and no duplicates),
#   insertion sort makes ~ 1/2*N^2 compares and ~ 1/2*N^2 exchanges (Slower that Selection sort)
#   X T S R P O M L E E A
#   For every step, it is not just comparing, it is also exchanging
#
# MEMORY: Insertion sort uses only a constant amount of memory (other than the input array).
# This is a key property of insertion sort.
#
# INSERTION SORT: PARTIALLY-SORTED ARRAYS 07:47 - 08:20
#   Appear often in practice:
#     1. All elems sorted except the last ones
#     2. Just a few elems out of place.
# DEFINITION: An INVERSION is a pair of keys that are out of order:
#   A E E L M O T R X P S (6 inversions: T-R T-P T-S R-P X-P X-S)
# DEFINITION: An array is PARTIALLY-SORTED if the number of inversions is <= c*N
#  * Ex 1. A subarray of size 10 appended to a sorted subarray of size N
#  * Ex 2. An array of size N with only 10 entries out of place
#
# PROPOSITION: For partially-sorted arrays, insertion sort runs in linear time. 08:57
# PROOF: Number of exchanges equals the numbers of inversions
#   number of compares = exchanges + (N - 1)
#
# INSERTION SORT IS INEFFICIENT because elements only move one place at a time
# even if we know that they have to move far away.
#
# QUESTION: How many compares does insertion sort make on an imput array that is already sorted?
# ANSWER: linear
#
# QUESTION: True or False? The expected #of compares to insertion sort an array containint N/2 0s and N/2 1s
# in uniformly random order is ~1/4 N^2.
# ANSWER: False. Consider element i> 0. How many of the items a[0], a[1], ..., a[i-1] is a[i] inverted with?
# If a[i] == 1 (which happens with probability 1/2), then the number is 0.
# If a[i] == 0 (which happens with probability 1/2), then we expect half of the i previous
# elements to be 1s, so the expected number is i/2.
# So the expected number of inversions is 1/2(0/2 + 1/2 + 2/2 + 3/2 + ... + (N-1)/2) ~N^2/8.
# Thus, the expected number of compares is ~ 1/8 N^2

# TRUE: Any pair of items is compared no more than once during insertion sort.
# EXPLANATION: Let a[i] and a[j] be two entries in the unsorted array with i<j.
# The entries a[i] and a[j] are compred no more than once during iteration j and they are not
# compared during any other iteration.



########################################################
### Stability (Week 3 Lecture "Stability")
########################################################
#
# #----------------------------------------------
# 03:29 PROPOSITION: INSERTION SORT IS STABLE
#
# PROOF: Equal items never move past each other (in the "Sort" code)
#
# NOTE: Items depicted as A1 and A2 in the example below have the same
# key, "A".  The 1 and 2 following the "A" are denote that A1 was 1st
# and A2 was 2nd.
#
# NOTE: if "__lt__" in the "Sort" routine were "less than or equal to",
# it would not work.
#
# i j   0   1   2   3   4
# -----------------------
# 0 0 >B1  A1  A2  A3  B2
# 1 0 >A1 *B1  A2  A3  B2
# 2 1 *A1 >A2 *B1  A3  B2
# 3 2 *A1 *A2 >A3 *B1  B2
# 4 4 *A1 *A2 *A3 *B1 >B2
#     *A1 *A2 *A3 *B1 *B2
#
#



#  #*
#  # Rearranges the array in ascending order, using a comparator.
#  # @param a the array
#  # @param c the comparator specifying the order
#  #/
# def Sort(a, c):
#     int N = len(a)
#     for (int i = 0; i < N; i++):
#         for (int j = i; j > 0 && less(c, a[j], a[j-1]); j--):
#             _exch(a, j, j-1);
#         assert _isSorted(a, c, 0, i)
#     assert _isSorted(a, c)

# return a permutation that gives the elements in a[] in ascending order
# do not change the original array a[]
 #*
 # Returns a permutation that gives the elements in the array in ascending order.
 # @param a the array
 # @param array_history; Used in tests. When true prints ASCII Art demonstrating the sort
 # @return a permutation <tt>p[]</tt> such that <tt>a[p[0]]</tt>, <tt>a[p[1]]</tt>,
 #    ..., <tt>a[p[N-1]]</tt> are in ascending order
 #/

