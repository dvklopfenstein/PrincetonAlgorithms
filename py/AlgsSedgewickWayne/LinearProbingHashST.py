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

# Algs 1, week 6 Lecture: Linear Probing (14:37)

# LINEAR PROBING HASH TABLE SUMMARY
#   HASH: Map key to integet i between 0 and M-1.
#   INSERT: Put at table index i if free; if not try i+1, i+2, etc.
#   SEARCH: Search table index i; if occupied but no match, try i+1, i+2, etc.
# NOTE: Array size M MUST BE greater than number of key-value pairs N.
# A good idea to ensure it stays half full. (3/2 for a hit, 5/2 for a miss)

# KNUTH'S PARKING PROBLEM:
# MODEL: Cars arrive at one-way street with M parking spaces.
# Each desires a random space: i if space i is taken, try i+1, i+2, etc.
# Q: What is the mean displacement of a car? 
#
# If every car starts looking for a parking place at a random time (hashing fnc),
# how far do they have to go to look for a place?
# 
# HALF-FULL. With M/2 cars, mean displacement is ~3/2
# FULL. With M cars, mean displacement is ~sqrt(pi*M/8)

# QUESTION: What is the average running time of delete in a linear-probing hash table?
# Assumt that your hash function satidfies the uniform hashing assumption and that the 
# hash table is at most 50% full.
# ANSWER: linear
# EXPLANATION: The easiest way to implement delete is to find and remove the
# key-value pair and then to reinsert all of the key-value pairs in the same
# cluster that appear after the deleted key-value pair. If the hash table
# doesn't get too full, the expected number of key-value pairs to reinsert 
# will be a small constant.
#
# An alternative is to flag the deleted linear probing talbe entry so that it is 
# skipped over during a search but is used for an insertion. If there are too
# many flagged entries, create a new hash table and rehash all key-value pairs.


#  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
#  Copyright 2014-2015, DV Klopfenstein, Python implementation.
