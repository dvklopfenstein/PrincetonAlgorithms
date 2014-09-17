#!/usr/bin/env python
#************************************************************************
#  Compilation:  javac ResizingArrayQueue.java
#  Execution:    java ResizingArrayQueue < input.txt
#  Data files:   http://algs4.cs.princeton.edu/13stacks/tobe.txt  
#  
#  Queue implementation with a resizing array.
#
#  % java ResizingArrayQueue < tobe.txt 
#  to be or not to be (2 left on queue)
#
#************************************************************************/

#  The <tt>ResizingArrayQueue</tt> class represents a first-in-first-out (FIFO)
#  queue of generic items.
#  It supports the usual <em>enqueue</em> and <em>dequeue</em>
#  operations, along with methods for peeking at the first item,
#  testing if the queue is empty, and iterating through
#  the items in FIFO order.
#  <p>
#  This implementation uses a resizing array, which double the underlying array
#  when it is full and halves the underlying array when it is one-quarter full.
#  The <em>enqueue</em> and <em>dequeue</em> operations take constant amortized time.
#  The <em>size</em>, <em>peek</em>, and <em>is-empty</em> operations takes
#  constant time in the worst case. 
#  <p>
#  For additional documentation, see <a href="http://algs4.cs.princeton.edu/13stacks">Section 1.3</a> of
#  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#
#  @author Robert Sedgewick
#  @author Kevin Wayne
#  @edited D Klopfenstein: Converted t Python


# Lecture Part 1 Week 2 Queues (4:33)
# 
# 04:28 QUESTION: Suppose that you implement a queue using a null-terminated
# usingly-linked list, maintaining a reference to the item least recently 
# added (the front of the list) but not maintiaining a reference to the 
# item most recently added (the end o the lsit). What are the worst case
# running times for enqueue and dequeue?
# 
#   No:  constant time for both enqueue and dequeue
#   No:  constant time for enqueue and linear time for dequeue
#   Yes: linear time for enqueue and constant time for dequeue
#   No:  linear time for both enqueue and dequeue
# 
# EXPLANATION: Removing a node from the fromt of a linked list takes constant time.
# However, it takes linear time to find the last node of a linked list
# (unless we are careful to maintain a reference to it).

class ResizingArrayQueue: # <Item> implements Iterable<Item>:

    def __init__(self):
      self._q = [None for i in range(2)]    # queue elements
      self._N = 0     # number of elements on queue
      self._first = 0 # index of first element of queue
      self._last  = 0 # index of next available slot

    # @return true if this queue is empty; false otherwise
    def isEmpty(self): return self._N == 0

    # Returns the number of items in this queue.
    def size(self): return self._N

    # resize the underlying array
    def _resize(self, maxval):
        assert maxval >= self._N
        temp = [None for i in range(maxval)] # (Item[]) new [maxval] # Item[]
        q_len = len(self._q)
        for i in range(self._N):
            temp[i] = self._q[(self._first + i) % q_len]
        self._q = temp
        self._first = 0
        self._last  = self._N

    # Adds the item to this queue.
    # @param item the item to add
    def enqueue(self, item):
        # double size of array if necessary and recopy to front of array
        if self._N == len(self._q): 
          self._resize(2*len(self._q)) # double size of array if necessary
        self._q[self._last] = item                        # add item
        self._last += 1
        if self._last == len(self._q): 
          self._last = 0          # wrap-around
        self._N += 1

    # Removes and returns the item on this queue that was least recently added.
    # @return the item on this queue that was least recently added
    # @throws java.util.NoSuchElementException if this queue is empty
    def dequeue(self):
        if self.isEmpty(): raise Exception("Queue underflow")
        item = self._q[self._first]
        self._q[self._first] = None     # to avoid loitering
        self._N     -= 1
        self._first += 1
        if self._first == len(self._q): self._first = 0  # wrap-around
        # shrink size of array if necessary
        if self._N > 0 and self._N == len(self._q)/4: 
          self._resize(len(self._q)/2)
        return item


    def __str__(self):
        return ' '.join(item for item in self._q[self._first:self._last])

#    # Returns the item least recently added to this queue.
#    # @return the item least recently added to this queue
#    # @throws java.util.NoSuchElementException if this queue is empty
#    def peek(self):
#        if self.isEmpty(): raise Exception("Queue underflow")
#        return self._q[self._first]
#
#    # Returns an iterator that iterates over the items in this queue in FIFO order.
#    # @return an iterator that iterates over the items in this queue in FIFO order
#    def iterator(self):
#        return new ArrayIterator()
#
#    # an iterator, doesn't implement remove() since it's optional
#    private class ArrayIterator implements Iterator<Item>:
#        private i = 0
#        def hasNext(): return i < N;                               }
#        def UnsupportedOperationException();  }
#
#        def next():
#            if !hasNext()) raise new NoSuchElementException()
#            Item item = q[(i + first) % len(q)]
#            i++
#            return item

    # Unit tests the <tt>ResizingArrayQueue</tt> data type.
def run(item_list):
  import sys
  sys.stdout.write("\nRUNNING: {}\n".format(' '.join(item_list)))
  q = ResizingArrayQueue()
  for item in item_list:
    if item != "-": q.enqueue(item)
    else: sys.stdout.write("  DEQUEUE: {}\n".format(q.dequeue()))
  sys.stdout.write("({} left on queue): {}\n".format(q.size(), q))


if __name__ == '__main__':
  import InputArgs as IA
  import sys
  # If user did not provide a sequence.
  if len(sys.argv) == 1:
    run( IA.get_seq__int_or_str("a b c d - - e f - - g h i -") )
    run( IA.get_seq__int_or_str("a - b - c d - - e f - - g h i -") )
  # If user provided a sequence in the runtime arguments.
  else:
    run( IA.get_list_from_args() )



# ResizingArrayQueue.java
# 05:57 Lecture Generics
#
# private Itemp[] s
# public FixedCapacityStack(int capacity)
# WANT:: s = new Item[capacity]; }  # GRRRR Java does not allow this
# CUR:: s = (Item[]) new [capacity]; }  # GRRRR Java does not allow this
#   warning: [unchecked] unchecked cast

# 08:59 GENERIC DATA TYPES: autoboxing
# QUESTION: What to do about primitive types?
# 
# WRAPPER TYPE: 
#   * Each primitive type has a wrapper object type.
#   * Ex: Interger is wrapper type for int.
# 
# AUTOBOXING: Automatic cast between a primitive type and its wrapper.
# 
# SYNTACTIC SUGAR: Behind-the-scenes casting.
#   Stack<Integer> s = new Stack<Integer>()
#   s.push(17)
#   a = s.pop()
# 
# BOTTOM LINE: Client code can use generic stack for any type of data.

# QUESTION: What is a type safe way to declare and initialize a Stack of integers?
# ANSWER:   Stack<Integer> stack = Stack<Integer>()

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Java last updated: Mon Oct 7 11:58:25 EDT 2013.
