#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.QuickFindUF import *

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

if __name__ == '__main__':
  unittest.main()
