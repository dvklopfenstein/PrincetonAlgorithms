#!/usr/bin/env python

class UnorderedMaxPQ(object): # <Key extends Comparable<Key>> # 10:38

  def __init__(self, capacity):
    self._pq = [None for i in range(capacity)]
    self._N = 0

  def isEmpty(self): return self._N == 0

  def insert(self, key): 
    self._pq[self._N] = key # Insert at end
    self._N += 1

  def delMax(self):
    int max_idx = 0
    # Must examine each elem, since unordered
    for i in range(self._N):
      if less(max_idx, i): max_idx = i
    exch(max_idx, self._N-1) # Exchange from end
    self._N -= 1
    return pq[self._N]
 
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
# public class MaxPQ<Key extends Comparable<Key> >  # 2:17
#   MaxPQ() # Create an empty priority queue
#   # MaxPQ(Key[] a) # Create a priority queue with given keys
#   void insert(Key v) # insert a key into the priority queue
#   Key delMax() # return and remove the largest key
#   boolean isEmpy() # is the priority queue empty?
#   # Key max() # return the largest key
#   # int size() # number of entries in the priority queue
# 
# Priority queue client example: 6:36
# CHALLENGE: Find the largest M items in a stream of N items.
# 
# # Use a min-oriented pq where we have the capability to delete the min
# # Transaction data type is Comparable (ordered by $$)
# MinPQ<Transaction> pq = new MinPQ<Transaction>();
# 
# while(StdIn.hasNextLine())
# {
#   String line = StdIn.readline();
#   Transaction item = new Transaction(line);
#   pq.insert(item);
#   if (pq.size() > M) # pq contains largest M items
#     # Keep track of the largest items by deleting the smallest items in a stream
#     pq.delMin();
# }
# 
# ORDER OF GROWTH OF FINDING THE LARGEST M IN A STREAM OF N ITEMS 08:29
#   implementation |  time   | space
#   ---------------+---------+-------
#   sort           | N log N |  N
#   elementary PQ  |  M * N  |  M
#   binary heap    | N log M |  M <- Close to best in theory
#   best in theory |    N    |  M
 
# A fine implementation if priority is going to be tiny all the time:
# CHALLENGE: Implement ALL operations efficiently
#
# Order-of-growth of running time for priority queue with N items
#
# Implementation | insert | del max | find max
# ---------------+--------+---------+-----
# unordered array|    1   |    N    |  N
# ordered array  |    N   |    1    |  1
# GOAL           | log N  |  log N  | log N
