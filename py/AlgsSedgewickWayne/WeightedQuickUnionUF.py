#!/usr/bin/env python

# DYNAMIC CONNECTIVITY APPLICATIONS: (04:50) Week 1 Lecture "Dynamic Connectivity(1:22) 
# * Pixels in a digitial photo
# * Computers in a network.
# * Friends in a social network.
# * Transistors in a computer chip.
# * Elements in a mathematical set.
# * Variable names in Fortran progam.
# * Metallic sites in a composit system.

# UNION-FIND APPLICATIONS: (00:27) Week 1 Lecture "Union-Find Applications" (1:22) 
# * Percolation
# * Games (Go, Hex)
# * Dynamic connectivity
# * Least common ancestor
# * Equivalence of finite state automata
# * Hoshen-Kopelman algorithm in physics.
# * Hinley-Milner polymorphic type inference.
# * Kruskal's minimum spanning tree algorithm.
# * Compiling equivalence statements in Fortran.
# * Morphological attribute openings and closings.
# * Matlab's bwlabel() function in image processing.

# Week 1 Lecture "Quick Union Improvements(13:02) at 4:03

# Cost model init union  union
# quick-find    N    N     1
# quick-union   N    N     N   <- worst case, if tree is tall
# weighter QU   N  lg(N) lg(N) <- includes cost of finding roots
#
## Quick-union defect: 
##   * Union too expensive (N array accesses)
##   * Trees are flat, but too expensive to keep them flat.
## 
## Quick-union defect: 
##   * Trees can get tall.
##   * Find too expensive (could be N array accesses).
## 
# Weighted Quick-union: 
#   * Modify quick-union to avoid tall trees
#   * Find:  takes time proportional to depth of p and q 05:38
#   * Union: takes constant time, given roots.
#
# PROPOSTION: Depth of any node x is at most lg N (lglog_2(N))
# The cost scales:
#     Ex: N =         1,000 depth is 10
#     Ex: N =     1,000,000 depth is 20
#     Ex: N = 1,000,000,000 depth is 30
#     depth for   10 objects <= lg(10)   = 3.322
#     depth for  100 objects <= lg(100)  = 6.644
#     depth for 1001 objects <= lg(1000) = 9.966
# PROOF: When does depth of x increase?
# Increases by 1 when tree T1 containing x is merged into another tree T2.
#  * The size of the tree containing x at least doubles since |T2| >= |T1|
#  * Size of tree containing x can double at most lg(N) times. Why?
#    When the depth of x increases, the size of its tree size at least doubles
# 
#--------------------------------------------------------------------------
# LECTURE QUESTION:
# Suppose that the id[] array during the weightes quick union algorithm is
#                          __0__    8
#   0 1 2 3 4 5 6 7 8 9   / /|\ \   |\ 
#   0 0 0 0 0 0 7 8 8 8  1 2 3 4 5  7 9
#                                   |
#                                   6
# ANSWER Which id[] entry changes with union(3,6)?  ID[8]

#--------------------------------------------------------------------------
# Question 3
# Which of the followint id[] arrays(s) could be thr result of running 
# the weightes quick union algorithm on a set of 10 items? Check all that apply
#    >>> print set([5,5,5,2,5,5,9,9,7,5]) set([9, 2, 5, 7])
#    YES: 2-3 5-0 0-2 9-6 7-8 6-7 4-5 7-4 5-1
#
#    >>> print set([8,9,7,9,9,9,9,8,9,2]) set([8, 9, 2, 7])
#    NO:  The id[] array contains a cycle: 2->7->8->9->2
#
#                   0,1,2,3,4,5,6,7,8,9
#    >>> print set([6,4,8,6,4,6,4,9,6,6]) set([8, 9, 4, 6])
#    NO: Size(10) of tree rooted at parent of 6 < twice(16) the size(8) of tree rooted at 6
#          4
#         / \
#        1 __6__
#         / /|\ \
#        0 3 5 8 9
#              | |
#              2 7
#
#    >>> print set([0,4,4,3,4,5,4,7,8,9]) set([0, 3, 4, 5, 7, 8, 9])
#    YES: 4-6 2-6 1-4
#
#    >>> print set([2,7,1,3,8,1,3,7,1,0]) set([0, 1, 2, 3, 7, 8])
#    NO:  Height of forest = 4 > lg N = lg(10)


import unittest
import numpy as np

class WeightedQuickUnionUF:
  """ UNION FIND: Modified Quick-union [lazy approach] to avoid tall trees.

      Uses a rooted tree.  Each element is in a rooted tree.
      Each item can be assoiciated with a root.
  """
 
  def __init__(self, N):
    self.cnt = N
    """Set if of each object to itself."""
    self.ID = np.arange(N, dtype=np.int32)
    # Keep track of size of each tree (number of objects)
    # Each entry contains a count of objects in the tree rooted at i.
    self.SZ = np.ones(N,dtype=np.int32) # Needed to determine  which tree is smaller and bigger

  def count(self): return self.cnt

  def root(self, i):
    """Chase parent pointers until reach root."""
    d = 0
    while i != self.ID[i]: # depth of i array accesses
      # IMPROVEMENT #2: Path compression. Keeps tree almost completely flat. 8:08..10:21
      # Make every path on that path point to the root.         N  lg*N
      # PROPOSITION: [Hopcroft-Ulman, Tarjan] Starting from an  1     0
      # empty data structure, any sequence of M union-find ops  2     1
      # on N objects makes <= c(N + M*lg(N) array accesses.     4     2
      #   * Analysis can be improved to N + M*alpha(M,N)       16     3
      #   * Simple algorithm with fascinating mathematics.  65536     4
      #self.ID[i] = self.ID[self.ID[i]]                  # 2^65536     5
      i = self.ID[i] 
      d += 1
    return i, d

  def connected(self, p, q):
    """Check if p and q have the same root."""
    return self.root(p)[0] == self.root(q)[0] # depth of p & q array accesses

  def union(self, p, q):
    """Link root of smaller tree to root of larger tree.
       each union involves changing only one array entry
    """
    # Depth of p and q array accesses
    i = self.root(p)[0]
    j = self.root(q)[0]
    if i ==  j:  return
    # IMPROVEMENT #1: Modification to Quick-Union to make it weights: 4:03
    # Balance trees by linking root of smaller tree to root of larger tree
    if   self.SZ[i] < self.SZ[j]: 
      self.ID[i] = j 
      self.SZ[j] += self.SZ[i]
    else: 
      self.ID[j] = i 
      self.SZ[i] += self.SZ[j]

  def __str__(self):
    """>>> print obj."""
    h  = " ".join('%3s'%str(e) for e in range(len(self.ID)))+" header" # Header
    s  = " ".join('%3s'%str(e) for e in self.SZ)+" size"     # Size
    rv = [self.root(e)[0] for e in self.ID]     # Root Values
    #roots = set(rv)
    rv = " ".join(['%3s'%str(e) for e in rv])+" root"     # Root Values
    return '\n'.join([h,rv,s])

  def __repr__(self):
    """>>> obj."""
    return __str__(self)


class WeightedQuickUnionUF_Tests(unittest.TestCase):

  def test_week1_lecture(self): # Lecture: Quick-Union Improvements 1:22
    print """test_week1_lecture quick-union.
       _____6
      /    /|\ 
     4    0 2 5
    /|\    / \ 
   3 8 9  1   7
    """
    o = WeightedQuickUnionUF(10); print o
    o.union(4,3); print o, "weighted union(4,3)", "\n"
    o.union(3,8); print o, "weighted union(3,8)", "\n"
    o.union(6,5); print o, "weighted union(6,5)", "\n"
    o.union(9,4); print o, "weighted union(9,4)", "\n"
    o.union(2,1); print o, "weighted union(2,1)", "\n"
    o.union(5,0); print o, "weighted union(5,0)", "\n"
    o.union(7,2); print o, "weighted union(7,2)", "\n"
    o.union(6,1); print o, "weighted union(6,1)", "\n"
    o.union(7,3); print o, "weighted union(7,3)", "\n"
    self.failUnless( np.array_equal(o.ID, [6,2,6,4,6,6,6,2,4,4] ))


  def test_week1_exercise_Q2(self):
    print """test_week1_exercise_Q2"
      The correct answer is: 0 0 1 0 0 0 0 1 0 7
      
      Here is the id[] array after each union operation:
      
            0 1 2 3 4 5 6 7 8 9 
      1-2:  0 1 1 3 4 5 6 7 8 9 
      7-9:  0 1 1 3 4 5 6 7 8 7 
      0-4:  0 1 1 3 0 5 6 7 8 7 
      8-0:  0 1 1 3 0 5 6 7 0 7 
      4-6:  0 1 1 3 0 5 0 7 0 7 
      1-9:  0 1 1 3 0 5 0 1 0 7 
      3-4:  0 1 1 0 0 5 0 1 0 7 
      7-0:  0 0 1 0 0 5 0 1 0 7 
      0-5:  0 0 1 0 0 0 0 1 0 7 
    """
    o = WeightedQuickUnionUF(10); print o
    o.union(1,2); print o, "weighted union(1,2)"
    o.union(7,9); print o, "weighted union(7,9)"
    o.union(0,4); print o, "weighted union(0,4)"
    o.union(8,0); print o, "weighted union(8,0)"
    o.union(4,6); print o, "weighted union(4,6)"
    o.union(1,9); print o, "weighted union(1,9)"
    o.union(3,4); print o, "weighted union(3,4)"
    o.union(7,0); print o, "weighted union(7,0)"
    o.union(0,5); print o, "weighted union(0,5)"
    print "ANSWER WEEK 1 Q2:", ' '.join(map(str,o.ID))
    self.failUnless( np.array_equal( o.ID, [0, 0, 1, 0, 0, 0, 0, 1, 0, 7] )) # Wrong Answer

  def test_week1_exercise_Q2b(self):
    print """test_week1_exercise_Q2b"""
    o = WeightedQuickUnionUF(10); print o
    o.union(0,4); print o, "weighted union(0,4)"
    o.union(7,3); print o, "weighted union(7,3)"
    o.union(9,1); print o, "weighted union(9,1)"
    o.union(5,0); print o, "weighted union(5,0)"
    o.union(8,6); print o, "weighted union(8,6)"
    o.union(8,3); print o, "weighted union(8,3)"
    o.union(8,2); print o, "weighted union(8,2)"
    o.union(9,0); print o, "weighted union(9,0)"
    o.union(3,1); print o, "weighted union(3,1)"
    print "ANSWER WEEK 1 Q2b:", ' '.join(map(str,o.ID))
    #self.failUnless( np.array_equal( o.ID, [0, 0, 1, 0, 0, 0, 0, 1, 0, 7] )) # Wrong Answer

if __name__ == '__main__':
  unittest.main()
