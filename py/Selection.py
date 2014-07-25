# Alg1 Week 2 Lecture Selection Sort
 #************************************************************************
 #  Compilation:  javac Selection.java
 #  Execution:    java  Selection < input.txt
 #  Dependencies: StdOut.java StdIn.java
 #  Data files:   http:#algs4.cs.princeton.edu/21sort/tiny.txt
 #                http:#algs4.cs.princeton.edu/21sort/words3.txt
 #   
 #  Sorts a sequence of strings from standard input using selection sort.
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

 #  The <tt>Selection</tt> class provides static methods for sorting an
 #  array using selection sort.
 #  <p>
 #  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

02:31 SELECTION SORT
ALGORITHM: Ptr which scans from left to right
INVARIANTS: 
  * Entries left of the Ptr (inc the Ptr) fixed and in ascending order
  * No entry to the right of Ptr is smaller than any entry to the left of Ptr.
TO MAINTAIN ALGORITHM INVARIANTS:
  * Move the pointer to the right: i++
  * Identify index of minimum entry on right. 03:27
PROPOSITION: 04:38
  * Selection sort uses ~ N^2/2 (Quadratic) compares and N (linear) exchanges:
    N^2/2 =~ (N-1) + (N-2) + ... + 1 + 0
RUNNING TIME INSENSITIVE TO INPUT: Quadratic time, even if input is sorted.
http://www.sorting-algorithms.com/selection-sort 06:39


# Rearranges the array in ascending order, using the natural order.
# @param a the array to be sorted
def sort(a):
  N = len(a)
  # Items from i to j-1 are sorted
  # IN the ith iteration, find the smallest remaining Item above i
  for i in range(N): 
    Min = i
    # Identify index of min Item right of j
    for j in range(i+1,N):
      if _less(a[j], a[Min]):  # COMPARE is counted toward cost
        Min = j
    _exch(a, i, Min)           # EXCHANGE is counted toward cost
    assert isSorted(a, 0, i)
  assert isSorted(a)

# Rearranges the array, a, in ascending order, using a comparator.
# @param a the array
# @param c the comparator specifying the order
def sort(a, c):
  N = len(a)
  for i in range(N):
    Min = i
    for j in range(i+1,N):
      if _less(c, a[j], a[Min]): Min = j;
    _exch(a, i, Min)
    assert isSorted(a, c, 0, i)
  assert isSorted(a, c);

#**********************************************************************
#  Helper sorting functions
#**********************************************************************/

# is v < w ?
def _less(v, w): return v.compareTo(w) < 0

# is v < w ?
def _less(c, v, w): return c.compare(v, w) < 0
    
# exchange a[i] and a[j]
def _exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap

#**********************************************************************
#  Check if array is sorted - useful for debugging
#**********************************************************************/

# is the array a[] sorted?
def _isSorted(Comparable[] a): return _isSorted(a, 0, a.length - 1)
    
# is the array sorted from a[lo] to a[hi]
def _isSorted(Comparable[] a, int lo, int hi):
    for i in range(lo+1, hi+1):
        if (_less(a[i], a[i-1])) return False
    return True

# is the array a[] sorted?
def _isSorted(a, c): return _isSorted(a, c, 0, a.length - 1)

# is the array sorted from a[lo] to a[hi]
def _isSorted(a, c, lo, hi):
    for i in rane(lo+1, hi+1):
        if _less(c, a[i], a[i-1]): return False;
    return True;

# print array to standard output
def show(a):
    for i in range(len(a)): 
        StdOut.println(a[i]);

# Reads in a sequence of strings from standard input; selection sorts them; 
# and prints them to standard output in ascending order. 
def main():
    String[] a = StdIn.readAllStrings();
    Selection.sort(a);
    show(a);

if __name__ == '__main__':
  main()
