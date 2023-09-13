#!/usr/bin/env python
#************************************************************************
 #  Compilation:  javac LinkedQueue.java
 #  Execution:    java LinkedQueue < input.txt
 #  Dependencies: StdIn.java StdOut.java
 #  Data files:   http://algs4.cs.princeton.edu/13stacks/tobe.txt
 #
 #  A generic queue, implemented using a singly-linked list.
 #
 #  % java Queue < tobe.txt
 #  to be or not to be (2 left on queue)
 #
 #************************************************************************/

import java.util.Iterator
import java.util.NoSuchElementException

#*
 #  The <tt>LinkedQueue</tt> class represents a first-in-first-out (FIFO)
 #  queue of generic items.
 #  It supports the usual <em>enqueue</em> and <em>dequeue</em>
 #  operations, along with methods for peeking at the first item,
 #  testing if the queue is empty, and iterating through
 #  the items in FIFO order.
 #  <p>
 #  This implementation uses a singly-linked list with a non-static nested class
 #  for linked-list nodes.  See {@link Queue} for a version that uses a static nested class.
 #  The <em>enqueue</em>, <em>dequeue</em>, <em>peek</em>, <em>size</em>, and <em>is-empty</em>
 #  operations all take constant time in the worst case.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class LinkedQueue<Item> implements Iterable<Item>:
    private N;         # number of elements on queue
    private  first;    # beginning of queue
    private  last;     # end of queue

    # helper linked list class
    private class:
        private Item item
        private  next

    #*
     # Initializes an empty queue.
     #/
    public LinkedQueue():
        first = None
        last  = None
        N = 0
        assert check()

    #*
     # Is this queue empty?
     # @return true if this queue is empty; false otherwise
     #/
    def isEmpty():
        return first == None

    #*
     # Returns the number of items in this queue.
     # @return the number of items in this queue
     #/
    def size():
        return N

    #*
     # Returns the item least recently added to this queue.
     # @return the item least recently added to this queue
     # @throws java.util.NoSuchElementException if this queue is empty
     #/
    def peek():
        if isEmpty()) raise new NoSuchElementException("Queue underflow")
        return first.item

    #*
     # Adds the item to this queue.
     # @param item the item to add
     #/
    def enqueue(Item item):
         oldlast = last
        last = new ()
        last.item = item
        last.next = None
        if isEmpty()) first = last
        else           oldlast.next = last
        N++
        assert check()

    #*
     # Removes and returns the item on this queue that was least recently added.
     # @return the item on this queue that was least recently added
     # @throws java.util.NoSuchElementException if this queue is empty
     #/
    def dequeue():
        if isEmpty()) raise new NoSuchElementException("Queue underflow")
        Item item = first.item
        first = first.next
        N--
        if isEmpty()) last = None;   # to avoid loitering
        assert check()
        return item

    #*
     # Returns a string representation of this queue.
     # @return the sequence of items in FIFO order, separated by spaces
     #/
    def toString():
        StringBuilder s = new StringBuilder()
        for (Item item : this)
            s.append(item + " ")
        return s.toString()

    # check internal invariants
    def _check():
        if N == 0):
            if first != None) return False
            if last  != None) return False
        elif (N == 1):
            if first == None or last == None) return False
            if first != last)                 return False
            if first.next != None)            return False
        else:
            if first == last)      return False
            if first.next == None) return False
            if last.next  != None) return False

            # check internal consistency of instance variable N
            numberOfs = 0
            for ( x = first; x != None; x = x.next):
               numberOfs++
            if numberOfs != N) return False

            # check internal consistency of instance variable last
             last = first
            while (last.next != None):
               last = last.next
            if last != last) return False

        return True


    #*
     # Returns an iterator that iterates over the items in this queue in FIFO order.
     # @return an iterator that iterates over the items in this queue in FIFO order
     #/
    def iterator():
        return new ListIterator()

    # an iterator, doesn't implement remove() since it's optional
    private class ListIterator implements Iterator<Item>:
        private  current = first

        def hasNext(): return current != None;                     }
        def UnsupportedOperationException();  }

        def next():
            if !hasNext()) raise new NoSuchElementException()
            Item item = current.item
            current = current.next
            return item


    #*
     # Unit tests the <tt>LinkedQueue</tt> data type.
     #/
    def main(String[] args):
        LinkedQueue<String> q = new LinkedQueue<String>()
        while (!StdIn.isEmpty()):
            String item = StdIn.readString()
            if !item.equals("-")) q.enqueue(item)
            elif (!q.isEmpty()) StdOut.print(q.dequeue() + " ")
        StdOut.println("(" + q.size() + " left on queue)")


# Copyright (C) 2002–2010, Robert Sedgewick and Kevin Wayne.
# Java last updated: Tue Sep 24 10:45:31 EDT 2013.
