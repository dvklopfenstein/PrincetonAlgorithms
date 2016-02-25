"""Weighted Quick Union Algorithm takes steps to avoid tall trees."""

from AlgsSedgewickWayne.BaseComp import BaseComp

class WeightedQuickUnionUF(BaseComp):
  """ UNION FIND: Weighted Quick-union [lazy approach] to avoid tall trees."""

  def __init__(self, N):     # $ = N
    """Initialize union-find data structure w/N objects (0 to N-1)."""
    super(WeightedQuickUnionUF, self).__init__("WeightedQuickUnionUF")
    self.ID = range(N) # Set if of each object to itself.
    # Keep track of SIZE(# objects in tree) of each tree rooted at i
    self.SZ = [1]*N # Needed to determine which tree is smaller/bigger

  def _root(self, i):
    """Chase parent pointers until reach root."""
    d = 0 # Used for informative prints for educational purposes
    while i != self.ID[i]: # depth of i array accesses
      i = self.ID[i]
      d += 1
    return BaseComp.NtRoot(rootnode=i, depth=d)

  def connected(self, p, q): # $ = lg N
    """Return if p and q are in the same connected component (i.e. have the same root)."""
    return self._root(p).rootnode == self._root(q).rootnode # Runs depth of p & q array accesses

  def union(self, p, q):     # $ = lg N
    """Add connection between p and q."""
    # Runs Depth of p and q array accesses...
    p_root = self._root(p).rootnode
    q_root = self._root(q).rootnode
    if p_root == q_root:
      return
    # IMPROVEMENT #1: Modification to Quick-Union to make it weighted: 4:03
    # Balance trees by linking root of smaller tree to root of larger tree
    #   Modified quick-union:
    #     * Link root of smaller tree to root of larger tree.
    #     * Update the SZ[] array.
    #   Each union involves changing only one array entry
    if self.SZ[p_root] < self.SZ[q_root]: # Make ID[p_root] a child of q_root
      self.ID[p_root] = q_root # link root of smaller tree(p_root) to root of larger tree(q_root)
      self.SZ[q_root] += self.SZ[p_root] # Larger tree size increases
    else: # Make ID[q_root] a child of p_root 
      self.ID[q_root] = p_root # link root of smaller tree(q_root) to root of larger tree(p_root)
      self.SZ[p_root] += self.SZ[q_root]

  def __str__(self):
    """Print the size vector as well as the ID vector."""
    return '\n'.join([
        super(WeightedQuickUnionUF, self).__str__(),
        "siz: " + ' '.join('{SZ:>2}'.format(SZ=e) for e in self.SZ)])

# algorithm   init  union  find
# ----------- ----  -----  ----
# quick-find    N     N     1
# quick-union   N     N*    N <- worst case, if tree is tall
# weighted QU   N  lg N  lg N 

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
# We assume "is connected to" is an **equivalence relation**:
# * **Reflexive**:  p is connected to p
# * **Symmetric**:  If p is connect to q, then q is connected to p.
# * **Transitive**: If p is connected to q and q is connected to r, then p is connected to r.

# 06:17 CONNECTED COMPONENTS
# Maximal set of objects that are mutually connected.
#
#   0 1 2-3
#    /  |/|
#   4-5 6 7
#
# 3 Connected Components: {0} {1 4 5} {2 3 6 7}
#
# PROPERTY: Any two objects in the component are connected,
# and there is no object outside that is connected to those objects

# 07:53 Union-find data type (API)
# **Goal:** Design efficient data structure for union-find
#   * Number of objects N can be huge.
#   * Number of operations(e.g. union, connected) M can be huge.
#   * Find queries and union commands may be intermixed.
#
# public class UF
#   UP(int N)                       # init union-find data structure w/N objects(0 to N-1)
#   void union(int p, int q)        # Add connection between p and q
#   boolean connected(int p, int q) # are p and q in the same component

# 10:15 QUESTION: How many connected components result after performing the
# following sequence of union operations on a set of 10 items?
#
#   1-2  3-4  5-6  7-8  2-8  0-5  1-9
#
# ANSWER: 3; { 1 2 7 8 9 }, {3 4}, AND {0 5 6}
#
#      0  1--2  3--4
#      |      \
#      5--6  7--8--9
#


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



###########################################################################
# Lecture Week 1 Quick-Union Improvements (13:02)
###########################################################################
#
# 00:22 IMPROVEMENT 1: WEIGHTING
#
# WEIGHTED QUICK-UNION.
# * Modify quick-union to avoid tall trees.
# * Keep track of size of each tree (number of objects).
# * Balance by linking root of smaller tree to root of larger tree.
#   reasonable alternatives: union by height or "rank"

# 01:21 WEIGHTED QUICK-UNION DEMO
# ------------------------------
#        i   0 1 2 3 4 5 6 7 8 9
#  INI: id[] 0 1 2 3 4 5 6 7 8 9
#
# 0  1  2  3  4  5  6  7  8  9
#
# 03:21 -- union(4, 3) --------
# WAS: id[] 0 1 2 3 4 5 6 7 8 9
# NOW: id[] 0 1 2 4 4 5 6 7 8 9
#           . . . X . . . . . .
#
# 0  1  2     4  5  6  7  8  9
#             |
#             3
#
#
# 01:45 -- union(3, 8) --------
# WAS: id[] 0 1 2 4 4 5 6 7 8 9
# NOW: id[] 0 1 2 4 4 5 6 7 4 9
#           . . . . . . . . X .
#
# 0  1  2     4  5  6  7     9
#            / \
#           3   8
#
#
# 01:58 -- union(6, 5) --------
# WAS: id[] 0 1 2 4 4 5 6 7 4 9
# NOW: id[] 0 1 2 4 4 6 6 7 4 9
#           . . . . . X . . . .
#
# 0  1  2     4     6  7     9
#            / \    |
#           3   8   5
#
# 02:04 -- union(9, 4) --------
# WAS: id[] 0 1 2 4 4 6 6 7 4 9
# NOW: id[] 0 1 2 4 4 6 6 7 4 4
#           . . . . . . . . . X
#
# 0  1  2     4     6  7
#            /|\    |
#           3 8 9   5
#
#
# 02:12 -- union(2, 1) --------
# WAS: id[] 0 1 2 4 4 6 6 7 4 4
# NOW: id[] 0 2 2 4 4 6 6 7 4 4
#           . X . . . . . . . .
#
# 0     2     4     6  7
#       |    /|\    |
#       1   3 8 9   5
#
#
# 02:17 -- union(5, 0) --------
# WAS: id[] 0 1 2 4 4 6 6 7 4 4
# NOW: id[] 6 2 2 4 4 6 6 7 4 4
#           X . . . . . . . . .
#
#       2     4      6  7
#       |    /|\    / \
#       1   3 8 9  0   5
#
#
# 02:29 -- union(7, 2) --------
# WAS: id[] 6 2 2 4 4 6 6 7 4 4
# NOW: id[] 6 2 2 4 4 6 6 2 4 4
#           . . . . . . . X . .
#
#       2     4      6
#      / \   /|\    / \
#     1   7 3 8 9  0   5
#
#
# 02:37 -- union(6, 1) --------
# WAS: id[] 6 2 2 4 4 6 6 2 4 4
# NOW: id[] 6 2 6 4 4 6 6 2 4 4
#           . . X . . . . . . .
#
#       2     4      6
#      / \   /|\    /|\
#     1   7 3 8 9  0 2 5
#                   / \
#                  1   7
#
#
# 02:37 -- union(6, 1) --------
# WAS: id[] 6 2 2 4 4 6 6 2 4 4
# NOW: id[] 6 2 6 4 4 6 6 2 4 4
#           . . X . . . . . . .
#
#      4      6
#     /|\    /|\
#    3 8 9  0 2 5
#            / \
#           1   7
#
# 02:50 -- union(7, 3) --------
# WAS: id[] 6 2 6 4 4 6 6 2 4 4
# NOW: id[] 6 2 6 4 6 6 6 2 4 4
#           . . . . X . . . . .
#
#         +----6
#        /    /|\
#       4    0 2 5
#      /|\    / \
#     3 8 9  1   7


#
## Quick-union defect:
##   * Union too expensive (N array accesses)
##   * Trees are flat, but too expensive to keep them flat.
##
## Quick-union defect:
##   * Trees can get tall.
##   * Find too expensive (could be N array accesses).
##

#--------------------------------------------------------------------------
# 05:28 WEIGHTED QUICK-UNION ANALYSIS
#
# 05:38 RUNNING TIME
# * FIND:  takes time proportional to depth of p and q.
# * UNION: takes constant time, given roots.
#
# 05:45 PROPOSTION: Depth of any node x is at most lg N (lg = log_2(N))
# The cost scales:
#     Ex: N =         1,000 depth is 10
#     Ex: N =     1,000,000 depth is 20
#     Ex: N = 1,000,000,000 depth is 30
#     depth for   10 objects <= lg(10)   = 3.322
#     depth for  100 objects <= lg(100)  = 6.644
#     depth for 1001 objects <= lg(1000) = 9.966
#
# 06:23 PROOF: When does depth of x increase?
#
# Increases by 1 when tree T1 containing x is merged into another tree T2.
#  * The size of the tree containing x at least doubles since |T2| >= |T1|
#  * Size of tree containing x can double at most lg(N) times. Why?
#    When the depth of x increases, the size of its tree size at least doubles

# Cost model init union  union
# quick-find    N    N     1
# quick-union   N    N     N   <- worst case, if tree is tall
# weighter QU   N  lg(N) lg(N) <- includes cost of finding roots

# Q: Stop at guaranteed acceptable performance?
# A: No, easy to improve further.

#--------------------------------------------------------------------------
# 08:26 IMPROVEMENT 2: PATH COMPRESSION
#
# QUICK UNION WITH PATH COMPRESSION.
# Just after computing the root of p, set the id of each examined node to point to that root.
#

# 10:01 WEIGHTED QUICK-UNION WITH PATH COMPRESSION: AMORTIZED ANALYSIS
#
# PROPOSITION: [Hopcroft-Ulman, Tarjan] Starting from an       N  lg*N (iterate log fnc)
# empty data structure, ny sequence of M union-find ops  -------  ----
# on N objects makes <= c(N + M lg* N) array accesses.         1  0
#  * Analysis can be improved to N + M alpha(M, N).            2  1
#  * Simple algorithm with fascinating mathematics.            4  2
#                                                             16  3
#                                                          65536  4
#                                                        2^65536  5
# ITERATIVE LOG FUNCTION:
# log*N function is the number of times you have to take the log of N to get 1.
# REAL WORLD: Think of it as a number less than 5

# 11:23 QUESTION: IS THERE A SIMPLE ALGORITHM THAT IS LINEAR (This one is so close)
# ANSWER: No (Fredman and Sacks)

#--------------------------------------------------------------------------
# 12:31 SUMMARY
# BOTTOM LINE. Weighted quick union (with path compression) makes it
# possible to solve problems that could not otherwise be addressed.
#
# $ M union-find operations on a set of N objects
#
# $ algorithm                       worst-case time
# $ ------------------------------  ---------------------
# $ quick-find                      M * N
# $ quick-union                     M * N
# $ weighted QU                     N + M log N
# $ QU + path compression           N + M log N
# $ weighted QU + path compression  N + M lg*N
#
# EX. [10^9 union and finds with 10^9 objects]
#   * WQUPC reduces time from 30 years to 6 seconds.
#   * Supercomputer won't help much; good algorithm enables solution.


#--------------------------------------------------------------------------
# LECTURE QUESTION:
# Suppose that the id[] array during the weightes quick union algorithm is
#                          __0__    8
#   0 1 2 3 4 5 6 7 8 9   / /|\ \   |\
#   0 0 0 0 0 0 7 8 8 8  1 2 3 4 5  7 9
#                                   |
#                                   6
# ANSWER Which id[] entry changes with union(3,6)?  ID[8]
#
# EXPLANATION: In weighted quick union, we make the root of the smaller tree
# points to the root of the larger tree. In this example, the algorithm sets id[8]=0
#
# Be careful not to confuse union-by-size with union-by-height - the former
# uses the **size** of the tree (number of nodes) while the latter uses
# the **height** of the tree (number of links on longest path from the root
# of the tree to a leaf node). Both variants guarantee logarithmic height.
# There is a third variant known as "union-by-rank" that is also widely used.




###########################################################################
# Lecture Week 1 Union-Find Applications (9:22)
###########################################################################

# UNION-FIND APPLICATIONS: (00:27) Week 1 Lecture "Union-Find Applications" (1:22)
#  * Percolation
#  * Games (Go, Hex)
#  X Dynamic connectivity
#  * Least common ancestor
#  * Equivalence of finite state automata
#  * Hoshen-Kopelman algorithm in physics.
#  * Hinley-Milner polymorphic type inference.
#  * Kruskal's minimum spanning tree algorithm.
#    Graph processing algorithm which uses Union-Find as a sub-routine
#  * Compiling equivalence statements in Fortran.
#  * Morphological attribute openings and closings.
# ** Matlab's bwlabel() function in **image processing.
#    How to label area in images

# 02:13 A MODEL FOR MANY PHYSICAL SYSTEMS:
#  * N-by-N grid of sites.
#  * Each site is open with probability p (or blocked with probability 1-p).
#  * System percolates iff top and bottom are connected by open sites.
#
# model              system     vacant site occupied site percolates
# ------------------ ---------- ----------- ------------- ----------
# electricity        material   conductor   insulated     conducts
# fluid flow         material   empty       blocked       porous
# social interaction population person      empty         communicates
#
# Goes on to describe percolation...

# 08:12 SUBTEXT OF TODAY'S LECTURE (AND THIS COURSE)
#
# STEPS TO DEVELOPING A USABLE ALGORITHM.
#  * Model the problem.
#  * Find an algorithm to solve it.
#  * Fast enough? Fits in memory?
#  * If not, figure out why.
#  * Find a way to address the problem.
#  * Iterate until satisfied.

# 09:15 QUESTION
# When opening one new site in the percolation simulation, how many times is union() called?
# ANSWER: 0, 1, 2, 3, or 4
# EXPLANATION: It is called for each neighboring site that is already open.
# There are 4 possible neighbors, but some of them may not already be open.


###########################################################################
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


#  Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-2016, DV Klopfenstein, Python implementation
