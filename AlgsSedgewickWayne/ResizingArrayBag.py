#************************************************************************
 #  Compilation:  javac ResizingArrayBag.java
 #  Execution:    java ResizingArrayBag
 #
 #  Bag implementation with a resizing array.
 #
 #************************************************************************/

import java.util.Iterator
import java.util.NoSuchElementException

#*
 #  The <tt>ResizingArrayBag</tt> class represents a bag (or multiset) of
 #  generic items. It supports insertion and iterating over the
 #  items in arbitrary order.
 #  <p>
 #  This implementation uses a resizing array.
 #  See {@link LinkedBag} for a version that uses a singly-linked list.
 #  The <em>add</em> operation takes constant amortized time; the
 #  <em>isEmpty</em>, and <em>size</em> operations
 #  take constant time. Iteration takes time proportional to the number of items.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class ResizingArrayBag<Item> implements Iterable<Item>:
    private Item[] a;         # array of items
    private N = 0;        # number of elements on stack

    #*
     # Initializes an empty bag.
     #/
    public ResizingArrayBag():
        a = (Item[]) new [2]

    #*
     # Is this bag empty?
     # @return true if this bag is empty; false otherwise
     #/
    def isEmpty():
        return N == 0

    #*
     # Returns the number of items in this bag.
     # @return the number of items in this bag
     #/
    def size():
        return N

    # resize the underlying array holding the elements
    def _resize(int capacity):
        assert capacity >= N
        Item[] temp = (Item[]) new [capacity]
        for (int i = 0; i < N; i++)
            temp[i] = a[i]
        a = temp

    #*
     # Adds the item to this bag.
     # @param item the item to add to this bag
     #/
    def add(Item item):
        if N == len(a)) resize(2*len(a));    # double size of array if necessary
        a[N++] = item;                            # add item


    #*
     # Returns an iterator that iterates over the items in the bag in arbitrary order.
     # @return an iterator that iterates over the items in the bag in arbitrary order
     #/
    def iterator():
        return new ArrayIterator()

    # an iterator, doesn't implement remove() since it's optional
    private class ArrayIterator implements Iterator<Item>:
        private i = 0
        def hasNext(): return i < N;                               }
        def UnsupportedOperationException();  }

        def next():
            if !hasNext()) raise new NoSuchElementException()
            return a[i++]

    #*
     # Unit tests the <tt>ResizingArrayBag</tt> data type.
     #/
    def main(String[] args):
        ResizingArrayBag<String> bag = new ResizingArrayBag<String>()
        bag.add("Hello")
        bag.add("World")
        bag.add("how")
        bag.add("are")
        bag.add("you")

        for (String s : bag)
            StdOut.println(s)


# Copyright (C) 2002–2010, Robert Sedgewick and Kevin Wayne.
# Java last updated: Tue Oct 8 21:23:24 EDT 2013.
