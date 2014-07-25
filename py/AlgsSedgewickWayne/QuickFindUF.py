#!/usr/bin/env python

# Week 1 Lecture "Quick Find(10:18) 

# Cost model init union find
# quick-find    N    N    1

# Quick-find defect: Union too expensive
# Ex: Takes N^2 accesses to process sequence of N union commands on N objects.
# QUADRATIC ALGORITHMS ARE UNEXCEPTABLY SLOW AND DO NOT SCALE WITH TECHNOLOGY: 08:50
#   * New computer may be 10x as fast 
#   * But, has 10x as much memory =>
#     want to solve a problem that is 10x as big.
#   * With quadratic algorithm, takes 10x as long!!

# The maximum number of ID[] array entries that can change (from one integer to a
# different integer) during one call to union when using the quick-find data
# structure on N elements?
# ANSWER: N - 1

class QuickFindUF:
  """ Quick-find [eager approach].

      Algorithm   init union find
      ---------   ---- ----- ----
      quick-find  N    N     1

      DEFECT: Union too expensive!
      Ex: Takes N^2 array accesses to process sequence of N union commands on N objects.
  """
 
  def __init__(self, N):
    """Set id of each object to itself."""
    self.ID = []
    # N array accesses
    for i in range(N):
      self.ID.append(i)

  def connected(self, p, q):
    """Check whether p and q are in the same component."""
    # 2 array accesses
    return self.ID[p] == self.ID[q]

  def union(self, p, q):
    """Change all entries with id[p] to id[q]."""
    # At most 2N + 2 accesses
    pID = self.ID[p]
    qID = self.ID[q]
    for i in range(len(self.ID)):
      # Mistake many make is to put id[p] instead of pID
      if self.ID[i] == pID:
        self.ID[i] = qID

  def __str__(self):
    """>>> print obj."""
    return " ".join(str(e) for e in self.ID)

  def __repr__(self):
    """>>> obj."""
    return __str__(self)

