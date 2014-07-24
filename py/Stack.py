#!/usr/bin/env python

 #************************************************************************
 #  Compilation:  javac Stack.java
 #  Execution:    java Stack < input.txt
 #
 #  A generic stack, implemented using a singly-linked list.
 #  Each stack element is of type Item.
 #
 #  This version uses a static nested class Node (to save 8 bytes per
 #  Node), whereas the version in the textbook uses a non-static nested
 #  class (for simplicity).
 #  
 #  % more tobe.txt 
 #  to be or not to - be - - that - - - is
 #
 #  % java Stack < tobe.txt
 #  to be not that or be (2 left on stack)
 #
 #************************************************************************/

# Week 2 Lecture
# https://class.coursera.org/algs4partI-005/lecture/23
# 05:13 STACK APPLICATIONS
#   * Parsing in a compiler
#   * Java virtual machine
#   * Undo in a word processor
#   * Back button in a Web browser
#   * PostScript language for printer
#   * Implementing function calls in a compiler.

# 06:15 RECURSINVE FUNCTION
# NOTE: Can always use an expilicit stack to remove recursion.
#     
#     static int gcd(int p, int q) {
#       if (q == 0) return p;
#       else return gcd(q, p % q);
#     }  
#     

 #*
 #  The <tt>Stack</tt> class represents a last-in-first-out (LIFO) stack of generic items.
 #  It supports the usual <em>push</em> and <em>pop</em> operations, along with methods
 #  for peeking at the top item, testing if the stack is empty, and iterating through
 #  the items in LIFO order.
 #  <p>
 #  This implementation uses a singly-linked list with a static nested class for
 #  linked-list nodes. See {@link LinkedStack} for the version from the
 #  textbook that uses a non-static nested class.
 #  The <em>push</em>, <em>pop</em>, <em>peek</em>, <em>size</em>, and <em>is-empty</em>
 #  operations all take constant time in the worst case.
 #  <p>
 #  For additional documentation, see <a href="/algs4/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

# 09:40/16:24 Stack: linked-list implementation performance
# TIME  PROPOSITION: Every operation takes constant time in the worst case. (No loops)
# SPACE PROPOSITION: A stack with N items useds ~40 N bytes:
#   16 bytes (object overhead)
#    8 bytes (inner class _Node extra overhead)
#    8 bytes (reference to String)
#    8 bytes (reference to Node)
#  --- -------------------------
#   40 bytes per stack Node
#  *** REMARK: Analysis included memory for the stack
#              (but not the strings themselves, which the client owns). 

import sys
import unittest

class Stack:

  class _Node: # helper linked list class
    Item = None # Type Item
    Next = None # Type Node<Item>

  def __init__(self):
    self.first = None # Node<Item>
    self.N = 0        # size of the stack

  def isEmpty(self): return self.first is None 

  def size(self): return self.N # Number of items in the stack

  def push(self, item):
      oldfirst = self.first
      self.first = self._Node()
      self.first.Item = item;
      self.first.Next = oldfirst;
      self.N += 1

  def pop(self):
      if self.isEmpty(): raise Exception("Stack underflow")
      item = self.first.Item        # save item to return
      self.first = self.first.Next            # delete first node
      self.N -= 1
      return item;                   # return the saved item

#     #*
#     # Returns (but does not remove) the item most recently added to this stack.
#     # @return the item most recently added to this stack
#     # @throws java.util.NoSuchElementException if this stack is empty
#     #/
#    public Item peek() {
#        if (isEmpty()) throw new NoSuchElementException("Stack underflow");
#        return first.item;
#    }
#
#     #*
#     # Returns a string representation of this stack.
#     # @return the sequence of items in the stack in LIFO order, separated by spaces
#     #/
#    public String toString() {
#        StringBuilder s = new StringBuilder();
#        for (Item item : this)
#            s.append(item + " ");
#        return s.toString();
#    }
#       
#
   #*
   # Returns an iterator to this stack that iterates through the items in LIFO order.
   # @return an iterator to this stack that iterates through the items in LIFO order.
   #/
  def iterator(self): return ListIterator(self.first)

  # an iterator, doesn't implement remove() since it's optional
  class ListIterator:

      # Iterator Starts at the first item
      def ListIterator(self, first):
          self.current = first; # Node<Item>
      
      def hasNext(self): return self.current is not None
      def remove(self):  raise Exception("UNSUPPORTED: remove")

      def next(self):
          if not self.hasNext(): raise Exception("NoSuchElementException");
          item = self.current.Item;
          self.current = self.current.Next; 
          return item;

# QUESTION: Suppose that we copy the iterator code from our linked list and resizing array
# implrmentations of a stack to the corresponging implementations of a queue.
# Which queue iterator(s) will correctly return the items in FIFO order?
# 
# ANSWER: The linked list iterator will work without modification because the items in the linked
# list are orered in FIFO  order (which is the main reason we dequeue from the front 
# and enqueue to the back instead of vece versa). The array iterator will fail for two reasons:
#   1) The items should be iterated over in the opposite order
#   2) the items won't typically be stored in the array as entries 0 to N-1.

def run(line):
  s = Stack()
  res = []
  for word in line.split():
    if not word: break
    if word != "-": s.push(word)
    elif not s.isEmpty(): res.append(s.pop())
  sys.stdout.write('(%d left on stack) OUTPUT: %s\n'%(s.size(),' '.join(res)))
  return res

def ex_stdin():
  s = Stack()
  res = ""
  while True:
    item = raw_input('TYPE WORDS OR -')
    #sys.stdout.write('"%s"\n'%(item))
    if not item: break
    if item != "-": s.push(item)
    elif not s.isEmpty(): res = ' '.join([res,s.pop()])
  sys.stdout.write('(%d left on stack) OUTPUT: %s\n'%(s.size(),res))


class Stack_Tests(unittest.TestCase):

  def chk(self, a, txt):
    b = txt.split()
    return len(a)==len(b) and len(a)==sum([1 for i,j in zip(a,b) if i==j])

  def test_wk2_ex_Stacks_489125(self):
    # (seed = 489125)
    # Suppose that an intermixed sequence of 10 push and 10 pop
    # operations are performed on a LIFO stack. The pushes push
    # the letters 0 through 9 in order; the pops print out the
    # return value. Which of the following output sequence(s)
    # could occur?
    # o = run("0 1 2 3 4 5 6 7 8 9")
    print "\n489125 DONE"
    o = run("0 - 1 - 2 3 - - 4 - 5 6 - 7 8 - - 9 -")
    #self.failUnless( self.chk(o, "0 1 3 2 4 6 8 5 7 9") )

    o = run("0 1 2 3 4 5 6 - - - - - - - 7 - 8 - 9 -")
    self.failUnless( self.chk(o, "6 5 4 3 2 1 0 7 8 9") )

    o = run("0 1 2 3 - 4 - 5 - 6 7 8 - 9 - - - - - -")
    self.failUnless( self.chk(o, "3 4 5 8 9 7 6 2 1 0") )

    o = run("0 - 1 2 3 - 4 5 6 7 - - - - - 8 9 - - -")
    self.failUnless( self.chk(o, "0 3 7 6 5 4 2 9 8 1") )

    o = run("0 1 - - 2 3 - 4 5 - 6 7 8 9")
    # self.failUnless( self.chk(o, "1 0 3 5 2 7 6 8 9 4") )
    print

  def test_wk2_ex_Stacks_634506(self):
    # (seed = 634506)
    # Suppose that an intermixed sequence of 10 push and 10 pop
    # operations are performed on a LIFO stack. The pushes push
    # the letters 0 through 9 in order; the pops print out the
    # return value. Which of the following output sequence(s)
    # could occur?
    print "\n634506 DONE"
    o = run("0 1 2 3 - - - 4 5 - 6 7 8 9")
    #self.failUnless( self.chk(o, "3 2 1 5 0 6 7 8 9 4") )
    o = run("0 1 2 - - - 3 - 4 - 5 - 6 - 7 - 8 - 9 -")
    self.failUnless( self.chk(o, "2 1 0 3 4 5 6 7 8 9") )
    o = run("0 - 1 - 2 3 - - 4 - 5 - 6 - 7 8 - - 9 -")
    self.failUnless( self.chk(o, "0 1 3 2 4 5 6 8 7 9") )
    o = run("0 1 2 3 - 4 5 - - 6 7 8 9")
    #self.failUnless( self.chk(o, "3 5 2 4 6 1 0 8 7 9") )
    o = run("0 1 2 - - 3 4 5 6 - - - 7 - - 8 - - 9 -")
    self.failUnless( self.chk(o, "2 1 6 5 4 7 3 8 0 9") )


  def test_wk2_ex_Stacks_634506b(self):
    # (seed = 634506)
    print "\n634506b DONE"
    o = run("0 1 2 3 - - - 4 5 - - 6 7 8 9")
    #self.failUnless( self.chk(o, "3 2 1 5 0 6 7 8 9 4") )
    o = run("0 1 2 - - - 3 - 4 - 5 - 6 - 7 - 8 - 9 -")
    self.failUnless( self.chk(o, "2 1 0 3 4 5 6 7 8 9") )
    o = run("0 - 1 - 2 3 - - 4 - 5 - 6 - 7 8 - - 9 -")
    self.failUnless( self.chk(o, "0 1 3 2 4 5 6 8 7 9") )
    o = run("0 1 2 3 - 4 5 - - 6 7 8 9")
    #self.failUnless( self.chk(o, "3 5 2 4 6 1 0 8 7 9") )
    o = run("0 1 2 - - 3 4 5 6 - - - 7 - - 8 - - 9 -")
    self.failUnless( self.chk(o, "2 1 6 5 4 7 3 8 0 9") )

  def test_wk2_ex_Stacks_489125b(self):
    # (seed = 489125)
    print "\n489125b"
    #o = run("0 1 2 3 4 5 6 7 8 9")
    o = run("0 - 1 - 2 3 - - 4 - 5 6 - 7 8 - - 9")
    #self.failUnless( self.chk(o, "0 1 3 2 4 6 8 5 7 9"))
    o = run("0 1 2 3 4 5 6 - - - - - - - 7 - 8 - 9 -")
    self.failUnless( self.chk(o, "6 5 4 3 2 1 0 7 8 9"))
    o = run("0 1 2 3 - 4 - 5 - 6 7 8 - 9 - - - - - -")
    self.failUnless( self.chk(o, "3 4 5 8 9 7 6 2 1 0"))
    o = run("0 - 1 2 3 - 4 5 6 7 - - - - - 8 9 - - -")
    self.failUnless( self.chk(o, "0 3 7 6 5 4 2 9 8 1"))
    o = run("0 1 - - 2 3 - 4 5 - - 6 7 8 9")
    #self.failUnless( self.chk(o, "1 0 3 5 2 7 6 8 9 4"))

if __name__ == '__main__':
  unittest.main()


