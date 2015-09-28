"""Binary Search Tree."""
# TBD: FINISH PYTHON PORT

class BST(object):

  def __init__(self):
    self.root = None      # root of BST is a _Node

  class _Node:
    def __init__(self, key, val, N):
      self.key   = key  # Key   sorted by key
      self.val   = val  # Value associated data
      self.left  = None # Node  left and right subtrees
      self.right = None # Node  and right subtrees
      self.N     = N    # number of nodes in subtree

  def isEmpty(self): return self.Size() == 0

  # return number of key-value pairs in BST
  def Size(self): return self._Size(self, root)

  # return number of key-value pairs in BST rooted at x
  def _Size(self, x): # Node
    if x is None: return 0
    else: return x.N

  def contains(self, key):
    """does there exist a key-value pair with given key?"""
    return self.get(self, key) is not None

  def get(self, key):
    """return value associated with the given key, or None if no such key exists"""
    return self._get(self, root, key)

  def _get(self, x, key):
    """Search for key. Return assc. value if found, return None if not found"""
    if x is None: return None
    if   key < x.key: return self.get(self, x.left,  key)
    elif key > x.key: return self.get(self, x.right, key)
    else:             return x.val

  def put(self, key, val):
    """Insert key-value pair into BST. If key already exists, update with new value."""
    if val is None: self.delete(self, key); return
    self.root = self._put(self.root, key, val)
    assert self._check()

  def _put(self, x, key, val):
    """Recursive put which returns node."""
    if x is None: return self._Node(key, val, 1)
    if   key < x.key:  x.left  = self.put(x.left,  key, val)
    elif key > x.key:  x.right = self.put(x.right, key, val)
    else:              x.val   = val # Reset value of already existing node
    x.N = 1 + self._Size(x.left) + self._Size(x.right)
    return x

  #**********************************************************************
  #  Delete
  #**********************************************************************/
  def deleteMin(self):
      if self.isEmpty(self): raise Exception("deleteMin Symbol table underflow")
      root = self.deleteMin(self, root)
      assert self._check(self)

  def _deleteMin(self, x):
      if x.left is None: return x.right
      x.left = self.deleteMin(x.left)
      x.N = Size(x.left) + self.Size(x.right) + 1
      return x

  def deleteMax(self):
      if self.isEmpty(self): raise Exception("deleteMax Symbol table underflow")
      self.root = self.deleteMax(self.root)
      assert self._check(self)

  def _deleteMax(self, x):
      if x.right is None: return x.left
      x.right = self.deleteMax(x.right)
      x.N = Size(x.left) + Size(x.right) + 1
      return x

  def delete(self, key):
      self.root = self.delete(self.root, key)
      assert self._check()

  def _delete(self, x, key):
      if x is None: return None
      #cmp = key.compareTo(x.key)
      if   key < x.key: x.left  = _delete(x.left,  key)
      elif key > x.key: x.right = _delete(x.right, key)
      else:
          if x.right is None: return x.left
          if x.left  is None: return x.right
          t = x
          x = self.Min(self, t.right)
          x.right = self._deleteMin(self, t.right)
          x.left = t.left
      x.N = self._Size(x.left) + self._Size(x.right) + 1
      return x


 #**********************************************************************
  #  Min, Max, floor, and ceiling
  #**********************************************************************/
  def Min(self):
      if self.isEmpty(): return None
      return Min(root).key

  def _Min(self, x):
      if x.left is None: return x
      else:              return self._Min(self, x.left)

  def Max(self):
      if self.isEmpty(): return None
      return self.Max(root).key

  def _Max(self, x):
      if x.right is None: return x
      else:               return self._Max(self, x.right)

  def floor(self, key):
      x = self._floor(self, root, key)
      if x is None: return None
      else: return x.key

  def _floor(self, x, key):
      if x is None: return None
      #cmp = key.compareTo(x.key)
      if key == x.key: return x
      if key <  x.key: return self._floor(self, x.left, key)
      t = self._floor(self, x.right, key)
      if t is not None: return t
      else: return x

  def ceiling(self, key):
      x = self._ceiling(self, root, key)
      if x is None: return None
      else: return x.key

  def _ceiling(self, x, key):
      if x is None: return None
      #cmp = key.compareTo(x.key)
      if key == x.key: return x
      if key <  x.key:
          t = self._ceiling(self, x.left, key)
          if t is not None: return t
          else: return x
      return self._ceiling(self, x.right, key)

  #**********************************************************************
  #  Rank and selection
  #**********************************************************************/
  def select(self, k):
    if k < 0 or k >= self.Size(self): return None
    x = self._select(self, root, k)
    return x.key

  # Return key of rank k.
  def _select(self, x, k):
    if x is None: return None
    t = self._Size(self, x.left)
    if   t > k: return self._select(self, x.left,  k)
    elif t < k: return self._select(self, x.right, k-t-1)
    else:       return x

  def rank(self, key):
    return self._rank(self, key, root)

  def _rank(self, key, x):
    """Number of keys in the subtree less than key."""
    if x is None: return 0
    #cmp = key.compareTo(x.key)
    if   key < x.key: return self._rank(self, key, x.left)
    elif key > x.key: return 1 + Size(x.left) + rank(key, x.right)
    else:             return Size(x.left)

  #**********************************************************************
  #  Range count and range search.
  #**********************************************************************/
  def keys(self):
    return self.keys(self.Min(), self.Max())

  def keys(self, lo, hi):
    import Queue
    queue = Queue()
    self.keys(self, root, queue, lo, hi)
    return queue

  def _keys(self, x, queue, lo, hi):
    if x is None: return
    cmplo = lo.compareTo(x.key)
    cmphi = hi.compareTo(x.key)
    if cmplo < 0: keys(x.left, queue, lo, hi)
    if cmplo <= 0 and cmphi >= 0: queue.enqueue(x.key)
    if cmphi > 0: keys(x.right, queue, lo, hi)

  def Size(self, lo, hi):
    if lo.compareTo(hi) > 0: return 0
    if contains(hi):  return self.rank(self, hi) - self.rank(self, lo) + 1
    else:             return self.rank(self, hi) - self.rank(self, lo)


  # height of this BST (one-node tree has height 0)
  def height(self, root): return self.height(self, root)
  def _height(self, x):
    if x is None: return -1
    return 1 + Math.Max(self.height(self, x.left), self.height(self, x.right))


  # level order traversal
  def levelOrder():
    import Queue
    keys  = Queue() # new Queue<Key>()
    queue = Queue() # new Queue<Node>()
    queue.enqueue(root)
    while not queue.self.isEmpty():
        x = queue.dequeue()
        if x is None: continue
        keys.enqueue(x.key)
        queue.enqueue(x.left)
        queue.enqueue(x.right)
    return keys

  #************************************************************************
  #  Check integrity of BST data structure
  #************************************************************************/
  def _check(self):
    if not self._isBST():            print "Not in symmetric order"
    if not self._isSizeConsistent(): print "Subtree counts not consistent"
    if not self._isRankConsistent(): print "Ranks not consistent"
    return self._isBST() and self.isSizeConsistent() and self.isRankConsistent()

  # does this binary tree satisfy symmetric order?
  # Note: this test also ensures that data structure is a binary tree since order is strict
  #def _isBST(self):
  #    return isBST(root, None, None)

  # is the tree rooted at x a BST with all keys strictly between Min and Max
  # (if Min or Max is None, treat as empty constraint)
  # Credit: Bob Dondero's elegant solution
  def _isBST(self, x=None, Min=None, Max=None):
    if x is None:
      x = self.root
    if x is None: return True
    if Min is not None and x.key.compareTo(Min) <= 0: return False
    if Max is not None and x.key.compareTo(Max) >= 0: return False
    return self._isBST(x.left, Min, x.key) and self._isBST(x.right, x.key, Max)

  # are the Size fields correct?
  def _isSizeConsistent(self): return self._isSizeConsistent(self.root)
  def _isSizeConsistent(self, x):
      if x is None: return True
      if x.N != self.Size(x.left) + self.Size(x.right) + 1: return False
      return self._isSizeConsistent(x.left) and self._isSizeConsistent(x.right)

  # check that ranks are consistent
  def _isRankConsistent(self):
      S = self.Size()
      for i in range(S):
          if i != self.rank(self.select(i)): return False

      #for (Key key : keys())
      #    if key.compareTo(select(rank(key))) != 0: return False
      key_queue = self.keys()
      for i in range(key_queue.size()):
        key = key_queue[i]
        if key != self.select( self.rank(key) ): return False

      return True

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Java Last updated: Tue Nov 19 01:56:07 EST 2013.


# Algorithms, Part 1 from Princeton University
# by Kevin Wayne, Robert Sedgewick
# https://class.coursera.org/algs4partI-005/lecture/46
# Alg1, Week 4 Lecture Binary Search Trees (19:56)

# --------------------------------------------------------------------------
# 00:08 Binary Search Trees are a classic data structure that will enable us
# to provide an efficient implementations of Symbol Table Algorithms
#
# 00:25 With Heaps we talk about implicit representations with an array.
# With Binary Search Tree actual explicit tree data structures.

# --------------------------------------------------------------------------
# 00:34 BINARY SEARCH TREES
# DEFINITION: A BST is a BINARY TREE in SYMMETRIC ORDER.
#
# A BINARY TREE is either:
#   * Empty
#   * Two disjoint trees (left and right).
#
# A BINARY SEARCH TREE is in SYMMETRIC ORDER: Each node has a key,
# and every node's key is:
#   * Larger  than all keys in its left  subtree
#   * Smaller than all keys in its right subtree

# 01:45 Different from a heap.  HEAPs had every node larger than its children.

# QUESTION: Suppose that N distinct keys are inserted into a binary
# search tree in random order. What is the expected number of 
# compares to search for one of the N keys?
# ANSWER: logorithmic.

