#!/usr/bin/env python#************************************************************************
 #  Compilation:  javac LinkedBag.java
 #  Execution:    java LinkedBag < input.txt
 #
 #  A generic bag or multiset, implemented using a singly-linked list.
 #
 #  % more tobe.txt
 #  to be or not to - be - - that - - - is
 #
 #  % java Bag < tobe.txt
 #  size of bag = 14
 #  is
 #  -
 #  -
 #  -
 #  that
 #  -
 #  -
 #  be
 #  -
 #  to
 #  not
 #  or
 #  be
 #  to
 #
 #************************************************************************/

import java.util.Iterator
import java.util.NoSuchElementException

#*
 #  The <tt>LinkedBag</tt> class represents a bag (or multiset) of
 #  generic items. It supports insertion and iterating over the
 #  items in arbitrary order.
 #  <p>
 #  This implementation uses a singly-linked list with a non-static nested class Node.
 #  See {@link Bag} for a version that uses a static nested class.
 #  The <em>add</em>, <em>isEmpty</em>, and <em>size</em> operations
 #  take constant time. Iteration takes time proportional to the number of items.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class LinkedBag<Item> implements Iterable<Item>:
    private N;         # number of elements in bag
    private  first;    # beginning of bag

    # helper linked list class
    private class:
        private Item item
        private  next

    #*
     # Initializes an empty bag.
     #/
    public LinkedBag():
        first = None
        N = 0

    #*
     # Is this bag empty?
     # @return true if this bag is empty; false otherwise
     #/
    def isEmpty():
        return first == None

    #*
     # Returns the number of items in this bag.
     # @return the number of items in this bag
     #/
    def size():
        return N

    #*
     # Adds the item to this bag.
     # @param item the item to add to this bag
     #/
    def add(Item item):
         oldfirst = first
        first = new ()
        first.item = item
        first.next = oldfirst
        N++


    #*
     # Returns an iterator that iterates over the items in the bag.
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
     # Unit tests the <tt>LinkedBag</tt> data type.
     #/
    def main(String[] args):
        LinkedBag<String> bag = new LinkedBag<String>()
        while (!StdIn.isEmpty()):
            String item = StdIn.readString()
            bag.add(item)

        StdOut.println("size of bag = " + bag.size())
        for (String s : bag):
            StdOut.println(s)




# Copyright (C) 2002–2010, Robert Sedgewick and Kevin Wayne.
# Java last updated: Tue Sep 24 10:45:31 EDT 2013.
