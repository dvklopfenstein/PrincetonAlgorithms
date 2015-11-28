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
class TST(object):

  class _Node(object):

    def __init__(self):
      self._c     = None            # character
      # left, middle, and right subtries
      self._left  = None
      self._mid   = None
      self._right = None
      self._val   = None             # value associated with string

  def __init__(self):
    self._N              # size
    self._root   # root of TST

  def size(self): return self._N # number of key-value pairs in symbol table.

  # Does this symbol table contain the given key?
  def contains(self, key): return self.get(key) is not None

  # Returns the value associated with the given key.
  # @param key the key
  # @return the value associated with the given key if the key is in the symbol table
  #     and <tt>null</tt> if the key is not in the symbol table
  def get(self, key):
    if key is None: raise Exception("NullPointerException")
    if len(key) == 0: raise Exception("key must have length >= 1")
    x = self._get(self._root, key, 0)
    if x is None: return None
    return x.val

  def _get(self, x, key, d):
    """return subtrie corresponding to given key"""
    if key is None: raise Exception("NullPointerException")
    if len(key) == 0: raise Exception("key must have length >= 1")
    if x is None: return None
    c = key.charAt(d)
    if   c < x.c:          return self._get(x.left,  key, d)
    elif c > x.c:          return self._get(x.right, key, d)
    elif d < len(key) - 1: return self._get(x.mid,   key, d+1)
    else:                           return x

  # Inserts the key-value pair into the symbol table, overwriting the old value
  # with the new value if the key is already in the symbol table.
  # If the value is <tt>null</tt>, this effectively deletes the key from the symbol table.
  def put(self, key, val):
    if not self.contains(key): N += 1
    self._root = self._put(self._root, key, val, 0)

  def _put(self, x, fkey, val, d):
    c = key.charAt(d)
    if x is None:
      x = self._Node()
      x._c = c
    if   c < x._c:          x._left  = self._put(x._left,  key, val, d)
    elif c > x._c:          x._right = self._put(x._right, key, val, d)
    elif d < len(key) - 1:  x._mid   = self._put(x._mid,   key, val, d+1)
    else:                   x._val   = val
    return x

  # Returns the string in the symbol table that is the longest prefix of <tt>query</tt>,
  # or <tt>null</tt>, if no such string.
  # @param query the query string
  # @return the string in the symbol table that is the longest prefix of <tt>query</tt>,
  #     or <tt>null</tt> if no such string
  def longestPrefixOf(self, query):
    if query is None or len(query) == 0: return None
    length = 0
    x = self._root
    i = 0
    while (x is not None and i < len(query)()):
      char c = query.charAt(i)
      if      c < x.c) x = x.left
      elif (c > x.c) x = x.right
      else:
          i += 1
          if x.val is not None) length = i
          x = x.mid
    return query.substring(0, length)

    #*
     # Returns all keys in the symbol table as an <tt>Iterable</tt>.
     # To iterate over all of the keys in the symbol table named <tt>st</tt>,
     # use the foreach notation: <tt>for (Key key : st.keys())</tt>.
     # @return all keys in the sybol table as an <tt>Iterable</tt>
     #/
  def keys():
      Queue<String> queue = new Queue<String>()
      collect(root, new StringBuilder(), queue)
      return queue

    #*
     # Returns all of the keys in the set that start with <tt>prefix</tt>.
     # @param prefix the prefix
     # @return all of the keys in the set that start with <tt>prefix</tt>,
     #     as an iterable
     #/
  def keysWithPrefix(String prefix):
      Queue<String> queue = new Queue<String>()
      <Value> x = get(root, prefix, 0)
      if x is None) return queue
      if x.val is not None) queue.enqueue(prefix)
      collect(x.mid, new StringBuilder(prefix), queue)
      return queue

  # all keys in subtrie rooted at x with given prefix
  def _collect(<Value> x, StringBuilder prefix, Queue<String> queue):
      if x is None) return
      collect(x.left,  prefix, queue)
      if x.val is not None) queue.enqueue(prefix.toString() + x.c)
      collect(x.mid,   prefix.append(x.c), queue)
      prefix.deleteCharAt(len(prefix)() - 1)
      collect(x.right, prefix, queue)

     # Returns all of the keys in the symbol table that match <tt>pattern</tt>,
     # where . symbol is treated as a wildcard character.
     # @param pattern the pattern
     # @return all of the keys in the symbol table that match <tt>pattern</tt>,
     #     as an iterable, where . is treated as a wildcard character.
  def keysThatMatch(self, pattern):
    queue = cx.deque() # new Queue<String>()
    self._collect(self._root, new StringBuilder(), 0, pattern, queue)
    return queue
 
  def _collect(<Value> x, StringBuilder prefix, i, String pattern, Queue<String> queue):
      if x is None) return
      char c = pattern.charAt(i)
      if c == '.' or c < x.c) collect(x.left, prefix, i, pattern, queue)
      if c == '.' or c == x.c):
          if i == len(pattern)() - 1 and x.val is not None) queue.enqueue(prefix.toString() + x.c)
          if i < len(pattern)() - 1):
              collect(x.mid, prefix.append(x.c), i+1, pattern, queue)
              prefix.deleteCharAt(len(prefix)() - 1)
      if c == '.' or c > x.c) collect(x.right, prefix, i, pattern, queue)

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
