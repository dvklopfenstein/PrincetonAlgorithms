"""Basic symbol table."""
# TBD: DO PYTHON PORT

class ST:
  """Associate one value with each key."""

  def __init__(self):
      self.st = None  # new TreeMap<, Value>() # TreeMap

  def get(self, key):
    """Returns the value associated with the given key."""
    if key is None: raise Exception("called get() with None key")
    return st.get(key)

  def put(self, key, val):
    """Inserts the key-value pair into the symbol table, overwriting the old value"""
    if key is None: raise Exception("called put() with None key")
    if val is None: self.st.remove(key)
    else:           self.st.put(key, val)

  def delete(self, key):
    """Removes the key and associated value from the symbol table."""
    if key is None: raise Exception("called delete() with None key")
    st.remove(key)

  def contains(self, key):
    """Does this symbol table contain the given key?"""
    if key is None: raise Exception("called contains() with None key")
    return self.st.contains(key)

  def Size(self): return self.st.Size()
  def isEmpty(self): return self.Size() == 0
  def keys(self): return self.st.keySet()

  def iterator(self): 
    """Returns all of the keys in the symbol table as an iterator."""
    return self.st.keySet().iterator()

  def Min(self):
    """Returns the smallest key in the symbol table."""
    if self.isEmpty(): raise Exception("called min() with empty symbol table")
    return self.st.first()

  def Max(self):
    """Returns the largest key in the symbol table."""
    if self.isEmpty(): raise Exception("called max() with empty symbol table")
    return self.st.last()

  def Ceiling(self, key):
    """Returns the smallest key in the symbol table <= key."""
    if key is None: raise Exception("called ceiling() with None key")
    k = self.st.ceiling(key)
    if k is None: raise Exception("all keys are less than {}".format(key))
    return k

  def Floor(self, key):
    """Returns the largest key in the symbol table <= key."""
    if key is None: raise Exception("called floor() with None key")
    k = self.st.floor(key)
    if k is None: raise Exception("all keys are greater than {}".format(key))
    return k

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2015, DV Klopfenstein, Python port
# Java Last updated: Tue Nov 19 11:23:29 EST 2013.
