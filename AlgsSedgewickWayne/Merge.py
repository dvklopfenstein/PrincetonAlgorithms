"""Merge Sort (Top Down) from Week 3 lecture."""

import sys
import collections as cx
from AlgsSedgewickWayne.utils import __lt__, _isSorted

# pylint: disable=invalid-name

def Sort(arr, array_history=None): # 09:30
    """Rearranges the array in ascending order, using the natural order."""
    # At most N lg N compares and 6 N lg N array accesses to sort any array of size N
    aux = [None]*len(arr)  # Create aux outside _sort to avoid extensive costs.
    _add_history(array_history, arr, aux) # Record initial state of arrays
    _sort(arr, aux, low=0, high=len(arr)-1, array_history=array_history)
    assert _isSorted(arr)

def _sort(arr, aux, low, high, array_history):
    """Recursive sort."""
    ## print('low({LO}) high({HI}) {A}'.format(HI=high, LO=low, A=arr))
    if low >= high:
        # _vis_merge(arr, aux, low, -1, high)
        return
    # Divide in half. If N.5 round down to N
    mid = low + (high - low)//2
    # _vis_merge(arr, aux, low, mid, high)
    # pylint: disable=line-too-long
    ## print("AAA low({:>2}) to high({:>2}) => sort(low({:>2}) mid({:>2})), sort(mid+1({:>2}) high({:>2}))".format(
    ##     low, high, low, mid, mid+1, high))
    # pylint: disable=bad-whitespace
    _sort(arr, aux, low,     mid,  array_history)
    _sort(arr, aux, mid + 1, high, array_history)
    merge(arr, aux, low, mid, high)
    _add_history(array_history, arr, aux, (low, high, mid))

def merge(arr, aux, low, mid, high): # 05:00-06:00
    """Merge 2 sorted arrays into 1 sorted array."""
    assert _isSorted(arr, low, mid)    # precondition: arr[low .. mid]   are sorted subarrays
    assert _isSorted(arr, mid+1, high)  # precondition: arr[mid+1 .. high] are sorted subarrays
    aux[low:high+1] = arr[low:high+1] # copy to aux[]
    # merge back to arr[] in sorted order
    i = low     # index of sorted arr[low .. mid]   ( left-half)
    j = mid+1  # index of sorted arr[mid+1 .. high] (right-half)
    ## print('RRRRRRRRRRRRRRRRR', range(low, high+1), aux[j], aux[i])
    for k in range(low, high+1): # k is current entry in the sorted result
        # i ptr is exhausted  - this copying is unnecessary
        if   i > mid:
            arr[k] = aux[j]
            j += 1
        # j ptr is exhausted
        elif j > high:
            arr[k] = aux[i]
            i += 1
        elif __lt__(aux[j], aux[i]):
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1
    # _vis_merge(arr, aux, low, mid, high)
    assert _isSorted(arr, low, high) # postcondition: arr[low .. high] is sorted



def _add_history(array_history, arr, aux, anno=None):
    """For visualizing array history."""
    if array_history is not None:
        anno_a = None
        if anno is not None:
            low, high, mid = anno
            anno_a = cx.OrderedDict([(low, '-'), (high, '+'), (mid, '*')])
        array_history.add_history(arr, anno_a, name="arr")
        array_history.add_history(aux, None, name="aux")

def _vis_merge(arr, aux, low, mid, high, prt=sys.stdout):
    """For visualizing Merge results."""
    txt = "MERGE({:>2} {:>2} {:>2})   ".format(low, mid, high)
    #print txt, ' '.join(["{:>2}".format(e) for e in arr])
    fno = lambda e: '__' if e is None else e
    dsy = {low:'> ', mid:'|', high:' <'}
    prt.write("{} {}\n".format(txt, ' '.join(["{:>2}".format(
        dsy.get(i, '..')) for i in range(len(arr))])))
    prt.write("{} {}\n".format(txt, ' '.join(["{:>2}".format(e) for e in arr])))
    prt.write("{} {}\n".format(txt, ' '.join(["{:>2}".format(fno(e)) for e in aux])))
    prt.write("MERGE\n")

#************************************************************************
# Top-Down Mergesort
#************************************************************************

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
#   1. Divide array into two halves.
#   2. **Recursively** sort each half.
#   3. Merge two halves.
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
### Sorting Complexity (9:05) Alg 1, Week 3
########################################################
# COMPUTATIONAL COMPLEXITY: Framework to study efficiency
#   of algorithms for solving a particula problem X.
# MODEL OF COMPUTATION: Allowable operations.
# COST MODEL: Operation count(s).
# UPPER BOUND: Cost guarantee provided by some algorithm for X.
# LOWER BOUND: Proven limit on cost guarantee of all algorithms for X.
# OPTIMAL ALGORITHM: Algorithm with best possible cost guarantee for X.
#   lower bound ~ upper bound
#
# Example: sorting.
#   MODEL OF COMPUTATION: Decision Tree (Only access info thru compares)
#   COST MODEL: # compares.
#   UPPER BOUND: ~ N lg N   for mergesort.
#   LOWER BOUND: ~ N lg N (Proved w/decision tree below)
#   OPTIMAL ALGORITHM: ?

# Example: Decision tree (for 3 distinct items a, b, c) >= N! leafs
#                   a<b
#              +-----+-----+
#       +------T           F----+
#      b<c                     a<c
#   +---+-------+           +---+-------+
#   T           F           T           F
#   |          a<c          |          b<c
#             T   F                   T   F
# a b c   a c b   c a b   b a c   b c a   c b a

# COMPARE-BASED LOWER BOUND FOR SORTING (04:43)
# PROPOSITION: Any compare-based sorting algorithm must use at least
# lg(N!) ~ N lg N (Stirling's Approximation) compares in the worst-case
#
# PROOF:
#  * Assume array consists of N distinct values a(1) thru a(n)
#  * Worst case dictated by height h of decision tree.
#  * Binary tree of height h has at most e^k leaves.
#  * N! different orderings => at least N! leaves.
#
#      2^h >=  # leaves >= N!
#   =>   h >=   lg(N!)   ~ N lg N

# COMPLEXITY RESULTS IN CONTEXT (07:47)
#
# COMPARES? Mergesort is optimal with respect to # compares
# SPACE?    Mergesort is NOT oprimal with respect to space usage (ie Insertion sort better)
#
# LESSONS:
#  ** Don't try to design sorting algorithm guaranteeing 1/2 N lg N compares
#   * Design sorting algorithm that is both time/space optimal?
#
# Lower bound may not hold if the algorithm has information about
# (ie. other than compares):
#  * The initial order of the input. e.g. partially sorted, sorted,
#  * The distribution of key values. e.g. A lot of equal keys (sort faster)
#  * The representation of the keys. i.e. digit/chr compares instead of key cmp

# QUESTION: Under which of the following scenarios does the N lg N
# lower bound for sorting apply? Assume the keys are accessed only through
# the compareTo() method unless otherwise specified.
# ANSWER: no two keys are equal



########################################################
### Stability (Alg 1Week 3 Lecture)
########################################################
#
#-------------------------------------------------------
# 05:00 PROPOSITION: Merge operation IS STABLE.
#   Stable:
#     * Insertion sort
#       We never move equal items past each other
#     * Merge sort
#   NOT Stable:
#     * Selection sort
#       Has a long distance exchange that might move an item past some equal item
#     * Shell sort
#       Long distance exchanges

# QUESTION: Given an array of points, which of the following approaches would
# be least useful for removing duplicate points? Assume the point data type has
# the following three orders:
#     * A natural order that compares the x-coordinate and breaks ties by y-coordinate
#     * One comparator that compares by x-coordinate; another by y-coordinate.
#  NO quicksort by natural order
#  NO quicksort by x-coordinate; mergesort by y-coordinate
# YES mergesort by x-coordinate; quicksort by y-coordinate
#  NO mergesort by x-coordinate; mergesort by y-coordinate

#
# PROOF: Takes from left subarray if equal keys.
#

########################################################
### Duplicate Keys (Alg 1, Week 3 Lecture) (11:25)
########################################################
#
# MERGESORT WITH DUPLICATE KEYS: Always between (01:29)
#   * 1/2 N lg N and
#   *     N lg N
# compares.

# stably merge a[lo .. mid] with a[mid+1 ..hi] using aux[lo .. hi]

# F: Mergesort is faster than quicksort in practice because it uses
#    fewer compares than quicksort.
#    EXPLANATION: Mergesort is typically slower tha quicksort in
#    practice even though it makes fewer compares. Other factors
#    (including array accesses and cache) outweigh the advantage
#    in the number of compares.

# T: For any array of N distinct keys with N a power of 2, top-down
#    mergesort and bottom-up mergesort compare exactly the same pairs
#    of keys (but possibly in a different order).
#    EXPLANATION: This can be proved by induction - in either version
#    of mergesort, all of the subarray sizes are powers of 2.

# T: Any two items are compared with one another no more than once
#    during bottom-up mergesort.
#    EXPLANATION: Once two items are compared, they are merged into
#    the same subarray. Only items in different subarraus can be compared.

# F: Mergesort is faster in practice than insertion sort regardless
#    of the number of items N in the array.
#    EXPLANATION: Insertion sort is faster for small values of N;
#    this explains why we can imporive mergesort by cutting off
#    to insertion sort for small values of N.

# F: For any array of N distinct keys, top-down mergesort and bottom-up
#    mergesort compare exactly the same pairs of keys (but possibly in a
#    different order)
#    EXPLANATION: The compares can be different if N is not a power of 2.
#    for example, consider the array 0 1 2 3 4. Top-down mergesort makes the compares:
#      {0-1, 0-2, 1-2, 3-4, 0-3, 1-3, 2-3}
#    while bottom-up mergesort makes the compares
#      {0-1, 2-3, 0-2, 1-2, 0-4, 1-4, 2-4, 3-4}


#**********************************************************************
#  Index mergesort
#**********************************************************************/
# stably merge arr[low .. mid] with arr[mid+1 .. high] using aux[low .. high]
def _merge_index(arr, index, aux, low, mid, high):

    # copy to aux[]
    for k in range(low, high+1):
        aux[k] = index[k]

    # Maintain 3 variables:
    #   i: Current entry on left-half
    #   j: Current entry on left-half
    #   k: Current entry in the sorted result

    # merge back to arr[]
    i = low     # Start LEFT-HAND-POINTER  at left-most side of Left-sided  list
    j = mid+1  # Start RIGHT-HAND-POINTER at left-most side of Right-sided list
    for k in range(low, high+1):
        # If left-half list has been completely examined
        if i > mid:
            index[k] = aux[j]
            j += 1
        # If right-half list has been completely examined
        elif j > high:
            index[k] = aux[i]
            i += 1
        # If current value at right-half < current value at right-half, copy smaller val.
        elif __lt__(arr[aux[j]], arr[aux[i]]):
            index[k] = aux[j]
            j += 1
        else:
            index[k] = aux[i]
            i += 1

def _sort_index(arr, index, aux, low, high):
    """Recursive sort."""
    if high <= low:
        return
    mid = low + (high - low) // 2
    _sort_index(arr, index, aux, low, mid)
    _sort_index(arr, index, aux, mid + 1, high)
    _merge_index(arr, index, aux, low, mid, high)

# @param arr the array
# @return arr permutation <tt>p[]</tt> such that <tt>arr[p[0]]</tt>, <tt>arr[p[1]]</tt>,
#    ..., <tt>arr[p[N-1]]</tt> are in ascending order
def indexSort(arr):
    """Get a permutation that gives the elements in the array in ascending order"""
    array_len = len(arr)
    index = [None]*array_len
    for i in range(array_len):
        index[i] = i

    aux = [None]*array_len
    _sort_index(arr, index, aux, 0, array_len-1)
    return index

# Copyright (C) 2002-present, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2019-present, DV Klopfenstein, Python implementation
# Based on java which was Last updated: Fri Feb 14 17:45:37 EST 2014
