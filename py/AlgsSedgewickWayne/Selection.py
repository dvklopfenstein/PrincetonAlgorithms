#!/usr/bin/env python

# Alg1 Week 2 Lecture Selection Sort
#************************************************************************
#  Compilation:  javac Selection.java
#  Execution:    java  Selection < input.txt
#  Dependencies: StdOut.java StdIn.java
#  Data files:   http:#algs4.cs.princeton.edu/21Sort/tiny.txt
#                http:#algs4.cs.princeton.edu/21Sort/words3.txt
#
#  Sorts a sequence of strings from standard input using selection Sort.
#
#  % more tiny.txt
#  S O R T E X A M P L E
#
#  % java Selection < tiny.txt
#  A E E L M O P R S T X                 [ one string per line ]
#
#  % more words3.txt
#  bed bug dad yes zoo ... all bad yet
#
#  % java Selection < words3.txt
#  all bad bed bug dad ... yes yet zoo    [ one string per line ]
#
#************************************************************************/

#  The <tt>Selection</tt> class provides static methods for Sorting an
#  array using selection Sort.
#  <p>
#  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne
#  @edited DV Klopfenstein
#/

########################################################
# Lecture Alg 1 Week 2 Selection Sort
########################################################
#
# ALGORITHM: Ptr which scans from left to right
# INVARIANTS:
#   * Entries left of the Ptr (inc the Ptr) fixed and in ascending order
#   * No entry to the right of Ptr is smaller than any entry to the left of Ptr.
# TO MAINTAIN ALGORITHM INVARIANTS:
#   * Move the pointer to the right: i++
#   * Identify index of minimum entry on right. 03:27 (Loop thru rhs array to get min)
#   * Exchange into position.
# PROPOSITION: 04:38
#   * Selection Sort uses ~ N^2/2 (Quadratic) compares and N (linear) exchanges:
#     N^2/2 =~ (N-1) + (N-2) + ... + 1 + 0
# 05:57 RUNNING TIME INSENSITIVE TO INPUT: Quadratic time, even if input is Sorted.
# 06:12 DATA MOVEMENT IS MIMAL. Linear number of exchanges.
# http://www.Sorting-algorithms.com/selection-Sort 06:39

# 06:52 QUESTION. How many compares does selection sort make when the input
# array is **already sorted**?
# ANSWER: quadratic


########################################################
# Lecture Alg 1 Week 2 "Sorting Introduction" (14:43)
########################################################

# 04:50 GOAL. Sort any type of data.
#
# Q. How can sort() know how to compare data of type "Double",
# "String", and "java.io.File" without any information about the
# type of an item's key?
#
# CALLBACK = REFERENCE TO EXECUTABLE CODE. (Passing fncs to fncs)
#   * Client passes array of objecys to sort() function.
#   * The "sort()" function calls back object's "compareTo()" method as needed.
#
# IMPLEMENTING CALLBACKS.
#   * java: interfaces
#   * C: function pointers.
#   * C++: class-type functors.
#   * C#: delegates.
#   * Python, Perl, ML, Javascript: first-class functions.
#
# 05:57 COMPARABLE INTERFACE
#
# public interface Comparable<Item>
# {
#   public int compareTo(Item that)
#   {
#     ...
#     return -1; # less than
#     ...
#     return +1; # greater than
#     ...
#     return 0;  # equal to
#   }
# }

# 08:05 TOTAL ORDER
#
# A TOTAL ORDER is a binary relation <= that satisfies:
#   * Antisymmetry: if v<=w and w<=v, then v==w.
#   * Transitivity: if v<=w and w<=x, then v<=x.   v-w-x
#   * Totality: either v<=w or w<=v or both.
#
# Rock-Paper-Scissors is NOT a TOTAL ORDER (intransitivity)

#13:21 TESTING IF SORTED
#
#GOAL. Test if an array is sorted.
#
#Q. If the sorting algorithm passes the test, did it correctly sor the array?
#A. YES. If you used the __lt__ and exchange method.

# 14:36 QUESTION: Consider the data type "Temp" defined below. Which
# of the following required properties of the "Comparble" interface
# does the compareTo() method violate?
#
# public class Temp implements Comparable<Temp> {
#   private final double deg;
#
#   public Temp(double deg) {
#     this.deg = deg;
#   }
#
#   public int compareTo(Temp that) {
#     double EPS = 0.1;
#     if (this.deg < that.deg - EPS)
#       return -1;
#     if (this.deg > that.deg + EPS)
#       return +1;
#     return 0;
#   }
#
#       deg-EPS    deg    deg+EPS
#             <     |     >
#
#       v     <   |   >
#       x    <   |   >
#       w           <   |   >
#          ------>v w<------------- v<=w
#          ->x          w<---------
#               000000000011111111112222222222
#               012345678901234567890123456789
#                     <         a         >
#            <          b         >
#	     <        c         >
# ---------->b                  a<---------- a>b
# ---->c                b<------------------ b>c => a>b>c => a>c
# ---->c                        a<---------- a:w
#
# ANSWER: Transitivity
# EXPLANATION: Transitivity is violated.
# YOU MUST NOT INTRODUCE A FUDGE FACTOR WHEN COMPARING TWO
# FLOATING_POINT NUMBERS IF YOU WANT TO IMPLEMENT THE Comparable INTERFACE.




########################################################
### Stability (Week 3 Lecture "Stability")
########################################################
#
#-------------------------------------------------------
# 03:42 PROPOSITION: Selection Sort IS NOT stable.
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
# i min 0  1   2
# ----------------
# 0 2 *B1 *B2 >A   > Choose min(A), exch(B1,A), B1 moved past equal B2
# 1 1  A  >B2 *B1
# 2 2  A   B2 >B1
#     *A  *A2 *A3
#
#


# Rearranges the array in ascending order, using the natural order.
# @param a the array to be Sorted
# @param array_history; Used in tests. When true prints ASCII Art demonstrating the sort
def Sort(ARR, array_history=None):
  N = len(ARR)
  # Items from i to j-1 are Sorted
  # IN the ith iteration, find the smallest remaining Item above i
  for i in range(N): # MOVE pointer to the right
    Min = i # Index of smallest element to the right
    # Identify index of min Item right of j
    for j in range(i+1,N):
      if __lt__(ARR[j], ARR[Min]):  # COMPARE is counted toward cost
        Min = j
    if array_history is not None: add_history(array_history, ARR, {i:'*', Min:'*'} )
    _exch(ARR, i, Min)           # EXCHANGE is counted toward cost
    assert _isSorted(ARR, 0, i)
  assert _isSorted(ARR)
  if array_history is not None: add_history(array_history, ARR, None )

## Rearranges the array, a, in ascending order, using a comparator.
## @param a the array
## @param c the comparator specifying the order
#def SortC(a, c):
#  N = len(a)
#  for i in range(N):
#    Min = i
#    for j in range(i+1,N):
#      if __lt__C(c, a[j], a[Min]): Min = j
#    _exch(a, i, Min)
#    assert isSorted(a, c, 0, i)
#  assert isSorted(a, c)

#**********************************************************************
#  Helper Sorting functions
#**********************************************************************/

# is v < w ?
def __lt__(v, w): return v < w

## is v < w ?
#def __lt__C(c, v, w): return v < w

# exchange a[i] and a[j]
def _exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap

#**********************************************************************
#  Check if array is Sorted - useful for debugging
#**********************************************************************/

# is the array Sorted from a[lo] to a[hi] inclusive of idx==lo and idx==hi
def _isSorted(a, lo=None, hi=None):
    if lo is None and hi is None:
      lo = 0
      hi = len(a)-1
    for i in range(lo+1, hi+1):
        if __lt__(a[i], a[i-1]): return False
    return True

# # is the array a[] Sorted?
# def _isSorted(a, c): return _isSorted(a, c, 0, a.length - 1)
#
# is the array Sorted from a[lo] to a[hi]
# def _isSortedC(a, c, lo, hi):
#     for i in rane(lo+1, hi+1):
#         if __lt__(c, a[i], a[i-1]): return False
#     return True

def add_history(ret, ARR, anno):
  import ArrayHistory
  ArrayHistory.add_history(ret, ARR, anno)

# Reads in a sequence of strings from standard input selection Sorts them;
# and prints them to standard output in ascending order.
def main():
    import InputArgs
    a = InputArgs.getStrArray()
    Sort(a)
    print ' '.join(a)

if __name__ == '__main__':
  main()
