# TBD Finish Python port
"""Ternary search trie (TST)."""

 #  The <tt>TST</tt> class represents an symbol table of key-value
 #  pairs, with string keys and generic values.
 #  It supports the usual <em>put</em>, <em>get</em>, <em>contains</em>,
 #  <em>delete</em>, <em>size</em>, and <em>is-empty</em> methods.
 #  It also provides character-based methods for finding the string
 #  in the symbol table that is the <em>longest prefix</em> of a given prefix,
 #  finding all strings in the symbol table that <em>start with</em> a given prefix,
 #  and finding all strings in the symbol table that <em>match</em> a given pattern.
 #  A symbol table implements the <em>associative array</em> abstraction:
 #  when associating a value with a key that is already in the symbol table,
 #  the convention is to replace the old value with the new value.
 #  Unlike {@link java.util.Map}, this class uses the convention that
 #  values cannot be <tt>null</tt>&mdash;setting the
 #  value associated with a key to <tt>null</tt> is equivalent to deleting the key
 #  from the symbol table.

import collections as cx

class TST(object):

  class _Node(object):

    def __init__(self, c):
      self._c     = c # character
      self._left  = None
      self._mid   = None
      self._right = None
      self._val   = None             # value associated with string

    def __str__(self):
      p = lambda n: '-' if n is None else n._c
      return ''.join(["{}:{} (".format(self._c, '-' if self._val is None else self._val),
        p(self._left), p(self._mid), p(self._right), ')'])

  def __init__(self):
    self._N = 0       # size
    self._root = None # root of TST

  def size(self): return self._N # number of key-value pairs in symbol table.
  def contains(self, key): return self.get(key) is not None # symbol table contain the given key?

  # Returns the value associated with the given key.
  # @param key the key
  # @return the value associated with the given key if the key is in the symbol table
  #     and <tt>null</tt> if the key is not in the symbol table
  def get(self, key):
    if key is None: raise Exception("NullPointerException")
    if len(key) == 0: raise Exception("key must have length >= 1")
    x = self._get(self._root, key, 0)
    if x is None: return None
    return x._val

  def _get(self, x, key, d):
    """return subtrie corresponding to given key"""
    if key is None: raise Exception("NullPointerException")
    if len(key) == 0: raise Exception("key must have length >= 1")
    if x is None: return None
    c = key[d]
    if   c < x._c:         return self._get(x._left,  key, d)
    elif c > x._c:         return self._get(x._right, key, d)
    elif d < len(key) - 1: return self._get(x._mid,   key, d+1)
    else:                  return x

  # Inserts the key-value pair into the symbol table, overwriting the old value
  # with the new value if the key is already in the symbol table.
  # If the value is <tt>null</tt>, this effectively deletes the key from the symbol table.
  def put(self, key, val):
    if not self.contains(key): self._N += 1
    print "{} KEY({})".format(val, key)
    self._root = self._put(self._root, key, val, 0)

  def _put(self, x, key, val, d):
    c = key[d]
    print "{} {} {} key({})".format(val, key, d, c)
    if x is None:
      x = self._Node(c)
    if   c < x._c:         x._left  = self._put(x._left,  key, val, d)
    elif c > x._c:         x._right = self._put(x._right, key, val, d)
    elif d < len(key) - 1: x._mid   = self._put(x._mid,   key, val, d+1)
    else:                  x._val   = val
    return x

  # Returns the string in the symbol table that is the longest prefix of <tt>query</tt>,
  # or <tt>null</tt>, if no such string.
  # @param query the query string
  # @return the string in the symbol table that is the longest prefix of <tt>query</tt>,
  #     or <tt>null</tt> if no such string
  def longestPrefixOf(self, query):
    if query is None or not query: return None
    length = 0
    x = self._root
    i = 0
    while x is not None and i < len(query):
      c = query[i]
      if   c < x._c: x = x._left
      elif c > x._c: x = x._right
      else:
        i += 1
        if x._val is not None: length = i
        x = x._mid
    return query.substring(0, length)

  def keys(self):
    """Returns all keys in the symbol table as an Iterable."""
    queue = cx.deque() # new Queue<String>()
    prefix = []
    self.collect("R", self._root, prefix, queue)
    return queue

  def collect(self, name, x, prefix, queue):
    """all keys in subtrie rooted at x with given prefix"""
    print "\nVVVV", name, x, prefix, queue
    if x is None: return
    print "WWWW", name, x, prefix, queue
    self.collect("L", x._left,  prefix, queue)
    print "XXXX", name, x, prefix, queue
    if x._val is not None: queue.append(''.join([str(prefix), x._c])) # enqueue(str(prefix) + x.c)
    self.collect("M", x._mid,   prefix.append(x._c), queue)
    prefix.pop()
    self.collect("R", x._right, prefix, queue)

  def _collect(self, x, prefix, i, pattern, queue):
    if x is None: return
    c = pattern.charAt(i)
    if c == '.' or c  < x._c: self._collect(x._left, prefix, i, pattern, queue)
    if c == '.' or c == x._c:
      if i == len(pattern) - 1 and x.val is not None: queue.append(prefix.toString() + x.c)
      if i <  len(pattern) - 1:
        self._collect(x._mid, prefix.append(x._c), i+1, pattern, queue)
        prefix.deleteCharAt(len(prefix) - 1)
    if c == '.' or c > x._c: self._collect(x.right, prefix, i, pattern, queue)

  def keysThatMatch(self, pattern):
    """Returns all of the keys in the symbol table that match pattern; . symbol is a wildcard"""
    queue = cx.deque() # new Queue<String>()
    self._collect(self._root, [], 0, pattern, queue)
    return queue
 
  def keysWithPrefix(self, prefix):
    """Returns all of the keys in the set that start with prefix."""
    queue = cx.deque() # new Queue<String>()
    x = self._get(self._root, prefix, 0)
    if x is None: return queue
    if x._val is not None: queue.append(prefix) # enqueue(prefix)
    self.collect(x._mid, [prefix], queue)
    return queue

# -----------------------------------------------------------------------------
# TERNARY SEARCH TRIES (22:42)

# TST vs. HASHING (20:37)
#
# HASHING
#   * Need to examine entire key
#   * Search hits and misses cost about the same
#   * Performance relies on hash function
#   * Does not support ordered symbol table operations.
#   * Hashing is only good for Search and Insert
#
# TSTs
#   * Works only for strings (or digital keys).
#   * Only examines just enough key characters.
#   * Search miss may involve only a few characters.
#   * Supports ordered symbol table operations (plus others!)
# 
# BOTTOM LINE: TSTs are:
#   * Faster than hashing (especiallyforsearch misses).
#   * More flexible than red-black BSTs.

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2002-2016, DV Klopfenstein, Python port
