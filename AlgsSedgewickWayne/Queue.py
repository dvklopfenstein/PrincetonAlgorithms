"""Class Queue."""

class Queue(object):
  """Queue container class."""

  class _Node(object):
    """Queue will contain _Nodes."""
    def __init__(self, item, last):
      self.Item = item
      self.Next = last

  def __init__(self):
    self.N = 0        # number of elements on queue
    self.first = None # Pointer to begining of queue (Remove items from beginning)
    self.last = None  # Pointer to end of queue (Add items to end)

  def isEmpty(self):
    """True if Queue is empty."""
    return self.first == None

  def enqueue(self, item):  # Week 2, "Queues" 02:32
    """Add new items to the back of the queue."""
    oldlast = self.last     # Save a link to last Node
    self.last = self._Node(item, None)  # Create a new Node at end of list
    # Link the new node to the end of the list
    if self.isEmpty():
      self.first = self.last
    else:
      oldlast.Next = self.last
    self.N += 1

  def dequeue(self):
    """Remove old items from the front of the list."""
    if self.isEmpty():
      raise Exception("Queue underflow")
    item = self.first.Item # Save item that will be returned
    self.first = self.first.Next
    self.N -= 1
    if self.isEmpty():
      self.last = None  # to avoid loitering
    return item

  def size(self):
    """Return size of Queue."""
    return self.N

  def peek(self):
    """Returns the item least recently added to this queue."""
    if self.isEmpty():
      raise Exception("Queue underflow")
    return self.first.Item

  def __str__(self):
    """Returns a string representation of this queue."""
    return ' '.join([str(item) for item in self])

  def __iter__(self):
    """Is an iterator that returns (yeilds) each item in this queue in FIFO order."""
    curr_node = self.first
    while curr_node is not None:
      item = curr_node.Item
      curr_node = curr_node.Next
      yield item
    raise StopIteration

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
 #  For additional documentation, see
 #  <a href="http:#algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/



# QUESTION: Suppose that you implement a queue using a
# null-terminated singly-linked list, maintaining a
# reference to the item least recently added ( the front of
# the list) but not maintaining a reference to the item most
# recently added ( the end of the list). What are the worst
# case running times for enqueue and dequeue? (04:28)
# ANSWER: linear time for enqueue and constant time for dequeue.
