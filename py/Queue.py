#!/usr/bin/env python

# https:class.coursera.org/algs4partI-005/lecture/20
# Week 2, Algorithms 1

 #************************************************************************
 #  Compilation:  javac Queue.java
 #  Execution:    java Queue < input.txt
 #  Data files:   http:#algs4.cs.princeton.edu/13stacks/tobe.txt  
 #
 #  A generic queue, implemented using a linked list.
 #
 #  % java Queue < tobe.txt 
 #  to be or not to be (2 left on queue)
 #
 #************************************************************************/

 #*
 #  The <tt>Queue</tt> class represents a first-in-first-out (FIFO)
 #  queue of generic items.
 #  It supports the usual <em>enqueue</em> and <em>dequeue</em>
 #  operations, along with methods for peeking at the first item,
 #  testing if the queue is empty, and iterating through
 #  the items in FIFO order.
 #  <p>
 #  This implementation uses a singly-linked list with a static nested class for
 #  linked-list nodes. See {@link LinkedQueue} for the version from the
 #  textbook that uses a non-static nested class.
 #  The <em>enqueue</em>, <em>dequeue</em>, <em>peek</em>, <em>size</em>, and <em>is-empty</em>
 #  operations all take constant time in the worst case.
 #  <p>
 #  For additional documentation, see <a href="http:#algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

# https://class.coursera.org/algs4partI-005/lecture/20
# QUESTION: Suppose that you implement a queue using a
# null-terminated singly-linked list, maintaining a
# reference to the item least recently added ( the front of
# the list) but not maintaining a reference to the item most
# recently added ( the end of the list). What are the worst
# case running times for enqueue and dequeue? (04:28)
# ANSWER: linear time for enqueue and constant time for dequeue.

import unittest

class Queue:

    class _Node:
      def __init__(self):
        self.Item = None
        self.Next = None

    def __init__(self):
      self.N = 0        # number of elements on queue
      self.first = None # Pointer to begining of queue
      self.last  = None # Pointer to end of queue

    def isEmpty(self): return self.first == None
    def size(self): return self.N

    def enqueue(self, item):
        oldlast = self.last
        self.last = self._Node()
        self.last.Item = item;
        self.last.Next = None;
        if self.isEmpty(): self.first = self.last
        else:            oldlast.Next = self.last
        self.N += 1

    def dequeue(self):
        if self.isEmpty(): raise Exception("Queue underflow")
        item       = self.first.Item
        self.first = self.first.Next
        self.N -= 1
        if self.isEmpty(): self.last = None  # to avoid loitering
        return item;

#      #*
#      # Returns the item least recently added to this queue.
#      # @return the item least recently added to this queue
#      # @throws java.util.NoSuchElementException if this queue is empty
#      #/
#     public Item peek() {
#         if (isEmpty()) throw new NoSuchElementException("Queue underflow");
#         return first.item;
#     }
# 
#      #*
#      # Returns a string representation of this queue.
#      # @return the sequence of items in FIFO order, separated by spaces
#      #/
#     public String toString() {
#         StringBuilder s = new StringBuilder();
#         for (Item item : this)
#             s.append(item + " ");
#         return s.toString();
#     } 
# 
#      #*
#      # Returns an iterator that iterates over the items in this queue in FIFO order.
#      # @return an iterator that iterates over the items in this queue in FIFO order
#      #/
#     public Iterator<Item> iterator()  {
#         return new ListIterator<Item>(first);  
#     }
# 
#     # an iterator, doesn't implement remove() since it's optional
#     private class ListIterator<Item> implements Iterator<Item> {
#         private Node<Item> current;
# 
#         public ListIterator(Node<Item> first) {
#             current = first;
#         }
# 
#         public boolean hasNext()  { return current != null;                     }
#         public void remove()      { throw new UnsupportedOperationException();  }
# 
#         public Item next() {
#             if (!hasNext()) throw new NoSuchElementException();
#             Item item = current.item;
#             current = current.next; 
#             return item;
#         }
#     }
# 
# 
#      #*
#      # Unit tests the <tt>Queue</tt> data type.
#      #/
#     public static void main(String[] args) {
#         Queue<String> q = new Queue<String>();
#         while (!StdIn.isEmpty()) {
#             String item = StdIn.readString();
#             if (!item.equals("-")) q.enqueue(item);
#             else if (!q.isEmpty()) StdOut.print(q.dequeue() + " ");
#         }
#         StdOut.println("(" + q.size() + " left on queue)");
#     }
# }

def run(line):
  import sys
  O = Queue()
  res = []
  for word in line.split():
    if not word: break
    if word != "-": O.enqueue(word)
    elif not O.isEmpty(): res.append(O.dequeue())
  sys.stdout.write('(%d left in Queue) OUTPUT: %s\n'%(O.size(),' '.join(res)))
  return res

class Stack_Tests(unittest.TestCase):

  def chk(self, a, txt):
    b = txt.split()
    return len(a)==len(b) and len(a)==sum([1 for i,j in zip(a,b) if i==j])

  def test_wk2_ex_Queues_608030(self):
    # Question 2
    # (seed = 608030)
    # Suppose that an intermixed sequence of 10 enqueue and 10
    # dequeue operations are performed on a FIFO queue. The
    # enqueues add the letters 0 through 9 in order; the dequeues
    # print out the return value. Which of the following output
    # sequence(s) could occur?
    # r = run("0 1 2 3 4 5 6 7 8 9")
    print "608030 DONE"
    r = run("0 - 1 2 - 3 4 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 2 1 3 7 4 9 6 8 5") )

    r = run("0 1 2 - - - 3 4 5 - 6 - - 7 8 9")
    #self.failUnless( self.chk(r, "0 1 2 5 6 4 8 9 3 7") )

    r = run("0 1 2 3 4 5 6 7 8 9 - - - - - - - - - -")
    self.failUnless( self.chk(r, "0 1 2 3 4 5 6 7 8 9") )

    r = run("0 - 1 2 3 4 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 7 4 1 8 3 6 2 9 5") )

    r = run("0 - 1 2 3 4 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 4 5 1 8 6 2 3 9 7") )

  def test_wk2_ex_Queues_511394(self):
    # (seed = 511394)
    # Suppose that an intermixed sequence of 10 enqueue and 10
    # dequeue operations are performed on a FIFO queue. The
    # enqueues add the letters 0 through 9 in order; the dequeues
    # print out the return value. Which of the following output
    # sequence(s) could occur?
    r = run("0 1 - - 2 3 4 - 5 6 7 8 9")
    #self.failUnless( self.chk(r, "0 1 4 9 6 8 5 2 7 3") )
    #self.failUnless( self.chk(r, "0 1 2 3 4 5 8 9 6 7") )
    #self.failUnless( self.chk(r, "0 1 2 4 8 6 5 9 7 3") )
    #self.failUnless( self.chk(r, "0 1 2 3 4 7 6 8 5 9") )
    #self.failUnless( self.chk(r, "0 1 2 3 4 5 6 7 8 9") )

if __name__ == '__main__':
  unittest.main()


