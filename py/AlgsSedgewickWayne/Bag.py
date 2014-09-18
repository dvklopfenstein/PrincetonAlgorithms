#!/usr/bin/env python

#************************************************************************
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
 #  @edited DV Klopfenstein
class Bag: # <Item> implements Iterable<Item>:

    # helper linked list class
    class _Node: # private static class <Item>:
        def __init__(self, Item, Next):
          self._item = Item
          self._next = Next

    # Initializes an empty bag.
    def __init__(self):
        self._first = None # number of elements in bag
        self._N = 0        # beginning of bag

    # Is this bag empty?
    # @return true if this bag is empty; false otherwise
    def isEmpty(self): return self._first == None

    # Returns the number of items in this bag.
    # @return the number of items in this bag
    def size(self): return self._N

    # Adds the item to this bag.
    # @param item the item to add to this bag
    def add(self, item):
        self._first = self._Node(item, self._first)
        self._N += 1

    # Returns an iterator that iterates over the items in the bag in arbitrary order.
    # @return an iterator that iterates over the items in the bag in arbitrary order
    def __iter__(self): return self._ListIterator(self._first)

    # an iterator, doesn't implement remove() since it's optional
    class _ListIterator: # <Item> implements Iterator<Item>:

        def __init__(self, first):
            self._current = first

        def hasNext(self): return self._current is not None

        def next(self):
            if not self.hasNext(): raise StopIteration
            item = self._current._item
            self._current = self._current._next
            return item

# Unit tests the <tt>Bag</tt> data type.
def run(item_list):
    import sys
    bag = Bag()
    for item in item_list:
        bag.add(item)

    sys.stdout.write("size of bag = {}\n".format(bag.size()))
    for s in bag:
        sys.stdout.write("  BAG CONTAINS: {}\n".format(s))

def default_examples():
  import InputArgs as IA
  bag = run( IA.get_seq__int_or_str("1 2 3 4 5 6 7 8 9") )

if __name__ == '__main__':
  import InputArgs as IA
  import sys
  if len(sys.argv) == 1: default_examples()
  else: run( IA.get_list_from_args() )




# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Java last updated: Tue Mar 25 04:52:35 EDT 2014.

