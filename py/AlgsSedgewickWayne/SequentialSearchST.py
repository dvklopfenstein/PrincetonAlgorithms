
from AlgsSedgewickWayne.Queue import Queue

class SequentialSearchST(object):

  class _Node:
    """a helper linked list data type."""

    def __init__(self, key, val, nxt):
      self._key  = key
      self._val  = val
      self._next = nxt

  def __init__(self):
    self._N = 0        # number of key-value pairs
    self._first = None # the linked list of key-value pairs

  def size(self): return self._N
  def isEmpty(self): return self.size() == 0
  def contains(self, key): return self.get(key) is not None

  def get(self, key):
    """Returns the value associated with the given key. None if key is not present."""
    x = self._first # loop thru: first -> end
    while x is not None:
      if key == x._key:
        return x._val
      x = x._next
    return None # key is not in symbol table

  def put(self, key, val):
    """Inserts the key-value pair into the symbol table, overwriting the old value if present."""
    if val is None:
      self.delete(key)
      return

    x = self._first # loop thru: first -> end
    while x is not None:
      if key == x._key:
        x._val = val
        return
      x = x._next
    self._first = self._Node(key, val, self._first)
    self._N += 1

  def delete(self, key):
    """Removes the key and associated value from the symbol table."""
    self._first = self._delete(self._first, key)

  def _delete(self, x, key):
    """delete key in linked list beginning at x."""
    # warning: function call stack too large if table is large
    if x is None: return None
    if key == x._key:
      self._N -= 1
      return x._next
    x._next = delete(x._next, key)
    return x

  def keys(self):
    """Returns all keys in the symbol table as an Iterable."""
    queue = Queue()
    x = self._first # loop thru: first -> end
    while x is not None:
      queue.enqueue(x._key)
      x = x._next
    return queue

  def __iter__(self):
    curr = self._first
    while curr is not None:
      key_val = (curr._key, curr._val)
      curr = curr._next
      yield key_val

#  Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-201r6 Python Implementation, DV Klopfenstein
