#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.QuickUnionUF import *


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

if __name__ == '__main__':
  unittest.main()
   
