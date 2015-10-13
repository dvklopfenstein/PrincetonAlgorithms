"""Avoiding collision through linear probing."""

import sys
from AlgsSedgewickWayne.Queue import Queue

class LinearProbingHashST(object):
  INIT_CAPACITY = 4

  def __init__(self, capacity=None):
    if capacity is None:
      capacity = self.INIT_CAPACITY
    self._N = 0  # number of key-value pairs in the symbol table
    self._M = capacity # size of linear probing table
    self._keys = [None for i in range(self._M)] # the keys
    self._vals = [None for i in range(self._M)] # the values

  def size(self): return self._N
  def isEmpty(self): return self.size() == 0
  def contains(self, key): return self.get(key) is not None

  def _hash(self, key):
    """hash function for keys - returns value between 0 and self._M-1."""
    return (hash(key) & 0x7fffffffffffffff) % self._M

  def _resize(self, capacity):
    """resize the hash table to the given capacity by re-hashing all of the self._keys"""
    temp = LinearProbingHashST(capacity)
    for i in range(self._M):
      if self._keys[i] is not None:
        temp.put(self._keys[i], self._vals[i])
    self._keys = temp._keys
    self._vals = temp._vals
    self._M    = temp._M

  def put(self, key, val):
    """Inserts the key-val pair into the sym tbl, overwriting the old val, if needed"""
    if val is None:
      self.delete(key)
      return

    # double table size if 50% full
    if self._N >= self._M/2: self._resize(2*self._M)

    i = self._hash(key)
    while self._keys[i] is not None:
      if self._keys[i] == key:
        self._vals[i] = val
        return
      i = (i + 1) % self._M
    self._keys[i] = key
    self._vals[i] = val
    self._N += 1

  def get(self, key):
    """Returns the value associated with the given key."""
    i = self._hash(key)
    while self._keys[i] is not None:
      if self._keys[i] == key:
        return self._vals[i]
      i = (i + 1) % self._M
    return None

  def delete(self, key):
    """Removes the key and associated value from the symbol table."""
    if not contains(key): return

    # find position i of key
    i = self._hash(key)
    while not key == self._keys[i]:
      i = (i + 1) % self._M

    # delete key and associated value
    self._keys[i] = None
    self._vals[i] = None

    # rehash all self._keys in same cluster
    i = (i + 1) % self._M
    while self._keys[i] is not None:
      # delete self._keys[i] an self._vals[i] and reinsert
      keyToRehash = self._keys[i]
      valToRehash = self._vals[i]
      self._keys[i] = None
      self._vals[i] = None
      self._N -= 1
      self.put(keyToRehash, valToRehash)
      i = (i + 1) % self._M

    self._N -= 1

    # halves size of array if it's 12.5% full or less
    if self._N > 0 and self._N <= self._M/8: self._resize(self._M/2)
    assert self._check()


  def keys(self):
    """Returns all self._keys in the symbol table as an Iterable."""
    queue = Queue()
    for i in range(self._M):
      if self._keys[i] is not None: queue.enqueue(self._keys[i])
    return queue

  def _check(self, prt=sys.stdout):
    """check - don't check after each put() - integrity not maintained during a delete()"""

    # check that hash table is at most 50% full
    if self._M < 2*self._N:
      prt.write("Hash table size self._M = {} array size self._N = {}\n".format(self._M, self._N))
      return False

    # check that each key in table can be found by get()
    for i in range(self._M):
      if self._keys[i] is None: continue
      elif self.get(self._keys[i]) != self._vals[i]:
        prt.write("get[{}] = {} self._vals[i] = {}\n".format(
          self._keys[i], self.get(self._keys[i]), self._vals[i]))
        return False
    return True

#  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
#  Copyright 2014-2015, DV Klopfenstein, Python implementation.
