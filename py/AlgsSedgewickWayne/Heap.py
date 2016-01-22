"""Heapsort."""

from AlgsSedgewickWayne.utils import _isSorted

def Sort(pq):
  N = len(pq)
  for k in range(N/2, 0, -1):
    _sink(pq, k, N)
  while (N > 1):
    _exch(pq, 1, N)
    N -= 1
    _sink(pq, 1, N)
  assert _isSorted(pq)

def _sink(pq, k, N):
  while 2*k <= N:
    j = 2*k
    if j < N and _less(pq, j, j+1): 
      j += 1
    if not _less(pq, k, j): 
      break
    _exch(pq, k, j)
    k = j

def _less(pq, i, j):
  return pq[i-1] < (pq[j-1])

def _exch(pq, i, j):
  pq[i-1], pq[j-1] = pq[j-1], pq[i-1]


# Copyright (C) 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2015, DV Klopfenstein, Python Implementation

## Algorithms, Part 1 from Princeton University
## by Kevin Wayne, Robert Sedgewick
## https://class.coursera.org/algs4partI-005 retreived July 2014
## Lecture 8 - 3 Heapsort (14-29)
#
#
## BASIC PLAN FOR AN IN-PLACE SORT:
## * Create max-heap with all N keys.
## * Repeatedly remove the maximum key
#
#1. START WITH ARRAY OF KEYS IN ARBITRARY ORDER
#
#            ______S______
#           /             \
#        __O__           __R__
#       /     \         /     \
#      T       E       X       A
#     / \     / \                
#    M   P   L   E                
#
#2. BUILD A MAX-HEAP (IN PLACE) USING BOTTOM-UP (right-to-left) METHOD. 03:57
#
#            ______X______
#           /             \
#        __T__           __S__
#       /     \         /     \
#      P       L       R       A
#     / \     / \                
#    M   O   E   E                
#
#3. SORTED RESULT (IN PLACE) 04:43
#A E E L M O P R S T X
#1 2 3 4 5 6 7 8 9 0 1
#
#                  A      
#                          
#          E               E  
#                              
#      L       M       O       P
#                                
#    R   S   T   X                
   
# Fine sort algorithm that is very little code
# Sort gets done while touching relatively few objects

    # HEAPSORT: HEAP CONSTRUCTION
    # First pass. Build using bottom-up method
    # Go backwards through the heap starting at N/2 because right-most 
    # half of array is little heaps of size 1
    # 
    #             ______1______  for(int k=5; k>=1; k--)...
    #            /             \
    #         __2__           __3__
    #        /     \         /     \
    #       4       5       -       -
    #      / \     / \                
    #     -   -   -   -                
    # 

    #   
    # HEAPSORT: SORTDOWN
    # Second pass.
    # * Remove the maximum, one at a time.
    # * Leave in array, instead of nulling out.

  # array helper functions (Lecture 8 - 2)
  # TBD: CONVERT FROM 1-BASED INDEXING TO 0-BASE INDEXING

# HEAPSORT: MATHEMATICAL ANALYSIS 10:47
# PROPOSITION. Heap construction uses <= 2 N (linear number) compares and exchanges.
# PROPOSITION. Heapsort uses <= 2 N lg N compares and exchanges.
#   Size of the heap is at most lg(N)
#
# SIGNIFICANCE. In-place sorting algorithm with N log N worst-case. 11:14
# First sorting algorithm that is both:
#   1. In-place
#   2. Manages to get sorting job done with guaranteed N lg N compares
# * Mergesort: no, linear extra space
#              in-place merge possible, not practical
# * Quicksort: no, quadratic time in worst case 
#              (even though unlikely with random shuffling).
#              N log N worst-case quicksort possible. not practical
# * Heapsort:  yes!

# Job interview Question:
# What is a sorting algorithm that is both in-place and guaranteed N lg N time? HEAPSORT 12:00

# In practice, heapsort is not used that much...
# BOTTOM LINE. Heapsort is optimal for both time and space, but:
# * Inner loop longer than quicksorts:
#   Two compares that get done N lg N times
#   And then there is the array arithmetic.
# * Makes poor use of cache memory:
#   References to memory are all over the place when it is a huge array 12:41
#   Quicksort has a local memory reference, but heapsort looks far away
# * Not stable. (Mergesort is stable)
#   Because it does long distance exchanges... 
#   brings items that have equal keys back out of order

# FULL SUMMARY OF SORTING ALGORITHMS
#           inplace?
#             stable?
#               Worst     Avg       Best      Remarks
# --------- - - --------  --------  --------  --------------------
# selection x   N^2/2     N^2/2     N^2/2     N exchanges
# insertion x x N^2/2     N^2/4       N       use for small N or partially ordered
# shell     x    ???       ???        N       tight code, subquadratic
# quick     x   N^2/2     2 N ln N  N lg N    N log N probabilistic guarantee
#                                             fastest in practice
# 3-way qu  x   N^2/2     2 N ln N    N       improves quicksort in presence
#                                             of duplicate keys
# merge       x N lg N    N lg N    N lg N    N log N guarantee, stable
# heap      x   2 N lg N  2 N lg N  N lg N    N log N guarantee, in-place
# ???       x x N lg N    N lg N    N lg N    Holy sorting grail

# QUESTION: How many compares does bottom-up heap construction perform 
# in the worst case when sorting an array of N keys?
# ANSWER: Linear. The bottom-up version of heapsort makes ~2N compares in the worst case.


# Java last updated: Sat Sep 26 08:34:31 EDT 2015.
