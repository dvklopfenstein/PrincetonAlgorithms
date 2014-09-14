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

import java.util.Iterator
import java.util.NoSuchElementException

#*
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
 #/
public class ResizingArrayQueue<Item> implements Iterable<Item>:
    private Item[] q;            # queue elements
    private N = 0;           # number of elements on queue
    private first = 0;       # index of first element of queue
    private last  = 0;       # index of next available slot


    #*
     # Initializes an empty queue.
     #/
    public ResizingArrayQueue():
        # cast needed since no generic array creation in Java
        q = (Item[]) new [2]

    #*
     # Is this queue empty?
     # @return true if this queue is empty; false otherwise
     #/
    def isEmpty():
        return N == 0

    #*
     # Returns the number of items in this queue.
     # @return the number of items in this queue
     #/
    def size():
        return N

    # resize the underlying array
    def _resize(int max):
        assert max >= N
        Item[] temp = (Item[]) new [max]
        for (int i = 0; i < N; i++):
            temp[i] = q[(first + i) % len(q)]
        q = temp
        first = 0
        last  = N

    #*
     # Adds the item to this queue.
     # @param item the item to add
     #/
    def enqueue(Item item):
        # double size of array if necessary and recopy to front of array
        if N == len(q)) resize(2*len(q));   # double size of array if necessary
        q[last++] = item;                        # add item
        if last == len(q)) last = 0;          # wrap-around
        N++

    #*
     # Removes and returns the item on this queue that was least recently added.
     # @return the item on this queue that was least recently added
     # @throws java.util.NoSuchElementException if this queue is empty
     #/
    def dequeue():
        if isEmpty()) raise new NoSuchElementException("Queue underflow")
        Item item = q[first]
        q[first] = None;                            # to avoid loitering
        N--
        first++
        if first == len(q)) first = 0;           # wrap-around
        # shrink size of array if necessary
        if N > 0 and N == len(q)/4) resize(len(q)/2)
        return item

    #*
     # Returns the item least recently added to this queue.
     # @return the item least recently added to this queue
     # @throws java.util.NoSuchElementException if this queue is empty
     #/
    def peek():
        if isEmpty()) raise new NoSuchElementException("Queue underflow")
        return q[first]


    #*
     # Returns an iterator that iterates over the items in this queue in FIFO order.
     # @return an iterator that iterates over the items in this queue in FIFO order
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
            Item item = q[(i + first) % len(q)]
            i++
            return item

   #*
     # Unit tests the <tt>ResizingArrayQueue</tt> data type.
     #/
    def main(String[] args):
        ResizingArrayQueue<String> q = new ResizingArrayQueue<String>()
        while (!StdIn.isEmpty()):
            String item = StdIn.readString()
            if !item.equals("-")) q.enqueue(item)
            elif (!q.isEmpty()) StdOut.print(q.dequeue() + " ")
        StdOut.println("(" + q.size() + " left on queue)")


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

# Copyright (C) 2002–2010, Robert Sedgewick and Kevin Wayne. 
# Java last updated: Mon Oct 7 11:58:25 EDT 2013.
