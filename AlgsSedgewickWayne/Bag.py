"""Bag class is a container for generic items."""

class Bag(object): # <Item> implements Iterable<Item>:
  """The Bag class represents a bag (or multiset) of generic items."""

  class _Node(object): # private static class <Item>:
    """helper linked list class"""

    def __init__(self, Item, Next):
      self._item = Item
      self._next = Next

  def __init__(self):
    self._first = None # beginning of bag
    self._N = 0        # number of elements in bag

  def isEmpty(self):
    """return true if this bag is empty; false otherwise."""
    return self._first is None

  def size(self):
    """Returns the number of items in this bag."""
    return self._N

  def add(self, item):
    """Adds the arg item to this bag."""
    self._first = self._Node(item, self._first)
    self._N += 1

  # Returns an iterator that iterates over the items in the bag in arbitrary order.
  def __iter__(self):
    return self._ListIterator(self._first)

  class _ListIterator(object): # <Item> implements Iterator<Item>:
    """an iterator, doesn't implement remove() since it's optional."""

    def __init__(self, first):
      self._current = first

    def hasNext(self):
      """If we are not at the end of the Bag."""
      return self._current is not None

    def next(self):
      """Go to the next element."""
      if not self.hasNext():
        raise StopIteration
      item = self._current._item
      self._current = self._current._next
      return item

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

# The Bag class represents a bag (or multiset) of generic items.
# It supports insertion and iterating over the
# items in arbitrary order.
#
# This implementation uses a singly-linked list with a static nested class Node.
# See {@link LinkedBag} for the version from the
# textbook that uses a non-static nested class.
# The <em>add</em>, <em>isEmpty</em>, and <em>size</em> operations
# take constant time. Iteration takes time proportional to the number of items.
#
# For additional documentation, see
# <a href="http://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
# <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
# @author Robert Sedgewick
# @author Kevin Wayne
# @converted to Python by DV Klopfenstein

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Java last updated: Tue Mar 25 04:52:35 EDT 2014.
