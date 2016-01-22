"""Class ResizingArrayStack."""

class ResizingArrayStack: #<Item> implements Iterable<Item>:
  """Stack implemented with an array instead of a linked list."""

  def __init__(self): # Initializes an empty stack.
    self._a = [None, None]
    # Also the next location in the array to get filled upon push
    self._N = 0 # number of elements on stack

  def isEmpty(self): 
    """return true if this stack is empty; false otherwise."""
    return self._N == 0

  def push(self, item):
    """Adds the item to this stack."""
    # double size of array if necessary
    if self._N == len(self._a):
      self._resize(2*len(self._a)) # Repeated doubling
    self._a[self._N] = item        # add item
    self._N += 1

  def pop(self):
    """Removes and returns the item most recently added to this stack."""
    if self.isEmpty():
      raise Exception("FatalResizingArrayStack.py: Stack underflow")
    item = self._a[self._N-1]
    self._N -= 1
    self._a[self._N] = None  # to avoid loitering
    # shrink size of array if necessary
    if self._N > 0 and self._N == len(self._a)/4: 
      self._resize(len(self._a)/2)
    return item

  def size(self): 
    """Returns the number of items in the stack."""
    return self._N

  def _resize(self, capacity):
    """resize the underlying array holding the elements."""
    assert capacity >= self._N
    temp = [None for i in range(capacity)] # type: Item[]
    for i in range(self._N): # Copy items into new array
        temp[i] = self._a[i]
    self._a = temp # Return new bigger array

  def __str__(self): 
    return ' '.join([str(item) for item in self])

  def peek():
    """Returns (but does not remove) the item most recently added to this stack."""
    if self.isEmpty(): raise Exception("Stack underflow")
    return self._a[N-1]

  def __iter__(self): 
    """Returns an iterator to this stack that iterates through the items in LIFO order."""
    return self._ReverseArrayIterator(self)

  class _ReverseArrayIterator: # implements Iterator<Item>:
    def __init__(self, stk):
      self._arr = stk._a
      self._i   = stk._N
    def hasNext(self): 
      return self._i > 0
    def next(self):
      if not self.hasNext():
        raise StopIteration
      self._i -= 1
      return self._arr[self._i]

#************************************************************************
 #  Compilation:  javac ResizingArrayStack.java
 #  Execution:    java ResizingArrayStack < input.txt
 #  Data files:   http://algs4.cs.princeton.edu/13stacks/tobe.txt
 #
 #  Stack implementation with a resizing array.
 #
 #  % more tobe.txt
 #  to be or not to - be - - that - - - is
 #
 #  % java ResizingArrayStack < tobe.txt
 #  to be not that or be (2 left on stack)
 #
 #************************************************************************/

 #  The <tt>ResizingArrayStack</tt> class represents a last-in-first-out (LIFO) stack
 #  of generic items.
 #  It supports the usual <em>push</em> and <em>pop</em> operations, along with methods
 #  for peeking at the top item, testing if the stack is empty, and iterating through
 #  the items in LIFO order.
 #  <p>
 #  This implementation uses a resizing array, which double the underlying array
 #  when it is full and halves the underlying array when it is one-quarter full.
 #  The <em>push</em> and <em>pop</em> operations take constant amortized time.
 #  The <em>size</em>, <em>peek</em>, and <em>is-empty</em> operations takes
 #  constant time in the worst case.
 #  <p>
 #  For additional documentation, see <a href="/algs4/13stacks">Section 1.3</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #  @edited DV Klopfenstein

# Lecture Week 2 Resizing Arrays (09:56)
# 00:51 17 PROBLEM. Requiring client to provide capacity does not implement API!
# Q. How to grow and shrink array?
#
# FIRST TRY.
#   * push(): increase size of array s[] by 1
#   * pop():  decrease size of array s[] by 1
#
# TOO EXPENSIVE. QUADRATIC TIME (Infeasible for large N)
#   * Need to copy all items to a new array.
#   * Inserting first N items takes time proportional to 1 + 2 +...+ N ~ N^2/2

# 02:41 18 REPEAT DOUBLING
#
# CONSEQUENCE. Inserting first N items takes time proportional to N (not N^2)
# COST OF INSERTING FIRST N ITEMS. N + (2 + 4 + 8 + ... + N) ~ 3N
#   N -> 1 array access per push
#   (2...N) -> k array acesses to double to size k (ignoring cost to create new array)

# 04:30 Q. How to shrink array?
#
# FIRST TRY.
#  * push(): double size of array s[] when array is full.
#  * pop():  halve  size of array s[] when array is ONE-HALF FULL.
#
# TOO EXPENSIVE IN WORST CASE. (THRASHING)
#  * Consider push-pop-push-pop-... sequcne when array is full.
#  * Each operation takes time proportional to N.
#    N = 5 |to   |be   |or   |not  |to   |None |None |None |
#    N = 4 |to   |be   |or   |not  |
#    N = 5 |to   |be   |or   |not  |to   |None |None |None |
#    N = 4 |to   |be   |or   |not  |

# 05:09 INVARIANT. Array is between 25% and 100% full.

# 06:45 STACK RESIZING-ARRAY IMPLEMENTATION: PERFORMANCE
#
# AMORTIZED ANALYSIS. Average running time per operation over
# a worst-case sequence of operations.
#
# PROPOSITION. Starting from an empty stack, any seauence of M push and
# pop operations takes time proportional to M.
#
# Order of growth of running time for resizing stack with N items:
#
#            | best | worst | amortized
#            +------+-------+----------
#  construct |    1 |     1 |         1
#  push      |    1 |     N |         1  N->Doubling operation
#  pop       |    1 |     N |         1  N->Halfing  operation
#  size      |    1 |     1 |         1

# 07:34 STACK RESIZING-ARRAY IMPLEMENTATION: MEMORY USAGE
#
# PROPOSITION. Uses between ~8N and ~32N bytes to represent a stack with N items.
#   * ~8N when full.
#   * ~32N when one quarter full.
#
# public class ResizingArrayStackOfStrings
# {                       24 bytes (array overhead)
#                          8 bytes (reference to array)
#   private String[] s; <- 8 bytes x array size
#   private int N = 0;  <- 4 bytes int
#   ...                    4 bytes (padding)
# }
#
# REMARK. Analysis includes memory for the stack
# (but not the strings themselves, which the client owns).

# 08:04 TRADEOFFS. Can implement a stack with either resizing array or linked list;
# client can use interchangeably. Which one is better?
#
# LINKED-LIST IMPLEMENTATION. (SLOWER) GUARANTED that each op is fast.
#  * Every operation takes constant time in the WORST CASE.
#  * Uses extra time and space to deal with the links.
#
# RESIZING-ARRAY IMPLEMENTATION. (FASTER for each operation. But delays upon resizing)
#  * Every operation takes constant AMORTIZED time.
#  * Less wasted space.

# 09:50 "Resizing Arrays" QUESTION: Suppose that, starting from an empty data structure,
# we perform N push operations in our resizing array implementation of a stack.
# How many times is the "resize()" method called?
#
# ANSWER: logarithmic
# EXPLANATION: The "resize()" method is called only when the size of the stack
# is a power of two.


    # 15:49 14 STACK CONSIDERATIONS: ...
    # LOITERING. Holding a reference to an object when it is no longer needed.
    # When we decrement the value N, there is still a pointer to the thing
    # that we took off the stack in that array even though we know are not using it,
    # The Java system does not know that we are no longer using it.
    #
    # LOITERING             AVOID LOITERING
    # -------------------   -------------------------
    # public String pop()   public String pop() {
    # { return s[--N]; }      String item = s[--N];
    #                         s[N] = null;
    #                         return item;
    #                       }
    #                       Garbage collector can reclaim memory only if no outstanding refs.

    # 16:18 QUESTION: Given a reference "first" to the first node of a null-terminated linked
    # list with at least two nodes, what does the code frag,emt below do?
    #
    #   Node x = first;
    #   while (x.next.next != null) {
    #     x = x.next;
    #   }
    #   x.next = null;
    #
    # ANSWER: Deletes the last node in the list
    # EXPLANATION: Upon termination of the loop, x is a reference to the second to last node.
    # The final statement deletes the last node from the list.
# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne.
# Copyright (C) 2014-2016, DV Klopfenstein ported to Python
# Java last updated: Mon Oct 7 11:58:25 EDT 2013.
