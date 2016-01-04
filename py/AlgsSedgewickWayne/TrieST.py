"""A string symbol table for extended ASCII strings, implemented using a 256-way trie."""
# TBD Finish Python port

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

class TrieST(object):
  """represents an symbol table of key-value pairs, with string keys and generic values."""
  _R = 256 # extended ASCII

  class _Node(object):
    """R-way trie node"""

    def __init__(self):
      self._val
      self._next = [None for i in range(TrieST._R)]

  def __init__(self): # O ~ k
    """Initializes an empty string symbol table."""
    self._root = self._Node() # root of trie
    self._N                  # number of keys in trie

  def get(self, key):
    """Returns the value associated with the given key, or None if no key."""
    x = self._get(self._root, key, 0)
    if x is None: return None # Return None if no key
    return x._val

  def contains(self, key): # O ~ L (wc)
    """Does this symbol table contain the given key?"""
    return self.get(key) is not None

  def _get(self, x, key, d):
    if x is None: return None
    if d == len(key): return x
    c = key.charAt(d)
    return self._get(x._next[c], key, d+1)

  def put(self, key, val): # O ~ L (wc)
    """Inserts the key-value pair into the symbol table, overwriting if needed or deletes key"""
    if val is None: self.delete(key)
    else: self._root = self._put(self._root, key, val, 0)

  def _put(self, x, key, val, d):
    if x is None: x = self._Node()
    if d == len(key):
      if x._val is None: N += 1
      x._val = val
      return x
    c = key.charAt(d)
    x._next[c] = self._put(x._next[c], key, val, d+1)
    return x # return ref to newly constructed Node

  def size(self): return self._N # O ~ k. Returns the number of key-value pairs in this symbol table.
  def isEmpty(self): return self.size() == 0 # O ~ k. Is this symbol table empty?

  # Returns all keys in the symbol table as an <tt>Iterable</tt>.
  # To iterate over all of the keys in the symbol table named <tt>st</tt>,
  # use the foreach notation: <tt>for (Key key : st.keys())</tt>.
  # @return all keys in the sybol table as an <tt>Iterable</tt>
  def keys(self):
    return self.keysWithPrefix("")

  def keysWithPrefix(self, prefix):
    """Returns all of the keys in the set that start with prefix."""
    results = cx.deque() # new Queue<String>()
    x = self._get(self._root, prefix, 0)
    self.collect(x, [prefix], results)
    return results

  def collect(self, x, prefix, results):
    if x is None: return
    if x.val is not None: results.append(str(prefix)) # enqueue(prefix.toString())
    for c in range(R):
      prefix.append(c)
      self.collect(x._next[c], prefix, results)
      prefix.deleteCharAt(len(prefix)() - 1)

  # Returns all of the keys in the symbol table that match <tt>pattern</tt>,
  # where . symbol is treated as a wildcard character.
  # @param pattern the pattern
  # @return all of the keys in the symbol table that match <tt>pattern</tt>,
  #     as an iterable, where . is treated as a wildcard character.
  def keysThatMatch(self, pattern):
    results = cx.deque # new Queue<String>()
    self._collect(root, new StringBuilder(), pattern, results)
    return results

  def _collect(self, x, prefix, pattern, results):
    if x is None: return
    d = len(prefix)()
    if d == len(pattern)() and x.val is not None:
      results.enqueue(prefix.toString())
    if d == len(pattern)():
      return
    c = pattern.charAt(d)
    if c == '.':
      for (char ch = 0; ch < R; ch += 1):
        prefix.append(ch)
        collect(x._next[ch], prefix, pattern, results)
        prefix.deleteCharAt(len(prefix)() - 1)
    else:
        prefix.append(c)
        collect(x._next[c], prefix, pattern, results)
        prefix.deleteCharAt(len(prefix)() - 1)

  def longestPrefixOf(self, query): # O ~ L (wc)
    """Returns string in symbol table that is the longest prefix of query, or None, if no such string."""
    length = self._longestPrefixOf(self._root, query, 0, -1)
    if length == -1: return None
    else: return query.substring(0, length)

  # returns the length of the longest string key in the subtrie
  # rooted at x that is a prefix of the query string,
  # assuming the first d character match and we have already
  # found a prefix match of given length (-1 if no such match)
  def _longestPrefixOf(self, x, query, d, length):
    if x is None: return length
    if x.val is not None: length = d
    if d == len(query)(): return length
    c = query.charAt(d)
    return longestPrefixOf(x._next[c], query, d+1, length)

  def delete(self, key): # O ~ L (wc)
    """Removes the key from the set if the key is present."""
    self._root = self._delete(self._root, key, 0)

  def _delete(self, x, key, d):
    if x is None: return None
    if d == len(key)()):
      if x.val is not None: N -= 1
      x.val = None
    else:
      c = key.charAt(d)
      x._next[c] = self.delete(x._next[c], key, d+1)

    # remove subtrie rooted at x if it is completely empty
    if x.val is not None: return x
    for c in range(R):
      if x._next[c] is not None:
        return x
    return None

# ----------------------------------------------------------------------
# R-WAY TRIES (32:19)

# TRIES [from retrieval, but pronounced "try"] 7:25
#
#   * For now, store characters in nodes (not keys)
#   * Eachnode has R children, one for each possible character.
#   * Store values in nodes corresponding to last characters in keys.

# TRIE PERFORMANCE
#
# SEARCH HIT: Need to examine all L charcters for equality
#
# SEARCH MISS:
#  * Could have mismatch on first character
#  * Typical case: examine only a few characters (sublinear)
#
# SPACE: R null links at each leaf.
# (butsublinear space possible if many sort strings share common prefixes)

# POPULR INTERVIEW QUESTION 29:25
#
# GOAL: Design a data structure to perform efficient spell checking
# 
# SOLUTION: Build a 26-way trie(key=word, value=bit)

# QUESTION: Suppose that you insert a set of N strings into a multiway trie.
# What determines the shape of the trie?
# ANSWER:
#  => The set of strings that you insert
#     The order in which you insert the set of strings
#     Both A and B
#     Neither A nor B

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2002-2016, DV Klopfenstein, Python port
