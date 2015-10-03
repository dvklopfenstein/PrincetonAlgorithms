#!/usr/bin/env python#*****************************************************************************
 #  Compilation:  javac RedBlackBST.java
 #  Execution:    java RedBlackBST < input.txt
 #  Dependencies: StdIn.java StdOut.java  
 #  Data files:   http://algs4.cs.princeton.edu/33balanced/tinyST.txt  
 #    
 #  A symbol table implemented using a left-leaning red-black BST.
 #  This is the 2-3 version.
 #
 #  Note: commented out assertions because DrJava now enables assertions
 #        by default.
 #
 #  % more tinyST.txt
 #  S E A R C H E X A M P L E
 #  
 #  % java RedBlackBST < tinyST.txt
 #  A 8
 #  C 4
 #  E 12
 #  H 5
 #  L 11
 #  M 9
 #  P 10
 #  R 3
 #  S 0
 #  X 7
 #
 #*****************************************************************************/

package edu.princeton.cs.algs4

import java.util.NoSuchElementException

#*
 #  The <tt>BST</tt> class represents an ordered symbol table of generic
 #  key-value pairs.
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
 #  <p>
 #  This implementation uses a left-leaning red-black BST. It requires that
 #  the key type implements the <tt>Comparable</tt> interface and calls the
 #  <tt>compareTo()</tt> and method to compare two keys. It does not call either
 #  <tt>equals()</tt> or <tt>hashCode()</tt>.
 #  The <em>put</em>, <em>contains</em>, <em>remove</em>, <em>minimum</em>,
 #  <em>maximum</em>, <em>ceiling</em>, and <em>floor</em> operations each take
 #  logarithmic time in the worst case, if the tree becomes unbalanced.
 #  The <em>size</em>, and <em>is-empty</em> operations take constant time.
 #  Construction takes constant time.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/33balanced">Section 3.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #  For other implementations, see {@link ST}, {@link BinarySearchST},
 #  {@link SequentialSearchST}, {@link BST},
 #  {@link SeparateChainingHashST}, and {@link LinearProbingHashST},
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #/

public class RedBlackBST< extends Comparable<>, Value>:

    private static final boolean RED   = True
    private static final boolean BLACK = False

    private  root;     # root of the BST

    # BST helper node data type
    private class:
        private  key;           # key
        private Value val;         # associated data
        private  left, right;  # links to left and right subtrees
        private boolean color;     # color of parent link
        private N;             # subtree count

        public ( key, Value val, boolean color, N):
            this.key = key
            this.val = val
            this.color = color
            this.N = N

    #*
     # Initializes an empty symbol table.
     #/
    public RedBlackBST():

   #**************************************************************************
    #  Node helper methods.
    #**************************************************************************/
    # is node x red; False if x is None ?
    def _isRed( x):
        if x == None) return False
        return x.color == RED

    # number of node in subtree rooted at x; 0 if x is None
    def _size( x):
        if x == None) return 0
        return x.N


    #*
     # Returns the number of key-value pairs in this symbol table.
     # @return the number of key-value pairs in this symbol table
     #/
    def size():
        return size(root)

   #*
     # Is this symbol table empty?
     # @return <tt>true</tt> if this symbol table is empty and <tt>false</tt> otherwise
     #/
    def isEmpty():
        return root == None


   #**************************************************************************
    #  Standard BST search.
    #**************************************************************************/

    #*
     # Returns the value associated with the given key.
     # @param key the key
     # @return the value associated with the given key if the key is in the symbol table
     #     and <tt>null</tt> if the key is not in the symbol table
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def get( key):
        return get(root, key)

    # value associated with the given key in subtree rooted at x; None if no such key
    def _get( x,  key):
        while (x != None):
            cmp = key.compareTo(x.key)
            if      cmp < 0) x = x.left
            elif (cmp > 0) x = x.right
            else:              return x.val
        return None

    #*
     # Does this symbol table contain the given key?
     # @param key the key
     # @return <tt>true</tt> if this symbol table contains <tt>key</tt> and
     #     <tt>false</tt> otherwise
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def contains( key):
        return get(key) != None

   #**************************************************************************
    #  Red-black tree insertion.
    #**************************************************************************/

    #*
     # Inserts the key-value pair into the symbol table, overwriting the old value
     # with the new value if the key is already in the symbol table.
     # If the value is <tt>null</tt>, this effectively deletes the key from the symbol table.
     # @param key the key
     # @param val the value
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def put( key, Value val):
        root = put(root, key, val)
        root.color = BLACK
        # assert check()

    # insert the key-value pair in the subtree rooted at h
    private  put( h,  key, Value val): 
        if h == None) return new (key, val, RED, 1)

        cmp = key.compareTo(h.key)
        if      cmp < 0) h.left  = put(h.left,  key, val)
        elif (cmp > 0) h.right = put(h.right, key, val)
        else              h.val   = val

        # fix-up any right-leaning links
        if isRed(h.right) and !isRed(h.left))      h = rotateLeft(h)
        if isRed(h.left)  and  isRed(h.left.left)) h = rotateRight(h)
        if isRed(h.left)  and  isRed(h.right))     flipColors(h)
        h.N = size(h.left) + size(h.right) + 1

        return h

   #**************************************************************************
    #  Red-black tree deletion.
    #**************************************************************************/

    #*
     # Removes the smallest key and associated value from the symbol table.
     # @throws NoSuchElementException if the symbol table is empty
     #/
    def deleteMin():
        if isEmpty()) raise new NoSuchElementException("BST underflow")

        # if both children of root are black, set root to red
        if !isRed(root.left) and !isRed(root.right))
            root.color = RED

        root = deleteMin(root)
        if !isEmpty()) root.color = BLACK
        # assert check()

    # delete the key-value pair with the minimum key rooted at h
    private  deleteMin( h): 
        if h.left == None)
            return None

        if !isRed(h.left) and !isRed(h.left.left))
            h = moveRedLeft(h)

        h.left = deleteMin(h.left)
        return balance(h)


    #*
     # Removes the largest key and associated value from the symbol table.
     # @throws NoSuchElementException if the symbol table is empty
     #/
    def deleteMax():
        if isEmpty()) raise new NoSuchElementException("BST underflow")

        # if both children of root are black, set root to red
        if !isRed(root.left) and !isRed(root.right))
            root.color = RED

        root = deleteMax(root)
        if !isEmpty()) root.color = BLACK
        # assert check()

    # delete the key-value pair with the maximum key rooted at h
    private  deleteMax( h): 
        if isRed(h.left))
            h = rotateRight(h)

        if h.right == None)
            return None

        if !isRed(h.right) and !isRed(h.right.left))
            h = moveRedRight(h)

        h.right = deleteMax(h.right)

        return balance(h)

    #*
     # Removes the key and associated value from the symbol table
     # (if the key is in the symbol table).
     # @param key the key
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def delete( key): 
        if !contains(key)):
            System.err.println("symbol table does not contain " + key)
            return

        # if both children of root are black, set root to red
        if !isRed(root.left) and !isRed(root.right))
            root.color = RED

        root = delete(root, key)
        if !isEmpty()) root.color = BLACK
        # assert check()

    # delete the key-value pair with the given key rooted at h
    private  delete( h,  key): 
        # assert get(h, key) != None

        if key.compareTo(h.key) < 0):
            if !isRed(h.left) and !isRed(h.left.left))
                h = moveRedLeft(h)
            h.left = delete(h.left, key)
        else:
            if isRed(h.left))
                h = rotateRight(h)
            if key.compareTo(h.key) == 0 and (h.right == None))
                return None
            if !isRed(h.right) and !isRed(h.right.left))
                h = moveRedRight(h)
            if key.compareTo(h.key) == 0):
                 x = min(h.right)
                h.key = x.key
                h.val = x.val
                # h.val = get(h.right, min(h.right).key)
                # h.key = min(h.right).key
                h.right = deleteMin(h.right)
            else h.right = delete(h.right, key)
        return balance(h)

   #**************************************************************************
    #  Red-black tree helper functions.
    #**************************************************************************/

    # make a left-leaning link lean to the right
    private  rotateRight( h):
        # assert (h != None) and isRed(h.left)
         x = h.left
        h.left = x.right
        x.right = h
        x.color = x.right.color
        x.right.color = RED
        x.N = h.N
        h.N = size(h.left) + size(h.right) + 1
        return x

    # make a right-leaning link lean to the left
    private  rotateLeft( h):
        # assert (h != None) and isRed(h.right)
         x = h.right
        h.right = x.left
        x.left = h
        x.color = x.left.color
        x.left.color = RED
        x.N = h.N
        h.N = size(h.left) + size(h.right) + 1
        return x

    # flip the colors of a node and its two children
    def _flipColors( h):
        # h must have opposite color of its two children
        # assert (h != None) and (h.left != None) and (h.right != None)
        # assert (!isRed(h) and  isRed(h.left) and  isRed(h.right))
        #    or (isRed(h)  and !isRed(h.left) and !isRed(h.right))
        h.color = !h.color
        h.left.color = !h.left.color
        h.right.color = !h.right.color

    # Assuming that h is red and both h.left and h.left.left
    # are black, make h.left or one of its children red.
    private  moveRedLeft( h):
        # assert (h != None)
        # assert isRed(h) and !isRed(h.left) and !isRed(h.left.left)

        flipColors(h)
        if isRed(h.right.left)): 
            h.right = rotateRight(h.right)
            h = rotateLeft(h)
            flipColors(h)
        return h

    # Assuming that h is red and both h.right and h.right.left
    # are black, make h.right or one of its children red.
    private  moveRedRight( h):
        # assert (h != None)
        # assert isRed(h) and !isRed(h.right) and !isRed(h.right.left)
        flipColors(h)
        if isRed(h.left.left)): 
            h = rotateRight(h)
            flipColors(h)
        return h

    # restore red-black tree invariant
    private  balance( h):
        # assert (h != None)

        if isRed(h.right))                      h = rotateLeft(h)
        if isRed(h.left) and isRed(h.left.left)) h = rotateRight(h)
        if isRed(h.left) and isRed(h.right))     flipColors(h)

        h.N = size(h.left) + size(h.right) + 1
        return h


   #**************************************************************************
    #  Utility functions.
    #**************************************************************************/

    #*
     # Returns the height of the BST (for debugging).
     # @return the height of the BST (a 1-node tree has height 0)
     #/
    def height():
        return height(root)
    def _height( x):
        if x == None) return -1
        return 1 + Math.max(height(x.left), height(x.right))

   #**************************************************************************
    #  Ordered symbol table methods.
    #**************************************************************************/

    #*
     # Returns the smallest key in the symbol table.
     # @return the smallest key in the symbol table
     # @throws NoSuchElementException if the symbol table is empty
     #/
    public  min():
        if isEmpty()) raise new NoSuchElementException("called min() with empty symbol table")
        return min(root).key

    # the smallest key in subtree rooted at x; None if no such key
    private  min( x): 
        # assert x != None
        if x.left == None) return x
        else:                return min(x.left)

    #*
     # Returns the largest key in the symbol table.
     # @return the largest key in the symbol table
     # @throws NoSuchElementException if the symbol table is empty
     #/
    public  max():
        if isEmpty()) raise new NoSuchElementException("called max() with empty symbol table")
        return max(root).key

    # the largest key in the subtree rooted at x; None if no such key
    private  max( x): 
        # assert x != None
        if x.right == None) return x
        else:                 return max(x.right)


    #*
     # Returns the largest key in the symbol table less than or equal to <tt>key</tt>.
     # @param key the key
     # @return the largest key in the symbol table less than or equal to <tt>key</tt>
     # @throws NoSuchElementException if there is no such key
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    public  floor( key):
        if isEmpty()) raise new NoSuchElementException("called floor() with empty symbol table")
         x = floor(root, key)
        if x == None) return None
        else:           return x.key

    # the largest key in the subtree rooted at x less than or equal to the given key
    private  floor( x,  key):
        if x == None) return None
        cmp = key.compareTo(x.key)
        if cmp == 0) return x
        if cmp < 0)  return floor(x.left, key)
         t = floor(x.right, key)
        if t != None) return t
        else:           return x

    #*
     # Returns the smallest key in the symbol table greater than or equal to <tt>key</tt>.
     # @param key the key
     # @return the smallest key in the symbol table greater than or equal to <tt>key</tt>
     # @throws NoSuchElementException if there is no such key
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    public  ceiling( key):  
        if isEmpty()) raise new NoSuchElementException("called ceiling() with empty symbol table")
         x = ceiling(root, key)
        if x == None) return None
        else:           return x.key

    # the smallest key in the subtree rooted at x greater than or equal to the given key
    private  ceiling( x,  key):  
        if x == None) return None
        cmp = key.compareTo(x.key)
        if cmp == 0) return x
        if cmp > 0)  return ceiling(x.right, key)
         t = ceiling(x.left, key)
        if t != None) return t
        else:           return x

    #*
     # Return the kth smallest key in the symbol table.
     # @param k the order statistic
     # @return the kth smallest key in the symbol table
     # @throws IllegalArgumentException unless <tt>k</tt> is between 0 and
     #     <em>N</em> &minus; 1
     #/
    public  select(int k):
        if k < 0 or k >= size()) raise new IllegalArgumentException()
         x = select(root, k)
        return x.key

    # the key of rank k in the subtree rooted at x
    private  select( x, k):
        # assert x != None
        # assert k >= 0 and k < size(x)
        t = size(x.left)
        if      t > k) return select(x.left,  k)
        elif (t < k) return select(x.right, k-t-1)
        else:            return x

    #*
     # Return the number of keys in the symbol table strictly less than <tt>key</tt>.
     # @param key the key
     # @return the number of keys in the symbol table strictly less than <tt>key</tt>
     # @throws NullPointerException if <tt>key</tt> is <tt>null</tt>
     #/
    def rank( key):
        return rank(key, root)

    # number of keys less than key in the subtree rooted at x
    def _rank( key,  x):
        if x == None) return 0
        cmp = key.compareTo(x.key)
        if      cmp < 0) return rank(key, x.left)
        elif (cmp > 0) return 1 + size(x.left) + rank(key, x.right)
        else:              return size(x.left)

   #**************************************************************************
    #  Range count and range search.
    #**************************************************************************/

    #*
     # Returns all keys in the symbol table as an <tt>Iterable</tt>.
     # To iterate over all of the keys in the symbol table named <tt>st</tt>,
     # use the foreach notation: <tt>for (Key key : st.keys())</tt>.
     # @return all keys in the sybol table as an <tt>Iterable</tt>
     #/
    def keys():
        return keys(min(), max())

    #*
     # Returns all keys in the symbol table in the given range,
     # as an <tt>Iterable</tt>.
     # @return all keys in the sybol table between <tt>lo</tt> 
     #    (inclusive) and <tt>hi</tt> (exclusive) as an <tt>Iterable</tt>
     # @throws NullPointerException if either <tt>lo</tt> or <tt>hi</tt>
     #    is <tt>null</tt>
     #/
    def keys( lo,  hi):
        Queue<> queue = new Queue<>()
        # if (isEmpty() or lo.compareTo(hi) > 0) return queue
        keys(root, queue, lo, hi)
        return queue

    # add the keys between lo and hi in the subtree rooted at x
    # to the queue
    def _keys( x, Queue<> queue,  lo,  hi): 
        if x == None) return
        cmplo = lo.compareTo(x.key)
        cmphi = hi.compareTo(x.key)
        if cmplo < 0) keys(x.left, queue, lo, hi)
        if cmplo <= 0 and cmphi >= 0) queue.enqueue(x.key)
        if cmphi > 0) keys(x.right, queue, lo, hi)

    #*
     # Returns the number of keys in the symbol table in the given range.
     # @return the number of keys in the sybol table between <tt>lo</tt> 
     #    (inclusive) and <tt>hi</tt> (exclusive)
     # @throws NullPointerException if either <tt>lo</tt> or <tt>hi</tt>
     #    is <tt>null</tt>
     #/
    def size( lo,  hi):
        if lo.compareTo(hi) > 0) return 0
        if contains(hi)) return rank(hi) - rank(lo) + 1
        else:              return rank(hi) - rank(lo)


   #**************************************************************************
    #  Check integrity of red-black tree data structure.
    #**************************************************************************/
    def _check():
        if !isBST())            prt.write("Not in symmetric order")
        if !isSizeConsistent()) prt.write("Subtree counts not consistent")
        if !isRankConsistent()) prt.write("Ranks not consistent")
        if !is23())             prt.write("Not a 2-3 tree")
        if !isBalanced())       prt.write("Not balanced")
        return isBST() and isSizeConsistent() and isRankConsistent() and is23() and isBalanced()

    # does this binary tree satisfy symmetric order?
    # Note: this test also ensures that data structure is a binary tree since order is strict
    def _isBST():
        return isBST(root, None, None)

    # is the tree rooted at x a BST with all keys strictly between min and max
    # (if min or max is None, treat as empty constraint)
    # Credit: Bob Dondero's elegant solution
    def _isBST( x,  min,  max):
        if x == None) return True
        if min != None and x.key.compareTo(min) <= 0) return False
        if max != None and x.key.compareTo(max) >= 0) return False
        return isBST(x.left, min, x.key) and isBST(x.right, x.key, max)

    # are the size fields correct?
    def _isSizeConsistent(root); }
    def _isSizeConsistent( x):
        if x == None) return True
        if x.N != size(x.left) + size(x.right) + 1) return False
        return isSizeConsistent(x.left) and isSizeConsistent(x.right)

    # check that ranks are consistent
    def _isRankConsistent():
        for (int i = 0; i < size(); i += 1)
            if i != rank(select(i))) return False
        for ( key : keys())
            if key.compareTo(select(rank(key))) != 0) return False
        return True

    # Does the tree have no red right links, and at most one (left)
    # red links in a row on any path?
    private boolean is23(): return is23(root); }
    private boolean is23( x):
        if x == None) return True
        if isRed(x.right)) return False
        if x != root and isRed(x) and isRed(x.left))
            return False
        return is23(x.left) and is23(x.right)

    # do all paths from root to leaf have same number of black edges?
    def _isBalanced(): 
        black = 0;     # number of black links on path from root to min
         x = root
        while (x != None):
            if !isRed(x)) black += 1
            x = x.left
        return isBalanced(root, black)

    # does every path from the root to a leaf have the given number of black links?
    def _isBalanced( x, black):
        if x == None) return black == 0
        if !isRed(x)) black -= 1
        return isBalanced(x.left, black) and isBalanced(x.right, black)


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

#*****************************************************************************
 #  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
 #
 #  This file is part of algs4.jar, which accompanies the textbook
 #
 #      Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
 #      Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
 #      http://algs4.cs.princeton.edu
 #
 #
 #  algs4.jar is free software: you can redistribute it and/or modify
 #  it under the terms of the GNU General Public License as published by
 #  the Free Software Foundation, either version 3 of the License, or
 #  (at your option) any later version.
 #
 #  algs4.jar is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with algs4.jar.  If not, see http://www.gnu.org/licenses.
 #*****************************************************************************/
