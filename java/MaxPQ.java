# Algorithms, Part 1 from Princeton University
# by Kevin Wayne, Robert Sedgewick
# https://class.coursera.org/algs4partI-005 retreived July 2014
# Lecture 8 - 2 Binary Heaps (23-36)

# BINARY   TREE: Empty or node with links to left and right binary trees.
# COMPLETE TREE: Pefectly balanced, except for bottom level.

PROPERTY: Height of complete tree with N nodes is [lg N]
PROOF: Height only increases whe N is a pwer of 2

BINARY HEAP: Array representation of a heap-ordered complete binary tree.

HEAP-ORDERED BINARY TREE: (01:44)
* Keys in nodes (associate information with each node)
* Parent's key is no smaller than children's keys

ARRAY REPRESENTATION: (02:06)
* Indices start at 1
* Take nodes in **level** order
* No explicit links needed!


# COMPLETE TREE WITH N=16 NODES (HEIGHT = 4) 00:54

            ______T______
           /             \
        __S__           __R__
       /     \         /     \
      P       N       O       A
     / \     / \     / \     / \
    E   I   H   G   *   *   *   *
   / \ / \ / \ / \ / \ / \ / \ / \ 
  *
 / \

i     0  1  2  3  4  5  6  7  8  9 10 11
a[i]  -  T  S  R  P  N  O  A  E  I  H  G 
a[i]  -  T                              
            S  R                        
            |  +---------+
            +--------    --
                  /  \  /  \
                  P  N  O  A            
                  |  +---------------+
                  +--------------    --
                              /  \  /  \
                              E  I  H  G

PROPOSITION: Largest key is a[1], which is root of binary tree

PROPOSITION: Can use array indices to move through tree. (03:19)
* Parent of node at k is at k/2
* Children of node at k are at 2k and 2k+1

PROMOTION IN A HEAP: (05:15)
Scenario: Child's key becomes larger key than its parents key.
To eliminate the violation:
* Exchange key in child with key in parent
* Repeat until heap order restored.
Peter principle: Node promoted to level of incompetence.

INSERTION IN A HEAP:
Insert: Add node at end, then swim it up.
Cost: At most 1+lg(N) compares


DEMOTION IN A HEAP (07:47):
Scenario: Parent's key becomes smaller than one (or both of its children)
To eliminate the violation:
* Exchange key in parent with key in **larger** child.
* Repeat until heap order restored.
Power struggle: Better subordinate promoted

DELETE THE MAXIMUM IN A HEAP (10:03)
Delete max: Exchange root(max) with node at end, then sink it down.
Cost: At most 2*lg(N) compares


# Binary Heap Implementation
# * Very Simple
# * Optimal representation of data
# * Just a little arithmetic
public class MaxPQ<Key extends Comparable<Key>> # 15:01
{
  private Key[] pq;
  private int N;

  public MaxPQ(int capacity)
  { pq = (Key[]) new Comparable[capacity+1]; }

  /// PQ ops
  public boolean isEmpty()
  { return N == 0; }
  public void insert(Key x) // 06:27
  {
    pq[++N] = x;
    swim(N);
  }
  public Key delMax() // 10:03
  {
    Key max = pq[1];
    # Exchange root(max) with node at end, 
    exch(1, N--);
    # then sink new root down to where it belongs.
    sink(1);
    # Prevent loitering by nulling out max position
    pq[N+1] = null;
    return max;
  }
  
  /// heap helper functions 
  private void swim(int k) // 05:15
  {
    while(k>1 && less(k/2, k))
    {
      exch(k, k/2);
      k = k/2;
    }
  }
  private void sink(int k) // 8:52
  {
    while (2*k <= N)
    {
      int j = 2*k;
      # Check if we are going off the end of the heap and which child is larger
      if (j < N && less(j, j+1)) j++;
      # If k is not less than either child, then we are done
      if (!less(k,j)) break;
      # If k is larger than a child, exchange
      exch(k,j);
      k = j;
    }
  }
  
  /// array helper functions 
  private boolean less(int i, int j)
  { return pq[i].compareTo(pq[j]) < 0; }
  private void exch(int i, int j)
  { Key t = pq[i]; pq[i] = pq[j]; pq[j] = t; }
}

PRIORITY QUEUES IMPLEMENTATION COST SUMMARY
order-of-growth of running time for priority queue with N items
implementation | insert | del max  | max
---------------+--------+----------+------
unordered array|    1   |     N    |   N
ordered array  |    N   |     1    |   1
binary heap    |  log N |  log N   |   1 <==
d'ary heap     |log_d(N)|d*log_d(N)|   1
Fibonacci      |    1   |  log N(*)|   1 *amortized
impossible     |    1   |     1    |   1

Possible improvements(slight possible):
1. d'way might work out better depending on freq on certain del max operations
2. Fibonacci (adv structure).  Too complicated to use in practice

BINARY HEAP CONSIDERATIONS: (18:11)
Immutabililty of keys.
* Assumption: client does not change keys while they're on the PQ.
* Best practice: use immutable keys.
Underflow and overflow (18:50)
* Underflow: throw exception if deleting from empty PQ.
* Overflow: add no-arg constructor and use resizing array.
  resizing array leads to log N amortized time per op (how to make worst case?)
Minimum-oriented priority queue (19:07)
Usually we provide two implementations. Second imp:
* Replace less() with greater()
* Implement greater()
Other operations for the future. (19:17)
Can implement with sink() and swim() [stay tuned]
* Aff the abillity to Remove an arbitrary item.
* Give the Client the ability to Change the priority of an item.

Immutable: String, Integer, Double, Color, Vector, Transaction, Point2D
Mutable: StringBuilder, Stack, Counter, Java array

Immutable Advantages: (22:03)
* Simplfies debugging
* Safer in presence of hostile code
* Simplifies concurren programming
* Safe to use as key in priority queue or symbol table +++++!!!!



