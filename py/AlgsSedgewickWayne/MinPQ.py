# TBD finish Python Port

class MinPQ(object):
  """Priority Queue supporting insert and delete-the-minimum key."""
  private Key[] pq;                    // store items at indices 1 to N
  private int N;                       // number of items on priority queue
  private Comparator<Key> comparator;  // optional comparator

  def __init__(initCapacity=None, **kwargs):
    if initCapacity is None:
      pass
    else:
      self.pq = (Key[]) new Object[initCapacity + 1];
      self.pq = [None for i in range(initCapacity+1)]
      self.N = 0

  # Initializes an empty priority queue with the given initial capacity,
  # using the given comparator.
  public MinPQ(int initCapacity, Comparator<Key> comparator) {
      this.comparator = comparator;
      pq = (Key[]) new Object[initCapacity + 1];
      N = 0;

  # Initializes an empty priority queue using the given comparator.
  public MinPQ(Comparator<Key> comparator) {
      this(1, comparator);

  # Initializes a priority queue from the array of keys.
  #
  # Takes time proportional to the number of keys, using sink-based heap construction.
  public MinPQ(Key[] keys) {
      N = keys.length;
      pq = (Key[]) new Object[keys.length + 1];
      for (int i = 0; i < N; i++)
          pq[i+1] = keys[i];
      for (int k = N/2; k >= 1; k--)
          sink(k);
      assert isMinHeap();

  def isEmpty(self):
    """Returns true if this priority queue is empty."""
    return self.N == 0

  def size(self):
    """Returns the number of keys on this priority queue."""
      return self.N

  def min(self):
    """Returns a smallest key on this priority queue."""
      if (isEmpty()) throw new NoSuchElementException("Priority queue underflow");
      return pq[1];

  def _resize(self, int capacity):
    """helper function to double the size of the heap array."""
    assert capacity > N;
    temp = [None for i in range(capacity)]
    for i, pq_elem in enumerate(self.pq):
      temp[i] = pq_elem
    self.pq = temp

  def insert(self, x):
    """Adds a new key to this priority queue."""
    # double size of array if necessary
    if (self.N == pq.length - 1):
      self._resize(2 * pq.length)

    # add x, and percolate it up to maintain heap invariant
    self.N += 1 
    pq[N] = x
    self._swim(N);
    assert self.isMinHeap();

  /**
   * Removes and returns a smallest key on this priority queue.
   *
   * @return a smallest key on this priority queue
   * @throws NoSuchElementException if this priority queue is empty
   */
  public Key delMin() {
      if (isEmpty()) throw new NoSuchElementException("Priority queue underflow");
      exch(1, N);
      Key min = pq[N--];
      sink(1);
      pq[N+1] = null;         // avoid loitering and help with garbage collection
      if ((N > 0) && (N == (pq.length - 1) / 4)) resize(pq.length  / 2);
      assert isMinHeap();
      return min;
  }


  #**************************************************************************
  # Helper functions to restore the heap invariant.
  #**************************************************************************
  def _swim(self, k):
    while (k > 1 && greater(k/2, k)) {
      exch(k, k/2);
      k = k/2;

  def _sink(self, k):
    while 2*k <= N:
      j = 2*k
      if j < N && greater(j, j+1): j += 1
      if not k > j: 
        break
      self._exch(k, j)
      k = j

  #***************************************************************************
  #* Helper functions for compares and swaps.
  #***************************************************************************
  def _greater(self, i, j):
    if self.comparator is None:
      return ((Comparable<Key>) pq[i]).compareTo(pq[j]) > 0;
    else:
      return comparator.compare(pq[i], pq[j]) > 0;

  def _exch(i, j):
    pq[i], pq[j] = pq[j], pq[i]

  def isMinHeap(self, k=1):
    """is subtree of pq[1..N] rooted at k a min heap?"""
    if k > N: 
      return True
    left = 2*k 
    right = left + 1
    if left  <= N && k > left:  return false;
    if right <= N && k > right: return false;
    return self.isMinHeap(left) && self.isMinHeap(right);


  /**
   * Returns an iterator that iterates over the keys on this priority queue
   * in ascending order.
   * <p>
   * The iterator doesn't implement <tt>remove()</tt> since it's optional.
   *
   * @return an iterator that iterates over the keys in ascending order
   */
  public Iterator<Key> iterator() { return new HeapIterator(); }

  private class HeapIterator implements Iterator<Key> {
      // create a new pq
      private MinPQ<Key> copy;

      // add all items to copy of heap
      // takes linear time since already in heap order so no keys move
      public HeapIterator() {
          if (comparator == null) copy = new MinPQ<Key>(size());
          else                    copy = new MinPQ<Key>(size(), comparator);
          for (int i = 1; i <= N; i++)
              copy.insert(pq[i]);
      }

      public boolean hasNext()  { return !copy.isEmpty();                     }
      public void remove()      { throw new UnsupportedOperationException();  }

      public Key next() {
          if (!hasNext()) throw new NoSuchElementException();
          return copy.delMin();
      }
  }

# Last updated: Sat Sep 26 08:34:31 EDT 2015.
