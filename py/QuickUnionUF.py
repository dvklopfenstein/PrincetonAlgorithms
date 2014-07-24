#!/usr/bin/env python

# Week 1 "Quick Union(7:50) lecture

# Cost model init union union
# quick-find    N    N    1
# quick-union   N    N    N <- worst case, if tree is tall

# Quick-union defect:  Too slow for huge problems
#   * Union too expensive (N array accesses)
#   * Trees are flat, but too expensive to keep them flat.
# 
# Quick-union defect: 
#   * Trees can get tall.
#   * Find too expensive (could be N array accesses).
# 

# What is the maximum number of array accesses during a find operation when using
# the quick-union stata structure on N elements?
# ANSWER: linear

# Suppose that in a quick-union data structure on 10 elements that the id[] array is
#   0 1 2 3 4 5 6 7 8 9 
#   0 9 6 5 4 2 6 1 0 5
# What are the roots of 2 and 7?
# ANSWER: 6 and 6

import unittest

class QuickUnionUF:
  """ Quick-union [lazy approach].

      Uses a rooted tree.  Each element is in a rooted tree.
      Each item can be assoiciated with a root.
  """
 
  def __init__(self, N):
    """Set if of each object to itself."""
    self.ID = []
    for i in range(N): self.ID.append(i) # N array accesses

  def root(self, i):
    """Chase parent pointers until reach root."""
    while i != self.ID[i]: # depth of i array accesses
      i = self.ID[i] 
    return i

  def connected(self, p, q):
    """Check if p and q have the same root."""
    return self.root(p) == self.root(q) # depth of p & q array accesses

  def union(self, p, q):
    """Change root of p to point to root of q.
       each union involves changing only one array entry
    """
    # Depth of p and q array accesses
    i = self.root(p)
    j = self.root(q)
    print p, q, i, j
    self.ID[i] = j

  def __str__(self):
    """>>> print obj."""
    k = " ".join(str(e) for e in range(len(self.ID)))
    v = " ".join(str(e) for e in self.ID)
    #prt = ['']*len(self.ID)
    #for i in self.ID:
    #  if self.ID[i] == i:
    #    prt[i] = '-'
    #for i,v in enumerate(prt):
    #  print v, i
    return '\n'.join([k,v])

  def __repr__(self):
    """>>> obj."""
    return __str__(self)


class QuickUnionUF_Tests(unittest.TestCase):

  def test_week1_lecture_print(self):
    #  -0
    #  -1
    #  -6
    #  --5
    #  -7
    #  -8
    #  -9
    #  --2
    #  --4
    #  ---3
    print "\ntest_week1_lecture quick-union print 00:51"
    o = QuickUnionUF(10); print o
    o.ID = [0,1,9,4,9,6,6,7,8,9]
    print o.ID

  def test_week1_lecture(self):
    print "\ntest_week1_lecture quick-union"
    o = QuickUnionUF(10); print o
    o.union(4,3); print o, "union(4,3)"
    o.union(3,8); print o, "union(3,8)"
    o.union(6,5); print o, "union(6,5)"
    o.union(9,4); print o, "union(9,4)"
    o.union(2,1); print o, "union(2,1)"
    o.union(8,9); print o, "union(8,9)"
    o.union(5,0); print o, "union(5,0)"
    o.union(7,2); print o, "union(7,2)"
    o.union(6,1); print o, "union(6,1)"
    o.union(7,3); print o, "union(7,3)"
    print o.ID
    self.failUnless( o.ID == [1,8,1,8,3,0,5,1,8,8] )

  def test_week1_exercise_Q2(self):
    print "\ntest_week1_exercise_Q2"
    o = QuickUnionUF(10); print o
    o.union(1,2); print o, "union(1,2)"
    o.union(7,9); print o, "union(7,9)"
    o.union(0,4); print o, "union(0,4)"
    o.union(8,0); print o, "union(8,0)"
    o.union(4,6); print o, "union(4,6)"
    o.union(1,9); print o, "union(1,9)"
    o.union(3,4); print o, "union(3,4)"
    o.union(7,0); print o, "union(7,0)"
    o.union(0,5); print o, "union(0,5)"
    print "ANSWER WEEK 1 Q2:", ' '.join(map(str,o.ID))
    print o.ID
    self.failUnless( o.ID == [4, 2, 9, 6, 6, 5, 5, 9, 4, 6] )

def main():
  unittest.main()
  

if __name__ == '__main__':
  main()
