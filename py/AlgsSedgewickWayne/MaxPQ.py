"""Priority Queue (unordered array implementation), return maximum value."""
# TBD: FINISH PYTHON PORT

class MaxPQ: # <Key extends Comparable<Key>> # 15:01
  """ Priority Queue implemented with a heap-ordered binary tree."""

  def __init__(self, capacity):
    self.pq = [None]*(capacity+1)
    self.N = 0

  def isEmpty(self): return self.N == 0

  def insert(self, x): # 06:27
    """insert a key into the priority queue."""
    self.N += 1
    self.pq[self.N] = x # Insert at end
    self._swim(self.N)   # swim up to proper position

  def delMax(self): # 10:03
    """Return and remove the largest key."""
    maxKey = self.pq[1]
    # Exchange root(maxKey) with node at end,
    self.exch(1, self.N)
    self.N -= 1
    # then sink new root down to where it belongs.
    self._sink(1)
    # Prevent loitering by nulling out maxKey position
    self.pq[self.N+1] = None
    return maxKey

  def _swim(self,k): # 05:15
    """Exchange smaller child w/larger parent up through the hierarchy."""
    while k>1 and k/2 < k:
      self.exch(k, k/2)
      k = k/2

  def _sink(self, k): # 8:52
    """Push node down one level at a time to order array."""
    while 2*k <= self.N:
      j = 2*k
      # Check if we are going off the end of the heap and which child is larger
      if j < self.N and self.less(j, j+1):
        j += 1
      # If k is not less than either child, then we are done
      if not self.less(k,j):
        break
      # If k is larger than a child, exchange
      self.exch(k,j)
      k = j

# APIS AND ELEMENTARY IMPLEMENTATIONS (12:52)
#
# QUESTION: what is the expected number of array accesses and compares, respectively,
# to insert a random key into an ordered array implementation of a priority queue?
# ANSWER: linear and logorithmic.
# We can use binary search to find the insertion point in logorithmic time.
# On average, the key to be inserted must be places in the middle of the
# array--to keep the array in order, we must shift over all larger keys.


# Binary Heap Implementation
# * Very Simple
# * Optimal representation of data
# * Just a little arithmetic

  # INSERT: IMPROVE TO lg (lg N)
  #
  # TRUE: It is possible to use binary search to improve our
  # binary heap implementation so that insert() takes ~ lg (lg N)
  # compares per operation (in the worst case), where N is
  # the number of keys in the data structure.
  #
  # EXPLANATION: Note that the keys on the path from a leaf to
  # the root are in nondecreasing order. Thus, we can binary
  # search to find how far up in the tree the inserted key will
  # end up. This takes only ~ lg lg N compares, though it still
  # takes ~ lg N exchanges (in the worst case).

# Algorithms, Part 1 from Princeton University
# by Kevin Wayne, Robert Sedgewick
# https://class.coursera.org/algs4partI-005/lecture/39
# Week 4 Lecture APIs and Elementary Implementations (12:52)

# 02:55 PRIORITY QUEUE APPLICATIONS
# * Event-driven simulation: customers in a line, colliding particles
# * Numerical computation:   reducing roundoff error
# * Data compression:        Huffman codes
# * Graph searching:         Dijkstra's algorithm, Prim's algorithm
# * Number theory:           sum of powers
# * Artificial intelligence: A* search
# * Statistics:              maintain largest M values in a sequence
# * Operating systems:       load balancing, interrupt handling
# * Discrete optimization:   bin packing, scheduling
# * Spam filtering:          Bayesian spam filter
#
# GENERALIZES: stack, queue, randomized queue


# Algorithms, Part 1 from Princeton University
# by Kevin Wayne, Robert Sedgewick
# https:#class.coursera.org/algs4partI-005 retreived July 2014
# Lecture 8 - 2 Binary Heaps (23-36)

# BINARY   TREE: Empty or node with links to left and right binary trees.
# COMPLETE TREE: Pefectly balanced, except for bottom level.

# PROPERTY: Height of complete tree with N nodes is [lg N]
# PROOF: Height only increases whe N is a pwer of 2
#
# BINARY HEAP: Array representation of a heap-ordered complete binary tree.
#
# HEAP-ORDERED BINARY TREE: (01:44)
# * Keys in nodes (associate information with each node)
# * Parent's key is no smaller than children's keys
#
# ARRAY REPRESENTATION: (02:06)
# * Indices start at 1
# * Take nodes in **level** order
# * No explicit links needed!
#
#
# # COMPLETE TREE WITH N=16 NODES (HEIGHT = 4) 00:54
#
#             ______T______
#            /             \
#         __S__           __R__
#        /     \         /     \
#       P       N       O       A
#      / \     / \     / \     / \
#     E   I   H   G   *   *   *   *
#    / \ / \ / \ / \ / \ / \ / \ / \
#   *
#  / \
#
# i     0  1  2  3  4  5  6  7  8  9 10 11
# a[i]  -  T  S  R  P  N  O  A  E  I  H  G
# a[i]  -  T
#             S  R
#             |  +---------+
#             +--------    --
#                   /  \  /  \
#                   P  N  O  A
#                   |  +---------------+
#                   +--------------    --
#                               /  \  /  \
#                               E  I  H  G
#
# PROPOSITION: Largest key is a[1], which is root of binary tree
#
# PROPOSITION: Can use array indices to move through tree. (03:19)
# * Parent of node at k is at k/2
# * Children of node at k are at 2k and 2k+1
#
# PROMOTION IN A HEAP: (05:15)
# Scenario: Child's key becomes larger key than its parents key.
# To eliminate the violation:
# * Exchange key in child with key in parent
# * Repeat until heap order restored.
# Peter principle: Node promoted to level of incompetence.
#
# INSERTION IN A HEAP:
# Insert: Add node at end, then swim it up.
# Cost: At most 1+lg(N) compares
#
#
# DEMOTION IN A HEAP (07:47):
# Scenario: Parent's key becomes smaller than one (or both of its children)
# To eliminate the violation:
# * Exchange key in parent with key in **larger** child.
# * Repeat until heap order restored.
# Power struggle: Better subordinate promoted
#
# DELETE THE MAXIMUM IN A HEAP (10:03)
# Delete max: Exchange root(max) with node at end, then sink it down.
# Cost: At most 2*lg(N) compares


# PRIORITY QUEUES IMPLEMENTATION COST SUMMARY
# order-of-growth of running time for priority queue with N items
# implementation | insert | del max  | max
# ---------------+--------+----------+------
# unordered array|    1   |     N    |   N
# ordered array  |    N   |     1    |   1
# binary heap    |  log N |  log N   |   1 <<<<<<<<<<<<<<<<<
# d'ary heap     |log_d(N)|d*log_d(N)|   1
# Fibonacci      |    1   |  log N(*)|   1 *amortized
# impossible     |    1   |     1    |   1
#
# Possible improvements(slight possible):
# 1. d'way might work out better depending on freq on certain del max operations
# 2. Fibonacci (adv structure).  Too complicated to use in practice
#
# BINARY HEAP CONSIDERATIONS: (18:11)
# Immutabililty of keys.
# * Assumption: client does not change keys while they're on the PQ.
# * Best practice: use immutable keys.
# Underflow and overflow (18:50)
# * Underflow: throw exception if deleting from empty PQ.
# * Overflow: add no-arg constructor and use resizing array.
#   resizing array leads to log N amortized time per op (how to make worst case?)
# Minimum-oriented priority queue (19:07)
#   Usually we provide two implementations. Second imp:
#   * Replace less() with greater()
#   * Implement greater()
# Other operations for the future. (19:17)
# Can implement with sink() and swim() [stay tuned]
# * Offer the ability to Remove an arbitrary item.
# * Give the Client the ability to Change the priority of an item.
#
# Immutable: String, Integer, Double, Color, Vector, Transaction, Point2D
# Mutable: StringBuilder, Stack, Counter, Java array
#
# Immutable Advantages: (22:03)
# * Simplfies debugging
# * Safer in presence of hostile code
# * Simplifies concurren programming
# * Safe to use as key in priority queue or symbol table +++++!!!!

##import math
##
##  def insert_array(self, ARR):
##    for A in ARR:
##      self.insert(A)
##
##  # From Lecture 8 - 3 Heapsort (14-29)
##  # First sorting algorithm that is BOTH in-place AND N log N worst-case
##  # Fine sort algorithm that is very little code
##  # Sort gets done while touching relatively few objects
##  # *** SEE NOTES From Heap.java
##
##  # FALSE: When heapsorting an array of N distinct keys, there
##  #   is at most one compare between the two keys x and y.
##  # EXP: Consider the array { -, 2, 1, 0 }. In the heap
##  #   construction phase, the two keys 0 and 1 are compared with
##  #   each other (when sinking 2). In the sortdown phase, the keys
##  #   0 and 1 are compared with each other when deleting 2.
##  def sort(self):
##    L = len(self.pq)
##    # HEAPSORT: HEAP CONSTRUCTION
##    # First pass. Build using bottom-up method
##    # Go backwards through the heap starting at L/2 because
##    # right-most
##    # half of array is little heaps of size 1
##    #
##    #             ______1______  for(int k=5; k>=1; k--)...
##    #            /             \
##    #         __2__           __3__
##    #        /     \         /     \
##    #       4       5       -       -
##    #      / \     / \
##    #     -   -   -   -
##    #
##    for k in range(L/2,0,-1): # Lecture 8 - 3 Heapsort 07:39
##      self.sink(k, L)
##    #
##    # HEAPSORT: SORTDOWN
##    # Second pass.
##    # * Remove the maximum, one at a time.
##    # * Leave in array, instead of nulling out.
##    while (L>1): # 8:26
##      self.exch(1, L)
##      L -= 1
##      self.sink(1, L)


##  # array helper functions
##  # TBD: change less and exch functions to start at index 0 instead of index 1
##  # In this course, we use the term compare to mean a comparison between two keys,
##  # i.e., one call to compareTo().
##  def less(self, i, j): return self.pq[i] < self.pq[j]
##
##  def exch(self, i, j):
##    t = self.pq[i]
##    self.pq[i] = self.pq[j]
##    self.pq[j] = t
##
##  # Print functions
##  def __str__(self):
##    return "".join(["N=%-2d pq[%d]="%(self.N,len(self.pq)),  " ".join(map(str,self.pq))])
##  def __repr__(self): return __str__(self)
##  def __len__(self):  return len(self.pq)
##  def draw(self): # TBD: Finish this
##    # 0 1   2 3   4 5 6 7   8 9 ...
##    #   S   P R   N H O A   E I ...
##    #   1   2 2   3 3 3 3   4 4 ...
##    for i,E in enumerate(self.pq):
##      if i==0 or E is None: continue
##      level = int(math.log(i,2))
##      print ''.join(['-']*(level+1)), E


# Which of the following statements about priority queues are
# true? Check all that apply. Unless otherwise specified,
# assume that the binary heap implementation is the one from
# lecture (e.g., max-oriented and using 1-based indexing).
#
# TRUE: It is possible to use binary search to improve our
# binary heap implementation so that insert() takes ~ lg (lg
# N) compares per operation (in the worst case), where N is
# the number of keys in the data structure.
# Inorrect	
# EXP: Note that the keys on the path from a leaf to the root
# are in nondecreasing order. Thus, we can binary search to
# find how far up in the tree the inserted key will end up.
# This takes only ~ lg lg N compares, though it still takes ~
# lg N exchanges (in the worst case).
#
# FALSE: The expected number of compares to heapsort a
# uniformly random array of N distinct keys is ~ N lg N.
# EXP: It is ~ 2 N lg N.
#               Worst     Avg       Best      Remarks
# --------- - - --------  --------  --------  --------------------
# heap      I   2 N lg N  2 N lg N  N lg N    N log N guarantee, in-place, not stable
#
# FALSE: When heapsorting an array of N distinct keys, there
# is at most one compare between the two keys x and y.
# EXP: Consider the array { -, 2, 1, 0 }. In the heap
# construction phase, the two keys 0 and 1 are compared with
# each other (when sinking 2). In the sortdown phase, the keys
# 0 and 1 are compared with each other when deleting 2.
#
# FALSE: A 3-heap is an array representation (using 1-based
# indexing) of a complete 3-way tree, where the key in each
# node is greater than (or equal to) its children's keys. In
# the worst case, the number of compares to insert a key in a
# 3-heap containing N keys is ~ lg N.
# EXP: It is ~ log_3 N. The height is ~ log_3 N. The number of
# compares is bounded by the height of the 3-way tree.
#
# FALSE: Let a[] be a binary heap that contains the N >= 100
# distinct integers 1, 2, ..., N. Then, key 1 can be in any
# one of a[floor(N/2)] through a[N].
# EXP: f N = 100, then key 1 cannot be in a[50] because a[100]
# must be less than a[50].


# Algorithms, Part 1 from Princeton University
# by Kevin Wayne, Robert Sedgewick
# https://class.coursera.org/algs4partI-005 retreived July 2014
# Lecture 8 - 2 Binary Heaps (23-36)

# BINARY   TREE: Empty or node with links to left and right binary trees.
# COMPLETE TREE: Pefectly balanced, except for bottom level.

# PROPERTY: Height of complete tree with N nodes is [lg N]
# PROOF: Height only increases whe N is a pwer of 2
# 
# BINARY HEAP: Array representation of a heap-ordered complete binary tree.
# 
# HEAP-ORDERED BINARY TREE: (01:44)
# * Keys in nodes (associate information with each node)
# * Parent's key is no smaller than children's keys
# 
# ARRAY REPRESENTATION: (02:06)
# * Indices start at 1
# * Take nodes in **level** order
# * No explicit links needed!
# 
# 
# # COMPLETE TREE WITH N=16 NODES (HEIGHT = 4) 00:54
# 
#             ______T______
#            /             \
#         __S__           __R__
#        /     \         /     \
#       P       N       O       A
#      / \     / \     / \     / \
#     E   I   H   G   *   *   *   *
#    / \ / \ / \ / \ / \ / \ / \ / \ 
#   *
#  / \
# 
# i     0  1  2  3  4  5  6  7  8  9 10 11
# a[i]  -  T  S  R  P  N  O  A  E  I  H  G 
# a[i]  -  T                              
#             S  R                        
#             |  +---------+
#             +--------    --
#                   /  \  /  \
#                   P  N  O  A            
#                   |  +---------------+
#                   +--------------    --
#                               /  \  /  \
#                               E  I  H  G
# 
# PROPOSITION: Largest key is a[1], which is root of binary tree
# 
# PROPOSITION: Can use array indices to move through tree. (03:19)
# * Parent of node at k is at k/2
# * Children of node at k are at 2k and 2k+1
# 
# PROMOTION IN A HEAP: (05:15)
# Scenario: Child's key becomes larger key than its parents key.
# To eliminate the violation:
# * Exchange key in child with key in parent
# * Repeat until heap order restored.
# Peter principle: Node promoted to level of incompetence.
# 
# INSERTION IN A HEAP:
# Insert: Add node at end, then swim it up.
# Cost: At most 1+lg(N) compares
# 
# 
# DEMOTION IN A HEAP (07:47):
# Scenario: Parent's key becomes smaller than one (or both of its children)
# To eliminate the violation:
# * Exchange key in parent with key in **larger** child.
# * Repeat until heap order restored.
# Power struggle: Better subordinate promoted
# 
# DELETE THE MAXIMUM IN A HEAP (10:03)
# Delete max: Exchange root(max) with node at end, then sink it down.
# Cost: At most 2*lg(N) compares
# 
# 
# # Binary Heap Implementation
# # * Very Simple
# # * Optimal representation of data
# # * Just a little arithmetic
# public class MaxPQ<Key extends Comparable<Key>> # 15:01
# {
#   private Key[] pq;
#   private int N;
# 
#   public MaxPQ(int capacity)
#   { pq = (Key[]) new Comparable[capacity+1]; }
# 
#   /// PQ ops
#   public boolean isEmpty()
#   { return N == 0; }
#   public void insert(Key x) // 06:27
#   {
#     pq[++N] = x;
#     swim(N);
#   }
#   public Key delMax() // 10:03
#   {
#     Key max = pq[1];
#     # Exchange root(max) with node at end, 
#     exch(1, N--);
#     # then sink new root down to where it belongs.
#     sink(1);
#     # Prevent loitering by nulling out max position
#     pq[N+1] = null;
#     return max;
#   }
#   
#   /// heap helper functions 
#   private void swim(int k) // 05:15
#   {
#     while(k>1 && less(k/2, k))
#     {
#       exch(k, k/2);
#       k = k/2;
#     }
#   }
#   private void sink(int k) // 8:52
#   {
#     while (2*k <= N)
#     {
#       int j = 2*k;
#       # Check if we are going off the end of the heap and which child is larger
#       if (j < N && less(j, j+1)) j++;
#       # If k is not less than either child, then we are done
#       if (!less(k,j)) break;
#       # If k is larger than a child, exchange
#       exch(k,j);
#       k = j;
#     }
#   }
#   
#   /// array helper functions 
#   private boolean less(int i, int j)
#   { return pq[i].compareTo(pq[j]) < 0; }
#   private void exch(int i, int j)
#   { Key t = pq[i]; pq[i] = pq[j]; pq[j] = t; }
# }
# 
# PRIORITY QUEUES IMPLEMENTATION COST SUMMARY
# order-of-growth of running time for priority queue with N items
# implementation | insert | del max  | max
# ---------------+--------+----------+------
# unordered array|    1   |     N    |   N
# ordered array  |    N   |     1    |   1
# binary heap    |  log N |  log N   |   1 <==
# d'ary heap     |log_d(N)|d*log_d(N)|   1
# Fibonacci      |    1   |  log N(*)|   1 *amortized
# impossible     |    1   |     1    |   1
# 
# Possible improvements(slight possible):
# 1. d'way might work out better depending on freq on certain del max operations
# 2. Fibonacci (adv structure).  Too complicated to use in practice
# 
# BINARY HEAP CONSIDERATIONS: (18:11)
# Immutabililty of keys.
# * Assumption: client does not change keys while they're on the PQ.
# * Best practice: use immutable keys.
# Underflow and overflow (18:50)
# * Underflow: throw exception if deleting from empty PQ.
# * Overflow: add no-arg constructor and use resizing array.
#   resizing array leads to log N amortized time per op (how to make worst case?)
# Minimum-oriented priority queue (19:07)
# Usually we provide two implementations. Second imp:
# * Replace less() with greater()
# * Implement greater()
# Other operations for the future. (19:17)
# Can implement with sink() and swim() [stay tuned]
# * Aff the abillity to Remove an arbitrary item.
# * Give the Client the ability to Change the priority of an item.
# 
# Immutable: String, Integer, Double, Color, Vector, Transaction, Point2D
# Mutable: StringBuilder, Stack, Counter, Java array
# 
# Immutable Advantages: (22:03)
# * Simplfies debugging
# * Safer in presence of hostile code
# * Simplifies concurren programming
# * Safe to use as key in priority queue or symbol table +++++!!!!
# 
# 
# 
