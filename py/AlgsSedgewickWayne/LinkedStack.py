#!/usr/bin/env python

#************************************************************************
 #  Compilation:  javac LinkedStack.java
 #  Execution:    java LinkedStack < input.txt
 #
 #  A generic stack, implemented using a linked list. Each stack
 #  element is of type Item.
 #
 #  % more tobe.txt
 #  to be or not to - be - - that - - - is
 #
 #  % java LinkedStack < tobe.txt
 #  to be not that or be (2 left on stack)
 #
 #************************************************************************/

#*
 #  The <tt>LinkedStack</tt> class represents a last-in-self._first-out (LIFO) stack of
 #  generic items.
 #  It supports the usual <em>push</em> and <em>pop</em> operations, along with methods
 #  for peeking at the top item, testing if the stack is empty, and iterating through
 #  the items in LIFO order.
 #  <p>
 #  This implementation uses a singly-linked list with a non-static nested class for
 #  linked-list nodes. See {@link Stack} for a version that uses a static nested class.
 #  The <em>push</em>, <em>pop</em>, <em>peek</em>, <em>size</em>, and <em>is-empty</em>
 #  operations all take constant time in the worst case.
 #  <p>
 #  For additional documentation, see <a href="/algs4/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #  @edited DV Klopfenstein
 #/
class LinkedStack: # <Item> implements Iterable<Item>:

    class _Node: # helper linked list class
        self.Item = None
        self.Next = None

    def __init__(self):    # Initializes an empty stack.
        self._first = None # top of stack
        self._N     = 0    # size of the stack
        assert self._check()

    # Is this stack empty?
    # @return true if this stack is empty; false otherwise
    def isEmpty(self): return (self._first is None)

    # Returns the number of items in the stack.
    # @return the number of items in the stack
    def size(self): return self._N

    # Adds the item to this stack.
    # @param item the item to add
    def push(item):
        old_first   = self._first  # Save pointer to the beginning of the list
        self._first = self._Node() # Create a new Node.  Put it at the beginning ot the list
        self._first.Item = item
        self._first.Next = old_first
        N += 1
        assert self._check()

    # Removes and returns the item most recently added to this stack.
    # @return the item most recently added
    # @throws java.util.NoSuchElementException if this stack is empty
    def pop(self):
        if self.isEmpty(): raise Exception("Stack underflow")
        item = self._first.item        # save item to return
        self._first = self._first.Next # delete self._first node
        self._N -= 1
        assert self._check()
        return item                    # return the saved item


#    # Returns (but does not remove) the item most recently added to this stack.
#    # @return the item most recently added to this stack
#    # @throws java.util.NoSuchElementException if this stack is empty
#    def peek():
#        if self.isEmpty()) raise Exception("Stack underflow")
#        return self._first.item

    # Returns a string representation of this stack.
    # @return the sequence of items in the stack in LIFO order, separated by spaces
    def __str__():
        s = []
        for (Item item : this)
            s.append(item)
        return s.__str__()

#    # Returns an iterator to this stack that iterates through the items in LIFO order.
#    # @return an iterator to this stack that iterates through the items in LIFO order.
#    def ListIterator();  }
#
#    # an iterator, doesn't implement remove() since it's optional
#    private class ListIterator implements Iterator<Item>:
#        private  current = self._first
#        def hasNext(): return current != None;                     }
#        def UnsupportedOperationException();  }
#
#        def Next():
#            if !hasNext()) raise new NoSuchElementException()
#            Item item = current.item
#            current = current.Next
#            return item


    # check internal invariants
    def _check():
        if N == 0:
            if self._first is not None: return False
        elif N == 1:
            if self._first is None:          return False
            if self._first.Next is not None: return False
        else:
            if self._first.Next is None: return False

        # check internal consistency of instance variable N
        numberOfs = 0
        for ( x = self._first; x != None; x = x.Next):
            numberOfs += 1:
        if numberOfs != N: return False

        return True

# Unit tests the <tt>LinkedStack</tt> data type.
def main(String[] args):
  s = LinkedStack()
  print s
  #while not StdIn.isEmpty():
  #  String item = StdIn.readString()
  #  if !item.equals("-")) s.push(item)
  #  elif (!s.isEmpty()) StdOut.print(s.pop() + " ")
  #StdOut.println("(" + s.size() + " left on stack)")





# Copyright (C) 2002–2010, Robert Sedgewick and Kevin Wayne.
# Java last updated: Tue Sep 24 10:45:31 EDT 2013.
