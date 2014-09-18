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
# 05:13 STACK APPLICATIONS
#   * Parsing in a compiler
#   * Java virtual machine
#   * Undo in a word processor
#   * Back button in a Web browser
#   * PostScript language for printer
#   * Implementing function calls in a compiler.

# 06:15 RECURSIVE FUNCTION
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
# 09:40 TIME  PROPOSITION: Every operation takes constant time in the worst case: 
#   * There are only a few operations for each function
#   * No loops
# 11:00 SPACE PROPOSITION: A stack with N items useds ~40 N bytes:
#   16 bytes (_Node object overhead)
#    8 bytes (inner class _Node extra overhead)
#    8 bytes (reference to _Node.Item; String)
#    8 bytes (reference to _Node.next; Node)
#  --- -------------------------
#   40 bytes per stack Node
# 
# 09:48 *** REMARK: Analysis included memory for the stack
#   (but not the strings themselves, which the client owns). 

# Lecture Week 2 "Resizing Arrays" (9:56)
# 
# 08:33 LINKED-LIST IMPLEMENTATION.
#   * Every operation takes constant time in the WORST CASE
#   * Uses extra time and space to deal with the links.

import sys

class Stack:

  class _Node: # helper linked list class
    Item = None # Type String Item
    Next = None # Type Node<Item>

  def __init__(self):
    self.first = None # Node<Item>
    self.N = 0        # size of the stack

  def isEmpty(self): return self.first is None 

  def size(self): return self.N # Number of items in the stack

  def push(self, item): # 05:27 Lecture Week 2 "Stacks" (16:24)
      oldfirst   = self.first    # Save a link to the list
      self.first = self._Node()  # Create a new node for the beginning
      # Set the instance variables in the new node
      self.first.Item = item;
      self.first.Next = oldfirst;
      self.N += 1

  def pop(self): # 06:30 Lecture Week 2 "Stacks" (16:24)
      if self.isEmpty(): raise Exception("Stack underflow")
      item = self.first.Item        # save item to return
      self.first = self.first.Next  # delete first node
      self.N -= 1
      return item                   # return the saved item

  # Returns (but does not remove) the item most recently added to this stack.
  # @return the item most recently added to this stack
  # @raises Exception if this stack is empty
  def peek(self):
      if isEmpty(): raise Exception("Stack underflow")
      return first.item

  # Returns a string representation of this stack.
  # @return the sequence of items in the stack in LIFO order, separated by spaces
  def __str__(self): return ' '.join([str(item) for item in self])

  # Returns an iterator to this stack that iterates through the items in LIFO order.
  # @return an iterator to this stack that iterates through the items in LIFO order.
  def __iter__(self): 
    return self.ListIterator(self.first)

  class ListIterator:
      # Iterator Starts at the first item
      def __init__(self, first):
          self.current = first # Node<Item>
      
      def next(self):
          if self.current is None:
            raise StopIteration
          item = self.current.Item
          self.current = self.current.Next 
          return item


# QUESTION: Suppose that we copy the iterator code from our linked list and resizing array
# implrmentations of a stack to the corresponging implementations of a queue.
# Which queue iterator(s) will correctly return the items in FIFO order?
# 
# ANSWER: The linked list iterator will work without modification because the items in the linked
# list are orered in FIFO  order (which is the main reason we dequeue from the front 
# and enqueue to the back instead of vece versa). The array iterator will fail for two reasons:
#   1) The items should be iterated over in the opposite order
#   2) the items won't typically be stored in the array as entries 0 to N-1.

def run(item_list):
  sys.stdout.write("\nINPUT: {}\n".format(' '.join(item_list)))
  s = Stack()
  for item in item_list:
    if not item: break
    if item != "-": 
      s.push(item)
      sys.stdout.write("{:10}   PUSH {:10} +STACK: {}\n".format("", item, s))
    elif not s.isEmpty(): 
      popped = s.pop()
      sys.stdout.write("{:>10} <-POP  {:10} -STACK: {}\n".format(popped, item, s))
  sys.stdout.write('({} left on stack)\n'.format(s.size()))
  return s

def ex_stdin():
  s = Stack()
  res = ""
  while True:
    item = raw_input('TYPE WORDS OR -')
    if not item: break
    if item != "-": s.push(item)
    elif not s.isEmpty(): res = ' '.join([res,s.pop()])
  sys.stdout.write('(%d left on stack) OUTPUT: %s\n'%(s.size(),res))

def default_examples():
  stk = run( IA.get_seq__int_or_str("to be or not to be - - - - - -") )
  # Slide 6 Week 2 Lecture 4-1-Stacks(16-24)
  stk = run( IA.get_seq__int_or_str("to be or not to - be - - that - - - is") )
  sys.stdout.write("\nDEMOSTRATE ITERATION:\n"); 
  for S in stk: print S
  sys.stdout.write("\nDEMONSTRATE 'toString()': {}\n".format(stk.__str__()))


if __name__ == '__main__':
  import InputArgs as IA
  if len(sys.argv) == 1: default_examples()
  else: run( IA.get_list_from_args() )


