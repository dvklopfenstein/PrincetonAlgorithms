class UnorderedArrayMaxPQ:

  def __init__(self, capacity):
    # set inititial size of heap to hold size elements
    self.pq = [None for i in range(capacity)] # elements
    self.N = 0 #  Number of elements

  def isEmpty(self): return self.N == 0
  def size(self): return self.N

  def insert(self, x): 
    self.pq[self.N] = x
    self.N += 1

  def delMax(self):
    max_idx = 0
    for i in range(self.N):
      if self._less(max_idx, i): 
        max_idx = i
    self._exch(max_idx, self.N-1)
    self.N -= 1
    return self.pq[self.N]

  # Helper functions.
  def _less(self, i, j): return self.pq[i] < self.pq[j]
  def _exch(self, i, j): self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

# 8 - 1 - APIs and Elementary Implementations (12-52)
# 
# * API and elementary implementations (00:15)
#   binary heaps
#   heapsort
#   event-driven simulation
# 
# COLLECTIONS: Insert and delete items.  Which item to delete?
#   Stack: Remove the item most recently added.
#   Queue: Remove the item least recently added.
#   Randomized queue: Remove a random item.
#   Priority queue: Remove the **largest** (or **smallest**) item.
#     insert('P') insert('Q') insert('E') removeMax -> Q
#     insert('X') insert('A') insert('M') removeMax -> X
#     insert('P') insert('L') insert('E') removeMax -> P
# 
# PRIORITY QUEUE APPLICATIONS: 02:54
#   Event-driven simulation [customers in a line, colliding particles
#   Numerical computation   [reducing roundoff error]
#   Data compression        [Huffman codes]
#   Graph searching         [Dijkstra's algorithm, Prim's algorithm]
#   Number theory           [sum of powers]
#   Artificial Intelligence [A* search]
#   Statistics              [maintain largest M values in a sequence]
#   Operating systems       [load balancing, interrupt handling]
#   Discrete optimization   [bin packing, scheduling]
#   Spam filtering          [Bayesian spam filter]
# 
# PRIORITY QUEUE PHILOSOPHY:
#   Generalizes stack, queue, randomized queue
#   Have data all at once.  Can not process it all at once.
#   Organize data so that we take the best one to process next...
# 
# public class MaxPQ< extends Comparable<> >  # 2:17
#   MaxPQ() # Create an empty priority queue
#   # MaxPQ(a) # Create a priority queue with given keys
#   void insert( v) # insert a key into the priority queue
#    delMax() # return and remove the largest key
#   boolean isEmpy() # is the priority queue empty?
#   #  max() # return the largest key
#   # size() # number of entries in the priority queue
# 
# Priority queue client example: 6:36
# CHALLENGE: Find the largest M items in a stream of N items.
# 
# # Use a min-oriented pq where we have the capability to delete the min
# # Transaction data type is (ordered by $$)
# MinPQ<Transaction> pq = new MinPQ<Transaction>()
# 
# while(StdIn.hasNextLine())
#:
#   String line = StdIn.readline()
#   Transaction item = new Transaction(line)
#   pq.insert(item)
#   if (pq.size() > M) # pq contains largest M items
#     # Keep track of the largest items by deleting the smallest items in a stream
#     pq.delMin()
# }
# 
# ORDER OF GROWTH OF FINDING THE LARGEST M IN A STREAM OF N ITEMS 08:29
#   implementation |  time   | space
#    -= 1 -= 1 -= 1 -= 1 -= 1 -= 1 -= 1-+ -= 1 -= 1 -= 1 -= 1-+ -= 1 -= 1 -= 1-
#   sort           | N log N |  N
#   elem PQ        |  M * N  |  M
#   binary heap    | N log M |  M <- Close to best in theory
#   best in theory |    N    |  M
 
# CHALLENGE: Implement ALL operations efficiently
#
# Order-of-growth of running time for priority queue with N items
#
# Implementation | insert | del max | find max
# ---------------|--------|---------|----------
# unordered array|    1   |    N    |  N
# ordered array  |    N   |    1    |  1
# GOAL           | log N  |  log N  | log N

# QUESTION: What is the expected nuber of array acesses and compares, 
# respectively, to insert a random key into an ordered array 
# implementation of a priority queue?
# ANSWER: linear and logarithmic
# EXPLANATION: We can use binary search to find the insertion point in
# logarithmic time. On average, the key to be inserted must be placed
# in the middle of the array -- to keep the array in order, we must shift over
# all larger keys.


# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2015, Python Implementation, DV Klopfenstein
# Java last updated: Wed Aug 26 05:30:12 EDT 2015.
