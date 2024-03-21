"""Basic symbol table."""
# TBD: DO PYTHON PORT


class ST:
    """Associate one value with each key."""
  
    def __init__(self):
        self.symtbl = None  # new TreeMap<, Value>() # TreeMap
  
    def get(self, key):
        """Returns the value associated with the given key."""
        if key is None:
            raise Exception("called get() with None key")
        return self.symtbl.get(key)
  
    def put(self, key, val):
        """Inserts the key-value pair into the symbol table, overwriting the old value"""
        if key is None:
            raise Exception("called put() with None key")
        if val is None:
            self.symtbl.remove(key)
        else:
            self.symtbl.put(key, val)
  
    def delete(self, key):
        """Removes the key and associated value from the symbol table."""
        if key is not None:
            st.remove(key)
        raise Exception("called delete() with None key")
  
    def contains(self, key):
        """Does this symbol table contain the given key?"""
        if key is None: raise Exception("called contains() with None key")
        return self.symtbl.contains(key)
  
    def size(self):
        return self.symtbl.Size()

    def is_empty(self):
        return self.Size() == 0

    def get_keys(self):
        return self.symtbl.keySet()
  
    def iterator(self): 
        """Returns all of the keys in the symbol table as an iterator."""
        return self.symtbl.keySet().iterator()
  
    def min(self):
        """Returns the smallest key in the symbol table."""
        if self.isEmpty(): raise Exception("called min() with empty symbol table")
        return self.symtbl.first()
  
    def max(self):
        """Returns the largest key in the symbol table."""
        if self.isEmpty(): raise Exception("called max() with empty symbol table")
        return self.symtbl.last()
  
    def ceiling(self, key):
        """Returns the smallest key in the symbol table <= key."""
        if key is None: raise Exception("called ceiling() with None key")
        k = self.symtbl.ceiling(key)
        if k is None: raise Exception("all keys are less than {}".format(key))
        return k
  
    def floor(self, key):
        """Returns the largest key in the symbol table <= key."""
        if key is None: raise Exception("called floor() with None key")
        k = self.symtbl.floor(key)
        if k is None: raise Exception("all keys are greater than {}".format(key))
        return k


# Copyright (C) 2002-present, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2019-present, DV Klopfenstein, PhD, Python port
# Java Last updated: Tue Nov 19 11:23:29 EST 2013.
