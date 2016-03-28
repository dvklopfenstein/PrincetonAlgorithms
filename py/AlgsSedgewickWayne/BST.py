"""A symbol table implemented with a binary search tree (BST)."""

# It also provides a **keys** method for iterating over all of the keys.
# A symbol table implements the **associative array** abstraction:
# when associating a value with a key that is already in the symbol table,
# the convention is to replace the old value with the new value.
# Unlike:@link java.util.Map}, self class uses the convention that
# values cannot be <tt>None</tt>&mdash;setting the
# value associated with a key to <tt>None</tt> is equivalent to deleting the key
# from the symbol table.
# <p>
# This implementation uses an (unbalanced) binary search tree. It requires that
# the key type implements the <tt>Comparable</tt> interface and calls the
# <tt>compareTo()</tt> and method to compare two keys. It does not call either
# <tt>equals()</tt> or <tt>hashCode()</tt>.
# The <em>put</em>, <em>contains</em>, <em>remove</em>, <em>minimum</em>,
# <em>maximum</em>, <em>ceiling</em>, <em>floor</em>, <em>select</em>, and
# <em>rank</em>  operations each take
# linear time in the worst case, if the tree becomes unbalanced.

# For other implementations, see 
# {@link ST},:@link BinarySearchST},
# {@link SequentialSearchST},:@link RedBlackBST},
# {@link SeparateChainingHashST}, and:@link LinearProbingHashST},
# <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.

import collections as cx
import sys

class BST(object):
    """Represents an ordered symbol table of generic key-value pairs.

       Supports: put, get, contains, delete, size, isEmpty
           get_min, get_max, floor, select, ceiling
    """

    class _Node(object):

        def __init__(self, key, val, N): 
            self.key = key # Key:   sorted by key
            self.val = val # Value: associated data
            self.N = N     # int:   number of nodes in subtree
            self.left = None  # left subtrees
            self.right = None # right subtrees

        def __str__(self):
            return "{K}\nv={V} N={N}".format(
                K=self.key, V=self.val, N=self.N)

    def __init__(self, keyvals=None):
        """Initializes an empty symbol table."""
        self.log = sys.stdout
        self._root = None       # root of BST
        if keyvals is not None:
            for key, val in keyvals:
                self.put(key, val)

    # Return True if self symbol table is empty; False otherwise. $ = K
    def isEmpty(self): return self.size() == 0

    # Returns the number of key-value pairs in self symbol table. $ = K
    def size(self): return self._size(self._root)

    # return number of key-value pairs in BST self._rooted at x. $ = K
    def _size(self, node_x): return node_x.N if node_x is not None else 0

    def contains(self, key):
        """Does self symbol table contain the given key?"""
        if key is None: raise Exception("argument to contains() is None")
        return self.get(key) is not None

    def get(self, key): # $ = 1 + depth
        """Returns the value associated with the given key or None."""
        return self._get(self._root, key)

    def _get(self, node_x, key):
        """Recursive method returns the value associated with the given key or None."""
        if node_x is None: return None
        if   key == node_x.key: return node_x.val
        elif key  < node_x.key: return self._get(node_x.left,  key)
        else:                   return self._get(node_x.right, key)
    
    # Inserts the specified key-value pair into the symbol table, overwriting the old 
    # value with the new value if the symbol table already contains the specified key.
    # Deletes the specified key (and its associated value) from self symbol table
    # if the specified value is None.
    def put(self, key, val):
        """Client method to add or update a key-value pair in a BST."""
        if key is None: raise Exception("first argument to put() is None")
        if val is None:
            self.delete(key)
            return
        self._root = self._put(self._root, key, val)
        assert self.check()

    def _put(self, node_x, key, val):
        """Recursive method to add or update a key-value pair in a BST."""
        if node_x is None: return self._Node(key, val, N=1)
        if   key == node_x.key: node_x.val   = val
        elif key  < node_x.key: node_x.left  = self._put(node_x.left,  key, val)
        else:                   node_x.right = self._put(node_x.right, key, val)
        node_x.N = 1 + self._size(node_x.left) + self._size(node_x.right)
        return node_x

    def deleteMin(self):
        """Removes the smallest key and associated value from the symbol table."""
        if self.isEmpty(): raise Exception("Symbol table underflow")
        self._root = self._deleteMin(self._root)
        assert self.check()

    def _deleteMin(self, node_x):
        if node_x.left is None: return node_x.right
        node_x.left = self._deleteMin(node_x.left)
        node_x.N = self._size(node_x.left) + self._size(node_x.right) + 1
        return node_x

    def deleteMax(self):
        """Removes the largest key and associated value from the symbol table."""
        if self.isEmpty(): raise Exception("Symbol table underflow")
        self._root = self._deleteMax(self._root)
        assert self.check()

    def _deleteMax(self, node_x):
        if node_x.right is None: return node_x.left
        node_x.right = self._deleteMax(node_x.right)
        node_x.N = self._size(node_x.left) + self._size(node_x.right) + 1
        return node_x

    def delete(self, key):
        """Removes the specified key and its associated value from self symbol table"""
        if key is None: raise Exception("argument to delete() is None")
        self._root = self._delete(self._root, key)
        assert self.check()

    def _delete(self, node_x, key):
        if node_x is None: return None
        if   key  < node_x.key: node_x.left = self._delete(node_x.left, key)
        elif key == node_x.key:
            if node_x.right is None: return node_x.left
            if node_x.left  is None: return node_x.right
            node_t = node_x
            node_x = self._get_min(node_t.right)
            node_x.right = self._deleteMin(node_t.right)
            node_x.left = node_t.left
        else: node_x.right = self._delete(node_x.right, key)
        node_x.self.N = self._size(node_x.left) + self._size(node_x.right) + 1
        return node_x


    # Returns the smallest key in the symbol table.
    def get_min(self): return self.get_min_node().key

    def _get_min_node(self, node_x):
        return node_x if node_x.left is None else self._get_min_node(node_x.left)

    # Returns the largest key in the symbol table.
    def get_max(self): return self.get_max_node().key

    def _get_max_node(self, node_x):
        return node_x if node_x.right is None else self._get_max_node(node_x.right)

    def get_min_node(self):
        """Returns the node with the smallest key in the symbol table."""
        if self.isEmpty(): raise Exception("called min() with empty symbol table")
        return self._get_min_node(self._root)

    def get_max_node(self):
        """Returns the node with the largest key in the symbol table."""
        if self.isEmpty(): raise Exception("called max() with empty symbol table")
        return self._get_max_node(self._root)


    def floor(self, key):
        """Returns the largest key in the symbol table less than or equal to key."""
        if key is None: raise Exception("argument to floor() is None")
        if self.isEmpty(): raise Exception("called floor() with empty symbol table")
        node_x = self._floor(self._root, key)
        return node_x.key if node_x is not None else None

    def _floor(self, node_x, key):
        if node_x is None: return None
        if key == node_x.key: return node_x
        if key  < node_x.key: return self._floor(node_x.left, key)
        node_tree = self._floor(node_x.right, key)
        return node_tree if node_tree is not None else node_x

    def ceiling(self, key):
        """Returns the smallest key in the symbol table greater than or equal to key."""
        if key is None:    raise Exception("argument to ceiling() is None")
        if self.isEmpty(): raise Exception("called ceiling() with empty symbol table")
        node_x = self._ceiling(self._root, key)
        return node_x.key if node_x is not None else None

    def _ceiling(self, node_x, key):
        if node_x is None: return None
        if key == node_x.key: return node_x
        if key  < node_x.key:
            node_t = self._ceiling(node_x.left, key)
            return node_t if node_t is not None else node_x
        return self._ceiling(node_x.right, key)

    def select(self, rank_k):
        """Return the kth smallest key in the symbol table."""
        if rank_k < 0 or rank_k >= self.size(): raise Exception("OUT OF RANGE: 0 to N")
        node_x = self._select(self._root, rank_k)
        return node_x.key

    def _select(self, node_x, rank_k):
        """Return key of rank k."""
        if node_x is None: return None
        sz_left = self._size(node_x.left)
        if   sz_left == rank_k: return node_x
        elif sz_left  < rank_k: return self._select(node_x.right, rank_k-sz_left-1)
        else:                   return self._select(node_x.left,  rank_k)

    def rank(self, key):
        """Return the number of keys in the symbol table strictly less than key."""
        if key is None: raise Exception("argument to rank() is None")
        return self._rank(key, self._root)

    def _rank(self, key, node_x):
        """Number of keys in the subtree less than key."""
        if node_x is None: return 0
        if   key == node_x.key: return self._size(node_x.left)
        elif key  < node_x.key: return self._rank(key, node_x.left)
        else:                   return 1 + self._size(node_x.left) + self._rank(key, node_x.right)


    def keys(self): 
        """return all keys in the symbol table."""
        return [n.key for n in self.nodes()]

    def nodes(self): return self._nodes_lohi(self.get_min(), self.get_max())

    def _nodes_lohi(self, lo_key, hi_key):
        """return all nodes in the symbol table between lo_key (inclusive) and hi_key (exclusive)"""
        if lo_key is None: raise Exception("first argument to nodes() is None")
        if hi_key is None: raise Exception("second argument to nodes() is None")
        queue = cx.deque() # new Queue<>()
        self._nodes(self._root, queue, lo_key, hi_key)
        return queue

    def _nodes(self, node_x, queue, lo_key, hi_key):
        if node_x is None: return
        #cmplo_key = lo_key.compareTo(node_x.key)
        #cmphi_key = hi_key.compareTo(node_x.key)
        #if cmplo_key < 0) nodes(node_x.left, queue, lo_key, hi_key)
        ndky = node_x.key
        if lo_key  < ndky: self._nodes(node_x.left, queue, lo_key, hi_key)
        #if cmplo_key <= 0 and cmphi_key >= 0) queue.enqueue(node_x.key)
        if lo_key <= ndky and hi_key >= ndky: queue.append(node_x) # queue.enqueue(node_x)
        #if cmphi_key > 0) nodes(node_x.right, queue, lo_key, hi_key)
        if hi_key  > ndky: self._nodes(node_x.right, queue, lo_key, hi_key)


    def size_lohi(self, lo, hi):
        """Returns the number of keys in the symbol table in the given range."""
        if lo is None: raise Exception("first argument to size() is None")
        if hi is None: raise Exception("second argument to size() is None")
        if lo > hi: return 0
        if self.contains(hi): return self.rank(hi) - self.rank(lo) + 1
        else:                 return self.rank(hi) - self.rank(lo)

    def height(self):
        """return the height of the BST (a 1-node tree has height 0) (for debugging)."""
        return self._height(self._root)

    def _height(self, node_x):
        if node_x is None: return -1
        return 1 + max(self._height(node_x.left), self._height(node_x.right))

    def levelOrder(self):
        """Return the keys in the BST in level order (for debugging)."""
        keys  = cx.deque() # new Queue<>()
        queue = cx.deque() # new Queue<>()
        queue.append(self._root) # queue.enqueue(self._root)
        while queue:
            node_x = queue.popleft() # queue.dequeue()
            if node_x is None: continue
            keys.append(node_x.key)    # keys.enqueue(node_x.key)
            queue.append(node_x.left)  # queue.enqueue(node_x.left)
            queue.append(node_x.right) # queue.enqueue(node_x.right)
        return keys

    # -- Write png --------------------------------------------------------------------
    def wr_png(self, fout_png):
        import AlgsSedgewickWayne.BST_utils as U
        childnames = cx.OrderedDict([('left', 'red'), ('right', 'green')])
        U.wr_png(fout_png, self.nodes(), childnames, self.log)

    # -- BST Checks -------------------------------------------------------------------
    def check(self):
        """Check integrity of BST data structure."""
        if not self.isBST():            self.log.write("Not in symmetric order")
        if not self.isSizeConsistent(): self.log.write("Subtree counts not consistent")
        if not self.isRankConsistent(): self.log.write("Ranks not consistent")
        return self.isBST() and self.isSizeConsistent() and self.isRankConsistent()

    # does self binary tree satisfy symmetric order?
    # Note: self test also ensures that data structure is a binary tree since order is strict
    def isBST(self): return self._isBST(self._root, minval=None, maxval=None)

    # is the tree self._rooted at x a BST with all keys strictly between min and max
    # (if min or max is None, treat as empty constraint)
    # Credit: Bob Dondero's elegant solution
    def _isBST(self, node_x, minval, maxval):
        if node_x is None: return True
        if minval is not None and node_x.key <= minval <= 0: return False
        if maxval is not None and node_x.key >= maxval >= 0: return False
        return self._isBST(node_x.left, minval, node_x.key) and \
               self._isBST(node_x.right, node_x.key, maxval)

    def isSizeConsistent(self): return self._isSizeConsistent(self._root)
    def _isSizeConsistent(self, node_x):
        """are the size fields correct?"""
        if node_x is None: return True
        if node_x.N != self._size(node_x.left) + self._size(node_x.right) + 1: return False
        return self._isSizeConsistent(node_x.left) and self._isSizeConsistent(node_x.right)

    def isRankConsistent(self):
        """check that ranks are consistent."""
        for i in range(self.size()):
            if i != self.rank(self.select(i)): return False
        for key in self.keys():
            if key != self.select(self.rank(key)): return False
        return True

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
# SYMMETRIC ORDER: Each node has a key and every node's key is:
#   * Larger  than all keys in its left  subtree
#   * Smaller than all keys in its right subtree

# 01:45 Different from a heap.  HEAPs had every node larger than its children.

# CORRESPONDENCE BETWEEN BSTs and QUICKSORT PARTITIONING 0:17
# REMARK: Correspondence is 1-1 if array has no duplicate keys

# QUESTION: Suppose that N distinct keys are inserted into a binary
# search tree in random order. What is the expected number of 
# compares to search for one of the N keys?
# ANSWER: logorithmic.

# From comments in the Discussion from a student who worked on the exercises for
# level-order traversal of a BST:
#   Each node has a key and every node's key is:
#     * Larger than all keys in its left subtree.
#     * Smaller than all keys in its right subtree.


# https://github.com/kevin-wayne/algs4/commits/master/src/main/java/edu/princeton/cs/algs4/BST.java

# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2015-2016, DV Klopfenstein, Python implementation.
