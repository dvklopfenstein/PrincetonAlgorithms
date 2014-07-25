# Algorithms, Part 1 from Princeton University
# by Kevin Wayne, Robert Sedgewick
# https://class.coursera.org/algs4partI-005 retreived July 2014
# Lecture 8 - 3 Heapsort (14-29)


# BASIC PLAN FOR AN IN-PLACE SORT:
# * Create max-heap with all N keys.
# * Repeatedly remove the maximum key

1. START WITH ARRAY OF KEYS IN ARBITRARY ORDER

            ______S______
           /             \
        __O__           __R__
       /     \         /     \
      T       E       X       A
     / \     / \                
    M   P   L   E                

2. BUILD A MAX-HEAP (IN PLACE) USING BOTTOM-UP (right-to-left) METHOD. 03:57

            ______X______
           /             \
        __T__           __S__
       /     \         /     \
      P       L       R       A
     / \     / \                
    M   O   E   E                

3. SORTED RESULT (IN PLACE) 04:43
A E E L M O P R S T X
1 2 3 4 5 6 7 8 9 0 1

                  A      
                          
          E               E  
                              
      L       M       O       P
                                
    R   S   T   X                
   
# Fine sort algorithm that is very little code
# Sort gets done while touching relatively few objects
public class Heap # 09:08
{
  public static void sort(Comparable[] pq)
  {
    int N = pq.length;
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
    for (int k=N/2; k >= 1; k--) # 07:39
      sink(a, k, N);
    #   
    # HEAPSORT: SORTDOWN
    # Second pass.
    # * Remove the maximum, one at a time.
    # * Leave in array, instead of nulling out.
    while (N>1) # 8:26
    {
      exch(a, 1, N--);
      sink(a, 1, N);
    }
  }

  private void sink(int k) # 8 - 2 8:52 
  {
    while (2*k <= N)
    {
      int j = 2*k;
      # Check if we are going off the end of the heap and which child is larger
      if (j < N && less(j, j+1)) j++;
      # If k is not less than either child, then we are done
      if (!less(k,j)) break;
      # If k is larger than a child, exchange
      exch(k,j);
      k = j;
    }
  }
  # array helper functions (Lecture 8 - 2)
  # TBD: CONVERT FROM 1-BASED INDEXING TO 0-BASE INDEXING
  private boolean less(int i, int j)
  { return pq[i].compareTo(pq[j]) < 0; }
  private void exch(int i, int j)
  { Key t = pq[i]; pq[i] = pq[j]; pq[j] = t; }
}

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


