#!/usr/bin/env python

#--------------------------------------------------------------------------
# Lecture Week 1 Union-Find: Dynamic Connectivity (10:22)
#--------------------------------------------------------------------------
# 00:55 STEPS TO DEVELOPING A USABLE ALGORITHM:
# * Model the problem. 
# * Find an algorithm to solve it.
# * Fast enough? Fits in memory?
# * If not, figure out why.
# * Find a way to address the problem.
# * Iterate until satidfied. (Find a new algorithm)
# 
# union(4, 3)       0  1--2  3--4 
# union(3, 8)                |  | 
# union(6, 5)       5--6  7  8  9 
# union(4, 4) 
# union(2, 1) 
# connected(0, 7) NO
# connected(8, 9) Yes
# 
# union(5, 0)       0--1--2  3--4
# union(7, 2)       |  |  |  |  |
# union(6, 1)       5--6  7  8  9
# union(1, 0)
# connected(0, 7) Yes

# DYNAMIC CONNECTIVITY APPLICATIONS: (04:50) Week 1 Lecture "Dynamic Connectivity(1:22) 
# * Pixels in a digitial photo
# * Computers in a network.
# * Friends in a social network.
# * Transistors in a computer chip.
# * Elements in a mathematical set.
# * Variable names in Fortran progam.
# * Metallic sites in a composit system.

# 04:51 WHEN PROGRAMMING, CONVENIENT TO NAME OBJECTS 0 TO N-1:
# * Use integers as array index.
# * Suppress details not relevant to union-find.
#   Can use symbol table to translate from site names to integers: 
#   Stay runed (Chapter 3)
# 
# 05:33 MODELING THE CONNECTIONS
# We assume "is connected to" is an equivalence relation:
# * Reflexive:  p is connected to p
# * Symmetric:  If p is connect to q, then q is connected to p.
# * Transitive: If p is connected to q and q is connected to r, then p is connected to r.

# 06:17 CONNECTED COMPONENTS
# Maximal set of objects that are mutually connected.
# 
#   0 1 2-3
#    /  |/|
#   4-5 6 7
# 
# 3 Connected Components: {0} {1 4 5} {2 3 6 7}


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


