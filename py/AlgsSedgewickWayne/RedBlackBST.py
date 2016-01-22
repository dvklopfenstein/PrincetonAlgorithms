"""2-3 version of left-leaning red-black BST implemented with a symbol table."""
# TBD: finish Python implementation

 #  It supports the usual <em>put</em>, <em>get</em>, <em>contains</em>,
 #  <em>delete</em>, <em>size</em>, and <em>is-empty</em> methods.
 #  It also provides ordered methods for finding the <em>minimum</em>,
 #  <em>maximum</em>, <em>floor</em>, and <em>ceiling</em>.
 #  It also provides a <em>keys</em> method for iterating over all of the keys.
 #  A symbol table implements the <em>associative array</em> abstraction:
 #  when associating a value with a key that is already in the symbol table,
 #  the convention is to replace the old value with the new value.
 #  Unlike {@link java.util.Map}, this class uses the convention that
 #  values cannot be <tt>null</tt>&mdash;setting the
 #  value associated with a key to <tt>null</tt> is equivalent to deleting the key
 #  from the symbol table.

 #  This implementation uses a left-leaning red-black BST. It requires that
 #  the key type implements the <tt>Comparable</tt> interface and calls the
 #  <tt>compareTo()</tt> and method to compare two keys. It does not call either
 #  <tt>equals()</tt> or <tt>hashCode()</tt>.
 #  The <em>put</em>, <em>contains</em>, <em>remove</em>, <em>minimum</em>,
 #  <em>maximum</em>, <em>ceiling</em>, and <em>floor</em> operations each take
 #  logarithmic time in the worst case, if the tree becomes unbalanced.
 #  The <em>size</em>, and <em>is-empty</em> operations take constant time.
 #  Construction takes constant time.

 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/33balanced">Section 3.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #  For other implementations, see {@link ST}, {@link BinarySearchST},
 #  {@link SequentialSearchST}, {@link BST},
 #  {@link SeparateChainingHashST}, and {@link LinearProbingHashST},
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #/

class RedBlackBST(object):
  """2-3 tree implements balanced trees in guaranteed lgN time."""

  RED   = True
  BLACK = False

  def __init__(self):
    self._root;     # self._root of the BST

  class _Node:

    def __init__(self, key, val, color, N):
      self.key = key       # key
      self.val = val       # associated data
      self.left  = None    # links to the left and right subtrees
      self.right = None    # links to the left and right subtrees
      self.color = color   # Color of parent link
      self.N = N           # subtree count


  #**************************************************************************
  #  Node helper methods.
  #**************************************************************************/
  def _isRed(self, x):
    """is node x red; False if x is None ?"""
    return x is not None and x.color == RED

  def _size(self, x):
    """number of node in subtree rooted at x; 0 if x is None"""
    return x.N if x is not None else 0

  def size(self):
    """Returns the number of key-value pairs in this symbol table."""
    return self._size(self._root)

  def isEmpty(): return self._root is None


  #**************************************************************************
  #  Standard BST search.
  #**************************************************************************/

  def get(self, key):
    """Returns the value associated with the given key or None."""
    return self._get(self._root, key)

  def _get(self, x, key):
    """value associated with the given key in subtree rooted at x; None if no such key"""
    while x is not None:
      cmp_keys = compareTo_keys(key, x.key)
      if   cmp_keys < 0: x = x.left
      elif cmp_keys > 0: x = x.right
      else:              return x.val
    return None

  @staticmethod
  def compareTo_keys(keya, keyb): return ((keya > keyb) - (keya < keyb))

  def contains(self, key):
    """Does this symbol table contain the given key?"""
    return self._get(key) is not None

 #**************************************************************************
  #  Red-black tree insertion.
  #**************************************************************************/

  # Inserts the key-value pair into the symbol table, overwriting the old value
  # with the new value if the key is already in the symbol table.
  # If the value is <tt>null</tt>, this effectively deletes the key from the symbol table.
  def put(key, val):
    self._root = put(self._root, key, val)
    self._root.color = BLACK
    # assert check()

  def _put(self, h, key, val): 
    """insert the key-value pair in the subtree rooted at h"""
    if h is None: return self._Node(key, val, RED, 1)

    cmp_keys = compareTo_keys(key, x.key)
    if   cmp_keys < 0: h.left  = self._put(h.left,  key, val)
    elif cmp_keys > 0: h.right = self._put(h.right, key, val)
    else               h.val   = val

    # fix-up any right-leaning links
    if self._isRed(h.right) and  not self._isRed(h.left):      h = self._rotateLeft(h)
    if self._isRed(h.left)  and      self._isRed(h.left.left): h = self._rotateRight(h)
    if self._isRed(h.left)  and      self._isRed(h.right):     flipColors(h)
    h.N = self._size(h.left) + self._size(h.right) + 1

    return h

 #**************************************************************************
  #  Red-black tree deletion.
  #**************************************************************************/

  def deleteMin(self):
    """Removes the smallest key and associated value from the symbol table."""
    if self.isEmpty(): raise Exception("BST underflow")

    # if both children of self._root are black, set self._root to red
    if not self._isRed(self._root.left) and not self._isRed(self._root.right):
      self._root.color = RED

    self._root = self._deleteMin(self._root)
    if not isEmpty(): self._root.color = BLACK
    # assert check()

  def _deleteMin(self, h): 
    """delete the key-value pair with the minimum key rooted at h."""
    if h.left is None:
      return None

    if not self._isRed(h.left) and not self._isRed(h.left.left):
      h = self._moveRedLeft(h)

    h.left = self._deleteMin(h.left)
    return self._balance(h)

  def deleteMax(self):
    """Removes the largest key and associated value from the symbol table."""
    if self.isEmpty(): raise Exception("BST underflow")

    # if both children of self._root are black, set self._root to red
    if not self._isRed(self._root.left) and not self._isRed(self._root.right):
        self._root.color = RED

    self._root = self._deleteMax(self._root)
    if !isEmpty()) self._root.color = BLACK
    # assert check()

  def _deleteMax(self, h): 
    """delete the key-value pair with the maximum key rooted at h."""
    if self._isRed(h.left):
        h = self._rotateRight(h)

    if h.right is None:
        return None

    if not self._isRed(h.right) and not self._isRed(h.right.left):
        h = self._moveRedRight(h)

    h.right = self._deleteMax(h.right)

    return self._balance(h)

  def delete(self, key): 
    """Removes the key and associated value from the symbol table."""
    if not self.contains(key):
      sys.stdout.write("symbol table does not contain {KEY|\n".format(key))
      return

    # if both children of self._root are black, set self._root to red
    if not self._isRed(self._root.left) and not self._isRed(self._root.right))
      self._root.color = RED

    self._root = self._delete(self._root, key)
    if not self.isEmpty(): self._root.color = BLACK
    # assert check()

  def _delete(self, h, key): 
    """delete the key-value pair with the given key rooted at h."""
    # assert get(h, key) is not None

    if key < h.key:
      if not self._isRed(h.left) and not self._isRed(h.left.left):
        h = self._moveRedLeft(h)
      h.left = self._delete(h.left, key)
    else:
      if self._isRed(h.left):
        h = self._rotateRight(h)
      if key == h.key and h.right is None:
        return None
      if not self._isRed(h.right) and not self._isRed(h.right.left):
        h = self._moveRedRight(h)
      if key == h.key:
        x = min(h.right)
        h.key = x.key
        h.val = x.val
        # h.val = get(h.right, min(h.right).key)
        # h.key = min(h.right).key
        h.right = deleteMin(h.right)
      else: h.right = delete(h.right, key)
    return balance(h)

  #**************************************************************************
  #  Red-black tree helper functions.

  def _rotateRight(self, h):
    """make a left-leaning link lean to the right."""
    # assert h is not None and self._isRed(h.left)
    x = h.left
    h.left = x.right
    x.right = h
    x.color = x.right.color
    x.right.color = RED
    x.N = h.N
    h.N = self._size(h.left) + self._size(h.right) + 1
    return x

  def _rotateLeft(self, h):
    """make a right-leaning link lean to the left."""
    # assert h is not None and self._isRed(h.right)
    x = h.right
    h.right = x.left
    x.left = h
    x.color = x.left.color
    x.left.color = RED
    x.N = h.N
    h.N = self._size(h.left) + self._size(h.right) + 1
    return x

  def _flipColors(self, h):
    """flip the colors of a node and its two children."""
    # h must have opposite color of its two children
    # assert h is not None and h.left is not None and h.right is not None
    # assert (!isRed(h) and  isRed(h.left) and  isRed(h.right))
    #    or (isRed(h)  and !isRed(h.left) and !isRed(h.right))
    h.color =  not h.color
    h.left.color = not h.left.color
    h.right.color = not h.right.color

  # Assuming that h is red and both h.left and h.left.left
  # are black, make h.left or one of its children red.
  def _moveRedLeft(self, h):
    # assert (h is not None)
    # assert isRed(h) and !isRed(h.left) and !isRed(h.left.left)
    self._flipColors(h)
    if self._isRed(h.right.left): 
      h.right = self._rotateRight(h.right)
      h = self._rotateLeft(h)
      self._flipColors(h)
    return h

  # Assuming that h is red and both h.right and h.right.left
  # are black, make h.right or one of its children red.
  def _moveRedRight(self, h):
    # assert h is not None
    # assert isRed(h) and !isRed(h.right) and !isRed(h.right.left)
    self._flipColors(h)
    if self._isRed(h.left.left): 
      h = self._rotateRight(h)
      self._flipColors(h)
    return h

  def _balance(self, h):
    """restore red-black tree invariant"""
    # assert (h is not None)
    if self._isRed(h.right):                             h = self._rotateLeft(h)
    if self._isRed(h.left) and self._isRed(h.left.left): h = rotateRight(h)
    if self._isRed(h.left) and self._isRed(h.right):     flipColors(h)
    h.N = self._size(h.left) + self._size(h.right) + 1
    return h


  #**************************************************************************
  #  Utility functions.
  #**************************************************************************/
  def height(self):
     """Returns the height of the BST (for debugging)."""
    return self._height(self._root)

  def _height(self, x):
    """return the height of the BST (a 1-node tree has height 0)."""
    if x is None: return -1
    return 1 + max(height(x.left), height(x.right))

  #**************************************************************************
  #  Ordered symbol table methods.
  #**************************************************************************/
  def min_key(self):
    """Returns the smallest key in the symbol table."""
    if self.isEmpty(): raise Exception("called min() with empty symbol table")
    return min(self._root).key

  def _min_key(self, x): 
    """the smallest key in subtree rooted at x; None if no such key"""
    # assert x is not None
    if x.left is None: return x
    else:              return self._min_key(x.left)

  def max_key(self):
    """Returns the largest key in the symbol table."""
    if self.isEmpty(): raise new Exception("called max() with empty symbol table")
    return self._max_key(self._root).key

  def _max_key(self, x): 
    """the largest key in the subtree rooted at x; None if no such key"""
    # assert x is not None
    if x.right is None: return x
    else:               return self._max_key(x.right)

   def floor(self, key):
     """Returns the largest key in the symbol table less than or equal to key."""
    if self.isEmpty(): raise Exception("called floor() with empty symbol table")
    x = self._floor(self._root, key)
    if x is None: return None
    else:         return x.key

  def _floor(self x, key):
    """the largest key in the subtree rooted at x less than or equal to the given key"""
    if x is None: return None
    cmp_key = compareTo_key(key, x.key)
    if cmp_key == 0: return x
    if cmp_key < 0:  return self._floor(x.left, key)
     t = self._floor(x.right, key)
    if t is not None: return t
    else:             return x

  def ceiling(self, key):  
    """Returns the smallest key in the symbol table greater than or equal to key."""
    if self.isEmpty(): raise Exception("called ceiling() with empty symbol table")
    x = self._ceiling(self._root, key)
    if x is None: return None
    else:         return x.key

  def _ceiling(self, x, key):  
    """the smallest key in the subtree rooted at x greater than or equal to the given key"""
    if x is None: return None
    cmp_key = compareTo_keys(key, x.key)
    if cmp_key == 0: return x
    if cmp_key > 0:  return self._ceiling(x.right, key)
     t = ceiling(x.left, key)
    if t is not None: return t
    else:             return x

  def select(self, k):
    """Return the kth smallest key in the symbol table."""
    if k < 0 or k >= self.size(): raise Exception("BAD k IN select")
    x = self._select(self._root, k)
    return x.key

  def select(self, x, k):
    """the key of rank k in the subtree rooted at x."""
    # assert x is not None
    # assert k >= 0 and k < self._size(x)
    t = self._size(x.left)
    if   t > k: return self._select(x.left,  k)
    elif t < k: return self._select(x.right, k-t-1)
    else:       return x

  #*
   # Return the number of keys in the symbol table strictly less than <tt>key</tt>.
   # @param key the key
   # @return the number of keys in the symbol table strictly less than <tt>key</tt>
   # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
   #/
  def rank(self, key):
    return self._rank(key, self._root)

  def _rank(self, key, x):
    """number of keys less than key in the subtree rooted at x."""
    if x is None: return 0
    cmp_key = self.compareTo_keys(key, x.key)
    if   cmp_key < 0: return self._rank(key, x.left)
    elif cmp_key > 0: return 1 + self._size(x.left) + self._rank(key, x.right)
    else:             return self._size(x.left)

  #**************************************************************************
  #  Range count and range search.
  #**************************************************************************/
  def keys(self):
    """Returns all keys in the symbol table as an Iterable."""
    return self.keys_lh(self.min_key(), self.max_key())

  def keys_lh(self, lo, hi):
    """Returns all keys in the symbol table in the given range as an Iterable"""
    queue = Queue()
    # if (isEmpty() or lo.compareTo(hi) > 0) return queue
    keys(self._root, queue, lo, hi)
    return queue

  def _keys(self, x, queue, lo, hi): 
    """add the keys between lo and hi in the subtree rooted at x to the queue."""
    if x is None: return
    cmplo = compareTo_keys(lo, x.key)
    cmphi = compareTo_keys(hi, x.key)
    if cmplo < 0: self._keys(x.left, queue, lo, hi)
    if cmplo <= 0 and cmphi >= 0: queue.enqueue(x.key)
    if cmphi > 0: self._keys(x.right, queue, lo, hi)

  def size_lh(self, lo, hi):
    """Returns the number of keys in the symbol table in the given range."""
    if lo > hi: return 0
    if self.contains(hi): return self.rank(hi) - self.rank(lo) + 1
    else:                 return self.rank(hi) - self.rank(lo)


  #**************************************************************************
  #  Check integrity of red-black tree data structure.
  #**************************************************************************/
  def _check(self, prt=sys.stdout):
      if not self.isBST())            prt.write("Not in symmetric order")
      if not self.isSizeConsistent()) prt.write("Subtree counts not consistent")
      if not self.isRankConsistent()) prt.write("Ranks not consistent")
      if not self.is23())             prt.write("Not a 2-3 tree")
      if not self.isBalanced())       prt.write("Not balanced")
      return self.isBST() and 
             self.isSizeConsistent() and 
             self.isRankConsistent() and 
             self.is23() and 
             self.isBalanced()

  def _isBST(self):
    """does this binary tree satisfy symmetric order?"""
    # Note: this test also ensures that data structure is a binary tree since order is strict
    return self._isBST(self._root, None, None)

  # (if min or max is None, treat as empty constraint)
  # Credit: Bob Dondero's elegant solution
  def _isBST(self, x, min_key, max_key):
    """is the tree rooted at x a BST with all keys strictly between min and max"""
    if x is None: return True
    if min_key is not None and x.key <= min_key: return False
    if max_key is not None and x.key >= max_key: return False
    return self._isBST(x.left, min_key, x.key) and self._isBST(x.right, x.key, max_key)

  # are the size fields correct?
  def _isSizeConsistent(self._root); }
  def _isSizeConsistent(self, x):
      if x is None) return True
      if x.N != self._size(x.left) + self._size(x.right) + 1) return False
      return isSizeConsistent(x.left) and isSizeConsistent(x.right)

  def _isRankConsistent(self):
    """check that ranks are consistent"""
    for i in self.size():
      if i != rank(select(i)): return False
    for ( key : keys())
        if key.compareTo(select(rank(key))) != 0) return False
    return True

  def _is23(self): return is23(self._root)
  def _is23_x(self, x):
    """No red right links, and at most one (left) red links in a row on any path?"""
    if x is None: return True
    if self._isRed(x.right): return False
    if x != self._root and self._isRed(x) and self._isRed(x.left):
      return False
    return self._is23_x(x.left) and self._is23_x(x.right)

  def _isBalanced(self): 
    """do all paths from self._root to leaf have same number of black edges?"""
    black = 0     # number of black links on path from self._root to min
    x = self._root
    while x is not None:
      if not self._isRed(x): black += 1
      x = x.left
    return self._isBalanced(self._root, black)

  def _isBalanced(self, x, black):
    """does every path from the self._root to a leaf have the given number of black links?"""
    if x is None: return black == 0
    if not self._isRed(x): black -= 1
    return self._isBalanced(x.left, black) and self._isBalanced(x.right, black)


  #*
   # Unit tests the <tt>RedBlackBST</tt> data type.
   #/
  def main(String[] args): 
      RedBlackBST<String, Integer> st = new RedBlackBST<String, Integer>()
      for (int i = 0; !StdIn.isEmpty(); i += 1):
          String key = StdIn.readString()
          st.put(key, i)
      for (String s : st.keys())
          prt.write(s + " " + st.get(s))
      prt.write()

# QUESTION: Suppose that you are inserting a new key into a 2-3 tree.
# Under which one of the following scenarios must the height of i
# the 2-3 tree increase by one?
# ANSWER: When every node on the search path from the root is a 3-node.
# EXPLANATION: The height of a 2-3 tree increases onlyl when the root splits,
# and this happens only when every node on the search path from the root
# to the leaf where the new key should be inserted is a 3-node.

# QUESTION: Suppose that you insert N keys in ascending order into a red-black BST.
# What is the height of the resulting tree?
# ANSWER: logorithmic


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015, DV Klopfenstein, Python implementation
