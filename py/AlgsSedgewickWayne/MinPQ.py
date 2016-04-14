"""Minimum Priority Queue data type"""

import copy

class MinPQ(object):
  """Priority Queue supporting insert and delete-the-minimum key."""

  def __init__(self, *args, **kwargs):
    if len(args) == 0:
      self._init_capacity(1)
    elif isinstance(args[0], int):
      self._init_capacity(args[0])
    else:
      self._init_w_keys(args[0])
    self.comparator = None if 'comparator' not in kwargs else kwargs['comparator']


  def _init_capacity(self, initCapacity):
    self.pq = [None for i in range(initCapacity+2)] # Pos 0 not used
    self.N = 0 # number of items on priority queue

  def _init_w_keys(self, keys):
    self.N = len(keys)
    self.pq = [None] + [elem for elem in keys] # Pos 0 not used
    for k in range(self.N/2, 0, -1):
      self._sink(k);
    assert self._isMinHeap()

  def isEmpty(self): return self.N == 0
  def size(self): return self.N

  def min(self):
    """Returns a smallest key on this priority queue."""
    if self.isEmpty(): 
      raise Exception("Priority queue underflow")
    return pq[1]

  def _resize(self, capacity):
    """helper function to double the size of the heap array."""
    assert capacity > self.N
    self.pq = [pq_elem for pq_elem in self.pq] + [None for i in range(capacity-len(self.pq))]

  def insert(self, x):
    """Adds a new key to this priority queue."""
    # double size of array if necessary
    if (self.N == len(self.pq) - 1):
      self._resize(2 * len(self.pq))
    # add x, and percolate it up to maintain heap invariant
    self.N += 1 
    self.pq[self.N] = x
    self._swim(self.N)
    assert self._isMinHeap()

  def delMin(self):
    """Removes and returns a smallest key on this priority queue."""
    if self.isEmpty(): raise Exception("Priority queue underflow")
    self._exch(1, self.N)
    min_key = self.pq[self.N]
    self.N -= 1
    self._sink(1)
    self.pq[self.N+1] = None # avoid loitering and help with garbage collection
    if self.N > 0 and (self.N == (len(self.pq) - 1) / 4): 
      self._resize(len(self.pq)/2)
    assert self._isMinHeap()
    return min_key

  def _swim(self, k):
    """Restore heap invariant by 'swimming' up large values."""
    while k > 1 and self._greater(k/2, k):
      self._exch(k, k/2)
      k = k/2

  def _sink(self, k):
    """Restore heap invariant by 'sinking' down small values."""
    while 2*k <= self.N:
      j = 2*k
      if j < self.N and self._greater(j, j+1):
        j += 1
      if not self._greater(k, j): 
        break
      self._exch(k, j)
      k = j

  def __str__(self): return "MinPQ({N}): {PQ}".format(N=self.N, PQ=self.pq)

  #***************************************************************************
  #* Helper functions for compares and swaps.
  #***************************************************************************
  def _greater(self, i, j):
    if self.comparator is None:
      return self.pq[i] > self.pq[j]
    else:
      return comparator.compare(self.pq[i], self.pq[j]) > 0;

  def _exch(self, i, j):
    self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

  def _isMinHeap(self, k=1):
    """is subtree of pq[1..N] rooted at k a min heap?"""
    if k > self.N: 
      return True
    left = 2*k 
    right = left + 1
    if left  <= self.N and self._greater(k, left):  return False;
    if right <= self.N and self._greater(k, right): return False;
    return self._isMinHeap(left) and self._isMinHeap(right)

  def __iter__(self):
    pq_copy = copy.deepcopy(self)
    while(not pq_copy.isEmpty()):
      yield pq_copy.delMin()


# Last updated: Sat Sep 26 08:34:31 EDT 2015.
