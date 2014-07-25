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


import unittest

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


class QuickFindUF_Tests(unittest.TestCase):

  def test_1(self):
    print "\ntest_1"
    o = QuickFindUF(10); print o
    o.union(4,3); print o, "union(4,3)"
    o.union(3,8); print o, "union(3,8)"
    o.union(6,5); print o, "union(6,5)"
    o.union(9,4); print o, "union(9,4)"
    o.union(2,1); print o, "union(2,1)"
    o.union(8,9); print o, "union(8,9)"
    o.union(5,0); print o, "union(5,0)"
    o.union(7,2); print o, "union(7,2)"
    o.union(6,1); print o, "union(6,1)"
    self.failUnless( o.ID == [1,1,1,8,8,1,1,1,8,8] )

  def test_week1_quiz_Q1(self): # seed = 686930
    print "\ntest_week1_quiz_Q1"
    o = QuickFindUF(10); print o
    o.union(6,3); print o, "union(6,3)"
    o.union(6,5); print o, "union(6,5)"
    o.union(9,5); print o, "union(9,5)"
    o.union(7,0); print o, "union(7,0)"
    o.union(3,1); print o, "union(3,1)"
    o.union(9,4); print o, "union(9,4)"
    self.failUnless( o.ID == [0,4,2,4,4,4,4,0,8,4] )

  def test_week1_quiz_Q1b(self): # seed = 686930
    print "\ntest_week1_quiz_Q1b"
    o = QuickFindUF(10); print o
    o.union(4,7); print o, "union(4,7)"
    o.union(7,6); print o, "union(7,6)"
    o.union(9,7); print o, "union(9,7)"
    o.union(6,5); print o, "union(6,5)"
    o.union(8,6); print o, "union(8,6)"
    o.union(2,0); print o, "union(2,0)"
    print 'ANSWER Q1b', o
    self.failUnless( o.ID == [0,1,0,3,5,5,5,5,5,5])

def main():
  unittest.main()

if __name__ == '__main__':
  main()
