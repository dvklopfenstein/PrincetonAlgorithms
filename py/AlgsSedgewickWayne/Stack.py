"""Stack Class"""

class Stack(object):
  """Stack class: Linked list of Nodes."""
  # Proposition: Every operation takes constant time in the worst case.

  class _Node(object): # helper linked list class
    """Node object. Nodes are stored in a Stack."""

    def __init__(self, item, nxt):
      self.Item = item # Type String Item
      self.Next = nxt  # Type Node<Item>

  def __init__(self):
    self.first = None # Node<Item>
    self.N = 0        # size of the stack

  def isEmpty(self):
    """Returns True if the Stack contains no nodes."""
    return self.first is None

  def push(self, item): # 05:27 Lecture Week 2 "Stacks" (16:24)
    """Add a new item to the top of the Stack."""
    oldfirst = self.first     # Save a link to the list
    self.first = self._Node(item, oldfirst) # first points to most recent Node
    self.N += 1

  def pop(self): # 06:30 Lecture Week 2 "Stacks" (16:24)
    """Returns the item most recently added."""
    if self.isEmpty():
      raise Exception("Stack underflow")
    item = self.first.Item        # save item to return
    self.first = self.first.Next  # delete last Node added
    self.N -= 1
    return item                   # return the saved item

  def size(self):
    """Returns the size of the Stack."""
    return self.N # Number of items in the stack

  def peek(self):
    """Returns (but does not remove) the item most recently added to this stack."""
    if self.isEmpty():
      raise Exception("Stack underflow") # Nothing to peek at
    return self.first.Item # most recently added item

  def __str__(self):
    """Returns string containing the sequence of items in the stack in LIFO order"""
    return ' '.join([str(item) for item in self])

  # Returns an iterator to this stack that iterates through the items in LIFO order.
  # https://mail.python.org/pipermail/tutor/2006-January/044455.html
  # https://www.inkling.com/read/learning-python-mark-lutz-4th/chapter-29/iterator-objects---iter---and--
  def __iter__(self):
    """Returns an iterator object."""
    return self.ListIterator(self.first)

  class ListIterator(object):
    """Iterator Starts at the first item."""

    def __init__(self, first):
      self.current = first # Node<Item>

    def next(self):
      """Return Next item."""
      if self.current is None:
        raise StopIteration
      item = self.current.Item
      self.current = self.current.Next
      return item

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


# -----------------------------------------------------------
# Bruno Lehouque: boolean is a primitive type while Boolean is an object type.
#   It's a wrapper type for booleans. Its size is
#   16(overhead) + 1(boolean value) + 7(padding)
#
# public class GenericMysteryBox<Item> {  16 bytes(class overhead)
#         private Node first;              8 bytes(reference)
#
#                                          8 bytes(inner class _Node overhead)
#         private class Node {            16 bytes(_Node overhead)
#             private Item item;           8 bytes(reference to _Node.Item, a Boolean)
#                                         24 bytes(Boolean)
#             private Node next;           8 bytes
#             private Node prev;           8 bytes
#         }
#         ...               ANSWER   24 + 72N
#     }

# -----------------------------------------------------------
#    public class MysteryBox {          16 class
#        private Node first;             8 reference
#
#                                        8 inner class
#        private static class Node {    16 class
#            private int item;           4 int
#            private Node next;          8 ref
#        }                               4 padding to round up to multiple of 8
#        ...                ANSWER 24 + 32N
#    }

# -----------------------------------------------------------
#     public class MysteryBox {      16 class
#         private int N;              4 int
#         private double[] items;    24 + 8N
#         ...
#     }                             ~8N


#
# 09:48 *** REMARK: Analysis included memory for the stack
#   (but not the strings themselves, which the client owns).

# Lecture Week 2 "Resizing Arrays" (9:56)
#
# 08:33 LINKED-LIST IMPLEMENTATION.
#   * Every operation takes constant time in the WORST CASE
#   * Uses extra time and space to deal with the links.
################################################################################
# Lecture Alg 1 Week 2 "Iterators" (7:16)
################################################################################
#
# Q. What is an "Iterable"?
# A. Has a method that returns an "Iterator."
#
#   JAVA ITERABLE INTERFACE
#
#       public interface Iterable<Item>
#       {
#         Iterator<Item> iterator();
#       }
#
# Q. What is an "Iterator"?
# A. Has methods "hasNext()" and "next()".
#
#   JAVA ITERATOR INTERFACE:
#
#       public interface Iterator<Item>
#       {
#         boolean hasNext();
#         Item next();
#         void remove(); # <- WARNING: USER AT YOUR OWN RISK
#       {
#
# Q. Why make data structures "Iterable"?
# A. Java supports elegant client code.
#
#   SHORTHAND "foreach" statement    LONGHAND equivalent code
#
#   for (String s: stack)            Iterator<String> i = stack.iterator();
#     StdOut.println(s);             while (i.hasNext())
#                                    {
#                                      String s = i.next();
#                                      Stdout.println(s);
#                                    }

# 07:13 QUESTION: Suppose that we copy the iterator code from our linked list
# and resizing array implementations of a stack to the corresponding
# implementations of a queue.
#
# Which queue iterator(s) will correctly return the items in FIFO order?
#    NO: neither
#   YES: linked list iterator only
#    NO: array iterator only
#    NO: both
#
# EXPLANATION: The linkes list iterator will work without modifiction because
# the items in the linked list are ordered in FIFO order (which is the main
# reason we dequeue from the front and enqueue to the back instead of vice versa).
# The array iterator will fail for two reasons:
#   i. the items should be iterated over in the opposite order
#   ii. the items won't typically be stored in the array as entries 0 to N-1

# QUESTION: Suppose that we copy the iterator code from our linked list and resizing array
# implrmentations of a stack to the corresponging implementations of a queue.
# Which queue iterator(s) will correctly return the items in FIFO order?
#
# ANSWER: The linked list iterator will work without modification because the items in the linked
# list are ordered in FIFO  order (which is the main reason we dequeue from the front
# and enqueue to the back instead of vece versa). The array iterator will fail for two reasons:
#   1) The items should be iterated over in the opposite order
#   2) the items won't typically be stored in the array as entries 0 to N-1.
