#!/ust/bin/env python

# Alg1 Week2 Lecture Insertion Sort


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
# BEST CASE 06:12: If the array is in ascneding order, insertion sort makes N-1 compares and 0 exchanges
#   A E E L , O P R S T X
# WORST CASE 06:37: If the array is in descending order (and no duplicates),
#   insertion sort makes ~ 1/2*N^2 compares and ~ 1/2*N^2 exchanges (Slower that Selection sort)
#   X T S R P O M L E E A
#   For every step, it is not just comparing, it is also exchanging
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
# QUESTION: How many compares does insertion sort make on an imput array that is already sorted? 
# ANSWER: linear




 # Rearranges the array in ascending order, using the natural order.
 # @param a the array to be sorted
def Sort(ARR, array_history=None):
    N = len(ARR)
    # 00:57 Everything to the left is in acending order
    #       Everything to the right, we have not seen at all
    for i in range(N):
        #for (int j = i; j > 0 && less(a[j], a[j-1]); j--):
        j = i
        # Exchange the curr Elem with every element to the left that is > 01:21
        while j > 0 and _less(ARR[j], ARR[j-1]): 
            _exch(ARR, j, j-1)
            if array_history is not None: add_history(array_history, ARR)
            j -= 1
        assert _isSorted(ARR, 0, i)
    assert _isSorted(ARR);

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
 # @return a permutation <tt>p[]</tt> such that <tt>a[p[0]]</tt>, <tt>a[p[1]]</tt>,
 #    ..., <tt>a[p[N-1]]</tt> are in ascending order
 #/
def indexSort(ARR, array_history=None):
    N = len(ARR)
    index = [None]*N
    for i in range(N):
        index[i] = i

    for i in range(N):
        j = i
        while j > 0 and _less(ARR[index[j]], ARR[index[j-1]]):
          _exch(index, j, j-1)
          if array_history is not None: add_history(array_history, ARR)
          j -= 1
    return index

#**********************************************************************
#  Helper sorting functions
#**********************************************************************/

# is v < w ?
def _less(v, w): return v < w

# # is v < w ?
# def _less(c, v, w):
#     return (c.compare(v, w) < 0);
    
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
    # is the array sorted from a[lo] to a[hi]
    for i in range(lo+1, hi+1):
        if _less(a[i], a[i-1]): return False
    return True

# def _isSorted(a, c):
#     return _isSorted(a, c, 0, a.length - 1)
# 
# # is the array sorted from a[lo] to a[hi]
# def _isSorted(a, c, lo, hi):
#     for i in range(lo+1,hi+1):
#         if less(c, a[i], a[i-1]): return False
#     return True

def add_history(ret, ARR):
  import copy
  if isinstance(ret, list):
    ret.append(copy.deepcopy(ARR))

#*
# Reads in a sequence of strings from standard input; insertion sorts them;
# and prints them to standard output in ascending order.
#/
def main():
    import InputArgs
    a = InputArgs.getStrArray();
    sort(a)
    print ' '.join(a)

if __name__ == '__main__':
  main()

