#!/usr/bin/env python#************************************************************************
 #  Compilation:  javac Bag.java
 #  Execution:    java Bag < input.txt
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
 #  The <tt>Bag</tt> class represents a bag (or multiset) of 
 #  generic items. It supports insertion and iterating over the 
 #  items in arbitrary order.
 #  <p>
 #  This implementation uses a singly-linked list with a static nested class Node.
 #  See {@link LinkedBag} for the version from the
 #  textbook that uses a non-static nested class.
 #  The <em>add</em>, <em>isEmpty</em>, and <em>size</em> operations
 #  take constant time. Iteration takes time proportional to the number of items.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class Bag<Item> implements Iterable<Item>:
    private N;               # number of elements in bag
    private <Item> first;    # beginning of bag

    # helper linked list class
    private static class <Item>:
        private Item item
        private <Item> next

    #*
     # Initializes an empty bag.
     #/
    public Bag():
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
        <Item> oldfirst = first
        first = new <Item>()
        first.item = item
        first.next = oldfirst
        N++


    #*
     # Returns an iterator that iterates over the items in the bag in arbitrary order.
     # @return an iterator that iterates over the items in the bag in arbitrary order
     #/
    def iterator():
        return new ListIterator<Item>(first)

    # an iterator, doesn't implement remove() since it's optional
    private class ListIterator<Item> implements Iterator<Item>:
        private <Item> current

        public ListIterator(<Item> first):
            current = first

        def hasNext(): return current != None;                     }
        def UnsupportedOperationException();  }

        def next():
            if !hasNext()) raise new NoSuchElementException()
            Item item = current.item
            current = current.next
            return item

    #*
     # Unit tests the <tt>Bag</tt> data type.
     #/
    def main(String[] args):
        Bag<String> bag = new Bag<String>()
        while (!StdIn.isEmpty()):
            String item = StdIn.readString()
            bag.add(item)

        StdOut.println("size of bag = " + bag.size())
        for (String s : bag):
            StdOut.println(s)



# Copyright (C) 2002–2010, Robert Sedgewick and Kevin Wayne. 
# Java last updated: Tue Mar 25 04:52:35 EDT 2014.

