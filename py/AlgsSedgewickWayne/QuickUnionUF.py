"""QuickUnion (union-find) Algorithm."""

from AlgsSedgewickWayne.BaseComp import BaseComp

class QuickUnionUF(BaseComp):
  """Union command is Quick."""

  def __init__(self, N):     # $ = N
    """Set if of each object to itself."""
    super(QuickUnionUF, self).__init__("QuickUnionUF")
    self.ID = range(N) # Runs N array accesses

  def _root(self, i):
    """Chase parent pointers until reach root."""
    while i != self.ID[i]: # Runs the depth of i array accesses
      i = self.ID[i] # Move i up one level of the tree
    return i # Found root: ID[i] == i

  def connected(self, p, q): # $ = N
    """Check if p and q have the same root."""
    return self._root(p) == self._root(q) # Runs the depth of p & q array accesses

  def union(self, p, q): #     $ = N
    """Change root of p to point to root of q: Changes only 1 array entry."""
    p_root = self._root(p)
    q_root = self._root(q)
    self.ID[p_root] = q_root

# 06:58 QUICK-UNION IS ALSO TOO SLOW
#
# COST MODEL. Number of array accesses (fro read or write).
# algorithm   init union find
# quick-find    N    N    1
# quick-union   N    N*   N <- worst case, if tree is tall
#     * Included cost of finding roots

# QUICK-FIND  DEFECT.  Too slow for huge problems
#   * UNION too expensive (N array accesses)
#   * Trees are flat, but too expensive to keep them flat.
#
# QUICK-UNION DEFECT.
#   * Trees can get too tall.
#   * FIND too expensive (could be N array accesses).
#


#  """ Quick-union [lazy approach].
#
#      Uses a rooted tree.  Each element is in a rooted tree.
#      Each item can be assoiciated with a root.
#  """
# --------------------------------------------------------------
# Lecture Week 1 "Quick Union"(7:50)
# --------------------------------------------------------------
# 00:32 QUICK-UNION [Lazy approach; Avoid doing work until we are force to]
# DATA STRUCTURE
# * Integer array id[] of size N.
#   Array represents a set of trees, called a forest.
# * Interpretation: id[i] is parent of i.
# * Root of i is id[id[id[...id[i]...]]].
#   ... => Keep going until id doesn't change (algorithm ensures no cycles)
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 1 9 4 9 6 6 7 8 9
#
# 0 1 9   6 8 8
#    / \  |
#   2   4 5
#       |
#       3
#
# Ex: id[2]=9 -> 9 is parent of 2
# Ex: id[4]=9 -> 9 is parent of 4
# Ex: id[3]=4 -> 4 is parent of 3
# Ex: id[5]=6 -> 6 is parent of 5
#
# Root of 3 is id[id[3]]
#              id[  4  ]
#                   9

# 01:43 QUESTION: Suppose that in a quick-union data structure on 10 elements
# that the id[] array is
#   0 9 6 5 4 2 6 1 0 5
#   0 1 2 3 4 5 6 7 8 9
# What are the roots of 3 and 7?
# ANSWER: 6 and 6
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 9 6 5 4 2 6 1 0 5
#
#  0    4    6
#  |         |
#  8         2
#            |
#            5
#           / \
#          3   9
#              |
#              1
#              |
#              7
#

# 2:42
# FIND. Check if p and q have the same root.
#
# UNION. To merge components containing p and q, set the id of
# p's root to the id of q's root.
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 1 9 4 9 6 6 7 8 9
#
# 0  1  9   6  7  8
#      / \  |
#     2   4 5=q
#         |
#         3=p
#
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 1 9 4 9 6 6 7 8 6
#      . . . . . . . . . X <- Only one value changes
#
# 0  1     6  7  8
#         /|
#        9 5=q
#       / \
#      2   4
#          |
#          3=p
#
# -----------------------------
#        i   0 1 2 3 4 5 6 7 8 9
#  INI: id[] 0 1 2 3 4 5 6 7 8 9
#
# 0  1  2  3  4  5  6  7  8  9
#
#  03:21 -- union(4, 3) --------
#  WAS: id[] 0 1 2 3 4 5 6 7 8 9
#  NOW: id[] 0 1 2 3 3 5 6 7 8 9
#            . . . . X . . . . .
#
# 0  1  2  3     5  6  7  8  9
#          |
#          4
#
#  03:37 -- union(3, 8) --------
#  WAS: id[] 0 1 2 3 3 5 6 7 8 9
#  NOW: id[] 0 1 2 8 3 5 6 7 8 9
#            . . . X . . . . . .
#
# 0  1  2        5  6  7  8  9
#                         |
#                         3
#                         |
#                         4
#
#  03:51 -- union(6, 5) --------
#  WAS: id[] 0 1 2 8 3 5 6 7 8 9
#  NOW: id[] 0 1 2 8 3 5 5 7 8 9
#            . . . . . . X . . .
#
# 0  1  2        5     7  8  9
#                |        |
#                6        3
#                         |
#                         4
#
#  03:55 -- union(9, 4) --------
#  WAS: id[] 0 1 2 8 3 5 5 7 8 9
#  NOW: id[] 0 1 2 8 3 5 5 7 8 8
#            . . . . . . . . . X
#
# 0  1  2        5     7  8
#                |        |\
#                6        3 9
#                         |
#                         4
#
#
#  04:12 -- union(2, 1) --------
#  WAS: id[] 0 1 2 8 3 5 5 7 8 8
#  NOW: id[] 0 1 1 8 3 5 5 7 8 8
#            . . X . . . . . . .
#
# 0  1           5     7  8
#    |           |        |\
#    2           6        3 9
#                         |
#                         4
#
#  04:12 -- union(5, 0) --------
#  WAS: id[] 0 1 1 8 3 5 5 7 8 8
#  NOW: id[] 0 1 1 8 3 0 5 7 8 8
#            . . . . . X . . . .
#
# 0  1                 7  8
# |  |                    |\
# 5  2                    3 9
# |                       |
# 6                       4
#
#
#  04:42 -- union(7, 2) --------
#  WAS: id[] 0 1 1 8 3 0 5 7 8 8
#  NOW: id[] 0 1 1 8 3 0 5 1 8 8
#            . . . . . . . X . .
#
# 0  1                    8
# |  |\                   |\
# 5  2 7                  3 9
# |                       |
# 6                       4
#
#
#  04:48 -- union(6, 1) --------
#  WAS: id[] 0 1 1 8 3 0 5 1 8 8
#  NOW: id[] 1 1 1 8 3 0 5 1 8 8
#            X . . . . . . . . .
#
#   1                    8
#  /|\                   |\
# 0 2 7                  3 9
# |                      |
# 5                      4
# |
# 6
#
#
#
#  05:08 -- union(7, 3) --------
#  WAS: id[] 1 1 1 8 3 0 5 1 8 8
#  NOW: id[] 1 8 1 8 3 0 5 1 8 8
#            . X . . . . . . . .
#
#          -8
#         / |\
#     1--+  3 9
#    /|\    |
#   0 2 7   4
#   |
#   5
#   |
#   6


# 07:43 QUESTION: What is the maximum number of array accesses during a
# find operation when using the quick-union stata structure on N elements?
# ANSWER: linear


#  Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-2016, DV Klopfenstein, Python implementation
