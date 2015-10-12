
from AlgsSedgewickWayne.Queue import Queue
from AlgsSedgewickWayne.SequentialSearchST import SequentialSearchST

class SeparateChainingHashST(object):
  _INIT_CAPACITY = 4

  # largest prime <= 2^i for i = 3 to 31
  # not currently used for doubling and shrinking
  # private static final int[] PRIMES =:
  #    7, 13, 31, 61, 127, 251, 509, 1021, 2039, 4093, 8191, 16381,
  #    32749, 65521, 131071, 262139, 524287, 1048573, 2097143, 4194301,
  #    8388593, 16777213, 33554393, 67108859, 134217689, 268435399,
  #    536870909, 1073741789, 2147483647
  # }
  def __init__(self, M=None):
    M = self._INIT_CAPACITY if M is None else M # hash table size
    self.N = 0 # number of key-value pairs
    self.M = M # hash table size
    self.st = [SequentialSearchST() for i in range(M)] # SequentialSearchST<, Value>[] st # array of linked-list symbol tables

  def _resize(self, chains):
    """resize the hash table to have the given number of chains b rehashing all of the keys."""
    temp = SeparateChainingHashST(chains)
    for i in range(M):
      for key in st[i].keys():
        temp.put(key, self.st[i].get(key))
    self.M  = temp.M
    self.N  = temp.N
    self.st = temp.st

  def _hash(self, key):
    """hash value between 0 and M-1."""
    return (hash(key) & 0x7fffffffffffffff) % self.M

  def size(self): return self.N
  def isEmpty(self): return self.size() == 0
  def contains(self, key): return self.get(key) is not None

  def get(self, key):
    """Returns the value associated with the given key."""
    i = self._hash(key)
    return self.st[i].get(key)

  def put(self, key, val):
    """Inserts the key-value pair into the symbol table, overwriting the old value if present."""
    if val is None:
      self.delete(key)
      return

    # double table size if average length of list >= 10
    if self.N >= 10*self.M: self.resize(2*self.M)

    i = self._hash(key)
    if not self.st[i].contains(key): self.N += 1
    self.st[i].put(key, val)

  def delete(self, key):
    """Removes the key and associated value from the symbol table, if the key is in the symbol tbl."""
    i = self._hash(key)
    if self.st[i].contains(key): self.N -= 1
    self.st[i].delete(key)

    # halve table size if average length of list <= 2
    if self.M > self._INIT_CAPACITY and self.N <= 2*self.M: self.resize(self.M/2)

  def keys(self):
    """return keys in symbol table as an Iterable."""
    queue = Queue()
    for i in range(self.M):
      for key in self.st[i].keys():
        queue.enqueue(key)
    return queue

#  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
#  Copyright 2014-2015, Python Implementation, DV Klopfenstein
